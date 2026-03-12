---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-025: MLOps Security Architecture

## Document Metadata

| Field | Value |
|-------|-------|
| **Document ID** | MOP-025 |
| **Version** | 1.0 |
| **Status** | DRAFT / IN REVIEW / ACTIVE / OBSOLETE |
| **Priority** | CRITICAL |
| **Owner** | [Security Architect / ML Platform Lead] |
| **Created** | [YYYY-MM-DD] |
| **Last Updated** | [YYYY-MM-DD] |
| **Next Review** | [YYYY-MM-DD] (Quarterly) |

---

## Dependencies

### Requires (Inputs)
| Document | Section Affected |
|----------|------------------|
| MOP-007: Architecture | Security layers |
| MOP-004: Requirements | Security requirements |
| Corporate Security Policy | Compliance |

### Feeds Into (Outputs)
| Document | What It Provides |
|----------|------------------|
| MOP-026: Access Control | RBAC design |
| MOP-027: Audit Logging | Audit specs |
| All Implementation Docs | Security specs |

---

## Template Content

---

# MLOps Security Architecture

## 1. Security Overview

### 1.1 Security Principles

| Principle | Description |
|-----------|-------------|
| **Defense in Depth** | Multiple security layers |
| **Least Privilege** | Minimal required access |
| **Zero Trust** | Verify everything, trust nothing |
| **Secure by Default** | Security enabled by default |
| **Audit Everything** | Complete audit trail |

### 1.2 Security Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    MLOps Security Layers                             │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ PERIMETER SECURITY                                              ││
│  │  WAF │ DDoS Protection │ API Gateway │ Rate Limiting           ││
│  └─────────────────────────────────────────────────────────────────┘│
│                                │                                    │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ IDENTITY & ACCESS                                               ││
│  │  SSO/OIDC │ MFA │ RBAC │ Service Accounts │ API Keys           ││
│  └─────────────────────────────────────────────────────────────────┘│
│                                │                                    │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ NETWORK SECURITY                                                ││
│  │  VPC │ Security Groups │ Network Policies │ mTLS │ Service Mesh││
│  └─────────────────────────────────────────────────────────────────┘│
│                                │                                    │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ APPLICATION SECURITY                                            ││
│  │  Input Validation │ Secrets Management │ Dependency Scanning   ││
│  └─────────────────────────────────────────────────────────────────┘│
│                                │                                    │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ DATA SECURITY                                                   ││
│  │  Encryption at Rest │ Encryption in Transit │ Data Masking     ││
│  └─────────────────────────────────────────────────────────────────┘│
│                                │                                    │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ MONITORING & AUDIT                                              ││
│  │  SIEM │ Audit Logs │ Anomaly Detection │ Incident Response     ││
│  └─────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Identity & Access Management

### 2.1 Authentication

```yaml
# OIDC Configuration
authentication:
  provider: okta  # or azure-ad, google
  oidc:
    issuer: "https://company.okta.com/oauth2/default"
    client_id: "${OIDC_CLIENT_ID}"
    client_secret: "${OIDC_CLIENT_SECRET}"
    scopes: ["openid", "profile", "email", "groups"]
  mfa:
    required: true
    methods: ["totp", "webauthn"]
```

### 2.2 Role-Based Access Control (RBAC)

| Role | Experiment Tracking | Model Registry | Serving | Admin |
|------|---------------------|----------------|---------|-------|
| **Viewer** | Read | Read | Read | - |
| **Data Scientist** | Read/Write | Read/Stage | Read | - |
| **ML Engineer** | Read/Write | Read/Write/Promote | Read/Write | - |
| **Platform Admin** | Full | Full | Full | Full |
| **Security Admin** | Audit | Audit | Audit | Security |

### 2.3 Service Authentication

```yaml
# Kubernetes Service Account
apiVersion: v1
kind: ServiceAccount
metadata:
  name: ml-pipeline-sa
  namespace: mlops
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::ACCOUNT:role/MLPipelineRole
---
# IAM Policy (AWS)
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::mlops-artifacts/*"
    }
  ]
}
```

---

## 3. Network Security

### 3.1 Network Segmentation

```yaml
# Kubernetes Network Policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: mlops-network-policy
  namespace: mlops
spec:
  podSelector:
    matchLabels:
      app: mlflow
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: ingress-nginx
    ports:
    - protocol: TCP
      port: 5000
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          name: databases
    ports:
    - protocol: TCP
      port: 5432
```

### 3.2 Service Mesh (Istio) Configuration

```yaml
# mTLS Configuration
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: mlops
spec:
  mtls:
    mode: STRICT
---
# Authorization Policy
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: mlflow-authz
  namespace: mlops
spec:
  selector:
    matchLabels:
      app: mlflow
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/mlops/sa/ml-pipeline-sa"]
    to:
    - operation:
        methods: ["GET", "POST"]
        paths: ["/api/*"]
```

---

## 4. Data Security

### 4.1 Encryption Configuration

| Data State | Method | Key Management |
|------------|--------|----------------|
| At Rest (S3) | AES-256 SSE | AWS KMS |
| At Rest (DB) | TDE | AWS RDS encryption |
| In Transit | TLS 1.3 | ACM/Let's Encrypt |
| Secrets | Vault Transit | HashiCorp Vault |

### 4.2 Data Classification

