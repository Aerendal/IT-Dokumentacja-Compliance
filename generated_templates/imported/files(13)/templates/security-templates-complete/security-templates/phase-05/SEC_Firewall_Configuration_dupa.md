---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-021: Firewall Configuration

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-021 |
| **Version** | 1.0 |
| **Classification** | Restricted |
| **Owner** | Network Security Engineer |
| **NIST CSF** | PR.AC-5, PR.PT-4 |
| **ISO 27001** | A.8.20, A.8.21 |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Implementation phase | Network design approved |
| **Active** | Firewall operation | Rules deployed |
| **Review** | Quarterly | Rule review |
| **Superseded** | Architecture change | Network redesign |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| SEC-013 Network Security Design | Architecture |

### Downstream
| Document | Relationship |
|----------|--------------|
| SEC-027 Security Configuration Testing | Testing |
| SEC-046 Security Monitoring Strategy | Logging |

---

## 1. FIREWALL ARCHITECTURE

### 1.1 Firewall Topology
```
INTERNET
    │
    ▼
┌─────────────┐
│  EDGE FW    │ ← External firewall
└──────┬──────┘
       │
┌──────▼──────┐
│    DMZ      │
└──────┬──────┘
       │
┌──────▼──────┐
│ INTERNAL FW │ ← Internal firewall
└──────┬──────┘
       │
   ┌───┴───┐
   ▼       ▼
┌─────┐ ┌─────┐
│ APP │ │ DATA│
└─────┘ └─────┘
```

### 1.2 Firewall Inventory

| Device | Model | Location | HA | Management IP |
|--------|-------|----------|-----|---------------|
| FW-EDGE-01 | [Model] | [DC] | Primary | [IP] |
| FW-EDGE-02 | [Model] | [DC] | Secondary | [IP] |
| FW-INT-01 | [Model] | [DC] | Primary | [IP] |

---

## 2. RULE SETS

### 2.1 External Firewall Rules

| Rule # | Name | Source | Dest | Port | Action | Log |
|--------|------|--------|------|------|--------|-----|
| 1 | HTTPS-Inbound | Any | DMZ-Web | 443 | Allow | Yes |
| 2 | API-Inbound | Allowed-IPs | DMZ-API | 443 | Allow | Yes |
| 3 | SSH-Admin | Admin-IPs | Mgmt | 22 | Allow | Yes |
| 4 | Block-All | Any | Any | Any | Deny | Yes |

### 2.2 Internal Firewall Rules

| Rule # | Name | Source | Dest | Port | Action | Log |
|--------|------|--------|------|------|--------|-----|
| 1 | DMZ-to-App | DMZ | App-Zone | 8080 | Allow | Yes |
| 2 | App-to-DB | App-Zone | DB-Zone | 5432 | Allow | Yes |
| 3 | Mgmt-SSH | Mgmt | All | 22 | Allow | Yes |
| 4 | Block-All | Any | Any | Any | Deny | Yes |

---

## 3. CHANGE MANAGEMENT

### 3.1 Rule Change Process
1. Request via ticketing system
2. Security review and approval
3. Change window scheduling
4. Implementation with rollback plan
5. Post-change verification

### 3.2 Emergency Change
| Item | Details |
|------|---------|
| Authorization | CISO or delegate |
| Documentation | Within 24 hours |
| Review | Next business day |

---

## 4. LOGGING CONFIGURATION

| Log Type | Destination | Retention |
|----------|-------------|-----------|
| Traffic logs | SIEM | 90 days |
| Rule hits | SIEM | 90 days |
| Admin activity | SIEM | 1 year |
| Denied traffic | SIEM | 30 days |

---

## APPROVAL & SIGN-OFF

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Network Security Engineer | | | |
| CISO | | | |

## REVISION HISTORY
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [DATE] | [Name] | Initial creation |
