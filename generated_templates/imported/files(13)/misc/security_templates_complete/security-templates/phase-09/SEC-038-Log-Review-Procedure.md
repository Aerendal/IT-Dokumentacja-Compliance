---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-038: Log Review Procedure

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-038 |
| **Version** | 1.0 |
| **Owner** | SOC Analyst |
| **NIST CSF** | DE.AE |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Operations | SOC operational |
| **Active** | Continuous | Daily operations |
| **Review** | Quarterly | Process improvement |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| SEC-024 SIEM Setup | Log sources |

### Downstream
| Document | Relationship |
|----------|--------------|
| SEC-042 IR Playbook | Incident detection |

---

## 1. LOG REVIEW SCHEDULE
| Log Type | Frequency | Reviewer |
|----------|-----------|----------|
| Authentication | Daily | SOC |
| Firewall | Daily | SOC |
| Privileged access | Daily | SOC |
| Application | Weekly | AppSec |

## 2. REVIEW CHECKLIST
- [ ] Failed authentication attempts
- [ ] After-hours access
- [ ] Privileged account usage
- [ ] Anomalous data transfers

## 3. ESCALATION CRITERIA
[When to escalate findings]
