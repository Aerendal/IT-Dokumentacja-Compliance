---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# QA-006: Acceptance Criteria

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | QA-006 |
| **Version** | 1.0 |
| **Owner** | Product Owner / QA Lead |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Story definition | Backlog refinement |
| **Active** | Sprint duration | Development |
| **Review** | Sprint planning | Story changes |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| User Stories | AC source |
### Downstream
| Document | Relationship |
|----------|--------------|
| QA-010 Test Cases | Test design |
| QA-032 UAT | UAT criteria |

---

## 1. ACCEPTANCE CRITERIA FORMAT
**Given** [precondition]
**When** [action]
**Then** [expected result]

## 2. EXAMPLE CRITERIA
| ID | Given | When | Then |
|----|-------|------|------|
| AC-001 | User logged in | Clicks dashboard | Loads <2s |
| AC-002 | On dashboard | Exports report | CSV downloads |

## 3. DEFINITION OF DONE
- [ ] All AC pass
- [ ] Unit tests pass (>80% coverage)
- [ ] Code reviewed
- [ ] No P1/P2 defects
- [ ] Documentation updated

---

## APPROVAL & SIGN-OFF
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Owner | | | |
| QA Lead | | | |
