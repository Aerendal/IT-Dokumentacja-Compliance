---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-026: Failover Testing

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-026 |
| **Version** | 1.0 |
| **Owner** | [SRE / Platform Engineer] |

---

## 1. Failover Test Scenarios

| Scenario | Method | Expected Recovery |
|----------|--------|-------------------|
| AZ Failure | Terminate instances in one AZ | <30 seconds |
| Database Failover | Force RDS failover | <2 minutes |
| NAT Gateway Failure | Delete NAT Gateway | <5 minutes |
| Region Failover | DNS failover to DR | <5 minutes |

---

## 2. Test Procedures

### 2.1 AZ Failure Test
```bash
# 1. Identify instances in AZ-a
aws ec2 describe-instances \
  --filters "Name=availability-zone,Values=us-east-1a"

# 2. Terminate instances
aws ec2 terminate-instances --instance-ids i-xxx i-yyy

# 3. Monitor recovery
watch -n 5 'kubectl get pods -o wide'

# 4. Verify traffic continues
curl -s https://app.example.com/health
```

### 2.2 Database Failover Test
```bash
# Force RDS failover
aws rds reboot-db-instance \
  --db-instance-identifier production-db \
  --force-failover

# Monitor failover
aws rds describe-events \
  --source-identifier production-db
```

---

## 3. Success Criteria

| Test | Pass Criteria |
|------|---------------|
| AZ Failure | Zero downtime, <30s recovery |
| DB Failover | <2 min downtime, no data loss |
| Region Failover | <5 min downtime, RPO met |

---

## 4. Test Schedule

| Test | Frequency | Window |
|------|-----------|--------|
| AZ Failure | Monthly | Maintenance window |
| DB Failover | Quarterly | Maintenance window |
| Region DR | Annually | Planned event |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial failover testing |
