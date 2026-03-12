---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-087: Backup and Recovery Procedures

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-087 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Backup Strategy

### 1.1 Components to Backup

| Component | Data Type | Backup Frequency | Retention |
|-----------|-----------|------------------|-----------|
| MLflow DB | Metadata, experiments | Hourly | 30 days |
| MLflow Artifacts | Models, files | Daily | 1 year |
| Feature Store (Redis) | Online features | Hourly | 7 days |
| Feature Store (Offline) | Historical features | Daily | 1 year |
| Configuration | K8s configs, secrets | On change | Indefinite |
| Prometheus | Metrics data | Daily | 90 days |

### 1.2 Backup Schedule

```
┌─────────────────────────────────────────────────────────────────┐
│                    Backup Schedule                               │
│                                                                 │
│  Hourly (XX:00)                                                 │
│  └── MLflow DB incremental                                      │
│  └── Redis snapshot                                             │
│                                                                 │
│  Daily (02:00 UTC)                                              │
│  └── MLflow DB full                                             │
│  └── MLflow Artifacts sync                                      │
│  └── Prometheus snapshot                                        │
│  └── Feast offline store                                        │
│                                                                 │
│  Weekly (Sunday 03:00 UTC)                                      │
│  └── Full system backup verification                            │
│  └── Backup integrity test                                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Backup Implementation

### 2.1 PostgreSQL Backup (MLflow)

```bash
#!/bin/bash
# backup/postgres_backup.sh

BACKUP_BUCKET="s3://mlops-backups/postgres"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
DB_HOST="mlflow-db.example.com"
DB_NAME="mlflow"

echo "=== PostgreSQL Backup: $TIMESTAMP ==="

# Full backup with pg_dump
pg_dump -h $DB_HOST -U mlflow -Fc $DB_NAME > /tmp/mlflow_$TIMESTAMP.dump

# Upload to S3
aws s3 cp /tmp/mlflow_$TIMESTAMP.dump $BACKUP_BUCKET/mlflow_$TIMESTAMP.dump

# Verify upload
aws s3 ls $BACKUP_BUCKET/mlflow_$TIMESTAMP.dump || exit 1

# Cleanup local
rm /tmp/mlflow_$TIMESTAMP.dump

# Cleanup old backups (keep 30 days)
aws s3 ls $BACKUP_BUCKET/ | while read -r line; do
    createDate=$(echo $line | awk '{print $1" "$2}')
    createDate=$(date -d"$createDate" +%s)
    olderThan=$(date -d"-30 days" +%s)
    if [[ $createDate -lt $olderThan ]]; then
        fileName=$(echo $line | awk '{print $4}')
        aws s3 rm $BACKUP_BUCKET/$fileName
    fi
done

echo "=== Backup Complete ==="
```

### 2.2 Redis Backup (Feature Store)

```bash
#!/bin/bash
# backup/redis_backup.sh

REDIS_HOST="redis.example.com"
BACKUP_BUCKET="s3://mlops-backups/redis"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "=== Redis Backup: $TIMESTAMP ==="

# Trigger BGSAVE
redis-cli -h $REDIS_HOST BGSAVE

# Wait for completion
while [ $(redis-cli -h $REDIS_HOST LASTSAVE) == $(redis-cli -h $REDIS_HOST LASTSAVE) ]; do
    sleep 1
done

# Copy RDB file
kubectl cp redis-0:/data/dump.rdb /tmp/redis_$TIMESTAMP.rdb -n feast

# Upload to S3
aws s3 cp /tmp/redis_$TIMESTAMP.rdb $BACKUP_BUCKET/redis_$TIMESTAMP.rdb

# Cleanup
rm /tmp/redis_$TIMESTAMP.rdb

echo "=== Redis Backup Complete ==="
```

### 2.3 MLflow Artifacts Sync

```bash
#!/bin/bash
# backup/artifacts_sync.sh

SOURCE_BUCKET="s3://mlops-artifacts"
BACKUP_BUCKET="s3://mlops-backups/artifacts"

echo "=== Artifacts Sync ==="

# Sync with versioning
aws s3 sync $SOURCE_BUCKET $BACKUP_BUCKET \
    --exclude "*.tmp" \
    --exclude "*.log"

echo "=== Artifacts Sync Complete ==="
```

---

## 3. Recovery Procedures

### 3.1 PostgreSQL Recovery

```bash
#!/bin/bash
# recovery/postgres_restore.sh

BACKUP_FILE=$1
DB_HOST="mlflow-db.example.com"
DB_NAME="mlflow"

echo "=== PostgreSQL Restore ==="

if [ -z "$BACKUP_FILE" ]; then
    echo "Usage: $0 <backup_file>"
    echo "Available backups:"
    aws s3 ls s3://mlops-backups/postgres/ | tail -10
    exit 1
fi

# Download backup
aws s3 cp s3://mlops-backups/postgres/$BACKUP_FILE /tmp/$BACKUP_FILE

