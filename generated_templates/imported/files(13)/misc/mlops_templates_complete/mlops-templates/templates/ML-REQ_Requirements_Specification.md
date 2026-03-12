# ML-REQ: ML Requirements Specification
## Specyfikacja Wymagań Systemu ML/AI

**Wersja szablonu:** 2.0  
**Standard:** IEEE 830, CRISP-DM, EU AI Act  
**Priorytet:** CRITICAL  
**Kod dokumentu:** ML-REQ

---

## METADANE DOKUMENTU

```yaml
document_id: ML-REQ-[PROJECT_ID]-[VERSION]
version: 1.0.0
status: [DRAFT|REVIEW|APPROVED|ACTIVE|SUPERSEDED|ARCHIVED]
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
created_date: YYYY-MM-DD
last_updated: YYYY-MM-DD
next_review: YYYY-MM-DD
author: [Name]
owner: [Product Owner]
stakeholders: [List]
classification: [INTERNAL|CONFIDENTIAL]

# Lifecycle
lifecycle:
  created_trigger: "Project initiation approved"
  valid_from: "Approval date"
  valid_until: "Project completion or major pivot"
  retention: "Project lifetime + 10 years"
```

---

## SEKCJA 1: WPROWADZENIE

### 1.1 Cel Dokumentu

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-PSD (Problem Statement) → context
├── INPUT: ML-FEA (Feasibility Assessment) → constraints
├── INPUT: ML-VIS (Vision Document) → strategic goals
├── OUTPUT: → Wszystkie kolejne dokumenty projektowe
└── TRIGGER: Zatwierdzenie inicjuje fazę Design
```

**Cel:**
```
[Opisz cel tego dokumentu wymagań]
```

**Zakres:**
```
[Co jest IN scope / OUT of scope]
```

### 1.2 Definicje i Skróty

| Termin | Definicja |
|--------|-----------|
| | |

### 1.3 Referencje

| Dokument | ID | Status |
|----------|-----|--------|
| Problem Statement | ML-PSD-XXX | |
| Feasibility Assessment | ML-FEA-XXX | |
| Stakeholder Analysis | ML-STA-XXX | |

---

## SEKCJA 2: OPIS OGÓLNY SYSTEMU

### 2.1 Perspektywa Produktu

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-PSD → business context
├── INPUT: ML-UCN → use cases
├── OUTPUT: → ML-ARC (system boundaries)
├── OUTPUT: → ML-RRC (regulatory scope)
└── WPŁYWA NA: Klasyfikację EU AI Act risk category
```

**Kontekst systemu:**
```
[Diagram kontekstowy lub opis]
```

**Integracje:**
| System | Typ integracji | Dane wymieniane | SLA |
|--------|----------------|-----------------|-----|
| | | | |

### 2.2 Funkcje Produktu (High-Level)

| ID | Funkcja | Priorytet | MVP |
|----|---------|-----------|-----|
| F-001 | | HIGH/MEDIUM/LOW | Y/N |
| F-002 | | | |

### 2.3 Charakterystyka Użytkowników

```
ZALEŻNOŚCI:
├── INPUT: ML-STA (Stakeholder Analysis)
├── OUTPUT: → ML-ONB (onboarding requirements)
├── OUTPUT: → ML-EUA (human oversight requirements)
└── EU AI ACT: Art. 14 - user competence requirements
```

| Typ użytkownika | Opis | Kompetencje | Dostęp |
|-----------------|------|-------------|--------|
| End User | | | |
| Operator | | | |
| Admin | | | |
| Auditor | | | |

### 2.4 Ograniczenia

| Ograniczenie | Typ | Źródło | Impact |
|--------------|-----|--------|--------|
| | Technical | | |
| | Regulatory | EU AI Act | |
| | Business | | |
| | Resource | | |

### 2.5 Założenia i Zależności

| Założenie/Zależność | Typ | Ryzyko jeśli fałszywe |
|---------------------|-----|----------------------|
| | Assumption | |
| | Dependency | |

---

## SEKCJA 3: WYMAGANIA FUNKCJONALNE ML

