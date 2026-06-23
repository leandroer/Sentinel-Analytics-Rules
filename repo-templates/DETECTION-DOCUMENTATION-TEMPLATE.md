# Detection Name

## Summary

Briefly describe the behavior being detected.

## Threat Scenario

Explain the attack, misuse, or suspicious behavior.

## Required Data Sources

- Table/log source 1
- Table/log source 2

## Detection Logic

```kql
// Query goes here
```

## Expected Output

| Field | Description |
|---|---|
| TimeGenerated | Event time |
| UserPrincipalName | User involved |
| SourceIP | Source IP address |
| DetectionName | Detection title |
| Severity | Detection severity |

## False Positives

- Legitimate admin activity
- Vulnerability scanners
- Automation jobs
- Business-approved testing

## Tuning Guidance

- Adjust thresholds based on baseline.
- Add approved admin accounts.
- Exclude known scanners.
- Restrict to critical assets if needed.

## Response Guidance

1. Validate the entity.
2. Review recent activity.
3. Correlate with identity, endpoint, cloud, and data logs.
4. Contain if malicious.
5. Document incident findings.

## MITRE ATT&CK Mapping

| Tactic | Technique |
|---|---|
| Initial Access | Example |
