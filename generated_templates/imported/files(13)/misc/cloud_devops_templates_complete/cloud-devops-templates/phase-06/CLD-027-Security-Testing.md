---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-027: Cloud Security Testing

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-027 |
| **Version** | 1.0 |
| **Owner** | [Security Engineer] |

---

## 1. Security Testing Types

| Type | Tool | Frequency |
|------|------|-----------|
| IaC Scanning | Checkov, tfsec | Every PR |
| Vulnerability Scanning | Trivy, Inspector | Daily |
| Penetration Testing | Manual + tools | Annually |
| Compliance Audit | AWS Config | Continuous |

---

## 2. Vulnerability Scanning

### 2.1 Container Scanning
```yaml
# CI Pipeline
- name: Trivy Scan
  run: |
    trivy image --severity HIGH,CRITICAL \
      --exit-code 1 \
      ${{ env.IMAGE }}:${{ env.TAG }}
```

### 2.2 Infrastructure Scanning
```bash
# AWS Inspector scan
aws inspector2 list-findings \
  --filter-criteria '{"severity":[{"comparison":"EQUALS","value":"CRITICAL"}]}'
```

---

## 3. Compliance Checks

| Standard | Check | Tool |
|----------|-------|------|
| CIS Benchmarks | All | AWS Security Hub |
| PCI-DSS | Network isolation | AWS Config |
| SOC 2 | Access logging | CloudTrail |

---

## 4. Remediation SLAs

| Severity | SLA | Escalation |
|----------|-----|------------|
| Critical | 24 hours | Immediate |
| High | 7 days | Security Lead |
| Medium | 30 days | Team Lead |
| Low | 90 days | Backlog |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial security testing |
