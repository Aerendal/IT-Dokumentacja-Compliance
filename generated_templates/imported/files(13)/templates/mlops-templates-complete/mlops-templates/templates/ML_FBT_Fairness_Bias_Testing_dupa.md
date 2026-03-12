# ML-FBT: Fairness & Bias Testing Documentation
## Dokumentacja Testów Fairness i Bias

**Wersja szablonu:** 2.0  
**Standard:** EU AI Act Art. 10, NIST AI RMF, ISO/IEC TR 24028  
**Priorytet:** CRITICAL  
**Kod dokumentu:** ML-FBT

---

## METADANE DOKUMENTU

```yaml
document_id: ML-FBT-[PROJECT_ID]-[VERSION]
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
ethics_reviewer: [Name]
compliance_officer: [Name]
classification: CONFIDENTIAL

# Lifecycle
lifecycle:
  created_trigger: "Model training completed (ML-MTC)"
  valid_from: "Testing completion date"
  valid_until: "Model retirement or re-testing"
  retention: "10 years (EU AI Act Art. 18)"
  re_test_trigger: "Model retraining, data change, incident"
```

---

## SEKCJA 1: OVERVIEW

### 1.1 Testing Scope

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-REQ → fairness requirements (FR-ML-003)
├── INPUT: ML-AET → ethical framework
├── INPUT: ML-RRC → regulatory requirements
├── OUTPUT: → ML-MDC (Model Card - Sekcja 5)
├── OUTPUT: → ML-EUA (EU AI Act compliance evidence)
├── OUTPUT: → ML-BIM (if bias detected)
└── EU AI ACT: Art. 10.2(f), Art. 10.5
```

**Model Information:**
| Field | Value | Source |
|-------|-------|--------|
| Model Name | | ML-MTC |
| Model Version | | ML-EXP |
| Model Type | | ML-MSL |
| Training Date | | ML-EXP |
| Test Date | | This doc |

**Testing Objectives:**
- [ ] Detect bias in model predictions
- [ ] Measure fairness across protected groups
- [ ] Identify sources of bias
- [ ] Document mitigation actions
- [ ] Provide EU AI Act compliance evidence

### 1.2 Regulatory Context

| Regulation | Requirement | Applicable |
|------------|-------------|------------|
| EU AI Act Art. 10.2(f) | Examine biases | [ ] Yes |
| EU AI Act Art. 10.5 | Bias detection and correction | [ ] Yes |
| GDPR Art. 22 | Automated decision-making | [ ] Yes |
| NYC Local Law 144 | Bias audit for employment | [ ] Yes |
| Industry-specific | | [ ] |

### 1.3 Risk Classification Impact

```
ZALEŻNOŚCI:
├── INPUT: ML-EUA (Sekcja 2 - Risk Classification)
└── OUTPUT: → Testing depth requirements
```

| Risk Category | Testing Requirements |
|---------------|---------------------|
| HIGH-RISK | Full bias audit, all protected groups, multiple metrics |
| LIMITED | Basic fairness check, key protected groups |
| MINIMAL | Optional, recommended best practice |

---

## SEKCJA 2: PROTECTED GROUPS DEFINITION

### 2.1 Protected Characteristics

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-DRQ → available data attributes
├── INPUT: ML-DDC → data composition
├── INPUT: Legal/regulatory requirements
├── OUTPUT: → Testing scope definition
└── CRITICAL: Define BEFORE testing begins
```

**Protected Characteristics Inventory:**

| Characteristic | Proxy Variables | Available in Data | Legal Basis |
|----------------|-----------------|-------------------|-------------|
| **Gender** | | [ ] Direct / [ ] Proxy / [ ] N/A | |
| **Age** | | [ ] Direct / [ ] Proxy / [ ] N/A | |
| **Race/Ethnicity** | | [ ] Direct / [ ] Proxy / [ ] N/A | |
| **Religion** | | [ ] Direct / [ ] Proxy / [ ] N/A | |
| **Disability** | | [ ] Direct / [ ] Proxy / [ ] N/A | |
| **National Origin** | | [ ] Direct / [ ] Proxy / [ ] N/A | |
| **Sexual Orientation** | | [ ] Direct / [ ] Proxy / [ ] N/A | |
| **Socioeconomic Status** | | [ ] Direct / [ ] Proxy / [ ] N/A | |
| **Other:** | | [ ] Direct / [ ] Proxy / [ ] N/A | |

