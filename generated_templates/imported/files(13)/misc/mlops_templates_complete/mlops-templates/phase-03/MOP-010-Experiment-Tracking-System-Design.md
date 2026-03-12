---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-010: Experiment Tracking System Design

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-010 |
| **Version** | 1.0 |
| **Status** | DRAFT / IN REVIEW / ACTIVE / OBSOLETE |
| **Priority** | CRITICAL |
| **Owner** | [ML Platform Lead] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Semi-annually) |

---

## Document Lifecycle

### When This Document Appears
-  MOP-007 Architecture Document approved
-  Multiple ML experiments being conducted
-  Need for reproducibility identified

### When This Document Becomes Invalid
-  Tracking platform migration
-  Fundamental architecture change
-  New experiment paradigms emerge

### Validity Conditions
-  Supports all ML frameworks in use
-  Integration with model registry established
-  Storage capacity meets requirements
-  Team adoption achieved

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-007: Architecture | System placement |
| MOP-005: ML Lifecycle Requirements | Tracking requirements |
| MOP-003: Tool Stack Vision | Platform selection |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-019: Experiment Tracking Setup | Implementation specs |
| MOP-009: Model Registry | Run-to-model linkage |
| MOP-008: CI/CD Pipeline | Experiment integration |

### Bidirectional Dependencies
| Document | Relationship |
|----------|--------------|
| MOP-009: Model Registry | Runs ↔ Models |
| MOP-011: Feature Store | Features ↔ Experiments |
| MOP-008: CI/CD Pipeline | Automated experiments |

---

## Section Dependencies (Internal)

```
┌────────────────────────────────────────────────────────────────┐
│              1. System Overview                                 │
└────────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
│ 2. Data Model    │ │ 3. Tracking  │ │ 4. Storage       │
│                  │ │    API       │ │    Architecture  │
└──────────────────┘ └──────────────┘ └──────────────────┘
        │                   │                  │
        └───────────────────┼──────────────────┘
                            ▼
┌────────────────────────────────────────────────────────────────┐
│              5. Comparison & Visualization                      │
└────────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
│ 6. Integration   │ │ 7. Best      │ │ 8. Governance    │
│    Points        │ │    Practices │ │                  │
└──────────────────┘ └──────────────┘ └──────────────────┘
```

---

## Template Content

---

# Experiment Tracking System Design

**[Organization Name]**

**Version:** [X.Y]  
**Date:** [YYYY-MM-DD]

---

## 1. System Overview

> **Section Dependencies:**
> - Depends on: MOP-007 Architecture
> - Feeds into: All other sections
> - Update trigger: Platform strategy changes

### 1.1 Purpose

The Experiment Tracking System provides:
- **Reproducibility**: Track all inputs needed to reproduce any experiment
- **Comparison**: Compare experiments across parameters, metrics, and artifacts
- **Collaboration**: Share experiments and results across teams
- **Lineage**: Link experiments to models and deployments
- **Governance**: Audit trail of all ML experiments

### 1.2 Scope

| In Scope | Out of Scope |
|----------|--------------|
| Parameter logging | Data versioning (DVC) |
| Metric tracking | Feature store |
| Artifact storage | Model serving |
| Run management | Infrastructure provisioning |
| Experiment organization | Job scheduling |
| Visualization & comparison | Hyperparameter optimization |

