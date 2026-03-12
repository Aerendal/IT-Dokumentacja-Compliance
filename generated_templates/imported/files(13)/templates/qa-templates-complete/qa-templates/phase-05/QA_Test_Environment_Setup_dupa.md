---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# QA-020: Test Environment Setup

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | QA-020 |
| **Version** | 1.0 |
| **Owner** | DevOps |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| QA-014 Environment Plan | Requirements |
### Downstream
| Document | Relationship |
|----------|--------------|
| QA-026 Test Execution | Execution |

---

## 1. ENVIRONMENT STATUS
| Environment | Status | URL | Last Refresh |
|-------------|--------|-----|--------------|
| QA | Active | [URL] | [Date] |
| Staging | Active | [URL] | [Date] |
| Performance | Active | [URL] | [Date] |

## 2. CONFIGURATION
| Component | Version | Status |
|-----------|---------|--------|
| App Server | v2.3.1 | Deployed |
| Database | PostgreSQL 14 | Running |
| Cache | Redis 7.0 | Running |
| Queue | RabbitMQ 3.11 | Running |

## 3. SETUP VERIFICATION
| Check | Status | Notes |
|-------|--------|-------|
| App accessible |  | [URL] |
| DB connected |  | |
| Auth working |  | Test accounts |
| Integrations |  | All mocked |

## 4. ACCESS MATRIX
| User | QA | Staging | Performance |
|------|-----|---------|-------------|
| QA Team | Admin | Read | Admin |
| Dev Team | Read | Read | None |
| DevOps | Admin | Admin | Admin |

---

## APPROVAL & SIGN-OFF
| Role | Name | Signature | Date |
|------|------|-----------|------|
| DevOps | | | |
| QA Lead | | | |
