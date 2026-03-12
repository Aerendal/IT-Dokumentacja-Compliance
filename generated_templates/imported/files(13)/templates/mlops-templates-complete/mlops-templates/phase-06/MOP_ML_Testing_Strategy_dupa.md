---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-022: ML Testing Strategy

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-022 |
| **Version** | 1.0 |
| **Status** | DRAFT / IN REVIEW / ACTIVE / OBSOLETE |
| **Priority** | HIGH |
| **Owner** | [ML Quality Lead] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Quarterly) |

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-005: ML Lifecycle Requirements | Stage requirements |
| MOP-004: MLOps Requirements | Quality requirements |
| MOP-008: CI/CD Design | Pipeline integration |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-023: Test Automation | Implementation |
| MOP-024: Performance Testing | Performance specs |
| MOP-008: CI/CD | Test gates |

---

## Template Content

---

# ML Testing Strategy

## 1. Testing Philosophy

### 1.1 Testing Pyramid for ML

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ML Testing Pyramid                                │
│                                                                     │
│                         ▲                                           │
│                        /│\                                          │
│                       / │ \    E2E Tests (Manual/Automated)        │
│                      /  │  \   - Full pipeline validation          │
│                     /───┼───\  - Business metrics validation       │
│                    /    │    \                                      │
│                   /     │     \ Integration Tests                   │
│                  /      │      \ - Pipeline tests                   │
│                 /       │       \ - Service integration            │
│                /────────┼────────\                                  │
│               /         │         \ Component Tests                 │
│              /          │          \ - Model validation            │
│             /           │           \ - Feature validation         │
│            /────────────┼────────────\                              │
│           /             │             \ Unit Tests                  │
│          /              │              \ - Data transforms         │
│         /               │               \ - Utility functions      │
│        ─────────────────┴─────────────────                          │
│                                                                     │
│   Coverage: Unit (70%) > Component (20%) > Integration (8%) > E2E (2%)│
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 ML-Specific Testing Categories

| Category | What It Tests | When |
|----------|---------------|------|
| Data Tests | Data quality, schema, drift | Every pipeline run |
| Feature Tests | Feature correctness, leakage | Feature creation |
| Model Tests | Performance, fairness, robustness | Model training |
| Integration Tests | End-to-end pipelines | Before deployment |
| Serving Tests | Latency, throughput, correctness | Deployment |

---

## 2. Data Testing

### 2.1 Data Quality Tests

```python
# data_quality_tests.py
import great_expectations as gx

def test_data_quality(df):
    """Run data quality validations."""
    context = gx.get_context()
    
    expectations = [
        # Completeness
        {"expectation": "expect_column_values_to_not_be_null",
         "column": "user_id"},
        
        # Validity
        {"expectation": "expect_column_values_to_be_between",
         "column": "amount", "min_value": 0, "max_value": 1000000},
        
        # Uniqueness
        {"expectation": "expect_column_values_to_be_unique",
         "column": "transaction_id"},
        
        # Consistency
        {"expectation": "expect_column_pair_values_A_to_be_greater_than_B",
         "column_A": "end_time", "column_B": "start_time"},
    ]
    
    results = context.run_checkpoint(
        checkpoint_name="data_quality",
        batch_request={"data": df}
    )
    
    assert results.success, f"Data quality failed: {results.statistics}"
```

### 2.2 Schema Tests

```python
# schema_tests.py
def test_schema_compliance(df, expected_schema):
    """Verify data matches expected schema."""
    
    # Check columns exist
    missing_cols = set(expected_schema.keys()) - set(df.columns)
    assert not missing_cols, f"Missing columns: {missing_cols}"
    
    # Check data types
    for col, expected_type in expected_schema.items():
        actual_type = df[col].dtype
        assert actual_type == expected_type, \
            f"Column {col}: expected {expected_type}, got {actual_type}"
```

### 2.3 Data Drift Tests

