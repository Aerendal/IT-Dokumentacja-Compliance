---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Internet Research — IT Documentation Matrix Part 3 (Branże 19–27)

Synthesized from web searches conducted 2026-01-31. Used to inform document_sections, document_standards, and RACI assignments in the database.

---

## Branża 19 — Product Management

### Key Document: PRD (Product Requirements Document)

**Recommended sections (consensus across Atlassian, Aha!, Product School, Medium):**
1. Title & Change History — version control, who changed what
2. Overview / Purpose — what is being built and why
3. Success Metrics — KPIs defined upfront (SMART principle)
4. Background & Strategic Fit — alignment to company goals
5. Target Audience / Personas — user segments, pain points, motivations
6. User Scenarios / Stories — full stories of how personas use the product
7. Features & Functionality — hierarchical: Themes → Epics → User Stories; MoSCoW prioritization (Must/Should/Could/Won't)
8. Requirements (Functional & Non-Functional) — user stories, wireframes, acceptance criteria
9. Out-of-Scope — explicitly stated to prevent scope creep
10. Assumptions & Constraints — risks, dependencies
11. Timeline / Release Planning — milestones, phased releases
12. Risks & Mitigations
13. Stakeholder Sign-off
14. Appendix — links to related docs, design decisions, GTM details

**Evolution:** Waterfall-era PRDs were 30+ pages; modern agile PRDs target 4–8 pages. Amazon's "6-page memo" approach is widely referenced. PRD is a living document updated each sprint.

**Standards referenced:** WCAG 2.1 (accessibility), Agile/Scrum frameworks, IEEE 830 (software requirements)

**Tools ecosystem:** Confluence blueprints, Aha! Roadmaps, Jira integration, Notion templates

### Product Roadmap
- Formats: timeline, swimlane, now/next/later
- Contains: KPIs, OKRs, initiatives, milestones
- Audience: executive stakeholders + engineering teams
- Best practice: separate strategic roadmap from delivery roadmap

---

## Branża 20 — Technical Writing

### Key Document: Style Guide

**Recommended sections (Google, Microsoft, IBM, DigitalOcean patterns):**
1. Purpose & Scope — which docs this guide covers
2. Audience Definition — primary vs secondary audiences, skill levels
3. Voice & Tone — formal but friendly; avoid anthropomorphizing software
4. Language & Grammar — sentence structure, terminology consistency, controlled language (ASD-STE100)
5. Terminology & Glossary — organization-specific vocab, abbreviations spelled out first use
6. Document Structure — H1–H4 heading hierarchy, logical flow, orphan subsection avoidance
7. Formatting Standards — markdown/HTML conventions, code blocks, lists (bulleted vs numbered)
8. Linking & References — descriptive link text, cross-referencing
9. Accessibility — alt text, screen reader support, inclusive language
10. Code Samples & Examples — language conventions, indentation, annotations
11. Screenshots & Visuals — when to use, how to annotate
12. Versioning & Review Process — who reviews, approval workflow

**Standards referenced:** Google Developer Style Guide, Microsoft Writing Style Guide, IBM Style Guide (400+ pages), Apple Developer Documentation Style Guide, ASD-STE100 (Simplified Technical English), Chicago Manual of Style

**Key principles:** 15–20 words per sentence target, consistent terminology throughout, write for AI (structured for search/retrieval), second-person voice ("you"), lead sentence before every list

### Information Architecture (IA) Document
- Defines content hierarchy, navigation patterns, topic grouping
- Follows DITA (Darwin Information Typing Architecture) principles: concept/task/reference separation
- Validated via card sorting, tree testing with users

---

## Branża 21 — Developer Relations (DevRel)

### Key Document: SDK Onboarding Guide / Developer Portal Architecture

**Four pillars of DevRel (Linux Foundation / industry consensus):**
1. **Developer Advocacy** — liaison between community and product teams
2. **Developer Marketing** — technical content, SEO, awareness
3. **Developer Enablement** — docs, SDKs, tutorials, support
4. **Developer Community** — Discord, GitHub Discussions, ambassador programs

**SDK Documentation recommended sections:**
1. Getting Started (< 5 min to first success — "Time to First Hello World" metric)
2. Authentication & Setup
3. Core Concepts — mental model, architecture overview
4. Quick Start Tutorial — end-to-end working example
5. API Reference — auto-generated, searchable
6. Code Samples — multiple languages, real-world scenarios
7. Error Handling & Troubleshooting
8. Migration Guide (if applicable)
9. Changelog & Versioning

**Key metrics:** Time to First Hello World (TTFHW), Weekly Active Tokens (WAT), support ticket reduction, community contribution rate. Developers who complete onboarding convert at 3× the rate.

**Best practices:** Hands-on learning environments (no setup barriers), interactive demos, version-specific docs, feedback loops from community to product roadmap

---

## Branża 22 — Blockchain / Web3

### Key Document: Smart Contract Audit Report

**Audit process (OWASP SCSVS + Smart Contract Security Alliance + OpenZeppelin):**
1. **Specification Agreement** — project's functional requirements, architecture, design decisions documented BEFORE audit begins
2. **Scope Definition** — which contracts, primary goals (security/correctness/gas efficiency), areas of concern
3. **Static Analysis** — automated tools (Slither, MythX, Solgraph) + manual code review line-by-line
4. **Formal Verification** — mathematical proofs of contract behavior (optional, recommended for DeFi)
5. **Integration & Interoperability Testing** — cross-contract interactions, oracle dependencies, external APIs
6. **Gas Optimization Review** — efficiency analysis
7. **Test Coverage Assessment** — line coverage, SCSVS G12 standards
8. **Initial Report** — findings categorized: Critical / High / Medium / Low / Informational
9. **Remediation** — project team fixes issues
10. **Final Report** — all findings marked resolved/unresolved, made public for transparency

**Severity classification:** Critical → High → Medium → Minor (inefficient code) → Informational (style/best practices)

**Standards referenced:** OWASP Smart Contract Security Verification Standard (SCSVS), ERC-20/ERC-721/ERC-4626 token standards, ISO/TC307 (blockchain standards)

**Key requirement:** Code must be open-source; specification document is the #1 prerequisite for audit. README must include security vulnerability disclosure process.

### Tokenomics Design Document
- Token parameters: name, symbol, decimals, supply
- Mint/burn mechanics, distribution schedule
- Economic attack vectors analysis
- Regulatory compliance considerations

---

## Branża 23 — IoT (Internet of Things)

### Key Document: Protocol & Communication Architecture Spec

**MQTT (de facto IoT standard — OASIS/ISO):**
- Publish/Subscribe pattern with central broker
- QoS levels: 0 (at most once), 1 (at least once), 2 (exactly once)
- Lightweight: minimal footprint, optimized for constrained devices
- Ports: 1883 (standard), 8883 (TLS encrypted)
- MQTT 5.0 features: reason codes, shared subscriptions, message expiry, topic aliases, session expiry intervals

**Topic design best practices (AWS IoT Core guidance):**
1. Hierarchical structure with `/` separators (max 7 levels on AWS)
2. Prefix convention: `dt/` for telemetry, separate namespaces for commands
3. Lowercase + numbers + dashes only (case-sensitive)
4. Separate telemetry topics from command/control topics
5. Include device ID in topic path for per-device routing

**IoT Architecture layers documented:**
1. **Edge/Device Layer** — firmware specs, hardware constraints, power management
2. **Gateway Layer** — protocol translation (BLE → MQTT, CoAP → MQTT), edge computing
3. **Connectivity Layer** — cellular (LTE/5G), WiFi, LoRaWAN selection criteria
4. **Cloud/Broker Layer** — broker deployment (on-prem vs cloud), load balancing, mTLS
5. **Application Layer** — backend services, analytics, dashboards

**Key features to document:** Last Will and Testament (LWT) for disconnect detection, persistent sessions for unreliable networks, retained messages for new subscribers

**Standards referenced:** MQTT v3.1.1 / v5.0 (OASIS), ISO 29100, AWS IoT Core, Google Cloud IoT architecture patterns

---

## Branża 24 — Big Data / Data Lakes

### Key Document: Data Lake Architecture Design

**Recommended layers (industry consensus — Microsoft, Databricks, GeeksforGeeks):**
1. **Ingestion Layer** — batch (ETL/ELT), real-time streaming (Kafka, Kinesis), CDC (Change Data Capture)
2. **Storage Layer** — raw format, schema-on-read, structured + semi-structured + unstructured; tiered storage (hot/warm/cold)
3. **Processing Layer** — Spark, MapReduce, dbt for transformations; orchestration (Airflow, Prefect, Dagster)
4. **Governance Layer** — metadata management, data lineage, data catalog (Azure Purview, Collibra), quality monitoring
5. **Security Layer** — encryption at rest + in transit, RBAC, audit trails
6. **Consumption Layer** — BI tools, ML pipelines, analytics dashboards

**Data organization best practices:**
- Folder structure: Raw → Processed → Curated (medallion architecture: Bronze → Silver → Gold)
- Domain-driven design — organize around business capabilities
- Naming conventions: consistent, hierarchical, business-function aligned
- Partitioning by date/region for query performance

**Pipeline architecture patterns:**
- ETL vs ELT vs Zero-ETL comparison
- Event sourcing: immutable log as source of truth
- 5–7 layer modern data stack
- Monitoring touchpoints built in from start (not afterthought)

**Anti-pattern:** "Data Swamp" — unmanaged data lake without governance = unusable

**Standards referenced:** AWS Well-Architected Framework (data pillar), Azure Data Lake Storage Gen2 best practices, Apache Spark/Kafka ecosystem, GDPR data residency requirements

---

## Branża 25 — ITSM (IT Service Management)

### Key Document: Incident Record / Service Catalog

*(Research from previous session — ITIL 4 deep dive)*

**ITIL 4 — 34 practices across 3 groups:**
- General management (10): strategy, governance, risk, change enablement
- Service management (17): incident, problem, change, service request, service design, SLA, catalog
- Technical management (7): deployment, release, infrastructure, configuration

**Incident Management flow:**
Detection → Logging → Categorization → Prioritization → Investigation → Escalation (if needed) → Resolution → Closure

**Priority Matrix:** Impact × Urgency = Priority (P1–P4)
| | High Urgency | Low Urgency |
|---|---|---|
| **High Impact** | P1 (Critical) | P2 (High) |
| **Low Impact** | P3 (Medium) | P4 (Low) |

**SLA targets by priority:**
- P1: Acknowledge 15 min, resolve 4 hrs
- P2: Acknowledge 1 hr, resolve 8 hrs  
- P3: Acknowledge 4 hrs, resolve 24 hrs
- P4: Acknowledge 8 hrs, resolve 72 hrs

**Change Management:** RFC → CAB Review → Approval → Implementation → Post-Implementation Review. Emergency changes bypass CAB with expedited approval.

**Key metrics:** MTTR (Mean Time To Repair), MTTA (Mean Time To Acknowledge), SLA compliance %, change success rate, incident recurrence rate

**Standards referenced:** ITIL 4 Framework, ISO 20000 (IT Service Management), COBIT 2019, ISO 22301 (Business Continuity)

---

## Branża 26 — Business Analysis

### Key Document: Business Requirements Document (BRD) / Requirements Traceability Matrix

**BABOK v3 — 6 Knowledge Areas relevant to documentation:**
1. Business Analysis Planning & Monitoring
2. Elicitation & Collaboration  
3. Requirements Life Cycle Management (trace, maintain, prioritize, approve)
4. Requirements Analysis & Design Definition
5. Solution Assessment & Validation
6. Stakeholder Analysis

**Requirements Traceability (BABOK core concept):**
- Forward traceability: Business Need → Requirement → Deliverable
- Backward traceability: Deliverable → Requirement → Business Need
- Every requirement must have unique ID + structured attributes
- Traceability Repository recommended for large projects
- Matrix method suitable for < 200 requirements; tooling needed beyond that

**BRD recommended sections:**
1. Executive Summary & Business Case
2. Project Scope & Boundaries
3. Stakeholder Analysis
4. Business Requirements (functional)
5. Non-Functional Requirements (performance, security, usability)
6. Business Rules
7. Use Cases & Scenarios (Actor + preconditions + steps + postconditions + exceptions)
8. Data Requirements & Data Dictionary
9. Interface Requirements
10. Requirements Traceability Matrix
11. Assumptions, Constraints, Risks
12. Acceptance Criteria

**Requirements quality criteria (BABOK):** Atomic, Consistent, Feasible, Independent, Precise, Unambiguous — each requirement verifiable with Yes/No

**Standards referenced:** BABOK v3 (IIBA), CMMI, ISO 9001, IEEE 830 (SRS), UML for modeling

---

## Branża 27 — Systems Integration

### Key Document: Integration Architecture Document / Interface Specification

**Enterprise Integration Patterns (EIP) — Hohpe & Woolf (65 patterns in 9 categories):**
1. **Messaging Channels** — how systems connect
2. **Message Construction** — format, envelope, correlation
3. **Message Routing** — content-based router, splitter, aggregator, filter
4. **Message Transformation** — translator, normalizer, canonical data model
5. **Messaging Systems** — message broker, publish-subscribe, dead letter channel
6. **System Management** — monitoring, logging, testing
7. **Conversation Patterns** (EIP 2.0) — stateful exchanges, request-reply, handshake

**Integration architecture viewpoints (6 levels):**
1. Scope of enterprise integration
2. Hierarchy of patterns
3. Application integration patterns
4. Horizontal integration of system layers
5. Stateless vs stateful integration
6. Integration security

**Modern relevance:** Same patterns apply to microservices, serverless, cloud-native architectures. Service Meshes, Event Buses, API Gateways are pattern implementations.

**Interface Specification recommended sections:**
1. Integration Overview — systems involved, business context
2. Architecture Diagram — using EIP icon notation ("GregorGrams")
3. Data Flow Description — sequence diagrams, message routing logic
4. Message Formats — schemas (JSON/XML/Protobuf), versioning strategy
5. API Contracts — OpenAPI/Swagger specs, authentication (OAuth2, mTLS)
6. Error Handling — dead letter queues, retry policies, circuit breakers
7. Security — transport encryption, authorization, audit logging
8. Monitoring & Observability — correlation IDs, distributed tracing, health checks
9. SLA & Performance Targets — latency, throughput, availability
10. Testing Strategy — integration tests, contract tests, chaos testing

**Standards referenced:** Enterprise Integration Patterns (Hohpe & Woolf), Apache Camel EIP catalog, OpenAPI 3.x, OAuth 2.0, gRPC/Protobuf, OWASP API Security Top 10

---

## Cross-Industry Findings

### Shared Document Standards (applicable across all 9 industries):
- **Version control** on all living documents (change log at top)
- **Stakeholder sign-off section** in all major specs
- **Assumptions & Risks** section is universal
- **Glossary/terminology** section prevents cross-team miscommunication
- **Acceptance criteria** defined before development begins

### Standards Mapping Summary:
| Standard | Applicable Industries |
|---|---|
| IEEE 830 | 19 (PM), 26 (BA), 27 (SI) |
| ITIL 4 | 25 (ITSM) |
| OWASP | 22 (Blockchain), 27 (SI) |
| ISO 27001 | 22, 23, 24, 25, 27 |
| GDPR | 24 (Big Data), 26 (BA) |
| COBIT | 25 (ITSM), 19 (PM governance) |
| AWS Well-Architected | 23 (IoT), 24 (Big Data) |
| EIP (Hohpe & Woolf) | 27 (SI) |
| Agile/Scrum | 19, 20, 21 |
| BABOK v3 | 26 (BA) |
| MQTT (OASIS) | 23 (IoT) |
| TOGAF | 27 (SI), 24 (Big Data) |
| ISO 22301 | 25 (ITSM — BCP) |
| ASD-STE100 | 20 (Technical Writing) |
