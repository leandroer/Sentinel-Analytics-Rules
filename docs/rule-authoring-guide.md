# Analytics Rule Authoring Guide

## Lifecycle

1. Define the adversary behavior and required telemetry.
2. Write a broad hunting query.
3. Validate against 7–30 days of representative data.
4. Test positive, negative, and threshold-boundary cases.
5. Tune exclusions and preserve known coverage gaps.
6. Map entities, custom details, and dynamic alert text.
7. Configure alert and incident grouping deliberately.
8. Deploy disabled or into a lab workspace.
9. Measure precision, volume, and investigation value.
10. Version and review the rule periodically.

## Requirements

- Filter time early and return `TimeGenerated` in the final output.
- Project every entity, custom-detail, and alert-template field.
- Bound `make_set()` and similar aggregations.
- Keep `queryFrequency` less than or equal to `queryPeriod`.
- Document connector and custom-schema assumptions.
- Do not force an Enterprise ATT&CK mapping when no defensible mapping exists.
- Treat keyword matches and UEBA scores as context rather than proof.
- Use stable GUIDs and semantic versions.

## Validation status

Rules are examples until evidence supports promotion to Lab Tested or Production Validated. Static YAML validation is necessary but does not compile KQL or prove tenant schema compatibility.