```python
# drift_tests.py
from evidently.metrics import DataDriftMetric
from evidently.report import Report

def test_data_drift(reference_df, current_df, threshold=0.1):
    """Detect statistical drift between datasets."""
    
    report = Report(metrics=[DataDriftMetric()])
    report.run(reference_data=reference_df, current_data=current_df)
    
    result = report.as_dict()
    drift_share = result["metrics"][0]["result"]["drift_share"]
    
    assert drift_share < threshold, \
        f"Data drift detected: {drift_share:.2%} > {threshold:.2%}"
```

---

## 3. Feature Testing

### 3.1 Feature Correctness Tests

```python
# feature_tests.py
def test_feature_computation(feature_pipeline):
    """Test feature computation logic."""
    
    # Prepare test data
    test_input = pd.DataFrame({
        "user_id": ["u1", "u1", "u1"],
        "amount": [100, 200, 300],
        "timestamp": pd.date_range("2024-01-01", periods=3)
    })
    
    # Expected output
    expected = pd.DataFrame({
        "user_id": ["u1"],
        "avg_amount_7d": [200.0],  # (100+200+300)/3
        "count_7d": [3]
    })
    
    # Run feature pipeline
    actual = feature_pipeline.compute(test_input)
    
    pd.testing.assert_frame_equal(actual, expected)
```

### 3.2 Data Leakage Tests

```python
# leakage_tests.py
def test_no_future_data_leakage(feature_df, target_df):
    """Ensure features don't use future information."""
    
    for idx, row in feature_df.iterrows():
        feature_timestamp = row["feature_timestamp"]
        event_timestamp = target_df.loc[idx, "event_timestamp"]
        
        assert feature_timestamp < event_timestamp, \
            f"Data leakage: feature at {feature_timestamp} " \
            f"uses data from after event at {event_timestamp}"
```

### 3.3 Training-Serving Consistency Tests

```python
# consistency_tests.py
def test_training_serving_parity(feature_store, entity_ids, timestamp):
    """Verify training and serving features match."""
    
    # Get training features (offline)
    training_features = feature_store.get_historical_features(
        entity_df=pd.DataFrame({"user_id": entity_ids, "ts": [timestamp]*len(entity_ids)}),
        features=["user_features:amount_avg_7d"]
    ).to_df()
    
    # Get serving features (online)
    serving_features = feature_store.get_online_features(
        entity_rows=[{"user_id": uid} for uid in entity_ids],
        features=["user_features:amount_avg_7d"]
    ).to_df()
    
    # Compare (allowing for timing differences)
    assert np.allclose(
        training_features["amount_avg_7d"],
        serving_features["amount_avg_7d"],
        rtol=0.01
    ), "Training-serving mismatch detected"
```

---

## 4. Model Testing

### 4.1 Model Performance Tests

```python
# model_performance_tests.py
def test_model_performance(model, test_data, baseline_metrics):
    """Validate model meets performance requirements."""
    
    X_test, y_test = test_data
    predictions = model.predict(X_test)
    
    # Calculate metrics
    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions),
        "recall": recall_score(y_test, predictions),
        "f1": f1_score(y_test, predictions),
        "auc": roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    }
    
    # Compare against baseline
    for metric, value in metrics.items():
        baseline = baseline_metrics[metric]
        assert value >= baseline * 0.95, \
            f"{metric}: {value:.4f} < baseline {baseline:.4f}"
```

### 4.2 Fairness Tests

```python
# fairness_tests.py
from fairlearn.metrics import MetricFrame, selection_rate

def test_model_fairness(model, test_data, sensitive_feature):
    """Test model for bias across protected groups."""
    
    X_test, y_test, sensitive = test_data
    predictions = model.predict(X_test)
    
    # Calculate metrics by group
    metric_frame = MetricFrame(
        metrics={
            "accuracy": accuracy_score,
            "selection_rate": selection_rate
        },
        y_true=y_test,
        y_pred=predictions,
        sensitive_features=sensitive
    )
    
    # Check demographic parity
    selection_rates = metric_frame.by_group["selection_rate"]
    disparity = selection_rates.max() - selection_rates.min()
    
    assert disparity < 0.1, \
        f"Fairness violation: selection rate disparity = {disparity:.2%}"
```

