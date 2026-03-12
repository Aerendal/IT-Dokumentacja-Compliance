---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-012: Model Serving Infrastructure Design

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-012 |
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
-  Models ready for production deployment
-  Latency and throughput requirements defined

### When This Document Becomes Invalid
-  Serving platform migration
-  New deployment paradigms (e.g., edge serving)
-  Fundamental architecture change

### Validity Conditions
-  Supports all model frameworks in use
-  Meets latency SLAs
-  Handles expected throughput
-  Integration with monitoring established

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-007: Architecture | Serving placement |
| MOP-006: Scalability Requirements | Performance needs |
| MOP-009: Model Registry | Model deployment |
| MOP-011: Feature Store | Online feature serving |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-021: Model Serving Setup | Implementation specs |
| MOP-029: Deployment Procedures | Deployment workflows |
| MOP-037: Pipeline Metrics | Performance baselines |
| MOP-038: Model Performance Monitoring | Monitoring requirements |

### Bidirectional Dependencies
| Document | Relationship |
|----------|--------------|
| MOP-008: CI/CD Pipeline | Deployment triggers |
| MOP-011: Feature Store | Feature serving |
| MOP-025: Security Architecture | Authentication/Authorization |

---

## Section Dependencies (Internal)

```
┌────────────────────────────────────────────────────────────────┐
│              1. Serving Overview                                │
└────────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
│ 2. Architecture  │ │ 3. Serving   │ │ 4. Deployment    │
│    Patterns      │ │    Frameworks│ │    Strategies    │
└──────────────────┘ └──────────────┘ └──────────────────┘
        │                   │                  │
        └───────────────────┼──────────────────┘
                            ▼
┌────────────────────────────────────────────────────────────────┐
│              5. API Design                                      │
└────────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
┌──────────────────┐ ┌──────────────┐ ┌──────────────────┐
│ 6. Scaling &     │ │ 7. Security  │ │ 8. Monitoring    │
│    Performance   │ │              │ │    & Observability│
└──────────────────┘ └──────────────┘ └──────────────────┘
```

---

## Template Content

---

# Model Serving Infrastructure Design

**[Organization Name]**

**Version:** [X.Y]  
**Date:** [YYYY-MM-DD]

---

## 1. Serving Overview

> **Section Dependencies:**
> - Depends on: MOP-007 Architecture
> - Feeds into: All other sections
> - Update trigger: Platform strategy changes

### 1.1 Purpose

Model Serving Infrastructure provides:
- **Low-Latency Inference**: Sub-100ms predictions for real-time use cases
- **High Throughput**: Handle thousands of requests per second
- **Multi-Model Serving**: Serve multiple models efficiently
- **Framework Agnostic**: Support sklearn, PyTorch, TensorFlow, XGBoost, etc.
- **Production Reliability**: High availability, monitoring, rollback capabilities

### 1.2 Serving Patterns

| Pattern | Latency | Use Case | Example |
|---------|---------|----------|---------|
| **Real-time** | <100ms | Online scoring | Fraud detection |
| **Near Real-time** | 100ms-1s | Recommendations | Product ranking |
| **Batch** | Minutes-hours | Bulk scoring | Risk assessment |
| **Streaming** | <10s | Event processing | Anomaly detection |
| **Edge** | <10ms | On-device | Mobile predictions |

