# ML-EUA: EU AI Act Compliance Documentation
## Dokumentacja Zgodności z EU AI Act

**Wersja szablonu:** 2.0  
**Standard:** Regulation (EU) 2024/1689, Annex IV, Article 11  
**Priorytet:** CRITICAL  
**Kod dokumentu:** ML-EUA

---

## METADANE DOKUMENTU

```yaml
document_id: ML-EUA-[PROJECT_ID]-[VERSION]
version: 1.0.0
status: [DRAFT|REVIEW|APPROVED|ACTIVE|SUPERSEDED|ARCHIVED]
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
created_date: YYYY-MM-DD
last_updated: YYYY-MM-DD
next_review: YYYY-MM-DD  # Annual minimum
author: [Name]
compliance_officer: [Name]
legal_reviewer: [Name]
classification: CONFIDENTIAL

# Lifecycle
lifecycle:
  created_trigger: "HIGH-RISK classification confirmed"
  valid_from: "Model deployment date"
  valid_until: "10 years after market placement (Art. 18)"
  retention: "10 years minimum"
  regulatory_authority: "[National authority]"
```

---

## SEKCJA 1: SYSTEM IDENTIFICATION

### 1.1 AI System Overview

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-PSD (Problem Statement) → cel systemu
├── INPUT: ML-REQ (Requirements) → funkcjonalność
├── INPUT: ML-ARC (Architecture) → opis techniczny
├── OUTPUT: → Sekcja 2 (Risk Classification)
└── EU AI ACT: Art. 6, Annex I, Annex III
```

| Pole | Wartość | Źródło |
|------|---------|--------|
| **Nazwa systemu AI** | | ML-REQ |
| **Wersja** | | ML-MDC |
| **Typ AI** | [ ] ML / [ ] DL / [ ] LLM / [ ] Rule-based | ML-ARC |
| **Provider** | [Nazwa organizacji] | |
| **Deployer** | [Jeśli inny niż provider] | |
| **Market placement date** | | |
| **EU Registration number** | | Art. 49 |

### 1.2 Intended Purpose (Art. 6, Annex III)

```
ZALEŻNOŚCI:
├── INPUT: ML-REQ → intended use cases
├── INPUT: ML-UCN → use case narratives
├── OUTPUT: → Sekcja 2.1 (risk determination)
└── CRITICAL: Determines HIGH-RISK classification
```

**Primary purpose:**
```
[Opisz główny cel systemu AI - max 200 słów]
```

**Use case categories:**
| Category | Applicable | Description |
|----------|------------|-------------|
| Critical Infrastructure | [ ] | |
| Education & Training | [ ] | |
| Employment & Workers | [ ] | |
| Essential Services | [ ] | |
| Law Enforcement | [ ] | |
| Migration & Border | [ ] | |
| Justice & Democracy | [ ] | |
| Other (specify) | [ ] | |

---

## SEKCJA 2: RISK CLASSIFICATION (Art. 6, Annex I, III)

### 2.1 Risk Assessment

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-RRC (Regulatory Requirements Checklist)
├── INPUT: ML-AET (AI Ethics Assessment)
├── INPUT: Sekcja 1.2 (Intended Purpose)
├── OUTPUT: → Wszystkie sekcje (określa wymagania)
├── OUTPUT: → ML-ACL (Audit Checklist scope)
└── EU AI ACT: Art. 6 - classification rules
```

**Risk Category Determination:**

| Category | Check | Criteria Met | Evidence |
|----------|-------|--------------|----------|
| **UNACCEPTABLE** (Art. 5) | | | |
| └─ Social scoring | [ ] N/A | | |
| └─ Subliminal manipulation | [ ] N/A | | |
| └─ Exploitation of vulnerabilities | [ ] N/A | | |
| └─ Biometric categorization | [ ] N/A | | |
| └─ Real-time biometric (public) | [ ] N/A | | |
| **HIGH-RISK** (Annex I/III) | | | |
| └─ Safety component | [ ] Yes/No | | |
| └─ Product under EU legislation | [ ] Yes/No | | |
| └─ Annex III category | [ ] Yes/No | Category: |
| **LIMITED RISK** (Art. 50) | | | |
| └─ Interacts with humans | [ ] Yes/No | | |
| └─ Generates content | [ ] Yes/No | | |
| └─ Emotion recognition | [ ] Yes/No | | |
| └─ Deep fake generation | [ ] Yes/No | | |
| **MINIMAL RISK** | | | |
| └─ None of the above | [ ] Yes/No | | |

