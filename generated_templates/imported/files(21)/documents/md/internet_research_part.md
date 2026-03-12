---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Internet Research — IT Documentation Matrix Part 9
## Branże 72–81 | Zebrane standardy, frameworki i best practices

**Data researchu:** 2026-02-01  
**Zakres:** 10 branż (72–81)  
**Cel:** Informowanie struktury sekcji, RACI i lifecycle w kolejnych faznach metodologii  

---

## 72. PropTech / Real Estate Technology

### Kluczowe standardy i frameworki
- **OSCRE International IDM (Integrated Data Model)** — standard interoperabilności danych w real estate. Adopcja przez MRI Software zmniejszyła czas integracji o 30%, koszty o 25%.
- **Project Haystack** — otwarty standard tagging'u dla danych smart building / IoT (temperatura, energia, ocupancy).
- **GDPR / CCPA** — mandatory dla danych najemców (tenant PII, dane finansowe).
- **Fair Housing Act compliance** — wymogi w procesach wynajmu i rekrutacji najemców.
- **ESG Reporting** — rosnące wymogi raportowania environmental/social governance dla portfolios.

### Architektura systemów
- Cloud-native, microservices/serverless — modularne platformy property management.
- API-first design: integracje z systemy płatności, portale najemców, IoT sensors.
- Docker/Kubernetes containerization dla skalowalności multi-tenant.
- Key components: Property Management Platform, Tenant Portal, Smart Building IoT, Virtual Tours, Lease Management, Analytics Dashboards.

### Platformy referencyjna
Buildium, Entrata, MRI Software (enterprise), Compass, Zillow, Airbnb, Guesty.

### Metryki branży
- Global PropTech market: $9.6B (2020) → $22.2B (2025), CAGR 18.3%.
- 97% real estate companies believe digital innovation will significantly impact business.

---

## 73. HRTech / Talent Management

### Kluczowe standardy i frameworki
- **GDPR** — data protection dla employee PII (szczególnie EU employees).
- **Local labor law compliance** — automated tracking wymógu płacy minimalnnej, czas pracy, etc.
- **SOC 2 Type II** — bezpieczeństwo danych w cloud HR platforms.
- **EEOC / diversity reporting** — wymogi raportowania w US.

### Typy systemów (hierarchia)
1. **HRIS** — core HR data (employee records, org structure)
2. **HRMS** — adds talent management (recruitment, performance, L&D)
3. **HCM** — full lifecycle + analytics + workforce planning

### Architektura
- Cloud-based, single sign-on, unified employee view across HR/finance/IT.
- API integrations: payroll, talent management, IT service management.
- Self-service portals dla pracowników.
- Real-time analytics dashboards (people analytics).

### Platformy referencyjna
Workday, Oracle HCM, SAP SuccessFactors (enterprise), BambooHR, Paycor (mid-market). Lever (ATS), Cornerstone OnDemand (LMS).

### Trends 2025–2026
- AI-driven talent management i predictive analytics.
- Hybrid workplace tools (post-COVID standard).
- HRIS-payroll-L&D integration (full stack).
- Automated compliance monitoring.
- 76% CHROs believe organizations will lag without AI adoption.

---

## 74. MarTech / AdTech

### Kluczowe standardy i frameworki
- **IAB Tech Lab** — interoperability standards dla advertising ecosystem (Supply Chain Object, ads.txt verification, GDPR consent).
- **GDPR / ePrivacy Directive** — consent management, cookie deprecation.
- **CCPA / CPRA** — US privacy compliance.
- **TCF (Transparency & Consent Framework)** — EU-specific consent management standard.

### Architektura — 4-layer stack
1. **Data/Content Management** — CRM, CDP (Customer Data Platform), CMS, DAM
2. **Social/Content Optimization** — social media management, SEO tools
3. **Analytics & Insights** — attribution, conversion tracking, BI
4. **Advertising/Programmatic** — DSP (Demand-Side Platform), SSP (Supply-Side Platform), ad exchanges

