---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Internet Research — IT Documentation Matrix Part 4 (Branże 28–36)
## Integration & Support: IAM, PM, PERF, SUPP, HD, SOL, APIM, INTG, VIRT

Synthesized 2026-02-01. Informs document_sections, document_raci, and cross-industry dependencies in the database.

---

## Cross-Industry Dependency Map

IAM is the foundational pillar — referenced by almost all other domains (APIM token validation, INTG cert management, HD access requests, VIRT certificate mgmt). APIM, INTG, and IAM form a tightly coupled triad. SUPP and HD share an escalation dependency (HD → SUPP L2/L3).

---

## 28 — IAM (Identity & Access Management)

### Standards
- NIST SP 800-53 Rev.5 — AC/IA control families
- NIST SP 800-63-4 — Digital Identity Guidelines (IAL/AAL/FAL)
- ISO 27001:2022 — A.5.15–A.5.18 access/identity controls
- NIST SP 800-207 — Zero Trust Architecture
- SOC 2 Trust Services — MFA, RBAC requirements

### IAM Strategy (IAM-001) Recommended Sections
1. Executive Summary — business context, investment summary
2. Current State Assessment — infra inventory, HR systems, gap analysis
3. Governance Framework — RACI, policy framework, compliance mapping
4. Target State Architecture — identity lifecycle, auth (SSO/MFA/Federation), RBAC/ABAC, PAM
5. IAM Policies & Standards — credential mgmt, JML (Joiner-Mover-Leaver)
6. Technology Stack — IdP, IGA, PAM, MFA platforms
7. Implementation Roadmap — phased maturity model
8. Compliance Alignment — NIST 800-53, ISO 27001, SOC 2 mappings
9. Success Metrics — security, operational, UX KPIs

### Key RACI Roles
- CISO/Security Director: Accountable for strategy & policies
- IAM Program Manager: Responsible for roadmap execution
- Identity Architect: Responsible for architecture & tech selection
- Business Unit Leaders: Accountable for role definitions & access reviews
- HR Department: Consulted on JML processes
- Internal Audit: Consulted on controls; reviews certifications

---

## 29 — PM (IT Project Management)

### Standards
- PMBOK 7th Edition (PMI) — principle-based, Charter, Management Plan, Risk Register
- PRINCE2 — stage-gate, PID, Business Case, Benefits Management
- ISO 21500 series — project mgmt concepts & guidance
- Agile/Scrum — lightweight docs: Product Backlog, User Stories, Definition of Done
- SAFe 6.0 — PI Objectives, Program Backlog, Lean Business Case

### Project Charter (PM-001) Recommended Sections
1. Project Title & Code
2. Purpose / Business Need — problem statement, strategic alignment
3. Objectives — SMART goals
4. High-Level Scope — inclusions, exclusions, boundaries
5. Key Deliverables — acceptance criteria
6. Success Criteria — measurable outcomes
7. Milestones — phase gates
8. Budget Summary — estimated costs, funding, contingency
9. Project Manager Assignment
10. Key Stakeholders — interests, influence
11. Assumptions & Constraints
12. High-Level Risks
13. Approval Signatures

### Key RACI Roles
- Executive Sponsor: Accountable for business outcomes & funding
- Project Manager: Responsible for delivery; Accountable for schedule/budget
- Product Owner (Agile): Accountable for backlog; Responsible for acceptance
- Technical Architect: Responsible for tech design
- Change Advisory Board: Consulted on changes

---

## 30 — PERF (Performance Engineering)

### Standards
- Google SRE Framework — SLOs, SLIs, Error Budgets
- ISTQB CT-PT — performance testing syllabus
- IEEE 829-2008 / ISO 29119 — test documentation
- APM Vendor Practices — Datadog, New Relic, Dynatrace

### Performance Goals (PERF-001) Recommended Sections
1. Executive Summary — business context, performance vision
2. Current Performance Baseline — measured KPIs, bottlenecks identified
3. Performance Targets — response time (p50/p90/p95/p99), throughput, error rate, Apdex
4. SLO Definitions — per-service targets aligned to business objectives
5. Error Budget Policy — allowable degradation, budget calculation
6. Scope & Boundaries — systems in scope, excluded components
7. Measurement Methodology — instrumentation, monitoring tools, data collection
8. Governance — review cadence, escalation thresholds
9. Success Criteria — pass/fail definitions

