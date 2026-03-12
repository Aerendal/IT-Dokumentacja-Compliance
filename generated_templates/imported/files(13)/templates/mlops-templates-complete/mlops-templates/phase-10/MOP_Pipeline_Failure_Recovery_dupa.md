---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-036: Pipeline Failure Recovery

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-036 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [MLOps SRE] |

---

## 1. Failure Categories

| Category | Examples | Severity |
|----------|----------|----------|
| Infrastructure | Node failure, storage unavailable | High |
| Data | Missing data, schema mismatch, corruption | High |
| Resource | OOM, timeout, quota exceeded | Medium |
| Code | Bug, dependency issue | Medium |
| External | API failure, network issue | Medium |

---

## 2. Diagnosis Procedures

### 2.1 Quick Diagnosis Script

```bash
#!/bin/bash
# recovery/diagnose_pipeline.sh

PIPELINE_NAME=$1
RUN_ID=$2

echo "=== Pipeline Failure Diagnosis ==="
echo "Pipeline: $PIPELINE_NAME"
echo "Run ID: $RUN_ID"

# 1. Check pipeline status
echo -e "\n[1/5] Pipeline Status:"
kubectl get pods -l pipeline=$PIPELINE_NAME -o wide

# 2. Get failed task
echo -e "\n[2/5] Failed Tasks:"
kubectl get pods -l pipeline=$PIPELINE_NAME --field-selector=status.phase=Failed

# 3. Check logs
echo -e "\n[3/5] Recent Logs:"
kubectl logs -l pipeline=$PIPELINE_NAME --tail=50 --all-containers

# 4. Check events
echo -e "\n[4/5] Events:"
kubectl get events --field-selector involvedObject.name=$PIPELINE_NAME --sort-by='.lastTimestamp'

# 5. Resource status
echo -e "\n[5/5] Resource Usage:"
kubectl top pods -l pipeline=$PIPELINE_NAME

echo -e "\n=== Diagnosis Complete ==="
```

### 2.2 Common Failure Patterns

| Pattern | Indicators | Likely Cause |
|---------|------------|--------------|
| OOMKilled | Exit code 137, OOMKilled in events | Insufficient memory |
| Timeout | Deadline exceeded, context cancelled | Task too slow or stuck |
| ImagePull | ImagePullBackOff status | Image not found or auth issue |
| CrashLoop | CrashLoopBackOff, multiple restarts | Code bug or missing config |
| Pending | Pod stuck in Pending | Resource constraints |

---

## 3. Recovery Procedures

### 3.1 Retry Failed Task

```bash
#!/bin/bash
# recovery/retry_task.sh

PIPELINE=$1
TASK=$2

echo "Retrying task $TASK in pipeline $PIPELINE"

# For Airflow
airflow tasks clear $PIPELINE $TASK --yes

# For Kubeflow
# Rerun from failed step
kfp run retry $RUN_ID
```

### 3.2 Resume from Checkpoint

```python
# recovery/resume_pipeline.py
import mlflow
from kfp import Client

def resume_from_checkpoint(run_id: str):
    """Resume pipeline from last successful checkpoint."""
    client = Client()
    
    # Get run details
    run = client.get_run(run_id)
    
    # Find last successful step
    last_success = None
    for node in run.pipeline_runtime.workflow_manifest['status']['nodes'].values():
        if node['phase'] == 'Succeeded':
            last_success = node['displayName']
    
    print(f"Last successful step: {last_success}")
    
    # Rerun from next step
    if last_success:
        client.run_pipeline(
            experiment_id=run.experiment_id,
            job_name=f"{run.name}-retry",
            pipeline_id=run.pipeline_id,
            params={'resume_from': last_success}
        )
```

### 3.3 Data Recovery

```python
# recovery/data_recovery.py
def recover_from_data_failure(pipeline_run_id: str):
    """Recover from data-related failures."""
    
    # 1. Identify data issue
    run_info = get_run_info(pipeline_run_id)
    data_path = run_info['params']['data_path']
    
    # 2. Check data availability
    if not check_data_exists(data_path):
        # Try to restore from backup
        backup_path = find_latest_backup(data_path)
        if backup_path:
            restore_data(backup_path, data_path)
            print(f"Restored data from {backup_path}")
        else:
            raise Exception("No backup available")
    
    # 3. Validate data
    validation_result = validate_data(data_path)
    if not validation_result.passed:
        print(f"Data validation failed: {validation_result.errors}")
        # Attempt data repair
        repair_data(data_path, validation_result.errors)
    
    # 4. Retry pipeline
    retry_pipeline(pipeline_run_id)
```

