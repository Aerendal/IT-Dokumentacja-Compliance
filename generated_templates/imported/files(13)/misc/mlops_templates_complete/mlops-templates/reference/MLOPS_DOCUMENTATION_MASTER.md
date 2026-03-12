---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MLOps Documentation Master Reference
## Kompletny System Szablonów Dokumentacji ML/AI

**Wersja:** 2.0  
**Data:** 2025-01-31  
**Standard:** EU AI Act, ISO/IEC 42001, NIST AI RMF

---

## SPIS TREŚCI

1. [Przegląd Systemu](#1-przegląd-systemu)
2. [Mapa Faz i Dokumentów](#2-mapa-faz-i-dokumentów)
3. [Macierz Zależności](#3-macierz-zależności)
4. [Lifecycle Dokumentów](#4-lifecycle-dokumentów)
5. [Triggery i Warunki](#5-triggery-i-warunki)
6. [Szablony Dokumentów](#6-szablony-dokumentów)

---

## 1. PRZEGLĄD SYSTEMU

### 1.1 Architektura Dokumentacji

```
┌─────────────────────────────────────────────────────────────────────┐
│                    GOVERNANCE LAYER                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                  │
│  │ AI Ethics   │  │ Compliance  │  │ Risk        │                  │
│  │ Framework   │  │ Framework   │  │ Register    │                  │
│  └─────────────┘  └─────────────┘  └─────────────┘                  │
└─────────────────────────────────────────────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    LIFECYCLE LAYER                                   │
│  CONCEPT → REQUIREMENTS → DESIGN → IMPLEMENT → TEST → DEPLOY        │
│     ▼           ▼            ▼         ▼         ▼       ▼          │
│  [PSD]      [REQ,DRQ]    [ARC,FEP]   [MTC]    [MTP]   [MSA]        │
└─────────────────────────────────────────────────────────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    OPERATIONS LAYER                                  │
│  MONITOR → INCIDENT → MAINTAIN → CHANGE → CAPACITY                  │
│     ▼          ▼          ▼         ▼         ▼                     │
│  [MMG,MDD]  [MFR,RBP]   [RTS]     [RFC]    [CAP]                   │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Kategorie Dokumentów

| Kategoria | Prefiks | Opis | Przykłady |
|-----------|---------|------|-----------|
| **SPEC** | ML-*-SPEC | Specyfikacje | REQ, DRQ, FEA |
| **ARCH** | ML-*-ARC | Architektury | ARC, MSA, FEP |
| **CODE** | ML-*-CODE | Kod/Implementacje | DPC, FEC, MTC |
| **TEST** | ML-*-TEST | Testy/Walidacje | MTP, FBT, CVS |
| **CARD** | ML-*-CARD | Karty (Model/Data) | MDC, DDC |
| **RUNBOOK** | ML-*-RUN | Procedury operacyjne | MMG, MFR, RBP |
| **AUDIT** | ML-*-AUD | Dokumenty audytowe | EUA, AET, ACL |
| **PLAN** | ML-*-PLAN | Plany | TLN, RSA, RTS |
| **REPORT** | ML-*-RPT | Raporty | PRR, BIR, MRE |

### 1.3 Priorytety Dokumentów

| Priorytet | Znaczenie | Liczba | % |
|-----------|-----------|--------|---|
| **CRITICAL** | Wymagane do uruchomienia/compliance | 23 | 19% |
| **HIGH** | Wymagane do produkcji | 58 | 47% |
| **MEDIUM** | Zalecane dla mature operations | 40 | 32% |
| **LOW** | Opcjonalne/Nice-to-have | 3 | 2% |

---

## 2. MAPA FAZ I DOKUMENTÓW

### Faza 1: KONCEPCJA I WIZJA

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-PSD | Problem Statement Document | CRITICAL | - | REQ, FEA, UCN |
| ML-FEA | Feasibility Assessment | CRITICAL | PSD | REQ, ARC |
| ML-UCN | Use Case Narrative | HIGH | PSD | REQ, DRQ |
| ML-VIS | ML Vision Document | MEDIUM | - | PSD, STR |

**Triggery wejścia:** Nowa inicjatywa ML, Business Request
**Triggery wyjścia:** Approval Gate → Faza 2
**Okres ważności:** Do zakończenia projektu lub anulowania

---

### Faza 2: ANALIZA WYMAGAŃ

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-REQ | ML Requirements Specification | CRITICAL | PSD, FEA, UCN | ARC, DRQ, FEP |
| ML-DRQ | Data Requirements Document | CRITICAL | REQ | DPC, DDC, FEP |
| ML-SMC | Success Metrics Criteria | HIGH | REQ | MTP, PRR |
| ML-RRC | Regulatory Requirements Checklist | HIGH | REQ | EUA, AET, RCC |
| ML-STA | Stakeholder Analysis | MEDIUM | PSD | SMC, RRC |

**Triggery wejścia:** Zatwierdzenie Fazy 1
**Triggery wyjścia:** Requirements Review Gate → Faza 3
**Warunkowe:** RRC wymagane dla HIGH-RISK AI (EU AI Act)

---

### Faza 3: PROJEKT / DESIGN

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-ARC | ML Architecture Document | CRITICAL | REQ, FEA | MSA, FEP, MTC |
| ML-FEP | Feature Engineering Plan | CRITICAL | REQ, DRQ, ARC | FEC, DDC |
| ML-MSL | Model Selection Document | HIGH | ARC, FEP | MTC, HPO |
| ML-HPO | Hyperparameter Strategy | HIGH | MSL | MTC, EXP |
| ML-DPD | Data Pipeline Design | HIGH | DRQ, ARC | DPC, FEP |
| ML-INF | Inference Architecture | HIGH | ARC, MSL | MSA, PDG |

**Triggery wejścia:** Zatwierdzenie Requirements
**Triggery wyjścia:** Design Review Gate → Faza 4
**Warunkowe:** INF wymagane dla real-time serving

---

### Faza 4: PLANOWANIE

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-TLN | Project Timeline | HIGH | ARC, FEP | wszystkie implementacje |
| ML-EXS | Experiment Tracking Setup | HIGH | HPO | EXP, MTC |
| ML-RSA | Resource Allocation Plan | HIGH | TLN, ARC | wszystkie implementacje |
| ML-RIS | Risk Assessment | HIGH | FEA, ARC | wszystkie fazy |

**Triggery wejścia:** Zatwierdzenie Design
**Triggery wyjścia:** Planning Review → Faza 5

---

### Faza 5: IMPLEMENTACJA

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-DPC | Data Preparation Code | CRITICAL | DRQ, DPD | FEC, MTC |
| ML-FEC | Feature Engineering Code | CRITICAL | FEP, DPC | MTC, FES |
| ML-MTC | Model Training Code | CRITICAL | FEC, MSL, HPO | TSE, MDC |
| ML-FES | Feature Store Implementation | HIGH | FEC, FEP | MTC, MSA |
| ML-EXP | Experiments Log | HIGH | EXS, MTC | MDC, MRE |

**Triggery wejścia:** Zatwierdzenie planowania
**Triggery wyjścia:** Code Review Gate → Faza 6
**Lifecycle:** Wersjonowane (Git), aktualizowane przy zmianach

---

### Faza 6: TESTOWANIE / QA

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-MTP | Model Testing Plan | CRITICAL | MTC, SMC | TSE, CVS, ADV |
| ML-TSE | Test Set Evaluation | HIGH | MTP, MTC | MDC, PRR |
| ML-CVS | Cross-Validation Strategy | HIGH | MTP | TSE, EXP |
| ML-ADV | Adversarial Testing | HIGH | MTP | FBT, MDC |
| ML-PFT | Performance Testing | HIGH | MTP, INF | MSA, PDG |

**Triggery wejścia:** Ukończenie implementacji
**Triggery wyjścia:** Testing Gate (metrics threshold) → Faza 7
**Warunkowe:** ADV wymagane dla HIGH-RISK AI

---

### Faza 7: BEZPIECZEŃSTWO / COMPLIANCE

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-EXP-DOC | Explainability Documentation | CRITICAL | MTC, TSE | MDC, EUA |
| ML-AET | AI Ethics Assessment | CRITICAL | RRC, TSE | EUA, FBT |
| ML-FBT | Fairness & Bias Testing | CRITICAL | MTC, ADV, AET | MDC, EUA, BIM |
| ML-BIM | Bias Mitigation Plan | HIGH | FBT | MTC (retrain), MDC |
| ML-EUA | EU AI Act Compliance | CRITICAL | AET, FBT, EXP-DOC | PDG, AUD |
| ML-MDC | Model Card | CRITICAL | MTC, TSE, FBT, EXP-DOC | MSA, PDG |

**Triggery wejścia:** Ukończenie testowania
**Triggery wyjścia:** Compliance Gate → Faza 8
**CRITICAL dla HIGH-RISK AI:** Wszystkie dokumenty wymagane
**EU AI Act Timeline:** Pełna zgodność od Aug 2026

---

### Faza 8: WDROŻENIE / DEPLOYMENT

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-MSA | Model Serving Architecture | CRITICAL | ARC, INF, MDC | PDG, MMG |
| ML-CON | Containerization Guide | HIGH | MSA, MTC | PDG |
| ML-ABT | A/B Testing Strategy | HIGH | MSA, SMC | PDG, PRR |
| ML-PDG | Production Deployment Guide | CRITICAL | MSA, CON, EUA | MMG, MFR |
| ML-CAN | Canary Deployment Plan | MEDIUM | PDG | ABT |

**Triggery wejścia:** Compliance Gate passed
**Triggery wyjścia:** Deployment Success → Faza 9
**Rollback Trigger:** Metrics degradation → RBP

---

### Faza 9: OPERACJE / MAINTENANCE

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-MMG | Monitoring Guide | CRITICAL | MSA, PDG | MDD, MFR |
| ML-MDD | Model Drift Detection | CRITICAL | MMG, SMC | RTS, MFR |
| ML-RTS | Retraining Schedule | HIGH | MDD, SMC | MTC (cycle) |
| ML-OPR | Operational Runbook | HIGH | MMG, PDG | MFR |
| ML-MAI | Maintenance Calendar | MEDIUM | RTS | wszystkie ops |

**Triggery wejścia:** Successful deployment
**Triggery ciągłe:** Drift detected → RTS, Performance degradation → MFR
**Lifecycle:** Continuous, aktualizowane przy incydentach

---

### Faza 10: INCIDENT MANAGEMENT

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-MFR | Model Failure Recovery | CRITICAL | MMG, OPR | RBP, PIR |
| ML-RBP | Rollback Procedure | CRITICAL | MFR, PDG | PIR |
| ML-PIR | Post-Incident Report | HIGH | MFR, RBP | LES, RTS |

**Triggery wejścia:** Incident detection (alert, manual report)
**Triggery wyjścia:** Incident resolved → PIR → LES
**Eskalacja:** P1 → Immediate, P2 → 4h, P3 → 24h

---

### Faza 11: MONITORING / OBSERVABILITY

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-PMT | Performance Metrics Definition | CRITICAL | SMC, MMG | MDD, PRR |
| ML-DDM | Data Drift Monitoring | HIGH | PMT, MDD | RTS, MFR |
| ML-MDM | Model Drift Monitoring | HIGH | PMT, MDD | RTS, MFR |
| ML-FMO | Feature Monitoring | HIGH | FES, PMT | DDM |
| ML-ALR | Alert Rules | HIGH | PMT | MFR, OPR |

**Triggery wejścia:** Deployment complete
**Triggery ciągłe:** Metric breach → Alert → MFR chain
**Dashboard updates:** Real-time, Reports: Daily/Weekly

---

### Faza 12: DOKUMENTACJA REFERENCYJNA

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-DOC | Model Documentation | CRITICAL | MDC, wszystkie | ONB, TRN |
| ML-DDC | Dataset Documentation | HIGH | DRQ, FEP | DOC |
| ML-API | API Reference | HIGH | MSA | DOC, ONB |
| ML-EXL | Experiments Library | MEDIUM | EXP | DOC |
| ML-REF | Reference Architecture | MEDIUM | ARC | DOC, ONB |

**Lifecycle:** Living documents, aktualizowane przy zmianach
**Review:** Quarterly lub przy major release

---

### Faza 13: SZKOLENIE / ONBOARDING

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-ONB | ML Engineer Onboarding | HIGH | DOC, REF | - |
| ML-TRN | Framework Training | HIGH | DOC | - |
| ML-TOO | MLOps Tools Training | MEDIUM | DOC | - |
| ML-BPT | Best Practices Training | MEDIUM | BPR | - |

**Triggery wejścia:** New team member, Tool adoption
**Lifecycle:** Updated przy major changes

---

### Faza 14: KOMUNIKACJA STAKEHOLDERS

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-PRR | Performance Report | HIGH | PMT, TSE | BIR |
| ML-BIR | Business Impact Report | HIGH | PRR, SMC | - |
| ML-STU | Status Update | MEDIUM | wszystkie ops | - |
| ML-DSH | Dashboard Specification | MEDIUM | PMT | PRR |

**Triggery:** Weekly/Monthly/Quarterly cadence
**Audience:** Executive, Technical, Business

---

### Faza 15: KNOWLEDGE MANAGEMENT

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-BPR | Best Practices | HIGH | wszystkie | TRN, ONB |
| ML-PAT | Design Patterns | HIGH | ARC, wszystkie | ONB |
| ML-FLB | Feature Library | MEDIUM | FEP, FES | FEC |
| ML-ISS | Common Issues & Solutions | MEDIUM | PIR, LES | OPR |
| ML-LES | Lessons Learned | MEDIUM | PIR, MRE | BPR |

**Lifecycle:** Continuous improvement
**Review:** Po każdym major incident/project

---

### Faza 16: POSTMORTEM / RETROSPEKTYWA

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-MRE | Model Retrospective | HIGH | EXP, PRR | LES, BPR |
| ML-PRE | Project Retrospective | HIGH | wszystkie | LES |
| ML-IMP | Improvement Recommendations | HIGH | MRE, PRE | BPR, PAT |
| ML-TAR | Tool Adoption Review | MEDIUM | TOO | IMP |

**Triggery:** Project completion, Major release, Incident
**Output:** Action items → Next iteration

---

### Faza 17: BUDŻETOWANIE / COST MANAGEMENT

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-BUD | Budget Proposal | HIGH | RSA, TLN | wszystkie |
| ML-CBA | Cost-Benefit Analysis | HIGH | FEA, BUD | ROI |
| ML-TCO | Total Cost of Ownership | HIGH | BUD, RSA | CBA |
| ML-CPX | CapEx/OpEx Planning | MEDIUM | TCO | BUD |
| ML-ROI | ROI Projections | HIGH | CBA | BIR |
| ML-CTR | Cost Tracking Report | HIGH | wszystkie ops | BIR |

**Lifecycle:** Initial planning, quarterly review
**Triggers:** Budget cycle, Cost overrun alert

---

### Faza 18: VENDOR / PROCUREMENT

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-RFP | Request for Proposal | HIGH | REQ, BUD | VEM |
| ML-RFI | Request for Information | MEDIUM | REQ | RFP |
| ML-VEM | Vendor Evaluation Matrix | HIGH | RFP | SLA |
| ML-COT | Contract Template | HIGH | VEM | SLA |
| ML-SLA | SLA Agreement | HIGH | VEM, COT | MMG, MFR |
| ML-VRA | Vendor Risk Assessment | HIGH | VEM | RIS |
| ML-PCH | Procurement Checklist | MEDIUM | wszystkie | - |

**Triggers:** Tool selection, Service procurement
**Lifecycle:** Per vendor engagement

---

### Faza 19: GOVERNANCE / COMPLIANCE AUDITING

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-ACL | Audit Checklist | HIGH | EUA, wszystkie | CRP |
| ML-CRP | Compliance Report | HIGH | ACL | - |
| ML-PRV | Policy Review Record | MEDIUM | CRP | ACL |
| ML-CER | Certification Documentation | HIGH | CRP, EUA | - |
| ML-RRG | Risk Register | HIGH | RIS, wszystkie | ACL |
| ML-CTM | Control Matrix | HIGH | ACL | CRP |
| ML-ATL | Audit Trail Log | CRITICAL | wszystkie | ACL, CRP |

**Triggers:** Scheduled audit (annual), Regulatory change, Major incident
**EU AI Act:** Annual compliance audit required

---

### Faza 20: DECOMMISSIONING / END-OF-LIFE

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-RET | System Retirement Plan | HIGH | wszystkie | DMI, ARS |
| ML-DMI | Data Migration Strategy | HIGH | RET | ARS |
| ML-ARS | Archive Strategy | HIGH | RET, DMI | HRP |
| ML-SCP | Sunset Communication Plan | HIGH | RET | - |
| ML-DIA | Dependency Impact Analysis | HIGH | RET | SCP |
| ML-DCH | Decommissioning Checklist | HIGH | wszystkie | - |
| ML-HRP | Historical Data Retention Policy | HIGH | ARS | - |

**Triggers:** Model obsolescence, Replacement model ready, Regulatory requirement
**Timeline:** 30-90 days notice

---

### Faza 21: DISASTER RECOVERY / BCP

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-DRP | Disaster Recovery Plan | CRITICAL | MSA, wszystkie | FAI |
| ML-BCP | Business Continuity Plan | CRITICAL | DRP | FAI |
| ML-RPO | RPO Definition | CRITICAL | DRP | FAI |
| ML-RTO | RTO Definition | CRITICAL | DRP | FAI |
| ML-FAI | Failover Procedures | HIGH | DRP, RPO, RTO | DRT |
| ML-DRT | DR Test Report | HIGH | FAI | DRP (update) |
| ML-CCP | Crisis Communication Plan | HIGH | BCP | - |
| ML-BVC | Backup Verification Checklist | HIGH | DRP | DRT |

**Triggers:** DR Test schedule (quarterly), Actual disaster
**Review:** Annual or after incident

---

### Faza 22: CHANGE MANAGEMENT

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-RFC | Change Request Form | HIGH | wszystkie | CIA |
| ML-CAB | CAB Meeting Notes | HIGH | RFC | CIA, RBK |
| ML-CCL | Change Calendar | MEDIUM | RFC | - |
| ML-CIA | Change Impact Assessment | HIGH | RFC | CAB |
| ML-RBK | Rollback Plan Template | HIGH | CIA | RBP |
| ML-ECP | Emergency Change Procedure | HIGH | RFC | - |
| ML-CSC | Change Success Criteria | HIGH | RFC | - |

**Triggers:** Any production change, Configuration update
**Process:** RFC → CIA → CAB → Approve/Reject → Execute

---

### Faza 23: CAPACITY PLANNING

| Kod | Nazwa Dokumentu | Priorytet | Zależności IN | Zależności OUT |
|-----|-----------------|-----------|---------------|----------------|
| ML-CAP | Capacity Forecast Report | HIGH | PMT, wszystkie ops | GRP |
| ML-GRP | Growth Projections | HIGH | CAP, BIR | RSA |
| ML-RAP | Resource Allocation Plan | HIGH | CAP | BUD |
| ML-SCA | Scalability Assessment | HIGH | CAP, ARC | ARC (update) |
| ML-PBL | Performance Baseline | HIGH | PMT | CAP |
| ML-CTA | Capacity Threshold Alerts | HIGH | CAP | ALR |
| ML-ISG | Infrastructure Sizing Guide | MEDIUM | CAP | RSA |

**Triggers:** Quarterly review, Traffic spike, Cost optimization initiative
**Thresholds:** 70% utilization → alert, 85% → scale

---

## 3. MACIERZ ZALEŻNOŚCI

### 3.1 Zależności REQUIRES (dokument A wymaga B przed utworzeniem)

```
ML-ARC  ──REQUIRES──▶  ML-REQ
ML-FEP  ──REQUIRES──▶  ML-REQ, ML-DRQ, ML-ARC
ML-MTC  ──REQUIRES──▶  ML-FEC, ML-DPC, ML-MSL
ML-MSA  ──REQUIRES──▶  ML-ARC, ML-MDC
ML-TSE  ──REQUIRES──▶  ML-MTP, ML-MTC
ML-MDC  ──REQUIRES──▶  ML-MTC, ML-TSE, ML-FBT, ML-EXP-DOC
ML-EUA  ──REQUIRES──▶  ML-AET, ML-FBT, ML-EXP-DOC
ML-PDG  ──REQUIRES──▶  ML-MSA, ML-CON, ML-EUA
ML-MMG  ──REQUIRES──▶  ML-MSA, ML-PDG
ML-MFR  ──REQUIRES──▶  ML-MMG, ML-OPR
ML-DRP  ──REQUIRES──▶  ML-MSA, ML-MMG
```

### 3.2 Zależności UPDATES (zmiana w A wymaga aktualizacji B)

```
ML-MTC (change)  ──UPDATES──▶  ML-MDC, ML-TSE, ML-EXP
ML-FBT (new findings)  ──UPDATES──▶  ML-MDC, ML-EUA, ML-BIM
ML-MDD (drift detected)  ──UPDATES──▶  ML-RTS, ML-MFR
ML-RFC (approved)  ──UPDATES──▶  ML-CCL, ML-PDG, ML-MMG
ML-PIR (completed)  ──UPDATES──▶  ML-LES, ML-BPR, ML-OPR
```

### 3.3 Zależności TRIGGERS (A wywołuje utworzenie B)

```
ML-PSD (approved)  ──TRIGGERS──▶  ML-REQ, ML-FEA
ML-DRQ (approved)  ──TRIGGERS──▶  ML-DPC, ML-DDC
ML-MTC (completed)  ──TRIGGERS──▶  ML-MTP, ML-MDC
ML-PDG (deployed)  ──TRIGGERS──▶  ML-MMG, ML-OPR
ML-DDM (drift alert)  ──TRIGGERS──▶  ML-RTS evaluation
ML-MDM (drift alert)  ──TRIGGERS──▶  ML-RTS execution
ML-MFR (incident)  ──TRIGGERS──▶  ML-PIR, ML-RBP (if needed)
```

### 3.4 Zależności VALIDATES (A weryfikuje poprawność B)

```
ML-TSE  ──VALIDATES──▶  ML-MTC
ML-FBT  ──VALIDATES──▶  ML-MTC (fairness)
ML-ADV  ──VALIDATES──▶  ML-MTC (robustness)
ML-DRT  ──VALIDATES──▶  ML-DRP
ML-ACL  ──VALIDATES──▶  ML-EUA
```

---

## 4. LIFECYCLE DOKUMENTÓW

### 4.1 Stany Dokumentu

```
┌─────────┐    ┌─────────┐    ┌──────────┐    ┌──────────┐
│  DRAFT  │───▶│ REVIEW  │───▶│ APPROVED │───▶│  ACTIVE  │
└─────────┘    └─────────┘    └──────────┘    └──────────┘
                   │                              │
                   ▼                              ▼
              ┌─────────┐                   ┌───────────┐
              │ REJECTED│                   │ SUPERSEDED│
              └─────────┘                   └───────────┘
                                                 │
                                                 ▼
                                            ┌──────────┐
                                            │ ARCHIVED │
                                            └──────────┘
```

### 4.2 Lifecycle per Document Type

| Typ | Utworzenie | Okres ważności | Przegląd | Archiwizacja |
|-----|------------|----------------|----------|--------------|
| SPEC | Project start | Project end | Przy zmianach | 10 lat (EU AI Act) |
| ARCH | Design phase | Model EOL | Quarterly | 10 lat |
| CODE | Implementation | Model EOL | Per commit | 10 lat |
| CARD | Pre-deployment | Model EOL | Per model version | 10 lat |
| RUNBOOK | Pre-deployment | Model EOL | Po incydencie | 10 lat |
| AUDIT | Scheduled/Triggered | Audit cycle | Annual | 10 lat |
| PLAN | Planning phase | Execution end | Per milestone | 5 lat |
| REPORT | Scheduled | Report period | N/A | 5 lat |

### 4.3 Retencja (EU AI Act Art. 18)

```
HIGH-RISK AI SYSTEMS:
├── Technical documentation: 10 lat od market placement
├── Quality management docs: 10 lat
├── Conformity assessment: 10 lat
├── EU declaration: 10 lat
└── Logs (automatic): 10 lat od last operation
```

---

## 5. TRIGGERY I WARUNKI

### 5.1 Triggery Automatyczne

| Trigger | Warunek | Akcja | Dokumenty |
|---------|---------|-------|-----------|
| **Drift Alert** | Data drift > threshold | Evaluate retraining | RTS, MDD |
| **Performance Drop** | Metrics < threshold | Incident escalation | MFR, PIR |
| **Scheduled Retrain** | Time interval | Execute pipeline | RTS, MTC |
| **Model Version** | New model deployed | Update cards | MDC, DDC |
| **Compliance Audit** | Annual schedule | Generate report | ACL, CRP |
| **Capacity Alert** | Utilization > 85% | Scale review | CAP, CTA |
| **Cost Threshold** | Budget > 90% | Review allocation | CTR, BUD |

### 5.2 Triggery Manualne

| Trigger | Inicjator | Akcja | Dokumenty |
|---------|-----------|-------|-----------|
| **Change Request** | Developer/PM | CAB review | RFC, CIA |
| **Incident Report** | On-call | Incident process | MFR, PIR |
| **Project Start** | Business | Initiate project | PSD, FEA |
| **Retirement Request** | PM/Arch | EOL process | RET, DMI |
| **Vendor Onboarding** | Procurement | Evaluation | RFP, VEM |

### 5.3 Warunki Obowiązywania

| Dokument | Obowiązuje KIEDY | NIE obowiązuje KIEDY |
|----------|------------------|----------------------|
| ML-EUA | HIGH-RISK AI (EU AI Act Annex III) | MINIMAL/LIMITED risk |
| ML-FBT | Decyzje dotyczące osób | Pure technical tasks |
| ML-MDC | Model w produkcji | Development only |
| ML-DRP | Production systems | Dev/Test environments |
| ML-SLA | External vendors | Internal tools |
| ML-ACL | Annual audit cycle | Between audits |

### 5.4 EU AI Act Timeline Triggers

| Data | Trigger | Wymagane Dokumenty |
|------|---------|-------------------|
| **Feb 2, 2025** | Prohibited AI banned | RRC, AET |
| **Aug 2, 2025** | GPAI rules apply | MDC, EXP-DOC |
| **Aug 2, 2026** | Full compliance | Wszystkie HIGH-RISK |
| **Aug 2, 2027** | Regulated products | Extended compliance |

---

## 6. SZABLONY DOKUMENTÓW

Szczegółowe szablony znajdują się w osobnych plikach:

### CRITICAL Documents (23)
1. `templates/ML-PSD_Problem_Statement.md`
2. `templates/ML-FEA_Feasibility_Assessment.md`
3. `templates/ML-REQ_Requirements_Specification.md`
4. `templates/ML-DRQ_Data_Requirements.md`
5. `templates/ML-ARC_Architecture_Document.md`
6. `templates/ML-FEP_Feature_Engineering_Plan.md`
7. `templates/ML-DPC_Data_Preparation_Code.md`
8. `templates/ML-MTC_Model_Training_Code.md`
9. `templates/ML-MTP_Model_Testing_Plan.md`
10. `templates/ML-FBT_Fairness_Bias_Testing.md`
11. `templates/ML-EXP-DOC_Explainability_Documentation.md`
12. `templates/ML-RCC_Regulatory_Compliance.md`
13. `templates/ML-EUA_EU_AI_Act_Compliance.md`
14. `templates/ML-MSA_Model_Serving_Architecture.md`
15. `templates/ML-PDG_Production_Deployment_Guide.md`
16. `templates/ML-MMG_Monitoring_Guide.md`
17. `templates/ML-MDD_Model_Drift_Detection.md`
18. `templates/ML-PMT_Performance_Metrics.md`
19. `templates/ML-MFR_Model_Failure_Recovery.md`
20. `templates/ML-RBP_Rollback_Procedure.md`
21. `templates/ML-MDC_Model_Card.md`
22. `templates/ML-DRP_Disaster_Recovery_Plan.md`
23. `templates/ML-BCP_Business_Continuity_Plan.md`

---

## APPENDIX A: Skróty i Definicje

| Skrót | Pełna nazwa |
|-------|-------------|
| ARC | Architecture |
| BCP | Business Continuity Plan |
| CAB | Change Advisory Board |
| DRP | Disaster Recovery Plan |
| EUA | EU AI Act |
| FBT | Fairness & Bias Testing |
| MDC | Model Card |
| MDD | Model Drift Detection |
| MFR | Model Failure Recovery |
| MMG | Monitoring Guide |
| MSA | Model Serving Architecture |
| PDG | Production Deployment Guide |
| PIR | Post-Incident Report |
| RBP | Rollback Procedure |
| RFC | Request for Change |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| RTS | Retraining Schedule |
| SLA | Service Level Agreement |
| TSE | Test Set Evaluation |

---

**Koniec dokumentu głównego. Szczegółowe szablony w kolejnych plikach.**
