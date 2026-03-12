---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-041: Security Patching Procedure

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-041 |
| **Version** | 1.0 |
| **Owner** | IT Operations |
| **NIST CSF** | PR.IP |
| **ISO 27001** | A.8.8 |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Operations | Patch mgmt program |
| **Active** | Monthly cycle | Patch Tuesday |
| **Review** | Quarterly | Process improvement |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| SEC-039 Vulnerability Management | Vulnerability input |

### Downstream
| Document | Relationship |
|----------|--------------|
| SEC-107 Change Request | Change tracking |

---

## 1. PATCHING SCHEDULE
| Environment | Frequency | Window |
|-------------|-----------|--------|
| Development | Weekly | Anytime |
| Test | Bi-weekly | Business hours |
| Production | Monthly | Maintenance window |

## 2. EMERGENCY PATCHING
| Criteria | Response |
|----------|----------|
| CVSS 9.0+ actively exploited | 24-48 hours |
| CVSS 9.0+ | 7 days |

## 3. ROLLBACK PROCEDURE
[Steps for patch rollback]