### Key RACI Roles
- Performance Engineer: Responsible for test design, execution, analysis
- SRE: Accountable for service reliability & SLOs
- Product Owner: Accountable for business requirements
- Developers: Responsible for code optimization
- Architect: Consulted on system design implications

---

## 31 — SUPP (Technical Support)

### Standards
- ITIL 4 — 34 practices incl. Service Desk, Incident, Problem Management
- KCS (Knowledge-Centered Service) — Solve Loop + Evolve Loop
- ISO/IEC 20000-1:2018 — SMS requirements
- HDI Standards — professional competency
- SDI Global Best Practice v8 — empathy-based service delivery

### Support Strategy (SUPP-001) Recommended Sections
1. Executive Summary — vision, strategic goals
2. Service Goals & KPIs — aligned to business
3. Support Model — tier structure (L0–L4), channel strategy
4. Service Catalog — scope & coverage
5. SLA Framework — response/resolution by priority
6. OLA Definitions — internal handoff agreements
7. Resource Planning — staffing, skills matrix, capacity
8. Technology Stack — ticketing, KB, monitoring
9. Knowledge Management — KCS adoption, content governance
10. Continuous Improvement — metrics review cadence

### Key RACI Roles
- Support Manager: Accountable for operations & SLA compliance
- Knowledge Manager: Accountable for KB quality & KCS
- Tier 1 Analyst: Responsible for first contact resolution
- Tier 2/3 Engineer: Responsible for advanced troubleshooting & RCA
- Incident Manager: Accountable for incident lifecycle
- Problem Manager: Accountable for RCA & known error DB

---

## 32 — HD (Help Desk / User Support)

### Standards
- ITIL 4 Service Desk — SPOC, Shift-Left strategy
- HDI Support Center Standard v5.3 — 8 categories, 4 maturity levels
- ISO/IEC 20000-1 — service catalog, SLAs, OLAs
- HDI Professional Certifications — CSR, SCA, DAST
- COBIT 5 — IT governance overlay

### Help Desk Vision (HD-001) Recommended Sections
1. Executive Summary — HD vision, strategic positioning
2. Business Objectives — cost reduction, user satisfaction targets
3. Service Scope — supported systems, user base, channels
4. Service Model — tier structure, first-call resolution targets
5. Self-Service Strategy — portal roadmap, deflection targets
6. Knowledge Management — KB structure, maintenance plan
7. SLA Commitments — response/resolution targets
8. Staffing & Training — roles, certification roadmap
9. Technology Requirements — ticketing system, monitoring
10. Success Metrics — CSAT, FCR, AHT, deflection rate

### Self-Service Portal Design (HD-008) Recommended Sections
1. Purpose & Objectives — deflection rate targets (20%+), cost savings
2. User Research & Personas — end-user analysis, journey mapping
3. Portal Architecture — Focused/Unified/Hybrid, ITSM integration, SSO
4. Service Catalog Design — categories, forms, role-based visibility
5. KB Integration — article structure, search optimization
6. UI Requirements — mobile-first, WCAG 2.2 accessibility
7. Automation & AI — chatbot, intelligent routing
8. Metrics & Analytics — usage, self-service resolution rate
9. Implementation Roadmap — phased rollout

### Key RACI Roles
- Help Desk Manager: Accountable for service desk operations & SLA
- Self-Service Portal Owner: Accountable for portal strategy & UX
- Tier 1 Analyst: Responsible for incident logging & categorization
- Knowledge Manager: Accountable for KB quality & article lifecycle
- QA Analyst: Responsible for interaction monitoring & quality scoring

---

## 33 — SOL (Solution Engineering / Presales)

### Standards
- TOGAF — Architecture Definition Document, Requirements Spec
- AWS Well-Architected — 6 pillars: Operations, Security, Reliability, Performance, Cost, Sustainability
- Azure Architecture Center — reference architectures, design patterns
- Google Cloud Architecture Framework — design decision documentation
- ITIL Service Design — Service Design Package (SDP)

