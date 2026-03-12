---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# SEC-011: Access Control Design

## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | SEC-011 |
| **Version** | 1.0 |
| **Classification** | Confidential |
| **Owner** | Security Architect / IAM Lead |
| **NIST CSF** | PR.AC |
| **ISO 27001** | A.5.15-A.5.18 |

## DOCUMENT LIFECYCLE
| Stage | Timing | Trigger |
|-------|--------|---------|
| **Created** | Design phase | After requirements |
| **Active** | System operation | Access control deployed |
| **Review** | Quarterly + changes | Role changes, audits |
| **Superseded** | Model change | RBAC→ABAC migration |

## DEPENDENCIES
### Upstream
| Document | Relationship |
|----------|--------------|
| SEC-004 Security Requirements | Access requirements |
| SEC-008 Security Architecture | Architecture context |

### Downstream
| Document | Relationship |
|----------|--------------|
| SEC-014 IAM Design | Implementation details |
| SEC-020 Controls Implementation | Deployment |
| SEC-038 Access Review Procedure | Operations |

---

## 1. ACCESS CONTROL MODEL

### 1.1 Model Selection

| Model | Use Case | Selected |
|-------|----------|----------|
| RBAC (Role-Based) | Standard business access |  Primary |
| ABAC (Attribute-Based) | Dynamic, contextual access |  Enhanced |
| MAC (Mandatory) | Classified environments | [ ] If required |
| DAC (Discretionary) | User-managed sharing | [ ] Limited use |

### 1.2 RBAC Hierarchy
```
┌─────────────────────────────────────────────────────────────────┐
│                    ROLE HIERARCHY                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│                    ┌──────────────────┐                        │
│                    │   SUPER ADMIN    │                        │
│                    └────────┬─────────┘                        │
│                             │                                   │
│            ┌────────────────┼────────────────┐                 │
│            ▼                ▼                ▼                 │
│     ┌──────────┐     ┌──────────┐     ┌──────────┐           │
│     │ SECURITY │     │   IT     │     │ BUSINESS │           │
│     │  ADMIN   │     │  ADMIN   │     │  ADMIN   │           │
│     └────┬─────┘     └────┬─────┘     └────┬─────┘           │
│          │                │                │                   │
│     ┌────┴────┐     ┌────┴────┐     ┌────┴────┐              │
│     │Analyst  │     │Operator │     │Manager  │              │
│     └────┬────┘     └────┬────┘     └────┬────┘              │
│          │                │                │                   │
│          └────────────────┼────────────────┘                   │
│                           ▼                                    │
│                    ┌──────────┐                                │
│                    │   USER   │                                │
│                    └──────────┘                                │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. ROLE DEFINITIONS

### 2.1 Role Matrix

| Role | Description | Permissions | Scope |
|------|-------------|-------------|-------|
| Super Admin | Full system access | All | Global |
| Security Admin | Security configuration | Security settings | Global |
| IT Admin | System administration | System config | Assigned systems |
| Business Admin | Business data management | Business data | Department |
| Analyst | Read and analyze | Read, reports | Assigned data |
| User | Standard access | Read, limited write | Own data |

### 2.2 Permission Matrix

| Resource | Super Admin | Security Admin | IT Admin | User |
|----------|-------------|----------------|----------|------|
| User accounts | CRUD | R | RU | R (self) |
| Security logs | CRUD | CRUD | R | - |
| Application config | CRUD | R | CRUD | - |
| Business data | CRUD | R | R | RU |
| Reports | CRUD | CRUD | R | R |

*CRUD = Create, Read, Update, Delete*

---

## 3. ABAC POLICIES

### 3.1 Attribute Categories

| Category | Attributes |
|----------|------------|
| Subject | Role, Department, Clearance, Location |
| Resource | Classification, Owner, Type |
| Action | Read, Write, Delete, Execute |
| Environment | Time, Network, Device |

### 3.2 Sample ABAC Policies

```
POLICY: High-sensitivity data access
IF Subject.Clearance >= "Confidential"
AND Subject.Department == Resource.Department
AND Environment.Network == "Corporate"
AND Environment.Time BETWEEN "08:00" AND "18:00"
THEN PERMIT Read
```

---

## 4. SEPARATION OF DUTIES

| Function | Role A | Role B | Conflict |
|----------|--------|--------|----------|
| Create user | IT Admin | - | - |
| Approve access | Manager | - | - |
| Provision access | IT Admin | ≠ Manager | SoD enforced |
| Review access | Security | ≠ IT Admin | SoD enforced |
| Delete user | IT Admin | + Security approval | Dual control |

---

## APPROVAL & SIGN-OFF

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Security Architect | | | |
| IAM Lead | | | |
| CISO | | | |

## REVISION HISTORY
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [DATE] | [Name] | Initial creation |
