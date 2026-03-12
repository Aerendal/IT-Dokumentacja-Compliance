---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-020: Feature Store Setup Guide

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-020 |
| **Version** | 1.0 |
| **Status** | DRAFT / IN REVIEW / ACTIVE / OBSOLETE |
| **Priority** | HIGH |
| **Owner** | [ML Platform Engineer / Data Engineer] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Quarterly) |

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-011: Feature Store Design | Architecture |
| MOP-007: Architecture | Infrastructure |
| MOP-006: Scalability Requirements | Capacity |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-045: Training Plan | User guides |
| MOP-038: Monitoring Setup | Metrics config |

---

## Template Content

---

# Feature Store Setup Guide (Feast)

## 1. Prerequisites

| Component | Specification | Status |
|-----------|---------------|--------|
| Kubernetes cluster | v1.25+ |  |
| Redis cluster | 6+ |  |
| S3/GCS bucket | Configured |  |
| PostgreSQL (registry) | 14+ |  |

---

## 2. Feast Installation

### 2.1 Install Feast CLI

```bash
pip install feast[redis,postgres,aws]
```

### 2.2 Initialize Feature Repository

```bash
mkdir -p /opt/feast/feature_repo
cd /opt/feast/feature_repo
feast init
```

### 2.3 Configure feature_store.yaml

```yaml
# feature_store.yaml
project: mlops_platform
registry:
  registry_type: sql
  path: postgresql://feast:${FEAST_DB_PASSWORD}@postgres:5432/feast
provider: aws
online_store:
  type: redis
  connection_string: "redis-cluster:6379,ssl=true"
offline_store:
  type: file  # or bigquery, redshift, snowflake
  # For BigQuery:
  # type: bigquery
  # project: my-gcp-project
  # dataset: feast_offline
entity_key_serialization_version: 2
```

---

## 3. Deploy Feature Server

### 3.1 Kubernetes Deployment

```yaml
# feast-server-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: feast-feature-server
  namespace: feast
spec:
  replicas: 3
  selector:
    matchLabels:
      app: feast-server
  template:
    metadata:
      labels:
        app: feast-server
    spec:
      containers:
      - name: feast
        image: feastdev/feature-server:0.36.0
        ports:
        - containerPort: 6566
        env:
        - name: FEAST_REPO_PATH
          value: "/feast/feature_repo"
        volumeMounts:
        - name: feast-config
          mountPath: /feast/feature_repo
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
      volumes:
      - name: feast-config
        configMap:
          name: feast-repo-config
---
apiVersion: v1
kind: Service
metadata:
  name: feast-server
  namespace: feast
spec:
  selector:
    app: feast-server
  ports:
  - port: 6566
    targetPort: 6566
```

---

## 4. Define Sample Features

### 4.1 Entity Definition

```python
# entities.py
from feast import Entity

user = Entity(
    name="user_id",
    join_keys=["user_id"],
    description="User identifier"
)

merchant = Entity(
    name="merchant_id", 
    join_keys=["merchant_id"],
    description="Merchant identifier"
)
```

### 4.2 Feature View Definition

```python
# features.py
from feast import FeatureView, Field, FileSource
from feast.types import Float32, Int64
from datetime import timedelta

user_source = FileSource(
    path="s3://feast-data/user_features.parquet",
    timestamp_field="event_timestamp"
)

user_features = FeatureView(
    name="user_features",
    entities=[user],
    ttl=timedelta(days=1),
    schema=[
        Field(name="avg_transaction_amount", dtype=Float32),
        Field(name="transaction_count_30d", dtype=Int64),
        Field(name="days_since_last_transaction", dtype=Int64),
    ],
    source=user_source,
    online=True,
    tags={"team": "fraud", "owner": "ml-platform"}
)
```

---

## 5. Apply and Materialize

```bash
# Apply feature definitions
cd /opt/feast/feature_repo
feast apply

# Materialize features to online store
feast materialize-incremental $(date +%Y-%m-%dT%H:%M:%S)

# Verify
feast feature-views list
feast entities list
```

---

## 6. Verification

```python
# test_feast_setup.py
from feast import FeatureStore
import pandas as pd

store = FeatureStore(repo_path="/opt/feast/feature_repo")

# Test online features
entity_dict = {"user_id": ["user_001"]}
features = store.get_online_features(
    features=["user_features:avg_transaction_amount"],
    entity_rows=[entity_dict]
).to_dict()

print(f"Online features: {features}")
assert "user_features__avg_transaction_amount" in features

# Test historical features
entity_df = pd.DataFrame({
    "user_id": ["user_001"],
    "event_timestamp": [pd.Timestamp.now()]
})
historical = store.get_historical_features(
    entity_df=entity_df,
    features=["user_features:avg_transaction_amount"]
).to_df()

print(f"Historical features: {historical}")
print(" Feature store setup verified")
```

---

## 7. Monitoring

### 7.1 Key Metrics

| Metric | Alert Threshold |
|--------|-----------------|
| Online latency P99 | >20ms |
| Materialization lag | >1 hour |
| Feature null rate | >5% |
| Redis memory usage | >80% |

### 7.2 Prometheus Metrics

```yaml
# ServiceMonitor for Feast
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: feast-monitor
  namespace: feast
spec:
  selector:
    matchLabels:
      app: feast-server
  endpoints:
  - port: http
    path: /metrics
```

---

## 8. Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Slow online retrieval | Redis connection | Check Redis cluster health |
| Materialization fails | S3 permissions | Verify IAM roles |
| Registry errors | PostgreSQL connection | Check DB connectivity |
| Stale features | Materialization not running | Check scheduler |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial setup guide |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| ML Platform Engineer | | | |
| Data Engineer Lead | | | |
