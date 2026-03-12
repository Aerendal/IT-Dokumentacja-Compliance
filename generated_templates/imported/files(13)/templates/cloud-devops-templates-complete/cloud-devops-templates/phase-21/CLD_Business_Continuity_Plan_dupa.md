---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Disaster Recovery / Business Continuity Document

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | [ID] |
| **Version** | 1.0 |
| **Owner** | [DR Manager / SRE Team] |

---

## 1. Recovery Objectives

| Application | RTO | RPO | Tier |
|-------------|-----|-----|------|
| Payment System | 15 min | 5 min | 1 |
| Customer Portal | 1 hour | 15 min | 2 |
| Internal Apps | 4 hours | 1 hour | 3 |

---

## 2. DR Architecture

```
Primary (us-east-1)          DR Site (us-west-2)
┌──────────────────┐        ┌──────────────────┐
│  Active          │        │  Standby         │
│  - App Servers   │ ──────►│  - App (scaled)  │
│  - Database      │  Repl  │  - DB Replica    │
│  - Storage       │ ──────►│  - S3 Replica    │
└──────────────────┘        └──────────────────┘
```

---

## 3. Failover Procedure

| Step | Action | Owner | Time |
|------|--------|-------|------|
| 1 | Declare disaster | DR Manager | T+0 |
| 2 | Activate DR site | Platform Team | T+5m |
| 3 | DNS failover | Network Team | T+10m |
| 4 | Validate services | QA Team | T+20m |
| 5 | Notify stakeholders | Communications | T+30m |

---

## 4. Testing Schedule

| Test Type | Frequency | Last Test | Next Test |
|-----------|-----------|-----------|-----------|
| Tabletop | Quarterly | [Date] | [Date] |
| Component | Monthly | [Date] | [Date] |
| Full DR | Annually | [Date] | [Date] |

---

## 5. Contact List

| Role | Primary | Backup |
|------|---------|--------|
| DR Manager | [Name] | [Name] |
| On-call Engineer | PagerDuty | [Name] |
| Communications | [Name] | [Name] |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial document |