### 1.3 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                   Experiment Tracking System                         │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                      User Interfaces                           │ │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐          │ │
│  │  │   UI    │  │   CLI   │  │   SDK   │  │   API   │          │ │
│  │  │(Web App)│  │         │  │(Python) │  │ (REST)  │          │ │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘          │ │
│  └──────────────────────────────┬────────────────────────────────┘ │
│                                 │                                   │
│  ┌──────────────────────────────┼────────────────────────────────┐ │
│  │                      Tracking Server                           │ │
│  │                              │                                 │ │
│  │  ┌─────────┐  ┌─────────────┴───────────────┐  ┌─────────┐   │ │
│  │  │ Run     │  │      Experiment Manager     │  │ Search  │   │ │
│  │  │ Manager │  │                             │  │ Engine  │   │ │
│  │  └─────────┘  └─────────────────────────────┘  └─────────┘   │ │
│  │                                                               │ │
│  │  ┌─────────┐  ┌─────────────────────────────┐  ┌─────────┐   │ │
│  │  │ Metric  │  │      Artifact Manager       │  │ Model   │   │ │
│  │  │ Logger  │  │                             │  │ Logger  │   │ │
│  │  └─────────┘  └─────────────────────────────┘  └─────────┘   │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                 │                                   │
│  ┌──────────────────────────────┼────────────────────────────────┐ │
│  │                      Storage Layer                             │ │
│  │  ┌─────────────────┐        │       ┌─────────────────┐       │ │
│  │  │  Metadata DB    │◄───────┴──────►│  Artifact Store │       │ │
│  │  │  (PostgreSQL)   │                │    (S3/GCS)     │       │ │
│  │  └─────────────────┘                └─────────────────┘       │ │
│  └───────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.4 Technology Selection

| Component | Options | Selected | Rationale |
|-----------|---------|----------|-----------|
| Platform | MLflow / W&B / Neptune / Comet | [Selection] | [Rationale] |
| Metadata DB | PostgreSQL / MySQL | PostgreSQL | JSONB support, scalability |
| Artifact Store | S3 / GCS / Azure Blob | [Selection] | Cloud alignment |
| UI | Native / Grafana / Custom | Native | Built-in capabilities |

### 1.5 Platform Comparison

| Feature | MLflow | W&B | Neptune | Comet |
|---------|--------|-----|---------|-------|
| Open Source |  |  |  |  |
| Self-hosted |  |  |  |  |
| Auto-logging |  |  |  |  |
| Model Registry |  |  |  |  |
| Collaboration | Basic | Excellent | Good | Good |
| Visualization | Basic | Excellent | Good | Good |
| Cost | Free | $/user | $/user | $/user |

---

## 2. Data Model

> **Section Dependencies:**
> - Depends on: Section 1 (Overview)
> - Feeds into: Section 3 (API), Section 4 (Storage)
> - Update trigger: New tracking requirements

### 2.1 Core Entities

```
┌───────────────────────────────────────────────────────────────────┐
│                     Entity Relationship Diagram                    │
│                                                                   │
│  ┌─────────────────┐                                             │
│  │   Experiment    │                                             │
│  │─────────────────│                                             │
│  │ experiment_id   │◄─────┐                                      │
│  │ name (unique)   │      │ 1:N                                  │
│  │ artifact_location│     │                                      │
│  │ lifecycle_stage │      │                                      │
│  │ tags[]          │      │                                      │
│  └─────────────────┘      │                                      │
│                           │                                       │
│  ┌────────────────────────┴──────────────────────────────┐       │
│  │                         Run                            │       │
│  │────────────────────────────────────────────────────────│       │
│  │ run_id (PK)                                            │       │
│  │ experiment_id (FK)                                     │       │
│  │ run_name                                               │       │
│  │ source_type (NOTEBOOK, JOB, LOCAL, PROJECT, RECIPE)   │       │
│  │ source_name                                            │       │
│  │ user_id                                                │       │
│  │ status (RUNNING, SCHEDULED, FINISHED, FAILED, KILLED) │       │
│  │ start_time                                             │       │
│  │ end_time                                               │       │
│  │ artifact_uri                                           │       │
│  │ lifecycle_stage (active, deleted)                      │       │
│  └────────────────────────────────────────────────────────┘       │
│           │           │           │           │                   │
│           │ 1:N       │ 1:N       │ 1:N       │ 1:N              │
│           ▼           ▼           ▼           ▼                   │
│  ┌─────────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐            │
│  │  Parameter  │ │ Metric  │ │   Tag   │ │ Artifact│            │
│  │─────────────│ │─────────│ │─────────│ │─────────│            │
│  │ key         │ │ key     │ │ key     │ │ path    │            │
│  │ value       │ │ value   │ │ value   │ │ is_dir  │            │
│  │             │ │ timestamp│ │         │ │ file_size│           │
│  │             │ │ step    │ │         │ │         │            │
│  └─────────────┘ └─────────┘ └─────────┘ └─────────┘            │
└───────────────────────────────────────────────────────────────────┘
```

