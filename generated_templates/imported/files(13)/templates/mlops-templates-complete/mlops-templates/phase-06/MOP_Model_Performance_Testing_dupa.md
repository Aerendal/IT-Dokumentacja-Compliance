---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# MOP-075: Model Performance Testing

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | MOP-075 |
| **Version** | 1.0 |
| **Status** | ACTIVE |
| **Owner** | [ML QA Lead] |

---

## 1. Performance Testing Overview

### 1.1 Test Types

| Test Type | Purpose | Frequency |
|-----------|---------|-----------|
| Load Test | Validate throughput capacity | Pre-deployment |
| Stress Test | Find breaking point | Quarterly |
| Endurance Test | Validate long-running stability | Monthly |
| Spike Test | Handle sudden traffic increases | Pre-deployment |
| Latency Test | Validate response times | Every deployment |

### 1.2 Performance Requirements

| Metric | Target | Critical |
|--------|--------|----------|
| P50 Latency | <30ms | <50ms |
| P99 Latency | <100ms | <200ms |
| Throughput | >1000 RPS | >500 RPS |
| Error Rate | <0.1% | <1% |
| Cold Start | <5s | <10s |

---

## 2. Load Testing

### 2.1 Locust Load Test

```python
# performance_tests/load_test.py
from locust import HttpUser, task, between
import json
import random

class ModelLoadTest(HttpUser):
    """Load test for model inference endpoint."""
    
    wait_time = between(0.1, 0.5)
    
    def on_start(self):
        """Setup test data."""
        self.test_payloads = self._generate_payloads(100)
    
    def _generate_payloads(self, count: int) -> list:
        """Generate realistic test payloads."""
        payloads = []
        for _ in range(count):
            payloads.append({
                "inputs": [{
                    "name": "input",
                    "shape": [1, 50],
                    "datatype": "FP32",
                    "data": [random.random() for _ in range(50)]
                }]
            })
        return payloads
    
    @task(10)
    def predict_single(self):
        """Single prediction request."""
        payload = random.choice(self.test_payloads)
        
        with self.client.post(
            "/v2/models/fraud-model/infer",
            json=payload,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                data = response.json()
                if "outputs" in data:
                    response.success()
                else:
                    response.failure("Invalid response format")
            else:
                response.failure(f"Status: {response.status_code}")
    
    @task(2)
    def predict_batch(self):
        """Batch prediction request."""
        batch_payload = {
            "inputs": [{
                "name": "input",
                "shape": [10, 50],  # Batch of 10
                "datatype": "FP32",
                "data": [[random.random() for _ in range(50)] for _ in range(10)]
            }]
        }
        
        self.client.post("/v2/models/fraud-model/infer", json=batch_payload)
    
    @task(1)
    def health_check(self):
        """Health check endpoint."""
        self.client.get("/v2/health/ready")
```

### 2.2 Load Test Execution

```bash
#!/bin/bash
# performance_tests/run_load_test.sh

MODEL_ENDPOINT=$1
USERS=${2:-100}
SPAWN_RATE=${3:-10}
DURATION=${4:-300}  # 5 minutes

echo "=== Running Load Test ==="
echo "Endpoint: $MODEL_ENDPOINT"
echo "Users: $USERS"
echo "Duration: ${DURATION}s"

locust -f performance_tests/load_test.py \
    --host=$MODEL_ENDPOINT \
    --users=$USERS \
    --spawn-rate=$SPAWN_RATE \
    --run-time=${DURATION}s \
    --headless \
    --csv=results/load_test_$(date +%Y%m%d_%H%M%S) \
    --html=results/load_test_report.html

echo "=== Load Test Complete ==="
```

---

## 3. Latency Testing

### 3.1 Latency Benchmarking

