---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# QA Templates Dependency Matrix

## Critical Path Dependencies

```
QA-001 QA Strategy
    │
    ├──► QA-002 Testing Vision
    │        │
    │        └──► QA-003 Quality Objectives
    │
    ├──► QA-004 Testing Requirements
    │        │
    │        └──► QA-008 Test Strategy
    │                  │
    │                  ├──► QA-009 Test Plan
    │                  │        │
    │                  │        └──► QA-010 Test Cases
    │                  │                  │
    │                  │                  └──► QA-022 Test Execution
    │                  │
    │                  └──► QA-011 Automation Strategy
    │                            │
    │                            └──► QA-018 Automation Code
    │
    └──► QA-005 Metrics Definition
             │
             └──► QA-025 Metrics Report
                      │
                      └──► QA-060 Retrospective
```

## Phase Dependencies

| Phase | Depends On | Enables |
|-------|------------|---------|
| 1 | Business Strategy | 2, 3, 4 |
| 2 | 1 | 3, 4, 5 |
| 3 | 1, 2 | 4, 5, 6 |
| 4 | 2, 3 | 5, 6 |
| 5 | 3, 4 | 6, 8 |
| 6 | 5 | 7, 8, 16 |
| 7 | 5, 6 | 8 |
| 8 | 6, 7 | 9 |
| 9-16 | 8 | Continuous |
| 17-23 | All prior | Governance |

## Key Integration Points

### Development Integration
- QA-008 ↔ Development methodology
- QA-011 ↔ CI/CD pipeline
- QA-018 ↔ Code repository

### Business Integration
- QA-030-032 ↔ Business stakeholders (UAT)
- QA-052-055 ↔ Management reporting
- QA-033 ↔ Release management