### 2.2 Experiment Schema

```yaml
experiment:
  experiment_id: string (auto-generated)
    format: "exp_{uuid}"
  
  name: string (unique, required)
    pattern: "^[a-zA-Z0-9_-/]+$"
    max_length: 500
    description: "Unique experiment name, can include paths"
  
  artifact_location: uri (optional)
    description: "Default artifact storage location"
  
  lifecycle_stage: enum
    values: [active, deleted]
    default: active
  
  tags: array[tag]
    items:
      key: string (max 250 chars)
      value: string (max 5000 chars)
  
  creation_time: datetime
  last_update_time: datetime
```

### 2.3 Run Schema

```yaml
run:
  run_id: string (auto-generated)
    format: "run_{uuid}"
  
  run_uuid: string (alias for run_id)
  
  experiment_id: string (FK)
  
  run_name: string (optional)
    description: "Human-readable run name"
  
  user_id: string
    description: "User who created the run"
  
  status: enum
    values:
      - RUNNING: "Run is executing"
      - SCHEDULED: "Run is scheduled"
      - FINISHED: "Run completed successfully"
      - FAILED: "Run failed with error"
      - KILLED: "Run was manually stopped"
  
  start_time: timestamp_ms
  end_time: timestamp_ms
  
  artifact_uri: uri
    description: "Root artifact location for this run"
  
  lifecycle_stage: enum
    values: [active, deleted]
  
  # Source tracking
  source:
    source_type: enum[NOTEBOOK, JOB, LOCAL, PROJECT, RECIPE]
    source_name: string
    source_version: string (git commit)
    entry_point_name: string
  
  # Git tracking
  git:
    commit: string
    branch: string
    repo_url: string
    dirty: boolean
```

### 2.4 Tracked Data Types

| Type | Description | Example |
|------|-------------|---------|
| **Parameters** | Input configuration values | learning_rate=0.01, epochs=100 |
| **Metrics** | Output measurements | accuracy=0.95, loss=0.12 |
| **Tags** | Metadata labels | team=fraud, environment=prod |
| **Artifacts** | Files and directories | model.pkl, plots/, data_sample.csv |

---

## 3. Tracking API

> **Section Dependencies:**
> - Depends on: Section 2 (Data Model)
> - Feeds into: Section 6 (Integrations)
> - Update trigger: API version changes

### 3.1 Python SDK Usage

#### Basic Tracking

```python
import mlflow

# Set experiment
mlflow.set_experiment("fraud-detection")

# Start run
with mlflow.start_run(run_name="baseline-v1"):
    # Log parameters (once at start)
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("batch_size", 32)
    mlflow.log_params({
        "epochs": 100,
        "optimizer": "adam",
        "model_type": "xgboost"
    })
    
    # Log metrics (during training)
    for epoch in range(100):
        train_loss = train_one_epoch()
        val_acc = validate()
        
        mlflow.log_metric("train_loss", train_loss, step=epoch)
        mlflow.log_metric("val_accuracy", val_acc, step=epoch)
    
    # Log final metrics
    mlflow.log_metrics({
        "test_accuracy": 0.92,
        "test_f1": 0.89,
        "test_auc": 0.95
    })
    
    # Log artifacts
    mlflow.log_artifact("confusion_matrix.png")
    mlflow.log_artifacts("plots/", artifact_path="visualizations")
    
    # Log model
    mlflow.sklearn.log_model(model, "model")
    
    # Set tags
    mlflow.set_tag("model_type", "classification")
    mlflow.set_tags({
        "team": "fraud-ml",
        "dataset_version": "v2.3"
    })
```

#### Auto-Logging

```python
import mlflow

# Enable auto-logging for specific frameworks
mlflow.sklearn.autolog()
mlflow.pytorch.autolog()
mlflow.tensorflow.autolog()
mlflow.xgboost.autolog()
mlflow.lightgbm.autolog()

# Or enable for all supported frameworks
mlflow.autolog()

# Auto-logged information:
# - Parameters: model hyperparameters
# - Metrics: training metrics
# - Artifacts: model, feature importance
# - Tags: estimator name, class
```

