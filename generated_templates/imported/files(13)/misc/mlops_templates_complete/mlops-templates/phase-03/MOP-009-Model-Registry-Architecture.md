---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-009: Model Registry Architecture

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-009 |
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
-  Need for centralized model management identified
-  Multiple models being developed across teams

### When This Document Becomes Invalid
-  Registry platform migration (create new version)
-  New model types require different registry patterns
-  Architecture fundamentally changes

### Validity Conditions
-  Supports all model types in use
-  Versioning scheme defined
-  Integration with CI/CD established
-  Access control implemented

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-007: Architecture | Registry placement in architecture |
| MOP-005: ML Lifecycle Requirements | Model lifecycle stages |
| MOP-025: Security Architecture | Access control requirements |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-018: Model Registry Setup | Implementation specs |
| MOP-026: Access Control | RBAC requirements |
| MOP-027: Audit Trail | Lineage requirements |
| MOP-008: CI/CD Pipeline | Model promotion workflow |

### Bidirectional Dependencies
| Document | Relationship |
|----------|--------------|
| MOP-008: CI/CD Pipeline | Registry ↔ Pipeline stages |
| MOP-010: Experiment Tracking | Experiments ↔ Models |
| MOP-012: Model Serving | Registry ↔ Serving |

---

## Section Dependencies (Internal)

```
┌────────────────────────────────────────────────────────────────┐
│              1. Registry Overview                               │
└────────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
│ 2. Data Model    │ │ 3. Version   │ │ 4. Lifecycle     │
│    & Schema      │ │    Strategy  │ │    Stages        │
└──────────────────┘ └──────────────┘ └──────────────────┘
        │                   │                  │
        └───────────────────┼──────────────────┘
                            ▼
┌────────────────────────────────────────────────────────────────┐
│              5. Model Metadata                                  │
└────────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
│ 6. Integration   │ │ 7. Access    │ │ 8. Lineage &     │
│    Points        │ │    Control   │ │    Governance    │
└──────────────────┘ └──────────────┘ └──────────────────┘
```

---

## Template Content

---

# Model Registry Architecture Document

**[Organization Name]**

**Version:** [X.Y]  
**Date:** [YYYY-MM-DD]

---

## 1. Registry Overview

> **Section Dependencies:**
> - Depends on: MOP-007 Architecture
> - Feeds into: All other sections
> - Update trigger: Platform strategy changes

### 1.1 Purpose

The Model Registry serves as the central repository for all machine learning models, providing:
- **Version Control**: Track all model versions and their evolution
- **Lifecycle Management**: Manage model stages from development to production
- **Lineage Tracking**: Maintain complete provenance of models
- **Governance**: Enable model governance and compliance
- **Collaboration**: Facilitate model sharing across teams

### 1.2 Scope

| In Scope | Out of Scope |
|----------|--------------|
| Model artifact storage | Training infrastructure |
| Model metadata management | Experiment tracking (separate system) |
| Version control | Data versioning (DVC/lakefs) |
| Lifecycle stage management | Model serving runtime |
| Model lineage | Feature store |
| Access control | Model monitoring |