### 2.2 Group Definitions

```
ZALEŻNOŚCI:
├── INPUT: Data availability
├── OUTPUT: → Subgroup performance analysis
└── NOTE: Document reasoning for group boundaries
```

| Characteristic | Groups | Definition | Sample Size |
|----------------|--------|------------|-------------|
| Gender | Male | | n= |
| | Female | | n= |
| | Non-binary | | n= |
| Age | <25 | | n= |
| | 25-44 | | n= |
| | 45-64 | | n= |
| | 65+ | | n= |
| [Add more] | | | |

### 2.3 Intersectionality Considerations

| Intersection | Groups Combined | Sample Size | Included in Testing |
|--------------|-----------------|-------------|---------------------|
| Gender × Age | Female 65+ | n= | [ ] |
| | Male <25 | n= | [ ] |
| [Add more] | | | |

---

## SEKCJA 3: BIAS TYPES ASSESSMENT

### 3.1 Bias Taxonomy

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-DDC → data collection methodology
├── INPUT: ML-DPC → preprocessing steps
├── INPUT: ML-MTC → model architecture
├── OUTPUT: → Targeted testing strategy
└── OUTPUT: → ML-BIM (mitigation per bias type)
```

#### 3.1.1 Historical Bias

**Definition:** Bias present in training data reflecting past discrimination

| Assessment | Finding | Evidence |
|------------|---------|----------|
| Data reflects historical inequities | [ ] Yes / [ ] No / [ ] Unknown | |
| Time period of data | | |
| Known historical issues | | |

**Mitigation (if detected):**
```
[Describe mitigation approach]
```

#### 3.1.2 Representation Bias

**Definition:** Training data doesn't represent deployment population

| Assessment | Finding | Evidence |
|------------|---------|----------|
| Training data demographics | | |
| Deployment population demographics | | |
| Representation gaps identified | [ ] Yes / [ ] No | |

**Representation Analysis:**

| Group | Training % | Population % | Gap | Acceptable |
|-------|------------|--------------|-----|------------|
| | | | | [ ] |

#### 3.1.3 Measurement Bias

**Definition:** Features/labels measured differently across groups

| Assessment | Finding | Evidence |
|------------|---------|----------|
| Measurement methodology varies | [ ] Yes / [ ] No | |
| Label quality varies by group | [ ] Yes / [ ] No | |
| Feature availability varies | [ ] Yes / [ ] No | |

#### 3.1.4 Aggregation Bias

**Definition:** Model assumes one-size-fits-all when subgroups differ

| Assessment | Finding | Evidence |
|------------|---------|----------|
| Subgroup-specific patterns exist | [ ] Yes / [ ] No | |
| Model treats groups uniformly | [ ] Yes / [ ] No | |
| Separate models considered | [ ] Yes / [ ] No | |

#### 3.1.5 Evaluation Bias

**Definition:** Test data doesn't represent all groups fairly

| Assessment | Finding | Evidence |
|------------|---------|----------|
| Test set demographics | | |
| Benchmark appropriateness | [ ] Yes / [ ] No | |
| Evaluation metric fairness | [ ] Yes / [ ] No | |

#### 3.1.6 Deployment Bias

**Definition:** Model used differently than intended

| Assessment | Finding | Evidence |
|------------|---------|----------|
| Usage monitoring in place | [ ] Yes / [ ] No | |
| Usage deviates from intent | [ ] Yes / [ ] No | |
| Feedback loops identified | [ ] Yes / [ ] No | |

### 3.2 Bias Assessment Summary

| Bias Type | Detected | Severity | Mitigation Status |
|-----------|----------|----------|-------------------|
| Historical | [ ] | H/M/L/None | |
| Representation | [ ] | H/M/L/None | |
| Measurement | [ ] | H/M/L/None | |
| Aggregation | [ ] | H/M/L/None | |
| Evaluation | [ ] | H/M/L/None | |
| Deployment | [ ] | H/M/L/None | |

---

## SEKCJA 4: FAIRNESS METRICS

### 4.1 Metrics Selection

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-REQ (FR-ML-003) → required metrics
├── INPUT: Use case context → metric appropriateness
├── OUTPUT: → ML-MDC (Model Card - Sekcja 4.2)
├── OUTPUT: → ML-MMG (monitoring thresholds)
└── NOTE: Different metrics may conflict - document tradeoffs
```

