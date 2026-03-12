---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-059: Resource Optimization Guide

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-059 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE / FinOps] |

---

## 1. Optimization Overview

### 1.1 Optimization Areas

| Area | Potential Savings | Effort |
|------|-------------------|--------|
| Compute (Reserved/Spot) | 30-70% | Low |
| Right-sizing | 20-40% | Medium |
| Auto-scaling | 15-25% | Medium |
| Storage tiering | 10-20% | Low |
| GPU sharing | 20-40% | High |

### 1.2 Current Cost Breakdown

| Category | Monthly Cost | % of Total |
|----------|-------------|------------|
| Compute (CPU) | $25,000 | 28% |
| Compute (GPU) | $35,000 | 39% |
| Storage | $12,000 | 13% |
| Database | $8,000 | 9% |
| Network | $5,000 | 6% |
| Other | $5,000 | 5% |
| **Total** | **$90,000** | **100%** |

---

## 2. Compute Optimization

### 2.1 Reserved Instances

| Workload | Recommendation | Savings |
|----------|----------------|---------|
| Model Serving (base) | 1-year reserved | 30-40% |
| Feature Store | 1-year reserved | 30-40% |
| Platform services | 1-year reserved | 30-40% |

**Implementation:**
```bash
# Calculate reserved instance needs
# Base capacity = minimum needed 24/7
aws ec2 describe-instances --filters "Name=tag:Environment,Values=production" \
  --query 'Reservations[*].Instances[*].[InstanceType]' | sort | uniq -c
```

### 2.2 Spot Instances for Training

| Use Case | Spot Eligible | Savings |
|----------|---------------|---------|
| Training jobs |  | 60-70% |
| Batch processing |  | 60-70% |
| CI/CD runners |  | 60-70% |
| Production serving |  | N/A |

**Spot Configuration:**
```yaml
# training-job-spot.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: training-job
spec:
  template:
    spec:
      nodeSelector:
        node.kubernetes.io/instance-type: spot
      tolerations:
        - key: "spot"
          operator: "Equal"
          value: "true"
      containers:
        - name: trainer
          resources:
            requests:
              cpu: "4"
              memory: "16Gi"
```

### 2.3 Right-Sizing

**Analysis Script:**
```python
# optimization/right_sizing.py
import boto3
from datetime import datetime, timedelta

def analyze_utilization(namespace: str, days: int = 7):
    """Analyze pod resource utilization."""
    
    # Query Prometheus for actual usage
    cpu_query = f'''
        avg by (pod) (
            rate(container_cpu_usage_seconds_total{{namespace="{namespace}"}}[{days}d])
        )
    '''
    
    memory_query = f'''
        avg by (pod) (
            container_memory_working_set_bytes{{namespace="{namespace}"}}
        )
    '''
    
    # Compare to requests
    recommendations = []
    for pod in get_pods(namespace):
        cpu_actual = query_prometheus(cpu_query, pod)
        cpu_requested = pod.resources.requests.cpu
        
        if cpu_actual < cpu_requested * 0.5:
            recommendations.append({
                'pod': pod.name,
                'resource': 'cpu',
                'current': cpu_requested,
                'recommended': cpu_actual * 1.3,  # 30% buffer
                'savings': f'{(1 - cpu_actual/cpu_requested) * 100:.0f}%'
            })
    
    return recommendations
```

**Right-Sizing Targets:**
| Resource | Target Utilization | Over-provisioned If |
|----------|-------------------|---------------------|
| CPU | 60-70% | <40% avg |
| Memory | 70-80% | <50% avg |
| GPU | 70-80% | <50% avg |

---

## 3. Storage Optimization

### 3.1 S3 Storage Classes

| Data Type | Storage Class | Cost Reduction |
|-----------|---------------|----------------|
| Active artifacts (<30 days) | Standard | Baseline |
| Older artifacts (30-90 days) | Standard-IA | 45% |
| Archive (>90 days) | Glacier | 80% |
| Experiment data (>1 year) | Glacier Deep | 95% |

**Lifecycle Policy:**
```json
{
  "Rules": [
    {
      "ID": "MLOps-Artifact-Lifecycle",
      "Status": "Enabled",
      "Filter": {"Prefix": "artifacts/"},
      "Transitions": [
        {"Days": 30, "StorageClass": "STANDARD_IA"},
        {"Days": 90, "StorageClass": "GLACIER"},
        {"Days": 365, "StorageClass": "DEEP_ARCHIVE"}
      ]
    }
  ]
}
```

