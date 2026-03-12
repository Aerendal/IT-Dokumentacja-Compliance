---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-021: Cloud Networking Setup

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-021 |
| **Version** | 1.0 |
| **Owner** | [Network Engineer / Platform Engineer] |

---

## 1. VPC Configuration

### 1.1 Production VPC
```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  name = "production-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  single_nat_gateway = false
  
  enable_dns_hostnames = true
  enable_dns_support   = true
}
```

---

## 2. Security Groups

| Name | Inbound | Source |
|------|---------|--------|
| alb-sg | 443 | 0.0.0.0/0 |
| app-sg | 8080 | alb-sg |
| db-sg | 5432 | app-sg |

---

## 3. Route Tables

| Route Table | Destination | Target |
|-------------|-------------|--------|
| Public | 0.0.0.0/0 | Internet Gateway |
| Private | 0.0.0.0/0 | NAT Gateway |
| Private | 10.0.0.0/8 | Local |

---

## 4. DNS Configuration

| Zone | Type | Records |
|------|------|---------|
| company.com | Public | A, CNAME |
| internal.company.com | Private | A, SRV |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial networking setup |
