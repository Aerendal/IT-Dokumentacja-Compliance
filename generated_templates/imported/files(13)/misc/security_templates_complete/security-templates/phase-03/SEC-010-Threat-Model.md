---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-010: Threat Model

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-010 |
| **Version** | 1.0 |
| **Classification** | Confidential |
| **Owner** | Security Architect |
| **NIST CSF** | ID.RA |
| **Methodology** | STRIDE / PASTA |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Design phase | System design initiated |
| **Active** | Development through operation | System active |
| **Review** | Per release + annually | New features, threats |
| **Superseded** | Major architecture change | System redesign |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| SEC-003 Threat Landscape | Threat context |
| SEC-008 Security Architecture | System scope |
| System Design | Technical details |

### Downstream
| Document | Relationship |
|----------|--------------|
| SEC-004 Security Requirements | Requirements derivation |
| SEC-025 Security Testing Plan | Test scenarios |
| SEC-042 IR Playbook | Incident scenarios |

---

## 1. SYSTEM OVERVIEW

### 1.1 Data Flow Diagram
```
┌──────────┐     HTTPS      ┌──────────┐      SQL       ┌──────────┐
│  USER    │───────────────▶│   WEB    │───────────────▶│ DATABASE │
│          │◀───────────────│  SERVER  │◀───────────────│          │
└──────────┘                └──────────┘                └──────────┘
     │                           │                           │
     │                           │                           │
Trust Boundary 1            Trust Boundary 2            Trust Boundary 3
(External)                  (DMZ)                       (Internal)
```

### 1.2 Assets
| Asset | Type | Sensitivity | Location |
|-------|------|-------------|----------|
| Customer PII | Data | High | Database |
| Session tokens | Data | High | Memory |
| API keys | Credential | Critical | Config |
| Application code | Code | Medium | Server |

---

## 2. STRIDE ANALYSIS

### 2.1 Threat Identification

| ID | Element | Threat Type | Threat Description | Mitigation |
|----|---------|-------------|-------------------|------------|
| T1 | User→Web | Spoofing | Credential theft | MFA, TLS |
| T2 | Web→DB | Tampering | SQL injection | Parameterized queries |
| T3 | Database | Repudiation | Unauthorized changes | Audit logging |
| T4 | Data flow | Info Disclosure | Data interception | TLS encryption |
| T5 | Web Server | DoS | Resource exhaustion | Rate limiting, WAF |
| T6 | User | Elevation | Privilege escalation | RBAC, least privilege |

### 2.2 STRIDE Per Element

| Element | S | T | R | I | D | E |
|---------|---|---|---|---|---|---|
| User |  | |  | | | |
| Web Server |  |  |  |  |  |  |
| Database | |  |  |  |  | |
| Data Flow | |  | |  |  | |

---

## 3. RISK RATING

### 3.1 DREAD Scoring

| Threat | Damage | Reproducibility | Exploitability | Affected Users | Discoverability | Total |
|--------|--------|-----------------|----------------|----------------|-----------------|-------|
| T1 | 8 | 7 | 6 | 9 | 5 | 35/High |
| T2 | 9 | 8 | 5 | 10 | 4 | 36/High |
| T3 | 6 | 5 | 4 | 5 | 3 | 23/Med |
| T4 | 7 | 6 | 4 | 8 | 3 | 28/Med |
| T5 | 6 | 9 | 7 | 10 | 7 | 39/High |
| T6 | 9 | 4 | 3 | 5 | 3 | 24/Med |

---

## 4. MITIGATIONS

| Threat | Mitigation | Control Type | Priority | Status |
|--------|------------|--------------|----------|--------|
| T1 | Implement MFA | Preventive | P1 | [ ] |
| T2 | Input validation, parameterized queries | Preventive | P1 | [ ] |
| T3 | Comprehensive audit logging | Detective | P2 | [ ] |
| T4 | TLS 1.3 encryption | Preventive | P1 | [ ] |
| T5 | WAF, rate limiting, DDoS protection | Preventive | P1 | [ ] |
| T6 | RBAC, regular access reviews | Preventive | P2 | [ ] |

---

## 5. ATTACK TREES

### 5.1 Data Breach Attack Tree
```
                    ┌─────────────────────┐
                    │   STEAL DATA        │
                    └──────────┬──────────┘
           ┌───────────────────┼───────────────────┐
           ▼                   ▼                   ▼
    ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
    │ Compromise   │   │ Exploit App  │   │ Insider      │
    │ Credentials  │   │ Vulnerability│   │ Threat       │
    └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
           │                  │                   │
    ┌──────┴──────┐   ┌──────┴──────┐    ┌──────┴──────┐
    │ Phishing    │   │ SQL Inject  │    │ Privileged  │
    │ Brute Force │   │ API Abuse   │    │ Misuse      │
    └─────────────┘   └─────────────┘    └─────────────┘
```

---

## APPROVAL & SIGN-OFF

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Security Architect | | | |
| Development Lead | | | |
| CISO | | | |

## REVISION HISTORY
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [DATE] | [Name] | Initial creation |
