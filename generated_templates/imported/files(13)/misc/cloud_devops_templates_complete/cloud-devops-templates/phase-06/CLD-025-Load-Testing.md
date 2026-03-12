---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-025: Cloud Load Testing

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-025 |
| **Version** | 1.0 |
| **Owner** | [QA / Performance Engineer] |

---

## 1. Load Test Configuration

### 1.1 k6 Test Script
```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '5m', target: 100 },   // Ramp up
    { duration: '10m', target: 100 },  // Steady state
    { duration: '5m', target: 200 },   // Peak load
    { duration: '5m', target: 0 },     // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],  // 95% under 500ms
    http_req_failed: ['rate<0.01'],    // <1% errors
  },
};

export default function () {
  const res = http.get('https://api.example.com/health');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });
  sleep(1);
}
```

---

## 2. Performance Targets

| Metric | Target | Critical |
|--------|--------|----------|
| Response Time (P95) | <500ms | <1000ms |
| Throughput | 1000 RPS | 500 RPS |
| Error Rate | <0.1% | <1% |
| CPU Utilization | <70% | <90% |

---

## 3. Test Scenarios

| Scenario | Users | Duration | Purpose |
|----------|-------|----------|---------|
| Baseline | 50 | 10 min | Normal load |
| Peak | 200 | 20 min | Expected peak |
| Stress | 500 | 30 min | Breaking point |
| Soak | 100 | 4 hours | Memory leaks |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial load testing |