### 3.2 REST API

#### Create Experiment

```http
POST /api/2.0/mlflow/experiments/create
Content-Type: application/json

{
  "name": "fraud-detection-experiments",
  "artifact_location": "s3://mlflow-artifacts/fraud-detection",
  "tags": [
    {"key": "team", "value": "fraud-ml"},
    {"key": "project", "value": "real-time-scoring"}
  ]
}

Response:
{
  "experiment_id": "exp_abc123"
}
```

#### Create Run

```http
POST /api/2.0/mlflow/runs/create
Content-Type: application/json

{
  "experiment_id": "exp_abc123",
  "run_name": "baseline-xgboost",
  "start_time": 1704067200000,
  "tags": [
    {"key": "mlflow.user", "value": "jane.doe"},
    {"key": "mlflow.source.type", "value": "NOTEBOOK"}
  ]
}

Response:
{
  "run": {
    "info": {
      "run_id": "run_xyz789",
      "experiment_id": "exp_abc123",
      "status": "RUNNING",
      ...
    }
  }
}
```

#### Log Batch

```http
POST /api/2.0/mlflow/runs/log-batch
Content-Type: application/json

{
  "run_id": "run_xyz789",
  "params": [
    {"key": "learning_rate", "value": "0.01"},
    {"key": "batch_size", "value": "32"}
  ],
  "metrics": [
    {"key": "accuracy", "value": 0.92, "timestamp": 1704067200000, "step": 100},
    {"key": "loss", "value": 0.12, "timestamp": 1704067200000, "step": 100}
  ],
  "tags": [
    {"key": "model_type", "value": "xgboost"}
  ]
}
```

### 3.3 Logging Best Practices

| What to Log | When | How |
|-------------|------|-----|
| Parameters | Start of run | `log_params()` once |
| Training metrics | Each epoch/step | `log_metric(step=n)` |
| Validation metrics | Each validation | `log_metric(step=n)` |
| Final metrics | End of training | `log_metrics()` |
| Model artifacts | After training | `log_model()` |
| Plots/figures | When generated | `log_artifact()` |
| Data samples | Start of run | `log_artifact()` |

---

## 4. Storage Architecture

> **Section Dependencies:**
> - Depends on: Section 2 (Data Model)
> - Feeds into: Section 8 (Governance)
> - Update trigger: Storage requirements change

### 4.1 Storage Components

```
┌─────────────────────────────────────────────────────────────────────┐
│                      Storage Architecture                            │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │                    Metadata Store (PostgreSQL)                   ││
│  │                                                                 ││
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               ││
│  │  │ experiments │ │    runs     │ │  params     │               ││
│  │  └─────────────┘ └─────────────┘ └─────────────┘               ││
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               ││
│  │  │   metrics   │ │    tags     │ │model_versions│              ││
│  │  └─────────────┘ └─────────────┘ └─────────────┘               ││
│  └─────────────────────────────────────────────────────────────────┘│
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │                    Artifact Store (S3/GCS)                       ││
│  │                                                                 ││
│  │  s3://mlflow-artifacts/                                         ││
│  │  └── {experiment_id}/                                           ││
│  │      └── {run_id}/                                              ││
│  │          └── artifacts/                                         ││
│  │              ├── model/                                         ││
│  │              │   ├── MLmodel                                    ││
│  │              │   ├── model.pkl                                  ││
│  │              │   └── requirements.txt                           ││
│  │              ├── visualizations/                                ││
│  │              │   ├── confusion_matrix.png                       ││
│  │              │   └── roc_curve.png                              ││
│  │              └── metrics.json                                   ││
│  └─────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 Storage Configuration

```yaml
# MLflow storage configuration
tracking:
  backend_store_uri: "postgresql://mlflow:password@db:5432/mlflow"
  default_artifact_root: "s3://mlflow-artifacts"
  
artifact_stores:
  s3:
    bucket: "mlflow-artifacts"
    region: "us-east-1"
    encryption: "AES256"
    lifecycle:
      - transition:
          days: 90
          storage_class: "GLACIER"
      - expiration:
          days: 365
          
  gcs:
    bucket: "mlflow-artifacts"
    location: "us-central1"
