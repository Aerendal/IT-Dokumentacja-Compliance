---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-017: Cloud Resource Planning

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-017 |
| **Version** | 1.0 |
| **Owner** | [Cloud Architect / FinOps] |

---

## 1. Compute Resource Plan

| Workload | Instance Type | Count | Environment |
|----------|---------------|-------|-------------|
| Web Tier | m5.large | 4 | Production |
| App Tier | m5.xlarge | 6 | Production |
| Database | r5.2xlarge | 2 | Production |
| Kubernetes | m5.xlarge | 10-20 | Production |
| Dev/Test | t3.medium | 10 | Non-prod |

---

## 2. Storage Resource Plan

| Type | Capacity | Class | Growth/Year |
|------|----------|-------|-------------|
| S3 Standard | 10 TB | Standard | 50% |
| S3 IA | 50 TB | Infrequent | 100% |
| EBS SSD | 5 TB | gp3 | 30% |
| EFS | 2 TB | Standard | 50% |

---

## 3. Network Resource Plan

| Resource | Specification |
|----------|---------------|
| VPCs | 3 (prod, staging, dev) |
| NAT Gateways | 3 per VPC |
| Data Transfer | 10 TB/month egress |
| Direct Connect | 1 Gbps |

---

## 4. Reserved Capacity

| Resource | Term | Coverage | Savings |
|----------|------|----------|---------|
| EC2 (Compute) | 1 year | 70% | 30% |
| RDS | 1 year | 100% | 35% |
| ElastiCache | 1 year | 100% | 30% |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial resource plan |
