---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-024: SIEM Setup

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-024 |
| **Version** | 1.0 |
| **Classification** | Confidential |
| **Owner** | SOC Manager |
| **NIST CSF** | DE.CM, DE.AE |
| **ISO 27001** | A.8.15, A.8.16 |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Implementation phase | SIEM procurement |
| **Active** | Continuous operation | SIEM operational |
| **Review** | Quarterly | Detection tuning |
| **Superseded** | Platform change | SIEM migration |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| SEC-008 Security Architecture | Integration points |
| SEC-046 Monitoring Strategy | Detection requirements |

### Downstream
| Document | Relationship |
|----------|--------------|
| SEC-042 IR Playbook | Alert response |
| SEC-049 Alerting Rules | Alert configuration |

---

## 1. SIEM ARCHITECTURE

### 1.1 Deployment Overview
```
┌─────────────────────────────────────────────────────────────────────┐
│                        SIEM ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  LOG SOURCES                                                        │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                     │
│  │Firewall│ │ AD  │ │ Web │ │ EDR │ │ Cloud│                      │
│  └───┬───┘ └───┬──┘ └──┬──┘ └──┬──┘ └──┬───┘                      │
│      │         │       │       │       │                           │
│      └─────────┴───────┴───────┴───────┘                           │
│                        │                                            │
│               ┌────────▼────────┐                                  │
│               │  LOG COLLECTOR  │                                  │
│               │   (Forwarder)   │                                  │
│               └────────┬────────┘                                  │
│                        │                                            │
│               ┌────────▼────────┐                                  │
│               │   SIEM CORE     │                                  │
│               │  ┌───────────┐  │                                  │
│               │  │ Parsing   │  │                                  │
│               │  │ Normalize │  │                                  │
│               │  │ Correlate │  │                                  │
│               │  │ Alert     │  │                                  │
│               │  └───────────┘  │                                  │
│               └────────┬────────┘                                  │
│                        │                                            │
│               ┌────────▼────────┐                                  │
│               │     SOAR        │                                  │
│               │  (Automation)   │                                  │
│               └─────────────────┘                                  │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Platform Details
| Component | Product | Version |
|-----------|---------|---------|
| SIEM | [Splunk/Sentinel/etc.] | [Version] |
| Collector | [Product] | [Version] |
| SOAR | [Product] | [Version] |

---

## 2. LOG SOURCES

### 2.1 Onboarded Sources
| Source | Type | Method | EPS | Status |
|--------|------|--------|-----|--------|
| Firewalls | Network | Syslog | 500 | Active |
| Active Directory | Identity | WEF | 200 | Active |
| Web servers | Application | Agent | 100 | Active |
| EDR | Endpoint | API | 1000 | Active |
| Cloud (AWS/Azure) | Cloud | API | 500 | Active |
| VPN | Network | Syslog | 50 | Active |

### 2.2 Parsing and Normalization
| Source | Parser | Fields Extracted |
|--------|--------|------------------|
| Firewall | [Parser name] | src_ip, dst_ip, action, etc. |
| AD | [Parser name] | user, event_id, result, etc. |

---

## 3. USE CASES AND RULES

### 3.1 Detection Rules
| Rule ID | Name | MITRE | Severity | Status |
|---------|------|-------|----------|--------|
| DET-001 | Brute force login | T1110 | High | Active |
| DET-002 | Impossible travel | T1078 | Medium | Active |
| DET-003 | Lateral movement | T1021 | High | Active |
| DET-004 | Data exfiltration | T1048 | Critical | Active |
| DET-005 | Privilege escalation | T1068 | High | Active |

### 3.2 Correlation Rules
| Rule | Sources | Logic | Action |
|------|---------|-------|--------|
| Failed login + success | AD | >5 fails then success | Alert |
| Malware + C2 | EDR + FW | Malware then outbound | Alert + Block |

---

## 4. ALERTING CONFIGURATION

### 4.1 Alert Priorities
| Priority | Response SLA | Notification |
|----------|--------------|--------------|
| Critical | 15 min | PagerDuty + Email |
| High | 1 hour | Slack + Email |
| Medium | 4 hours | Email |
| Low | 24 hours | Queue |

### 4.2 Integration Points
| Destination | Method | Use |
|-------------|--------|-----|
| Ticketing | API | Incident creation |
| Slack | Webhook | Notifications |
| SOAR | API | Automation |
| Dashboard | Native | Visualization |

---

## 5. RETENTION AND STORAGE

| Data Type | Hot (Days) | Warm (Days) | Cold (Days) | Total |
|-----------|------------|-------------|-------------|-------|
| Security events | 30 | 60 | 275 | 365 |
| Network flows | 7 | 23 | - | 30 |
| Raw logs | 7 | 83 | - | 90 |

---

## APPROVAL & SIGN-OFF

| Role | Name | Signature | Date |
|------|------|-----------|------|
| SOC Manager | | | |
| CISO | | | |

## REVISION HISTORY
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [DATE] | [Name] | Initial creation |
