#!/usr/bin/env python3
"""Validate Microsoft Sentinel scheduled analytics-rule examples."""

from __future__ import annotations

import re
import sys
import uuid
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
RULE_ROOT = ROOT / "analytics-rules"
REQUIRED = (
    "id", "name", "description", "severity", "status", "requiredDataConnectors",
    "queryFrequency", "queryPeriod", "triggerOperator", "triggerThreshold", "tactics",
    "relevantTechniques", "query", "entityMappings", "customDetails",
    "eventGroupingSettings", "incidentConfiguration", "version", "kind",
)


def duration(value: object) -> int | None:
    match = re.fullmatch(r"(\d+)([mhd])", str(value))
    if not match:
        return None
    return int(match.group(1)) * {"m": 1, "h": 60, "d": 1440}[match.group(2)]


def final_output(query: str) -> str:
    projects = list(re.finditer(r"(?ms)^\s*\|\s*project\s+(.+?)(?=^\s*\||\Z)", query))
    return projects[-1].group(1) if projects else query


def main() -> int:
    errors: list[str] = []
    ids: dict[str, Path] = {}
    rules = sorted(RULE_ROOT.rglob("*.yaml"))
    if not rules:
        errors.append("analytics-rules: no rule YAML files found")
    for path in rules:
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        if "REPLACE-WITH" in text or "T0000" in text:
            errors.append(f"{rel}: unresolved placeholder")
        try:
            rule = yaml.safe_load(text)
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: invalid YAML: {exc}")
            continue
        for field in REQUIRED:
            if field not in rule:
                errors.append(f"{rel}: missing required field '{field}'")
        rule_id = str(rule.get("id", ""))
        try:
            uuid.UUID(rule_id)
        except ValueError:
            errors.append(f"{rel}: id is not a valid GUID")
        if rule_id in ids:
            errors.append(f"{rel}: duplicate id also used by {ids[rule_id].relative_to(ROOT)}")
        ids[rule_id] = path
        query = str(rule.get("query", ""))
        output = final_output(query)
        if not re.search(r"\bTimeGenerated\b", output):
            errors.append(f"{rel}: final query output must include TimeGenerated")
        referenced: list[tuple[str, object]] = []
        for mapping in rule.get("entityMappings", []):
            for field in mapping.get("fieldMappings", []):
                referenced.append(("entity mapping", field.get("columnName")))
        referenced.extend(("custom detail", value) for value in rule.get("customDetails", {}).values())
        override = " ".join(str(v) for v in rule.get("alertDetailsOverride", {}).values())
        referenced.extend(("alert placeholder", value) for value in re.findall(r"\{\{\s*(\w+)\s*\}\}", override))
        for kind, column in referenced:
            if column and not re.search(rf"\b{re.escape(str(column))}\b", output):
                errors.append(f"{rel}: {kind} column '{column}' is not in the final output")
        frequency, period = duration(rule.get("queryFrequency")), duration(rule.get("queryPeriod"))
        if frequency is None or period is None:
            errors.append(f"{rel}: schedule must use m, h, or d duration syntax")
        elif frequency > period:
            errors.append(f"{rel}: queryFrequency must not exceed queryPeriod")
    for fixture in sorted((ROOT / "tests" / "fixtures").glob("*.test.kql")):
        content = fixture.read_text(encoding="utf-8")
        if "datatable(" not in content or "TestPassed" not in content:
            errors.append(f"{fixture.relative_to(ROOT)}: fixture requires datatable() and TestPassed")
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"Validated {len(rules)} analytics rules.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