### Key distinction: MarTech vs AdTech
- **MarTech** = engagement/retention, 1st-party data, CRM/CDP focused.
- **AdTech** = paid media activation/reach, historically 3rd-party data → shifting to 1st-party + contextual targeting.

### CDP role
- Unified customer profiles via identity resolution.
- Connects MarTech and AdTech ecosystems.
- Enables omnichannel personalization, frequency capping, audience activation.

### Metryki branży
- 14,106 MarTech solutions tracked (2024), 27.8% YoY growth.
- U.S. B2B MarTech spend approaching $14B by 2027.
- Global MarTech category: $215B+ by 2027.

### Trends
- Privacy-first measurement (server-side tracking, composable CDP).
- Generative AI for content creation at scale.
- Real-time personalization across channels.

---

## 75. GovTech / Public Sector IT

### Kluczowe standardy i frameworki
- **OECD Digital Government Policy Framework** — 6 dimensions: Digital by design, Data-driven, Government as platform, Open by default, User-driven, Proactiveness.
- **NIST Cybersecurity Framework (CSF 2.0)** — primary cybersecurity standard.
- **FISMA (Federal Information Security Management Act)** — US federal IT security compliance.
- **WCAG 2.0/2.1 AA** — mandatory accessibility standards dla government digital services.
- **ISO/IEC 27001** — information security management.
- **IPv6 (USGv6 Profile)** — mandatory IPv6 support dla US federal networks.

### Compliance & regulatory
- **SOX (Sarbanes-Oxley)** — financial reporting controls.
- **PCI DSS** — payment card data security (e-gov payments).
- **FAR (Federal Acquisition Regulation)** — procurement standards.
- **GDPR** — dla EU government data processing.

### Architektura
- Enterprise Architecture (EA): business / information / application / technology layers.
- Zero Trust Architecture (GovZTA) — never trust, always verify.
- API-driven data exchange, common interoperability frameworks.
- Digital identity/authentication (unique digital identifiers, e.g. MPID).
- Shared cloud platforms, e-document management.

### Trends
- Agile governance replacing waterfall procurement/development.
- GovTech startup collaboration — 70% OECD members have digital strategies.
- AI adoption with ethical/accountability frameworks.
- Open data standards, citizen-centric service design.

---

## 76. Automotive IT / Connected Vehicles

### Kluczowe standardy i frameworki — SAFETY CRITICAL
- **ISO 26262:2018** — *Primary* functional safety standard for E/E systems. ASIL ratings A–D (Automotive Safety Integrity Levels) based on severity × occurrence × exposure. Covers full lifecycle: concept → decommissioning.
- **ISO 21434** — cybersecurity engineering dla automotive.
- **SAE J3061** — cyber best practices dla automotive.
- **UNECE WP.29** — mandatory cybersecurity management systems (mandatory for new type approvals).
- **IACS UR E26** — system integration requirements (mandatory newbuilds after July 2024).
- **IACS UR E27** — essential onboard systems requirements.

### Architektura — evolucja
1. **Distributed ECU** (legacy) — individual Electronic Control Units per function
2. **Domain-based** — ECUs grouped by domain (powertrain, chassis, body)
3. **Zonal** — geographic zones in vehicle
4. **Centralized compute** (current trend) — central HPC + thin zones

### Software platform
- **AUTOSAR Classic** — traditional embedded automotive software (real-time, bare metal).
- **AUTOSAR Adaptive** — modern, OS-based, for high-performance computing domains (ADAS, infotainment).

### OTA Updates
- Over-the-air software updates dla ECUs — growing standard.
- Must comply z ISO 26262, security verification, rollback capabilities.
- UNECE WP.29 requires cryptographic verification.

### Development standards
- **ASPICE (Automotive Software Process Improvement and Capability Evaluation)** — process capability assessment (SPICE-based).
- **MISRA C/C++** — coding standards dla safety-critical embedded software.
- Influence from DO-178 (aerospace) dla safety-critical software.

---

## 77. Aerospace / Aviation IT