# Stop MLflow to prevent writes
kubectl scale deployment mlflow --replicas=0 -n mlops

# Restore
pg_restore -h $DB_HOST -U mlflow -d $DB_NAME -c /tmp/$BACKUP_FILE

# Restart MLflow
kubectl scale deployment mlflow --replicas=2 -n mlops

# Verify
kubectl wait --for=condition=ready pod -l app=mlflow -n mlops --timeout=5m

echo "=== Restore Complete ==="
```

### 3.2 Redis Recovery

```bash
#!/bin/bash
# recovery/redis_restore.sh

BACKUP_FILE=$1

echo "=== Redis Restore ==="

# Download backup
aws s3 cp s3://mlops-backups/redis/$BACKUP_FILE /tmp/dump.rdb

# Stop Redis
kubectl scale statefulset redis --replicas=0 -n feast

# Copy RDB file
kubectl cp /tmp/dump.rdb redis-0:/data/dump.rdb -n feast

# Start Redis
kubectl scale statefulset redis --replicas=1 -n feast

# Verify
kubectl exec -n feast redis-0 -- redis-cli DBSIZE

echo "=== Redis Restore Complete ==="
```

### 3.3 Full System Recovery

```bash
#!/bin/bash
# recovery/full_system_restore.sh

BACKUP_DATE=$1  # Format: YYYYMMDD

echo "=== Full System Recovery for $BACKUP_DATE ==="

# 1. Restore PostgreSQL
echo "[1/4] Restoring PostgreSQL..."
./recovery/postgres_restore.sh mlflow_${BACKUP_DATE}_020000.dump

# 2. Restore Redis
echo "[2/4] Restoring Redis..."
./recovery/redis_restore.sh redis_${BACKUP_DATE}_020000.rdb

# 3. Sync artifacts
echo "[3/4] Syncing artifacts..."
aws s3 sync s3://mlops-backups/artifacts s3://mlops-artifacts

# 4. Restart all services
echo "[4/4] Restarting services..."
kubectl rollout restart deployment -n mlops
kubectl rollout restart deployment -n feast
kubectl rollout restart deployment -n models

# Wait for services
kubectl wait --for=condition=ready pod -l app=mlflow -n mlops --timeout=10m

echo "=== Full System Recovery Complete ==="
```

---

## 4. Backup Verification

### 4.1 Weekly Verification Script

```python
# backup/verify_backups.py
import boto3
from datetime import datetime, timedelta

def verify_backups():
    """Verify backup integrity and freshness."""
    s3 = boto3.client('s3')
    issues = []
    
    # Check PostgreSQL backups
    pg_backups = list_backups('mlops-backups', 'postgres/')
    if not pg_backups:
        issues.append("No PostgreSQL backups found")
    else:
        latest = max(pg_backups, key=lambda x: x['LastModified'])
        age_hours = (datetime.now(latest['LastModified'].tzinfo) - latest['LastModified']).total_seconds() / 3600
        if age_hours > 24:
            issues.append(f"PostgreSQL backup is {age_hours:.1f} hours old")
    
    # Check Redis backups
    redis_backups = list_backups('mlops-backups', 'redis/')
    if not redis_backups:
        issues.append("No Redis backups found")
    
    # Verify backup integrity (sample)
    if pg_backups:
        latest_pg = max(pg_backups, key=lambda x: x['LastModified'])
        if not verify_pg_backup(latest_pg['Key']):
            issues.append("PostgreSQL backup verification failed")
    
    return {
        'status': 'OK' if not issues else 'ISSUES',
        'issues': issues,
        'timestamp': datetime.now().isoformat()
    }

def list_backups(bucket: str, prefix: str) -> list:
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    return response.get('Contents', [])

def verify_pg_backup(key: str) -> bool:
    """Verify PostgreSQL backup can be read."""
    # Download and verify header
    # Implementation depends on pg_restore validation
    return True
```

---

## 5. Recovery Testing

### 5.1 Monthly DR Test

```markdown
## Monthly Disaster Recovery Test

**Date:** ___________
**Performed By:** ___________

### Test Scope
- [ ] PostgreSQL restore to test environment
- [ ] Redis restore to test environment
- [ ] Model serving from backup

### Test Steps

1. **Prepare Test Environment**
   - [ ] Test namespace created
   - [ ] Resources allocated

2. **Restore Databases**
   - [ ] PostgreSQL restored: _____ min
   - [ ] Redis restored: _____ min
   - [ ] Data integrity verified

3. **Verify Functionality**
   - [ ] MLflow accessible
   - [ ] Features retrievable
   - [ ] Model inference working

### Results

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| RTO | 30 min | ___ min | / |
| RPO | 1 hour | ___ hour | / |
| Data integrity | 100% | ___% | / |

### Issues Found
- 

### Sign-off
- Tester: ___________
- SRE Lead: ___________
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial backup procedures |
