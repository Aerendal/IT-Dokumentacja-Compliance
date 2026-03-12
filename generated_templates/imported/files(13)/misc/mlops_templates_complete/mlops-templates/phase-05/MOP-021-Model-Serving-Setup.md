---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-021: Model Serving Setup Guide

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-021 |
| **Version** | 1.0 |
| **Status** | DRAFT / IN REVIEW / ACTIVE / OBSOLETE |
| **Priority** | CRITICAL |
| **Owner** | [ML Platform Engineer] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Quarterly) |

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-012: Model Serving Design | Architecture |
| MOP-007: Architecture | Infrastructure |
| MOP-009: Model Registry | Model artifacts |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-029: Deployment Procedures | Deployment steps |
| MOP-038: Monitoring Setup | Serving metrics |

---

## Template Content

---

# Model Serving Infrastructure Setup (Triton + KServe)

## 1. Prerequisites

| Component | Specification | Status |
|-----------|---------------|--------|
| Kubernetes cluster | v1.25+ |  |
| GPU nodes (optional) | NVIDIA drivers |  |
| Istio | v1.17+ |  |
| KNative | v1.10+ |  |
| Model Registry | MLflow accessible |  |

---

## 2. KServe Installation

### 2.1 Install KServe

```bash
# Install KServe
kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.12.0/kserve.yaml

# Install KServe runtime
kubectl apply -f https://github.com/kserve/kserve/releases/download/v0.12.0/kserve-runtimes.yaml

# Verify installation
kubectl get pods -n kserve
```

### 2.2 Configure Inference Service Defaults

```yaml
# kserve-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: inferenceservice-config
  namespace: kserve
data:
  deploy: |-
    {
      "defaultDeploymentMode": "Serverless"
    }
  predictors: |-
    {
      "triton": {
        "image": "nvcr.io/nvidia/tritonserver",
        "defaultImageVersion": "23.10-py3",
        "supportedModelFormats": [
          {"name": "tensorrt", "version": "8"},
          {"name": "tensorflow", "version": "2"},
          {"name": "onnx", "version": "1"},
          {"name": "pytorch", "version": "2"}
        ]
      }
    }
```

---

## 3. Triton Model Repository

### 3.1 Model Repository Structure

```
s3://model-repository/
├── fraud_model/
│   ├── config.pbtxt
│   └── 1/
│       └── model.onnx
├── recommendation_model/
│   ├── config.pbtxt
│   └── 1/
│       └── model.pt
```

### 3.2 Model Configuration

```protobuf
# config.pbtxt
name: "fraud_model"
platform: "onnxruntime_onnx"
max_batch_size: 32
input [
  {
    name: "input"
    data_type: TYPE_FP32
    dims: [ -1, 50 ]
  }
]
output [
  {
    name: "output"
    data_type: TYPE_FP32
    dims: [ -1, 2 ]
  }
]
instance_group [
  {
    count: 2
    kind: KIND_CPU
  }
]
dynamic_batching {
  preferred_batch_size: [ 8, 16, 32 ]
  max_queue_delay_microseconds: 5000
}
```

---

## 4. Deploy InferenceService

### 4.1 Basic Deployment

```yaml
# fraud-model-inference.yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: fraud-model
  namespace: models
  annotations:
    serving.kserve.io/deploymentMode: Serverless
spec:
  predictor:
    minReplicas: 2
    maxReplicas: 10
    scaleTarget: 10  # concurrent requests per pod
    scaleMetric: concurrency
    triton:
      storageUri: "s3://model-repository/fraud_model"
      runtimeVersion: "23.10-py3"
      resources:
        limits:
          cpu: "2"
          memory: "4Gi"
        requests:
          cpu: "1"
          memory: "2Gi"
```

### 4.2 GPU Deployment

```yaml
# gpu-model-inference.yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: nlp-model
  namespace: models
spec:
  predictor:
    minReplicas: 1
    maxReplicas: 5
    triton:
      storageUri: "s3://model-repository/nlp_model"
      resources:
        limits:
          cpu: "4"
          memory: "16Gi"
          nvidia.com/gpu: "1"
        requests:
          cpu: "2"
          memory: "8Gi"
          nvidia.com/gpu: "1"
      nodeSelector:
        accelerator: nvidia-tesla-t4
```

---

## 5. Canary Deployment

```yaml
# canary-deployment.yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: fraud-model
  namespace: models
spec:
  predictor:
    canaryTrafficPercent: 10
    triton:
      storageUri: "s3://model-repository/fraud_model/v2"
      resources:
        limits:
          cpu: "2"
          memory: "4Gi"
  transformer:
    containers:
    - name: transformer
      image: custom-transformer:latest
```

---

## 6. Verification

### 6.1 Check Deployment

```bash
# Check InferenceService status
kubectl get inferenceservices -n models

# Get service URL
kubectl get inferenceservice fraud-model -n models -o jsonpath='{.status.url}'

# Check pods
kubectl get pods -n models -l serving.kserve.io/inferenceservice=fraud-model
```

### 6.2 Test Inference

```python
# test_inference.py
import requests
import json

url = "https://fraud-model.models.example.com/v2/models/fraud_model/infer"
headers = {"Content-Type": "application/json"}

payload = {
    "inputs": [{
        "name": "input",
        "shape": [1, 50],
        "datatype": "FP32",
        "data": [[0.1] * 50]
    }]
}

response = requests.post(url, headers=headers, json=payload)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")
assert response.status_code == 200
print(" Inference test passed")
```

---

## 7. Monitoring

### 7.1 Prometheus Metrics

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: kserve-pods
  namespace: models
spec:
  selector:
    matchLabels:
      serving.kserve.io/inferenceservice: fraud-model
  podMetricsEndpoints:
  - port: http
    path: /metrics
```

### 7.2 Key Metrics

| Metric | Description | Alert |
|--------|-------------|-------|
| `nv_inference_request_duration_us` | Inference latency | P99 >100ms |
| `nv_inference_request_success` | Success count | Error rate >1% |
| `nv_inference_queue_duration_us` | Queue wait time | >10ms |
| `kserve_request_count` | Request count | - |

---

## 8. Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Pod stuck Pending | No GPU nodes | Check node selector |
| Model load fails | S3 access denied | Verify IAM role |
| High latency | Cold start | Increase minReplicas |
| OOM errors | Model too large | Increase memory limits |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial setup guide |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| ML Platform Engineer | | | |
| SRE Lead | | | |
