---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-035: Cutover Procedure

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-035 |
| **Version** | 1.0 |
| **Owner** | [Migration Lead] |

---

## 1. Cutover Timeline

| Time | Action | Owner |
|------|--------|-------|
| T-24h | Final sync | Data Team |
| T-4h | Freeze changes | All Teams |
| T-2h | Pre-checks | Platform Team |
| T-0 | DNS switch | Network Team |
| T+1h | Validation | QA Team |
| T+4h | All clear | Migration Lead |

---

## 2. Go/No-Go Criteria

| Criteria | Status |
|----------|--------|
| Data sync complete | [ ] |
| Health checks pass | [ ] |
| Rollback tested | [ ] |
| Team availability | [ ] |

---

## 3. Rollback Trigger

- Error rate > 5%
- Response time > 2x baseline
- Critical functionality failure

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial cutover procedure |