### Kluczowe standardy i frameworki — SAFETY CRITICAL (highest rigor)
- **DO-178C / ED-12C** — *Primary* standard dla software w airborne systems. Recognized by FAA, EASA, Transport Canada. Replaced DO-178B in 2012.
- **DO-254 / ED-79** — hardware design assurance for airborne electronic equipment.
- **SAE ARP4754A** — system-level development (Guidelines for Development of Aviation Products).
- **AS9100D** — quality management system for aerospace/defense organizations.

### Design Assurance Levels (DAL)
| DAL | Failure Effect | Rigor Level |
|-----|---------------|-------------|
| A | Catastrophic | Highest — every requirement verified independently |
| B | Hazardous | Very high |
| C | Major | High |
| D | Minor | Moderate |
| E | No effect | No assurance required |

### DO-178C Supplements
- **DO-330** — Tool Qualification (kwalifikacja narzędzi)
- **DO-331** — Model-Based Development (MBD)
- **DO-332** — Object-Oriented Technologies
- **DO-333** — Formal Methods

### Lifecycle (DO-178C)
Planning (PSAC, SDP, SVP, SCMP, SQAP) → Development → Verification → Configuration Management → Quality Assurance → Certification.

- **Stage of Involvement (SOI)** reviews z certification authorities (FAA/EASA).
- **Bidirectional traceability** mandatory: system req → software req → design → code → tests → verification results.

### Open Architecture
- **FACE Consortium** — open architecture standards dla defense/aerospace (reuse, affordability, portability).

### Challenges
- Highest complexity i regulatory burden w IT industry.
- Time/cost intensive — DAL A certification may take years.
- Tool qualification required for all tools w development chain.

---

## 78. Maritime / Shipping IT

### Kluczowe standardy i frameworki — REGULATORY MANDATORY
- **IMO Resolution MSC.428(98)** — *mandatory* cyber risk management w Safety Management Systems (SMS) per ISM Code. Effective January 1, 2021 dla wszystkich SOLAS/ISM vessels.
- **MSC-FAL.1/Circ.3** — Maritime Cyber Risk Management Guidelines (IMO).
- **BIMCO Guidelines on Cyber Security Onboard Ships** — Version 5 (November 2024), industry best practice.
- **IACS UR E26** — system integration requirements dla newbuilds (mandatory po July 1, 2024).
- **IACS UR E27** — essential onboard systems (engine control, steering, navigation, communications, fire detection).

### Compliance frameworks
- **NIST Cybersecurity Framework** — risk-based approach.
- **ISO/IEC 27001** — information security management.
- **ISPS Code** — International Ship and Port Facility Security.
- **IAPH Cybersecurity Guidelines for Ports** — port-specific guidance.
- **EU NIS2 Directive (2024)** — essential services including maritime/ports.

### Vulnerable systems (attack surface)
Bridge systems (ECDIS, GPS, radar), propulsion/machinery control, cargo management, passenger systems, communications, administrative/crew welfare.

### Risk management process
PDCA (Plan-Do-Check-Act): threat identification → vulnerability assessment → protective/detective controls → incident response → recovery procedures.

### Maritime conventions (traditional + cyber)
UNCLOS, COLREG, SOLAS, STCW, SUA — traditional safety framework now incorporating cyber requirements.

---

## 79. Construction Tech (ConTech / BIM)

### Kluczowe standardy i frameworki
- **IFC (Industry Foundation Classes)** — *primary* open interoperability standard dla BIM. Official ISO standard: **ISO 16739-1:2024**. Developed by buildingSMART International.
- **IEC 61508** — functional safety dla E/E/PE systems — applicable do building automation/control systems. Safety Integrity Levels (SIL 1–4).
- **NBIMS-US (National BIM Standard — United States)** — US national standard incorporating IFC.
- **buildingSMART national requirements** — per-country mandates (e.g., Finland Common BIM Requirements 2012).

### IFC file formats
| Format | Extension | Standard | Notes |
|--------|-----------|----------|-------|
| IFC-SPF | .ifc | ISO 10303-21 (STEP) | Most common, compact text |
| IFC-XML | .ifcXML | ISO 10303-28 (STEP-XML) | Good for partial models |
| IFC-ZIP | .ifcZIP | — | Compressed IFC-SPF/XML |
| IFC-Turtle | .ifcTurtle | RDF/ifcOWL | Semantic web format |