---

## 4. Failure-Specific Playbooks

### 4.1 OOM Failure

```markdown
## OOM Failure Recovery

**Symptoms:**
- Exit code 137
- OOMKilled in pod events
- "Killed" in logs

**Recovery Steps:**

1. **Immediate:** Increase memory limit
   ```bash
   kubectl patch deployment $DEPLOYMENT -p \
     '{"spec":{"template":{"spec":{"containers":[{"name":"main","resources":{"limits":{"memory":"8Gi"}}}]}}}}'
   ```

2. **Retry:** Restart the failed task
   ```bash
   airflow tasks clear $DAG $TASK --yes
   ```

3. **Long-term:** 
   - Profile memory usage
   - Optimize code or use chunking
   - Consider distributed processing
```

### 4.2 Data Schema Mismatch

```markdown
## Schema Mismatch Recovery

**Symptoms:**
- "Column not found" errors
- "Type mismatch" errors
- Great Expectations validation failures

**Recovery Steps:**

1. **Identify:** Compare schemas
   ```python
   expected_schema = load_schema('expected_schema.json')
   actual_schema = infer_schema(data_path)
   diff = compare_schemas(expected_schema, actual_schema)
   ```

2. **Fix Options:**
   - Update pipeline to handle new schema
   - Transform data to match expected schema
   - Update expected schema if change is valid

3. **Retry:** Clear cache and retry
   ```bash
   # Clear any cached schemas
   rm -rf /tmp/schema_cache/
   airflow tasks clear $DAG $TASK --yes
   ```
```

### 4.3 External API Failure

```markdown
## External API Failure Recovery

**Symptoms:**
- Connection timeout
- HTTP 5xx errors
- Rate limit errors (429)

**Recovery Steps:**

1. **Check:** Verify external service status
   ```bash
   curl -I https://external-api.com/health
   ```

2. **If rate limited:** Wait and retry with backoff
   ```python
   from tenacity import retry, wait_exponential
   
   @retry(wait=wait_exponential(multiplier=1, max=60))
   def call_api():
       return requests.get(API_URL)
   ```

3. **If service down:** 
   - Use cached data if available
   - Switch to backup service
   - Wait for service recovery
```

---

## 5. Automated Recovery

### 5.1 Auto-Retry Configuration

```yaml
# airflow/dag_config.yaml
default_args:
  retries: 3
  retry_delay: timedelta(minutes=5)
  retry_exponential_backoff: true
  max_retry_delay: timedelta(minutes=30)

# Task-specific overrides
tasks:
  data_fetch:
    retries: 5  # More retries for external data
  training:
    retries: 2  # Fewer retries for expensive tasks
```

### 5.2 Self-Healing Pipeline

```python
# recovery/self_healing.py
class SelfHealingPipeline:
    """Pipeline with automatic failure recovery."""
    
    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.recovery_strategies = {
            'OOMKilled': self.handle_oom,
            'ImagePullBackOff': self.handle_image_pull,
            'Timeout': self.handle_timeout,
        }
    
    def on_failure(self, task_id: str, error: str):
        """Handle task failure."""
        failure_type = self.classify_failure(error)
        
        if failure_type in self.recovery_strategies:
            strategy = self.recovery_strategies[failure_type]
            if strategy(task_id):
                self.retry_task(task_id)
                return
        
        # Escalate if no auto-recovery
        self.alert_oncall(task_id, error)
    
    def handle_oom(self, task_id: str) -> bool:
        """Handle OOM by increasing memory."""
        current_memory = self.get_task_memory(task_id)
        new_memory = min(current_memory * 2, MAX_MEMORY)
        
        if new_memory > current_memory:
            self.update_task_memory(task_id, new_memory)
            return True
        return False
```

---

## 6. Recovery Metrics

| Metric | Target | Description |
|--------|--------|-------------|
| MTTR | <30 min | Mean time to recover |
| Auto-recovery rate | >80% | % failures auto-recovered |
| Manual intervention rate | <20% | % requiring human action |
| Repeat failure rate | <5% | Same failure recurring |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial recovery procedures |
