---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-023: Pipeline Validation Tests

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-023 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML QA Engineer] |

---

## 1. Test Categories

### 1.1 Pipeline Test Pyramid

```
                    ┌─────────┐
                    │   E2E   │  5%
                    │  Tests  │
                   ┌┴─────────┴┐
                   │Integration│  15%
                   │   Tests   │
                  ┌┴───────────┴┐
                  │  Component  │  30%
                  │    Tests    │
                 ┌┴─────────────┴┐
                 │  Unit Tests   │  50%
                 └───────────────┘
```

---

## 2. Data Pipeline Tests

### 2.1 Data Validation Tests

```python
# tests/pipeline/test_data_validation.py
import pytest
import great_expectations as gx
from src.pipelines.data_validation import validate_training_data

class TestDataValidation:
    """Data validation pipeline tests."""
    
    def test_schema_compliance(self, sample_data):
        """Test data matches expected schema."""
        expected_columns = ['feature_1', 'feature_2', 'label']
        assert list(sample_data.columns) == expected_columns
    
    def test_no_nulls_in_required_fields(self, sample_data):
        """Test required fields have no nulls."""
        required = ['feature_1', 'label']
        for col in required:
            assert sample_data[col].isna().sum() == 0
    
    def test_value_ranges(self, sample_data):
        """Test values within expected ranges."""
        assert sample_data['feature_1'].between(0, 100).all()
        assert sample_data['label'].isin([0, 1]).all()
    
    def test_data_freshness(self, sample_data):
        """Test data is recent enough."""
        from datetime import datetime, timedelta
        max_age = timedelta(days=7)
        latest = sample_data['timestamp'].max()
        assert datetime.now() - latest < max_age
    
    def test_great_expectations_suite(self, sample_data):
        """Run Great Expectations validation suite."""
        context = gx.get_context()
        suite = context.get_expectation_suite("training_data_suite")
        result = context.run_validation_operator(
            "action_list_operator",
            assets_to_validate=[sample_data],
            expectation_suite_name="training_data_suite"
        )
        assert result.success
```

### 2.2 Feature Pipeline Tests

```python
# tests/pipeline/test_feature_pipeline.py
import pytest
from feast import FeatureStore

class TestFeaturePipeline:
    """Feature engineering pipeline tests."""
    
    @pytest.fixture
    def store(self):
        return FeatureStore(repo_path="feature_repo/")
    
    def test_feature_freshness(self, store):
        """Test features are materialized recently."""
        from datetime import datetime, timedelta
        
        fv = store.get_feature_view("user_features")
        # Check materialization timestamp
        assert fv.last_updated_timestamp > datetime.now() - timedelta(hours=1)
    
    def test_feature_schema(self, store):
        """Test feature schema matches expectations."""
        fv = store.get_feature_view("user_features")
        expected_features = {'user_age', 'user_tenure', 'transaction_count'}
        actual_features = {f.name for f in fv.features}
        assert expected_features == actual_features
    
    def test_online_offline_consistency(self, store):
        """Test online and offline features match."""
        entity_rows = [{"user_id": "user_123"}]
        
        # Get online features
        online = store.get_online_features(
            features=["user_features:user_age"],
            entity_rows=entity_rows
        ).to_dict()
        
        # Get offline features
        offline = store.get_historical_features(
            entity_df=pd.DataFrame(entity_rows),
            features=["user_features:user_age"]
        ).to_df()
        
        assert online['user_age'][0] == offline['user_age'].iloc[0]
    
    def test_no_data_leakage(self, store, training_data):
        """Test no future data in training features."""
        for idx, row in training_data.iterrows():
            event_time = row['event_timestamp']
            features = store.get_historical_features(
                entity_df=pd.DataFrame([row]),
                features=["user_features:user_age"]
            ).to_df()
            
            feature_time = features['event_timestamp'].iloc[0]
            assert feature_time <= event_time, "Data leakage detected!"
```

---

## 3. Training Pipeline Tests

### 3.1 Training Workflow Tests

