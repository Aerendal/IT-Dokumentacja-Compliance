---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-081: ML Integration Testing Guide

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-081 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML QA Lead] |

---

## 1. Integration Test Scope

### 1.1 Test Categories

| Category | Components Tested | Frequency |
|----------|------------------|-----------|
| Data Integration | Source → Pipeline → Store | Daily |
| Feature Integration | Feature Store → Model | Per deployment |
| Model Integration | Model → Serving → API | Per deployment |
| End-to-End | Full pipeline | Weekly |

---

## 2. Data Pipeline Integration

### 2.1 Source to Lake Tests

```python
# tests/integration/test_data_ingestion.py
import pytest
from datetime import datetime, timedelta

class TestDataIngestion:
    """Test data ingestion pipeline integration."""
    
    def test_source_to_raw_layer(self, spark_session):
        """Verify data flows from source to raw layer."""
        # Trigger ingestion
        result = trigger_ingestion_job("transactions", 
                                       date=datetime.today() - timedelta(days=1))
        
        assert result.status == "SUCCESS"
        
        # Verify data in raw layer
        raw_data = spark_session.read.parquet(
            "s3://data-lake/raw/transactions/date=2024-01-15/"
        )
        
        assert raw_data.count() > 0
        assert set(raw_data.columns) == {"id", "amount", "timestamp", "user_id"}
    
    def test_raw_to_processed_layer(self, spark_session):
        """Verify transformation from raw to processed."""
        result = trigger_transformation_job("transactions")
        
        assert result.status == "SUCCESS"
        
        processed = spark_session.read.parquet(
            "s3://data-lake/processed/transactions/"
        )
        
        # Verify transformations applied
        assert "amount_normalized" in processed.columns
        assert "hour_of_day" in processed.columns
        
        # Verify no nulls in required columns
        null_count = processed.filter(processed.user_id.isNull()).count()
        assert null_count == 0
```

### 2.2 Feature Store Integration

```python
# tests/integration/test_feature_store.py
import pytest
from feast import FeatureStore

class TestFeatureStoreIntegration:
    """Test feature store integration."""
    
    @pytest.fixture
    def feature_store(self):
        return FeatureStore(repo_path="feature_repo/")
    
    def test_offline_feature_retrieval(self, feature_store):
        """Test historical feature retrieval."""
        entity_df = pd.DataFrame({
            "user_id": ["user_1", "user_2", "user_3"],
            "event_timestamp": [datetime.now()] * 3
        })
        
        features = feature_store.get_historical_features(
            entity_df=entity_df,
            features=[
                "user_features:age",
                "user_features:transaction_count_30d",
                "user_features:avg_transaction_amount"
            ]
        ).to_df()
        
        assert len(features) == 3
        assert "age" in features.columns
        assert features["age"].notna().all()
    
    def test_online_feature_retrieval(self, feature_store):
        """Test real-time feature retrieval."""
        features = feature_store.get_online_features(
            features=[
                "user_features:age",
                "user_features:transaction_count_30d"
            ],
            entity_rows=[{"user_id": "user_1"}]
        ).to_dict()
        
        assert "age" in features
        assert features["age"][0] is not None
    
    def test_feature_freshness(self, feature_store):
        """Verify features are fresh."""
        # Check materialization timestamp
        from feast.infra.registry.base_registry import BaseRegistry
        
        registry = feature_store.registry
        fv = registry.get_feature_view("user_features")
        
        last_materialized = fv.materialization_intervals[-1].end_time
        age_hours = (datetime.utcnow() - last_materialized).total_seconds() / 3600
        
        assert age_hours < 24, f"Features are {age_hours:.1f} hours old"
```

---

## 3. Model Integration Tests

### 3.1 Model Loading Tests

