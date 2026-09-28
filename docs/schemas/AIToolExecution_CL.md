# `AIToolExecution_CL` Contract

`AIToolExecution_CL` is a repository-defined custom table for agent, connector, plugin, and function execution.

Required fields:

| Column | Type | Purpose |
|---|---|---|
| `TimeGenerated` | `datetime` | Execution time |
| `UserPrincipalName_s` | `string` | Requesting identity |
| `SourceIP_s` | `string` | Source address |
| `AgentId_s` | `string` | Agent identifier |
| `ToolName_s` | `string` | Tool or connector |
| `Result_s` | `string` | Execution result |
| `RiskLevel_s` | `string` | Environment-defined risk |
| `ApprovalStatus_s` | `string` | Approval state |

Do not ingest secrets, full tokens, authorization headers, or unredacted sensitive parameters. Preserve correlation from session through approval, execution, and result.