**Metric Selection Rationale:**

| Metric | Selected | Rationale | Tradeoffs |
|--------|----------|-----------|-----------|
| Demographic Parity | [ ] | | |
| Equalized Odds | [ ] | | |
| Equal Opportunity | [ ] | | |
| Predictive Parity | [ ] | | |
| Calibration | [ ] | | |
| Individual Fairness | [ ] | | |

### 4.2 Metric Definitions and Thresholds

#### 4.2.1 Demographic Parity (Statistical Parity)

**Definition:** P(Ŷ=1|A=a) = P(Ŷ=1|A=b) for all groups a, b

**Threshold:** Ratio within [0.8, 1.25] (Four-Fifths Rule)

| Group A | Group B | P(Ŷ=1|A) | P(Ŷ=1|B) | Ratio | Pass |
|---------|---------|----------|----------|-------|------|
| | | | | | [ ] |

#### 4.2.2 Equalized Odds

**Definition:** TPR and FPR equal across groups

**Threshold:** Difference < 0.1

| Group | TPR | FPR | Δ TPR | Δ FPR | Pass |
|-------|-----|-----|-------|-------|------|
| Reference | | | - | - | - |
| | | | | | [ ] |

#### 4.2.3 Equal Opportunity

**Definition:** TPR equal across groups (for positive class)

**Threshold:** Difference < 0.1

| Group | TPR | Δ from Reference | Pass |
|-------|-----|------------------|------|
| Reference | | - | - |
| | | | [ ] |

#### 4.2.4 Predictive Parity

**Definition:** PPV equal across groups

**Threshold:** Difference < 0.1

| Group | PPV (Precision) | Δ from Reference | Pass |
|-------|-----------------|------------------|------|
| Reference | | - | - |
| | | | [ ] |

#### 4.2.5 Calibration

**Definition:** P(Y=1|Ŷ=p) = p for all groups

| Group | Calibration Error | Pass |
|-------|-------------------|------|
| | | [ ] |

### 4.3 Metrics Summary

| Metric | Status | Value | Threshold | Compliant |
|--------|--------|-------|-----------|-----------|
| Demographic Parity | / | | 0.8-1.25 | [ ] |
| Equalized Odds | / | | Δ<0.1 | [ ] |
| Equal Opportunity | / | | Δ<0.1 | [ ] |
| Predictive Parity | / | | Δ<0.1 | [ ] |
| Calibration | / | | | [ ] |

---

## SEKCJA 5: TESTING METHODOLOGY

### 5.1 Testing Tools

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: Available tools and infrastructure
├── OUTPUT: → Reproducible testing process
└── OUTPUT: → Tool requirements for ML-TOO
```

| Tool | Version | Purpose | Configuration |
|------|---------|---------|---------------|
| IBM AI Fairness 360 | | | |
| Microsoft Fairlearn | | | |
| Google What-If Tool | | | |
| Aequitas | | | |
| Custom scripts | | | |

### 5.2 Test Data

```
ZALEŻNOŚCI:
├── INPUT: ML-TSE → test set
├── OUTPUT: → Reproducibility documentation
└── NOTE: Test data must include protected attributes
```

| Dataset | Size | Protected Attrs | Period | Source |
|---------|------|-----------------|--------|--------|
| Test Set | | | | |
| Validation Set | | | | |
| Production Sample | | | | |

### 5.3 Testing Procedure

**Step 1: Data Preparation**
```python
# Example code/pseudocode
# Load test data with protected attributes
# Verify group sample sizes
# Check for missing values
```

**Step 2: Baseline Metrics Calculation**
```
[Document baseline calculation methodology]
```

**Step 3: Subgroup Analysis**
```
[Document subgroup analysis approach]
```

**Step 4: Statistical Significance Testing**
```
[Document significance testing approach]
```

### 5.4 Reproducibility

| Element | Location | Version |
|---------|----------|---------|
| Test code | | |
| Test data | | |
| Environment | | |
| Random seeds | | |

---

## SEKCJA 6: DETAILED RESULTS

### 6.1 Overall Model Performance

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: ML-TSE → overall metrics
├── OUTPUT: → Comparison baseline for subgroup analysis
└── OUTPUT: → ML-MDC (Model Card - Sekcja 4)
```

