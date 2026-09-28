# Coverage Matrix

| Rule | Identity | Endpoint | Cloud | Data | AI/Agent | Framework |
|---|---:|---:|---:|---:|---:|---|
| Password spray | ✓ |  |  |  |  | ATT&CK T1110.003 |
| Suspicious PowerShell | ✓ | ✓ |  |  |  | ATT&CK T1059.001 |
| Azure resource deletion | ✓ |  | ✓ |  |  | ATT&CK T1485 |
| AI and mass file activity | ✓ |  | ✓ | ✓ | ✓ | ATT&CK T1530 |
| Prompt-injection indicators | ✓ |  |  |  | ✓ | OWASP LLM01 |
| Unauthorized agent tool use | ✓ |  | ✓ | ✓ | ✓ | ATT&CK T1059; agent-risk context |
| Privileged-identity anomaly | ✓ |  | ✓ |  |  | ATT&CK T1078 |

Blank cells are intentional visibility gaps rather than claims of complete coverage. Future rules should be chosen to close meaningful data-source and behavioral gaps, not merely increase rule count.
