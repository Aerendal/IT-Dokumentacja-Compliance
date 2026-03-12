---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-020: Cloud Resource Provisioning Guide

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-020 |
| **Version** | 1.0 |
| **Owner** | [Platform Engineer] |

---

## 1. Resource Provisioning Process

```
Request ──► Approval ──► IaC Code ──► PR Review ──► Apply ──► Verify
```

---

## 2. Standard Resources

### 2.1 EC2 Instance
```bash
# Via Terraform
terraform apply -target=module.ec2

# Via AWS CLI (emergency only)
aws ec2 run-instances \
  --image-id ami-xxx \
  --instance-type m5.large \
  --subnet-id subnet-xxx \
  --security-group-ids sg-xxx \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=app-server}]'
```

### 2.2 RDS Database
```hcl
module "rds" {
  source = "./modules/rds"
  
  identifier     = "app-database"
  engine         = "postgres"
  engine_version = "15.4"
  instance_class = "db.r5.large"
  allocated_storage = 100
  multi_az       = true
}
```

### 2.3 S3 Bucket
```hcl
module "s3" {
  source = "./modules/s3"
  
  bucket_name = "company-app-data"
  versioning  = true
  encryption  = "aws:kms"
}
```

---

## 3. Provisioning Checklist

- [ ] Resource request approved
- [ ] IaC code written
- [ ] Security review completed
- [ ] Cost estimate reviewed
- [ ] PR merged
- [ ] Resource deployed
- [ ] Monitoring configured
- [ ] Documentation updated

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial provisioning guide |
