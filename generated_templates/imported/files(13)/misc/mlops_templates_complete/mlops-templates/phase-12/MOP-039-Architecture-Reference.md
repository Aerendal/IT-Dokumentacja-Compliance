---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-039: MLOps Architecture Reference

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-039 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML Platform Lead] |

---

## 1. Architecture Overview

### 1.1 System Context Diagram
```
┌─────────────────────────────────────────────────────────────────┐
│                      MLOps Platform                              │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐           │
│  │ MLflow  │  │  Feast  │  │ Triton  │  │Kubeflow │           │
│  │Tracking │  │Feature  │  │ Server  │  │Pipelines│           │
│  │+Registry│  │ Store   │  │         │  │         │           │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘           │
│       └────────────┴────────────┴────────────┘                 │
│                         │                                       │
│              ┌──────────┴──────────┐                           │
│              │    Kubernetes       │                           │
│              │    (EKS/GKE)        │                           │
│              └──────────┬──────────┘                           │
│                         │                                       │
│    ┌────────────────────┼────────────────────┐                 │
│    │                    │                    │                 │
│ ┌──┴───┐          ┌─────┴─────┐        ┌────┴────┐           │
│ │ S3   │          │PostgreSQL │        │  Redis  │           │
│ └──────┘          └───────────┘        └─────────┘           │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Component Inventory

| Component | Version | Purpose | Port |
|-----------|---------|---------|------|
| MLflow | 2.10.x | Experiment tracking, registry | 5000 |
| Feast | 0.36.x | Feature store | 6566 |
| Triton | 23.10 | Model inference | 8000/8001 |
| KServe | 0.12.x | Model serving orchestration | - |
| Airflow | 2.8.x | Data pipelines | 8080 |
| Kubeflow | 1.8.x | ML pipelines | - |
| Prometheus | 2.48.x | Metrics | 9090 |
| Grafana | 10.x | Dashboards | 3000 |

---

## 2. Network Architecture

### 2.1 Network Topology
```
Internet
    │
    ▼
┌─────────────────┐
│   CloudFront    │
│   (CDN/WAF)     │
└────────┬────────┘
         │
┌────────▼────────┐
│  Load Balancer  │
│   (ALB/NLB)     │
└────────┬────────┘
         │
┌────────▼────────────────────────────────────┐
│              VPC (10.0.0.0/16)              │
│  ┌──────────────┐  ┌──────────────┐        │
│  │Public Subnet │  │Public Subnet │        │
│  │ 10.0.1.0/24  │  │ 10.0.2.0/24  │        │
│  │   (AZ-a)     │  │   (AZ-b)     │        │
│  └──────┬───────┘  └──────┬───────┘        │
│         │                 │                 │
│  ┌──────▼───────┐  ┌──────▼───────┐        │
│  │Private Subnet│  │Private Subnet│        │
│  │ 10.0.10.0/24 │  │ 10.0.20.0/24 │        │
│  │  (Workloads) │  │  (Workloads) │        │
│  └──────────────┘  └──────────────┘        │
│  ┌──────────────┐  ┌──────────────┐        │
│  │  DB Subnet   │  │  DB Subnet   │        │
│  │ 10.0.100.0/24│  │ 10.0.200.0/24│        │
│  └──────────────┘  └──────────────┘        │
└─────────────────────────────────────────────┘
```

### 2.2 Endpoints Reference

| Service | Internal URL | External URL |
|---------|--------------|--------------|
| MLflow | mlflow.mlops.svc:5000 | mlflow.example.com |
| Feast | feast.feast.svc:6566 | feast.example.com |
| Model API | {model}.models.svc:8080 | {model}.api.example.com |
| Grafana | grafana.monitoring.svc:3000 | grafana.example.com |

---

## 3. Data Flow Reference

### 3.1 Training Data Flow
```
Data Lake (S3) → Airflow → Feature Engineering → Feast (offline)
                                    ↓
                              MLflow Tracking
                                    ↓
                              Model Registry
```

### 3.2 Inference Data Flow
```
Client Request → API Gateway → KServe → Triton
                                  ↓
                            Feast (online)
                                  ↓
                              Response
```

---

## 4. Security Reference

### 4.1 Authentication Endpoints

| Provider | URL | Protocol |
|----------|-----|----------|
| Okta OIDC | company.okta.com | OAuth2/OIDC |
| Vault | vault.internal:8200 | HTTPS |

### 4.2 Service Accounts

| Service Account | Namespace | Purpose |
|-----------------|-----------|---------|
| mlflow-sa | mlops | MLflow operations |
| feast-sa | feast | Feature store |
| model-serving-sa | models | Model inference |

---

## 5. Quick Reference Commands

```bash
# Check platform health
kubectl get pods -n mlops
kubectl get pods -n models
kubectl get pods -n feast

# View logs
kubectl logs -l app=mlflow -n mlops --tail=100
kubectl logs -l app=feast-server -n feast --tail=100

# Port forward for debugging
kubectl port-forward svc/mlflow 5000:5000 -n mlops
kubectl port-forward svc/grafana 3000:3000 -n monitoring
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial reference |
