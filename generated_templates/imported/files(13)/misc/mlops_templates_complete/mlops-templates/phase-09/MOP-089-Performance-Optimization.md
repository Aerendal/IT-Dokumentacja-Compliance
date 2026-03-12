---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-089: Performance Optimization Playbook

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-089 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Performance Targets

| Metric | Target | Critical | Measurement |
|--------|--------|----------|-------------|
| Inference P50 | <30ms | <50ms | Continuous |
| Inference P99 | <100ms | <200ms | Continuous |
| Throughput | >1000 RPS | >500 RPS | Per model |
| Cold Start | <5s | <10s | On scale-up |
| Training Time | Baseline | 2x baseline | Per job |

---

## 2. Model Inference Optimization

### 2.1 Model Optimization Techniques

| Technique | Latency Reduction | Accuracy Impact | Effort |
|-----------|-------------------|-----------------|--------|
| Quantization (INT8) | 30-50% | <1% | Low |
| Pruning | 20-40% | 1-3% | Medium |
| Distillation | 40-60% | 2-5% | High |
| ONNX conversion | 10-30% | None | Low |
| TensorRT | 30-50% | <1% | Medium |

### 2.2 ONNX Conversion

```python
# optimization/convert_to_onnx.py
import torch
import onnx
import onnxruntime as ort

def convert_pytorch_to_onnx(model, sample_input, output_path: str):
    """Convert PyTorch model to ONNX."""
    model.eval()
    
    torch.onnx.export(
        model,
        sample_input,
        output_path,
        export_params=True,
        opset_version=14,
        do_constant_folding=True,
        input_names=['input'],
        output_names=['output'],
        dynamic_axes={
            'input': {0: 'batch_size'},
            'output': {0: 'batch_size'}
        }
    )
    
    # Verify
    onnx_model = onnx.load(output_path)
    onnx.checker.check_model(onnx_model)
    
    # Test inference
    ort_session = ort.InferenceSession(output_path)
    ort_inputs = {ort_session.get_inputs()[0].name: sample_input.numpy()}
    ort_output = ort_session.run(None, ort_inputs)
    
    return ort_output
```

### 2.3 Quantization

```python
# optimization/quantize_model.py
import torch
from torch.quantization import quantize_dynamic

def quantize_model(model, dtype=torch.qint8):
    """Apply dynamic quantization."""
    quantized = quantize_dynamic(
        model,
        {torch.nn.Linear, torch.nn.LSTM},
        dtype=dtype
    )
    return quantized

# For static quantization
def calibrate_and_quantize(model, calibration_data):
    """Calibrate and apply static quantization."""
    model.qconfig = torch.quantization.get_default_qconfig('fbgemm')
    model_prepared = torch.quantization.prepare(model)
    
    # Calibration
    with torch.no_grad():
        for data in calibration_data:
            model_prepared(data)
    
    model_quantized = torch.quantization.convert(model_prepared)
    return model_quantized
```

---

## 3. Infrastructure Optimization

### 3.1 Scaling Configuration

```yaml
# k8s/optimized-hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: model-serving-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: model-serving
  minReplicas: 3
  maxReplicas: 50
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Pods
      pods:
        metric:
          name: inference_queue_length
        target:
          type: AverageValue
          averageValue: "10"
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
        - type: Percent
          value: 100
          periodSeconds: 60
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 25
          periodSeconds: 120
```

### 3.2 Resource Tuning

```yaml
# Optimized pod resources
resources:
  requests:
    cpu: "1"
    memory: "2Gi"
  limits:
    cpu: "2"
    memory: "4Gi"
    
# Pod anti-affinity for spread
affinity:
  podAntiAffinity:
    preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          topologyKey: kubernetes.io/hostname
```

---

## 4. Feature Store Optimization

### 4.1 Redis Optimization

```python
# optimization/feast_optimization.py
# Use pipeline for batch operations
def get_features_batch(entity_ids: list, features: list):
    """Optimized batch feature retrieval."""
    pipe = redis_client.pipeline()
    
    for entity_id in entity_ids:
        key = f"feast:user:{entity_id}"
        pipe.hgetall(key)
    
    results = pipe.execute()
    return results

# Configure connection pooling
REDIS_POOL = redis.ConnectionPool(
    host='redis.example.com',
    port=6379,
    max_connections=100,
    socket_timeout=0.5,
    socket_connect_timeout=0.5
)
```

---

## 5. Training Optimization

### 5.1 Distributed Training

```python
# optimization/distributed_training.py
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel

def setup_distributed():
    dist.init_process_group(backend='nccl')
    
def train_distributed(model, train_loader, epochs):
    model = DistributedDataParallel(model)
    
    for epoch in range(epochs):
        train_loader.sampler.set_epoch(epoch)
        for batch in train_loader:
            # Training step
            pass
```

### 5.2 Mixed Precision

```python
# Use automatic mixed precision
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for batch in train_loader:
    optimizer.zero_grad()
    
    with autocast():
        output = model(batch)
        loss = criterion(output, target)
    
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

---

## 6. Optimization Checklist

```markdown
## Performance Optimization Checklist

### Model Level
- [ ] Model profiled for bottlenecks
- [ ] Quantization evaluated
- [ ] ONNX conversion tested
- [ ] Batch inference optimized

### Infrastructure Level
- [ ] HPA configured properly
- [ ] Resource requests/limits tuned
- [ ] Connection pooling enabled
- [ ] Caching implemented

### Data Level
- [ ] Feature retrieval optimized
- [ ] Preprocessing moved to pipeline
- [ ] Data loading parallelized
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial optimization playbook |
