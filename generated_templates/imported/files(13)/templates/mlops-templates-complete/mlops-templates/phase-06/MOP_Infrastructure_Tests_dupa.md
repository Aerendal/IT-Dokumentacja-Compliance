---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-026: MLOps Infrastructure Tests

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-026 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Infrastructure Test Categories

| Category | Purpose | Frequency |
|----------|---------|-----------|
| Smoke Tests | Basic health | Every deploy |
| Integration Tests | Component interaction | Daily |
| Load Tests | Performance validation | Weekly |
| Chaos Tests | Resilience | Monthly |
| DR Tests | Recovery capability | Quarterly |

---

## 2. Smoke Tests

### 2.1 Health Check Suite

```bash
#!/bin/bash
# tests/infra/smoke_tests.sh

set -e
echo "=== MLOps Infrastructure Smoke Tests ==="

# Test 1: Kubernetes cluster
echo "[1/6] Checking Kubernetes cluster..."
kubectl cluster-info > /dev/null && echo " Kubernetes OK"

# Test 2: MLflow
echo "[2/6] Checking MLflow..."
curl -sf https://mlflow.example.com/health > /dev/null && echo " MLflow OK"

# Test 3: Feature Store
echo "[3/6] Checking Feature Store..."
curl -sf https://feast.example.com/health > /dev/null && echo " Feast OK"

# Test 4: Model Serving
echo "[4/6] Checking Model Serving..."
curl -sf https://models.example.com/v2/health/ready > /dev/null && echo " Model Serving OK"

# Test 5: Monitoring
echo "[5/6] Checking Prometheus..."
curl -sf https://prometheus.example.com/-/healthy > /dev/null && echo " Prometheus OK"

# Test 6: Object Storage
echo "[6/6] Checking S3..."
aws s3 ls s3://mlops-artifacts > /dev/null && echo " S3 OK"

echo "=== All smoke tests passed ==="
```

### 2.2 Automated Smoke Test Job

```yaml
# k8s/smoke-test-cronjob.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: mlops-smoke-tests
  namespace: mlops
spec:
  schedule: "*/5 * * * *"  # Every 5 minutes
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: smoke-test
            image: mlops/test-runner:latest
            command: ["/bin/bash", "/tests/smoke_tests.sh"]
          restartPolicy: OnFailure
```

---

## 3. Integration Tests

### 3.1 Component Integration Tests

```python
# tests/infra/test_integration.py
import pytest
import mlflow
from feast import FeatureStore
import requests

class TestMLflowFeastIntegration:
    """Test MLflow and Feast integration."""
    
    def test_mlflow_can_log_feast_features(self):
        """Test MLflow can log feature metadata from Feast."""
        store = FeatureStore(repo_path="feature_repo/")
        
        with mlflow.start_run():
            # Log feature view metadata
            fv = store.get_feature_view("user_features")
            mlflow.log_param("feature_view", fv.name)
            mlflow.log_param("features", [f.name for f in fv.features])
            
            run_id = mlflow.active_run().info.run_id
        
        # Verify logged
        run = mlflow.get_run(run_id)
        assert run.data.params['feature_view'] == 'user_features'


class TestModelServingIntegration:
    """Test model serving integration."""
    
    def test_kserve_loads_mlflow_model(self):
        """Test KServe can load model from MLflow registry."""
        # Register test model
        model_uri = "models:/test-model/Production"
        
        # Deploy via KServe
        response = requests.post(
            "https://kserve-api.example.com/v1/models",
            json={
                "name": "test-model",
                "modelUri": model_uri
            }
        )
        assert response.status_code == 201
        
        # Wait for ready
        import time
        for _ in range(30):
            status = requests.get(
                "https://models.example.com/v2/models/test-model/ready"
            )
            if status.status_code == 200:
                break
            time.sleep(2)
        
        assert status.status_code == 200


class TestMonitoringIntegration:
    """Test monitoring stack integration."""
    
    def test_prometheus_scrapes_mlflow(self):
        """Test Prometheus collects MLflow metrics."""
        response = requests.get(
            "https://prometheus.example.com/api/v1/query",
            params={"query": "mlflow_http_requests_total"}
        )
        data = response.json()
        assert data['status'] == 'success'
        assert len(data['data']['result']) > 0
    
    def test_grafana_dashboard_loads(self):
        """Test Grafana dashboards are accessible."""
        response = requests.get(
            "https://grafana.example.com/api/dashboards/uid/mlops-overview",
            headers={"Authorization": f"Bearer {GRAFANA_TOKEN}"}
        )
        assert response.status_code == 200
```

---

## 4. Load Tests

### 4.1 Model Serving Load Test

