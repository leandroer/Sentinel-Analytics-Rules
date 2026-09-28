# Contributing and Maintainer Workflow

The repository is not currently accepting unsolicited contributions. This guide documents the maintainer's quality standard.

Every rule must include a stable GUID, semantic version, required connectors, schedule, severity, MITRE mapping where applicable, `TimeGenerated` in the final result, mapped entities, visible custom details, alert grouping, incident configuration, false-positive guidance, and response guidance.

## Workflow

1. Develop and test the KQL in a non-production Sentinel workspace.
2. Exercise positive, negative, and boundary cases.
3. Add or update a self-contained fixture when practical.
4. Run `python3 scripts/validate_rules.py`.
5. Regenerate the catalog with `python3 scripts/generate_catalog.py`.
6. Record schema assumptions and test evidence in the pull request.

Increment the rule version when logic, tables, thresholds, mappings, schedule, or incident behavior changes. Never commit credentials, tenant identifiers, personal data, real incident evidence, or unredacted prompts and responses.
