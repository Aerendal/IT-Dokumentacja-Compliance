# ML-MDC: Model Card Template
## Szablon Karty Modelu ML/AI

**Wersja szablonu:** 2.0  
**Standard:** Google Model Cards, Hugging Face, EU AI Act Art. 11, Annex IV  
**Priorytet:** CRITICAL  
**Kod dokumentu:** ML-MDC

---

## METADANE DOKUMENTU

```yaml
document_id: ML-MDC-[PROJECT_ID]-[VERSION]
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
owner: [Team/Person]
classification: [INTERNAL|CONFIDENTIAL|PUBLIC]

# Lifecycle
lifecycle:
  created_trigger: "Model training completed (ML-MTC)"
  valid_from: "Deployment date"
  valid_until: "Model retirement or version supersede"
  retention: "10 years (EU AI Act Art. 18)"
  archive_location: "[Archive path]"
```

---

## SEKCJA 1: MODEL DETAILS (Szczegóły Modelu)

### 1.1 Podstawowe Informacje

| Pole | Wartość | Źródło danych |
|------|---------|---------------|
| **Nazwa modelu** | | ML-MTC |
| **Wersja** | | ML-EXP |
| **Typ modelu** | | ML-MSL |
| **Framework** | | ML-MTC |
| **Data treningu** | | ML-EXP |
| **Właściciel** | | ML-REQ |

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-MTC (Model Training Code) → nazwa, wersja, framework
├── INPUT: ML-MSL (Model Selection) → typ modelu
├── INPUT: ML-EXP (Experiments Log) → data treningu, wersja
├── OUTPUT: → Sekcja 2 (Intended Use), Sekcja 3 (Training Data)
└── TRIGGER: Aktualizacja przy nowej wersji modelu
```

### 1.2 Opis Modelu

**Architektura:**
```
[Opisz architekturę modelu - np. CNN, Transformer, ensemble]
```

**Cel biznesowy:**
```
[Jaki problem biznesowy rozwiązuje model]
```

**Kontakt:**
| Rola | Osoba | Email |
|------|-------|-------|
| Model Owner | | |
| ML Engineer | | |
| Data Scientist | | |
| Compliance | | |

---

## SEKCJA 2: INTENDED USE (Zamierzone Użycie)

### 2.1 Primary Use Cases

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-REQ → wymagania funkcjonalne
├── INPUT: ML-UCN → scenariusze użycia
├── INPUT: ML-PSD → problem statement
├── OUTPUT: → Sekcja 6 (Ethical Considerations)
├── OUTPUT: → ML-EUA (EU AI Act - intended purpose)
└── WARUNEK: HIGH-RISK AI wymaga szczegółowego opisu
```

**Zamierzone zastosowania:**
1. [ ] [Zastosowanie 1]
2. [ ] [Zastosowanie 2]
3. [ ] [Zastosowanie 3]

### 2.2 Primary Users

| Typ użytkownika | Opis | Wymagania |
|-----------------|------|-----------|
| **End Users** | | |
| **Operators** | | |
| **Administrators** | | |

### 2.3 Out-of-Scope Uses (CRITICAL)

```
 OSTRZEŻENIE: Model NIE powinien być używany do:
```

| Zabronione użycie | Przyczyna | Ryzyko |
|-------------------|-----------|--------|
| | | HIGH/MEDIUM/LOW |
| | | |
| | | |

### 2.4 EU AI Act Risk Category

```
ZALEŻNOŚCI:
├── INPUT: ML-RRC (Regulatory Requirements)
├── INPUT: ML-AET (AI Ethics Assessment)
├── OUTPUT: → ML-EUA (determines compliance requirements)
└── TRIGGER: Zmiana regulacji → re-assessment
```

| Kategoria | Status | Uzasadnienie |
|-----------|--------|--------------|
| [ ] UNACCEPTABLE | N/A | |
| [ ] HIGH-RISK | | Annex III category: |
| [ ] LIMITED | | Transparency req: |
| [ ] MINIMAL | | |

---

## SEKCJA 3: TRAINING DATA (Dane Treningowe)