### 1.3 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Model Serving Architecture                        │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                      API Gateway                               │ │
│  │  (Kong / AWS ALB / Istio Ingress)                             │ │
│  │  - Rate limiting                                               │ │
│  │  - Authentication                                              │ │
│  │  - Request routing                                             │ │
│  └────────────────────────────┬──────────────────────────────────┘ │
│                               │                                     │
│  ┌────────────────────────────┼──────────────────────────────────┐ │
│  │                     Service Mesh (Istio)                       │ │
│  │                            │                                   │ │
│  │  ┌─────────────────────────┼─────────────────────────────────┐│ │
│  │  │              Model Serving Layer                           ││ │
│  │  │                         │                                  ││ │
│  │  │  ┌──────────────┐ ┌─────┴─────┐ ┌──────────────┐         ││ │
│  │  │  │   Triton     │ │ TorchServe│ │   TFServing  │         ││ │
│  │  │  │   Server     │ │           │ │              │         ││ │
│  │  │  └──────────────┘ └───────────┘ └──────────────┘         ││ │
│  │  └────────────────────────────────────────────────────────────┘│ │
│  │                            │                                   │ │
│  │  ┌────────────────────────┬┴───────────────────────────────┐  │ │
│  │  │              Support Services                            │  │ │
│  │  │  ┌──────────────┐ ┌───────────┐ ┌──────────────┐       │  │ │
│  │  │  │ Feature Store│ │  Model    │ │  Config      │       │  │ │
│  │  │  │   Client     │ │  Registry │ │  Service     │       │  │ │
│  │  │  └──────────────┘ └───────────┘ └──────────────┘       │  │ │
│  │  └────────────────────────────────────────────────────────┘  │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                               │                                     │
│  ┌────────────────────────────┼──────────────────────────────────┐ │
│  │                      Observability                             │ │
│  │  ┌──────────────┐ ┌───────┴───────┐ ┌──────────────┐         │ │
│  │  │  Prometheus  │ │     Jaeger    │ │    Grafana   │         │ │
│  │  │  (Metrics)   │ │   (Tracing)   │ │ (Dashboards) │         │ │
│  │  └──────────────┘ └───────────────┘ └──────────────┘         │ │
│  └───────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.4 Technology Selection

| Component | Options | Selected | Rationale |
|-----------|---------|----------|-----------|
| Serving Framework | Triton / TorchServe / TFServing / Seldon | [Selection] | [Rationale] |
| Orchestration | Kubernetes | Kubernetes | Industry standard |
| Service Mesh | Istio / Linkerd | [Selection] | Traffic management |
| API Gateway | Kong / AWS ALB / Traefik | [Selection] | Existing infra |
| GPU Support | NVIDIA GPU Operator | Yes/No | [Based on models] |

---

## 2. Architecture Patterns

> **Section Dependencies:**
> - Depends on: Section 1 (Overview)
> - Feeds into: Section 3 (Frameworks), Section 4 (Deployment)
> - Update trigger: New serving requirements

### 2.1 Single Model Serving

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Single Model Pattern                              │
│                                                                     │
│  Client ──► API Gateway ──► Model Server ──► Response               │
│                                  │                                  │
│                                  ▼                                  │
│                             ┌─────────┐                            │
│                             │  Model  │                            │
│                             │   v1    │                            │
│                             └─────────┘                            │
│                                                                     │
│  Use case: Single model, simple deployment                          │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Multi-Model Serving

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Multi-Model Pattern                               │
│                                                                     │
│  Client ──► API Gateway ──► Router ──┬──► Model A                   │
│                                      ├──► Model B                   │
│                                      └──► Model C                   │
│                                                                     │
│  Routing logic:                                                     │
│  - /v1/models/fraud-detection → Model A                            │
│  - /v1/models/recommendations → Model B                            │
│  - /v1/models/churn-prediction → Model C                           │
│                                                                     │
│  Use case: Multiple models, shared infrastructure                   │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.3 Model Ensemble

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Ensemble Pattern                                  │
│                                                                     │
│  Client ──► API Gateway ──► Ensemble Server                         │
│                                  │                                  │
│                    ┌─────────────┼─────────────┐                   │
│                    ▼             ▼             ▼                   │
│               ┌─────────┐  ┌─────────┐  ┌─────────┐               │
│               │ Model 1 │  │ Model 2 │  │ Model 3 │               │
│               │(XGBoost)│  │  (NN)   │  │  (RF)   │               │
│               └────┬────┘  └────┬────┘  └────┬────┘               │
│                    │            │            │                     │
│                    └────────────┼────────────┘                     │
│                                 ▼                                   │
│                          ┌──────────┐                              │
│                          │ Combiner │                              │
│                          │(Average) │                              │
│                          └──────────┘                              │
│                                                                     │
│  Use case: Improved accuracy via model combination                  │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.4 Model Pipeline (Chained)

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Pipeline Pattern                                  │
│                                                                     │
│  Input ──► Preprocessor ──► Model ──► Postprocessor ──► Output      │
│                                                                     │
│  ┌────────────────┐    ┌────────────┐    ┌────────────────┐       │
│  │  Text Cleaning │ ─► │ BERT Model │ ─► │ Label Mapping  │       │
│  │  Tokenization  │    │            │    │ Threshold      │       │
│  └────────────────┘    └────────────┘    └────────────────┘       │
│                                                                     │
│  Use case: Complex preprocessing/postprocessing needs               │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.5 A/B Testing Pattern