### 3.1 Model Requirements

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-PSD → problem to solve
├── INPUT: ML-FEA → feasibility constraints
├── OUTPUT: → ML-ARC (architecture decisions)
├── OUTPUT: → ML-MSL (model selection criteria)
├── OUTPUT: → ML-SMC (success metrics definition)
└── WARUNEK: Każde wymaganie musi być testowalne
```

#### FR-ML-001: Typ Problemu ML

| Parametr | Wartość | Uzasadnienie |
|----------|---------|--------------|
| Problem type | [ ] Classification / [ ] Regression / [ ] Clustering / [ ] Ranking / [ ] Generation | |
| Output type | [ ] Binary / [ ] Multi-class / [ ] Multi-label / [ ] Continuous / [ ] Sequence | |
| Learning type | [ ] Supervised / [ ] Unsupervised / [ ] Semi-supervised / [ ] RL | |

#### FR-ML-002: Wymagania Dokładności

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-SMC (Success Metrics Criteria)
├── OUTPUT: → ML-MTP (testing thresholds)
├── OUTPUT: → ML-MDC (performance section)
└── LIFECYCLE: Reviewed gdy metryki nie spełnione
```

| Metryka | Minimum | Target | Stretch | Rationale |
|---------|---------|--------|---------|-----------|
| Accuracy | | | | |
| Precision | | | | |
| Recall | | | | |
| F1-Score | | | | |
| AUC-ROC | | | | |
| MAE/RMSE | | | | |
| Custom: | | | | |

#### FR-ML-003: Wymagania Fairness (CRITICAL dla HIGH-RISK)

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-FBT (Fairness & Bias Testing)
├── OUTPUT: → ML-EUA (compliance evidence)
└── EU AI ACT: Art. 10 - bias requirements
```

| Protected Group | Fairness Metric | Threshold | Priority |
|-----------------|-----------------|-----------|----------|
| | Demographic Parity | 0.8-1.2 | MUST |
| | Equalized Odds | | SHOULD |
| | Equal Opportunity | | SHOULD |

#### FR-ML-004: Wymagania Explainability

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-EXP-DOC (Explainability Documentation)
├── OUTPUT: → ML-MSL (interpretability as selection criteria)
└── EU AI ACT: Art. 13 - transparency requirements
```

| Requirement | Level | Method | Audience |
|-------------|-------|--------|----------|
| Global explanations | MUST/SHOULD/MAY | | Technical |
| Local explanations | | | Business |
| Feature importance | | | Audit |
| Decision rules | | | End-user |

### 3.2 Prediction/Inference Requirements

#### FR-INF-001: Real-time vs Batch

| Mode | Required | Volume | Frequency |
|------|----------|--------|-----------|
| Real-time | [ ] | requests/sec | |
| Batch | [ ] | records/run | |
| Streaming | [ ] | events/sec | |

#### FR-INF-002: Input Requirements

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-DRQ (Data Requirements)
├── OUTPUT: → ML-FEP (Feature Engineering Plan)
└── OUTPUT: → ML-API (API specification)
```

| Input Field | Type | Format | Required | Validation |
|-------------|------|--------|----------|------------|
| | | | Y/N | |

#### FR-INF-003: Output Requirements

| Output | Type | Format | Latency | SLA |
|--------|------|--------|---------|-----|
| Prediction | | | | |
| Confidence | | | | |
| Explanation | | | | |

---

## SEKCJA 4: WYMAGANIA NIEFUNKCJONALNE

### 4.1 Wydajność (Performance)

```
ZALEŻNOŚCI SEKCJI:
├── OUTPUT: → ML-MSA (serving architecture)
├── OUTPUT: → ML-INF (inference architecture)
├── OUTPUT: → ML-CAP (capacity planning)
└── TRIGGER: Niespełnienie → performance optimization
```

#### NFR-PERF-001: Latency Requirements

| Percentile | Inference | End-to-end | Priority |
|------------|-----------|------------|----------|
| P50 | ms | ms | MUST |
| P95 | ms | ms | MUST |
| P99 | ms | ms | SHOULD |

#### NFR-PERF-002: Throughput Requirements

| Metric | Normal | Peak | Burst |
|--------|--------|------|-------|
| Requests/second | | | |
| Records/batch | | | |

### 4.2 Skalowalność (Scalability)

#### NFR-SCALE-001: Scaling Requirements

| Dimension | Current | 1 Year | 3 Years |
|-----------|---------|--------|---------|
| Data volume | | | |
| Request volume | | | |
| Model complexity | | | |

#### NFR-SCALE-002: Scaling Strategy

| Type | Supported | Trigger |
|------|-----------|---------|
| Horizontal | [ ] | |
| Vertical | [ ] | |
| Auto-scaling | [ ] | |

### 4.3 Dostępność (Availability)

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-DRP (Disaster Recovery Plan)
├── OUTPUT: → ML-BCP (Business Continuity Plan)
├── OUTPUT: → ML-SLA (SLA definition)
└── TRIGGER: SLA breach → incident
```