| Metric | Overall | Baseline | Change |
|--------|---------|----------|--------|
| Accuracy | | | |
| Precision | | | |
| Recall | | | |
| F1-Score | | | |
| AUC-ROC | | | |

### 6.2 Subgroup Performance

#### 6.2.1 Performance by Gender

| Gender | n | Accuracy | Precision | Recall | F1 | AUC |
|--------|---|----------|-----------|--------|----|----|
| Male | | | | | | |
| Female | | | | | | |
| Non-binary | | | | | | |
| **Gap (max-min)** | | | | | | |

#### 6.2.2 Performance by Age

| Age Group | n | Accuracy | Precision | Recall | F1 | AUC |
|-----------|---|----------|-----------|--------|----|----|
| <25 | | | | | | |
| 25-44 | | | | | | |
| 45-64 | | | | | | |
| 65+ | | | | | | |
| **Gap (max-min)** | | | | | | |

#### 6.2.3 Performance by [Other Protected Characteristic]

| Group | n | Accuracy | Precision | Recall | F1 | AUC |
|-------|---|----------|-----------|--------|----|----|
| | | | | | | |
| **Gap (max-min)** | | | | | | |

### 6.3 Confusion Matrices by Group

**Template per group:**

| | Predicted Positive | Predicted Negative |
|---|-------------------|-------------------|
| Actual Positive | TP = | FN = |
| Actual Negative | FP = | TN = |

### 6.4 Statistical Significance

| Comparison | Metric | Difference | p-value | Significant |
|------------|--------|------------|---------|-------------|
| Group A vs B | | | | [ ] |

---

## SEKCJA 7: BIAS MITIGATION

### 7.1 Mitigation Strategies Evaluated

```
ZALEŻNOŚCI SEKCJI:
├── INPUT: Bias findings (Sekcja 3, 6)
├── OUTPUT: → ML-BIM (Bias Mitigation Plan)
├── OUTPUT: → ML-MTC (if retraining needed)
└── LIFECYCLE: Re-test after mitigation
```

#### 7.1.1 Pre-processing Techniques

| Technique | Applied | Effect on Bias | Effect on Performance |
|-----------|---------|----------------|----------------------|
| Resampling | [ ] | | |
| Reweighting | [ ] | | |
| Data augmentation | [ ] | | |
| Feature transformation | [ ] | | |

#### 7.1.2 In-processing Techniques

| Technique | Applied | Effect on Bias | Effect on Performance |
|-----------|---------|----------------|----------------------|
| Fairness constraints | [ ] | | |
| Adversarial debiasing | [ ] | | |
| Regularization | [ ] | | |

#### 7.1.3 Post-processing Techniques

| Technique | Applied | Effect on Bias | Effect on Performance |
|-----------|---------|----------------|----------------------|
| Threshold adjustment | [ ] | | |
| Calibration | [ ] | | |
| Reject option | [ ] | | |

