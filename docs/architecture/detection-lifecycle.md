# Detection Lifecycle

```mermaid
flowchart LR
    H["Hunt"] --> V["Validate"]
    V --> T["Tune"]
    T --> R["Rule"]
    R --> L["Lab deployment"]
    L --> M["Measure"]
    M --> I["Improve"]
    I --> T
```

A detection is mature only when its telemetry assumptions, expected positives, expected benign activity, alert behavior, response ownership, and known blind spots are documented and periodically reviewed.
