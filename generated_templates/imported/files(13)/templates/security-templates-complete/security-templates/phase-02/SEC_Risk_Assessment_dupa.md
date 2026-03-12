---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-007: Risk Assessment

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-007 |
| **Version** | 1.0 |
| **Classification** | Confidential |
| **Owner** | Risk Manager / CISO |
| **NIST CSF** | ID.RA, GV.RM |
| **ISO 27001** | Clause 6.1.2, 8.2 |
| **NIST SP** | 800-30, 800-39 |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Requirements phase | Program initiation, new system |
| **Active** | Until next assessment | Ongoing risk management |
| **Review** | Annual + upon major changes | Incidents, new threats, changes |
| **Superseded** | New assessment | Annual cycle |
| **Archived** | Post-assessment | Compliance (7+ years) |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| SEC-003 Threat Landscape | Threat input |
| Asset Inventory | Asset scope |
| SEC-005 Regulatory Requirements | Compliance context |

### Downstream
| Document | Relationship |
|----------|--------------|
| SEC-002 Security Strategy | Strategy input |
| SEC-008 Security Architecture | Design priorities |
| SEC-092 Risk Register | Risk tracking |

---

## 1. EXECUTIVE SUMMARY

### 1.1 Assessment Overview
| Item | Details |
|------|---------|
| Assessment Date | [DATE] |
| Assessment Scope | [Scope description] |
| Methodology | [NIST 800-30 / ISO 27005 / FAIR] |
| Assessor | [Name/Team] |

### 1.2 Risk Summary

| Risk Level | Count | Immediate Action |
|------------|-------|------------------|
| **Critical** | [X] | Executive attention required |
| **High** | [X] | 30-day remediation plan |
| **Medium** | [X] | 90-day remediation plan |
| **Low** | [X] | Accept or address in next cycle |

---

## 2. RISK ASSESSMENT METHODOLOGY

### 2.1 Risk Calculation

**Risk = Likelihood × Impact**

### 2.2 Likelihood Scale

| Level | Score | Description | Frequency |
|-------|-------|-------------|-----------|
| Very High | 5 | Almost certain | >1/year |
| High | 4 | Likely | 1/year |
| Medium | 3 | Possible | 1/3 years |
| Low | 2 | Unlikely | 1/10 years |
| Very Low | 1 | Rare | <1/10 years |

### 2.3 Impact Scale

| Level | Score | Financial | Operational | Reputational |
|-------|-------|-----------|-------------|--------------|
| Critical | 5 | >$10M | Business failure | National media |
| High | 4 | $1M-$10M | Major disruption | Industry news |
| Medium | 3 | $100K-$1M | Service degradation | Local media |
| Low | 2 | $10K-$100K | Minor impact | Limited |
| Negligible | 1 | <$10K | No impact | None |

### 2.4 Risk Matrix

```
         │ IMPACT
LIKELIHOOD│  1    2    3    4    5
──────────┼─────────────────────────
    5     │  5   10   15   20   25
    4     │  4    8   12   16   20
    3     │  3    6    9   12   15
    2     │  2    4    6    8   10
    1     │  1    2    3    4    5

Legend: 1-4 Low │ 5-9 Medium │ 10-15 High │ 16-25 Critical
```

---

## 3. ASSET INVENTORY

### 3.1 Critical Assets

| Asset ID | Asset Name | Type | Owner | Classification | Criticality |
|----------|------------|------|-------|----------------|-------------|
| A-001 | Customer Database | Data | DBA | Confidential | Critical |
| A-002 | Payment System | System | IT | Restricted | Critical |
| A-003 | Email Server | System | IT | Internal | High |
| A-004 | [Asset] | [Type] | [Owner] | [Class] | [Level] |

### 3.2 Asset Valuation

| Asset | CIA Impact | Business Value | Replacement Cost |
|-------|------------|----------------|------------------|
| A-001 | C:5 I:5 A:4 | $XXX | $XXX |
| A-002 | C:5 I:5 A:5 | $XXX | $XXX |

---

## 4. THREAT ANALYSIS

### 4.1 Threat Catalog