### Government adoption (mandatory)
- **Denmark (2010):** IFC mandatory dla publicly aided building projects.
- **Finland:** Senate Properties requires IFC compatible software + BIM for all projects.
- **Norway:** Government/Health/Defense require IFC BIM in all projects.

### IFC extensions
- IFC Infrastructure Research Initiative — roads, tunnels, railways, bridges.
- Parametric geometry integration (IFC-Bridge).

### Software support
Autodesk Revit (IFC4 certified), Bentley, TEIGHA BIM, ArchiCAD. Certification via buildingSMART.

### Scope
Covers full building lifecycle: design → construction → operation → maintenance → demolition.

---

## 80. BioTech / Life Sciences IT

### Kluczowe standardy i frameworki — REGULATORY CRITICAL
- **FDA 21 CFR Part 11** — *primary* regulation dla electronic records i electronic signatures w FDA-regulated industries (pharma, biotech, medical devices). Enacted 1997. Requirements: system validation, audit trails, access controls, electronic signatures unique per user.
- **EU GMP Annex 11** — EU counterpart do 21 CFR Part 11 dla computerized systems.
- **GxP regulations** — umbrella:
  - **GMP** (Good Manufacturing Practice)
  - **GCP** (Good Clinical Practice)  
  - **GLP** (Good Laboratory Practice)
  - **GDP** (Good Distribution Practice)
- **ISO 13485** — quality management system dla medical devices (applicable to biotech devices).
- **HIPAA** — US health data privacy (dla biotech working with patient data).

### Data integrity standard
**ALCOA+ principles** — Attributable, Legible, Contemporaneous, Original, Accurate + (extended) Complete, Consistent, Enduring, Available. Mandatory framework dla regulated lab data.

### Key IT systems
- **LIMS (Laboratory Information Management System)** — sample tracking, workflow automation, instrument integration, data management. Core system dla lab operations.
- **ELN (Electronic Lab Notebook)** — digital recording of experiments, replacing paper lab notebooks.
- **SDMS (Scientific Data Management System)** — structured/unstructured scientific data management.
- **QMS (Quality Management System)** — quality control, document management, CAPA.
- **Clinical Trial Management Systems (CTMS)** — trial lifecycle management.
- **EDC (Electronic Data Capture)** — clinical trial data collection.

### 21 CFR Part 11 key requirements (IT perspective)
1. **System Validation** — CSV (Computer System Validation) mandatory before go-live.
2. **Audit Trails** — automatic, time-stamped, captures all create/modify/delete actions.
3. **Access Controls** — role-based, unique user IDs, session timeouts.
4. **Electronic Signatures** — unique per user, with date/time, non-reusable.
5. **Record Retention** — secure storage, retrieval capability per FDA timelines.
6. **Temporary Data** — must be captured in permanent record before manipulation possible (FDA 2016 guidance).

### FDA enforcement trends (2023–2024)
- 37% of regulated firms had Part 11-related finding in past 3 years.
- 80% of FDA warning letters (2015–2016) cited data integrity failures.
- Part 11 enforced increasingly in digital health technologies.

---

## 81. Pharma IT / Clinical Systems

### Kluczowe standardy i frameworki — REGULATORY CRITICAL
- **GAMP 5® (Good Automated Manufacturing Practice, 2nd Edition, 2022)** — *primary* guideline dla computer system validation (CSV) w pharma/life sciences. Published by ISPE. Risk-based approach. De facto industry standard, referenced by FDA, EMA, MHRA.
- **FDA 21 CFR Part 11** — electronic records/signatures (see industry 80).
- **EU GMP Annex 11** — computerized systems w EU GMP (draft revision 2025 underway).
- **ICH Q9** — Quality Risk Management — aligned w GAMP 5 QRM approach.
- **ISPE GAMP® Guide: Artificial Intelligence (July 2025)** — NEW comprehensive 290-page guide dla AI-enabled computerized systems w GxP.