| Classification | Description | Controls |
|----------------|-------------|----------|
| **Public** | Non-sensitive | Standard encryption |
| **Internal** | Business data | Access control, encryption |
| **Confidential** | Sensitive business | MFA, audit logging |
| **Restricted** | PII, financial | Full controls, DLP |

### 4.3 Data Masking

```python
# Feature Store Data Masking
def mask_pii_features(df):
    """Mask PII before feature creation."""
    pii_columns = ["ssn", "email", "phone"]
    
    for col in pii_columns:
        if col in df.columns:
            df[col] = df[col].apply(hash_value)
    
    return df
```

---

## 5. Secrets Management

### 5.1 Vault Integration

```yaml
# External Secrets Operator
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: mlflow-secrets
  namespace: mlops
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: vault-backend
    kind: ClusterSecretStore
  target:
    name: mlflow-secrets
  data:
  - secretKey: db-password
    remoteRef:
      key: mlops/mlflow
      property: db_password
  - secretKey: s3-access-key
    remoteRef:
      key: mlops/aws
      property: access_key
```

### 5.2 Secret Rotation

| Secret Type | Rotation Period | Method |
|-------------|-----------------|--------|
| Database passwords | 90 days | Automated |
| API keys | 30 days | Automated |
| Service account keys | 365 days | Manual approval |
| TLS certificates | 30 days | Auto (cert-manager) |

---

## 6. Application Security

### 6.1 Input Validation

```python
# Model Inference Input Validation
from pydantic import BaseModel, validator
from typing import List

class InferenceRequest(BaseModel):
    features: List[float]
    
    @validator('features')
    def validate_features(cls, v):
        if len(v) != 50:
            raise ValueError('Expected 50 features')
        if any(not math.isfinite(x) for x in v):
            raise ValueError('Features must be finite')
        if any(x < -1e6 or x > 1e6 for x in v):
            raise ValueError('Features out of range')
        return v
```

### 6.2 Dependency Scanning

```yaml
# GitHub Actions - Security Scanning
- name: Run Trivy vulnerability scanner
  uses: aquasecurity/trivy-action@master
  with:
    image-ref: 'mlops/serving:${{ github.sha }}'
    format: 'sarif'
    severity: 'CRITICAL,HIGH'
    exit-code: '1'

- name: Run Snyk to check for vulnerabilities
  uses: snyk/actions/python@master
  with:
    args: --severity-threshold=high
```

### 6.3 Container Security

```dockerfile
# Secure Dockerfile
FROM python:3.11-slim AS builder
# Build stage...

FROM gcr.io/distroless/python3-debian12
COPY --from=builder /app /app
USER nonroot:nonroot
ENTRYPOINT ["python", "/app/main.py"]
```

---

## 7. Audit & Compliance

### 7.1 Audit Log Schema

```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "event_type": "model.deployed",
  "actor": {
    "id": "user@company.com",
    "ip": "10.0.0.1",
    "user_agent": "mlflow-client/2.10.0"
  },
  "resource": {
    "type": "model",
    "id": "fraud-model",
    "version": "3"
  },
  "action": "promote_to_production",
  "result": "success",
  "metadata": {
    "environment": "production",
    "approver": "ml-lead@company.com"
  }
}
```

### 7.2 Compliance Requirements

| Framework | Requirement | Implementation |
|-----------|-------------|----------------|
| SOC2 | Access Control | RBAC, audit logs |
| SOC2 | Encryption | TLS 1.3, AES-256 |
| GDPR | Data Protection | Encryption, access control |
| GDPR | Right to Erasure | Data deletion pipeline |
| HIPAA | PHI Protection | Additional encryption, audit |

### 7.3 Security Monitoring

```yaml
# Falco Rules for ML Workloads
- rule: Suspicious ML Model Access
  desc: Detect unusual model artifact access
  condition: >
    open_read and
    container and
    fd.name startswith "/models/" and
    not proc.name in (tritonserver, python)
  output: >
    Suspicious model access (user=%user.name command=%proc.cmdline file=%fd.name)
  priority: WARNING
```

---

## 8. Incident Response

### 8.1 Security Incident Types

| Type | Severity | Response Time |
|------|----------|---------------|
| Data breach | Critical | 15 minutes |
| Unauthorized access | High | 30 minutes |
| Model tampering | High | 30 minutes |
| Credential exposure | High | 1 hour |
| Vulnerability discovered | Medium | 24 hours |

### 8.2 Incident Response Procedure

1. **Detection** - Alert triggered
2. **Triage** - Assess severity
3. **Containment** - Isolate affected systems
4. **Investigation** - Determine root cause
5. **Remediation** - Fix vulnerability
6. **Recovery** - Restore services
7. **Post-mortem** - Document lessons learned

---

## 9. Security Checklist

### Pre-Deployment Security Checklist

| Category | Item | Status |
|----------|------|--------|
| **Authentication** | SSO/OIDC configured |  |
| | MFA enabled |  |
| | Service accounts secured |  |
| **Authorization** | RBAC implemented |  |
| | Least privilege verified |  |
| **Network** | Network policies applied |  |
| | mTLS enabled |  |
| **Data** | Encryption at rest |  |
| | Encryption in transit |  |
| **Secrets** | Vault integration |  |
| | No hardcoded secrets |  |
| **Audit** | Logging enabled |  |
| | Log retention configured |  |
| **Scanning** | Vulnerability scan passed |  |
| | Dependency scan passed |  |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial architecture |

---

## Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Security Architect | | | |
| ML Platform Lead | | | |
| CISO | | | |
