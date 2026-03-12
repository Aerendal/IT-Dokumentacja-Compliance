---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-036: Rollback Plan

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-036 |
| **Version** | 1.0 |
| **Owner** | [Migration Lead] |

---

## 1. Rollback Decision

| Condition | Decision |
|-----------|----------|
| Error rate > 5% for 15 min | Rollback |
| Data corruption detected | Rollback |
| Critical feature failure | Rollback |
| Performance degradation | Evaluate |

---

## 2. Rollback Steps

1. **Decision** - Migration Lead declares rollback
2. **Communication** - Notify all stakeholders
3. **DNS Revert** - Switch DNS back to on-premise
4. **Data Sync** - Sync delta data if needed
5. **Validation** - Verify on-premise functionality
6. **Post-mortem** - Document issues

---

## 3. Rollback Timeline

| Action | Duration |
|--------|----------|
| DNS propagation | 5-10 min |
| Application warmup | 5 min |
| Full recovery | <30 min |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial rollback plan |