```python
# tests/integration/test_model_loading.py
import pytest
import mlflow

class TestModelIntegration:
    """Test model registry and loading integration."""
    
    def test_load_production_model(self):
        """Test loading model from registry."""
        model = mlflow.pyfunc.load_model(
            "models:/fraud-detection/Production"
        )
        
        assert model is not None
        
        # Test prediction
        sample_input = pd.DataFrame({
            "amount": [100.0],
            "user_age_days": [365],
            "transaction_count_30d": [10]
        })
        
        prediction = model.predict(sample_input)
        
        assert len(prediction) == 1
        assert prediction[0] in [0, 1]
    
    def test_model_signature_matches(self):
        """Verify model signature matches expected schema."""
        client = mlflow.tracking.MlflowClient()
        
        model_version = client.get_latest_versions(
            "fraud-detection", stages=["Production"]
        )[0]
        
        run = client.get_run(model_version.run_id)
        
        # Check input schema
        input_schema = run.data.tags.get("mlflow.log-model.input_schema")
        assert "amount" in input_schema
        assert "user_age_days" in input_schema
```

### 3.2 Serving Integration Tests

```python
# tests/integration/test_model_serving.py
import pytest
import requests

class TestModelServing:
    """Test model serving integration."""
    
    MODEL_ENDPOINT = "https://fraud-model.models.example.com"
    
    def test_health_endpoint(self):
        """Test serving health check."""
        response = requests.get(f"{self.MODEL_ENDPOINT}/v2/health/ready")
        assert response.status_code == 200
    
    def test_inference_endpoint(self):
        """Test inference request."""
        payload = {
            "inputs": [{
                "name": "input",
                "shape": [1, 3],
                "datatype": "FP32",
                "data": [100.0, 365, 10]
            }]
        }
        
        response = requests.post(
            f"{self.MODEL_ENDPOINT}/v2/models/fraud-model/infer",
            json=payload
        )
        
        assert response.status_code == 200
        
        result = response.json()
        assert "outputs" in result
        assert len(result["outputs"]) > 0
    
    def test_batch_inference(self):
        """Test batch inference."""
        batch_size = 10
        payload = {
            "inputs": [{
                "name": "input",
                "shape": [batch_size, 3],
                "datatype": "FP32",
                "data": [[100.0, 365, 10]] * batch_size
            }]
        }
        
        response = requests.post(
            f"{self.MODEL_ENDPOINT}/v2/models/fraud-model/infer",
            json=payload
        )
        
        assert response.status_code == 200
        result = response.json()
        assert len(result["outputs"][0]["data"]) == batch_size
```

---

## 4. End-to-End Tests

### 4.1 Full Pipeline Test

```python
# tests/e2e/test_ml_pipeline.py
import pytest
from datetime import datetime

class TestE2EPipeline:
    """End-to-end ML pipeline tests."""
    
    def test_training_to_serving_pipeline(self):
        """Test complete pipeline from training to serving."""
        
        # 1. Trigger training
        training_run = trigger_training_pipeline(
            experiment_name="e2e-test",
            data_version="v2024.01.15"
        )
        
        assert training_run.status == "COMPLETED"
        
        # 2. Verify model registered
        model_version = get_latest_model_version("fraud-detection-e2e-test")
        assert model_version is not None
        
        # 3. Deploy to staging
        deployment = deploy_model(
            model_name="fraud-detection-e2e-test",
            version=model_version,
            environment="staging"
        )
        
        assert deployment.status == "READY"
        
        # 4. Test inference
        response = test_inference(deployment.endpoint)
        assert response.status_code == 200
        
        # 5. Cleanup
        undeploy_model(deployment.id)
        delete_model_version("fraud-detection-e2e-test", model_version)
```

---

## 5. CI/CD Integration

### 5.1 GitHub Actions

```yaml
# .github/workflows/integration-tests.yml
name: Integration Tests

on:
  push:
    branches: [main, develop]
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM

jobs:
  integration-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements-test.txt
      
      - name: Run integration tests
        env:
          MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_URI }}
          FEAST_REPO_PATH: ${{ secrets.FEAST_PATH }}
        run: |
          pytest tests/integration/ -v --tb=short
      
      - name: Upload results
        uses: actions/upload-artifact@v4
        with:
          name: integration-test-results
          path: reports/
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial integration testing guide |