```
┌─────────────────────────────────────────────────────────────────────┐
│                    A/B Testing Pattern                               │
│                                                                     │
│  Client ──► API Gateway ──► Traffic Splitter                        │
│                                  │                                  │
│                    ┌─────────────┴─────────────┐                   │
│                    │                           │                    │
│                    ▼ (90%)                     ▼ (10%)              │
│               ┌─────────┐               ┌─────────┐                │
│               │Champion │               │Challenger│               │
│               │ Model   │               │  Model   │               │
│               └─────────┘               └─────────┘                │
│                                                                     │
│  Traffic split: weight-based or header-based routing                │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Serving Frameworks

> **Section Dependencies:**
> - Depends on: Section 2 (Patterns)
> - Feeds into: Section 5 (API), Section 6 (Scaling)
> - Update trigger: New frameworks needed

### 3.1 Framework Comparison

| Feature | Triton | TorchServe | TFServing | Seldon | BentoML |
|---------|--------|------------|-----------|--------|---------|
| Multi-framework |  | PyTorch | TensorFlow |  |  |
| Dynamic batching |  |  |  | Via config |  |
| Model ensemble |  | Limited |  |  |  |
| GPU support |  |  |  |  |  |
| gRPC |  |  |  |  |  |
| K8s native | Via Helm | KServe | Via Helm |  |  |
| Model versioning |  |  |  |  |  |

### 3.2 NVIDIA Triton Inference Server

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Triton Architecture                               │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                    HTTP/gRPC Interface                         │ │
│  └────────────────────────────┬──────────────────────────────────┘ │
│                               │                                     │
│  ┌────────────────────────────┼──────────────────────────────────┐ │
│  │                    Inference Engine                            │ │
│  │                            │                                   │ │
│  │  ┌─────────────────────────┼─────────────────────────────────┐│ │
│  │  │              Model Repository                              ││ │
│  │  │  model_repo/                                               ││ │
│  │  │  ├── fraud_model/                                         ││ │
│  │  │  │   ├── config.pbtxt                                     ││ │
│  │  │  │   └── 1/                                               ││ │
│  │  │  │       └── model.onnx                                   ││ │
│  │  │  └── recommendations/                                      ││ │
│  │  │      ├── config.pbtxt                                     ││ │
│  │  │      └── 1/                                               ││ │
│  │  │          └── model.savedmodel/                            ││ │
│  │  └────────────────────────────────────────────────────────────┘│ │
│  │                            │                                   │ │
│  │  ┌────────────────────────┬┴───────────────────────────────┐  │ │
│  │  │              Backends                                    │  │ │
│  │  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐           │  │ │
│  │  │  │ TensorRT│ │ ONNX   │ │PyTorch │ │TensorFlow│         │  │ │
│  │  │  └────────┘ └────────┘ └────────┘ └────────┘           │  │ │
│  │  └────────────────────────────────────────────────────────┘  │ │
│  └───────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

#### Triton Model Configuration

```protobuf
# config.pbtxt
name: "fraud_detection"
platform: "onnxruntime_onnx"
max_batch_size: 64

input [
  {
    name: "features"
    data_type: TYPE_FP32
    dims: [ 128 ]
  }
]

output [
  {
    name: "prediction"
    data_type: TYPE_FP32
    dims: [ 1 ]
  },
  {
    name: "probability"
    data_type: TYPE_FP32
    dims: [ 2 ]
  }
]

instance_group [
  {
    count: 2
    kind: KIND_GPU
    gpus: [ 0 ]
  }
]

dynamic_batching {
  preferred_batch_size: [ 16, 32, 64 ]
  max_queue_delay_microseconds: 100
}

version_policy {
  latest { num_versions: 2 }
}
```

### 3.3 TorchServe

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TorchServe Architecture                           │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                    Frontend (Java)                             │ │
│  │  - Model management API                                        │ │
│  │  - Inference API                                               │ │
│  │  - Request queuing                                             │ │
│  └────────────────────────────┬──────────────────────────────────┘ │
│                               │                                     │
│  ┌────────────────────────────┼──────────────────────────────────┐ │
│  │                    Backend (Python)                            │ │
│  │                            │                                   │ │
│  │  ┌────────────────────────┬┴───────────────────────────────┐  │ │
│  │  │              Model Workers                               │  │ │
│  │  │  ┌────────┐ ┌────────┐ ┌────────┐                       │  │ │
│  │  │  │Worker 1│ │Worker 2│ │Worker N│                       │  │ │
│  │  │  └────────┘ └────────┘ └────────┘                       │  │ │
│  │  └────────────────────────────────────────────────────────┘  │ │
│  └───────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

#### TorchServe Handler

```python
# handler.py
import torch
from ts.torch_handler.base_handler import BaseHandler

