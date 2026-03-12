---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# QA-024: Test Coverage Report

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | QA-024 |
| **Version** | 1.0 |
| **Owner** | QA Lead |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| QA-004 Testing Requirements | Requirements |
### Downstream
| Document | Relationship |
|----------|--------------|
| QA-057 Quality Status | Reporting |

---

## 1. COVERAGE SUMMARY
| Type | Total | Covered | Coverage |
|------|-------|---------|----------|
| Requirements | 50 | 48 | 96% |
| Test Cases | 150 | 145 | 97% |
| Code (Unit) | 100% | 82% | 82% |
| Code (Branch) | 100% | 75% | 75% |

## 2. REQUIREMENT COVERAGE
| Req ID | Title | Test Cases | Status |
|--------|-------|------------|--------|
| REQ-001 | Login | TC-001, TC-002 | Covered |
| REQ-002 | Dashboard | TC-010-015 | Covered |
| REQ-003 | Reports | - | Not Covered |

## 3. COVERAGE GAP ANALYSIS
| Gap | Risk | Plan |
|-----|------|------|
| REQ-003 not covered | Medium | Add TCs Sprint 5 |

## 4. COVERAGE TREND
```
100%│         ●
 90%│     ●       ●
 80%│ ●
    └────────────────
     S1  S2  S3  S4
```

---

## APPROVAL & SIGN-OFF
| Role | Name | Signature | Date |
|------|------|-----------|------|
| QA Lead | | | |
