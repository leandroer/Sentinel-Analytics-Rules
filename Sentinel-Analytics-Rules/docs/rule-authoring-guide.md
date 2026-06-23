# Sentinel Analytics Rule Authoring Guide

## Recommended Rule Development Lifecycle

1. Write hunting query.
2. Test against 7-30 days of data.
3. Identify false positives.
4. Add thresholds and allowlists.
5. Add entity mappings.
6. Add MITRE ATT&CK mapping.
7. Add response guidance.
8. Deploy as scheduled analytics rule.
9. Review alert volume after deployment.

## KQL Best Practices

- Filter by time early.
- Use `project` before joins.
- Use `make_set(Column, 50)` with explicit max size.
- Use `let` statements for readability.
- Avoid overly broad matching.
- Build thresholds from baseline behavior.