class FraudDetectionHandler(BaseHandler):
    def __init__(self):
        super().__init__()
        self.initialized = False
    
    def initialize(self, context):
        self.manifest = context.manifest
        properties = context.system_properties
        model_dir = properties.get("model_dir")
        
        # Load model
        serialized_file = self.manifest['model']['serializedFile']
        model_path = os.path.join(model_dir, serialized_file)
        self.model = torch.jit.load(model_path)
        self.model.eval()
        
        self.initialized = True
    
    def preprocess(self, data):
        # Transform input data
        inputs = []
        for row in data:
            features = row.get("data") or row.get("body")
            if isinstance(features, dict):
                features = features.get("features")
            inputs.append(torch.tensor(features, dtype=torch.float32))
        return torch.stack(inputs)
    
    def inference(self, data):
        with torch.no_grad():
            outputs = self.model(data)
        return outputs
    
    def postprocess(self, inference_output):
        predictions = torch.sigmoid(inference_output).tolist()
        return [{"fraud_probability": p[0]} for p in predictions]
```

---

## 4. Deployment Strategies

> **Section Dependencies:**
> - Depends on: Section 2 (Patterns), Section 3 (Frameworks)
> - Feeds into: MOP-008 (CI/CD), MOP-029 (Deployment Procedures)
> - Update trigger: Deployment policy changes

### 4.1 Strategy Comparison

| Strategy | Risk | Rollback Speed | Resource Cost | Use Case |
|----------|------|----------------|---------------|----------|
| Rolling | Low-Medium | Minutes | 1x | Standard updates |
| Blue/Green | Low | Instant | 2x | Critical models |
| Canary | Very Low | Instant | 1.1x-1.5x | High-traffic |
| Shadow | None | N/A | 2x | Validation only |

### 4.2 Rolling Deployment

```yaml
# Kubernetes rolling deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fraud-detection-model
spec:
  replicas: 5
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # 1 extra pod during update
      maxUnavailable: 0  # No downtime
  selector:
    matchLabels:
      app: fraud-detection
  template:
    metadata:
      labels:
        app: fraud-detection
        version: v2.1.0
    spec:
      containers:
      - name: model-server
        image: model-server:v2.1.0
        ports:
        - containerPort: 8080
        readinessProbe:
          httpGet:
            path: /v2/health/ready
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
        livenessProbe:
          httpGet:
            path: /v2/health/live
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
```

### 4.3 Blue/Green Deployment

```yaml
# Blue deployment (current production)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fraud-detection-blue
  labels:
    app: fraud-detection
    version: blue
spec:
  replicas: 5
  template:
    metadata:
      labels:
        app: fraud-detection
        version: blue
---
# Green deployment (new version)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fraud-detection-green
  labels:
    app: fraud-detection
    version: green
spec:
  replicas: 5
  template:
    metadata:
      labels:
        app: fraud-detection
        version: green
---
# Service pointing to active version
apiVersion: v1
kind: Service
metadata:
  name: fraud-detection
spec:
  selector:
    app: fraud-detection
    version: blue  # Switch to 'green' for cutover
  ports:
  - port: 80
    targetPort: 8080
```

### 4.4 Canary Deployment (Istio)

```yaml
# Istio VirtualService for canary
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: fraud-detection
spec:
  hosts:
  - fraud-detection
  http:
  - match:
    - headers:
        x-canary:
          exact: "true"
    route:
    - destination:
        host: fraud-detection
        subset: canary
  - route:
    - destination:
        host: fraud-detection
        subset: stable
      weight: 90
    - destination:
        host: fraud-detection
        subset: canary
      weight: 10
---
# DestinationRule
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: fraud-detection
spec:
  host: fraud-detection
  subsets:
  - name: stable
    labels:
      version: v1.0.0
  - name: canary
    labels:
      version: v1.1.0
