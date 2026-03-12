---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# QA-112: Infrastructure Sizing Guide
## DOCUMENT METADATA
| Attribute | Value |
|-----------|-------|
| **Document ID** | QA-112 |
| **Owner** | QA Manager |
---
## 1. SIZING GUIDELINES
| Component | Small | Medium | Large |
|-----------|-------|--------|-------|
| Test env | 2 CPU, 4GB | 4 CPU, 8GB | 8 CPU, 16GB |
| Selenium Grid | 5 nodes | 10 nodes | 20 nodes |
## 2. SCALING TRIGGERS
| Trigger | Action |
|---------|--------|
| >50 parallel tests | Add nodes |
| Response >2s | Upgrade env |
---
## APPROVAL
| Role | Name | Date |
|------|------|------|
| QA Manager | | |
