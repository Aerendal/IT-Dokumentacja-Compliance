---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# QA-026: Test Result Analysis

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | QA-026 |
| **Version** | 1.0 |
| **Owner** | QA Lead |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| QA-022 Test Execution | Test results |
### Downstream
| Document | Relationship |
|----------|--------------|
| QA-068 Retrospective | Process improvement |

---

## 1. ANALYSIS SUMMARY
| Category | Findings |
|----------|----------|
| Total Failures | [X] |
| True Defects | [X] |
| Test Issues | [X] |
| Environment | [X] |
| Data Issues | [X] |

## 2. FAILURE ROOT CAUSE
| Cause | Count | % | Action |
|-------|-------|---|--------|
| Code defect | 8 | 53% | Fix bugs |
| Test script | 3 | 20% | Update tests |
| Test data | 2 | 13% | Refresh data |
| Environment | 2 | 13% | Stabilize env |

## 3. DEFECT DISTRIBUTION
| Module | Defects | Severity |
|--------|---------|----------|
| Login | 2 | 1 High, 1 Med |
| Dashboard | 3 | 2 Med, 1 Low |
| Reports | 1 | 1 Low |

## 4. RECOMMENDATIONS
1. Prioritize Login module fixes
2. Stabilize test environment
3. Improve test data management

---

## APPROVAL & SIGN-OFF
| Role | Name | Signature | Date |
|------|------|-----------|------|
| QA Lead | | | |