```

### 4.3 Storage Sizing

| Component | Initial Size | Growth Rate | Retention |
|-----------|--------------|-------------|-----------|
| Metadata DB | 10 GB | 1 GB/month | Indefinite |
| Model artifacts | 100 GB | 50 GB/month | 1 year active |
| Logs/metrics | 5 GB | 500 MB/month | 2 years |
| Visualizations | 20 GB | 10 GB/month | 6 months |

### 4.4 Retention Policies

```yaml
retention_policies:
  experiments:
    active: indefinite
    deleted: 30 days (soft delete)
    
  runs:
    successful: 365 days
    failed: 90 days
    killed: 30 days
    
  artifacts:
    models:
      registered: indefinite
      unregistered: 180 days
    visualizations: 90 days
    logs: 365 days
    
  cleanup:
    schedule: "0 2 * * 0"  # Weekly Sunday 2 AM
    dry_run_first: true
```

---

## 5. Comparison & Visualization

> **Section Dependencies:**
> - Depends on: Section 2 (Data Model), Section 3 (API)
> - Feeds into: Decision making, Model selection
> - Update trigger: New visualization requirements

### 5.1 Run Comparison

```python
from mlflow import MlflowClient

client = MlflowClient()

# Search runs
runs = client.search_runs(
    experiment_ids=["exp_abc123"],
    filter_string="metrics.accuracy > 0.9 AND params.model_type = 'xgboost'",
    order_by=["metrics.accuracy DESC"],
    max_results=10
)

# Compare runs
for run in runs:
    print(f"Run: {run.info.run_id}")
    print(f"  Accuracy: {run.data.metrics.get('accuracy')}")
    print(f"  Learning Rate: {run.data.params.get('learning_rate')}")
```

### 5.2 Visualization Components

| Visualization | Purpose | Implementation |
|---------------|---------|----------------|
| Metric charts | Track metric over steps | Line chart, multiple runs |
| Parallel coordinates | Compare parameters | Hyperparameter patterns |
| Scatter plot | Metric correlations | Parameter vs metric |
| Bar chart | Final metric comparison | Across runs |
| Artifact viewer | Inspect images/plots | Built-in UI |

### 5.3 Custom Visualizations

```python
import mlflow
import matplotlib.pyplot as plt

# Generate and log visualization
with mlflow.start_run():
    # Training code...
    
    # Create custom visualization
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Confusion matrix
    axes[0, 0].imshow(confusion_matrix)
    axes[0, 0].set_title("Confusion Matrix")
    
    # ROC curve
    axes[0, 1].plot(fpr, tpr)
    axes[0, 1].set_title("ROC Curve")
    
    # Feature importance
    axes[1, 0].barh(feature_names, importances)
    axes[1, 0].set_title("Feature Importance")
    
    # Learning curves
    axes[1, 1].plot(train_losses, label="Train")
    axes[1, 1].plot(val_losses, label="Validation")
    axes[1, 1].set_title("Learning Curves")
    
    plt.tight_layout()
    plt.savefig("training_summary.png")
    
    # Log artifact
    mlflow.log_artifact("training_summary.png")
```

### 5.4 Dashboard Integration

```yaml
# Grafana dashboard for experiment metrics
grafana_dashboard:
  panels:
    - title: "Experiment Success Rate"
      type: stat
      query: |
        SELECT 
          COUNT(*) FILTER (WHERE status = 'FINISHED') * 100.0 / COUNT(*) as success_rate
        FROM runs
        WHERE start_time > NOW() - INTERVAL '7 days'
    
    - title: "Model Accuracy Trend"
      type: timeseries
      query: |
        SELECT 
          date_trunc('day', start_time) as time,
          AVG(m.value) as avg_accuracy
        FROM runs r
        JOIN metrics m ON r.run_id = m.run_id
        WHERE m.key = 'accuracy'
        GROUP BY 1
    
    - title: "Runs by Team"
      type: piechart
      query: |
        SELECT 
          t.value as team,
          COUNT(*) as runs
        FROM runs r
        JOIN tags t ON r.run_id = t.run_id
        WHERE t.key = 'team'
        GROUP BY 1