**FINAL CLASSIFICATION:**
```
[ ] UNACCEPTABLE - PROHIBITED
[ ] HIGH-RISK - Full compliance required
[ ] LIMITED RISK - Transparency obligations
[ ] MINIMAL RISK - Voluntary codes
```

### 2.2 High-Risk Annex III Subcategory (if applicable)

| Subcategory | Applicable | Specific Use |
|-------------|------------|--------------|
| 1. Biometrics | [ ] | |
| 2. Critical infrastructure | [ ] | |
| 3. Education & vocational | [ ] | |
| 4. Employment & workers | [ ] | |
| 5. Essential services | [ ] | |
| 6. Law enforcement | [ ] | |
| 7. Migration & asylum | [ ] | |
| 8. Justice & democracy | [ ] | |

---

## SEKCJA 3: TECHNICAL DOCUMENTATION (Art. 11, Annex IV)

### 3.1 General Description (Annex IV, Section 1)

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-ARC (Architecture Document)
├── INPUT: ML-REQ (Requirements)
├── INPUT: ML-MDC (Model Card)
├── OUTPUT: → Conformity assessment
└── EU AI ACT: Annex IV, Section 1
```

**3.1.1 Intended purpose description:**
```
[Detailed description]
```

**3.1.2 Interaction with other systems:**
| System | Type | Interface | Data Exchange |
|--------|------|-----------|---------------|
| | | | |

**3.1.3 Hardware requirements:**
| Component | Specification | Purpose |
|-----------|---------------|---------|
| | | |

**3.1.4 Product integration (if applicable):**
| Product | Type | Integration Point |
|---------|------|-------------------|
| | | |

### 3.2 Development Process (Annex IV, Section 2)

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-FEP (Feature Engineering Plan)
├── INPUT: ML-DPC (Data Preparation Code)
├── INPUT: ML-MTC (Model Training Code)
├── INPUT: ML-EXP (Experiments Log)
├── OUTPUT: → Reproducibility evidence
└── EU AI ACT: Annex IV, Section 2
```

**3.2.1 Design specifications:**
```
[Reference: ML-ARC]
```

**3.2.2 System architecture:**
```
[Include architecture diagram reference]
```

**3.2.3 Computational resources:**
| Resource | Training | Inference |
|----------|----------|-----------|
| GPU | | |
| Memory | | |
| Storage | | |

**3.2.4 Development methodology:**
| Phase | Methodology | Documentation |
|-------|-------------|---------------|
| Data | | ML-DPC |
| Features | | ML-FEP |
| Training | | ML-MTC |
| Testing | | ML-MTP |

### 3.3 Data Requirements (Annex IV, Section 2d)

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-DRQ (Data Requirements)
├── INPUT: ML-DDC (Dataset Documentation)
├── INPUT: ML-DPC (Data Preparation Code)
├── OUTPUT: → Data governance compliance
└── EU AI ACT: Annex IV, Section 2d + GDPR
```

**3.3.1 Training data:**
| Dataset | Size | Source | Period | GDPR Basis |
|---------|------|--------|--------|------------|
| | | | | |

**3.3.2 Data governance measures:**
| Measure | Implemented | Evidence |
|---------|-------------|----------|
| Relevance assessment | [ ] | |
| Representativeness | [ ] | |
| Error examination | [ ] | |
| Gap identification | [ ] | |
| Bias detection | [ ] | |

**3.3.3 Data preparation:**
| Step | Description | Tool | Validation |
|------|-------------|------|------------|
| | | | |

### 3.4 Model Information (Annex IV, Section 2)

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-MSL (Model Selection)
├── INPUT: ML-MTC (Model Training Code)
├── INPUT: ML-MDC (Model Card)
├── OUTPUT: → Conformity assessment
└── EU AI ACT: Annex IV, Section 2e-g
```