```python
# tests/infra/load_test.py
from locust import HttpUser, task, between
import json

class ModelServingUser(HttpUser):
    """Load test for model serving endpoint."""
    
    wait_time = between(0.1, 0.5)
    
    @task(10)
    def predict(self):
        """Send prediction request."""
        payload = {
            "inputs": [{
                "name": "input",
                "shape": [1, 50],
                "datatype": "FP32",
                "data": [0.1] * 50
            }]
        }
        
        with self.client.post(
            "/v2/models/fraud-model/infer",
            json=payload,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Status: {response.status_code}")
    
    @task(1)
    def health_check(self):
        """Check model health."""
        self.client.get("/v2/health/ready")
```

### 4.2 Load Test Execution

```bash
# Run load test
locust -f tests/infra/load_test.py \
    --host=https://models.example.com \
    --users=100 \
    --spawn-rate=10 \
    --run-time=10m \
    --headless \
    --csv=load_test_results

# Check results
cat load_test_results_stats.csv
```

### 4.3 Load Test Thresholds

| Metric | Target | Critical |
|--------|--------|----------|
| P50 Latency | <50ms | <100ms |
| P99 Latency | <100ms | <500ms |
| Throughput | >1000 RPS | >500 RPS |
| Error Rate | <0.1% | <1% |

---

## 5. Chaos Tests

### 5.1 Chaos Experiments

```yaml
# chaos/pod-failure.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata:
  name: model-serving-pod-kill
  namespace: chaos-testing
spec:
  action: pod-kill
  mode: one
  selector:
    namespaces:
      - models
    labelSelectors:
      app: fraud-model
  scheduler:
    cron: "@every 1h"
```

### 5.2 Chaos Test Scenarios

```python
# tests/infra/chaos_tests.py
import pytest
import subprocess
import time
import requests

class TestChaosResilience:
    """Chaos engineering tests."""
    
    def test_pod_failure_recovery(self):
        """Test system recovers from pod failure."""
        # Get initial pod count
        initial_pods = self._get_pod_count("models", "fraud-model")
        
        # Kill one pod
        subprocess.run([
            "kubectl", "delete", "pod", "-l", "app=fraud-model",
            "-n", "models", "--wait=false"
        ])
        
        # Wait for recovery
        time.sleep(60)
        
        # Verify recovered
        final_pods = self._get_pod_count("models", "fraud-model")
        assert final_pods >= initial_pods
        
        # Verify service still working
        response = requests.get("https://models.example.com/v2/health/ready")
        assert response.status_code == 200
    
    def test_network_latency_tolerance(self):
        """Test service handles network latency."""
        # Inject 100ms latency
        subprocess.run([
            "kubectl", "apply", "-f", "chaos/network-delay.yaml"
        ])
        
        time.sleep(30)
        
        # Test service still responds
        start = time.time()
        response = requests.post(
            "https://models.example.com/v2/models/fraud-model/infer",
            json={"inputs": [...]},
            timeout=5
        )
        latency = time.time() - start
        
        assert response.status_code == 200
        assert latency < 5  # Should complete within timeout
        
        # Cleanup
        subprocess.run([
            "kubectl", "delete", "-f", "chaos/network-delay.yaml"
        ])
    
    def _get_pod_count(self, namespace, app):
        result = subprocess.run(
            ["kubectl", "get", "pods", "-n", namespace,
             "-l", f"app={app}", "-o", "json"],
            capture_output=True, text=True
        )
        import json
        pods = json.loads(result.stdout)
        return len(pods['items'])
```

---

## 6. DR Tests

### 6.1 DR Test Checklist

```markdown
## DR Test Checklist

**Test Date:** ___________
**Test Type:** Failover / Failback / Full DR

### Pre-Test
- [ ] Notify stakeholders
- [ ] Backup current state
- [ ] Verify DR environment ready

### Failover Tests
- [ ] Database failover: _____ seconds
- [ ] Model serving failover: _____ seconds
- [ ] Feature store failover: _____ seconds
- [ ] DNS update: _____ seconds

### Validation
- [ ] All services responding
- [ ] Data integrity verified
- [ ] Inference working correctly

### Metrics
- Total RTO achieved: _____ minutes
- RTO target: 30 minutes
- Pass/Fail: _____

### Issues Found
1. _____
2. _____

### Action Items
1. _____
2. _____
```

---

## 7. Test Reporting

### 7.1 Test Results Dashboard

```yaml
# grafana/infra-tests-dashboard.json
{
  "title": "Infrastructure Test Results",
  "panels": [
    {
      "title": "Smoke Test Success Rate",
      "type": "stat",
      "targets": [{
        "expr": "sum(smoke_test_success) / sum(smoke_test_total)"
      }]
    },
    {
      "title": "Load Test P99 Latency",
      "type": "timeseries",
      "targets": [{
        "expr": "histogram_quantile(0.99, load_test_latency_bucket)"
      }]
    }
  ]
}
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial tests |
