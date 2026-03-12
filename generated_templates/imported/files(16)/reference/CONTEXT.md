---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# IT Documentation Matrix — Part 4: Integration & Support
## CONTEXT.md — Reference Guide

**Version:** 1.0 | **Created:** 2026-02-01 | **Part:** 4 of 9  
**Scope:** Industries 28–36 (IAM, PM, PERF, SUPP, HD, SOL, APIM, INTG, VIRT)  
**Total Documents:** 521 (472 unique + 49 shared)

---

## 1. Project Overview

This is Part 4 of the IT Documentation Matrix — a comprehensive system for standardizing documentation templates across IT specializations. Each Part covers 9 industry sectors with full document extraction, dependency mapping, lifecycle management, section structure, and RACI assignments.

**Parts completed so far:**
- Part 1: Security & Cybersecurity (branże 1–9) — 122 templates
- Part 2: QA / Testing (branże 10–18) — 114 templates  
- Part 3: Product & Management (branże 19–27) — ~603 documents
- **Part 4: Integration & Support (branże 28–36) — 521 documents** ← this file

---

## 2. Industries in This Part

| # | Code | Industry EN | Industry PL | Category | Docs |
|---|------|-------------|-------------|----------|------|
| 28 | IAM | Identity & Access Management | Zarządzanie tożsamością i dostępem | INTEGRATION | 59 |
| 29 | PM | IT Project Management | Zarządzanie projektami IT | MANAGEMENT | 59 |
| 30 | PERF | Performance Engineering | Inżynieria wydajności | OPTIMIZATION | 51 |
| 31 | SUPP | Technical Support | Wsparcie techniczne | SUPPORT | 53 |
| 32 | HD | Help Desk / User Support | Help Desk | SUPPORT | 49 |
| 33 | SOL | Solution Engineering | Inżynieria rozwiązań | MANAGEMENT | 47 |
| 34 | APIM | API Management | Zarządzanie API | INTEGRATION | 52 |
| 35 | INTG | Integration Engineering | Inżynieria integracji | INTEGRATION | 48 |
| 36 | VIRT | Virtualization Engineering | Inżynieria zwirtualizowania | INTEGRATION | 54 |
| — | SHARED | Shared Docs (Phases 17–23) | Dokumenty wspólne | ALL | 49 |

**Category breakdown:**
- INTEGRATION: IAM, APIM, INTG, VIRT (shared security & connectivity concerns)
- SUPPORT: SUPP, HD (user-facing service delivery)
- MANAGEMENT: PM, SOL (project & solution lifecycle)
- OPTIMIZATION: PERF (performance & reliability)

---

## 3. Phase Structure (23 Phases)

All 23 phases are consistent across all Parts of the project:

| Phase | Code | Name EN | Group |
|-------|------|---------|-------|
| 1 | CONCEPT | Concept & Vision | INITIATION |
| 2 | REQUIREMENTS | Requirements Analysis | INITIATION |
| 3 | DESIGN | System Design | DELIVERY |
| 4 | PLANNING | Detailed Planning | DELIVERY |
| 5 | PROTOTYPING | Prototyping / POC | DELIVERY |
| 6 | DEVELOPMENT | Development / Implementation | DELIVERY |
| 7 | TESTING | Testing & Validation | DELIVERY |
| 8 | STAGING | Staging / Pre-Production | DELIVERY |
| 9 | DEPLOYMENT | Deployment / Go-Live | DELIVERY |
| 10 | MONITORING | Monitoring Setup | OPERATIONS |
| 11 | OPTIMIZATION | Performance Optimization | OPERATIONS |
| 12 | INCIDENT_MGMT | Incident Management | OPERATIONS |
| 13 | MAINTENANCE | Maintenance | OPERATIONS |
| 14 | TRAINING | Training & Onboarding | OPERATIONS |
| 15 | DOCUMENTATION | Documentation & Knowledge Base | OPERATIONS |
| 16 | REVIEW | Review & Retrospective | OPERATIONS |
| 17 | BUDGET | Budgeting / Cost Management | GOVERNANCE |
| 18 | VENDOR | Vendor / Procurement | GOVERNANCE |
| 19 | GOVERNANCE | Governance / Compliance | GOVERNANCE |
| 20 | DECOMMISSION | Decommissioning | GOVERNANCE |
| 21 | DISASTER_RECOVERY | Disaster Recovery / BCP | GOVERNANCE |
| 22 | CHANGE_MGMT | Change Management | GOVERNANCE |
| 23 | CAPACITY | Capacity Planning | GOVERNANCE |