**3.4.1 Model architecture:**
| Parameter | Value |
|-----------|-------|
| Model type | |
| Architecture | |
| Parameters | |
| Layers | |

**3.4.2 Training process:**
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Epochs | | |
| Batch size | | |
| Learning rate | | |
| Optimizer | | |
| Loss function | | |

**3.4.3 Model selection rationale:**
```
[Why this model was chosen - reference ML-MSL]
```

---

## SEKCJA 4: HUMAN OVERSIGHT (Art. 14)

### 4.1 Oversight Measures

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-AET (AI Ethics Assessment)
├── INPUT: ML-MDC (Model Card - Sekcja 8)
├── OUTPUT: → ML-OPR (Operational Runbook)
├── OUTPUT: → ML-TRN (Training materials)
└── EU AI ACT: Art. 14 - Human oversight
```

**4.1.1 Oversight capabilities:**
| Capability | Implemented | Method | Documentation |
|------------|-------------|--------|---------------|
| Understand system | [ ] | | |
| Monitor operation | [ ] | | |
| Interpret outputs | [ ] | | |
| Override/reverse | [ ] | | |
| Intervene/stop | [ ] | | |

**4.1.2 Human-in-the-loop configuration:**
| Decision Type | Automation Level | Human Review |
|---------------|------------------|--------------|
| | Full/Partial/None | Always/Threshold/Random |

**4.1.3 Override procedures:**
```
[Reference: ML-OPR Section X]
```

### 4.2 User Information Requirements

| Information | Provided | Format | Location |
|-------------|----------|--------|----------|
| AI nature | [ ] | | |
| Capabilities | [ ] | | |
| Limitations | [ ] | | |
| Contact info | [ ] | | |

---

## SEKCJA 5: ACCURACY, ROBUSTNESS, CYBERSECURITY (Art. 15)

### 5.1 Accuracy Metrics (Art. 15.1)

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-TSE (Test Set Evaluation)
├── INPUT: ML-SMC (Success Metrics)
├── INPUT: ML-MDC (Model Card - Sekcja 4)
├── OUTPUT: → Conformity declaration
└── EU AI ACT: Art. 15.1 - Accuracy
```

| Metric | Value | Threshold | Compliant |
|--------|-------|-----------|-----------|
| | | | [ ] |
| | | | [ ] |

**Accuracy declaration:**
```
System achieves [X]% accuracy on [dataset] under [conditions].
Confidence interval: [X-Y]% at 95% confidence level.
```

### 5.2 Robustness Measures (Art. 15.4)

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-ADV (Adversarial Testing)
├── INPUT: ML-MTP (Model Testing Plan)
├── OUTPUT: → Risk mitigation evidence
└── EU AI ACT: Art. 15.4 - Robustness
```

| Test Type | Performed | Result | Mitigation |
|-----------|-----------|--------|------------|
| Adversarial inputs | [ ] | | |
| Edge cases | [ ] | | |
| Distribution shift | [ ] | | |
| Error handling | [ ] | | |

### 5.3 Cybersecurity (Art. 15.5)

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-MSA (Model Serving Architecture)
├── INPUT: Security assessment
├── OUTPUT: → Security compliance evidence
└── EU AI ACT: Art. 15.5 - Cybersecurity
```

| Threat | Protection | Verified |
|--------|------------|----------|
| Data poisoning | | [ ] |
| Model extraction | | [ ] |
| Adversarial attacks | | [ ] |
| Unauthorized access | | [ ] |

---

## SEKCJA 6: RISK MANAGEMENT (Art. 9)

