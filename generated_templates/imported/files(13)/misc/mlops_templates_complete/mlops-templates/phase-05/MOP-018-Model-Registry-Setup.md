---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-018: Model Registry Setup

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-018 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Engineer] |

---

## 1. Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| Kubernetes | 1.25+ | Orchestration |
| PostgreSQL | 14+ | MLflow backend |
| S3/GCS | - | Artifact storage |
| MLflow (tracking) | 2.10+ | Already deployed |

---

## 2. Model Registry Configuration

### 2.1 Enable Model Registry in MLflow

```yaml
# mlflow-deployment.yaml (updated)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mlflow
  namespace: mlops
spec:
  replicas: 2
  selector:
    matchLabels:
      app: mlflow
  template:
    spec:
      containers:
      - name: mlflow
        image: ghcr.io/mlflow/mlflow:v2.10.0
        command:
          - mlflow
          - server
          - --backend-store-uri=postgresql://$(DB_USER):$(DB_PASSWORD)@$(DB_HOST):5432/mlflow
          - --default-artifact-root=s3://mlops-artifacts/mlflow
          - --host=0.0.0.0
          - --port=5000
        env:
        - name: MLFLOW_TRACKING_URI
          value: "postgresql://..."
        - name: AWS_ACCESS_KEY_ID
          valueFrom:
            secretKeyRef:
              name: mlflow-s3-credentials
              key: access-key
        - name: AWS_SECRET_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: mlflow-s3-credentials
              key: secret-key
```

### 2.2 Registry Database Schema

MLflow automatically creates registry tables:
- `registered_models` - Model metadata
- `model_versions` - Version history
- `model_version_tags` - Version tags

---

## 3. Model Lifecycle Stages

### 3.1 Stage Configuration

| Stage | Purpose | Auto-transition |
|-------|---------|-----------------|
| None | Initial registration | - |
| Staging | Testing/validation | On registration |
| Production | Live serving | Manual approval |
| Archived | Deprecated models | Manual |

### 3.2 Stage Transition Workflow

```
┌──────────────────────────────────────────────────────────┐
│              Model Version Lifecycle                      │
│                                                          │
│  ┌──────┐    ┌─────────┐    ┌────────────┐    ┌────────┐│
│  │ None │───►│ Staging │───►│ Production │───►│Archived││
│  └──────┘    └─────────┘    └────────────┘    └────────┘│
│     │             │               │                      │
│     │        Validation      Approval             Retire │
│     │           Tests        Required                    │
│     │                                                    │
│     └────────────────────────────────────────────────────│
│              (Direct archive if validation fails)        │
└──────────────────────────────────────────────────────────┘
```

---

## 4. Model Registration API

### 4.1 Register Model (Python)

```python
import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Register model from run
model_uri = f"runs:/{run_id}/model"
result = mlflow.register_model(model_uri, "fraud-detection-model")

print(f"Model registered: {result.name} v{result.version}")

# Add description
client.update_registered_model(
    name="fraud-detection-model",
    description="Fraud detection model using XGBoost"
)

# Add tags
client.set_registered_model_tag(
    name="fraud-detection-model",
    key="team",
    value="fraud-team"
)
```

### 4.2 Transition Model Stage

```python
# Transition to staging (auto after validation)
client.transition_model_version_stage(
    name="fraud-detection-model",
    version=1,
    stage="Staging"
)

# Transition to production (requires approval)
client.transition_model_version_stage(
    name="fraud-detection-model",
    version=1,
    stage="Production",
    archive_existing_versions=True  # Archive old production version
)
```

### 4.3 Load Model by Stage

```python
# Load production model
model = mlflow.pyfunc.load_model("models:/fraud-detection-model/Production")

# Load specific version
model_v2 = mlflow.pyfunc.load_model("models:/fraud-detection-model/2")

# Load staging for testing
staging_model = mlflow.pyfunc.load_model("models:/fraud-detection-model/Staging")
```

---

## 5. Model Metadata Standards

### 5.1 Required Metadata

```python
# Set required metadata on registration
client.set_model_version_tag(name, version, "model_type", "classification")
client.set_model_version_tag(name, version, "framework", "xgboost")
client.set_model_version_tag(name, version, "owner", "fraud-team@company.com")
client.set_model_version_tag(name, version, "tier", "1")  # Risk tier
client.set_model_version_tag(name, version, "training_data_version", "v2024.01")
```

### 5.2 Metadata Schema

| Tag | Required | Description |
|-----|----------|-------------|
| model_type | Yes | classification/regression/etc |
| framework | Yes | sklearn/xgboost/pytorch/etc |
| owner | Yes | Team email |
| tier | Yes | Risk tier (1-4) |
| training_data_version | Yes | Data version used |
| accuracy | Yes | Primary metric |
| approved_by | Prod only | Approver name |
| deployment_date | Prod only | Production deploy date |

---

## 6. Access Control

### 6.1 RBAC Configuration

```python
# Example: Restrict production transitions
from mlflow.server.auth import create_permission

# Only senior ML engineers can promote to production
create_permission(
    name="promote_to_production",
    permission_level="MANAGE",
    experiment_ids=None,
    registered_model_names=["*"],
    stages=["Production"]
)
```

### 6.2 Permission Matrix

| Role | None→Staging | Staging→Prod | Archive | Delete |
|------|--------------|--------------|---------|--------|
| ML Engineer |  |  |  |  |
| Sr ML Engineer |  |  |  |  |
| ML Lead |  |  |  |  |
| Platform Admin |  |  |  |  |

---

## 7. Verification

### 7.1 Health Check

```bash
# Check MLflow registry endpoint
curl -sf https://mlflow.example.com/api/2.0/mlflow/registered-models/list

# List registered models
mlflow models list

# Get model details
mlflow models get --name fraud-detection-model
```

### 7.2 Functional Test

```python
# Test registration workflow
def test_model_registration():
    import mlflow
    from mlflow.tracking import MlflowClient
    
    client = MlflowClient()
    
    # Create test model
    with mlflow.start_run():
        mlflow.log_param("test", True)
        mlflow.sklearn.log_model(
            sk_model=DummyClassifier(),
            artifact_path="model"
        )
        run_id = mlflow.active_run().info.run_id
    
    # Register
    result = mlflow.register_model(f"runs:/{run_id}/model", "test-model")
    assert result.version == "1"
    
    # Transition
    client.transition_model_version_stage("test-model", "1", "Staging")
    version = client.get_model_version("test-model", "1")
    assert version.current_stage == "Staging"
    
    # Cleanup
    client.delete_registered_model("test-model")
    print(" Model registry test passed")
```

---

## 8. Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Registration fails | DB connection | Check PostgreSQL connectivity |
| Artifact not found | S3 permissions | Verify IAM role |
| Stage transition denied | RBAC | Check user permissions |
| Slow queries | DB performance | Add indexes, vacuum |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial setup |