| Metric | Requirement | Measurement |
|--------|-------------|-------------|
| Uptime | 99.X% | Monthly |
| MTTR | hours | |
| MTBF | hours | |

### 4.4 Niezawodność (Reliability)

#### NFR-REL-001: Failure Handling

| Failure Type | Handling | Fallback |
|--------------|----------|----------|
| Model unavailable | | |
| Invalid input | | |
| Timeout | | |

### 4.5 Bezpieczeństwo (Security)

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-MSA (security architecture)
├── OUTPUT: → ML-EUA (cybersecurity - Art. 15.5)
└── COMPLIANCE: GDPR, industry standards
```

#### NFR-SEC-001: Data Security

| Requirement | Implementation | Priority |
|-------------|----------------|----------|
| Encryption at rest | | MUST |
| Encryption in transit | | MUST |
| Access control | | MUST |
| Audit logging | | MUST |

#### NFR-SEC-002: Model Security

| Threat | Protection | Status |
|--------|------------|--------|
| Model extraction | | |
| Data poisoning | | |
| Adversarial attacks | | |

### 4.6 Compliance Requirements

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-RRC (Regulatory Requirements Checklist)
├── OUTPUT: → ML-EUA (EU AI Act Compliance)
└── TRIGGER: Regulation change → requirement update
```

| Regulation | Applicable | Requirements | Priority |
|------------|------------|--------------|----------|
| EU AI Act | [ ] | | MUST |
| GDPR | [ ] | | MUST |
| Industry-specific | [ ] | | |

---

## SEKCJA 5: WYMAGANIA DANYCH (→ ML-DRQ)

### 5.1 Data Sources

```
ZALEŻNOŚCI SEKCJI:
├── OUTPUT: → ML-DRQ (Data Requirements Document)
├── OUTPUT: → ML-DPC (Data Preparation Code)
├── OUTPUT: → ML-DDC (Dataset Documentation)
└── TRIGGER: Nowe źródło danych → requirements update
```

| Source | Type | Volume | Frequency | Owner |
|--------|------|--------|-----------|-------|
| | | | | |

### 5.2 Data Quality Requirements

| Dimension | Requirement | Measurement |
|-----------|-------------|-------------|
| Completeness | | |
| Accuracy | | |
| Consistency | | |
| Timeliness | | |

### 5.3 Data Governance

| Requirement | Implementation | Responsible |
|-------------|----------------|-------------|
| Data lineage | | |
| Data versioning | | |
| Access control | | |
| Retention policy | | |

---

## SEKCJA 6: WYMAGANIA OPERACYJNE

### 6.1 Monitoring Requirements

```
ZALEŻNOŚCI SEKCJI:
├── OUTPUT: → ML-MMG (Monitoring Guide)
├── OUTPUT: → ML-PMT (Performance Metrics)
├── OUTPUT: → ML-ALR (Alert Rules)
└── EU AI ACT: Art. 72 - post-market monitoring
```

| Category | Metrics | Frequency | Alerting |
|----------|---------|-----------|----------|
| Model performance | | | |
| Data drift | | | |
| System health | | | |
| Business KPIs | | | |