### 3.1 Dataset Overview

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-DRQ (Data Requirements) → specyfikacja danych
├── INPUT: ML-DDC (Dataset Documentation) → szczegóły datasetu
├── INPUT: ML-DPC (Data Preparation Code) → preprocessing
├── OUTPUT: → Sekcja 5 (Bias Testing) - wpływ danych na bias
├── OUTPUT: → ML-EUA - data governance compliance
└── WARUNEK: GDPR compliance dla danych osobowych
```

| Parametr | Wartość | Źródło |
|----------|---------|--------|
| **Nazwa datasetu** | | ML-DDC |
| **Rozmiar** | | ML-DPC |
| **Okres czasowy** | | ML-DDC |
| **Źródło** | | ML-DRQ |
| **Format** | | ML-DPC |

### 3.2 Data Composition

**Rozkład danych:**
| Feature | Typ | Rozkład | Missing % |
|---------|-----|---------|-----------|
| | | | |
| | | | |

**Protected attributes (jeśli dotyczy):**
| Atrybut | Rozkład | Uwagi |
|---------|---------|-------|
| Gender | | |
| Age | | |
| Race/Ethnicity | | |
| | | |

### 3.3 Data Preprocessing

```
ZALEŻNOŚCI:
├── INPUT: ML-DPC → kroki preprocessingu
├── INPUT: ML-FEC → feature engineering
└── OUTPUT: → reproducibility documentation
```

**Pipeline preprocessingu:**
1. [ ] [Krok 1]
2. [ ] [Krok 2]
3. [ ] [Krok 3]

**Transformacje:**
| Transformacja | Parametry | Cel |
|---------------|-----------|-----|
| | | |
| | | |

---

## SEKCJA 4: PERFORMANCE METRICS (Metryki Wydajności)

### 4.1 Overall Performance

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-TSE (Test Set Evaluation) → wyniki testów
├── INPUT: ML-SMC (Success Metrics Criteria) → thresholds
├── INPUT: ML-EXP (Experiments Log) → historia metryk
├── OUTPUT: → Sekcja 5 (subgroup performance)
├── OUTPUT: → ML-PRR (Performance Report)
├── OUTPUT: → ML-MMG (monitoring thresholds)
└── TRIGGER: Metryki poniżej threshold → ML-RTS review
```

| Metryka | Wartość | Threshold | Status |
|---------|---------|-----------|--------|
| **Accuracy** | | | / |
| **Precision** | | | / |
| **Recall** | | | / |
| **F1-Score** | | | / |
| **AUC-ROC** | | | / |
| **Latency P50** | | | / |
| **Latency P99** | | | / |

### 4.2 Subgroup Performance (CRITICAL for Fairness)

```
ZALEŻNOŚCI:
├── INPUT: ML-FBT (Fairness & Bias Testing)
├── OUTPUT: → ML-BIM (jeśli disparities detected)
└── EU AI ACT: Wymagane dla HIGH-RISK
```

**Performance by Protected Group:**

| Grupa | Accuracy | Precision | Recall | Disparate Impact |
|-------|----------|-----------|--------|------------------|
| Group A | | | | |
| Group B | | | | |
| Δ (difference) | | | | |

**Fairness Metrics:**
| Metryka | Wartość | Threshold | Status |
|---------|---------|-----------|--------|
| Demographic Parity | | 0.8-1.2 | |
| Equalized Odds | | | |
| Equal Opportunity | | | |
| Calibration | | | |

### 4.3 Confidence Intervals

| Metryka | Mean | 95% CI Lower | 95% CI Upper |
|---------|------|--------------|--------------|
| | | | |

---

## SEKCJA 5: BIAS & FAIRNESS TESTING (CRITICAL)

