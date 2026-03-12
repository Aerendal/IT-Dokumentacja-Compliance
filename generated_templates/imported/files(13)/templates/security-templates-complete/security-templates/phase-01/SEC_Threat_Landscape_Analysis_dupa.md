---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-003: Threat Landscape Analysis

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-003 |
| **Version** | 1.0 |
| **Classification** | Confidential |
| **Owner** | Threat Intelligence Lead / CISO |
| **Last Review** | [DATE] |
| **Next Review** | [DATE + 6 months] |
| **NIST CSF** | ID.RA, ID.SC |
| **MITRE ATT&CK** | All Tactics |

## DOCUMENT LIFECYCLE

### Validity Period
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Strategy phase | SEC-002 in progress |
| **Active** | 6-12 months | Threat landscape evolves |
| **Review** | Quarterly or upon major threat | New APT, vulnerability, incident |
| **Superseded** | Major threat shift | Significant landscape change |
| **Archived** | After supersession | Historical reference |

### When This Document Applies
-  Security strategy development
-  Risk assessment activities
-  Threat modeling for new systems
-  Security awareness content creation
-  Incident response planning

### When This Document Does NOT Apply
-  Real-time threat intelligence (use TI feeds)
-  Specific vulnerability remediation (use Vuln reports)
-  Active incident investigation (use IR playbooks)

---

## DOCUMENT DEPENDENCIES

### Cross-Document Dependencies

#### Upstream (Required Inputs)
| Document | Relationship |
|----------|--------------|
| SEC-001 Vision | Industry context |
| Industry threat reports | External intelligence |
| MITRE ATT&CK | Threat framework |
| Threat Intelligence feeds | Current threats |

#### Downstream (Outputs To)
| Document | Relationship |
|----------|--------------|
| SEC-002 Strategy | Risk context |
| SEC-007 Risk Assessment | Threat input |
| SEC-009 Threat Model | Threat scenarios |
| SEC-047 Monitoring Strategy | Detection priorities |
| SEC-043 IR Playbook | Incident scenarios |

---

## 1. EXECUTIVE SUMMARY

### 1.1 Threat Landscape Overview
[Summary of current threat environment relevant to organization]

### 1.2 Key Findings

| Finding | Severity | Trend | Action Required |
|---------|----------|-------|-----------------|
| Ransomware remains #1 threat | Critical | ↑ Increasing | Enhance backup, EDR |
| Supply chain attacks rising | High | ↑ Increasing | Vendor security program |
| Cloud misconfig exploited | High | → Stable | CSPM implementation |
| Insider threats underestimated | Medium | ↑ Increasing | UEBA, DLP deployment |

---

## 2. THREAT ACTOR ANALYSIS

### 2.1 Relevant Threat Actor Categories

| Actor Type | Motivation | Capability | Relevance to Org |
|------------|------------|------------|------------------|
| **Nation-State APT** | Espionage, disruption | Very High | [High/Medium/Low] |
| **Cybercriminal Groups** | Financial gain | High | High |
| **Hacktivists** | Ideology, publicity | Medium | [High/Medium/Low] |
| **Insider Threats** | Various | Medium | Medium |
| **Script Kiddies** | Curiosity, recognition | Low | Low |

### 2.2 Specific Threat Actors of Concern

| Actor | Attribution | TTPs | Target Relevance |
|-------|-------------|------|------------------|
| [APT Group 1] | [Country] | [MITRE ATT&CK IDs] | [Why relevant] |
| [APT Group 2] | [Country] | [MITRE ATT&CK IDs] | [Why relevant] |
| [Ransomware Group] | Cybercrime | [MITRE ATT&CK IDs] | [Why relevant] |

---

## 3. THREAT ANALYSIS BY CATEGORY

### 3.1 Ransomware

| Attribute | Analysis |
|-----------|----------|
| **Current State** | [X] attacks on similar orgs in past year |
| **Attack Vectors** | Phishing, RDP, VPN vulnerabilities |
| **Notable Groups** | LockBit, BlackCat, Cl0p |
| **Average Ransom** | $XXX million |
| **Trend** | ↑ Increasing sophistication, double extortion |
| **Our Exposure** | [High/Medium/Low] |
| **Recommended Controls** | Backup, EDR, network segmentation |

### 3.2 Phishing / Social Engineering

| Attribute | Analysis |
|-----------|----------|
| **Current State** | XX% of breaches start with phishing |
| **Attack Types** | BEC, credential harvesting, malware delivery |
| **Trend** | ↑ AI-generated content, targeted spear-phishing |
| **Our Exposure** | [High/Medium/Low] |
| **Recommended Controls** | SEG, awareness training, MFA |

### 3.3 Supply Chain Attacks

| Attribute | Analysis |
|-----------|----------|
| **Current State** | [Notable recent incidents] |
| **Attack Types** | Software supply chain, MSP compromise |
| **Notable Incidents** | SolarWinds, Kaseya, MOVEit |
| **Trend** | ↑ Significant increase |
| **Our Exposure** | [High/Medium/Low] |
| **Recommended Controls** | Vendor assessment, SBOM, monitoring |

### 3.4 Cloud Security Threats

