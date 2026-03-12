---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-007: Cloud Compliance and Regulatory Requirements

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-007 |
| **Version** | 1.0 |
| **Status** | DRAFT / APPROVED |
| **Owner** | [Compliance Officer / Cloud Architect] |

---

## 1. Applicable Regulations

| Regulation | Scope | Impact | Priority |
|------------|-------|--------|----------|
| GDPR | EU personal data | Data residency, DPA | Critical |
| PCI-DSS | Payment card data | Network segmentation | Critical |
| SOC 2 | Service organization | Audit logging | High |
| HIPAA | Healthcare data | BAA, encryption | High |
| ISO 27001 | Information security | Certification | Medium |

---

## 2. Data Residency Requirements

| Data Type | Required Location | Cloud Regions |
|-----------|-------------------|---------------|
| EU Personal Data | EU only | eu-west-1, eu-central-1 |
| US Healthcare | US only | us-east-1, us-west-2 |
| Financial Data | Specific countries | As required |
| General Data | No restriction | Any region |

---

## 3. Security Controls Mapping

### 3.1 GDPR Requirements

| Article | Requirement | Cloud Implementation |
|---------|-------------|---------------------|
| Art. 32 | Encryption | KMS, TLS 1.3 |
| Art. 17 | Right to erasure | Data deletion procedures |
| Art. 33 | Breach notification | CloudTrail, alerts |
| Art. 25 | Privacy by design | Default encryption |

### 3.2 PCI-DSS Requirements

| Requirement | Control | Implementation |
|-------------|---------|----------------|
| 1.3 | Network segmentation | Dedicated VPC, security groups |
| 3.4 | Encrypt stored data | KMS encryption |
| 8.2 | MFA | IAM + MFA required |
| 10.1 | Audit trails | CloudTrail enabled |

---

## 4. Cloud Provider Certifications

| Certification | AWS | Azure | GCP |
|---------------|-----|-------|-----|
| SOC 1/2/3 |  |  |  |
| ISO 27001 |  |  |  |
| PCI-DSS |  |  |  |
| HIPAA |  (BAA) |  (BAA) |  (BAA) |
| FedRAMP |  |  |  |

---

## 5. Compliance Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  Compliance Architecture                         │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    PCI-DSS Scope                         │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │   │
│  │  │ Payment App │  │ Payment DB  │  │ HSM/KMS     │     │   │
│  │  │ Isolated VPC│  │ Encrypted   │  │ Key Mgmt    │     │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    GDPR Scope (EU)                       │   │
│  │  ┌─────────────┐  ┌─────────────┐                       │   │
│  │  │ EU Region   │  │ Data Lake   │  Data Residency: EU   │   │
│  │  │ eu-west-1   │  │ Encrypted   │  DPA in place         │   │
│  │  └─────────────┘  └─────────────┘                       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    General Workloads                     │   │
│  │  Standard security controls, logging, encryption         │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. Required Cloud Controls

| Control | Service | Configuration |
|---------|---------|---------------|
| Encryption at Rest | KMS | AES-256, CMK |
| Encryption in Transit | ALB/NLB | TLS 1.2+ |
| Access Logging | CloudTrail | All regions, S3 |
| Network Logging | VPC Flow Logs | All VPCs |
| Vulnerability Scanning | Inspector | Weekly |
| Configuration Compliance | Config | Continuous |

---

## 7. Audit Requirements

| Audit Type | Frequency | Scope | Owner |
|------------|-----------|-------|-------|
| Internal Audit | Quarterly | All controls | Internal Audit |
| External Audit (SOC 2) | Annual | Full platform | External Auditor |
| PCI-DSS QSA | Annual | Cardholder environment | QSA |
| Penetration Test | Annual | External + Internal | Security Team |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial compliance requirements |
