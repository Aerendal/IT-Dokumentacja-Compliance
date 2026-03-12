---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-006: Compliance Framework Selection

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-006 |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Owner** | CISO / Compliance Officer |
| **NIST CSF** | GV.OC-01, GV.OC-02 |
| **ISO 27001** | Clause 4.1, 4.2 |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Requirements phase | Security program initiation |
| **Active** | 3-5 years | Until framework update |
| **Review** | Annual + framework updates | New versions, business changes |
| **Superseded** | Framework migration | Major version changes |
| **Archived** | Post-transition | Historical reference |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| SEC-002 Security Strategy | Strategic alignment |
| SEC-005 Regulatory Requirements | Compliance drivers |
| Business requirements | Operational context |

### Downstream
| Document | Relationship |
|----------|--------------|
| SEC-008 Security Architecture | Design framework |
| SEC-030 Compliance Audit | Audit criteria |
| SEC-054 Compliance Matrix | Control mapping |

---

## 1. FRAMEWORK EVALUATION

### 1.1 Framework Comparison Matrix

| Framework | Scope | Industry Fit | Certification | Cost | Complexity |
|-----------|-------|--------------|---------------|------|------------|
| **NIST CSF 2.0** | Comprehensive | All | No (voluntary) | Low | Medium |
| **ISO 27001:2022** | ISMS | All | Yes | Medium | High |
| **SOC 2 Type II** | Service Orgs | SaaS/Cloud | Yes | High | High |
| **CIS Controls v8** | Technical | All | No | Low | Low |
| **COBIT 2019** | IT Governance | Enterprise | Yes | High | High |
| **PCI DSS 4.0** | Payment | Payment processors | Yes | High | High |

### 1.2 Coverage Analysis

| Control Domain | NIST CSF | ISO 27001 | SOC 2 | CIS | Selection |
|----------------|----------|-----------|-------|-----|-----------|
| Governance |  GV |  Clause 5 |  CC |  1 | [Choice] |
| Risk Management |  ID.RA |  6.1 |  CC3 | - | [Choice] |
| Access Control |  PR.AC |  A.5.15 |  CC6 |  5,6 | [Choice] |
| Data Protection |  PR.DS |  A.5.33 |  CC6 |  3 | [Choice] |
| Incident Response |  RS |  A.5.24 |  CC7 |  17 | [Choice] |

---

## 2. SELECTED FRAMEWORKS

### 2.1 Primary Framework
**Framework:** [NIST CSF 2.0 / ISO 27001:2022 / etc.]

**Justification:**
1. [Reason 1 - regulatory requirement]
2. [Reason 2 - industry standard]
3. [Reason 3 - customer requirement]
4. [Reason 4 - certification need]

### 2.2 Supplementary Frameworks

| Framework | Purpose | Integration Approach |
|-----------|---------|---------------------|
| [Framework 1] | [Purpose] | [How integrated] |
| [Framework 2] | [Purpose] | [How integrated] |

### 2.3 Framework Mapping

```
┌─────────────────────────────────────────────────────────────┐
│              FRAMEWORK HIERARCHY                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           PRIMARY: [NIST CSF 2.0]                   │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐            │   │
│  │  │ GOVERN  │  │IDENTIFY │  │ PROTECT │            │   │
│  │  └────┬────┘  └────┬────┘  └────┬────┘            │   │
│  │       │            │            │                  │   │
│  │  ┌────┴────┐  ┌────┴────┐  ┌────┴────┐            │   │
│  │  │ DETECT  │  │ RESPOND │  │ RECOVER │            │   │
│  │  └─────────┘  └─────────┘  └─────────┘            │   │
│  └─────────────────────────────────────────────────────┘   │
│                          │                                  │
│           ┌──────────────┼──────────────┐                  │
│           ▼              ▼              ▼                  │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐       │
│  │ ISO 27001    │ │ CIS Controls │ │ PCI DSS      │       │
│  │ (Certif.)    │ │ (Technical)  │ │ (Payment)    │       │
│  └──────────────┘ └──────────────┘ └──────────────┘       │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. IMPLEMENTATION APPROACH

### 3.1 Phased Rollout

| Phase | Framework Focus | Timeline | Deliverables |
|-------|-----------------|----------|--------------|
| Phase 1 | Core controls (CIS 1-6) | Q1-Q2 | Baseline security |
| Phase 2 | Full NIST CSF mapping | Q2-Q3 | Gap remediation |
| Phase 3 | ISO 27001 certification | Q3-Q4 | Certified ISMS |

### 3.2 Resource Requirements

| Resource | Phase 1 | Phase 2 | Phase 3 |
|----------|---------|---------|---------|
| Personnel | [X] FTE | [X] FTE | [X] FTE |
| Tools | $[X] | $[X] | $[X] |
| Consulting | $[X] | $[X] | $[X] |
| Training | $[X] | $[X] | $[X] |
| **Total** | $[X] | $[X] | $[X] |

---

## 4. SUCCESS CRITERIA

| Criteria | Metric | Target | Measurement |
|----------|--------|--------|-------------|
| Framework coverage | % controls implemented | 100% | Control assessment |
| Certification | Certification achieved | Yes | Audit result |
| Compliance score | Audit findings | 0 critical | Audit report |
| Maturity | Maturity level | Level 3+ | Assessment |

---

## APPROVAL & SIGN-OFF

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CISO | | | |
| CIO | | | |
| CEO | | | |

## REVISION HISTORY
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [DATE] | [Name] | Initial creation |