### 5.1 Bias Assessment Summary

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-FBT (Fairness & Bias Testing) → wyniki testów
├── INPUT: ML-AET (AI Ethics Assessment) → ethical framework
├── INPUT: ML-ADV (Adversarial Testing) → robustness
├── OUTPUT: → ML-BIM (Bias Mitigation Plan) jeśli bias detected
├── OUTPUT: → ML-EUA (compliance evidence)
├── OUTPUT: → Sekcja 6 (Ethical Considerations)
└── EU AI ACT: MANDATORY dla HIGH-RISK AI
```

**Bias Testing Results:**
| Typ Bias | Testowany | Wykryty | Severity | Mitigation |
|----------|-----------|---------|----------|------------|
| Selection Bias | / | / | H/M/L | |
| Measurement Bias | / | / | H/M/L | |
| Algorithmic Bias | / | / | H/M/L | |
| Representation Bias | / | / | H/M/L | |
| Historical Bias | / | / | H/M/L | |

### 5.2 Fairness Methodology

**Narzędzia użyte:**
- [ ] IBM AI Fairness 360
- [ ] Microsoft Fairlearn
- [ ] Google What-If Tool
- [ ] Aequitas
- [ ] Custom: ____________

**Protected Groups Analyzed:**
| Group | Definition | Sample Size | Notes |
|-------|------------|-------------|-------|
| | | | |

### 5.3 Bias Mitigation Actions

```
ZALEŻNOŚCI:
├── INPUT: Bias detection results (5.1)
├── OUTPUT: → ML-BIM (detailed plan)
├── OUTPUT: → ML-MTC (retraining requirements)
└── LIFECYCLE: Re-evaluate after each mitigation
```

| Action | Status | Impact | Owner |
|--------|--------|--------|-------|
| | Planned/Done | | |
| | | | |

---

## SEKCJA 6: EXPLAINABILITY (CRITICAL for EU AI Act)

### 6.1 Model Interpretability

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-EXP-DOC (Explainability Documentation)
├── INPUT: ML-MTC (model architecture)
├── OUTPUT: → ML-EUA (transparency requirements)
├── OUTPUT: → ML-ONB (user understanding)
└── EU AI ACT Art. 13: Transparency requirements
```

**Interpretability Level:**
| Poziom | Status | Uzasadnienie |
|--------|--------|--------------|
| [ ] Glass Box (fully interpretable) | | |
| [ ] Post-hoc Explainable | | |
| [ ] Black Box | | |

### 6.2 Explanation Methods Used

| Metoda | Scope | Output Type | Stakeholder |
|--------|-------|-------------|-------------|
| SHAP | Global/Local | Feature importance | Technical |
| LIME | Local | Feature weights | Business |
| Attention Maps | Local | Visual | End-user |
| Decision Rules | Global | Rules | Audit |

### 6.3 Feature Importance (Global)

| Feature | Importance | Direction | Confidence |
|---------|------------|-----------|------------|
| | | +/- | |
| | | | |
| | | | |

### 6.4 Example Explanations

**Positive Prediction Example:**
```
Input: [...]
Prediction: [...]
Explanation: [...]
Top factors: [...]
```

**Negative Prediction Example:**
```
Input: [...]
Prediction: [...]
Explanation: [...]
Top factors: [...]
```

---

## SEKCJA 7: LIMITATIONS & RISKS

### 7.1 Known Limitations

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-TSE (test limitations)
├── INPUT: ML-ADV (adversarial weaknesses)
├── INPUT: ML-FBT (fairness limitations)
├── OUTPUT: → ML-EUA (risk documentation)
├── OUTPUT: → ML-MMG (monitoring focus areas)
├── OUTPUT: → ML-OPR (operational awareness)
└── LIFECYCLE: Update after each incident
```

| Limitation | Description | Impact | Mitigation |
|------------|-------------|--------|------------|
| Data Distribution | | | |
| Edge Cases | | | |
| Temporal Validity | | | |
| Domain Shift | | | |

### 7.2 Risk Assessment

| Risk | Probability | Impact | Risk Score | Owner |
|------|-------------|--------|------------|-------|
| | H/M/L | H/M/L | | |
| | | | | |

### 7.3 Failure Modes

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-MFR (failure recovery)
├── OUTPUT: → ML-RBP (rollback triggers)
└── TRIGGER: Failure occurrence → ML-PIR
```

| Failure Mode | Symptoms | Detection | Response |
|--------------|----------|-----------|----------|
| | | | |
| | | | |

---

## SEKCJA 8: ETHICAL CONSIDERATIONS (CRITICAL for EU AI Act)

### 8.1 Human Oversight

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-AET (AI Ethics Assessment)
├── INPUT: ML-EUA (EU AI Act requirements)
├── OUTPUT: → ML-OPR (operational procedures)
└── EU AI ACT Art. 14: Human oversight requirements
```

| Requirement | Implementation | Status |
|-------------|----------------|--------|
| Human-in-the-loop | | / |
| Override capability | | / |
| Appeal process | | / |
| Monitoring capability | | / |

### 8.2 Societal Impact

| Impact Area | Assessment | Mitigation |
|-------------|------------|------------|
| Employment | | |
| Privacy | | |
| Equality | | |
| Environment | | |

### 8.3 Compliance Status

| Regulation | Status | Evidence | Review Date |
|------------|--------|----------|-------------|
| EU AI Act | | ML-EUA | |
| GDPR | | | |
| Local Laws | | | |

---

## SEKCJA 9: DEPLOYMENT & OPERATIONS

### 9.1 Deployment Information

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-MSA (Model Serving Architecture)
├── INPUT: ML-PDG (Production Deployment Guide)
├── OUTPUT: → ML-MMG (monitoring setup)
├── OUTPUT: → ML-OPR (runbook reference)
└── TRIGGER: Deployment change → update this section
```