### 3.2 Storage Cleanup

**Automated Cleanup:**
```python
# optimization/storage_cleanup.py
def cleanup_orphaned_artifacts():
    """Remove artifacts not referenced by any model."""
    
    # Get all registered model artifacts
    registered_artifacts = get_registered_artifacts()
    
    # List all S3 artifacts
    all_artifacts = list_s3_artifacts('mlops-artifacts')
    
    # Find orphaned
    orphaned = set(all_artifacts) - set(registered_artifacts)
    
    # Delete (with safety check)
    for artifact in orphaned:
        if artifact_age(artifact) > timedelta(days=30):
            delete_artifact(artifact)
            
    return len(orphaned)
```

---

## 4. GPU Optimization

### 4.1 GPU Sharing (MIG/Time-slicing)

| Technique | Use Case | Efficiency Gain |
|-----------|----------|-----------------|
| MIG (A100) | Multiple small models | 2-7x |
| Time-slicing | Inference workloads | 2-4x |
| Multi-instance | Training + inference | Variable |

**Time-slicing Configuration:**
```yaml
# gpu-time-slicing.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nvidia-device-plugin-config
  namespace: kube-system
data:
  config.yaml: |
    sharing:
      timeSlicing:
        resources:
          - name: nvidia.com/gpu
            replicas: 4  # Share each GPU 4 ways
```

### 4.2 GPU Scheduling

```yaml
# Prefer spot GPUs for training
spec:
  affinity:
    nodeAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
        - weight: 100
          preference:
            matchExpressions:
              - key: node.kubernetes.io/instance-type
                operator: In
                values: ["spot"]
```

---

## 5. Auto-Scaling Optimization

### 5.1 HPA Tuning

```yaml
# Optimized HPA configuration
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: model-serving-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: model-serving
  minReplicas: 2      # Minimum for HA
  maxReplicas: 20     # Cost cap
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300  # Prevent thrashing
      policies:
        - type: Percent
          value: 25
          periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
        - type: Percent
          value: 100
          periodSeconds: 60
```

### 5.2 Scheduled Scaling

```yaml
# Scale down during off-hours
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: model-serving-scheduled
spec:
  scaleTargetRef:
    name: model-serving
  minReplicaCount: 1
  maxReplicaCount: 20
  triggers:
    - type: cron
      metadata:
        timezone: America/New_York
        start: 0 8 * * 1-5    # Scale up 8 AM Mon-Fri
        end: 0 20 * * 1-5     # Scale down 8 PM Mon-Fri
        desiredReplicas: "10"
    - type: cron
      metadata:
        timezone: America/New_York
        start: 0 20 * * *     # Off hours
        end: 0 8 * * *
        desiredReplicas: "2"
```

---

## 6. Optimization Tracking

### 6.1 Savings Dashboard

| Initiative | Projected Savings | Actual | Status |
|------------|-------------------|--------|--------|
| Reserved instances | $15,000/mo | $14,200 |  |
| Spot for training | $8,000/mo | $7,500 |  |
| Storage tiering | $3,000/mo | $2,800 |  |
| Right-sizing | $5,000/mo | In progress |  |
| **Total** | **$31,000/mo** | **$24,500** | |

### 6.2 Cost Alerts

```yaml
# prometheus/cost-alerts.yaml
groups:
  - name: cost-alerts
    rules:
      - alert: UnexpectedCostIncrease
        expr: |
          increase(aws_cost_total[1d]) > 
          avg_over_time(increase(aws_cost_total[1d])[7d:1d]) * 1.2
        for: 1h
        annotations:
          summary: "Daily cost 20% above average"
          
      - alert: IdleGPUResources
        expr: DCGM_FI_DEV_GPU_UTIL < 10
        for: 2h
        annotations:
          summary: "GPU {{ $labels.gpu }} underutilized (<10%)"
```

---

## 7. Monthly Optimization Review

### 7.1 Review Checklist

- [ ] Review cost trends vs budget
- [ ] Identify top 5 cost contributors
- [ ] Check resource utilization reports
- [ ] Review auto-scaling effectiveness
- [ ] Validate reserved instance coverage
- [ ] Check for orphaned resources
- [ ] Update optimization initiatives

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial optimization guide |
