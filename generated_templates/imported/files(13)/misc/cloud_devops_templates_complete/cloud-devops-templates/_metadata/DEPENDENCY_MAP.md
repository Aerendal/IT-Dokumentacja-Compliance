---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Cloud Infrastructure / DevOps - Dependency Map

##  COMPLETED: 123 Templates

| Phase | Count | Description |
|-------|-------|-------------|
| Phase 01 | 3 | Strategy & Vision |
| Phase 02 | 5 | Requirements Analysis |
| Phase 03 | 6 | Design |
| Phase 04 | 4 | Planning |
| Phase 05 | 5 | Implementation |
| Phase 06 | 5 | Testing / QA |
| Phase 07 | 5 | Security / Compliance |
| Phase 08 | 4 | Deployment |
| Phase 09 | 5 | Operations / Maintenance |
| Phase 10 | 4 | Incident Management |
| Phase 11 | 6 | Monitoring / Observability |
| Phase 12 | 5 | Documentation |
| Phase 13 | 5 | Training / Onboarding |
| Phase 14 | 4 | Stakeholder Communication |
| Phase 15 | 4 | Knowledge Management |
| Phase 16 | 4 | Postmortem / Retrospective |
| Phase 17 | 6 | Budget / Cost Management |
| Phase 18 | 7 | Vendor / Procurement |
| Phase 19 | 7 | Governance / Compliance Auditing |
| Phase 20 | 7 | Decommissioning / End-of-Life |
| Phase 21 | 8 | Disaster Recovery / BCP |
| Phase 22 | 7 | Change Management |
| Phase 23 | 7 | Capacity Planning |
| **TOTAL** | **123** | **Complete** |

---

## Document Dependencies

### Phase 1 → Phase 2
- CLD-001 (Cloud Strategy) → CLD-004 (Requirements)
- CLD-002 (Architecture Vision) → CLD-009 (Architecture Design)

### Phase 2 → Phase 3
- CLD-004 (Requirements) → CLD-009-014 (Design docs)
- CLD-008 (HA Requirements) → CLD-014 (HA Design)

### Phase 3 → Phase 5
- CLD-009 (Architecture) → CLD-019-023 (Implementation)
- CLD-010 (IaC Design) → CLD-019 (IaC Implementation)

### Phase 5 → Phase 6
- CLD-019-023 (Implementation) → CLD-024-028 (Testing)

### Operations Flow
- CLD-047 (Monitoring Strategy) → CLD-043 (Incident Response)
- CLD-102 (DR Plan) → CLD-106 (Failover Procedures)

---

## Document Range: CLD-001 through CLD-123

**Completed:** 2026-01-31
