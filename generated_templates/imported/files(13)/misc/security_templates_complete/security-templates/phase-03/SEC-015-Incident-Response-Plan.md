---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-015: Incident Response Plan

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-015 |
| **Version** | 1.0 |
| **Classification** | Confidential |
| **Owner** | CISO / IR Lead |
| **NIST CSF** | RS.AN, RS.CO, RS.MI, RS.RP |
| **NIST SP** | 800-61 Rev3 |
| **ISO 27001** | A.5.24-A.5.28 |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Design phase | IR program initiation |
| **Active** | Ongoing operations | Continuous |
| **Review** | Annual + post-incident | Incidents, exercises |
| **Superseded** | Major process change | IR restructure |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| SEC-002 Security Strategy | Strategic alignment |
| SEC-003 Threat Landscape | Threat context |

### Downstream
| Document | Relationship |
|----------|--------------|
| SEC-042 IR Playbook | Detailed procedures |
| SEC-045 Communication Plan | Stakeholder comms |
| SEC-068 Incident Postmortem | Post-incident |

---

## 1. INCIDENT RESPONSE FRAMEWORK

### 1.1 IR Phases (NIST CSF 2.0 Aligned)
```
┌─────────────────────────────────────────────────────────────────────┐
│                    INCIDENT RESPONSE LIFECYCLE                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐           │
│  │  GOVERN  │──│ IDENTIFY │──│ PROTECT  │──│  DETECT  │           │
│  │          │  │          │  │          │  │          │           │
│  │•Roles    │  │•Assets   │  │•Controls │  │•Monitor  │           │
│  │•Policies │  │•Risks    │  │•Awareness│  │•Analyze  │           │
│  └──────────┘  └──────────┘  └──────────┘  └────┬─────┘           │
│                                                  │                  │
│                                                  ▼                  │
│                              ┌──────────┐  ┌──────────┐            │
│                              │ RESPOND  │──│ RECOVER  │            │
│                              │          │  │          │            │
│                              │•Contain  │  │•Restore  │            │
│                              │•Eradicate│  │•Improve  │            │
│                              │•Mitigate │  │•Lessons  │            │
│                              └──────────┘  └──────────┘            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. INCIDENT CLASSIFICATION

### 2.1 Severity Levels

| Severity | Criteria | Response Time | Examples |
|----------|----------|---------------|----------|
| **SEV-1 Critical** | Business critical impact | 15 min | Active breach, ransomware |
| **SEV-2 High** | Significant impact | 1 hour | Compromised admin account |
| **SEV-3 Medium** | Moderate impact | 4 hours | Malware detection |
| **SEV-4 Low** | Minimal impact | 24 hours | Policy violation |

### 2.2 Incident Categories

| Category | Description | Primary Handler |
|----------|-------------|-----------------|
| Malware | Virus, ransomware, trojan | SOC |
| Phishing | Social engineering attempts | SOC |
| Data Breach | Unauthorized data access | IR Team + Legal |
| DoS/DDoS | Availability attacks | SOC + Network |
| Insider Threat | Employee misuse | IR Team + HR |
| Unauthorized Access | Account compromise | SOC |

---

## 3. ROLES AND RESPONSIBILITIES

### 3.1 IR Team Structure

| Role | Responsibilities | Contact |
|------|------------------|---------|
| IR Lead | Overall coordination | [Contact] |
| SOC Analyst | Initial triage, monitoring | [Contact] |
| Forensics Lead | Evidence collection, analysis | [Contact] |
| Communications Lead | Internal/external comms | [Contact] |
| Legal Liaison | Regulatory, legal guidance | [Contact] |
| IT Lead | System recovery, containment | [Contact] |

### 3.2 RACI Matrix

| Activity | IR Lead | SOC | Forensics | Legal | Comms | IT |
|----------|---------|-----|-----------|-------|-------|-----|
| Detection | I | R | C | I | I | C |
| Triage | A | R | C | I | I | C |
| Containment | A | R | C | C | I | R |
| Investigation | A | C | R | C | I | C |
| Eradication | A | C | C | I | I | R |
| Recovery | A | C | I | I | C | R |
| Communication | A | I | I | C | R | I |
| Postmortem | R | C | C | C | C | C |

---

## 4. RESPONSE PROCEDURES

### 4.1 Initial Response (First 60 Minutes)

| Step | Action | Owner | Time |
|------|--------|-------|------|
| 1 | Alert received, log incident | SOC | T+0 |
| 2 | Initial triage and classification | SOC | T+15 |
| 3 | Escalate per severity | SOC | T+20 |
| 4 | Activate IR team (SEV1/2) | IR Lead | T+30 |
| 5 | Initial containment decision | IR Lead | T+45 |
| 6 | Stakeholder notification | Comms | T+60 |

### 4.2 Containment Strategies

| Strategy | Use Case | Trade-offs |
|----------|----------|------------|
| Isolate system | Active compromise | Service disruption |
| Block network | Lateral movement | Connectivity loss |
| Disable account | Credential compromise | User impact |
| Quarantine endpoint | Malware | User productivity |

---

## 5. COMMUNICATION PLAN

### 5.1 Internal Notifications

| Severity | Notify | Timing | Method |
|----------|--------|--------|--------|
| SEV-1 | C-Suite, Legal, Board | 30 min | Phone + Email |
| SEV-2 | CISO, IT Director | 1 hour | Email + Slack |
| SEV-3 | Security Manager | 4 hours | Email |
| SEV-4 | Team Lead | 24 hours | Ticket |

### 5.2 External Notifications

| Stakeholder | Trigger | Timing | Owner |
|-------------|---------|--------|-------|
| Regulators | Data breach (per law) | 72 hours (GDPR) | Legal |
| Customers | PII affected | Per policy | Comms |
| Law Enforcement | Criminal activity | As needed | Legal |

---

## 6. EVIDENCE HANDLING

### 6.1 Chain of Custody
1. Document who collected what and when
2. Use write blockers for forensic imaging
3. Hash all evidence files
4. Secure storage with access logs
5. Maintain evidence log

### 6.2 Evidence Types
| Type | Collection Method | Retention |
|------|-------------------|-----------|
| Memory | RAM capture | Case duration |
| Disk | Forensic image | 7 years |
| Logs | SIEM export | 1 year min |
| Network | PCAP capture | Case duration |

---

## APPROVAL & SIGN-OFF

| Role | Name | Signature | Date |
|------|------|-----------|------|
| IR Lead | | | |
| CISO | | | |
| General Counsel | | | |

## REVISION HISTORY
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [DATE] | [Name] | Initial creation |
