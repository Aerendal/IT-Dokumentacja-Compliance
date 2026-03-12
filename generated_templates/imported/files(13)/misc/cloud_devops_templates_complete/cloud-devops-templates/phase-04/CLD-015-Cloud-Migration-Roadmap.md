---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-015: Cloud Migration Roadmap

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-015 |
| **Version** | 1.0 |
| **Owner** | [Migration Lead] |

---

## 1. Migration Timeline

```
Q1 2024          Q2 2024          Q3 2024          Q4 2024
────────────────────────────────────────────────────────────
│ WAVE 1         │ WAVE 2         │ WAVE 3         │ WAVE 4
│ Foundation     │ Core Apps      │ Data Platform  │ Legacy
│                │                │                │
│ • Landing Zone │ • Web Apps     │ • Databases    │ • Complex
│ • Network      │ • APIs         │ • Analytics    │ • Mainframe
│ • Security     │ • Microservices│ • Data Lake    │
│ • Dev/Test     │                │                │
────────────────────────────────────────────────────────────
```

---

## 2. Wave Details

### Wave 1: Foundation (Q1)
| Milestone | Target Date | Owner |
|-----------|-------------|-------|
| Landing Zone Setup | Week 4 | Platform Team |
| Network Connectivity | Week 6 | Network Team |
| Security Baselines | Week 8 | Security Team |
| Dev/Test Migration | Week 12 | Dev Teams |

### Wave 2: Core Applications (Q2)
| Application | Strategy | Effort | Risk |
|-------------|----------|--------|------|
| Customer Portal | Replatform | 4 weeks | Medium |
| API Gateway | Refactor | 6 weeks | Low |
| Mobile Backend | Rehost | 2 weeks | Low |

### Wave 3: Data Platform (Q3)
| Component | Strategy | Effort |
|-----------|----------|--------|
| Data Warehouse | Replatform to Redshift | 8 weeks |
| ETL Pipelines | Refactor to Glue | 6 weeks |
| Analytics | Migrate to QuickSight | 4 weeks |

### Wave 4: Legacy Systems (Q4)
| System | Strategy | Notes |
|--------|----------|-------|
| Mainframe Apps | Retain/Hybrid | Long-term modernization |
| Legacy ERP | Evaluate SaaS | Potential repurchase |

---

## 3. Success Criteria

| Phase | Criteria | Target |
|-------|----------|--------|
| Wave 1 | Landing zone operational | 100% |
| Wave 2 | Core apps in cloud | 100% uptime |
| Wave 3 | Data platform migrated | <5% performance variance |
| Wave 4 | Legacy integration | Hybrid operational |

---

## 4. Resource Plan

| Role | Wave 1 | Wave 2 | Wave 3 | Wave 4 |
|------|--------|--------|--------|--------|
| Cloud Architects | 2 | 2 | 2 | 1 |
| Platform Engineers | 4 | 3 | 2 | 2 |
| App Developers | 0 | 6 | 4 | 4 |
| Data Engineers | 0 | 0 | 4 | 2 |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial roadmap |
