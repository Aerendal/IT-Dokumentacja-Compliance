---
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# DATA SCIENCE / ANALYTICS DOCUMENTATION MATRIX - CONTEXT REPORT
> Generated: 2026-01-31 08:19:51
> System Version: 1.0.0
> Industry: Data Science / Analytics (Industry #5)

## OVERVIEW

This documentation matrix system provides a comprehensive framework for managing Data Science and Analytics documentation across 23 phases of the documentation lifecycle. It incorporates 2024-2025 standards including modern BI tools, Python data science ecosystem, statistical methods, and analytics best practices.

## DATABASE STATISTICS

| Metric | Count |
|--------|-------|
| Total Documents | 107 |
| Lifecycle Phases | 23 |
| Document Relationships | 25 |
| BI Tools | 12 |
| Python Libraries | 15 |
| Statistical Tests | 16 |
| Analysis Methods | 15 |
| Visualization Types | 15 |
| Quality Dimensions | 8 |
| Analysis Metrics | 15 |
| Notebook Environments | 10 |

## PHASES OVERVIEW

| Phase | Name | Documents | Description |
|-------|------|-----------|-------------|
| 1 | Concept & Vision | 3 | Define analytics strategy and problem statements... |
| 2 | Requirements Analysis | 4 | Gather data and stakeholder requirements... |
| 3 | Design | 5 | Design analytics approach and methodology... |
| 4 | Planning | 3 | Plan project timeline and iterations... |
| 5 | Implementation | 5 | Execute data preparation and analysis... |
| 6 | Testing / QA | 4 | Validate analysis results and reproducibility... |
| 7 | Security / Compliance | 3 | Ensure data privacy and audit compliance... |
| 8 | Deployment | 3 | Deploy dashboards and reports... |
| 9 | Operations / Maintenance | 3 | Maintain dashboards and data refreshes... |
| 10 | Incident Management | 3 | Handle incorrect results and data quality issues... |
| 11 | Monitoring / Observability | 3 | Monitor dashboard performance and usage... |
| 12 | Reference Documentation | 4 | Document methodology and metrics... |
| 13 | Training / Onboarding | 4 | Train analysts and business users... |
| 14 | Stakeholder Communication | 4 | Communicate insights and recommendations... |
| 15 | Knowledge Management | 4 | Capture best practices and patterns... |
| 16 | Postmortem / Retrospective | 3 | Review project outcomes and lessons learned... |
| 17 | Budgeting / Cost Management | 6 | Manage analytics project budgets... |
| 18 | Vendor / Procurement | 7 | Manage tool vendors and procurement... |
| 19 | Governance / Compliance Auditing | 7 | Audit analytics governance and compliance... |
| 20 | Decommissioning / End-of-Life | 7 | Retire analytics assets and dashboards... |
| 21 | Disaster Recovery / BCP | 8 | Plan for analytics continuity... |
| 22 | Change Management | 7 | Manage changes to analytics systems... |
| 23 | Capacity Planning | 7 | Plan for analytics growth and resources... |


## CRITICAL DOCUMENTS

| Code | Title | Priority |
|------|-------|----------|
| DS-AAD | Analytics Approach Document |  CRITICAL |
| DS-ADG | Analytics Deployment Guide |  CRITICAL |
| DS-AMD | Analysis Methodology Document |  CRITICAL |
| DS-APL | Analysis Plan |  CRITICAL |
| DS-AVP | Analysis Validation Plan |  CRITICAL |
| DS-BCP | Business Continuity Plan |  CRITICAL |
| DS-DDR | Data-Driven Recommendations |  CRITICAL |
| DS-DPA | Data Privacy in Analysis |  CRITICAL |
| DS-DPP | Data Preparation Procedure |  CRITICAL |
| DS-DRA | Data Requirements for Analysis |  CRITICAL |
| DS-DRE | Disaster Recovery Plan |  CRITICAL |
| DS-EDA | Exploratory Data Analysis Report |  CRITICAL |
| DS-ESR | Executive Summary Report |  CRITICAL |
| DS-MTD | Metric Definitions |  CRITICAL |
| DS-PSD | Problem Statement for Analytics |  CRITICAL |
| DS-SDH | Sensitive Data Handling |  CRITICAL |
| DS-STR | Analytics Strategy Document |  CRITICAL |


## BI TOOLS (12)

| Tool | Vendor | Type | Best For |
|------|--------|------|----------|
| Apache Superset | Apache | Open-Source | Enterprise open-source BI... |
| Domo | Domo | Enterprise | Executive dashboards... |
| Holistics | Holistics | Enterprise | Dashboard as code... |
| Looker | Google | Enterprise | Data governance, LookML modeling... |
| Looker Studio | Google | Free | Marketing teams, Google ecosystem... |
| Metabase | Metabase | Open-Source | Startups, simple BI... |
| Mode | ThoughtSpot | Enterprise | Data teams, SQL notebooks... |
| Power BI | Microsoft | Enterprise | Microsoft ecosystem, SMB... |
| Qlik Sense | Qlik | Enterprise | Associative analytics... |
| Sigma | Sigma Computing | Enterprise | Spreadsheet-like interface... |
| Tableau | Salesforce | Enterprise | Complex visualizations, executive d... |
| ThoughtSpot | ThoughtSpot | Enterprise | Self-service search analytics... |


## PYTHON LIBRARIES (15)

| Library | Category | Best For | Performance |
|---------|----------|----------|-------------|
| Altair | Visualization | Declarative visualizations... | N/A |
| Bokeh | Visualization | Interactive dashboards... | N/A |
| Dask | Data Processing | Parallel/distributed computing... | Scales to clusters |
| Matplotlib | Visualization | Static plots, publication qual... | N/A |
| NumPy | Numerical | Numerical computing, arrays... | N/A |
| Pingouin | Statistical | Statistical tests with pandas... | N/A |
| Plotly | Visualization | Interactive web visualizations... | N/A |
| Polars | Data Processing | Large datasets (10GB+), perfor... | 10-50x faster |
| PyArrow | Data Processing | Columnar data, interop... | Very fast I/O |
| SciPy | Statistical | Scientific computing, optimiza... | N/A |
| Seaborn | Visualization | Statistical visualizations... | N/A |
| Vaex | Data Processing | Out-of-core processing... | Memory efficient |
| pandas | Data Processing | Small-medium datasets, stable ... | Baseline |
| scikit-learn | ML | Classical ML, preprocessing... | N/A |
| statsmodels | Statistical | Statistical modeling, tests... | N/A |


## STATISTICAL TESTS (16)

| Test | Type | Use Case | Python Function |
|------|------|----------|------------------|
| Chi-square test | Non-parametric | Test categorical independ... | scipy.stats.chi2_contingency |
| Fisher exact test | Non-parametric | Test categorical independ... | scipy.stats.fisher_exact |
| Kolmogorov-Smirnov | Non-parametric | Compare to distribution... | scipy.stats.kstest |
| Kruskal-Wallis | Non-parametric | Compare multiple groups... | scipy.stats.kruskal |
| Levene test | Variance | Test equal variances... | scipy.stats.levene |
| Mann-Whitney U | Non-parametric | Compare two distributions... | scipy.stats.mannwhitneyu |
| One-sample t-test | Parametric | Compare sample mean to va... | scipy.stats.ttest_1samp |
| One-way ANOVA | Parametric | Compare multiple group me... | scipy.stats.f_oneway |
| Paired t-test | Parametric | Compare paired observatio... | scipy.stats.ttest_rel |
| Pearson correlation | Parametric | Linear correlation... | scipy.stats.pearsonr |
| Shapiro-Wilk | Normality | Test for normality... | scipy.stats.shapiro |
| Spearman correlation | Non-parametric | Monotonic correlation... | scipy.stats.spearmanr |
| Two-sample t-test | Parametric | Compare two group means... | scipy.stats.ttest_ind |
| Welch t-test | Parametric | Compare means, unequal va... | scipy.stats.ttest_ind(equal_var=False) |
| Wilcoxon signed-rank | Non-parametric | Compare paired observatio... | scipy.stats.wilcoxon |
| Z-test | Parametric | Compare sample mean to po... | statsmodels.stats.weightstats.ztest |


## ANALYSIS METHODS (15)

| Method | Category | Output | Complexity |
|--------|----------|--------|------------|
| A/B Testing | Inferential | Statistical significance | Medium |
| Causal Inference | Inferential | Treatment effects | High |
| Cohort Analysis | Descriptive | Retention charts | Medium |
| Descriptive Statistics | Descriptive | Summary tables | Low |
| Difference-in-Differences | Inferential | Effect estimates | High |
| Exploratory Data Analysis | Descriptive | Visualizations, insights | Medium |
| Factor Analysis | Descriptive | Factor loadings | High |
| Funnel Analysis | Descriptive | Funnel charts | Low |
| Hypothesis Testing | Inferential | P-values, conclusions | Medium |
| Propensity Score Matching | Inferential | Matched groups | High |
| RFM Analysis | Descriptive | Customer segments | Low |
| Regression Analysis | Inferential | Model coefficients, R² | Medium |
| Segmentation | Descriptive | Segment definitions | Medium |
| Survival Analysis | Predictive | Survival curves | High |
| Time Series Analysis | Predictive | Forecasts, trends | High |


## VISUALIZATION TYPES (15)

| Visualization | Category | Best For |
|---------------|----------|----------|
| Bar Chart | Comparison | Comparing categories |
| Box Plot | Distribution | Distribution comparison |
| Bullet Chart | Comparison | Performance vs target |
| Funnel Chart | Comparison | Conversion funnels |
| Geographic Map | Spatial | Location-based data |
| Heatmap | Relationship | Patterns in matrix data |
| Histogram | Distribution | Distribution of values |
| KPI Card | Summary | Key metrics display |
| Line Chart | Temporal | Trends over time |
| Pie Chart | Composition | Part-to-whole relationships |
| Sankey Diagram | Flow | Flow between nodes |
| Scatter Plot | Relationship | Correlation between variables |
| Sparkline | Temporal | Compact trends |
| Treemap | Composition | Hierarchical part-to-whole |
| Waterfall Chart | Composition | Cumulative effect |


## DOCUMENTS BY PHASE


### Phase 1: Concept & Vision

| Code | Title | Priority |
|------|-------|----------|
| DS-KQD | Key Questions Document |  HIGH |
| DS-PSD | Problem Statement for Analytics |  CRITICAL |
| DS-STR | Analytics Strategy Document |  CRITICAL |

### Phase 2: Requirements Analysis

| Code | Title | Priority |
|------|-------|----------|
| DS-ASD | Analysis Scope Definition |  HIGH |
| DS-DAA | Data Availability Assessment |  HIGH |
| DS-DRA | Data Requirements for Analysis |  CRITICAL |
| DS-SRQ | Stakeholder Requirements |  HIGH |

### Phase 3: Design

| Code | Title | Priority |
|------|-------|----------|
| DS-AAD | Analytics Approach Document |  CRITICAL |
| DS-APL | Analysis Plan |  CRITICAL |
| DS-HYP | Hypothesis Document |  HIGH |
| DS-SDS | Statistical Design Specification |  HIGH |
| DS-VZD | Visualization Design |  HIGH |

### Phase 4: Planning

| Code | Title | Priority |
|------|-------|----------|
| DS-ITP | Data Science Iteration Plan |  MEDIUM |
| DS-PTL | Project Timeline for Analysis |  HIGH |
| DS-SCP | Stakeholder Communication Plan |  MEDIUM |

### Phase 5: Implementation

| Code | Title | Priority |
|------|-------|----------|
| DS-DPP | Data Preparation Procedure |  CRITICAL |
| DS-EDA | Exploratory Data Analysis Report |  CRITICAL |
| DS-FES | Feature Engineering Specification |  HIGH |
| DS-SAC | Statistical Analysis Code |  HIGH |
| DS-VZC | Visualization Code |  MEDIUM |

### Phase 6: Testing / QA

| Code | Title | Priority |
|------|-------|----------|
| DS-AVP | Analysis Validation Plan |  CRITICAL |
| DS-PRV | Peer Review Process |  HIGH |
| DS-RPC | Reproducibility Checklist |  HIGH |
| DS-SST | Statistical Significance Testing |  HIGH |

### Phase 7: Security / Compliance

| Code | Title | Priority |
|------|-------|----------|
| DS-ATA | Audit Trail for Analysis |  HIGH |
| DS-DPA | Data Privacy in Analysis |  CRITICAL |
| DS-SDH | Sensitive Data Handling |  CRITICAL |

### Phase 8: Deployment

| Code | Title | Priority |
|------|-------|----------|
| DS-ADG | Analytics Deployment Guide |  CRITICAL |
| DS-DPU | Dashboard Publishing Procedure |  HIGH |
| DS-RDP | Report Distribution Plan |  HIGH |

### Phase 9: Operations / Maintenance

| Code | Title | Priority |
|------|-------|----------|
| DS-AMO | Analytics Monitoring |  MEDIUM |
| DS-DMS | Dashboard Maintenance Schedule |  HIGH |
| DS-DRP | Data Refresh Procedure |  HIGH |

### Phase 10: Incident Management

| Code | Title | Priority |
|------|-------|----------|
| DS-DQI | Data Quality Issues in Analysis |  HIGH |
| DS-IRI | Incorrect Results Investigation |  HIGH |
| DS-TGA | Troubleshooting Guide for Analytics |  MEDIUM |

### Phase 11: Monitoring / Observability

| Code | Title | Priority |
|------|-------|----------|
| DS-DFM | Data Freshness Monitoring |  HIGH |
| DS-DPM | Dashboard Performance Monitoring |  MEDIUM |
| DS-UEM | User Engagement Metrics |  MEDIUM |

### Phase 12: Reference Documentation

| Code | Title | Priority |
|------|-------|----------|
| DS-ACR | Analysis Code Repository |  HIGH |
| DS-AMD | Analysis Methodology Document |  CRITICAL |
| DS-DRG | Dashboard Reference Guide |  HIGH |
| DS-MTD | Metric Definitions |  CRITICAL |

### Phase 13: Training / Onboarding

| Code | Title | Priority |
|------|-------|----------|
| DS-AMT | Analysis Methodology Training |  MEDIUM |
| DS-BTR | BI Tool Training |  HIGH |
| DS-DAO | Data Analyst Onboarding |  HIGH |
| DS-DUG | Dashboard Usage Guide |  HIGH |

### Phase 14: Stakeholder Communication

| Code | Title | Priority |
|------|-------|----------|
| DS-DDR | Data-Driven Recommendations |  CRITICAL |
| DS-ESR | Executive Summary Report |  CRITICAL |
| DS-IAN | Insights Announcement |  HIGH |
| DS-SCT | Stakeholder Communication Template |  MEDIUM |

### Phase 15: Knowledge Management

| Code | Title | Priority |
|------|-------|----------|
| DS-ABP | Analytics Best Practices |  HIGH |
| DS-APT | Analysis Patterns Library |  MEDIUM |
| DS-CMC | Common Metrics Catalog |  HIGH |
| DS-IKB | Data Insights Knowledge Base |  MEDIUM |

### Phase 16: Postmortem / Retrospective

| Code | Title | Priority |
|------|-------|----------|
| DS-APR | Analysis Project Retrospective |  MEDIUM |
| DS-IVR | Insights Validation Results |  HIGH |
| DS-LLA | Lessons Learned from Analysis |  MEDIUM |

### Phase 17: Budgeting / Cost Management

| Code | Title | Priority |
|------|-------|----------|
| DS-BPT | Budget Proposal Template |  MEDIUM |
| DS-CBA | Cost-Benefit Analysis |  HIGH |
| DS-CEO | CapEx/OpEx Planning |  MEDIUM |
| DS-CTR | Cost Tracking Report |  MEDIUM |
| DS-ROI | ROI Projections |  HIGH |
| DS-TCO | Total Cost of Ownership |  MEDIUM |

### Phase 18: Vendor / Procurement

| Code | Title | Priority |
|------|-------|----------|
| DS-CTT | Contract Template |  MEDIUM |
| DS-PCH | Procurement Checklist |  MEDIUM |
| DS-RFI | Request for Information |  MEDIUM |
| DS-RFP | Request for Proposal |  HIGH |
| DS-SLT | SLA Agreement Template |  MEDIUM |
| DS-VEM | Vendor Evaluation Matrix |  HIGH |
| DS-VRA | Vendor Risk Assessment |  HIGH |

### Phase 19: Governance / Compliance Auditing

| Code | Title | Priority |
|------|-------|----------|
| DS-ACH | Audit Checklist |  HIGH |
| DS-ATL | Audit Trail Log |  HIGH |
| DS-CED | Certification Documentation |  MEDIUM |
| DS-CMX | Control Matrix |  HIGH |
| DS-CRT | Compliance Report Template |  HIGH |
| DS-PRR | Policy Review Record |  MEDIUM |
| DS-RRG | Risk Register |  HIGH |

### Phase 20: Decommissioning / End-of-Life

| Code | Title | Priority |
|------|-------|----------|
| DS-ARS | Archive Strategy Document |  MEDIUM |
| DS-DCH | Decommissioning Checklist |  MEDIUM |
| DS-DIA | Dependency Impact Analysis |  HIGH |
| DS-DMG | Data Migration Strategy |  HIGH |
| DS-HDR | Historical Data Retention Policy |  HIGH |
| DS-SRP | System Retirement Plan |  HIGH |
| DS-SUN | Sunset Communication Plan |  MEDIUM |

### Phase 21: Disaster Recovery / BCP

| Code | Title | Priority |
|------|-------|----------|
| DS-BCP | Business Continuity Plan |  CRITICAL |
| DS-BVC | Backup Verification Checklist |  HIGH |
| DS-CCP | Crisis Communication Plan |  MEDIUM |
| DS-DRE | Disaster Recovery Plan |  CRITICAL |
| DS-DTR | DR Test Report |  HIGH |
| DS-FOP | Failover Procedures |  HIGH |
| DS-RPO | RPO Definition |  HIGH |
| DS-RTO | RTO Definition |  HIGH |

### Phase 22: Change Management

| Code | Title | Priority |
|------|-------|----------|
| DS-CAB | CAB Notes |  MEDIUM |
| DS-CCL | Change Calendar |  HIGH |
| DS-CIA | Change Impact Assessment |  HIGH |
| DS-CSC | Change Success Criteria |  MEDIUM |
| DS-ECP | Emergency Change Procedure |  HIGH |
| DS-RBP | Rollback Plan Template |  HIGH |
| DS-RFC | Change Request Form |  HIGH |

### Phase 23: Capacity Planning

| Code | Title | Priority |
|------|-------|----------|
| DS-CFR | Capacity Forecast Report |  HIGH |
| DS-CTA | Capacity Threshold Alerts |  MEDIUM |
| DS-GPR | Growth Projections |  MEDIUM |
| DS-ISG | Infrastructure Sizing Guide |  MEDIUM |
| DS-PBL | Performance Baseline |  MEDIUM |
| DS-RAP | Resource Allocation Plan |  HIGH |
| DS-SAS | Scalability Assessment |  MEDIUM |


## USAGE NOTES

### Quick Start
1. Use the database for querying documentation requirements
2. Export to JSON for integration with other systems
3. Use CONTEXT.md as a quick reference

### Statistical Test Selection Guide
1. **Binary metric (CTR, conversion)** → Chi-square or Fisher's exact test
2. **Continuous metric + Normal distribution** → Two-sample t-test
3. **Continuous + Non-normal** → Mann-Whitney U test
4. **Multiple groups** → ANOVA (parametric) or Kruskal-Wallis (non-parametric)

### BI Tool Selection Guide
- **Tableau**: Best for complex visualizations, executive dashboards
- **Power BI**: Best for Microsoft ecosystem, cost-effective
- **Looker**: Best for data governance, LookML modeling
- **Metabase/Superset**: Best for open-source, startups

### Python Library Selection Guide
- **pandas**: Standard for small-medium data, stable API
- **Polars**: 10-50x faster, for large datasets (10GB+)
- **Dask**: For distributed processing, scales to clusters

---
*Generated by Data Science Documentation Matrix System v1.0.0*