### 6.1 Risk Management System

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-RRG (Risk Register)
├── INPUT: ML-FBT (Fairness & Bias Testing)
├── INPUT: ML-AET (AI Ethics Assessment)
├── OUTPUT: → Continuous risk monitoring
└── EU AI ACT: Art. 9 - Risk management
```

**6.1.1 Identified risks:**
| Risk | Probability | Impact | Score | Mitigation | Status |
|------|-------------|--------|-------|------------|--------|
| | H/M/L | H/M/L | | | |
| | | | | | |

**6.1.2 Risk mitigation measures:**
| Measure | Risk Addressed | Effectiveness |
|---------|----------------|---------------|
| | | |

**6.1.3 Residual risks:**
| Risk | Level | Acceptance Rationale |
|------|-------|---------------------|
| | | |

### 6.2 Testing for Risk Identification

```
ZALEŻNOŚCI:
├── INPUT: ML-MTP, ML-FBT, ML-ADV
└── OUTPUT: → Risk register updates
```

| Test | Performed | Findings | Actions |
|------|-----------|----------|---------|
| Functionality | [ ] | | |
| Performance | [ ] | | |
| Bias & Fairness | [ ] | | |
| Robustness | [ ] | | |

---

## SEKCJA 7: TRANSPARENCY & INFORMATION (Art. 13, 50)

### 7.1 Instructions for Use

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-MDC (Model Card)
├── INPUT: ML-DOC (Documentation)
├── OUTPUT: → User documentation package
└── EU AI ACT: Art. 13 - Transparency
```

**Required information checklist:**
| Information | Included | Location |
|-------------|----------|----------|
| Provider identity | [ ] | |
| Contact details | [ ] | |
| AI system characteristics | [ ] | |
| Capabilities & limitations | [ ] | |
| Intended purpose | [ ] | |
| Accuracy metrics | [ ] | |
| Known risks | [ ] | |
| Input data specs | [ ] | |
| Human oversight measures | [ ] | |
| Expected lifetime | [ ] | |
| Maintenance info | [ ] | |

### 7.2 Transparency Obligations (Art. 50)

| Obligation | Applicable | Implementation |
|------------|------------|----------------|
| AI interaction disclosure | [ ] | |
| Emotion recognition notice | [ ] | |
| Biometric categorization notice | [ ] | |
| Deep fake labeling | [ ] | |
| AI-generated content marking | [ ] | |

---

## SEKCJA 8: BIAS & DISCRIMINATION (Art. 10)

### 8.1 Bias Assessment

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-FBT (Fairness & Bias Testing) → REQUIRED
├── INPUT: ML-BIM (Bias Mitigation Plan)
├── INPUT: ML-MDC (Model Card - Sekcja 5)
├── OUTPUT: → Compliance evidence
└── EU AI ACT: Art. 10.2(f), Art. 10.5 - Bias
```

**8.1.1 Protected characteristics tested:**
| Characteristic | Tested | Bias Found | Mitigation |
|----------------|--------|------------|------------|
| Gender | [ ] | [ ] | |
| Age | [ ] | [ ] | |
| Race/Ethnicity | [ ] | [ ] | |
| Disability | [ ] | [ ] | |
| Religion | [ ] | [ ] | |
| Other: | [ ] | [ ] | |

**8.1.2 Fairness metrics:**
| Metric | Value | Threshold | Compliant |
|--------|-------|-----------|-----------|
| Demographic Parity | | 0.8-1.2 | [ ] |
| Equalized Odds | | | [ ] |
| Equal Opportunity | | | [ ] |

### 8.2 Bias Mitigation

| Technique | Applied | Effect |
|-----------|---------|--------|
| Pre-processing | [ ] | |
| In-processing | [ ] | |
| Post-processing | [ ] | |

---

## SEKCJA 9: QUALITY MANAGEMENT (Art. 17)

### 9.1 Quality Management System

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: Organizational QMS
├── OUTPUT: → Audit trail
└── EU AI ACT: Art. 17 - Quality management
```

**QMS Components:**
| Component | Documented | Location |
|-----------|------------|----------|
| Compliance strategy | [ ] | |
| Design & development procedures | [ ] | |
| Testing & validation procedures | [ ] | |
| Data management procedures | [ ] | |
| Risk management procedures | [ ] | |
| Post-market monitoring | [ ] | |
| Incident reporting | [ ] | |
| Communication with authorities | [ ] | |

### 9.2 Documentation Control

| Document Type | Version Control | Retention |
|---------------|-----------------|-----------|
| Technical docs | [ ] | 10 years |
| Test results | [ ] | 10 years |
| Change records | [ ] | 10 years |
| Audit reports | [ ] | 10 years |

---

## SEKCJA 10: POST-MARKET MONITORING (Art. 72)

