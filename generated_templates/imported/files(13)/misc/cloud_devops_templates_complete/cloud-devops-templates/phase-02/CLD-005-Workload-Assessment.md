---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-005: Workload Assessment

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-005 |
| **Version** | 1.0 |
| **Status** | DRAFT / APPROVED |
| **Owner** | [Cloud Architect / Migration Lead] |

---

## 1. Assessment Overview

### 1.1 Scope
| Metric | Count |
|--------|-------|
| Total Applications Assessed | XX |
| Total Servers | XX |
| Total Databases | XX |
| Total Storage (TB) | XX |

### 1.2 Assessment Methodology
1. Discovery and inventory
2. Dependency mapping
3. Technical assessment
4. Business criticality rating
5. Migration strategy recommendation

---

## 2. Application Inventory

### 2.1 Application Catalog

| App ID | Application Name | Owner | Criticality | Users | Technology Stack |
|--------|------------------|-------|-------------|-------|------------------|
| APP-001 | Customer Portal | Team A | Critical | 50,000 | Java, PostgreSQL |
| APP-002 | Internal CRM | Team B | Important | 500 | .NET, SQL Server |
| APP-003 | Analytics Platform | Team C | Important | 100 | Python, Spark |
| APP-004 | Legacy Billing | Team D | Critical | 200 | COBOL, DB2 |

### 2.2 Detailed Assessment Template

```markdown
### Application: [Name]

**General Information**
| Field | Value |
|-------|-------|
| Application ID | |
| Business Owner | |
| Technical Owner | |
| Description | |
| Criticality | Critical / Important / Standard / Low |
| Users | |
| Peak Usage | |

**Technical Profile**
| Component | Details |
|-----------|---------|
| Architecture | Monolithic / Microservices / SOA |
| Language | |
| Framework | |
| Web Server | |
| App Server | |
| Database | |
| Message Queue | |
| File Storage | |

**Infrastructure**
| Resource | Current | Peak |
|----------|---------|------|
| Servers | X | |
| vCPU | X | |
| Memory (GB) | X | |
| Storage (GB) | X | |
| Network (Mbps) | X | |

**Dependencies**
| Direction | System | Type | Criticality |
|-----------|--------|------|-------------|
| Inbound | [System] | API/DB/File | |
| Outbound | [System] | API/DB/File | |

**Migration Assessment**
| Factor | Score (1-5) | Notes |
|--------|-------------|-------|
| Cloud Readiness | | |
| Technical Complexity | | |
| Business Risk | | |
| Data Sensitivity | | |
| Dependency Complexity | | |

**Recommended Strategy:** Rehost / Replatform / Refactor / Repurchase / Retain / Retire
```

---

## 3. Migration Strategy by Application

### 3.1 Strategy Distribution

| Strategy | Count | % | Applications |
|----------|-------|---|--------------|
| Rehost | XX | XX% | APP-001, APP-005 |
| Replatform | XX | XX% | APP-002, APP-003 |
| Refactor | XX | XX% | APP-006 |
| Repurchase | XX | XX% | APP-007 |
| Retain | XX | XX% | APP-004 |
| Retire | XX | XX% | APP-008 |

### 3.2 Migration Complexity Matrix

| Application | Complexity | Effort (weeks) | Risk | Wave |
|-------------|------------|----------------|------|------|
| APP-001 | Low | 2 | Low | 1 |
| APP-002 | Medium | 4 | Medium | 2 |
| APP-003 | High | 8 | High | 3 |
| APP-004 | Very High | 16+ | Critical | 4+ |

---

## 4. Dependency Map

```
┌─────────────────────────────────────────────────────────────────┐
│                    Application Dependencies                      │
│                                                                 │
│  ┌─────────┐     ┌─────────┐     ┌─────────┐                  │
│  │ APP-001 │────►│ APP-002 │────►│   DB-01 │                  │
│  │ Portal  │     │   CRM   │     │PostgreSQL│                  │
│  └─────────┘     └─────────┘     └─────────┘                  │
│       │               │               ▲                        │
│       │               │               │                        │
│       ▼               ▼               │                        │
│  ┌─────────┐     ┌─────────┐     ┌─────────┐                  │
│  │ APP-003 │────►│ Queue   │────►│ APP-004 │                  │
│  │Analytics│     │ Kafka   │     │ Billing │                  │
│  └─────────┘     └─────────┘     └─────────┘                  │
│                                                                 │
│  Legend: ──► Data flow / API call                              │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Risk Assessment

### 5.1 Migration Risks by Application

| Application | Risk Category | Description | Mitigation |
|-------------|---------------|-------------|------------|
| APP-001 | Data Loss | Large database migration | Parallel running |
| APP-002 | Downtime | Complex integrations | Blue-green deployment |
| APP-004 | Compatibility | Legacy COBOL code | Retain initially |

---

## 6. Recommendations

### 6.1 Migration Waves

| Wave | Timeline | Applications | Dependencies |
|------|----------|--------------|--------------|
| Wave 1 | Q1 | APP-001, APP-005 | None |
| Wave 2 | Q2 | APP-002, APP-003 | Wave 1 complete |
| Wave 3 | Q3 | APP-006 | Wave 2 complete |
| Wave 4 | Q4+ | APP-004 | Major refactoring |

### 6.2 Quick Wins
- [Application with low complexity and high value]
- [Dev/Test environments]

### 6.3 Long-term Initiatives
- [Legacy modernization]
- [Data center exit]

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial workload assessment |