### Solution Strategy (SOL-001) Recommended Sections
1. Executive Summary — solution engineering vision
2. Market & Competitive Analysis — positioning, differentiators
3. Target Customer Profiles — industries, pain points, maturity
4. Solution Portfolio — product/service offerings
5. Go-to-Market Strategy — sales motion, partner channels
6. Delivery Model — POC/pilot approach, implementation methodology
7. Technology Stack — platforms, tools, partners
8. Success Metrics — win rate, POC conversion, customer satisfaction

### Solution Architecture (SOL-009) Recommended Sections
1. Executive Summary — business alignment
2. Scope & Constraints — boundaries, assumptions
3. Stakeholder Analysis — concerns, viewpoints
4. Architecture Vision — target state, value proposition
5. Business Architecture — processes, capabilities
6. Data Architecture — entities, flows, storage
7. Application Architecture — components, interfaces
8. Technology Architecture — infra, platforms, stack
9. Security Architecture — requirements, controls
10. Architecture Decisions (ADRs) — rationale, alternatives
11. NFRs — performance, scalability, availability
12. Migration Plan — phased approach
13. Risks & Mitigations

### Key RACI Roles
- Solution Architect: Responsible for technical design & architecture decisions
- Presales/Sales Engineer: Responsible for discovery, demos, POCs
- Account Executive: Accountable for deal ownership
- Customer Success Manager: Responsible for post-sales adoption
- Professional Services Lead: Responsible for implementation planning

---

## 34 — APIM (API Management)

### Standards
- OpenAPI Specification 3.1 — REST API description, JSON Schema compatible
- AsyncAPI 3.0 — event-driven APIs (Kafka, MQTT, WebSocket)
- OWASP API Security Top 10 — BOLA, broken auth, resource consumption
- Google API Design Guide — resource-oriented design, naming conventions
- Microsoft REST API Guidelines — HTTP methods, error handling, pagination

### API Strategy (APIM-001) Recommended Sections
1. Executive Summary — API program vision
2. Business Objectives — revenue, market, partnership strategy
3. Governance Model — design standards, approval workflows, lifecycle
4. Audience/Personas — internal devs, partners, public consumers
5. Architecture Principles — REST vs GraphQL, event-driven
6. Security Strategy — auth methods, authorization, OWASP alignment
7. Lifecycle Management — versioning policy, deprecation, migration
8. Success Metrics — adoption, developer satisfaction, uptime
9. Technology Stack — gateway, portal, monitoring
10. Cross-Domain Dependencies — IAM, Security, DevOps, Compliance

### Key RACI Roles
- API Product Manager: Accountable for strategy & roadmap
- API Architect: Accountable for architecture, standards, consistency
- API Developer: Responsible for implementation & specs
- API Gateway Admin: Responsible for gateway policies & monitoring
- API Security Engineer: Accountable for security controls
- DevRel: Responsible for developer community & portal content

---

## 35 — INTG (Integration Engineering)

### Standards
- Enterprise Integration Patterns (EIP) — 65 patterns in 9 categories (Hohpe & Woolf)
- TOGAF — ADM lifecycle, Architecture Building Blocks
- Apache Camel — EIP implementation, 300+ connectors
- MuleSoft API-Led Connectivity — Experience/Process/System API layers
- Cloud Integration Services — AWS EventBridge, Azure Logic Apps, Step Functions

### Integration Vision (INTG-001) Recommended Sections
1. Executive Summary — integration program vision
2. Business Context — driving business needs, strategic alignment
3. Current Integration Landscape — existing systems, pain points, tech debt
4. Integration Principles — technology-agnostic, loose coupling, event-driven
5. Target Architecture Vision — pattern-based, scalable, observable
6. Integration Patterns Roadmap — sync vs async, batch vs real-time priorities
7. Technology Evaluation — iPaaS, ESB, event brokers comparison
8. Governance Model — standards, review process, ownership
9. Success Metrics — integration reliability, latency SLAs, onboarding time

### Key RACI Roles
- Integration Architect: Accountable for strategy & pattern selection
- Integration Developer: Responsible for implementation & transformations
- Data Engineer: Accountable for ETL/ELT pipelines & data quality
- API Developer: Responsible for API contracts
- Enterprise Architect: Consulted for strategic alignment
- DevOps Engineer: Accountable for CI/CD & deployment

