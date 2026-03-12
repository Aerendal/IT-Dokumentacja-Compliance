---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-076: Secrets Management for MLOps

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-076 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [Security / ML Platform Lead] |

---

## 1. Secrets Categories

### 1.1 Secret Types

| Category | Examples | Rotation |
|----------|----------|----------|
| API Keys | MLflow, cloud providers | 90 days |
| Database Credentials | PostgreSQL, Redis | 90 days |
| Service Accounts | K8s, GCP, AWS | 365 days |
| Certificates | TLS, mTLS | 365 days |
| Encryption Keys | KMS, data encryption | 365 days |

### 1.2 Secret Locations

| Environment | Secret Store | Access Method |
|-------------|--------------|---------------|
| Development | Local .env (gitignored) | Direct read |
| CI/CD | GitHub Secrets | Environment variables |
| Kubernetes | K8s Secrets + Vault | Volume mount / env |
| Production | HashiCorp Vault | Vault Agent |

---

## 2. HashiCorp Vault Setup

### 2.1 Vault Configuration

```hcl
# vault/config.hcl
storage "postgresql" {
  connection_url = "postgres://vault:password@postgres:5432/vault"
}

listener "tcp" {
  address     = "0.0.0.0:8200"
  tls_disable = false
  tls_cert_file = "/vault/certs/vault.crt"
  tls_key_file  = "/vault/certs/vault.key"
}

api_addr = "https://vault.mlops.svc:8200"
cluster_addr = "https://vault.mlops.svc:8201"

ui = true

seal "awskms" {
  region     = "us-west-2"
  kms_key_id = "alias/vault-unseal"
}
```

### 2.2 Secrets Engine Setup

```bash
#!/bin/bash
# vault/setup_secrets.sh

# Enable KV secrets engine for MLOps
vault secrets enable -path=mlops kv-v2

# Create MLOps secrets structure
vault kv put mlops/mlflow \
    tracking_uri="postgresql://mlflow:pass@db:5432/mlflow" \
    artifact_root="s3://mlops-artifacts"

vault kv put mlops/feast \
    redis_host="redis.mlops.svc" \
    redis_password="secret" \
    offline_store_conn="postgresql://feast:pass@db:5432/feast"

vault kv put mlops/model-serving \
    s3_access_key="AKIAXXXXXXXX" \
    s3_secret_key="secret"

# Enable database secrets engine
vault secrets enable database

vault write database/config/mlflow-db \
    plugin_name=postgresql-database-plugin \
    connection_url="postgresql://{{username}}:{{password}}@db:5432/mlflow" \
    allowed_roles="mlflow-role" \
    username="vault_admin" \
    password="admin_password"
```

---

## 3. Kubernetes Integration

### 3.1 External Secrets Operator

```yaml
# k8s/external-secret.yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: mlflow-secrets
  namespace: mlops
spec:
  refreshInterval: 1h
  secretStoreRef:
    kind: ClusterSecretStore
    name: vault-backend
  target:
    name: mlflow-credentials
    creationPolicy: Owner
  data:
    - secretKey: MLFLOW_TRACKING_URI
      remoteRef:
        key: mlops/mlflow
        property: tracking_uri
    - secretKey: AWS_ACCESS_KEY_ID
      remoteRef:
        key: mlops/model-serving
        property: s3_access_key
    - secretKey: AWS_SECRET_ACCESS_KEY
      remoteRef:
        key: mlops/model-serving
        property: s3_secret_key
```

### 3.2 Vault Agent Injector

```yaml
# k8s/deployment-with-vault.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mlflow
  namespace: mlops
spec:
  template:
    metadata:
      annotations:
        vault.hashicorp.com/agent-inject: "true"
        vault.hashicorp.com/role: "mlflow"
        vault.hashicorp.com/agent-inject-secret-config: "mlops/mlflow"
        vault.hashicorp.com/agent-inject-template-config: |
          {{- with secret "mlops/mlflow" -}}
          export MLFLOW_TRACKING_URI="{{ .Data.data.tracking_uri }}"
          export ARTIFACT_ROOT="{{ .Data.data.artifact_root }}"
          {{- end -}}
    spec:
      serviceAccountName: mlflow
      containers:
        - name: mlflow
          image: mlflow/mlflow:latest
          command: ["/bin/sh", "-c"]
          args:
            - source /vault/secrets/config && mlflow server
```