**Phases 17–23** use **SHARED documents** — created once and referenced by all 9 industries.

---

## 4. Document Types

| Type | Description | Typical Phases |
|------|-------------|----------------|
| STRATEGY | High-level direction & vision | 1–2 |
| DESIGN | Architecture & detailed design | 3–4 |
| PLAN | Action plans with timelines | 3–5 |
| SPEC | Technical specifications | 3–6 |
| PROCEDURE | Step-by-step processes | 6–13 |
| GUIDE | Reference guides & how-tos | 9–15 |
| REPORT | Status & analysis reports | 10–16 |
| CHECKLIST | Verification checklists | 7–19 |
| TEMPLATE | Reusable document templates | 6–15 |
| ANALYSIS | Assessment & analysis docs | 2–11 |
| METRICS | KPI & metrics definitions | 10–16 |
| TRAINING | Training materials | 14 |
| COMMUNICATION | Stakeholder communications | 9–20 |
| REFERENCE | Reference documentation | 15 |

---

## 5. Priority Levels

| Priority | Meaning | Action |
|----------|---------|--------|
| CRITICAL | Must-have — project cannot proceed without | Create first, block delivery if missing |
| HIGH | Important — required for production readiness | Create before go-live |
| MEDIUM | Recommended — improves operations | Create within first sprint post go-live |
| LOW | Nice-to-have — enhances completeness | Create when capacity allows |

---

## 6. Database Schema

### Tables (8)
```
industries          — 9 industries + metadata
phases              — 23 lifecycle phases
documents           — 521 document records (code, name EN/PL, type, priority, phase)
document_dependencies — ~60 relationships between documents
document_phases     — when each document is created/updated/referenced/archived
document_sections   — internal section structure for key documents
document_lifecycle  — lifecycle states with triggers & review frequency
document_raci       — RACI assignments per document
```

### Views (6)
```
v_documents_full            — Full document info with industry & phase joins
v_document_phase_matrix     — Matrix of documents across phases
v_document_dependencies     — Readable dependency graph
v_document_lifecycle        — Lifecycle rules with document info
v_document_raci             — RACI with document context
v_document_sections         — Sections with document context
```

---

## 7. Key Cross-Industry Dependencies

```
IAM ─────────┬──→ APIM (token validation, OAuth2)
             ├──→ INTG (certificate management)  
             ├──→ HD   (access requests, password resets)
             ├──→ VIRT (cert management, VM identity)
             └──→ SOL  (security requirements)

APIM ────────┬──→ INTG (API contracts, gateway policies)
             └──→ SOL  (API-led presales demos)

SUPP ◄────────── HD   (L2/L3 escalation)

SOL ──────────→ SUPP  (handover to support after implementation)
```

**Dependency types used:**
- `DEPENDS_ON` — cannot be completed without the other
- `EXTENDS` — builds upon / is a more detailed version
- `REFERENCES` — cites or uses information from
- `IMPLEMENTS` — puts into practice what was designed
- `TRIGGERS` — initiates the other document's creation/update
- `VALIDATES` — used to verify correctness
- `FEEDS_INTO` — output becomes input for the other
- `REPLACES` — supersedes an older document

---

## 8. Shared Documents (Phases 17–23)

49 documents shared across all industries. Created once, referenced by each industry.

| Phase | Prefix | Count | Key Documents |
|-------|--------|-------|---------------|
| 17 Budget | SHARED-B | 6 | Budget Proposal, CBA, TCO, CapEx/OpEx, ROI, Cost Tracking |
| 18 Vendor | SHARED-V | 7 | RFP, RFI, Vendor Evaluation, Contract, SLA, Risk Assessment, Procurement Checklist |
| 19 Governance | SHARED-G | 7 | Audit Checklist, Compliance Report, Policy Review, Certification, Risk Register, Control Matrix, Audit Trail |
| 20 Decommission | SHARED-D | 7 | Retirement Plan, Data Migration, Archive Strategy, Sunset Communication, Dependency Analysis, Decommissioning Checklist, Data Retention |
| 21 DR/BCP | SHARED-DR | 8 | DRP, BCP, RPO, RTO, Failover Procedures, DR Test Report, Crisis Communication, Backup Verification |
| 22 Change | SHARED-CM | 7 | RFC, CAB Notes, Change Calendar, Impact Assessment, Rollback Plan, Emergency Change, Success Criteria |
| 23 Capacity | SHARED-CP | 7 | Capacity Forecast, Growth Projections, Resource Allocation, Scalability Assessment, Performance Baseline, Threshold Alerts, Sizing Guide |

