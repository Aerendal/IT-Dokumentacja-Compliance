---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-040: Pipeline Documentation Reference

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-040 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## 1. Pipeline Catalog

### 1.1 Training Pipelines

| Pipeline | Trigger | Schedule | Owner |
|----------|---------|----------|-------|
| fraud-model-training | Manual/Scheduled | Daily 02:00 | fraud-team |
| recommendation-training | Manual | Weekly Sun | rec-team |
| nlp-model-training | On data change | - | nlp-team |

### 1.2 Data Pipelines

| Pipeline | Source | Destination | Schedule |
|----------|--------|-------------|----------|
| feature-ingestion | Snowflake | Feast | Hourly |
| data-quality-check | S3 | Reports | Daily |
| model-metrics-etl | Prometheus | Snowflake | Hourly |

### 1.3 CI/CD Pipelines

| Pipeline | Trigger | Stages |
|----------|---------|--------|
| model-ci | PR to main | Lint → Test → Build |
| model-cd | Merge to main | Validate → Stage → Prod |
| infra-ci | PR to infra/ | Terraform plan |

---

## 2. Pipeline Specifications

### 2.1 Standard Training Pipeline

```yaml
# training-pipeline-spec.yaml
name: standard-training
stages:
  - name: data-validation
    image: mlops/data-validator:latest
    inputs: [data_path]
    outputs: [validation_report]
    
  - name: feature-engineering
    image: mlops/feature-eng:latest
    inputs: [validated_data]
    outputs: [feature_set]
    
  - name: training
    image: mlops/trainer:latest
    inputs: [feature_set, hyperparams]
    outputs: [model_artifact]
    resources:
      gpu: 1
      memory: 16Gi
      
  - name: evaluation
    image: mlops/evaluator:latest
    inputs: [model_artifact, test_data]
    outputs: [metrics, reports]
    
  - name: registration
    image: mlops/registrar:latest
    inputs: [model_artifact, metrics]
    outputs: [model_uri]
    condition: metrics.accuracy > 0.9
```

### 2.2 CI/CD Pipeline Stages

```
┌─────────────────────────────────────────────────────────────┐
│                    Model CI/CD Pipeline                      │
│                                                             │
│  PR Created                                                 │
│      │                                                      │
│      ▼                                                      │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐   │
│  │  Lint   │──►│  Test   │──►│  Build  │──►│ Publish │   │
│  │         │   │  Unit   │   │  Image  │   │ to ECR  │   │
│  └─────────┘   └─────────┘   └─────────┘   └─────────┘   │
│                                                  │          │
│  Merge to Main                                   │          │
│      │                                           │          │
│      ▼                                           ▼          │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐   │
│  │Validate │──►│ Deploy  │──►│ Smoke   │──►│ Deploy  │   │
│  │ Model   │   │ Staging │   │  Test   │   │  Prod   │   │
│  └─────────┘   └─────────┘   └─────────┘   └─────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Pipeline Parameters Reference

### 3.1 Common Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `data_path` | string | - | S3 path to training data |
| `model_name` | string | - | Name for model registration |
| `experiment_name` | string | "default" | MLflow experiment |
| `gpu_count` | int | 0 | Number of GPUs |
| `memory_gb` | int | 8 | Memory allocation |

### 3.2 Model-Specific Parameters

| Model | Parameter | Type | Default |
|-------|-----------|------|---------|
| fraud | threshold | float | 0.5 |
| fraud | lookback_days | int | 30 |
| recommendation | num_factors | int | 100 |
| nlp | max_seq_length | int | 512 |

---

## 4. Pipeline Monitoring

### 4.1 Key Metrics

| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| pipeline_duration_seconds | Total runtime | >2x baseline |
| pipeline_success_rate | Success percentage | <95% |
| stage_failure_count | Failed stages | >0 |

### 4.2 Dashboard Links

| Dashboard | URL |
|-----------|-----|
| Pipeline Overview | grafana.example.com/d/pipelines |
| Training Metrics | grafana.example.com/d/training |
| CI/CD Status | grafana.example.com/d/cicd |

---

## 5. Troubleshooting Quick Reference

| Issue | Check | Fix |
|-------|-------|-----|
| Pipeline stuck | Airflow UI, pod logs | Restart task |
| OOM error | Resource limits | Increase memory |
| Data not found | S3 permissions | Check IAM role |
| Model too large | Artifact size | Use compression |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial reference |