### 1.3 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Model Registry                                │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │                       Registry API                               ││
│  │  - REST API      - Python SDK      - CLI                        ││
│  └──────────────────────────┬──────────────────────────────────────┘│
│                             │                                       │
│  ┌──────────────────────────┼──────────────────────────────────────┐│
│  │                    Registry Core                                 ││
│  │                          │                                       ││
│  │  ┌─────────┐  ┌─────────┴─────────┐  ┌─────────┐               ││
│  │  │ Version │  │     Lifecycle     │  │ Lineage │               ││
│  │  │ Manager │  │      Manager      │  │ Tracker │               ││
│  │  └─────────┘  └───────────────────┘  └─────────┘               ││
│  │                                                                  ││
│  │  ┌─────────┐  ┌───────────────────┐  ┌─────────┐               ││
│  │  │ Search  │  │     Metadata      │  │ Access  │               ││
│  │  │ & Query │  │      Store        │  │ Control │               ││
│  │  └─────────┘  └───────────────────┘  └─────────┘               ││
│  └─────────────────────────────────────────────────────────────────┘│
│                             │                                       │
│  ┌──────────────────────────┼──────────────────────────────────────┐│
│  │                    Storage Layer                                 ││
│  │                          │                                       ││
│  │  ┌─────────────────┐    │    ┌─────────────────┐               ││
│  │  │  Metadata DB    │◄───┴───►│  Artifact Store │               ││
│  │  │  (PostgreSQL)   │         │    (S3/GCS)     │               ││
│  │  └─────────────────┘         └─────────────────┘               ││
│  └─────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────┘
```

### 1.4 Technology Selection

| Component | Technology | Rationale |
|-----------|------------|-----------|
| Registry Platform | [MLflow / Custom / Vertex AI] | [Rationale] |
| Metadata Database | [PostgreSQL / MySQL] | Relational metadata |
| Artifact Storage | [S3 / GCS / Azure Blob] | Scalable object storage |
| API Framework | [FastAPI / Flask] | If custom |
| Authentication | [OAuth2 / OIDC] | Enterprise SSO |

---

## 2. Data Model & Schema

> **Section Dependencies:**
> - Depends on: Section 1 (Overview)
> - Feeds into: Section 5 (Metadata), Implementation
> - Update trigger: New model types, new metadata requirements

### 2.1 Core Entities

```
┌───────────────────────────────────────────────────────────────────┐
│                     Entity Relationship Diagram                    │
│                                                                   │
│  ┌─────────────────┐         ┌─────────────────┐                 │
│  │ Registered Model│         │    Experiment   │                 │
│  │─────────────────│         │─────────────────│                 │
│  │ name (PK)       │         │ experiment_id   │                 │
│  │ description     │         │ name            │                 │
│  │ created_at      │         │ artifact_location│                │
│  │ updated_at      │         └────────┬────────┘                 │
│  │ tags[]          │                  │                          │
│  └────────┬────────┘                  │ 1:N                      │
│           │                           │                          │
│           │ 1:N                       ▼                          │
│           │                  ┌─────────────────┐                 │
│           │                  │      Run        │                 │
│           │                  │─────────────────│                 │
│           │                  │ run_id (PK)     │                 │
│           ▼                  │ experiment_id   │                 │
│  ┌─────────────────┐         │ status          │                 │
│  │  Model Version  │◄────────│ start_time      │                 │
│  │─────────────────│  1:1    │ end_time        │                 │
│  │ version (PK)    │         │ metrics{}       │                 │
│  │ model_name (FK) │         │ params{}        │                 │
│  │ run_id (FK)     │         └─────────────────┘                 │
│  │ source          │                                             │
│  │ stage           │                                             │
│  │ created_at      │                                             │
│  │ aliases[]       │                                             │
│  │ tags[]          │                                             │
│  └─────────────────┘                                             │
│           │                                                       │
│           │ 1:N                                                   │
│           ▼                                                       │
│  ┌─────────────────┐                                             │
│  │    Artifact     │                                             │
│  │─────────────────│                                             │
│  │ artifact_path   │                                             │
│  │ file_size       │                                             │
│  │ file_type       │                                             │
│  └─────────────────┘                                             │
└───────────────────────────────────────────────────────────────────┘
```

### 2.2 Registered Model Schema

```yaml
registered_model:
  name: string (unique, required)
    pattern: "^[a-zA-Z][a-zA-Z0-9_-]{0,127}$"
    description: "Unique model identifier"
  
  description: string (optional)
    max_length: 5000
    description: "Human-readable model description"
  
  tags: array[tag]
    description: "Key-value tags for categorization"
    items:
      key: string (max 250 chars)
      value: string (max 5000 chars)
  
  aliases: array[string]
    description: "Named references to versions"
    examples: ["champion", "challenger", "latest"]
  
  created_timestamp: datetime
  last_updated_timestamp: datetime
  
  # Extended metadata (custom)
  owner: string
  team: string
  use_case: string
  model_type: enum[classification, regression, ranking, nlp, cv, llm]
  business_domain: string
```

### 2.3 Model Version Schema

```yaml
model_version:
  name: string (FK to registered_model)
  version: integer (auto-increment per model)
  
  # Source tracking
  run_id: string (FK to experiment run)
  source: uri (artifact location)
  
  # Lifecycle
  stage: enum[None, Staging, Production, Archived]
    deprecated: true  # Use aliases instead for MLflow 2.x+
  current_stage: string (deprecated)
  aliases: array[string]
  
  # Timestamps
  creation_timestamp: datetime
  last_updated_timestamp: datetime
  
  # Metadata
  description: string
  tags: array[tag]
  
  # Model signature
  signature:
    inputs: schema
    outputs: schema
  
  # Extended metadata (custom)
  model_size_bytes: integer
  framework: enum[sklearn, pytorch, tensorflow, xgboost, lightgbm, custom]
  framework_version: string
  python_version: string
  
  # Performance metadata
  metrics:
    training_accuracy: float
    validation_accuracy: float
    test_accuracy: float
    # ... other metrics
  
  # Deployment metadata
  deployed_to: array[string]
  deployment_timestamp: datetime
