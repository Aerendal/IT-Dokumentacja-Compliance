---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-023: Container Orchestration Setup (Kubernetes)

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-023 |
| **Version** | 1.0 |
| **Owner** | [Platform Engineer] |

---

## 1. EKS Cluster Configuration

### 1.1 Cluster Setup
```hcl
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.0.0"

  cluster_name    = "production-cluster"
  cluster_version = "1.28"

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets

  eks_managed_node_groups = {
    general = {
      instance_types = ["m5.xlarge"]
      min_size       = 3
      max_size       = 10
      desired_size   = 5
    }
  }

  cluster_addons = {
    coredns = { most_recent = true }
    kube-proxy = { most_recent = true }
    vpc-cni = { most_recent = true }
  }
}
```

---

## 2. Core Components

| Component | Version | Purpose |
|-----------|---------|---------|
| AWS Load Balancer Controller | 2.6 | ALB/NLB integration |
| External DNS | 0.13 | Route 53 integration |
| Cluster Autoscaler | 1.28 | Node scaling |
| Metrics Server | 0.6 | Resource metrics |

---

## 3. Namespace Structure

| Namespace | Purpose | Resource Quotas |
|-----------|---------|-----------------|
| production | Prod workloads | CPU: 100, Mem: 200Gi |
| staging | Staging workloads | CPU: 50, Mem: 100Gi |
| monitoring | Observability | CPU: 20, Mem: 50Gi |
| ingress | Ingress controllers | CPU: 10, Mem: 20Gi |

---

## 4. GitOps Setup (ArgoCD)

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: app-production
spec:
  project: default
  source:
    repoURL: https://github.com/company/k8s-manifests
    path: apps/production
    targetRevision: main
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial K8s setup |