### 7.2 Selected Mitigation Approach

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-BIM (detailed implementation)
├── OUTPUT: → ML-MTC (code changes)
└── TRIGGER: Re-testing required after implementation
```

| Mitigation | Rationale | Implementation Status |
|------------|-----------|----------------------|
| | | Planned/In Progress/Complete |

### 7.3 Post-Mitigation Results

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Demographic Parity | | | |
| Equalized Odds | | | |
| Overall Accuracy | | | |

---

## SEKCJA 8: CONCLUSIONS AND RECOMMENDATIONS

### 8.1 Overall Assessment

```
ZALEŻNOŚCI SEKCJI:
├── OUTPUT: → ML-MDC (summary in Model Card)
├── OUTPUT: → ML-EUA (compliance evidence)
├── OUTPUT: → Deployment decision
└── EU AI ACT: Required for HIGH-RISK approval
```

**Fairness Assessment Summary:**

| Criterion | Assessment | Confidence |
|-----------|------------|------------|
| No significant bias detected | [ ] Pass / [ ] Fail | High/Medium/Low |
| All protected groups tested | [ ] Yes / [ ] Partial / [ ] No | |
| Metrics within thresholds | [ ] All / [ ] Most / [ ] Some / [ ] None | |
| Mitigation effective | [ ] Yes / [ ] Partial / [ ] No / [ ] N/A | |

**Overall Verdict:**
```
[ ] APPROVED - Model meets fairness requirements
[ ] CONDITIONAL - Approved with monitoring/mitigation
[ ] REJECTED - Significant bias, requires rework
```

### 8.2 Recommendations

| Priority | Recommendation | Owner | Timeline |
|----------|----------------|-------|----------|
| HIGH | | | |
| MEDIUM | | | |
| LOW | | | |

### 8.3 Monitoring Requirements

```
ZALEŻNOŚCI:
├── OUTPUT: → ML-MMG (monitoring setup)
├── OUTPUT: → ML-MDD (drift detection)
└── EU AI ACT: Art. 72 - post-market monitoring
```

| Metric | Monitoring Frequency | Alert Threshold |
|--------|---------------------|-----------------|
| | | |

### 8.4 Re-testing Triggers

| Trigger | Condition | Action |
|---------|-----------|--------|
| Model retrained | Any retraining | Full re-test |
| Data distribution change | Drift > threshold | Subgroup re-test |
| Incident reported | Bias-related complaint | Targeted re-test |
| Scheduled | Every 6 months | Full re-test |
| Regulatory | EU AI Act audit | Full re-test |

---

## SEKCJA 9: EVIDENCE AND ARTIFACTS

### 9.1 Test Artifacts

| Artifact | Location | Description |
|----------|----------|-------------|
| Test code | | |
| Test data | | |
| Results data | | |
| Visualizations | | |
| Tool outputs | | |

### 9.2 Visualizations

**Include or reference:**
- [ ] ROC curves by group
- [ ] Calibration plots by group
- [ ] Confusion matrix heatmaps
- [ ] Performance gap charts
- [ ] Fairness metric comparisons

---

## LIFECYCLE SUMMARY

```yaml
KIEDY DOKUMENT SIĘ POJAWIA:
  trigger: "Model training completed (ML-MTC)"
  prerequisites:
    - ML-MTC (Model Training Code) complete
    - Test data with protected attributes available
    - ML-AET (AI Ethics Assessment) framework defined
    
KIEDY DOKUMENT ZNIKA/WYGASA:
  triggers:
    - Model retired
    - Model version superseded (new FBT created)
    - Project cancelled
  retention: "10 years (EU AI Act Art. 18)"
  
KIEDY OBOWIĄZUJE:
  conditions:
    - Model in production
    - Model version active
    - HIGH-RISK AI system
    
KIEDY NIE OBOWIĄZUJE:
  conditions:
    - MINIMAL risk systems (optional)
    - Model superseded by new version
    - Model retired
    
AKTUALIZACJE WYMAGANE GDY:
  - Model retrained
  - Training data changed significantly
  - Bias-related incident reported
  - Regulatory requirements change
  - Scheduled re-assessment (every 6 months)
  - New protected groups identified
  
RE-TESTING TRIGGERS:
  - automatic: Model version change
  - automatic: Data drift alert (DDM threshold)
  - manual: Incident report
  - scheduled: Semi-annual review
  - regulatory: Compliance audit
```

---

## APPROVALS

| Role | Name | Date | Signature | Assessment |
|------|------|------|-----------|------------|
| ML Engineer | | | | Technical validity |
| Data Scientist | | | | Methodology |
| Ethics Officer | | | | Ethical compliance |
| Compliance Officer | | | | Regulatory compliance |
| Product Owner | | | | Business acceptance |

---

**END OF TEMPLATE**