```

---

## 6. Integration Points

> **Section Dependencies:**
> - Depends on: MOP-007 Architecture
> - Feeds into: Implementation
> - Update trigger: New integration requirements

### 6.1 Integration Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│               Experiment Tracking Integrations                       │
│                                                                     │
│  ┌─────────────┐                              ┌─────────────┐       │
│  │  Notebooks  │──────┐              ┌───────│    Model    │       │
│  │ (Jupyter)   │      │              │       │  Registry   │       │
│  └─────────────┘      │              │       └─────────────┘       │
│                       ▼              ▲                              │
│  ┌─────────────┐  ┌──────────────────────┐  ┌─────────────┐       │
│  │   CI/CD     │──│  Experiment Tracking │──│  Feature    │       │
│  │  Pipeline   │  │       System         │  │   Store     │       │
│  └─────────────┘  └──────────────────────┘  └─────────────┘       │
│                       ▲              ▼                              │
│  ┌─────────────┐      │              │       ┌─────────────┐       │
│  │  Training   │──────┘              └───────│ Monitoring  │       │
│  │   Jobs      │                             │   System    │       │
│  └─────────────┘                             └─────────────┘       │
└─────────────────────────────────────────────────────────────────────┘
```

### 6.2 CI/CD Integration

```yaml
# GitHub Actions - Automated experiment
name: ML Training Pipeline
on:
  push:
    paths:
      - 'src/models/**'
      - 'data/**'

jobs:
  train:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run training
        env:
          MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }}
          MLFLOW_TRACKING_USERNAME: ${{ secrets.MLFLOW_USERNAME }}
          MLFLOW_TRACKING_PASSWORD: ${{ secrets.MLFLOW_PASSWORD }}
        run: |
          python train.py \
            --experiment-name "automated-training" \
            --run-name "ci-${{ github.sha }}"
      
      - name: Register model if improved
        run: |
          python scripts/register_if_improved.py \
            --model-name "fraud-detection" \
            --metric "accuracy" \
            --threshold 0.01
```

### 6.3 Feature Store Integration

```python
import mlflow
from feast import FeatureStore

# Initialize feature store
store = FeatureStore(repo_path="feature_repo/")

# Get training features
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=[
        "user_features:transaction_count_7d",
        "user_features:avg_transaction_amount",
        "merchant_features:fraud_rate"
    ]
).to_df()

# Track feature store reference in experiment
with mlflow.start_run():
    # Log feature store metadata
    mlflow.log_param("feature_store_repo", "feature_repo/")
    mlflow.set_tag("feast.feature_view", "user_features,merchant_features")
    mlflow.set_tag("feast.entity_df_hash", entity_df_hash)
    
    # Train model with features
    model.fit(training_df[features], training_df[target])
```

### 6.4 Model Registry Integration

```python
import mlflow

with mlflow.start_run() as run:
    # Train model
    model.fit(X_train, y_train)
    
    # Log model
    mlflow.sklearn.log_model(model, "model")
    
    # Evaluate
    accuracy = model.score(X_test, y_test)
    mlflow.log_metric("test_accuracy", accuracy)
    
    # Register model if accuracy threshold met
    if accuracy > 0.9:
        model_uri = f"runs:/{run.info.run_id}/model"
        mlflow.register_model(model_uri, "fraud-detection-model")
        
        # Set alias
        client = mlflow.MlflowClient()
        client.set_registered_model_alias(
            "fraud-detection-model",
            "challenger",
            version=latest_version
        )
```

---

## 7. Best Practices

> **Section Dependencies:**
> - Depends on: All previous sections
> - Feeds into: Team guidelines, Training materials
> - Update trigger: Lessons learned

### 7.1 Experiment Organization

```
Experiment Naming Convention:
{project}/{use-case}/{experiment-type}

Examples:
- fraud-detection/realtime-scoring/baseline
- fraud-detection/realtime-scoring/feature-engineering
- fraud-detection/realtime-scoring/hyperparameter-tuning
- recommendations/collaborative-filtering/v2-experiments
```