### 10.1 Monitoring Plan

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-MMG (Monitoring Guide)
├── INPUT: ML-MDD (Model Drift Detection)
├── OUTPUT: → Continuous compliance monitoring
└── EU AI ACT: Art. 72 - Post-market monitoring
```

**Monitoring scope:**
| Aspect | Metric | Frequency | Threshold |
|--------|--------|-----------|-----------|
| Performance | | | |
| Fairness | | | |
| Drift | | | |
| Incidents | | | |

### 10.2 Incident Reporting

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-PIR (Post-Incident Report)
├── OUTPUT: → Authority notification (Art. 73)
└── TIMELINE: 72 hours for serious incidents
```

| Incident Type | Reporting Timeline | Authority |
|---------------|-------------------|-----------|
| Serious incident | 72 hours | |
| Malfunction | 15 days | |
| Systematic issues | 30 days | |

---

## SEKCJA 11: CONFORMITY ASSESSMENT (Art. 43)

### 11.1 Assessment Procedure

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: Wszystkie poprzednie sekcje
├── OUTPUT: → EU Declaration of Conformity
├── OUTPUT: → CE Marking eligibility
└── EU AI ACT: Art. 43, Annex VI/VII
```

**Assessment type:**
| Type | Applicable | Justification |
|------|------------|---------------|
| Self-assessment (Annex VI) | [ ] | |
| Notified body (Annex VII) | [ ] | |
| Third-party (biometrics) | [ ] | |

### 11.2 Conformity Checklist

| Requirement | Article | Compliant | Evidence |
|-------------|---------|-----------|----------|
| Risk management | Art. 9 | [ ] | |
| Data governance | Art. 10 | [ ] | |
| Technical documentation | Art. 11 | [ ] | |
| Record-keeping | Art. 12 | [ ] | |
| Transparency | Art. 13 | [ ] | |
| Human oversight | Art. 14 | [ ] | |
| Accuracy & robustness | Art. 15 | [ ] | |
| Quality management | Art. 17 | [ ] | |

### 11.3 EU Declaration of Conformity

```
[To be completed after conformity assessment]

Declaration Number: _______________
Date: _______________

We hereby declare that the AI system described in this 
documentation is in conformity with Regulation (EU) 2024/1689.

Provider: _______________
Authorized representative: _______________
Signature: _______________
```

---

## SEKCJA 12: REGISTRATION (Art. 49)

### 12.1 EU Database Registration

| Field | Value |
|-------|-------|
| Provider name | |
| Provider address | |
| Authorized representative | |
| AI system name | |
| Intended purpose | |
| Status | [ ] Registered / [ ] Pending |
| Registration date | |
| Registration number | |

---

## LIFECYCLE SUMMARY

```yaml
KIEDY DOKUMENT SIĘ POJAWIA:
  trigger: "HIGH-RISK classification confirmed (Sekcja 2)"
  prerequisites:
    - ML-RRC (Regulatory Requirements Checklist) complete
    - ML-AET (AI Ethics Assessment) complete
    - ML-FBT (Fairness & Bias Testing) complete
  timeline: "Before market placement"
    
KIEDY DOKUMENT ZNIKA/WYGASA:
  triggers:
    - System withdrawn from market
    - Classification downgraded to LIMITED/MINIMAL
    - System superseded
  retention: "10 years after last market presence (Art. 18)"
  
KIEDY OBOWIĄZUJE:
  conditions:
    - System classified as HIGH-RISK
    - System placed on EU market
    - System put into service in EU
    
KIEDY NIE OBOWIĄZUJE:
  conditions:
    - MINIMAL/LIMITED risk systems (partial requirements only)
    - Systems outside EU market
    - Research & development only
    - Military/national security use
    
AKTUALIZACJE WYMAGANE GDY:
  - Substantial modification (Art. 43.4)
  - Regulatory changes
  - Incident requiring corrective action
  - Annual review (minimum)
  - Conformity re-assessment triggered
  
NOTIFICATION REQUIREMENTS:
  - Serious incidents: 72 hours
  - Market withdrawal: Immediate
  - Corrective actions: 15 days
```

---

## APPROVAL & SIGNATURES

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Technical Lead | | | |
| Data Protection Officer | | | |
| Compliance Officer | | | |
| Legal Counsel | | | |
| CEO/Authorized Rep | | | |

---

**END OF TEMPLATE**