---

## 9. Standards & Frameworks Referenced

| Standard | Industries | Key Use |
|----------|-----------|---------|
| NIST SP 800-53 Rev.5 | IAM, VIRT | Access control & identity control families |
| NIST SP 800-63-4 | IAM | Digital identity guidelines (IAL/AAL/FAL) |
| NIST SP 800-207 | IAM, VIRT | Zero Trust Architecture |
| NIST SP 800-145 | VIRT | Cloud computing service/deployment models |
| ISO 27001:2022 | IAM, SUPP, APIM, INTG, VIRT | Information security management |
| ISO/IEC 20000-1 | SUPP, HD | IT Service Management certification |
| ITIL 4 | SUPP, HD | Service management practices |
| PMBOK 7 | PM | Project management global standard |
| PRINCE2 | PM | Stage-gate project methodology |
| ISO 21500 | PM | International project management guidance |
| Google SRE | PERF | SLOs, error budgets, reliability engineering |
| ISTQB CT-PT | PERF | Performance testing syllabus |
| TOGAF | SOL, INTG | Enterprise architecture framework |
| OpenAPI 3.1 | APIM | REST API specification standard |
| AsyncAPI 3.0 | APIM, INTG | Event-driven API specification |
| OWASP API Security Top 10 | APIM, INTG | API security risk framework |
| EIP (Hohpe & Woolf) | INTG | 65 enterprise integration patterns |
| CIS Benchmarks | VIRT | Virtualization security configuration |
| HDI Standards | SUPP, HD | Help desk professional competency |
| KCS | SUPP | Knowledge-Centered Service methodology |
| AWS Well-Architected | SOL, VIRT | Cloud architecture best practices |

---

## 10. Usage Guide

### Initialize database
```bash
python scripts/db_manager.py init
```

### List documents by industry
```bash
python scripts/db_manager.py list --industry IAM
python scripts/db_manager.py list --industry APIM --type STRATEGY
```

### Generate a single template
```bash
python scripts/db_manager.py template IAM-001
python scripts/db_manager.py template APIM-009
```

### Generate all templates
```bash
python scripts/db_manager.py template-all
python scripts/db_manager.py template-all --industry VIRT
```

### Export data
```bash
python scripts/db_manager.py export --format json
python scripts/db_manager.py export --format csv
```

### Generate report
```bash
python scripts/db_manager.py report
```

### Custom queries
```bash
python scripts/db_manager.py query "SELECT doc_code, doc_name_en FROM documents WHERE priority='CRITICAL'"
python scripts/db_manager.py query "SELECT * FROM v_document_dependencies WHERE source_industry='IAM'"
```

---

## 11. File Structure

```
part4-doc-matrix/
├── db/
│   ├── schema.sql                      # Database schema (8 tables + 6 views)
│   ├── data_industries_phases.sql      # 9 industries + 23 phases
│   ├── data_documents.sql              # 521 document records
│   ├── data_relationships_lifecycle.sql # Dependencies, lifecycle, sections, RACI (core)
│   ├── data_sections_raci_expanded.sql  # Expanded sections & RACI (from research)
│   └── part4_doc_matrix.db             # SQLite database (generated by init)
├── scripts/
│   └── db_manager.py                   # CLI management tool
├── research/
│   └── internet_research.md            # Research findings per industry
├── reference/
│   └── CONTEXT.md                      # This file
├── exports/                            # JSON/CSV exports (generated)
└── templates/                          # Markdown templates (generated)
```

---

*IT Documentation Matrix Part 4 — Generated 2026-02-01*  
*Research-first methodology: internet research → database → sections → RACI → templates*