| Threat ID | Threat | Source | Target | Likelihood |
|-----------|--------|--------|--------|------------|
| T-001 | Ransomware | External criminal | All systems | High (4) |
| T-002 | Phishing | External | Users | Very High (5) |
| T-003 | Insider theft | Internal | Data | Medium (3) |
| T-004 | DDoS | External | Web services | High (4) |
| T-005 | Supply chain attack | External | Software | Medium (3) |

### 4.2 Threat Actor Profiles

| Actor | Motivation | Capability | Targeting |
|-------|------------|------------|-----------|
| Cybercriminals | Financial | High | Opportunistic |
| Nation-state | Espionage | Very High | Targeted |
| Hacktivists | Ideology | Medium | Targeted |
| Insiders | Various | Medium | Targeted |

---

## 5. VULNERABILITY ANALYSIS

### 5.1 Technical Vulnerabilities

| Vuln ID | Description | CVSS | Affected Assets | Exploitability |
|---------|-------------|------|-----------------|----------------|
| V-001 | Unpatched servers | 9.8 | A-002, A-003 | High |
| V-002 | Weak authentication | 8.1 | A-001 | High |
| V-003 | Missing encryption | 7.5 | A-001 | Medium |

### 5.2 Process Vulnerabilities

| Vuln ID | Description | Impact | Likelihood |
|---------|-------------|--------|------------|
| VP-001 | No security training | High | High |
| VP-002 | Inadequate access reviews | Medium | Medium |

---

## 6. RISK REGISTER

### 6.1 Identified Risks

| Risk ID | Risk Description | Asset | Threat | Vuln | L | I | Score | Level |
|---------|------------------|-------|--------|------|---|---|-------|-------|
| R-001 | Ransomware encryption of production | A-001,A-002 | T-001 | V-001 | 4 | 5 | 20 | Critical |
| R-002 | Data breach via phishing | A-001 | T-002 | VP-001 | 5 | 4 | 20 | Critical |
| R-003 | Insider data theft | A-001 | T-003 | VP-002 | 3 | 4 | 12 | High |
| R-004 | Service outage from DDoS | A-002 | T-004 | - | 4 | 3 | 12 | High |
| R-005 | Supply chain compromise | All | T-005 | - | 3 | 4 | 12 | High |

### 6.2 Risk Heat Map

```
         │ IMPACT
         │ 1     2     3     4     5
─────────┼──────────────────────────────────
    5    │                   R-002
─────────┼──────────────────────────────────
    4    │             R-004 R-003 R-001
─────────┼──────────────────────────────────
    3    │             R-005
─────────┼──────────────────────────────────
    2    │
─────────┼──────────────────────────────────
    1    │
```

---

## 7. RISK TREATMENT PLAN

### 7.1 Treatment Options

| Risk ID | Treatment | Controls | Owner | Due Date | Status |
|---------|-----------|----------|-------|----------|--------|
| R-001 | Mitigate | Backup, EDR, patching | IT | [Date] | In Progress |
| R-002 | Mitigate | MFA, training, SEG | Security | [Date] | Planned |
| R-003 | Mitigate | DLP, UEBA, access review | Security | [Date] | Planned |
| R-004 | Transfer | DDoS protection service | IT | [Date] | Complete |
| R-005 | Mitigate | SBOM, vendor assessment | Security | [Date] | Planned |

### 7.2 Residual Risk

| Risk ID | Inherent Risk | Treatment | Residual Risk | Acceptable? |
|---------|---------------|-----------|---------------|-------------|
| R-001 | 20 (Critical) | Mitigate | 8 (Medium) | Yes |
| R-002 | 20 (Critical) | Mitigate | 10 (High) | Yes |
| R-003 | 12 (High) | Mitigate | 6 (Medium) | Yes |

---

## 8. RISK ACCEPTANCE

### 8.1 Accepted Risks

| Risk ID | Description | Residual Score | Accepted By | Date | Expiry |
|---------|-------------|----------------|-------------|------|--------|
| [ID] | [Description] | [Score] | [Name/Role] | [Date] | [Date] |

---

## APPROVAL & SIGN-OFF

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Risk Manager | | | |
| CISO | | | |
| CIO | | | |

## REVISION HISTORY
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [DATE] | [Name] | Initial assessment |
