---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-092: Continuous Training Pipeline

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-092 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## 1. Continuous Training Overview

### 1.1 Training Triggers

| Trigger | Condition | Action |
|---------|-----------|--------|
| Scheduled | Daily/Weekly/Monthly | Full retraining |
| Data Drift | Drift score > threshold | Automatic retraining |
| Performance Degradation | Accuracy drop > 5% | Automatic retraining |
| New Data | Data volume increase | Incremental training |
| Manual | On-demand | Full retraining |

### 1.2 Training Modes

| Mode | Use Case | Duration |
|------|----------|----------|
| Full Retraining | New algorithm, major changes | Hours |
| Incremental | New data, same algorithm | Minutes |
| Fine-tuning | Domain adaptation | Minutes-Hours |

---

## 2. Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│              Continuous Training Pipeline                        │
│                                                                 │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐     │
│  │ Trigger │───►│ Prepare │───►│  Train  │───►│ Validate│     │
│  └─────────┘    └─────────┘    └─────────┘    └─────────┘     │
│       │              │              │              │            │
│       ▼              ▼              ▼              ▼            │
│  • Schedule     • Fetch data   • Train model  • Evaluate      │
│  • Drift alert  • Validate     • Log metrics  • Compare       │
│  • API trigger  • Transform    • Save model   • Quality gates │
│                                                                │
│                         ▼                                      │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐                    │
│  │Register │───►│ Approve │───►│ Deploy  │                    │
│  └─────────┘    └─────────┘    └─────────┘                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Kubeflow Pipeline Implementation

```python
# pipelines/continuous_training.py
from kfp import dsl
from kfp.dsl import component, Input, Output, Dataset, Model, Metrics

@component(base_image="python:3.11")
def prepare_data(
    data_source: str,
    output_data: Output[Dataset]
):
    """Prepare training data."""
    import pandas as pd
    
    # Fetch data
    df = pd.read_parquet(data_source)
    
    # Validate
    assert len(df) > 1000, "Insufficient data"
    assert df.isnull().sum().sum() / len(df) < 0.05, "Too many nulls"
    
    # Save
    df.to_parquet(output_data.path)

@component(base_image="python:3.11")
def train_model(
    train_data: Input[Dataset],
    model_output: Output[Model],
    metrics_output: Output[Metrics],
    hyperparameters: dict
):
    """Train model."""
    import mlflow
    import xgboost as xgb
    
    # Load data
    df = pd.read_parquet(train_data.path)
    X, y = df.drop('label', axis=1), df['label']
    
    # Train
    with mlflow.start_run():
        model = xgb.XGBClassifier(**hyperparameters)
        model.fit(X, y)
        
        # Log metrics
        metrics = evaluate_model(model, X, y)
        mlflow.log_metrics(metrics)
        
        # Save model
        mlflow.xgboost.log_model(model, "model")
        
        # Output
        model.save_model(model_output.path)
        
        for name, value in metrics.items():
            metrics_output.log_metric(name, value)

@component(base_image="python:3.11")
def validate_model(
    model: Input[Model],
    test_data: Input[Dataset],
    baseline_metrics: dict,
    validation_result: Output[str]
):
    """Validate model against baseline."""
    import xgboost as xgb
    
    # Load
    model = xgb.XGBClassifier()
    model.load_model(model.path)
    
    df = pd.read_parquet(test_data.path)
    X, y = df.drop('label', axis=1), df['label']
    
    # Evaluate
    metrics = evaluate_model(model, X, y)
    
    # Compare to baseline
    passed = all(
        metrics[k] >= baseline_metrics[k] * 0.98  # Allow 2% degradation
        for k in ['accuracy', 'f1']
    )
    
    validation_result.value = "PASSED" if passed else "FAILED"

@component(base_image="python:3.11")
def register_model(
    model: Input[Model],
    model_name: str,
    validation_result: str
):
    """Register model if validation passed."""
    import mlflow
    
    if validation_result != "PASSED":
        raise ValueError("Model validation failed")
    
    # Register
    mlflow.register_model(
        model_uri=model.uri,
        name=model_name
    )

@dsl.pipeline(name="continuous-training")
def continuous_training_pipeline(
    data_source: str,
    model_name: str,
    hyperparameters: dict
):
    """Continuous training pipeline."""
    
    # Prepare data
    prepare_task = prepare_data(data_source=data_source)
    
    # Train model
    train_task = train_model(
        train_data=prepare_task.outputs["output_data"],
        hyperparameters=hyperparameters
    )
    
    # Validate
    validate_task = validate_model(
        model=train_task.outputs["model_output"],
        test_data=prepare_task.outputs["output_data"],
        baseline_metrics={"accuracy": 0.90, "f1": 0.85}
    )
    
    # Register if passed
    register_task = register_model(
        model=train_task.outputs["model_output"],
        model_name=model_name,
        validation_result=validate_task.outputs["validation_result"]
    )
```

---

## 4. Scheduled Training

### 4.1 Airflow DAG

```python
# dags/scheduled_retraining.py
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

with DAG(
    'scheduled_retraining',
    schedule_interval='0 2 * * 0',  # Weekly Sunday 2 AM
    catchup=False,
) as dag:
    
    retrain = KubernetesPodOperator(
        task_id='retrain_model',
        name='retrain-fraud-model',
        namespace='training',
        image='mlops/training:latest',
        cmds=['python', '-m', 'pipelines.train'],
        arguments=['--model', 'fraud-detection'],
        env_vars={
            'MLFLOW_TRACKING_URI': '{{ var.value.mlflow_uri }}'
        },
        resources={
            'request_cpu': '4',
            'request_memory': '16Gi',
            'limit_gpu': '1'
        }
    )
```

---

## 5. Drift-Triggered Training

```python
# triggers/drift_trigger.py
def check_and_trigger_retraining(model_name: str):
    """Check drift and trigger retraining if needed."""
    from kfp import Client
    
    # Check drift score
    drift_score = get_current_drift_score(model_name)
    
    if drift_score > DRIFT_THRESHOLD:
        # Trigger pipeline
        client = Client()
        client.create_run_from_pipeline_func(
            continuous_training_pipeline,
            arguments={
                'data_source': f's3://data/{model_name}/latest/',
                'model_name': model_name,
                'hyperparameters': get_hyperparameters(model_name)
            },
            run_name=f"drift-triggered-{model_name}-{datetime.now().isoformat()}"
        )
        
        notify(f"Retraining triggered for {model_name} due to drift")
```

---

## 6. Monitoring Training Runs

### 6.1 Metrics

| Metric | Target | Alert |
|--------|--------|-------|
| Training success rate | >95% | <90% |
| Training duration | <baseline×2 | >baseline×3 |
| Model improvement | >0% | <-5% |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial continuous training |