```

### 4.5 Canary Progression

```yaml
# Canary progression stages
canary_stages:
  - stage: 1
    weight: 5
    duration: 10m
    success_criteria:
      error_rate: < 0.5%
      latency_p99: < 100ms
      
  - stage: 2
    weight: 25
    duration: 30m
    success_criteria:
      error_rate: < 0.5%
      latency_p99: < 100ms
      model_accuracy: >= baseline - 0.01
      
  - stage: 3
    weight: 50
    duration: 1h
    success_criteria:
      error_rate: < 0.5%
      latency_p99: < 100ms
      model_accuracy: >= baseline - 0.01
      
  - stage: 4
    weight: 100
    duration: final
    success_criteria:
      error_rate: < 0.5%
      latency_p99: < 100ms

rollback_trigger:
  - error_rate: > 1%
  - latency_p99: > 200ms
  - model_accuracy: < baseline - 0.05
```

---

## 5. API Design

> **Section Dependencies:**
> - Depends on: Section 3 (Frameworks)
> - Feeds into: Client integration
> - Update trigger: API version changes

### 5.1 REST API Specification

```yaml
openapi: 3.0.0
info:
  title: Model Serving API
  version: 2.0.0
  description: ML Model Inference API

paths:
  /v2/models/{model_name}/infer:
    post:
      summary: Run inference
      parameters:
        - name: model_name
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/InferenceRequest'
      responses:
        '200':
          description: Successful inference
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InferenceResponse'
        '400':
          description: Invalid input
        '503':
          description: Model not ready

  /v2/models/{model_name}:
    get:
      summary: Get model metadata
      responses:
        '200':
          description: Model information
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ModelMetadata'

  /v2/health/ready:
    get:
      summary: Readiness check
      responses:
        '200':
          description: Server is ready

  /v2/health/live:
    get:
      summary: Liveness check
      responses:
        '200':
          description: Server is alive

components:
  schemas:
    InferenceRequest:
      type: object
      required:
        - inputs
      properties:
        id:
          type: string
          description: Request ID for tracing
        inputs:
          type: array
          items:
            $ref: '#/components/schemas/InputTensor'
        parameters:
          type: object
          description: Optional inference parameters
          
    InferenceResponse:
      type: object
      properties:
        id:
          type: string
        model_name:
          type: string
        model_version:
          type: string
        outputs:
          type: array
          items:
            $ref: '#/components/schemas/OutputTensor'
            
    InputTensor:
      type: object
      required:
        - name
        - shape
        - datatype
        - data
      properties:
        name:
          type: string
        shape:
          type: array
          items:
            type: integer
        datatype:
          type: string
          enum: [BOOL, UINT8, INT32, INT64, FP32, FP64, BYTES]
        data:
          type: array
```

### 5.2 gRPC API

```protobuf
// inference.proto
syntax = "proto3";
package inference;

service GRPCInferenceService {
  rpc ModelInfer(ModelInferRequest) returns (ModelInferResponse);
  rpc ModelReady(ModelReadyRequest) returns (ModelReadyResponse);
  rpc ModelMetadata(ModelMetadataRequest) returns (ModelMetadataResponse);
  rpc ServerLive(ServerLiveRequest) returns (ServerLiveResponse);
  rpc ServerReady(ServerReadyRequest) returns (ServerReadyResponse);
}

message ModelInferRequest {
  string model_name = 1;
  string model_version = 2;
  string id = 3;
  repeated InferInputTensor inputs = 4;
  repeated InferRequestedOutputTensor outputs = 5;
  map<string, InferParameter> parameters = 6;
}

message ModelInferResponse {
  string model_name = 1;
  string model_version = 2;
  string id = 3;
  repeated InferOutputTensor outputs = 4;
}

message InferInputTensor {
  string name = 1;
  string datatype = 2;
  repeated int64 shape = 3;
  InferTensorContents contents = 4;
}

message InferTensorContents {
  repeated bool bool_contents = 1;
  repeated int32 int_contents = 2;
  repeated int64 int64_contents = 3;
  repeated float fp32_contents = 4;
  repeated double fp64_contents = 5;
  repeated bytes bytes_contents = 6;
}
```

### 5.3 Request/Response Examples

#### REST Request
```http
POST /v2/models/fraud-detection/infer HTTP/1.1
Host: inference.example.com
Content-Type: application/json
X-Request-ID: req-12345

