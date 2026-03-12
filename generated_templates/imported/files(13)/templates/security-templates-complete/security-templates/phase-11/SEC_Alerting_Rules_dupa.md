---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-048: Alerting Rules

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-048 |
| **Version** | 1.0 |
| **Owner** | SOC Manager |
| **NIST CSF** | DE.AE |

---

## 1. ALERT CATALOG

| Rule ID | Name | Severity | MITRE | Threshold |
|---------|------|----------|-------|-----------|
| ALT-001 | Brute force attack | High | T1110 | >10 failures/5min |
| ALT-002 | Impossible travel | Medium | T1078 | Distance/time impossible |
| ALT-003 | Malware detected | High | T1204 | EDR detection |
| ALT-004 | Data exfiltration | Critical | T1048 | >100MB outbound |
| ALT-005 | Privilege escalation | High | T1068 | Admin rights granted |
| ALT-006 | After-hours access | Low | T1078 | Access outside hours |

## 2. ALERT ROUTING

| Severity | Destination | Response SLA |
|----------|-------------|--------------|
| Critical | PagerDuty + SOAR | 15 min |
| High | Slack #security + Queue | 1 hour |
| Medium | Queue | 4 hours |
| Low | Queue | 24 hours |

## 3. TUNING PROCESS
1. Weekly false positive review
2. Threshold adjustment
3. Whitelist management
4. Documentation update