```

### 2.4 Model Artifacts Structure

```
models/
└── {model_name}/
    └── {version}/
        ├── MLmodel              # Model metadata file
        ├── model.pkl            # Serialized model (sklearn)
        │   OR model.pt          # (PyTorch)
        │   OR saved_model.pb    # (TensorFlow)
        ├── conda.yaml           # Environment specification
        ├── requirements.txt     # Pip requirements
        ├── python_env.yaml      # Python environment
        ├── input_example.json   # Sample input
        └── artifacts/           # Additional artifacts
            ├── feature_importance.png
            ├── confusion_matrix.png
            └── metrics.json
```

---

## 3. Versioning Strategy

> **Section Dependencies:**
> - Depends on: Section 2 (Data Model)
> - Feeds into: CI/CD Pipeline, Release management
> - Update trigger: Versioning policy changes

### 3.1 Version Numbering

| Scheme | Format | Use Case |
|--------|--------|----------|
| Sequential | 1, 2, 3, ... | Default auto-increment |
| Semantic | 1.0.0, 1.0.1, 1.1.0 | Complex model evolution |
| Git-based | git commit hash | Traceability to code |
| Date-based | 2024.01.15.1 | Time-based releases |

**Recommended:** Sequential versioning with aliases for stage management.

### 3.2 Model Aliases

```yaml
aliases:
  champion:
    description: "Current production model"
    version: 5
    auto_update: false
  
  challenger:
    description: "Candidate for next champion"
    version: 6
    auto_update: false
  
  latest:
    description: "Most recent registered version"
    version: 7
    auto_update: true
  
  baseline:
    description: "Reference baseline model"
    version: 1
    auto_update: false
```

### 3.3 Version Comparison

| Version A | Version B | Comparison |
|-----------|-----------|------------|
| v5 (champion) | v6 (challenger) | A/B test results |
| v6 | v1 (baseline) | Improvement over baseline |
| v7 (latest) | v6 | Latest vs challenger |

### 3.4 Version Retention Policy

| Stage | Retention | Action |
|-------|-----------|--------|
| None | 30 days | Auto-archive |
| Staging | 90 days | Review for promotion/archive |
| Production | Indefinite | Manual archive only |
| Archived | 1 year | Auto-delete (configurable) |

---

## 4. Lifecycle Stages

> **Section Dependencies:**
> - Depends on: Section 3 (Versioning), MOP-008 (CI/CD)
> - Feeds into: Deployment procedures, Access control
> - Update trigger: Process changes

### 4.1 Stage Definitions

```
┌─────────────────────────────────────────────────────────────────────┐
│                     Model Lifecycle Stages                          │
│                                                                     │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐         │
│  │  None   │───►│ Staging │───►│Production│───►│ Archived│         │
│  │(Development)│ │         │    │         │    │         │         │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘         │
│       │              │              │              │                │
│       │              │              │              │                │
│       ▼              ▼              ▼              ▼                │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐         │
│  │ - Dev   │    │ - Staging│   │ - Prod  │    │ - Read  │         │
│  │   testing│   │   tests  │    │   deploy│   │   only  │         │
│  │ - No SLA│    │ - Limited│   │ - Full  │    │ - No    │         │
│  │         │    │   traffic│   │   traffic│   │   deploy│         │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘         │
└─────────────────────────────────────────────────────────────────────┘
```

### 4.2 Stage Transitions

| From | To | Trigger | Requirements | Approver |
|------|-----|---------|--------------|----------|
| None | Staging | Manual/Auto | Quality gates pass | ML Engineer |
| Staging | Production | Manual | Staging tests pass, approval | ML Lead + Product |
| Production | Archived | Manual | Replacement deployed | ML Lead |
| Staging | Archived | Manual/Auto | Failed tests or timeout | ML Engineer |
| Staging | None | Manual | Rollback needed | ML Engineer |
| Production | None | Manual | Emergency rollback | ML Lead + SRE |

### 4.3 Stage Requirements

#### None (Development)
- [ ] Model registered
- [ ] Basic metadata present
- [ ] Model signature defined

#### Staging
- [ ] All "None" requirements
- [ ] Unit tests pass
- [ ] Model quality metrics meet threshold
- [ ] Input/output validation
- [ ] Performance benchmark run
- [ ] Bias/fairness check (if applicable)

#### Production
- [ ] All "Staging" requirements
- [ ] Integration tests pass
- [ ] Load tests pass
- [ ] Security scan clear
- [ ] Model documentation complete
- [ ] Rollback plan documented
- [ ] Approval from stakeholders

#### Archived
- [ ] No active deployments
- [ ] Lineage preserved
- [ ] Successor documented

### 4.4 Stage Transition Automation

```yaml
# Stage transition rules
transitions:
  none_to_staging:
    automated: true
    conditions:
      - quality_gate: model_accuracy >= 0.85
      - quality_gate: latency_p99 <= 100ms
      - check: model_signature_present
      - check: unit_tests_pass
    
  staging_to_production:
    automated: false
    conditions:
      - check: staging_tests_pass
      - check: load_tests_pass
      - check: security_scan_clear
      - check: documentation_complete
    approval:
      required: true
      approvers:
        - role: ml_lead
        - role: product_owner
    
  auto_archive:
    trigger: "staging_age > 90 days AND not_promoted"
    notify: [model_owner, ml_team]