---

## 36 — VIRT (Virtualization Engineering)

### Standards
- VMware Validated Design (VVD) — prescriptive SDDC design
- CIS Benchmarks for VMware — Level 1/2 profiles, 100+ checks
- NIST SP 800-145 — cloud computing definitions (SaaS/PaaS/IaaS)
- ISO 27001:2022 — config mgmt (8.9), cloud security (5.23), continuity (5.30)
- VMware Security Configuration Guide — CIS/DISA STIG alignment

### Virtualization Strategy (VIRT-001) Recommended Sections
1. Executive Summary — virtualization vision & business case
2. Current State Assessment — existing infra, utilization rates, sprawl analysis
3. Strategic Objectives — consolidation ratios, cost targets, agility goals
4. Target Architecture — hypervisor strategy, cloud hybrid model
5. VM Standards & Governance — naming, sizing, lifecycle policies
6. Security Framework — hardening, CIS benchmarks, compliance
7. Capacity Planning Approach — forecasting model, growth projections
8. DR & Business Continuity — replication strategy, RPO/RTO targets
9. Implementation Roadmap — phased migration, quick wins
10. Success Metrics — consolidation ratio, TCO savings, availability

### Key RACI Roles
- Virtualization Architect: Accountable for strategic design & standards
- VM Administrator: Responsible for day-to-day operations & provisioning
- Infrastructure Engineer: Responsible for hardware, networking, storage
- Security Engineer: Accountable for hardening & compliance
- DR Coordinator: Responsible for continuity & DR testing
- Capacity Planner: Responsible for forecasting & rightsizing

---

## SHARED Documents (Phases 17–23)

### Budget (Phase 17) — SHARED-B01 to SHARED-B06
Roles: Finance Manager (R), VP Finance (A), Project Leads (C), Board (I)

### Vendor (Phase 18) — SHARED-V01 to SHARED-V07
Roles: Procurement Manager (R), Director (A), Technical Leads (C), Legal (C)

### Governance (Phase 19) — SHARED-G01 to SHARED-G07
Roles: Compliance Manager (R), CISO (A), Team Leads (C), Board (I)

### Decommission (Phase 20) — SHARED-D01 to SHARED-D07
Roles: Decommission Lead (R), IT Director (A), System Owners (C), HR (I)

### DR/BCP (Phase 21) — SHARED-DR01 to SHARED-DR08
Roles: Continuity Manager (R), CTO (A), Tech Leads (C), All Teams (I)

### Change Management (Phase 22) — SHARED-CM01 to SHARED-CM07
Roles: Change Manager (R), CAB Chair (A), Requestors (C), Stakeholders (I)

### Capacity Planning (Phase 23) — SHARED-CP01 to SHARED-CP07
Roles: Capacity Planner (R), Infrastructure Director (A), App Owners (C), Finance (I)

---

## Standards Mapping Summary

| Standard | Applicable Industries |
|---|---|
| NIST SP 800-53 | IAM (28), VIRT (36) |
| NIST SP 800-63 | IAM (28) |
| NIST SP 800-207 | IAM (28), VIRT (36) |
| ISO 27001:2022 | IAM (28), SUPP (31), APIM (34), INTG (35), VIRT (36) |
| ISO/IEC 20000 | SUPP (31), HD (32) |
| ITIL 4 | SUPP (31), HD (32) |
| PMBOK 7 / PRINCE2 | PM (29) |
| ISO 21500 | PM (29) |
| Google SRE | PERF (30) |
| ISTQB | PERF (30) |
| TOGAF | SOL (33), INTG (35) |
| OpenAPI 3.1 | APIM (34) |
| AsyncAPI 3.0 | APIM (34), INTG (35) |
| OWASP API Security | APIM (34), INTG (35) |
| EIP (Hohpe & Woolf) | INTG (35) |
| CIS Benchmarks | VIRT (36) |
| NIST SP 800-145 | VIRT (36) |
| HDI Standards | SUPP (31), HD (32) |
| AWS Well-Architected | SOL (33), VIRT (36) |
| KCS | SUPP (31) |
| COBIT | HD (32), PM (29) |
