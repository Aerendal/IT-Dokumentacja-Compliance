---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-046: Security Monitoring Strategy

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-046 |
| **Version** | 1.0 |
| **Owner** | SOC Manager |
| **NIST CSF** | DE.CM, DE.AE |
| **ISO 27001** | A.8.15, A.8.16 |

---

## 1. MONITORING SCOPE

### 1.1 Coverage Matrix
| Layer | What to Monitor | Tool | Alert Level |
|-------|-----------------|------|-------------|
| Network | Traffic, flows, DNS | SIEM, NDR | All anomalies |
| Endpoint | Process, file, registry | EDR | High+ severity |
| Identity | Auth, privilege use | SIEM, IdP | All failures |
| Application | Errors, access patterns | APM, SIEM | Critical events |
| Cloud | Config, API, data | CSPM, SIEM | All changes |

## 2. USE CASES (MITRE ATT&CK ALIGNED)

| Tactic | Technique | Detection Rule |
|--------|-----------|----------------|
| Initial Access | Phishing (T1566) | Email attachment analysis |
| Execution | PowerShell (T1059.001) | Encoded command detection |
| Persistence | Scheduled Task (T1053) | New task creation |
| Privilege Escalation | Valid Accounts (T1078) | Anomalous admin login |
| Lateral Movement | RDP (T1021.001) | Unusual RDP connections |
| Exfiltration | Data Transfer (T1041) | Large outbound transfers |

## 3. METRICS AND KPIS

| Metric | Target | Current |
|--------|--------|---------|
| MTTD (Mean Time to Detect) | <1 hour | [X] |
| MTTR (Mean Time to Respond) | <4 hours | [X] |
| Alert-to-Incident ratio | <10:1 | [X] |
| False positive rate | <5% | [X] |
