# Deployment Guidance

The YAML files are source-controlled analytics-rule examples, not a guarantee of one-click tenant deployment.

## Recommended process

1. Review the rule and its custom-schema dependencies.
2. Confirm that required tables contain recent representative data.
3. Run the KQL in Microsoft Sentinel Logs and resolve schema differences.
4. Create the rule disabled or in a non-production workspace.
5. Verify entities, custom details, dynamic text, alert grouping, and incident grouping.
6. Run controlled positive and negative scenarios.
7. Record evidence before enabling production incident creation.

For repeatable deployment, translate validated rules into an approved ARM, Bicep, or Microsoft Sentinel solution packaging workflow. Keep tenant IDs, workspace IDs, credentials, and environment-specific exclusions outside this public repository.

Do not use force-push bootstrap scripts or long-lived Azure credentials. Use protected environments and workload identity federation when deployment automation is introduced.