```python
# tests/pipeline/test_training_pipeline.py
import pytest
import mlflow
from src.pipelines.training import TrainingPipeline

class TestTrainingPipeline:
    """Training pipeline tests."""
    
    def test_training_completes(self, sample_data):
        """Test training pipeline runs to completion."""
        pipeline = TrainingPipeline(
            data=sample_data,
            model_type="xgboost",
            experiment_name="test-experiment"
        )
        result = pipeline.run()
        
        assert result.status == "COMPLETED"
        assert result.run_id is not None
    
    def test_metrics_logged(self, sample_data):
        """Test all required metrics are logged."""
        pipeline = TrainingPipeline(data=sample_data)
        result = pipeline.run()
        
        client = mlflow.tracking.MlflowClient()
        run = client.get_run(result.run_id)
        
        required_metrics = ['accuracy', 'precision', 'recall', 'f1', 'auc_roc']
        logged_metrics = run.data.metrics.keys()
        
        for metric in required_metrics:
            assert metric in logged_metrics
    
    def test_model_artifact_saved(self, sample_data):
        """Test model artifact is saved correctly."""
        pipeline = TrainingPipeline(data=sample_data)
        result = pipeline.run()
        
        # Load model
        model_uri = f"runs:/{result.run_id}/model"
        model = mlflow.pyfunc.load_model(model_uri)
        
        assert model is not None
        # Test inference
        prediction = model.predict(sample_data.drop('label', axis=1).head(1))
        assert len(prediction) == 1
    
    def test_reproducibility(self, sample_data):
        """Test training is reproducible with same seed."""
        pipeline1 = TrainingPipeline(data=sample_data, seed=42)
        pipeline2 = TrainingPipeline(data=sample_data, seed=42)
        
        result1 = pipeline1.run()
        result2 = pipeline2.run()
        
        client = mlflow.tracking.MlflowClient()
        metrics1 = client.get_run(result1.run_id).data.metrics
        metrics2 = client.get_run(result2.run_id).data.metrics
        
        assert metrics1['accuracy'] == metrics2['accuracy']
```

---

## 4. Serving Pipeline Tests

### 4.1 Inference Tests

```python
# tests/pipeline/test_serving_pipeline.py
import pytest
import requests
import numpy as np

class TestServingPipeline:
    """Model serving pipeline tests."""
    
    @pytest.fixture
    def model_endpoint(self):
        return "http://fraud-model.models.svc:8080/v2/models/fraud-model/infer"
    
    def test_health_check(self, model_endpoint):
        """Test model endpoint is healthy."""
        health_url = model_endpoint.replace("/infer", "/ready")
        response = requests.get(health_url)
        assert response.status_code == 200
    
    def test_inference_response_format(self, model_endpoint, sample_request):
        """Test inference returns expected format."""
        response = requests.post(model_endpoint, json=sample_request)
        
        assert response.status_code == 200
        data = response.json()
        assert "outputs" in data
        assert len(data["outputs"]) > 0
    
    def test_inference_latency(self, model_endpoint, sample_request):
        """Test inference latency is acceptable."""
        import time
        
        latencies = []
        for _ in range(100):
            start = time.time()
            requests.post(model_endpoint, json=sample_request)
            latencies.append(time.time() - start)
        
        p99_latency = np.percentile(latencies, 99)
        assert p99_latency < 0.1, f"P99 latency {p99_latency}s exceeds 100ms"
    
    def test_batch_inference(self, model_endpoint):
        """Test batch inference works correctly."""
        batch_request = {
            "inputs": [{"data": [...]} for _ in range(100)]
        }
        response = requests.post(model_endpoint, json=batch_request)
        
        assert response.status_code == 200
        assert len(response.json()["outputs"]) == 100
```

---

## 5. End-to-End Pipeline Tests

### 5.1 Full Pipeline Test

```python
# tests/e2e/test_full_pipeline.py
import pytest
from datetime import datetime

class TestE2EPipeline:
    """End-to-end pipeline tests."""
    
    @pytest.mark.e2e
    def test_full_training_to_serving(self):
        """Test complete pipeline from data to serving."""
        
        # Step 1: Data ingestion
        from src.pipelines.data_ingestion import ingest_data
        data = ingest_data(source="test_source", date=datetime.now())
        assert len(data) > 0
        
        # Step 2: Feature engineering
        from src.pipelines.feature_engineering import create_features
        features = create_features(data)
        assert 'feature_1' in features.columns
        
        # Step 3: Training
        from src.pipelines.training import train_model
        model_uri = train_model(features, model_name="e2e-test-model")
        assert model_uri.startswith("models:/")
        
        # Step 4: Validation
        from src.pipelines.validation import validate_model
        passed = validate_model(model_uri, threshold=0.85)
        assert passed
        
        # Step 5: Deployment
        from src.pipelines.deployment import deploy_model
        endpoint = deploy_model(model_uri, environment="test")
        assert endpoint is not None
        
        # Step 6: Inference test
        import requests
        response = requests.post(f"{endpoint}/infer", json={"data": [...]})
        assert response.status_code == 200
        
        # Cleanup
        from src.pipelines.deployment import undeploy_model
        undeploy_model("e2e-test-model", environment="test")
```

---

## 6. Test Execution

### 6.1 CI Configuration

```yaml
# .github/workflows/pipeline-tests.yml
name: Pipeline Tests

on: [push, pull_request]

jobs:
  pipeline-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Run unit tests
        run: pytest tests/pipeline/unit -v
        
      - name: Run integration tests
        run: pytest tests/pipeline/integration -v
        
      - name: Run E2E tests (on main only)
        if: github.ref == 'refs/heads/main'
        run: pytest tests/e2e -v -m e2e
```

### 6.2 Test Commands

```bash
# Run all pipeline tests
pytest tests/pipeline -v

# Run with coverage
pytest tests/pipeline --cov=src/pipelines --cov-report=html

# Run specific category
pytest tests/pipeline -m "data_validation"
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial tests |
