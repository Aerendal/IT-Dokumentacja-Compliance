---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-018: Penetration Testing Schedule

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-018 |
| **Version** | 1.0 |
| **Classification** | Confidential |
| **Owner** | Security Testing Lead |
| **NIST CSF** | ID.RA, PR.IP |
| **ISO 27001** | A.8.8 |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Planning phase | Testing program initiation |
| **Active** | Annual cycle | Testing execution |
| **Review** | Quarterly | Schedule updates |
| **Superseded** | Annual refresh | New cycle |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| SEC-007 Risk Assessment | Target prioritization |
| SEC-010 Threat Model | Attack scenarios |

### Downstream
| Document | Relationship |
|----------|--------------|
| SEC-027 Penetration Testing Report | Findings |
| SEC-037 Vulnerability Management | Remediation |

---

## 1. ANNUAL TESTING CALENDAR

| Quarter | Test Type | Scope | Vendor | Budget |
|---------|-----------|-------|--------|--------|
| Q1 | External network pentest | Internet-facing | [Vendor] | $XXX |
| Q2 | Web application pentest | Tier 1 apps | [Vendor] | $XXX |
| Q3 | Internal network pentest | Corporate network | [Vendor] | $XXX |
| Q4 | Red team exercise | Full enterprise | [Vendor] | $XXX |

---

## 2. TEST TYPES AND SCOPE

### 2.1 External Penetration Test
| Item | Details |
|------|---------|
| Scope | All external IP ranges, domains |
| Methodology | OWASP, PTES |
| Duration | 2 weeks |
| Rules of Engagement | [Link to RoE] |

### 2.2 Web Application Test
| Item | Details |
|------|---------|
| Scope | Tier 1 & 2 web applications |
| Methodology | OWASP ASVS, WSTG |
| Duration | 2 weeks per app |
| Coverage | OWASP Top 10, business logic |

### 2.3 Internal Network Test
| Item | Details |
|------|---------|
| Scope | Internal network, AD |
| Methodology | MITRE ATT&CK |
| Duration | 2 weeks |
| Focus | Lateral movement, privilege escalation |

### 2.4 Red Team Exercise
| Item | Details |
|------|---------|
| Scope | Full enterprise |
| Objectives | [Specific objectives] |
| Duration | 4 weeks |
| Assumed breach | Yes/No |

---

## 3. RULES OF ENGAGEMENT

### 3.1 Boundaries
| Allowed | Prohibited |
|---------|------------|
| Testing in scope systems | DoS attacks |
| Social engineering (with approval) | Physical access attempts |
| Exploitation (controlled) | Third-party systems |

### 3.2 Communication
| Contact | Role | Phone | Email |
|---------|------|-------|-------|
| [Name] | Primary POC | [Phone] | [Email] |
| [Name] | Technical POC | [Phone] | [Email] |
| [Name] | Emergency contact | [Phone] | [Email] |

---

## 4. DELIVERABLES

| Deliverable | Format | Due |
|-------------|--------|-----|
| Kickoff presentation | PPT | Day 1 |
| Daily status updates | Email | Daily |
| Draft report | PDF | Test end +5 days |
| Final report | PDF | Test end +10 days |
| Executive briefing | PPT | Test end +15 days |
| Retest | Report | +60 days |

---

## APPROVAL & SIGN-OFF

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Security Testing Lead | | | |
| CISO | | | |
| Legal | | | |

## REVISION HISTORY
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [DATE] | [Name] | Initial creation |