### GAMP 5 software categories
| Category | Type | Validation Effort |
|----------|------|-------------------|
| 1 | Infrastructure (OS, middleware) | Minimal |
| 2 | Off-the-shelf (no config) | Limited |
| 3 | Commercial (configured) | Moderate |
| 4 | Custom-built | High |
| 5 | Custom-developed | Highest |

### GAMP 5 core principles (5 pillars)
1. **Lifecycle thinking** — concept to retirement, full traceability.
2. **Critical thinking** — risk-based decisions by knowledgeable SMEs.
3. **Risk-based validation** — scale effort to system criticality/complexity.
4. **Scalability** — flexible approach per system type.
5. **Leveraging supplier input** — maximize vendor documentation/expertise.

### CSV (Computer System Validation) lifecycle
Concept → Project Initiation → Risk Assessment → Specification (URS, FS, DS) → Design → Build → Testing (IQ, OQ, PQ) → Deployment → Operation → Retirement.

- **IQ** (Installation Qualification) — verify correct installation.
- **OQ** (Operational Qualification) — verify correct operation.
- **PQ** (Performance Qualification) — verify correct performance in intended use.

### Key pharma IT systems
- **CTMS (Clinical Trial Management System)** — end-to-end trial lifecycle.
- **EDC (Electronic Data Capture)** — eCRF for clinical trial data.
- **RTSM (Randomization & Trial Supply Management)** — trial logistics.
- **MES (Manufacturing Execution System)** — production control.
- **EBR (Electronic Batch Record)** — manufacturing batch documentation.
- **Regulatory Information Management System (RIMS)** — submission management.

### GAMP 5 2nd Edition updates (2022)
- Cloud computing & SaaS validation approaches.
- Agile/iterative development alignment.
- Cybersecurity integration.
- AI/ML considerations (expanded in 2025 standalone guide).
- Automated testing & tool-based verification encouraged.
- CSA (Computer Software Assurance) alignment with FDA direction.

---

## Cross-Industry Observations (72–81)

### Universal patterns
1. **Cloud-native architectures** dominant across all 10 sectors.
2. **API-first integration** strategies universal — enables ecosystem connectivity.
3. **Cybersecurity** elevated to board-level — regulatory requirement in 76, 77, 78.
4. **Regulatory compliance** increasingly complex and global (GDPR + local regulations).
5. **AI/ML adoption** accelerating but with governance requirements (esp. 80, 81).
6. **Open standards** gaining traction to avoid vendor lock-in (IFC, OSCRE, AUTOSAR, IAB).
7. **Privacy-first design** mandatory — GDPR/CCPA influence across all sectors.
8. **Real-time data analytics** becoming baseline expectation.

### Safety-critical tier (highest documentation rigor)
- **76 Automotive:** ISO 26262 ASIL ratings, ASPICE process capability.
- **77 Aerospace:** DO-178C DAL levels, SOI reviews, bidirectional traceability.
- **78 Maritime:** IMO mandatory cyber risk management, IACS requirements.

### Regulatory-critical tier (validated IT systems)
- **80 BioTech:** FDA 21 CFR Part 11, ALCOA+ data integrity, LIMS validation.
- **81 Pharma:** GAMP 5 CSV, GxP compliance, EU Annex 11.

### Cross-industry dependencies (informuje mapping w DB)
- **80 BioTech → 81 Pharma:** shared FDA 21 CFR Part 11, GxP frameworks, clinical trial systems.
- **76 Automotive → 77 Aerospace:** safety engineering methodology overlap (ASPICE ↔ DO-178C influence).
- **79 ConTech → 76 Automotive/78 Maritime:** IoT/sensor integration patterns.
- **75 GovTech → 72 PropTech:** public procurement, smart city integration.
- **73 HRTech → 75 GovTech:** public sector workforce management.

---

*Koniec researchu. Gotowe do: SQLite schema → document extraction → dependencies → lifecycle → sections → RACI → scripts → templates.*
