---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-035: Tool Updates and Patches

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-035 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE / Platform Lead] |

---

## 1. Update Policy

### 1.1 Update Categories

| Category | Response Time | Approval |
|----------|---------------|----------|
| Critical Security | 24-72 hours | Emergency CAB |
| High Security | 1-2 weeks | CAB |
| Minor Security | 30 days | Standard |
| Feature Update | Quarterly | Standard |
| Major Version | Planning cycle | Architecture Review |

### 1.2 Tool Update Matrix

| Tool | Current | Update Frequency | Testing Required |
|------|---------|------------------|------------------|
| MLflow | 2.10.x | Quarterly | Full regression |
| Feast | 0.36.x | Quarterly | Full regression |
| Triton | 23.10 | Semi-annual | Performance test |
| KServe | 0.12.x | Quarterly | Integration test |
| Kubernetes | 1.28 | Semi-annual | Full regression |
| Prometheus | 2.48 | Quarterly | Smoke test |

---

## 2. Update Process

### 2.1 Update Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    Update Workflow                           │
│                                                             │
│  1. Monitor    ──►  2. Assess    ──►  3. Plan              │
│  (Releases)        (Impact)          (Schedule)            │
│                                                             │
│       │                │                  │                 │
│       ▼                ▼                  ▼                 │
│                                                             │
│  4. Test       ──►  5. Stage     ──►  6. Production        │
│  (Dev/QA)          (Canary)          (Full rollout)        │
│                                                             │
│       │                │                  │                 │
│       ▼                ▼                  ▼                 │
│                                                             │
│  7. Monitor    ──►  8. Document  ──►  9. Close             │
│  (Post-deploy)      (Changelog)       (Complete)           │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Pre-Update Checklist

```markdown
## Pre-Update Checklist

**Tool:** ___________
**Current Version:** ___________
**Target Version:** ___________
**Date:** ___________

### Assessment
- [ ] Release notes reviewed
- [ ] Breaking changes identified
- [ ] Dependencies checked
- [ ] Rollback plan documented

### Testing
- [ ] Dev environment updated
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Performance baseline captured

### Approval
- [ ] Change request submitted
- [ ] CAB approval (if required)
- [ ] Stakeholders notified
```

---

## 3. Tool-Specific Procedures

### 3.1 MLflow Update

```bash
#!/bin/bash
# updates/update_mlflow.sh

NEW_VERSION=$1
NAMESPACE="mlops"

echo "=== Updating MLflow to $NEW_VERSION ==="

# 1. Update image in deployment
echo "[1/5] Updating deployment..."
kubectl set image deployment/mlflow \
  mlflow=ghcr.io/mlflow/mlflow:v${NEW_VERSION} \
  -n $NAMESPACE

# 2. Wait for rollout
echo "[2/5] Waiting for rollout..."
kubectl rollout status deployment/mlflow -n $NAMESPACE --timeout=5m

# 3. Run health check
echo "[3/5] Running health check..."
curl -sf https://mlflow.example.com/health || exit 1

# 4. Run smoke tests
echo "[4/5] Running smoke tests..."
python tests/smoke/test_mlflow.py

# 5. Verify database migrations
echo "[5/5] Checking database..."
kubectl exec -n $NAMESPACE deploy/mlflow -- mlflow db upgrade

echo "=== MLflow Update Complete ==="
```

### 3.2 Feast Update

```bash
#!/bin/bash
# updates/update_feast.sh

NEW_VERSION=$1

echo "=== Updating Feast to $NEW_VERSION ==="

# 1. Update feature server
kubectl set image deployment/feast-server \
  feast=feastdev/feature-server:${NEW_VERSION} \
  -n feast

# 2. Wait for rollout
kubectl rollout status deployment/feast-server -n feast --timeout=5m

# 3. Verify materialization
feast materialize-incremental $(date -u +"%Y-%m-%dT%H:%M:%S")

# 4. Test online features
python tests/smoke/test_feast.py

echo "=== Feast Update Complete ==="
```

### 3.3 Kubernetes Update

```bash
#!/bin/bash
# updates/update_kubernetes.sh

NEW_VERSION=$1
CLUSTER_NAME="mlops-cluster"

echo "=== Updating Kubernetes to $NEW_VERSION ==="

# 1. Update control plane (EKS)
echo "[1/4] Updating control plane..."
aws eks update-cluster-version \
  --name $CLUSTER_NAME \
  --kubernetes-version $NEW_VERSION

# Wait for control plane
aws eks wait cluster-active --name $CLUSTER_NAME

# 2. Update node groups (rolling)
echo "[2/4] Updating node groups..."
for ng in $(aws eks list-nodegroups --cluster-name $CLUSTER_NAME --query 'nodegroups[]' --output text); do
  aws eks update-nodegroup-version \
    --cluster-name $CLUSTER_NAME \
    --nodegroup-name $ng \
    --kubernetes-version $NEW_VERSION
done

# 3. Update add-ons
echo "[3/4] Updating add-ons..."
aws eks update-addon --cluster-name $CLUSTER_NAME --addon-name vpc-cni
aws eks update-addon --cluster-name $CLUSTER_NAME --addon-name coredns
aws eks update-addon --cluster-name $CLUSTER_NAME --addon-name kube-proxy

# 4. Verify
echo "[4/4] Verifying..."
kubectl get nodes
kubectl get pods --all-namespaces | grep -v Running

echo "=== Kubernetes Update Complete ==="
```

---

## 4. Security Patching

### 4.1 Vulnerability Scanning

```yaml
# .github/workflows/security-scan.yml
name: Security Scan

on:
  schedule:
    - cron: '0 6 * * *'  # Daily at 6 AM

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - name: Scan container images
        uses: aquasecurity/trivy-action@master
        with:
          image-ref: 'ghcr.io/mlflow/mlflow:latest'
          severity: 'CRITICAL,HIGH'
          
      - name: Create issue if vulnerabilities found
        if: failure()
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: 'Security vulnerabilities detected',
              body: 'Critical/High vulnerabilities found in container images.'
            })
```

### 4.2 Emergency Patch Procedure

```markdown
## Emergency Security Patch Procedure

1. **Assessment** (15 min)
   - Verify vulnerability severity
   - Identify affected components
   - Assess exposure

2. **Communication** (5 min)
   - Page on-call team
   - Notify security team
   - Create incident ticket

3. **Mitigation** (varies)
   - Apply temporary mitigation if available
   - Test patch in dev environment
   - Fast-track CAB approval

4. **Deployment** (30 min)
   - Deploy to staging
   - Quick smoke test
   - Deploy to production

5. **Verification** (15 min)
   - Confirm patch applied
   - Verify no regression
   - Update vulnerability tracker
```

---

## 5. Version Tracking

### 5.1 Tool Inventory

```yaml
# inventory/tool_versions.yaml
tools:
  mlflow:
    current_version: "2.10.0"
    latest_version: "2.10.2"
    update_available: true
    last_updated: "2024-01-15"
    
  feast:
    current_version: "0.36.0"
    latest_version: "0.36.1"
    update_available: true
    last_updated: "2024-01-10"
    
  triton:
    current_version: "23.10"
    latest_version: "24.01"
    update_available: true
    last_updated: "2023-11-20"
```

### 5.2 Update Dashboard

| Tool | Current | Latest | Status | Last Updated |
|------|---------|--------|--------|--------------|
| MLflow | 2.10.0 | 2.10.2 |  Update Available | 2024-01-15 |
| Feast | 0.36.0 | 0.36.0 |  Current | 2024-01-10 |
| Triton | 23.10 | 24.01 |  Update Available | 2023-11-20 |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial update procedures |
