# Purview Audit Assumptions

The Purview rules use `OfficeActivity` for SharePoint and OneDrive operations. Sensitivity-label fields are not guaranteed to have the same names or availability in every tenant, connector, workload, or event type.

Before deploying label-aware rules:

1. Inspect representative audit events for the target operations.
2. Confirm whether labels are direct columns, nested properties, or available through another Purview source.
3. Replace `SensitivityLabel` and `OldSensitivityLabel` with authoritative tenant fields.
4. Test labeled, unlabeled, downgraded, unchanged, internal-sharing, and external-sharing events.
5. Verify that a missing field cannot silently turn the rule into a permanent zero-result query.

The AI-assisted exfiltration rule correlates temporal proximity between AI and file activity. It does not establish that AI caused the file operation or that exfiltration occurred; analysts must validate intent, data sensitivity, destination, and business context.