| Attribute | Analysis |
|-----------|----------|
| **Current State** | XX% of orgs experienced cloud incident |
| **Attack Types** | Misconfiguration, credential theft, API abuse |
| **Trend** | → Stable but significant |
| **Our Exposure** | [High/Medium/Low] |
| **Recommended Controls** | CSPM, CIEM, CNAPP |

### 3.5 Insider Threats

| Attribute | Analysis |
|-----------|----------|
| **Current State** | XX% of incidents involve insiders |
| **Threat Types** | Malicious, negligent, compromised |
| **Trend** | ↑ Increasing (remote work) |
| **Our Exposure** | [High/Medium/Low] |
| **Recommended Controls** | UEBA, DLP, access reviews |

---

## 4. MITRE ATT&CK MAPPING

### 4.1 Top Techniques Observed

| Tactic | Technique | ID | Frequency | Detection Coverage |
|--------|-----------|----|-----------|--------------------|
| Initial Access | Phishing | T1566 | Very High | [%] |
| Initial Access | Exploit Public-Facing App | T1190 | High | [%] |
| Execution | PowerShell | T1059.001 | Very High | [%] |
| Persistence | Scheduled Task | T1053 | High | [%] |
| Privilege Escalation | Valid Accounts | T1078 | High | [%] |
| Defense Evasion | Obfuscated Files | T1027 | High | [%] |
| Credential Access | OS Credential Dumping | T1003 | High | [%] |
| Lateral Movement | Remote Services | T1021 | High | [%] |
| Exfiltration | Exfil Over C2 | T1041 | Medium | [%] |
| Impact | Data Encrypted | T1486 | High | [%] |

### 4.2 Coverage Heat Map

```
MITRE ATT&CK Coverage Assessment
─────────────────────────────────────────────────────
Tactic                │ Detection │ Prevention │ Gap
─────────────────────────────────────────────────────
Initial Access        │    70%    │    60%     │ Med
Execution             │    80%    │    50%     │ Med
Persistence           │    60%    │    40%     │ High
Privilege Escalation  │    50%    │    40%     │ High
Defense Evasion       │    40%    │    30%     │ Crit
Credential Access     │    60%    │    50%     │ Med
Discovery             │    50%    │    20%     │ High
Lateral Movement      │    40%    │    30%     │ Crit
Collection            │    50%    │    40%     │ High
Exfiltration          │    60%    │    50%     │ Med
Impact                │    70%    │    60%     │ Med
─────────────────────────────────────────────────────
```

---

## 5. INDUSTRY-SPECIFIC THREATS

### 5.1 Industry Context
**Industry:** [Your Industry]

### 5.2 Industry-Specific Threats

| Threat | Description | Recent Incidents | Relevance |
|--------|-------------|------------------|-----------|
| [Industry Threat 1] | [Description] | [Incidents] | High |
| [Industry Threat 2] | [Description] | [Incidents] | Medium |

### 5.3 Regulatory Drivers

| Regulation | Security Requirement | Threat Addressed |
|------------|---------------------|------------------|
| [Regulation 1] | [Requirement] | [Threat] |
| [Regulation 2] | [Requirement] | [Threat] |

---

## 6. VULNERABILITY LANDSCAPE

### 6.1 Critical Vulnerabilities (Past 12 Months)

| CVE | CVSS | Affected | Exploitation | Our Status |
|-----|------|----------|--------------|------------|
| CVE-XXXX-XXXXX | 10.0 | [Product] | Active | [Patched/Vulnerable] |
| CVE-XXXX-XXXXX | 9.8 | [Product] | Active | [Patched/Vulnerable] |

### 6.2 Vulnerability Trends

| Category | Trend | Action |
|----------|-------|--------|
| Zero-days | ↑ Increasing | Rapid patching, compensating controls |
| Cloud vulns | → Stable | CSPM, configuration management |
| Supply chain | ↑ Increasing | SBOM, vendor monitoring |

---

## 7. RECOMMENDATIONS

### 7.1 Priority Actions

| Priority | Recommendation | Threat Addressed | Investment |
|----------|----------------|------------------|------------|
| P1 | Implement XDR/EDR | Ransomware, APT | High |
| P1 | Zero Trust initiative | All threats | High |
| P2 | Supply chain security program | Supply chain | Medium |
| P2 | Enhanced phishing protection | Social engineering | Medium |
| P3 | Insider threat program | Insider threats | Medium |

### 7.2 Detection Improvements

| Gap | Current State | Recommended | Timeline |
|-----|---------------|-------------|----------|
| Lateral movement | Limited | Network detection | Q2 |
| Defense evasion | Weak | Advanced EDR | Q1 |
| Persistence | Moderate | Enhanced logging | Q2 |

---

## 8. THREAT INTELLIGENCE SOURCES

### 8.1 Intelligence Feeds

| Source | Type | Frequency | Value |
|--------|------|-----------|-------|
| [Commercial TI vendor] | Commercial | Real-time | High |
| CISA Alerts | Government | As published | High |
| ISAC | Industry | Daily | High |
| Open source (OSINT) | Community | Continuous | Medium |

### 8.2 Information Sharing

| Partner | Type | Information Shared |
|---------|------|-------------------|
| [ISAC name] | Industry | IOCs, TTPs |
| [Partner org] | Bilateral | Threat intel |

---

## APPROVAL & SIGN-OFF

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Threat Intel Lead** | | | |
| **CISO** | | | |

---

## REVISION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [DATE] | [Name] | Initial creation |
