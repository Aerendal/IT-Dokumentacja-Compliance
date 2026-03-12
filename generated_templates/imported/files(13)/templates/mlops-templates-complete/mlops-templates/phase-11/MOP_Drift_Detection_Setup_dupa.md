---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-080: Drift Detection Setup

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-080 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## 1. Drift Types

### 1.1 Drift Categories

| Type | Description | Detection Method |
|------|-------------|------------------|
| Data Drift | Input distribution change | Statistical tests |
| Concept Drift | Target relationship change | Performance monitoring |
| Prediction Drift | Output distribution change | Distribution comparison |
| Feature Drift | Individual feature shift | Per-feature monitoring |

### 1.2 Detection Thresholds

| Drift Type | Warning | Critical | Action |
|------------|---------|----------|--------|
| Data Drift (PSI) | >0.1 | >0.2 | Investigate / Retrain |
| Feature Drift (KS) | >0.05 | >0.1 | Alert / Investigate |
| Prediction Drift | >0.1 | >0.2 | Alert / Retrain |
| Performance Drop | >5% | >10% | Alert / Retrain |

---

## 2. Evidently Setup

### 2.1 Configuration

```python
# drift_detection/config.py
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class DriftConfig:
    model_name: str
    reference_dataset_path: str
    
    # Features to monitor
    numerical_features: List[str]
    categorical_features: List[str]
    target_column: Optional[str] = None
    prediction_column: str = "prediction"
    
    # Thresholds
    data_drift_threshold: float = 0.1
    feature_drift_threshold: float = 0.05
    
    # Scheduling
    check_frequency: str = "hourly"  # hourly, daily
    window_size: str = "1d"

# Example config
FRAUD_MODEL_CONFIG = DriftConfig(
    model_name="fraud-detection",
    reference_dataset_path="s3://mlops-data/reference/fraud_model_v2.parquet",
    numerical_features=["amount", "user_age_days", "transaction_count_30d"],
    categorical_features=["merchant_category", "country"],
    target_column="is_fraud",
    prediction_column="prediction",
    data_drift_threshold=0.1,
    feature_drift_threshold=0.05
)
```

### 2.2 Drift Monitor Implementation

```python
# drift_detection/monitor.py
from evidently.report import Report
from evidently.metrics import (
    DataDriftTable,
    DatasetDriftMetric,
    ColumnDriftMetric
)
from evidently.test_suite import TestSuite
from evidently.tests import (
    TestColumnDrift,
    TestShareOfDriftedColumns
)
import pandas as pd
from prometheus_client import Gauge

# Prometheus metrics
drift_score = Gauge(
    'mlops_drift_score',
    'Overall drift score',
    ['model_name']
)

feature_drift = Gauge(
    'mlops_feature_drift_score',
    'Per-feature drift score',
    ['model_name', 'feature_name']
)

class DriftMonitor:
    """Monitor data and prediction drift."""
    
    def __init__(self, config: DriftConfig):
        self.config = config
        self.reference_data = pd.read_parquet(config.reference_dataset_path)
    
    def check_drift(self, current_data: pd.DataFrame) -> dict:
        """Check for drift in current data."""
        
        # Create drift report
        report = Report(metrics=[
            DatasetDriftMetric(),
            DataDriftTable(),
        ])
        
        report.run(
            reference_data=self.reference_data,
            current_data=current_data
        )
        
        results = report.as_dict()
        
        # Extract results
        dataset_drift = results['metrics'][0]['result']['dataset_drift']
        drift_share = results['metrics'][0]['result']['share_of_drifted_columns']
        
        # Per-feature drift
        column_drift = {}
        for col_result in results['metrics'][1]['result']['drift_by_columns'].values():
            column_drift[col_result['column_name']] = {
                'drift_detected': col_result['drift_detected'],
                'drift_score': col_result['drift_score'],
                'stattest_name': col_result['stattest_name']
            }
        
        # Update Prometheus metrics
        drift_score.labels(model_name=self.config.model_name).set(drift_share)
        
        for feature, info in column_drift.items():
            feature_drift.labels(
                model_name=self.config.model_name,
                feature_name=feature
            ).set(info['drift_score'])
        
        return {
            'dataset_drift': dataset_drift,
            'drift_share': drift_share,
            'column_drift': column_drift,
            'timestamp': pd.Timestamp.now().isoformat()
        }
    
    def run_tests(self, current_data: pd.DataFrame) -> dict:
        """Run drift tests."""
        
        tests = TestSuite(tests=[
            TestShareOfDriftedColumns(lt=0.3),  # Less than 30% drifted
        ])
        
        # Add per-feature tests
        for feature in self.config.numerical_features + self.config.categorical_features:
            tests.add(TestColumnDrift(
                column_name=feature,
                stattest_threshold=self.config.feature_drift_threshold
            ))
        
        tests.run(
            reference_data=self.reference_data,
            current_data=current_data
        )
        
        return tests.as_dict()
```

---

## 3. Scheduled Monitoring

### 3.1 Airflow DAG

```python
# dags/drift_monitoring.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'mlops',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

def check_model_drift(model_name: str, **context):
    """Check drift for a model."""
    from drift_detection.monitor import DriftMonitor
    from drift_detection.config import get_config
    
    config = get_config(model_name)
    monitor = DriftMonitor(config)
    
    # Get recent inference data
    current_data = get_recent_inference_data(
        model_name=model_name,
        hours=24
    )
    
    # Check drift
    results = monitor.check_drift(current_data)
    
    # Alert if drift detected
    if results['dataset_drift']:
        alert_drift_detected(model_name, results)
    
    # Store results
    store_drift_results(model_name, results)
    
    return results

with DAG(
    'drift_monitoring',
    default_args=default_args,
    schedule_interval='0 */6 * * *',  # Every 6 hours
    catchup=False,
) as dag:
    
    models = ['fraud-detection', 'recommendation', 'churn-prediction']
    
    for model in models:
        PythonOperator(
            task_id=f'check_drift_{model}',
            python_callable=check_model_drift,
            op_kwargs={'model_name': model},
        )
```

---

## 4. Alerting

### 4.1 Prometheus Alerts

```yaml
# prometheus/drift-alerts.yaml
groups:
  - name: drift-alerts
    rules:
      - alert: DataDriftDetected
        expr: mlops_drift_score > 0.2
        for: 1h
        labels:
          severity: warning
        annotations:
          summary: "Data drift detected for {{ $labels.model_name }}"
          description: "Drift score: {{ $value }}"
          
      - alert: FeatureDriftCritical
        expr: mlops_feature_drift_score > 0.15
        for: 30m
        labels:
          severity: high
        annotations:
          summary: "Critical feature drift: {{ $labels.feature_name }}"
          
      - alert: ModelPerformanceDegraded
        expr: |
          (mlops_model_accuracy_baseline - mlops_model_accuracy_live) 
          / mlops_model_accuracy_baseline > 0.05
        for: 2h
        labels:
          severity: high
        annotations:
          summary: "Model {{ $labels.model_name }} accuracy dropped >5%"
```

---

## 5. Dashboard

### 5.1 Grafana Queries

```promql
# Overall drift score
mlops_drift_score{model_name="$model"}

# Feature drift heatmap
mlops_feature_drift_score{model_name="$model"}

# Drift trend over time
avg_over_time(mlops_drift_score{model_name="$model"}[7d])

# Drifted features count
count(mlops_feature_drift_score{model_name="$model"} > 0.1)
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial drift detection setup |
