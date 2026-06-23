# Sentinel Analytics Rules

Professional Microsoft Sentinel analytics rule library for Identity, Microsoft Purview, AI Security, Microsoft Agent 365, and SOC operations.

## Purpose

This repository provides production-minded Sentinel analytics rule examples with:

- KQL detection logic
- YAML rule structure
- MITRE ATT&CK mapping
- required data connectors
- false-positive guidance
- tuning guidance
- response recommendations

## Repository Structure

```text
.
├── analytics/
│   ├── Identity/
│   ├── Purview/
│   ├── AI-Security/
│   └── Agent-365/
└── docs/
```

## Rule Quality Standard

Each rule should include:

- clear rule name
- severity
- query frequency
- query period
- MITRE tactic and technique
- data connector requirements
- entity mappings
- incident response guidance

## Disclaimer

Validate and tune all rules before production deployment.