### 4.3 Robustness Tests

```python
# robustness_tests.py
def test_model_robustness(model, test_data, noise_level=0.05):
    """Test model stability under input perturbation."""
    
    X_test, y_test = test_data
    base_predictions = model.predict(X_test)
    
    # Add noise
    X_noisy = X_test + np.random.normal(0, noise_level, X_test.shape)
    noisy_predictions = model.predict(X_noisy)
    
    # Check prediction stability
    changed = (base_predictions != noisy_predictions).sum()
    change_rate = changed / len(base_predictions)
    
    assert change_rate < 0.1, \
        f"Model unstable: {change_rate:.2%} predictions changed with noise"
```

---

## 5. Integration Testing

### 5.1 Pipeline Integration Tests

```python
# pipeline_integration_tests.py
def test_training_pipeline_integration():
    """Test complete training pipeline."""
    
    # Run pipeline with test data
    result = training_pipeline.run(
        data_source="test_data",
        experiment_name="integration_test",
        model_params={"n_estimators": 10}  # Small for speed
    )
    
    # Verify outputs
    assert result.status == "SUCCESS"
    assert result.model_uri is not None
    assert result.metrics["accuracy"] > 0.5
    
    # Verify artifacts
    model = mlflow.sklearn.load_model(result.model_uri)
    assert model is not None
```

### 5.2 Serving Integration Tests

```python
# serving_integration_tests.py
def test_serving_integration(model_endpoint, test_payload):
    """Test model serving end-to-end."""
    
    # Make prediction request
    response = requests.post(
        f"{model_endpoint}/v2/models/fraud_model/infer",
        json=test_payload
    )
    
    # Verify response
    assert response.status_code == 200
    result = response.json()
    assert "outputs" in result
    assert len(result["outputs"]) > 0
```

---

## 6. Test Automation

### 6.1 CI Pipeline Tests

```yaml
# .github/workflows/ml-tests.yml
name: ML Tests
on: [push, pull_request]

jobs:
  data-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run data quality tests
        run: pytest tests/data/ -v --junitxml=data-results.xml

  feature-tests:
    runs-on: ubuntu-latest
    steps:
      - name: Run feature tests
        run: pytest tests/features/ -v --junitxml=feature-results.xml

  model-tests:
    runs-on: ubuntu-latest
    needs: [data-tests, feature-tests]
    steps:
      - name: Run model tests
        run: pytest tests/models/ -v --junitxml=model-results.xml
```

### 6.2 Test Configuration

```python
# conftest.py
import pytest

@pytest.fixture
def model_fixture():
    """Load model for testing."""
    return mlflow.sklearn.load_model("models:/fraud_model/Production")

@pytest.fixture
def test_data():
    """Load test dataset."""
    return pd.read_parquet("tests/data/test_data.parquet")

@pytest.fixture
def feature_store():
    """Initialize feature store for testing."""
    return FeatureStore(repo_path="tests/feast_repo")
```

---

## 7. Test Metrics & Reporting

### 7.1 Required Metrics

| Test Category | Metric | Threshold |
|---------------|--------|-----------|
| Unit Tests | Coverage | >80% |
| Data Tests | Pass Rate | 100% |
| Model Tests | Performance vs Baseline | >95% |
| Integration Tests | Success Rate | 100% |
| E2E Tests | Success Rate | 100% |

### 7.2 Test Dashboard

Track and visualize:
- Test pass/fail trends
- Test execution time
- Coverage metrics
- Flaky test detection

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial strategy |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| ML Quality Lead | | | |
| ML Platform Lead | | | |
