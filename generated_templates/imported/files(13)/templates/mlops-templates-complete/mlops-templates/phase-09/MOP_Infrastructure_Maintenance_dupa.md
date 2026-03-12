---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-033: MLOps Infrastructure Maintenance

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-033 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Maintenance Schedule

### 1.1 Regular Maintenance Windows

| Type | Schedule | Duration | Impact |
|------|----------|----------|--------|
| Weekly | Tuesday 02:00-04:00 UTC | 2h | Minimal |
| Monthly | 1st Saturday 02:00-06:00 UTC | 4h | Moderate |
| Quarterly | Last Saturday of quarter | 8h | Significant |

### 1.2 Maintenance Calendar

```
Week 1: Routine checks, minor updates
Week 2: Database maintenance, cleanup
Week 3: Security patches (if available)
Week 4: Performance optimization, capacity review
```

---

## 2. Database Maintenance

### 2.1 PostgreSQL (MLflow)

```bash
#!/bin/bash
# maintenance/postgres_maintenance.sh

DB_HOST="mlflow-db.example.com"
DB_NAME="mlflow"

echo "=== PostgreSQL Maintenance ==="

# 1. Vacuum and analyze
echo "[1/4] Running VACUUM ANALYZE..."
psql -h $DB_HOST -d $DB_NAME -c "VACUUM ANALYZE;"

# 2. Reindex if needed
echo "[2/4] Checking index bloat..."
psql -h $DB_HOST -d $DB_NAME -c "
SELECT schemaname, tablename, 
       pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables 
WHERE schemaname = 'public'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC
LIMIT 10;
"

# 3. Update statistics
echo "[3/4] Updating statistics..."
psql -h $DB_HOST -d $DB_NAME -c "ANALYZE VERBOSE;"

# 4. Check for long-running queries
echo "[4/4] Checking long-running queries..."
psql -h $DB_HOST -d $DB_NAME -c "
SELECT pid, now() - pg_stat_activity.query_start AS duration, query
FROM pg_stat_activity
WHERE state = 'active' AND now() - pg_stat_activity.query_start > interval '5 minutes';
"

echo "=== PostgreSQL Maintenance Complete ==="
```

### 2.2 Redis (Feature Store)

```bash
#!/bin/bash
# maintenance/redis_maintenance.sh

REDIS_HOST="redis.example.com"

echo "=== Redis Maintenance ==="

# 1. Check memory usage
echo "[1/3] Memory usage..."
redis-cli -h $REDIS_HOST INFO memory | grep used_memory_human

# 2. Check key count
echo "[2/3] Key statistics..."
redis-cli -h $REDIS_HOST DBSIZE

# 3. Cleanup expired keys (if using lazy expiration)
echo "[3/3] Running active defrag..."
redis-cli -h $REDIS_HOST CONFIG SET activedefrag yes
sleep 60
redis-cli -h $REDIS_HOST CONFIG SET activedefrag no

echo "=== Redis Maintenance Complete ==="
```

---

## 3. Storage Maintenance

### 3.1 S3 Artifact Cleanup

```python
# maintenance/s3_cleanup.py
import boto3
from datetime import datetime, timedelta

def cleanup_old_artifacts(bucket: str, prefix: str, days: int = 90):
    """Clean up old ML artifacts."""
    s3 = boto3.client('s3')
    cutoff = datetime.now() - timedelta(days=days)
    
    deleted = []
    paginator = s3.get_paginator('list_objects_v2')
    
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get('Contents', []):
            if obj['LastModified'].replace(tzinfo=None) < cutoff:
                # Check if referenced by any model
                if not is_artifact_in_use(obj['Key']):
                    s3.delete_object(Bucket=bucket, Key=obj['Key'])
                    deleted.append(obj['Key'])
    
    return deleted

def cleanup_orphaned_experiments():
    """Remove artifacts from deleted experiments."""
    import mlflow
    client = mlflow.tracking.MlflowClient()
    
    # Get all experiment IDs
    valid_exp_ids = {e.experiment_id for e in client.search_experiments()}
    
    # Check S3 for orphaned directories
    s3 = boto3.client('s3')
    for prefix in list_experiment_prefixes():
        exp_id = extract_exp_id(prefix)
        if exp_id not in valid_exp_ids:
            delete_prefix(BUCKET, prefix)
```

### 3.2 Log Rotation

```yaml
# k8s/log-rotation-cronjob.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: log-rotation
  namespace: mlops
spec:
  schedule: "0 3 * * *"  # Daily at 3 AM
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: log-rotator
            image: mlops/maintenance:latest
            command:
              - /bin/bash
              - -c
              - |
                # Compress logs older than 7 days
                find /var/log/mlops -name "*.log" -mtime +7 -exec gzip {} \;
                # Delete compressed logs older than 30 days
                find /var/log/mlops -name "*.log.gz" -mtime +30 -delete
          restartPolicy: OnFailure
```

---

## 4. Kubernetes Maintenance

### 4.1 Node Maintenance

```bash
#!/bin/bash
# maintenance/node_maintenance.sh

NODE=$1

echo "=== Node Maintenance: $NODE ==="

# 1. Cordon node
echo "[1/5] Cordoning node..."
kubectl cordon $NODE

# 2. Drain workloads
echo "[2/5] Draining workloads..."
kubectl drain $NODE --ignore-daemonsets --delete-emptydir-data

# 3. Perform maintenance (patches, etc.)
echo "[3/5] Node ready for maintenance..."
# ... maintenance tasks ...

# 4. Uncordon node
echo "[4/5] Uncordoning node..."
kubectl uncordon $NODE

# 5. Verify node ready
echo "[5/5] Verifying node status..."
kubectl get node $NODE

echo "=== Node Maintenance Complete ==="
```

### 4.2 Pod Cleanup

```bash
#!/bin/bash
# maintenance/pod_cleanup.sh

echo "=== Pod Cleanup ==="

# Delete completed jobs older than 24h
kubectl delete jobs --field-selector status.successful=1 --all-namespaces

# Delete failed pods
kubectl delete pods --field-selector status.phase=Failed --all-namespaces

# Delete evicted pods
kubectl get pods --all-namespaces | grep Evicted | awk '{print $2 " -n " $1}' | xargs -L1 kubectl delete pod

echo "=== Pod Cleanup Complete ==="
```

---

## 5. Maintenance Checklist

### 5.1 Weekly Checklist

```markdown
## Weekly Maintenance Checklist

**Date:** ___________
**Performed By:** ___________

### Pre-Maintenance
- [ ] Notify stakeholders
- [ ] Check current system health
- [ ] Verify backup status

### Database
- [ ] PostgreSQL VACUUM ANALYZE
- [ ] Check slow queries
- [ ] Review connection pool

### Storage
- [ ] Check S3 usage
- [ ] Review storage growth
- [ ] Clean temp files

### Kubernetes
- [ ] Delete completed jobs
- [ ] Check node health
- [ ] Review resource usage

### Post-Maintenance
- [ ] Verify all services healthy
- [ ] Update maintenance log
- [ ] Document any issues
```

---

## 6. Maintenance Automation

### 6.1 Automated Maintenance Jobs

```yaml
# k8s/maintenance-jobs.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: weekly-maintenance
  namespace: mlops
spec:
  schedule: "0 2 * * 2"  # Tuesday 2 AM
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: maintenance
            image: mlops/maintenance:latest
            command: ["/scripts/weekly_maintenance.sh"]
          restartPolicy: OnFailure
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial maintenance procedures |