```

---

## 5. Model Metadata

> **Section Dependencies:**
> - Depends on: Section 2 (Schema), MOP-027 (Audit Trail)
> - Feeds into: Search, Governance, Documentation
> - Update trigger: Metadata requirements change

### 5.1 Required Metadata

| Category | Field | Required | Source |
|----------|-------|----------|--------|
| **Identity** | model_name |  | User |
| | version |  | System |
| | run_id |  | Experiment tracker |
| **Ownership** | owner |  | User/SSO |
| | team |  | User |
| | contact |  | User |
| **Technical** | framework |  | Auto-detected |
| | python_version |  | Auto-detected |
| | model_signature |  | Auto-detected |
| | model_size |  | Auto-computed |
| **Lifecycle** | stage |  | System |
| | created_at |  | System |
| | updated_at |  | System |

### 5.2 Recommended Metadata

| Category | Field | Purpose |
|----------|-------|---------|
| **Business** | use_case | Business context |
| | business_owner | Stakeholder |
| | cost_center | Chargeback |
| **Training** | training_dataset | Data provenance |
| | training_date | When trained |
| | hyperparameters | Reproducibility |
| **Performance** | accuracy | Quality metric |
| | f1_score | Quality metric |
| | auc | Quality metric |
| | latency_p50 | Performance |
| | latency_p99 | Performance |
| **Governance** | bias_report | Fairness |
| | explainability | Interpretability |
| | data_sensitivity | Compliance |

### 5.3 Model Card Template

```yaml
model_card:
  model_details:
    name: "{model_name}"
    version: "{version}"
    type: "{classification|regression|ranking|nlp|cv|llm}"
    framework: "{sklearn|pytorch|tensorflow|xgboost}"
    description: |
      {Detailed description of what the model does}
    
  intended_use:
    primary_uses:
      - "{Primary use case 1}"
      - "{Primary use case 2}"
    out_of_scope_uses:
      - "{What the model should NOT be used for}"
    users:
      - "{Target user persona}"
    
  training_data:
    datasets:
      - name: "{dataset_name}"
        version: "{version}"
        size: "{n samples}"
        features: "{n features}"
    preprocessing: |
      {Description of data preprocessing}
    
  evaluation:
    metrics:
      - metric: accuracy
        value: 0.92
        dataset: test_set
      - metric: f1_score
        value: 0.89
        dataset: test_set
    sliced_metrics:
      - slice: "age_group=18-25"
        accuracy: 0.90
      - slice: "age_group=25-35"
        accuracy: 0.93
    
  ethical_considerations:
    bias_analysis: |
      {Results of bias/fairness analysis}
    sensitive_data: |
      {Any sensitive data used}
    limitations: |
      {Known limitations}
    
  caveats_and_recommendations:
    - "{Caveat 1}"
    - "{Recommendation 1}"