| Parameter | Value |
|-----------|-------|
| Deployment Date | |
| Environment | |
| Serving Platform | |
| Endpoint | |
| SLA | |

### 9.2 Monitoring Setup

| Metric | Threshold | Alert | Dashboard |
|--------|-----------|-------|-----------|
| | | | |
| | | | |

### 9.3 Retraining Schedule

```
ZALEŻNOŚCI:
├── INPUT: ML-RTS (Retraining Schedule)
├── TRIGGER: Drift detection → evaluate retraining
└── OUTPUT: → new Model Card version
```

| Trigger | Condition | Action |
|---------|-----------|--------|
| Scheduled | | |
| Performance | | |
| Drift | | |

---

## SEKCJA 10: VERSION HISTORY

### 10.1 Model Versions

| Version | Date | Changes | Metrics Change | Author |
|---------|------|---------|----------------|--------|
| 1.0.0 | | Initial release | - | |
| | | | | |

### 10.2 Card Update History

| Version | Date | Section Updated | Reason |
|---------|------|-----------------|--------|
| | | | |

---

## SEKCJA 11: APPENDICES

### 11.1 Related Documents

```
DOCUMENT DEPENDENCIES MAP:

INPUTS (wymagane przed utworzeniem):
├── ML-MTC (Model Training Code) ─── REQUIRED
├── ML-TSE (Test Set Evaluation) ─── REQUIRED
├── ML-FBT (Fairness & Bias Testing) ─── REQUIRED
├── ML-EXP-DOC (Explainability) ─── REQUIRED
├── ML-DDC (Dataset Documentation) ─── RECOMMENDED
├── ML-MSL (Model Selection) ─── RECOMMENDED
└── ML-AET (AI Ethics Assessment) ─── REQUIRED for HIGH-RISK

OUTPUTS (dokumenty zależne od Model Card):
├── ML-MSA (Model Serving Architecture) ─── references MDC
├── ML-PDG (Production Deployment Guide) ─── includes MDC
├── ML-EUA (EU AI Act Compliance) ─── evidence from MDC
├── ML-PRR (Performance Report) ─── metrics from MDC
├── ML-MMG (Monitoring Guide) ─── thresholds from MDC
└── ML-ONB (Onboarding) ─── training material
```

### 11.2 Glossary

| Term | Definition |
|------|------------|
| | |

### 11.3 Approval History

| Role | Name | Date | Signature |
|------|------|------|-----------|
| ML Engineer | | | |
| Data Scientist | | | |
| Ethics Officer | | | |
| Compliance | | | |
| Product Owner | | | |

---

## LIFECYCLE SUMMARY

```yaml
KIEDY DOKUMENT SIĘ POJAWIA:
  trigger: "ML-MTC (Model Training Code) completed successfully"
  prerequisites:
    - ML-MTC status = COMPLETE
    - ML-TSE status = PASSED
    - ML-FBT status = COMPLETE (for HIGH-RISK)
    
KIEDY DOKUMENT ZNIKA/WYGASA:
  triggers:
    - Model retired (ML-RET executed)
    - Model version superseded
    - Project cancelled
  retention: "10 years after last use (EU AI Act Art. 18)"
  
KIEDY OBOWIĄZUJE:
  conditions:
    - Model is in production
    - Model is available for inference
    - Model is used in decision-making
    
KIEDY NIE OBOWIĄZUJE:
  conditions:
    - Model in development only (use draft version)
    - Model retired and archived
    - Superseded by newer version
    
AKTUALIZACJE WYMAGANE GDY:
  - Model retrained (ML-RTS executed)
  - Performance metrics change significantly
  - Bias testing reveals new findings
  - Regulatory requirements change
  - Incident occurs (ML-PIR created)
  - Deployment configuration changes
```

---

**END OF TEMPLATE**
