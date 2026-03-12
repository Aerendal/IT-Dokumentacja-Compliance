---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-010: Infrastructure as Code (IaC) Design

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-010 |
| **Version** | 1.0 |
| **Status** | DRAFT / APPROVED |
| **Owner** | [Platform Engineer / Cloud Architect] |

---

## 1. IaC Strategy

### 1.1 Tool Selection

| Tool | Use Case | Why |
|------|----------|-----|
| Terraform | Infrastructure provisioning | Multi-cloud, declarative, mature |
| Helm | Kubernetes deployments | K8s native packaging |
| Ansible | Configuration management | Agentless, idempotent |

### 1.2 IaC Principles

| Principle | Description |
|-----------|-------------|
| Declarative | Define desired state, not steps |
| Version Controlled | All code in Git |
| Modular | Reusable modules |
| DRY | Don't Repeat Yourself |
| Immutable | Replace, don't modify |

---

## 2. Repository Structure

```
infrastructure/
├── terraform/
│   ├── modules/
│   │   ├── vpc/
│   │   │   ├── main.tf
│   │   │   ├── variables.tf
│   │   │   └── outputs.tf
│   │   ├── eks/
│   │   ├── rds/
│   │   ├── s3/
│   │   └── security-groups/
│   ├── environments/
│   │   ├── dev/
│   │   │   ├── main.tf
│   │   │   ├── terraform.tfvars
│   │   │   └── backend.tf
│   │   ├── staging/
│   │   └── production/
│   └── global/
│       ├── iam/
│       └── route53/
├── kubernetes/
│   ├── base/
│   ├── overlays/
│   │   ├── dev/
│   │   ├── staging/
│   │   └── production/
│   └── helm-charts/
└── ansible/
    ├── playbooks/
    └── roles/
```

---

## 3. Terraform Standards

### 3.1 Module Structure

```hcl
# modules/vpc/main.tf
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = merge(var.common_tags, {
    Name = "${var.environment}-vpc"
  })
}

resource "aws_subnet" "public" {
  count             = length(var.availability_zones)
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone = var.availability_zones[count.index]

  tags = merge(var.common_tags, {
    Name = "${var.environment}-public-${count.index + 1}"
    Tier = "Public"
  })
}
```

### 3.2 State Management

| Environment | Backend | State File |
|-------------|---------|------------|
| All | S3 + DynamoDB | s3://company-terraform-state/{env}/terraform.tfstate |

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket         = "company-terraform-state"
    key            = "production/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
```

### 3.3 Naming Conventions

| Resource | Pattern | Example |
|----------|---------|---------|
| VPC | {env}-vpc | prod-vpc |
| Subnet | {env}-{tier}-{az} | prod-private-1a |
| Security Group | {env}-{app}-sg | prod-web-sg |
| EC2 | {env}-{app}-{index} | prod-web-001 |
| RDS | {env}-{app}-db | prod-app-db |

---

## 4. GitOps Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                      GitOps Workflow                             │
│                                                                 │
│  Developer ──► Feature Branch ──► Pull Request ──► Review       │
│                                                      │          │
│                                                      ▼          │
│                                               Terraform Plan    │
│                                               (CI Pipeline)     │
│                                                      │          │
│                                                      ▼          │
│                                               Merge to Main     │
│                                                      │          │
│                                                      ▼          │
│                                               Terraform Apply   │
│                                               (CD Pipeline)     │
│                                                      │          │
│                                                      ▼          │
│                                               Infrastructure    │
│                                               Updated           │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. CI/CD Pipeline

```yaml
# .github/workflows/terraform.yml
name: Terraform

on:
  pull_request:
    paths: ['terraform/**']
  push:
    branches: [main]
    paths: ['terraform/**']

jobs:
  terraform:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        
      - name: Terraform Init
        run: terraform init
        
      - name: Terraform Plan
        if: github.event_name == 'pull_request'
        run: terraform plan -no-color
        
      - name: Terraform Apply
        if: github.ref == 'refs/heads/main'
        run: terraform apply -auto-approve
```

---

## 6. Security Controls

| Control | Implementation |
|---------|----------------|
| Secrets | Never in code, use Vault/Secrets Manager |
| State Encryption | S3 server-side encryption |
| Access Control | OIDC for CI/CD, no long-lived credentials |
| Drift Detection | Weekly terraform plan |
| Policy as Code | Sentinel/OPA policies |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial IaC design |
