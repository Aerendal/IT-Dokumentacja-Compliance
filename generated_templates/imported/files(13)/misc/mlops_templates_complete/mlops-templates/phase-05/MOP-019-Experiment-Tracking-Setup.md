---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-019: Experiment Tracking Setup Guide

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-019 |
| **Version** | 1.0 |
| **Status** | DRAFT / IN REVIEW / ACTIVE / OBSOLETE |
| **Priority** | HIGH |
| **Owner** | [ML Platform Engineer] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Quarterly) |

---

## Document Lifecycle

### When This Document Appears
-  MOP-010 Design approved
-  Infrastructure provisioned
-  Phase 1 implementation begins

### When This Document Becomes Invalid
-  Major tool version upgrade
-  Architecture redesign
-  Platform migration

### Validity Conditions
-  Infrastructure ready
-  Network configured
-  Secrets available
-  Team trained

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-010: Experiment Tracking Design | Architecture |
| MOP-007: Architecture | Infrastructure |
| MOP-014: Tool Evaluation | Tool selection |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-045: Training Plan | User guides |
| MOP-038: Monitoring Setup | Metrics config |
| MOP-029: Deployment Guide | Deployment steps |

---

## Template Content

---

# Experiment Tracking Setup Guide

## 1. Prerequisites

### 1.1 Infrastructure Requirements

| Component | Specification | Status |
|-----------|---------------|--------|
| Kubernetes cluster | v1.25+ |  |
| PostgreSQL | 14+ |  |
| S3/GCS bucket | Configured |  |
| Load balancer | Ingress ready |  |
| DNS | Domain configured |  |

### 1.2 Access Requirements

| Item | Details | Status |
|------|---------|--------|
| AWS/GCP credentials | Service account |  |
| PostgreSQL credentials | In Vault |  |
| Container registry | Push access |  |
| Kubernetes access | kubectl configured |  |

---

## 2. Installation Steps

### 2.1 Namespace Setup

```bash
# Create namespace
kubectl create namespace mlflow

# Create service account
kubectl create serviceaccount mlflow-sa -n mlflow

# Apply RBAC
kubectl apply -f - <<EOF
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: mlflow-role
  namespace: mlflow
rules:
- apiGroups: [""]
  resources: ["pods", "services", "configmaps", "secrets"]
  verbs: ["get", "list", "watch", "create", "update", "delete"]
EOF
```

### 2.2 Database Setup

```bash
# Create PostgreSQL database
psql -h $DB_HOST -U postgres <<EOF
CREATE DATABASE mlflow;
CREATE USER mlflow WITH ENCRYPTED PASSWORD '${MLFLOW_DB_PASSWORD}';
GRANT ALL PRIVILEGES ON DATABASE mlflow TO mlflow;
EOF

# Store credentials in Kubernetes secret
kubectl create secret generic mlflow-db-credentials \
  --from-literal=username=mlflow \
  --from-literal=password=${MLFLOW_DB_PASSWORD} \
  --from-literal=host=${DB_HOST} \
  -n mlflow
```

### 2.3 Storage Configuration

```yaml
# mlflow-storage-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mlflow-storage-config
  namespace: mlflow
data:
  MLFLOW_S3_ENDPOINT_URL: "https://s3.amazonaws.com"
  MLFLOW_ARTIFACT_ROOT: "s3://mlflow-artifacts/experiments"
  AWS_DEFAULT_REGION: "us-east-1"
```

### 2.4 MLflow Deployment

```yaml
# mlflow-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mlflow-server
  namespace: mlflow
spec:
  replicas: 2
  selector:
    matchLabels:
      app: mlflow
  template:
    metadata:
      labels:
        app: mlflow
    spec:
      serviceAccountName: mlflow-sa
      containers:
      - name: mlflow
        image: ghcr.io/mlflow/mlflow:2.10.0
        ports:
        - containerPort: 5000
        env:
        - name: MLFLOW_BACKEND_STORE_URI
          valueFrom:
            secretKeyRef:
              name: mlflow-db-credentials
              key: connection-string
        envFrom:
        - configMapRef:
            name: mlflow-storage-config
        command:
        - mlflow
        - server
        - --host=0.0.0.0
        - --port=5000
        - --serve-artifacts
        resources:
          requests:
            memory: "1Gi"
            cpu: "500m"
          limits:
            memory: "2Gi"
            cpu: "1000m"
        livenessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: mlflow-service
  namespace: mlflow
spec:
  selector:
    app: mlflow
  ports:
  - port: 5000
    targetPort: 5000
  type: ClusterIP
```

### 2.5 Ingress Configuration

```yaml
# mlflow-ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mlflow-ingress
  namespace: mlflow
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - mlflow.example.com
    secretName: mlflow-tls
  rules:
  - host: mlflow.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: mlflow-service
            port:
              number: 5000
```

---

## 3. Verification Steps

### 3.1 Health Checks

```bash
# Check pod status
kubectl get pods -n mlflow

# Check logs
kubectl logs -l app=mlflow -n mlflow

# Test API endpoint
curl -s https://mlflow.example.com/health | jq .

# Expected output: {"status": "OK"}
```

### 3.2 Functional Tests

```python
# test_mlflow_setup.py
import mlflow

# Set tracking URI
mlflow.set_tracking_uri("https://mlflow.example.com")

# Test experiment creation
experiment_id = mlflow.create_experiment("setup-test")
print(f"Created experiment: {experiment_id}")

# Test run logging
with mlflow.start_run(experiment_id=experiment_id):
    mlflow.log_param("test_param", "value")
    mlflow.log_metric("test_metric", 0.95)
    print("Run logged successfully")

# Verify
runs = mlflow.search_runs(experiment_ids=[experiment_id])
assert len(runs) == 1
print(" All tests passed")
```

---

## 4. Configuration

### 4.1 Auto-Logging Configuration

```python
# Enable auto-logging in notebooks/scripts
import mlflow

# For scikit-learn
mlflow.sklearn.autolog()

# For PyTorch
mlflow.pytorch.autolog()

# For TensorFlow
mlflow.tensorflow.autolog()

# For XGBoost
mlflow.xgboost.autolog()
```

### 4.2 Team Configuration

```python
# Create team experiments
teams = ["fraud", "recommendation", "nlp"]
for team in teams:
    mlflow.create_experiment(
        name=f"{team}/default",
        tags={"team": team, "environment": "production"}
    )
```

---

## 5. Monitoring Setup

### 5.1 Prometheus Metrics

```yaml
# prometheus-servicemonitor.yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: mlflow-monitor
  namespace: mlflow
spec:
  selector:
    matchLabels:
      app: mlflow
  endpoints:
  - port: http
    path: /metrics
    interval: 30s
```

### 5.2 Grafana Dashboard

Import dashboard ID: `[MLFLOW_DASHBOARD_ID]` or use provided JSON.

---

## 6. Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Pod CrashLoopBackOff | DB connection failed | Check DB credentials, network |
| Artifact upload fails | S3 permissions | Check IAM role/service account |
| Slow UI | Too many experiments | Enable pagination, archive old |
| Auth errors | OIDC misconfigured | Check OAuth settings |

---

## 7. Rollback Procedure

```bash
# Rollback to previous version
kubectl rollout undo deployment/mlflow-server -n mlflow

# Verify rollback
kubectl rollout status deployment/mlflow-server -n mlflow
```

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
| DevOps Lead | | | |
