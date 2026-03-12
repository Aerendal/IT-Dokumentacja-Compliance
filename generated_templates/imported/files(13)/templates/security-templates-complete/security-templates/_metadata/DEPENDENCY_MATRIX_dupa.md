---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Security Templates Dependency Matrix

## Critical Path Dependencies

```
SEC-001 Vision
    │
    ├──► SEC-002 Strategy
    │        │
    │        ├──► SEC-006 Framework Selection
    │        │
    │        └──► SEC-016 Roadmap
    │
    ├──► SEC-003 Threat Landscape
    │        │
    │        └──► SEC-007 Risk Assessment
    │                  │
    │                  └──► SEC-010 Threat Model
    │
    └──► SEC-004 Requirements
             │
             ├──► SEC-008 Security Architecture
             │        │
             │        ├──► SEC-009 Zero Trust Design
             │        ├──► SEC-013 Network Security
             │        └──► SEC-014 IAM Design
             │
             └──► SEC-020-024 Implementation
                      │
                      └──► SEC-025-029 Testing
                               │
                               └──► SEC-034-036 Deployment
                                        │
                                        └──► SEC-037-041 Operations
```

## Phase Dependencies

| Phase | Depends On | Enables |
|-------|------------|---------|
| 1 | Business Strategy | 2, 3, 4 |
| 2 | 1 | 3, 4, 5 |
| 3 | 1, 2 | 4, 5, 6 |
| 4 | 1, 2, 3 | 5, 6, 7 |
| 5 | 3, 4 | 6, 7, 8 |
| 6 | 5 | 7, 8 |
| 7 | 5, 6 | 8, 19 |
| 8 | 6, 7 | 9, 10, 11 |
| 9-16 | 8 | Continuous |
| 17-23 | All prior | Governance |