{
  "id": "req-12345",
  "inputs": [
    {
      "name": "features",
      "shape": [1, 128],
      "datatype": "FP32",
      "data": [0.1, 0.2, ..., 0.9]
    }
  ],
  "parameters": {
    "explain": true
  }
}
```

#### REST Response
```json
{
  "id": "req-12345",
  "model_name": "fraud-detection",
  "model_version": "3",
  "outputs": [
    {
      "name": "prediction",
      "shape": [1],
      "datatype": "INT32",
      "data": [1]
    },
    {
      "name": "probability",
      "shape": [1, 2],
      "datatype": "FP32",
      "data": [0.15, 0.85]
    }
  ]
}
```

---

## 6. Scaling & Performance

> **Section Dependencies:**
> - Depends on: Section 3 (Frameworks), MOP-006 (Scalability)
> - Feeds into: Section 8 (Monitoring)
> - Update trigger: Performance requirements change

### 6.1 Performance Requirements

| Metric | Requirement | Target |
|--------|-------------|--------|
| Latency P50 | < 20ms | 10ms |
| Latency P99 | < 100ms | 50ms |
| Throughput | > 10K RPS | 15K RPS |
| Availability | 99.9% | 99.95% |
| Error rate | < 0.1% | 0.01% |

### 6.2 Horizontal Pod Autoscaler

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: fraud-detection-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: fraud-detection-model
  minReplicas: 3
  maxReplicas: 50
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  - type: Pods
    pods:
      metric:
        name: inference_requests_per_second
      target:
        type: AverageValue
        averageValue: "1000"
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 10
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
      - type: Percent
        value: 100
        periodSeconds: 15
      - type: Pods
        value: 4
        periodSeconds: 15
      selectPolicy: Max
```

### 6.3 GPU Autoscaling

```yaml
# GPU-specific resource configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fraud-detection-gpu
spec:
  replicas: 2
  template:
    spec:
      containers:
      - name: model-server
        image: tritonserver:latest
        resources:
          requests:
            memory: "4Gi"
            cpu: "2"
            nvidia.com/gpu: 1
          limits:
            memory: "8Gi"
            cpu: "4"
            nvidia.com/gpu: 1
        env:
        - name: NVIDIA_VISIBLE_DEVICES
          value: "all"
      nodeSelector:
        accelerator: nvidia-tesla-t4
      tolerations:
      - key: "nvidia.com/gpu"
        operator: "Exists"
        effect: "NoSchedule"
```

### 6.4 Dynamic Batching

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Dynamic Batching                                  │
│                                                                     │
│  Request Queue:                                                     │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐               │
│  │ Req 1 │ │ Req 2 │ │ Req 3 │ │ Req 4 │ │ Req 5 │               │
│  └───────┘ └───────┘ └───────┘ └───────┘ └───────┘               │
│      │         │         │         │         │                     │
│      └─────────┴─────────┴─────────┴─────────┘                     │
│                          │                                          │
│                          ▼                                          │
│                   ┌──────────────┐                                 │
│                   │ Batch (5 req)│                                 │
│                   │  ────────►   │ Single GPU inference            │
│                   └──────────────┘                                 │
│                          │                                          │
│      ┌─────────┬─────────┼─────────┬─────────┐                     │
│      ▼         ▼         ▼         ▼         ▼                     │
│  ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐               │
│  │ Res 1 │ │ Res 2 │ │ Res 3 │ │ Res 4 │ │ Res 5 │               │
│  └───────┘ └───────┘ └───────┘ └───────┘ └───────┘               │
│                                                                     │
│  Benefits:                                                          │
│  - Higher GPU utilization (batched matrix ops)                      │
│  - Better throughput                                                │
│  - Trade-off: slightly higher latency for some requests             │
└─────────────────────────────────────────────────────────────────────┘
```

```protobuf
# Triton dynamic batching config
dynamic_batching {
  preferred_batch_size: [ 8, 16, 32 ]
  max_queue_delay_microseconds: 5000  # 5ms max wait
  preserve_ordering: true
  default_queue_policy {
    timeout_action: DELAY
    default_timeout_microseconds: 10000
    allow_timeout_override: true
  }
}
```

### 6.5 Caching

```yaml
# Response caching configuration
caching:
  enabled: true
  backend: redis
  connection: redis://cache:6379
  
  policies:
    - model: "static-recommendations"
      ttl: 3600  # 1 hour
      max_size: 10000
      
    - model: "user-embeddings"
      ttl: 300   # 5 minutes
      key_pattern: "user:{user_id}"
      
    - model: "fraud-detection"
      enabled: false  # Real-time, no caching
