---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-022: Cloud Security Implementation

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-022 |
| **Version** | 1.0 |
| **Owner** | [Security Engineer] |

---

## 1. IAM Configuration

### 1.1 IAM Policies
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::app-bucket/*"
    }
  ]
}
```

### 1.2 IAM Roles
| Role | Trust | Policies |
|------|-------|----------|
| ec2-app-role | EC2 | S3ReadWrite, SSM |
| lambda-role | Lambda | S3Read, DynamoDB |
| eks-node-role | EC2 | EKS Worker Policy |

---

## 2. Encryption Configuration

### 2.1 KMS Keys
| Key | Purpose | Rotation |
|-----|---------|----------|
| app-data-key | S3, EBS encryption | Annual |
| db-key | RDS encryption | Annual |
| secrets-key | Secrets Manager | Annual |

### 2.2 S3 Encryption
```hcl
resource "aws_s3_bucket_server_side_encryption_configuration" "example" {
  bucket = aws_s3_bucket.example.id
  rule {
    apply_server_side_encryption_by_default {
      kms_master_key_id = aws_kms_key.app_key.arn
      sse_algorithm     = "aws:kms"
    }
  }
}
```

---

## 3. Security Services

| Service | Purpose | Configuration |
|---------|---------|---------------|
| GuardDuty | Threat detection | Enabled, all regions |
| Security Hub | Compliance | CIS, PCI-DSS |
| CloudTrail | Audit logging | All regions, S3 |
| Config | Configuration audit | All resources |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial security implementation |
