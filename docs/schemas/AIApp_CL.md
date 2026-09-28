# `AIApp_CL` Contract

`AIApp_CL` is a repository-defined custom table, not a built-in Sentinel table.

Required fields:

| Column | Type | Purpose |
|---|---|---|
| `TimeGenerated` | `datetime` | Event time |
| `UserPrincipalName_s` | `string` | User or workload identity |
| `SourceIP_s` | `string` | Source address |
| `SessionId_s` | `string` | AI session |
| `Application_s` | `string` | AI application |
| `Prompt_s` | `string` | Submitted prompt |

Prompts can contain credentials, personal information, or proprietary data. Minimize collection, redact secrets, restrict access, and document retention before ingestion. Normalize DCR-created columns without legacy suffixes at ingestion or with a parser.
