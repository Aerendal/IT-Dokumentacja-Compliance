---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-019: Infrastructure as Code Implementation

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-019 |
| **Version** | 1.0 |
| **Owner** | [Platform Engineer] |

---

## 1. Terraform Configuration

### 1.1 Provider Configuration
```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    bucket         = "terraform-state-bucket"
    key            = "infrastructure/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "Terraform"
      Project     = var.project_name
    }
  }
}
```

### 1.2 Module Usage
```hcl
module "vpc" {
  source = "./modules/vpc"
  
  vpc_cidr           = "10.0.0.0/16"
  availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
  environment        = var.environment
}

module "eks" {
  source = "./modules/eks"
  
  cluster_name    = "${var.environment}-cluster"
  vpc_id          = module.vpc.vpc_id
  subnet_ids      = module.vpc.private_subnet_ids
  node_count      = 3
  instance_type   = "m5.xlarge"
}
```

---

## 2. CI/CD Pipeline

### 2.1 GitHub Actions Workflow
```yaml
name: Terraform Deploy

on:
  push:
    branches: [main]
    paths: ['terraform/**']
  pull_request:
    paths: ['terraform/**']

jobs:
  plan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
      - run: terraform init
      - run: terraform plan -out=plan.tfplan
      - uses: actions/upload-artifact@v4
        with:
          name: plan
          path: plan.tfplan

  apply:
    needs: plan
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v4
      - uses: hashicorp/setup-terraform@v3
      - uses: actions/download-artifact@v4
      - run: terraform apply plan.tfplan
```

---

## 3. State Management

| Environment | State Location | Lock Table |
|-------------|----------------|------------|
| Production | s3://state/prod/ | terraform-locks-prod |
| Staging | s3://state/staging/ | terraform-locks-staging |
| Development | s3://state/dev/ | terraform-locks-dev |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial IaC implementation |