### 7.2 Run Naming Convention

```
Run Naming:
{model-type}-{description}-{date/version}

Examples:
- xgboost-baseline-20240115
- rf-with-new-features-v2
- lstm-sequence-length-experiment
- ensemble-final-candidate
```

### 7.3 Tagging Strategy

| Tag Category | Key | Example Values |
|--------------|-----|----------------|
| **Team** | team | fraud-ml, recommendations |
| **Environment** | environment | dev, staging, prod |
| **Model Type** | model_type | classification, regression |
| **Data** | dataset_version | v1.2.3 |
| **Experiment** | experiment_type | baseline, ablation, tuning |
| **Priority** | priority | high, medium, low |
| **Status** | status | wip, review, approved |

### 7.4 Common Mistakes to Avoid

| Mistake | Impact | Solution |
|---------|--------|----------|
| Not setting experiment | All runs in default | Always `set_experiment()` |
| Logging params after training | Partial tracking | Log params at start |
| Missing step in metrics | No training curves | Always include step |
| Large artifacts | Storage costs | Compress, sample |
| No run names | Hard to identify | Descriptive names |
| Missing tags | Poor organization | Standard tag set |

---

## 8. Governance & Operations

> **Section Dependencies:**
> - Depends on: MOP-025 Security Architecture
> - Feeds into: Compliance, Operations
> - Update trigger: Policy changes

### 8.1 Access Control

| Role | Experiments | Runs | Artifacts | Admin |
|------|-------------|------|-----------|-------|
| Viewer | Read | Read | Read | None |
| ML Engineer | Create/Edit | Create/Edit | Create/Edit | None |
| ML Lead | All | All | All | Experiments |
| Admin | All | All | All | All |

### 8.2 Operational Runbooks

#### Backup Procedure
```bash
#!/bin/bash
# Backup MLflow metadata database

# PostgreSQL backup
pg_dump -h $DB_HOST -U mlflow mlflow > mlflow_backup_$(date +%Y%m%d).sql

# S3 artifact sync to backup bucket
aws s3 sync s3://mlflow-artifacts s3://mlflow-artifacts-backup/$(date +%Y%m%d)/
```

#### Cleanup Procedure
```bash
#!/bin/bash
# Clean up old experiments and runs

# Delete runs older than retention period
mlflow gc --backend-store-uri postgresql://mlflow@db/mlflow

# Archive experiments with no recent runs
python scripts/archive_stale_experiments.py --days 180
```

### 8.3 Monitoring

| Metric | Alert Threshold | Action |
|--------|-----------------|--------|
| DB connections | > 80% | Scale connections |
| Storage usage | > 80% | Add storage / cleanup |
| API latency P99 | > 1s | Investigate / scale |
| Failed runs % | > 20% | Investigate failures |
| Tracking errors | > 10/hour | Check connectivity |

---

## Appendices

### Appendix A: Quick Reference

```python
# Essential MLflow commands
import mlflow

# Configuration
mlflow.set_tracking_uri("http://mlflow-server:5000")
mlflow.set_experiment("my-experiment")

# Tracking
with mlflow.start_run(run_name="my-run"):
    mlflow.log_param("key", "value")
    mlflow.log_metric("accuracy", 0.95, step=10)
    mlflow.log_artifact("file.txt")
    mlflow.set_tag("key", "value")
    mlflow.sklearn.log_model(model, "model")

# Search
client = mlflow.MlflowClient()
runs = client.search_runs(experiment_ids=["0"], filter_string="metrics.acc > 0.9")

# Model registry
mlflow.register_model("runs:/run_id/model", "model-name")
```

### Appendix B: Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Tracking server unreachable | Network/auth | Check URI, credentials |
| Artifact upload fails | Storage permissions | Check S3/GCS IAM |
| Run not appearing | Wrong experiment | Verify experiment ID |
| Metrics not updating | Connection timeout | Batch logging |
| Large artifact error | Size limits | Compress or chunk |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [Date] | [Author] | Initial draft |
| 1.0 | [Date] | [Author] | Approved version |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| ML Platform Lead | | | |
| Data Engineering Lead | | | |
