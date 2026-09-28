# Coverage Matrix

| Domain | Rules | Principal telemetry | Primary coverage |
|---|---:|---|---|
| AI security | 5 | `AIApp_CL` | Prompt manipulation, sensitive output, resource consumption, safety controls |
| Agent 365 | 5 | `AIToolExecution_CL` | Tool authorization, privilege, volume, connector novelty, data movement |
| Identity | 5 | `SigninLogs`, `AuditLogs` | Credential attacks, MFA abuse, roles, consent, emergency access |
| Purview | 5 | `OfficeActivity`, `AIApp_CL` | Collection, sharing, labels, mass access, AI/data correlation |
| Cloud | 5 | `AzureActivity`, `AzureDiagnostics` | Destruction, secrets, monitoring, exposure, network controls |
| Endpoint | 5 | `DeviceProcessEvents` | Scripting, LOLBins, child processes, credentials, persistence |
| UEBA | 5 | `BehaviorAnalytics`, `IdentityInfo`, `AuditLogs` | Privilege, novelty, service identities, context deviations, correlation |

The generated [rule catalog](rule-catalog.md) lists the exact ATT&CK techniques, entities, tables, severity, and version for each rule. Blank or omitted framework mappings are intentional where no defensible Enterprise ATT&CK technique is asserted.

Coverage breadth does not prove detection quality. Each rule remains an example until tenant schemas, expected positives, benign activity, alert behavior, and response ownership are validated.