---

## 4. Secret Rotation

### 4.1 Automated Rotation Policy

```python
# secrets/rotation.py
from datetime import datetime, timedelta
import hvac

class SecretRotator:
    """Automated secret rotation."""
    
    ROTATION_POLICIES = {
        'api_keys': timedelta(days=90),
        'database': timedelta(days=90),
        'certificates': timedelta(days=365),
    }
    
    def __init__(self, vault_addr: str, vault_token: str):
        self.client = hvac.Client(url=vault_addr, token=vault_token)
    
    def check_rotation_needed(self, secret_path: str, secret_type: str) -> bool:
        """Check if secret needs rotation."""
        secret = self.client.secrets.kv.v2.read_secret_version(path=secret_path)
        
        created_time = datetime.fromisoformat(
            secret['data']['metadata']['created_time'].replace('Z', '+00:00')
        )
        
        max_age = self.ROTATION_POLICIES.get(secret_type, timedelta(days=90))
        return datetime.now(created_time.tzinfo) - created_time > max_age
    
    def rotate_database_credentials(self, db_name: str):
        """Rotate database credentials."""
        # Generate new credentials via Vault database engine
        new_creds = self.client.secrets.database.generate_credentials(
            name=f"{db_name}-role"
        )
        
        # Update applications (this triggers rolling restart)
        # Applications should be configured to reload on secret change
        
        return new_creds
```

### 4.2 Rotation Schedule

```yaml
# k8s/secret-rotation-cronjob.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: secret-rotation-check
  namespace: mlops
spec:
  schedule: "0 0 * * 0"  # Weekly
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: rotator
            image: mlops/secret-rotator:latest
            command: ["python", "-m", "secrets.rotation", "--check-all"]
            env:
            - name: VAULT_ADDR
              value: "https://vault.mlops.svc:8200"
          restartPolicy: OnFailure
```

---

## 5. Access Control

### 5.1 Vault Policies

```hcl
# vault/policies/mlflow.hcl
path "mlops/data/mlflow" {
  capabilities = ["read"]
}

path "mlops/data/model-serving" {
  capabilities = ["read"]
}

path "database/creds/mlflow-role" {
  capabilities = ["read"]
}

# vault/policies/admin.hcl
path "mlops/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

path "sys/policies/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}
```

### 5.2 Kubernetes Auth

```bash
# Configure Kubernetes auth method
vault auth enable kubernetes

vault write auth/kubernetes/config \
    kubernetes_host="https://$KUBERNETES_PORT_443_TCP_ADDR:443"

vault write auth/kubernetes/role/mlflow \
    bound_service_account_names=mlflow \
    bound_service_account_namespaces=mlops \
    policies=mlflow \
    ttl=1h
```

---

## 6. Secret Audit

### 6.1 Audit Logging

```hcl
# vault/audit.hcl
audit {
  file {
    path = "file"
    file_path = "/vault/logs/audit.log"
    log_raw = false
  }
}
```

### 6.2 Secret Access Report

```sql
-- Query Vault audit logs
SELECT 
    timestamp,
    auth_entity_id,
    request_path,
    request_operation,
    response_error
FROM vault_audit_logs
WHERE request_path LIKE 'mlops/%'
    AND timestamp > NOW() - INTERVAL '7 days'
ORDER BY timestamp DESC;
```

---

## 7. Best Practices

### 7.1 Do's and Don'ts

|  Do |  Don't |
|-------|---------|
| Use Vault for all secrets | Hardcode secrets in code |
| Rotate regularly | Use same secret across envs |
| Audit secret access | Share secrets via Slack/email |
| Use short-lived tokens | Store secrets in Git |
| Encrypt at rest | Use default/weak passwords |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial secrets management |
