---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-014: High Availability Design

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-014 |
| **Version** | 1.0 |
| **Owner** | [Cloud Architect] |

---

## 1. HA Components

### 1.1 Compute HA
| Component | HA Mechanism |
|-----------|--------------|
| EC2/VMs | Auto Scaling Group across AZs |
| Kubernetes | Multi-AZ node groups |
| Lambda | Regional service (multi-AZ) |

### 1.2 Database HA
| Database | HA Configuration |
|----------|------------------|
| RDS | Multi-AZ deployment |
| ElastiCache | Cluster mode with replicas |
| DocumentDB | 3-node replica set |

### 1.3 Storage HA
| Storage | Durability | Availability |
|---------|------------|--------------|
| S3 | 99.999999999% | 99.99% |
| EFS | 99.999999999% | 99.99% (Multi-AZ) |

---

## 2. Load Balancing

### 2.1 Application Load Balancer
```yaml
Type: AWS::ElasticLoadBalancingV2::LoadBalancer
Properties:
  Type: application
  Subnets: [subnet-az-a, subnet-az-b, subnet-az-c]
  SecurityGroups: [sg-alb]
```

### 2.2 Health Checks
| Check | Interval | Threshold |
|-------|----------|-----------|
| HTTP /health | 30s | 3 failures |
| TCP port | 10s | 2 failures |

---

## 3. Auto Scaling

### 3.1 Scaling Policies
| Metric | Scale Out | Scale In |
|--------|-----------|----------|
| CPU | >70% for 5 min | <30% for 15 min |
| Memory | >80% for 5 min | <40% for 15 min |
| Request Count | >1000/min | <200/min |

---

## 4. Failover Testing

| Test | Frequency | Method |
|------|-----------|--------|
| AZ Failure | Monthly | Terminate instances in one AZ |
| DB Failover | Quarterly | Force RDS failover |
| Region Failover | Annually | Full DR test |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial HA design |
