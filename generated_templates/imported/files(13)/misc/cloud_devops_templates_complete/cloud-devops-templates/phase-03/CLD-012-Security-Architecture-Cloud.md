---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-012: Security Architecture for Cloud

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-012 |
| **Version** | 1.0 |
| **Owner** | [Security Architect / Cloud Architect] |

---

## 1. Security Layers

```
┌─────────────────────────────────────────────────────────────────┐
│                    Defense in Depth                              │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  PERIMETER: WAF, DDoS Protection, CDN                    │   │
│  │  ┌─────────────────────────────────────────────────┐    │   │
│  │  │  NETWORK: VPC, Security Groups, NACLs, VPN      │    │   │
│  │  │  ┌───────────────────────────────────────────┐  │    │   │
│  │  │  │  IDENTITY: IAM, MFA, SSO, RBAC            │  │    │   │
│  │  │  │  ┌─────────────────────────────────────┐  │  │    │   │
│  │  │  │  │  APPLICATION: SAST, DAST, Secrets   │  │  │    │   │
│  │  │  │  │  ┌─────────────────────────────┐   │  │  │    │   │
│  │  │  │  │  │  DATA: Encryption, DLP, KMS │   │  │  │    │   │
│  │  │  │  │  └─────────────────────────────┘   │  │  │    │   │
│  │  │  │  └─────────────────────────────────────┘  │  │    │   │
│  │  │  └───────────────────────────────────────────┘  │    │   │
│  │  └─────────────────────────────────────────────────┘    │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Identity & Access Management

### 2.1 IAM Principles
- Least privilege access
- No long-lived credentials
- MFA for all human access
- Service accounts for automation

### 2.2 Role Structure

| Role | Permissions | Use Case |
|------|-------------|----------|
| Admin | Full access | Break-glass only |
| Developer | Read + limited write | Development |
| Operator | Monitoring + restart | Operations |
| Auditor | Read-only | Compliance |

---

## 3. Network Security

| Control | Implementation |
|---------|----------------|
| Segmentation | VPC, subnets, security groups |
| Micro-segmentation | Service mesh (Istio) |
| Encryption | TLS 1.3 everywhere |
| DDoS Protection | AWS Shield / Cloud Armor |
| WAF | OWASP rules, custom rules |

---

## 4. Data Protection

| Data State | Protection |
|------------|------------|
| At Rest | AES-256 (KMS) |
| In Transit | TLS 1.3 |
| In Use | Confidential computing (optional) |

### 4.1 Key Management

| Key Type | Service | Rotation |
|----------|---------|----------|
| Master Keys | KMS (CMK) | Annual |
| Data Keys | Auto-generated | Per-use |
| Secrets | Secrets Manager | 90 days |

---

## 5. Detection & Response

| Capability | Service | Alert Destination |
|------------|---------|-------------------|
| Threat Detection | GuardDuty | SIEM |
| Config Compliance | AWS Config | Security team |
| Audit Logs | CloudTrail | S3 + SIEM |
| Vulnerability Scanning | Inspector | Security team |

---

## 6. Compliance Controls

| Control | Implementation | Evidence |
|---------|----------------|----------|
| Access Logging | CloudTrail | S3 logs |
| Encryption | KMS | Key policies |
| Network Isolation | VPC, SG | Terraform |
| Vulnerability Mgmt | Inspector | Reports |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial security architecture |