```

---

## 7. Security

> **Section Dependencies:**
> - Depends on: MOP-025 (Security Architecture)
> - Feeds into: MOP-026 (Access Control)
> - Update trigger: Security policy changes

### 7.1 Authentication & Authorization

```yaml
# Istio AuthorizationPolicy
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: fraud-detection-policy
  namespace: ml-serving
spec:
  selector:
    matchLabels:
      app: fraud-detection
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/default/sa/fraud-service"]
    to:
    - operation:
        methods: ["POST"]
        paths: ["/v2/models/fraud-detection/infer"]
  - from:
    - source:
        principals: ["cluster.local/ns/monitoring/sa/prometheus"]
    to:
    - operation:
        methods: ["GET"]
        paths: ["/metrics", "/v2/health/*"]
```

### 7.2 API Key Authentication

```python
# API key validation middleware
from fastapi import Security, HTTPException
from fastapi.security.api_key import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

async def validate_api_key(api_key: str = Security(api_key_header)):
    # Validate against key store
    if not await key_store.validate(api_key):
        raise HTTPException(status_code=403, detail="Invalid API key")
    
    # Rate limiting check
    if await rate_limiter.is_exceeded(api_key):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    
    return api_key
```

### 7.3 Encryption

```yaml
# TLS configuration
tls:
  enabled: true
  cert_file: /etc/certs/tls.crt
  key_file: /etc/certs/tls.key
  client_ca_file: /etc/certs/ca.crt  # mTLS
  min_version: "TLS1.3"
  
# Secrets management
secrets:
  provider: vault
  config:
    address: https://vault.example.com
    role: ml-serving
    mount_path: secret/data/ml
```

### 7.4 Input Validation

```python
from pydantic import BaseModel, validator
from typing import List
import numpy as np

class InferenceInput(BaseModel):
    features: List[float]
    
    @validator('features')
    def validate_features(cls, v):
        # Check length
        if len(v) != 128:
            raise ValueError(f"Expected 128 features, got {len(v)}")
        
        # Check range
        arr = np.array(v)
        if np.any(np.isnan(arr)):
            raise ValueError("NaN values not allowed")
        if np.any(np.isinf(arr)):
            raise ValueError("Infinite values not allowed")
        if np.any(arr < -1e6) or np.any(arr > 1e6):
            raise ValueError("Feature values out of expected range")
        
        return v
```

---

## 8. Monitoring & Observability

> **Section Dependencies:**
> - Depends on: All sections
> - Feeds into: MOP-037 (Metrics), MOP-038 (Performance Monitoring)
> - Update trigger: Monitoring requirements change

### 8.1 Metrics Collection

```python
# Prometheus metrics
from prometheus_client import Counter, Histogram, Gauge

# Request metrics
inference_requests = Counter(
    'inference_requests_total',
    'Total inference requests',
    ['model', 'version', 'status']
)

inference_latency = Histogram(
    'inference_latency_seconds',
    'Inference latency in seconds',
    ['model', 'version'],
    buckets=[0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0]
)

# Model metrics
model_loaded = Gauge(
    'model_loaded',
    'Model load status',
    ['model', 'version']
)

batch_size = Histogram(
    'inference_batch_size',
    'Batch size distribution',
    ['model'],
    buckets=[1, 2, 4, 8, 16, 32, 64]
)

# GPU metrics
gpu_utilization = Gauge(
    'gpu_utilization_percent',
    'GPU utilization percentage',
    ['gpu_id']
)

gpu_memory_used = Gauge(
    'gpu_memory_used_bytes',
    'GPU memory used',
    ['gpu_id']
)
```

### 8.2 Distributed Tracing

```python
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Configure tracing
trace.set_tracer_provider(TracerProvider())
jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger-agent",
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(jaeger_exporter)
)

tracer = trace.get_tracer(__name__)

async def infer(request):
    with tracer.start_as_current_span("inference") as span:
        span.set_attribute("model.name", model_name)
        span.set_attribute("model.version", model_version)
        span.set_attribute("batch.size", len(request.inputs))
        
        # Preprocessing
        with tracer.start_span("preprocess"):
            inputs = preprocess(request.inputs)
        
        # Model inference
        with tracer.start_span("model_forward"):
            outputs = model(inputs)
        
        # Postprocessing
        with tracer.start_span("postprocess"):
            results = postprocess(outputs)
        
        span.set_attribute("inference.success", True)
        return results
