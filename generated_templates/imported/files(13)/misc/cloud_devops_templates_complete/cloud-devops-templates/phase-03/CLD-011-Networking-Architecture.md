---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# CLD-011: Cloud Networking Architecture

## Document Metadata
| Field | Value |
|-------|-------|
| **Document ID** | CLD-011 |
| **Version** | 1.0 |
| **Owner** | [Network Architect / Cloud Architect] |

---

## 1. Network Design Overview

### 1.1 VPC Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     Production VPC: 10.0.0.0/16                          │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │                        AZ-a (10.0.0.0/18)                          │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐               │ │
│  │  │ Public      │  │ Private     │  │ Data        │               │ │
│  │  │ 10.0.0.0/22 │  │ 10.0.16.0/20│  │ 10.0.32.0/21│               │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘               │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │                        AZ-b (10.0.64.0/18)                         │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐               │ │
│  │  │ Public      │  │ Private     │  │ Data        │               │ │
│  │  │ 10.0.64.0/22│  │ 10.0.80.0/20│  │ 10.0.96.0/21│               │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘               │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │                        AZ-c (10.0.128.0/18)                        │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐               │ │
│  │  │ Public      │  │ Private     │  │ Data        │               │ │
│  │  │10.0.128.0/22│  │10.0.144.0/20│  │10.0.160.0/21│               │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘               │ │
│  └───────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────┘
```

### 1.2 IP Address Plan

| Environment | VPC CIDR | Available IPs |
|-------------|----------|---------------|
| Production | 10.0.0.0/16 | 65,536 |
| Staging | 10.1.0.0/16 | 65,536 |
| Development | 10.2.0.0/16 | 65,536 |
| Management | 10.3.0.0/16 | 65,536 |

---

## 2. Connectivity

### 2.1 Internet Connectivity

| Component | Configuration |
|-----------|---------------|
| Internet Gateway | 1 per VPC |
| NAT Gateway | 1 per AZ (HA) |
| Egress Only | IPv6 traffic |

### 2.2 Hybrid Connectivity

| Connection | Type | Bandwidth | Redundancy |
|------------|------|-----------|------------|
| On-Premise | Direct Connect | 1 Gbps | 2 connections |
| Backup | Site-to-Site VPN | 1.25 Gbps | 2 tunnels |

### 2.3 Cross-VPC Connectivity

| Pattern | Use Case | Implementation |
|---------|----------|----------------|
| VPC Peering | Low traffic | Direct peering |
| Transit Gateway | Hub-and-spoke | Centralized routing |
| PrivateLink | Service access | Endpoint services |

---

## 3. DNS Design

| Zone | Type | Purpose |
|------|------|---------|
| company.com | Public | External services |
| internal.company.com | Private | Internal services |
| *.region.internal | Private | Service discovery |

---

## 4. Load Balancing

| Type | Use Case | Features |
|------|----------|----------|
| ALB | HTTP/HTTPS | Path routing, WAF |
| NLB | TCP/UDP | Low latency, static IP |
| GLB | Cross-region | Global anycast |

---

## 5. Security

### 5.1 Network ACLs

| Rule | Direction | CIDR | Port | Action |
|------|-----------|------|------|--------|
| 100 | Inbound | 0.0.0.0/0 | 443 | Allow |
| 110 | Inbound | 10.0.0.0/8 | All | Allow |
| * | Inbound | 0.0.0.0/0 | All | Deny |

### 5.2 VPC Flow Logs

| Destination | Retention | Filter |
|-------------|-----------|--------|
| CloudWatch Logs | 30 days | All traffic |
| S3 | 1 year | Rejected only |

---

## Document History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author] | Initial network design |
