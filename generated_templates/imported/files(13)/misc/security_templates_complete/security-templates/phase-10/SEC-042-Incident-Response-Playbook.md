---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-042: Incident Response Playbook

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-042 |
| **Version** | 1.0 |
| **Classification** | Confidential |
| **Owner** | IR Lead |
| **NIST CSF** | RS.AN, RS.MI, RS.RP |
| **ISO 27001** | A.5.24-A.5.28 |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| SEC-015 IR Plan | Strategic framework |
| SEC-010 Threat Model | Attack scenarios |

### Downstream
| Document | Relationship |
|----------|--------------|
| SEC-068 Incident Postmortem | Post-incident |
| SEC-045 Communication Plan | Stakeholder comms |

---

## 1. PLAYBOOK: RANSOMWARE

### 1.1 Detection Indicators
- Multiple file encryption alerts
- Ransom note files detected
- Unusual process activity (vssadmin, bcdedit)

### 1.2 Immediate Actions (First 30 min)
| Step | Action | Owner |
|------|--------|-------|
| 1 | Isolate affected systems | SOC |
| 2 | Preserve volatile evidence | Forensics |
| 3 | Notify IR Lead | SOC |
| 4 | Activate IR team | IR Lead |

### 1.3 Containment
- Network isolation of affected segments
- Disable compromised accounts
- Block known IOCs at perimeter

### 1.4 Eradication & Recovery
- Restore from clean backups
- Rebuild affected systems
- Reset credentials

---

## 2. PLAYBOOK: PHISHING/BEC

### 2.1 Detection Indicators
- User report of suspicious email
- Email security gateway alert
- Credential harvesting site detected

### 2.2 Response Steps
| Step | Action | Owner |
|------|--------|-------|
| 1 | Quarantine email | Email Admin |
| 2 | Reset user credentials | IAM |
| 3 | Check for lateral movement | SOC |
| 4 | Block sender/domain | Email Security |

---

## 3. PLAYBOOK: DATA BREACH

### 3.1 Detection Indicators
- DLP alert on sensitive data
- Unusual data access patterns
- External report of data exposure

### 3.2 Response Steps
| Step | Action | Owner |
|------|--------|-------|
| 1 | Confirm breach scope | IR Team |
| 2 | Preserve evidence | Forensics |
| 3 | Notify Legal | IR Lead |
| 4 | Begin breach notification process | Legal/Comms |

---

## APPROVAL & SIGN-OFF
| Role | Name | Signature | Date |
|------|------|-----------|------|
| IR Lead | | | |
| CISO | | | |