```

---

## 6. Integration Points

> **Section Dependencies:**
> - Depends on: MOP-007 Architecture
> - Feeds into: Implementation, API design
> - Update trigger: New integrations needed

### 6.1 Integration Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Model Registry Integrations                       │
│                                                                     │
│  ┌─────────────────┐              ┌─────────────────┐              │
│  │   Experiment    │              │    CI/CD        │              │
│  │    Tracking     │──────────────│    Pipeline     │              │
│  │   (MLflow)      │   Register   │                 │              │
│  └─────────────────┘              └────────┬────────┘              │
│           │                                │                        │
│           │ Experiments                    │ Promote                │
│           ▼                                ▼                        │
│  ┌────────────────────────────────────────────────────────────────┐│
│  │                      MODEL REGISTRY                             ││
│  │                                                                 ││
│  │  REST API  │  Python SDK  │  CLI  │  UI                        ││
│  └────────────────────────────────────────────────────────────────┘│
│           │                                │                        │
│           │ Load                           │ Deploy                 │
│           ▼                                ▼                        │
│  ┌─────────────────┐              ┌─────────────────┐              │
│  │   Notebooks     │              │  Model Serving  │              │
│  │   (JupyterHub)  │              │    (Triton)     │              │
│  └─────────────────┘              └─────────────────┘              │
│                                            │                        │
│                                            │ Metrics                │
│                                            ▼                        │
│                                   ┌─────────────────┐              │
│                                   │   Monitoring    │              │
│                                   │   (Prometheus)  │              │
│                                   └─────────────────┘              │
└─────────────────────────────────────────────────────────────────────┘
```

### 6.2 API Specifications

#### Register Model

```http
POST /api/2.0/mlflow/registered-models/create
Content-Type: application/json

{
  "name": "fraud-detection-model",
  "description": "Fraud detection for payment transactions",
  "tags": [
    {"key": "team", "value": "fraud-ml"},
    {"key": "use_case", "value": "realtime-scoring"}
  ]
}
```

#### Create Model Version

```http
POST /api/2.0/mlflow/model-versions/create
Content-Type: application/json

{
  "name": "fraud-detection-model",
  "source": "runs:/abc123/model",
  "run_id": "abc123",
  "description": "New version with updated features"
}
```

#### Promote Model (Set Alias)

```http
POST /api/2.0/mlflow/registered-models/alias
Content-Type: application/json

{
  "name": "fraud-detection-model",
  "alias": "champion",
  "version": 5
}
```

#### Load Model for Inference

```python
import mlflow

# Load by version
model = mlflow.pyfunc.load_model("models:/fraud-detection-model/5")

# Load by alias
model = mlflow.pyfunc.load_model("models:/fraud-detection-model@champion")

# Load for production serving
model_uri = "models:/fraud-detection-model@champion"
```

### 6.3 Event Webhooks

| Event | Payload | Subscribers |
|-------|---------|-------------|
| `MODEL_REGISTERED` | model_name | Notification, Audit |
| `MODEL_VERSION_CREATED` | model_name, version | CI/CD, Notification |
| `MODEL_VERSION_STAGE_CHANGED` | model_name, version, stage | Serving, Notification |
| `MODEL_VERSION_TAG_SET` | model_name, version, tag | Audit |
| `MODEL_VERSION_DELETED` | model_name, version | Audit, Cleanup |

```yaml
webhooks:
  - event: MODEL_VERSION_STAGE_CHANGED
    url: https://cicd.example.com/hooks/model-promoted
    secret: ${WEBHOOK_SECRET}
    filter:
      new_stage: Production
      
  - event: MODEL_VERSION_CREATED
    url: https://slack.example.com/hooks/ml-notifications
    template: "New model version: {{model_name}} v{{version}}"
```

---

## 7. Access Control

> **Section Dependencies:**
> - Depends on: MOP-025 Security Architecture
> - Feeds into: MOP-026 Access Control Document
> - Update trigger: Policy changes

### 7.1 Role-Based Access Control (RBAC)

| Role | Models | Versions | Stage Transitions | Admin |
|------|--------|----------|-------------------|-------|
| Viewer | Read | Read | None | None |
| ML Engineer | Read/Write | Read/Write | None → Staging | None |
| ML Lead | Read/Write | Read/Write | All except to Prod | None |
| Release Manager | Read | Read | Staging → Prod | None |
| Admin | Full | Full | Full | Full |

### 7.2 Permission Matrix

| Action | Viewer | ML Engineer | ML Lead | Release Mgr | Admin |
|--------|--------|-------------|---------|-------------|-------|
| List models |  |  |  |  |  |
| View model details |  |  |  |  |  |
| Register model |  |  |  |  |  |
| Create version |  |  |  |  |  |
| Update metadata |  |  |  |  |  |
| Delete model |  |  |  |  |  |
| Promote to Staging |  |  |  |  |  |
| Promote to Production |  |  |  |  |  |
| Archive model |  |  |  |  |  |
| Manage permissions |  |  |  |  |  |