```python
# performance_tests/latency_test.py
import requests
import time
import statistics
from dataclasses import dataclass
from typing import List

@dataclass
class LatencyResult:
    p50: float
    p90: float
    p95: float
    p99: float
    mean: float
    min: float
    max: float
    samples: int

def benchmark_latency(
    endpoint: str,
    payload: dict,
    num_requests: int = 1000,
    warmup_requests: int = 100
) -> LatencyResult:
    """Benchmark inference latency."""
    
    # Warmup
    print(f"Warming up with {warmup_requests} requests...")
    for _ in range(warmup_requests):
        requests.post(endpoint, json=payload)
    
    # Benchmark
    latencies: List[float] = []
    print(f"Running {num_requests} benchmark requests...")
    
    for i in range(num_requests):
        start = time.perf_counter()
        response = requests.post(endpoint, json=payload)
        end = time.perf_counter()
        
        if response.status_code == 200:
            latencies.append((end - start) * 1000)  # Convert to ms
        
        if (i + 1) % 100 == 0:
            print(f"  Completed {i + 1}/{num_requests}")
    
    # Calculate percentiles
    sorted_latencies = sorted(latencies)
    n = len(sorted_latencies)
    
    return LatencyResult(
        p50=sorted_latencies[int(n * 0.50)],
        p90=sorted_latencies[int(n * 0.90)],
        p95=sorted_latencies[int(n * 0.95)],
        p99=sorted_latencies[int(n * 0.99)],
        mean=statistics.mean(sorted_latencies),
        min=min(sorted_latencies),
        max=max(sorted_latencies),
        samples=n
    )

def validate_latency(result: LatencyResult, requirements: dict) -> bool:
    """Validate latency against requirements."""
    passed = True
    
    if result.p50 > requirements.get('p50', float('inf')):
        print(f" P50 {result.p50:.2f}ms exceeds {requirements['p50']}ms")
        passed = False
    else:
        print(f" P50 {result.p50:.2f}ms")
    
    if result.p99 > requirements.get('p99', float('inf')):
        print(f" P99 {result.p99:.2f}ms exceeds {requirements['p99']}ms")
        passed = False
    else:
        print(f" P99 {result.p99:.2f}ms")
    
    return passed
```

---

## 4. Stress Testing

### 4.1 Stress Test Configuration

```python
# performance_tests/stress_test.py
from locust import HttpUser, task, events
from locust.runners import MasterRunner

class StressTest(HttpUser):
    """Stress test to find breaking point."""
    
    @task
    def predict(self):
        payload = self._generate_payload()
        self.client.post("/v2/models/fraud-model/infer", json=payload)

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    """Report stress test results."""
    stats = environment.stats.total
    
    print("\n=== Stress Test Results ===")
    print(f"Max RPS achieved: {stats.current_rps:.0f}")
    print(f"Total requests: {stats.num_requests}")
    print(f"Failure rate: {stats.fail_ratio * 100:.2f}%")
    print(f"P99 latency: {stats.get_response_time_percentile(0.99):.0f}ms")
    
    # Determine breaking point
    if stats.fail_ratio > 0.01:  # >1% error rate
        print(f"\n Breaking point reached at ~{stats.current_rps:.0f} RPS")
```

### 4.2 Run Stress Test

```bash
# Gradually increase load to find breaking point
locust -f performance_tests/stress_test.py \
    --host=https://model.example.com \
    --users=500 \
    --spawn-rate=10 \
    --run-time=600s \
    --step-load \
    --step-users=50 \
    --step-time=60s
```

---

## 5. Profiling

### 5.1 Model Profiling

```python
# performance_tests/profile_model.py
import cProfile
import pstats
import io
import time

def profile_inference(model, sample_input, num_iterations: int = 1000):
    """Profile model inference."""
    
    # CPU profiling
    profiler = cProfile.Profile()
    
    profiler.enable()
    for _ in range(num_iterations):
        model.predict(sample_input)
    profiler.disable()
    
    # Generate report
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats('cumulative')
    stats.print_stats(20)
    
    print("=== Profiling Results ===")
    print(stream.getvalue())
    
    # Memory profiling (if tracemalloc available)
    import tracemalloc
    tracemalloc.start()
    
    for _ in range(100):
        model.predict(sample_input)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"\nMemory usage:")
    print(f"  Current: {current / 1024 / 1024:.2f} MB")
    print(f"  Peak: {peak / 1024 / 1024:.2f} MB")
```

---

## 6. Performance Test Report

### 6.1 Report Template

```markdown
# Model Performance Test Report

**Model:** [Model Name]
**Version:** [Version]
**Date:** [Date]
**Environment:** [staging/production]

## Summary
| Metric | Result | Target | Status |
|--------|--------|--------|--------|
| P50 Latency | Xms | <30ms | / |
| P99 Latency | Xms | <100ms | / |
| Max Throughput | X RPS | >1000 RPS | / |
| Error Rate | X% | <0.1% | / |

## Load Test Results
[Chart/Table of results]

## Latency Distribution
[Histogram]

## Recommendations
- [Recommendation 1]
- [Recommendation 2]

## Approval
- [ ] Performance acceptable for deployment
```

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial performance testing guide |