```

### 8.3 Alerting Rules

```yaml
# Prometheus alerting rules
groups:
- name: model-serving
  rules:
  - alert: HighLatency
    expr: |
      histogram_quantile(0.99, rate(inference_latency_seconds_bucket[5m])) > 0.1
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High inference latency"
      description: "P99 latency > 100ms for {{ $labels.model }}"
      
  - alert: HighErrorRate
    expr: |
      rate(inference_requests_total{status="error"}[5m]) 
      / rate(inference_requests_total[5m]) > 0.01
    for: 2m
    labels:
      severity: critical
    annotations:
      summary: "High error rate"
      description: "Error rate > 1% for {{ $labels.model }}"
      
  - alert: ModelNotReady
    expr: model_loaded == 0
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "Model not loaded"
      description: "{{ $labels.model }} v{{ $labels.version }} not loaded"
      
  - alert: LowThroughput
    expr: |
      rate(inference_requests_total[5m]) < 100
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "Unusually low throughput"
```

### 8.4 Dashboard Configuration

```json
{
  "title": "Model Serving Dashboard",
  "panels": [
    {
      "title": "Request Rate",
      "type": "graph",
      "targets": [
        {
          "expr": "sum(rate(inference_requests_total[5m])) by (model)",
          "legendFormat": "{{ model }}"
        }
      ]
    },
    {
      "title": "Latency (P50, P95, P99)",
      "type": "graph",
      "targets": [
        {
          "expr": "histogram_quantile(0.50, rate(inference_latency_seconds_bucket[5m]))",
          "legendFormat": "P50"
        },
        {
          "expr": "histogram_quantile(0.95, rate(inference_latency_seconds_bucket[5m]))",
          "legendFormat": "P95"
        },
        {
          "expr": "histogram_quantile(0.99, rate(inference_latency_seconds_bucket[5m]))",
          "legendFormat": "P99"
        }
      ]
    },
    {
      "title": "Error Rate",
      "type": "singlestat",
      "targets": [
        {
          "expr": "sum(rate(inference_requests_total{status='error'}[5m])) / sum(rate(inference_requests_total[5m])) * 100"
        }
      ],
      "thresholds": "0.1,1",
      "colors": ["green", "yellow", "red"]
    }
  ]
}
```

---

## Appendices

### Appendix A: Kubernetes Deployment Template

```yaml
# Complete deployment manifest
apiVersion: v1
kind: Namespace
metadata:
  name: ml-serving
  labels:
    istio-injection: enabled
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: model-config
  namespace: ml-serving
data:
  config.yaml: |
    models:
      fraud-detection:
        version: "3"
        replicas: 5
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: triton-inference-server
  namespace: ml-serving
spec:
  replicas: 3
  selector:
    matchLabels:
      app: triton
  template:
    metadata:
      labels:
        app: triton
    spec:
      containers:
      - name: triton
        image: nvcr.io/nvidia/tritonserver:23.10-py3
        args:
        - tritonserver
        - --model-repository=s3://model-repo
        - --model-control-mode=explicit
        - --strict-model-config=false
        ports:
        - containerPort: 8000
          name: http
        - containerPort: 8001
          name: grpc
        - containerPort: 8002
          name: metrics
        resources:
          requests:
            memory: "4Gi"
            cpu: "2"
          limits:
            memory: "8Gi"
            cpu: "4"
---
apiVersion: v1
kind: Service
metadata:
  name: triton-inference-server
  namespace: ml-serving
spec:
  selector:
    app: triton
  ports:
  - name: http
    port: 8000
  - name: grpc
    port: 8001
  - name: metrics
    port: 8002
```

### Appendix B: Load Testing

```python
# Locust load test
from locust import HttpUser, task, between
import json

class InferenceUser(HttpUser):
    wait_time = between(0.1, 0.5)
    
    @task
    def infer(self):
        payload = {
            "inputs": [
                {
                    "name": "features",
                    "shape": [1, 128],
                    "datatype": "FP32",
                    "data": [0.1] * 128
                }
            ]
        }
        
        self.client.post(
            "/v2/models/fraud-detection/infer",
            json=payload,
            headers={"Content-Type": "application/json"}
        )

# Run: locust -f load_test.py --host=http://inference:8000
```

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
| Infrastructure Lead | | | |
| Security | | | |
