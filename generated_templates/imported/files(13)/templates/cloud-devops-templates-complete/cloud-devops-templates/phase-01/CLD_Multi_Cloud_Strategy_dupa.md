---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-003: Multi-Cloud Strategy

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-003 |
| **Version** | 1.0 |
| **Owner** | [Cloud Architect] |

---

## 1. Cloud Deployment Model Decision

| Model | Pros | Cons | Recommendation |
|-------|------|------|----------------|
| Single Cloud | Simplicity, discounts | Lock-in | Most orgs |
| Multi-Cloud | Best-of-breed | Complexity | Large enterprise |
| Hybrid | Flexibility, compliance | Network complexity | Regulated |

**Selected Model:** [ ] Single  [ ] Multi-Cloud  [ ] Hybrid

---

## 2. Provider Distribution (If Multi-Cloud)

| Provider | Workloads | Percentage | Rationale |
|----------|-----------|------------|-----------|
| AWS | Core apps, data | 60% | Primary |
| Azure | O365 integration | 25% | Microsoft |
| GCP | Analytics, ML | 15% | BigQuery |

---

## 3. Abstraction Strategy

| Layer | Tool | Lock-in Risk |
|-------|------|--------------|
| IaC | Terraform | Low |
| Containers | Kubernetes | Low |
| Databases | Provider-specific | High |
| Serverless | Provider-specific | High |
| Monitoring | Datadog/Grafana | Low |

---

## 4. Management Strategy

| Function | Tool | Coverage |
|----------|------|----------|
| Cost | CloudHealth | Multi-cloud |
| Security | Prisma Cloud | Multi-cloud |
| Identity | Okta | Federated |
| Observability | Datadog | All |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial strategy |