### 7.3 Model-Level Permissions

```yaml
model_permissions:
  fraud-detection-model:
    owners:
      - user: jane.doe@company.com
        role: admin
    teams:
      - team: fraud-ml
        role: ml_engineer
      - team: ml-platform
        role: admin
    service_accounts:
      - sa: cicd-pipeline@serviceaccount
        role: ml_engineer
```

---

## 8. Lineage & Governance

> **Section Dependencies:**
> - Depends on: Section 5 (Metadata), MOP-027 (Audit Trail)
> - Feeds into: Compliance reports, Audits
> - Update trigger: Compliance requirements change

### 8.1 Lineage Tracking

```
┌─────────────────────────────────────────────────────────────────────┐
│                      Model Lineage                                   │
│                                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐            │
│  │   Dataset   │───►│   Feature   │───►│  Training   │            │
│  │  (v1.2.3)   │    │    Set      │    │    Run      │            │
│  └─────────────┘    └─────────────┘    └──────┬──────┘            │
│                                               │                     │
│                                               ▼                     │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐            │
│  │  Deployed   │◄───│   Model     │◄───│   Model     │            │
│  │  Endpoint   │    │  Version 5  │    │  Artifact   │            │
│  └─────────────┘    └─────────────┘    └─────────────┘            │
│         │                                                          │
│         │ Predictions                                              │
│         ▼                                                          │
│  ┌─────────────┐                                                   │
│  │ Monitoring  │                                                   │
│  │   Metrics   │                                                   │
│  └─────────────┘                                                   │
└─────────────────────────────────────────────────────────────────────┘
```

### 8.2 Lineage Data Captured

| Entity | Tracked Information |
|--------|---------------------|
| Data Source | Source system, table, query, timestamp |
| Dataset Version | DVC/lakefs version, schema, statistics |
| Feature Set | Feature store reference, feature versions |
| Training Run | Experiment ID, run ID, parameters, metrics |
| Model Artifact | Storage URI, hash, size, format |
| Code | Git commit, repository, branch |
| Environment | Container image, dependencies |
| Deployment | Endpoint, timestamp, traffic percentage |

### 8.3 Governance Policies

```yaml
governance_policies:
  registration:
    required_fields:
      - owner
      - team
      - use_case
      - description
    naming_convention: "^[a-z][a-z0-9-]*$"
    max_name_length: 128
    
  production_promotion:
    required_documentation:
      - model_card
      - training_data_reference
      - bias_report
    required_tests:
      - unit_tests
      - integration_tests
      - performance_tests
    required_approvals: 2
    
  retention:
    archived_models: 365 days
    deleted_models: 90 days (soft delete)
    audit_logs: 7 years
    
  compliance:
    pii_check: required
    bias_check: required for user-facing models
    explainability: required for financial models
```

### 8.4 Audit Log

| Event | Logged Fields | Retention |
|-------|---------------|-----------|
| Model registered | user, timestamp, model_name | 7 years |
| Version created | user, timestamp, model, version, run_id | 7 years |
| Stage changed | user, timestamp, model, version, old_stage, new_stage | 7 years |
| Permission changed | user, timestamp, model, permission_change | 7 years |
| Model deleted | user, timestamp, model, reason | 7 years |
| Model accessed | user, timestamp, model, version, action | 1 year |

---

## Appendices

### Appendix A: MLflow Model Registry Quick Reference

```python
import mlflow
from mlflow import MlflowClient

client = MlflowClient()

# Register a model
model_uri = f"runs:/{run_id}/model"
mv = mlflow.register_model(model_uri, "model-name")

# Set alias (MLflow 2.x)
client.set_registered_model_alias("model-name", "champion", version=5)

# Get model by alias
model = mlflow.pyfunc.load_model("models:/model-name@champion")

# Search models
models = client.search_registered_models(filter_string="name LIKE '%fraud%'")

# Search versions
versions = client.search_model_versions(filter_string="run_id='abc123'")
```

### Appendix B: Migration Guide

| From | To | Migration Steps |
|------|-----|-----------------|
| File-based | MLflow | Export models, register in MLflow |
| Custom registry | MLflow | Map schemas, migrate metadata |
| MLflow 1.x | MLflow 2.x | Update stage → aliases |

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
| Data Governance | | | |
| Security | | | |
