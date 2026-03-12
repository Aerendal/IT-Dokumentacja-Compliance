---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-016: Compliance Requirements for ML

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-016 |
| **Version** | 1.0 |
| **Status** | DRAFT / ACTIVE |
| **Owner** | [Compliance / ML Platform Lead] |

---

## 1. Regulatory Landscape

### 1.1 Applicable Regulations

| Regulation | Scope | Key Requirements | Applicability |
|------------|-------|------------------|---------------|
| GDPR | EU data subjects | Data protection, consent, erasure | High |
| CCPA | California residents | Privacy rights, opt-out | High |
| EU AI Act | AI systems in EU | Risk classification, transparency | High |
| SOC2 | Service providers | Security controls | High |
| HIPAA | Healthcare data | PHI protection | If applicable |
| FCRA | Credit decisions | Adverse action notices | If applicable |
| SR 11-7 | Banking | Model risk management | If applicable |

### 1.2 Risk Classification (EU AI Act)

| Risk Level | Description | Our Models | Requirements |
|------------|-------------|------------|--------------|
| Unacceptable | Banned uses | None | Prohibited |
| High-Risk | Critical decisions | Credit, Fraud | Full compliance |
| Limited | Transparency needed | Chatbots | Disclosure |
| Minimal | Low impact | Recommendations | Self-assessment |

---

## 2. Data Protection Requirements

### 2.1 Data Collection

| ID | Requirement | Regulation | Priority |
|----|-------------|------------|----------|
| DC-001 | Document legal basis for data processing | GDPR Art.6 | P0 |
| DC-002 | Obtain consent where required | GDPR Art.7 | P0 |
| DC-003 | Implement data minimization | GDPR Art.5 | P0 |
| DC-004 | Maintain data inventory | GDPR Art.30 | P0 |
| DC-005 | Document data sources and lineage | SOC2 | P1 |

### 2.2 Data Subject Rights

| ID | Requirement | Regulation | Implementation |
|----|-------------|------------|----------------|
| DSR-001 | Right to access | GDPR Art.15 | Data export API |
| DSR-002 | Right to erasure | GDPR Art.17 | Deletion pipeline |
| DSR-003 | Right to rectification | GDPR Art.16 | Update process |
| DSR-004 | Right to portability | GDPR Art.20 | Export format |
| DSR-005 | Right to explanation | GDPR Art.22 | Explainability tools |

### 2.3 Data Retention

| Data Type | Retention Period | Basis |
|-----------|------------------|-------|
| Training data | 3 years | Business need |
| Model artifacts | 7 years | Audit requirement |
| Inference logs | 1 year | Debugging |
| PII data | Per consent | Legal basis |

---

## 3. Model Governance Requirements

### 3.1 Documentation Requirements

| ID | Requirement | Regulation | Deliverable |
|----|-------------|------------|-------------|
| MG-001 | Model documentation | EU AI Act | Model card |
| MG-002 | Training data documentation | EU AI Act | Data card |
| MG-003 | Risk assessment | SR 11-7 | Risk document |
| MG-004 | Performance documentation | SOC2 | Metrics report |
| MG-005 | Change documentation | SOC2 | Change log |

### 3.2 Fairness & Non-Discrimination

| ID | Requirement | Regulation | Metric |
|----|-------------|------------|--------|
| FN-001 | Bias testing on protected attributes | EU AI Act | Demographic parity |
| FN-002 | Disparate impact analysis | ECOA | 80% rule |
| FN-003 | Regular fairness monitoring | EU AI Act | Continuous |
| FN-004 | Bias mitigation documentation | EU AI Act | Mitigation report |

### 3.3 Transparency & Explainability

| ID | Requirement | Regulation | Implementation |
|----|-------------|------------|----------------|
| TE-001 | Model explainability | GDPR Art.22 | SHAP/LIME |
| TE-002 | Decision transparency | EU AI Act | Feature importance |
| TE-003 | Automated decision disclosure | GDPR | User notification |
| TE-004 | Human oversight capability | EU AI Act | Override mechanism |

---

## 4. Security Requirements

### 4.1 Access Control

| ID | Requirement | Regulation | Implementation |
|----|-------------|------------|----------------|
| AC-001 | Role-based access | SOC2 | RBAC system |
| AC-002 | Least privilege | SOC2 | Access reviews |
| AC-003 | MFA for sensitive access | SOC2 | MFA enforcement |
| AC-004 | Access logging | SOC2, GDPR | Audit logs |

### 4.2 Data Security

| ID | Requirement | Regulation | Implementation |
|----|-------------|------------|----------------|
| DS-001 | Encryption at rest | SOC2, GDPR | AES-256 |
| DS-002 | Encryption in transit | SOC2, GDPR | TLS 1.3 |
| DS-003 | Key management | SOC2 | KMS/Vault |
| DS-004 | Data masking/anonymization | GDPR | PII handling |

---

## 5. Audit Requirements

### 5.1 Audit Trail

| Event | Data Captured | Retention |
|-------|---------------|-----------|
| Model training | Params, data version, user | 7 years |
| Model deployment | Version, approver, time | 7 years |
| Predictions (high-risk) | Input hash, output, time | 7 years |
| Data access | User, resource, time | 3 years |
| Configuration changes | Before/after, user | 7 years |

### 5.2 Audit Reports

| Report | Frequency | Audience |
|--------|-----------|----------|
| Model inventory | Quarterly | Compliance |
| Access review | Quarterly | Security |
| Fairness assessment | Quarterly | Ethics board |
| Incident summary | Monthly | Management |

---

## 6. Compliance Checklist by Model Tier

### Tier 1 (High-Risk) Models

- [ ] Full model card documentation
- [ ] Bias testing completed
- [ ] Explainability implemented
- [ ] Human oversight mechanism
- [ ] Quarterly compliance review
- [ ] Governance board approval
- [ ] Audit trail complete

### Tier 2 (Medium-Risk) Models

- [ ] Standard model card
- [ ] Basic bias testing
- [ ] Feature importance available
- [ ] Semi-annual review
- [ ] Manager approval

### Tier 3 (Low-Risk) Models

- [ ] Minimal documentation
- [ ] Annual review
- [ ] Self-certification

---

## 7. Compliance Monitoring

### 7.1 Key Metrics

| Metric | Target | Frequency |
|--------|--------|-----------|
| Models with complete documentation | 100% | Monthly |
| Bias tests passing | 100% | Continuous |
| Access reviews completed | 100% | Quarterly |
| Audit findings resolved | 100% in 30 days | Monthly |

### 7.2 Non-Compliance Handling

| Severity | Response Time | Escalation |
|----------|---------------|------------|
| Critical | 24 hours | CISO, Legal |
| High | 7 days | Compliance Lead |
| Medium | 30 days | Team Lead |
| Low | 90 days | Owner |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial requirements |
