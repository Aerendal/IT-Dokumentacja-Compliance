---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-028: Cost Optimization Testing

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-028 |
| **Version** | 1.0 |
| **Owner** | [FinOps / Platform Engineer] |

---

## 1. Cost Analysis Tools

| Tool | Purpose | Frequency |
|------|---------|-----------|
| AWS Cost Explorer | Cost analysis | Daily |
| Infracost | IaC cost estimation | Every PR |
| Spot.io / CloudHealth | Optimization | Weekly |

---

## 2. Infracost Integration

```yaml
# .github/workflows/infracost.yml
- name: Infracost
  uses: infracost/actions/setup@v2
  
- name: Generate cost estimate
  run: |
    infracost breakdown --path=terraform/ \
      --format=json --out-file=/tmp/infracost.json
    
- name: Post PR comment
  run: |
    infracost comment github --path=/tmp/infracost.json \
      --github-token=${{ secrets.GITHUB_TOKEN }}
```

---

## 3. Optimization Checks

| Check | Threshold | Action |
|-------|-----------|--------|
| Idle Resources | >7 days | Terminate |
| Oversized Instances | CPU <20% | Right-size |
| Unattached EBS | >1 day | Delete |
| Old Snapshots | >30 days | Archive/Delete |

---

## 4. Right-Sizing Analysis

```bash
# AWS Compute Optimizer recommendations
aws compute-optimizer get-ec2-instance-recommendations \
  --instance-arns arn:aws:ec2:us-east-1:ACCOUNT:instance/i-xxx
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial cost optimization |