### 6.2 Retraining Requirements

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-RTS (Retraining Schedule)
├── OUTPUT: → ML-MDD (Model Drift Detection)
└── TRIGGER: Drift/performance → retraining evaluation
```

| Trigger | Condition | Action |
|---------|-----------|--------|
| Scheduled | | |
| Performance-based | | |
| Drift-based | | |
| Manual | | |

### 6.3 Incident Management Requirements

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-MFR (Model Failure Recovery)
├── OUTPUT: → ML-RBP (Rollback Procedure)
└── EU AI ACT: Art. 73 - incident reporting
```

| Severity | Response Time | Resolution Time |
|----------|---------------|-----------------|
| P1 - Critical | | |
| P2 - High | | |
| P3 - Medium | | |
| P4 - Low | | |

---

## SEKCJA 7: WYMAGANIA INTEGRACYJNE

### 7.1 API Requirements

```
ZALEŻNOŚCI SEKCJI:
├── OUTPUT: → ML-API (API Reference)
├── OUTPUT: → ML-MSA (serving endpoints)
└── OUTPUT: → Integration testing scope
```

| Endpoint | Method | Input | Output | Auth |
|----------|--------|-------|--------|------|
| /predict | | | | |
| /explain | | | | |
| /health | | | | |

### 7.2 Integration Points

| System | Direction | Protocol | Data Format |
|--------|-----------|----------|-------------|
| | IN/OUT/BOTH | | |

---

## SEKCJA 8: TRACEABILITY MATRIX

### 8.1 Requirements to Design

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-ARC traceability
├── OUTPUT: → ML-MTP test coverage
└── AUDIT: Provides compliance evidence
```

| Req ID | Design Doc | Section | Status |
|--------|------------|---------|--------|
| FR-ML-001 | ML-ARC | 3.1 | |
| FR-ML-002 | ML-SMC | 2.1 | |
| | | | |

### 8.2 Requirements to Tests

| Req ID | Test Case | Test Type | Priority |
|--------|-----------|-----------|----------|
| FR-ML-002 | TC-001 | Unit | MUST |
| | | | |

---

## SEKCJA 9: AKCEPTACJA I WALIDACJA

### 9.1 Acceptance Criteria

| Requirement | Criterion | Verification Method |
|-------------|-----------|---------------------|
| | | |

### 9.2 Sign-off Requirements

| Stakeholder | Role | Required |
|-------------|------|----------|
| Product Owner | Business approval | [ ] |
| Tech Lead | Technical approval | [ ] |
| Data Science Lead | ML approval | [ ] |
| Compliance | Regulatory approval | [ ] |

---

## LIFECYCLE SUMMARY

```yaml
KIEDY DOKUMENT SIĘ POJAWIA:
  trigger: "Project initiation approved (ML-PSD approved)"
  prerequisites:
    - ML-PSD (Problem Statement) approved
    - ML-FEA (Feasibility Assessment) positive
    - Stakeholder buy-in confirmed
    
KIEDY DOKUMENT ZNIKA/WYGASA:
  triggers:
    - Project cancelled
    - Major pivot requiring new requirements
    - Project completed and archived
  retention: "Project lifetime + 10 years"
  
KIEDY OBOWIĄZUJE:
  conditions:
    - Active project development
    - Production system based on these requirements
    - Testing against these requirements
    
KIEDY NIE OBOWIĄZUJE:
  conditions:
    - Superseded by new version
    - Project cancelled
    - System decommissioned
    
AKTUALIZACJE WYMAGANE GDY:
  - Scope change requested
  - Regulatory requirements change
  - Technical feasibility assessment changes
  - Business priorities shift
  - Stakeholder requirements change
  
DOCUMENTS THAT DEPEND ON THIS:
  - ML-ARC (Architecture) - REQUIRES ML-REQ
  - ML-DRQ (Data Requirements) - REQUIRES ML-REQ
  - ML-FEP (Feature Engineering) - REQUIRES ML-REQ
  - ML-SMC (Success Metrics) - REQUIRES ML-REQ
  - ML-MTP (Testing Plan) - REQUIRES ML-REQ
  - ML-RRC (Regulatory Checklist) - REQUIRES ML-REQ
```

---

## APPENDIX

### A. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | | | Initial version |

### B. Approval History

| Role | Name | Date | Signature |
|------|------|------|-----------|
| | | | |

---

**END OF TEMPLATE**
