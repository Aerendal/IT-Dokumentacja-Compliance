---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Decommissioning Document

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | [ID] |
| **Version** | 1.0 |
| **Owner** | [Platform Team / Project Lead] |

---

## 1. System Information

| Field | Value |
|-------|-------|
| System Name | [Name] |
| Owner | [Team] |
| Decommission Date | [Date] |
| Replacement | [New system or N/A] |

---

## 2. Pre-Decommission Checklist

- [ ] All data migrated/archived
- [ ] Dependencies identified and updated
- [ ] Stakeholders notified
- [ ] Backup verified
- [ ] Rollback plan documented

---

## 3. Data Handling

| Data Type | Action | Destination | Retention |
|-----------|--------|-------------|-----------|
| User data | Migrate | New system | N/A |
| Logs | Archive | S3 Glacier | 7 years |
| Configs | Archive | Git | Indefinite |

---

## 4. Timeline

| Phase | Date | Action |
|-------|------|--------|
| T-30d | [Date] | Announce deprecation |
| T-14d | [Date] | Final migration |
| T-7d | [Date] | Read-only mode |
| T-0 | [Date] | Shutdown |
| T+30d | [Date] | Resource cleanup |

---

## 5. Sign-off

| Role | Name | Date |
|------|------|------|
| System Owner | | |
| Security | | |
| Compliance | | |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial document |
