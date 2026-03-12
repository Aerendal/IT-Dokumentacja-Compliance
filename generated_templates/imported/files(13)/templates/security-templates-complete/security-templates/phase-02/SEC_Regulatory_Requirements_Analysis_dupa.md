---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-005: Regulatory Requirements Analysis

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-005 |
| **Version** | 1.0 |
| **Classification** | Confidential |
| **Owner** | Compliance Officer / CISO |
| **NIST CSF** | GV.OC, GV.SC |
| **ISO 27001** | A.5.31, A.5.32 |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Requirements phase | Project initiation |
| **Active** | Ongoing | Organization operates in regulated space |
| **Review** | Quarterly + upon regulatory changes | New laws, regulatory updates |
| **Superseded** | Major regulatory overhaul | Significant legal changes |
| **Archived** | Post-compliance cycle | Audit requirements (7+ years) |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| SEC-002 Security Strategy | Compliance context |
| Legal/Regulatory landscape | Primary input |
| Business operations scope | Applicability |

### Downstream
| Document | Relationship |
|----------|--------------|
| SEC-006 Compliance Framework | Framework selection |
| SEC-030 Compliance Audit | Audit scope |
| SEC-085 Audit Checklist | Audit criteria |

---

## 1. REGULATORY LANDSCAPE

### 1.1 Applicable Regulations

| Regulation | Jurisdiction | Applicability | Effective Date | Owner |
|------------|--------------|---------------|----------------|-------|
| **GDPR** | EU/EEA | [ ] Yes [ ] No | May 2018 | DPO |
| **CCPA/CPRA** | California | [ ] Yes [ ] No | Jan 2020/2023 | Legal |
| **HIPAA** | USA (Healthcare) | [ ] Yes [ ] No | 1996/ongoing | CISO |
| **PCI DSS 4.0** | Global (Payments) | [ ] Yes [ ] No | Mar 2024 | CISO |
| **SOX** | USA (Public Co.) | [ ] Yes [ ] No | 2002 | CFO |
| **NIS2** | EU | [ ] Yes [ ] No | Oct 2024 | CISO |
| **DORA** | EU (Financial) | [ ] Yes [ ] No | Jan 2025 | CISO |

### 1.2 Industry-Specific Requirements

| Industry | Regulation | Requirements Summary |
|----------|------------|---------------------|
| Financial | [Specify] | [Requirements] |
| Healthcare | [Specify] | [Requirements] |
| Government | [Specify] | [Requirements] |

---

## 2. DETAILED REQUIREMENTS ANALYSIS

### 2.1 Data Protection (GDPR/Privacy)

| Article | Requirement | Our Status | Gap | Action |
|---------|-------------|------------|-----|--------|
| Art. 5 | Data processing principles | [ ] Compliant | [Gap] | [Action] |
| Art. 6 | Lawful basis for processing | [ ] Compliant | [Gap] | [Action] |
| Art. 17 | Right to erasure | [ ] Compliant | [Gap] | [Action] |
| Art. 25 | Privacy by design | [ ] Compliant | [Gap] | [Action] |
| Art. 32 | Security of processing | [ ] Compliant | [Gap] | [Action] |
| Art. 33 | Breach notification (72hr) | [ ] Compliant | [Gap] | [Action] |

### 2.2 Financial Services (PCI DSS)

| Requirement | Description | Status | Evidence |
|-------------|-------------|--------|----------|
| Req 1 | Install and maintain firewall | [ ] Met | [Link] |
| Req 2 | No vendor defaults | [ ] Met | [Link] |
| Req 3 | Protect stored cardholder data | [ ] Met | [Link] |
| Req 4 | Encrypt transmission | [ ] Met | [Link] |
| Req 5 | Anti-malware | [ ] Met | [Link] |
| Req 6-12 | [Continue] | [ ] Met | [Link] |

### 2.3 Sector-Specific Requirements

| Requirement Source | Key Obligations | Impact |
|--------------------|-----------------|--------|
| [Regulator 1] | [Obligations] | [Impact] |
| [Regulator 2] | [Obligations] | [Impact] |

---

## 3. COMPLIANCE GAP ANALYSIS

### 3.1 Gap Summary

| Category | Total Reqs | Compliant | Partial | Non-Compliant |
|----------|------------|-----------|---------|---------------|
| Data Protection | [X] | [X] | [X] | [X] |
| Access Control | [X] | [X] | [X] | [X] |
| Encryption | [X] | [X] | [X] | [X] |
| Monitoring | [X] | [X] | [X] | [X] |
| Incident Response | [X] | [X] | [X] | [X] |

### 3.2 Critical Gaps

| Gap ID | Regulation | Requirement | Current State | Risk | Remediation |
|--------|------------|-------------|---------------|------|-------------|
| GAP-001 | [Reg] | [Req] | [State] | High | [Action] |
| GAP-002 | [Reg] | [Req] | [State] | High | [Action] |

---

## 4. REGULATORY CALENDAR

| Date | Regulation | Event | Action Required |
|------|------------|-------|-----------------|
| [Date] | [Reg] | Effective date | [Action] |
| [Date] | [Reg] | Annual audit | [Action] |
| [Date] | [Reg] | Renewal | [Action] |

---

## 5. PENALTIES AND RISKS

| Regulation | Max Penalty | Reputational Risk | Business Impact |
|------------|-------------|-------------------|-----------------|
| GDPR | €20M or 4% revenue | High | Operations suspension |
| PCI DSS | $100K/month + card loss | High | Payment processing loss |
| HIPAA | $1.9M per violation | High | License revocation |

---

## APPROVAL & SIGN-OFF

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Compliance Officer | | | |
| Legal Counsel | | | |
| CISO | | | |

## REVISION HISTORY
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [DATE] | [Name] | Initial creation |
