# 04 — PostgreSQL Data Model

**Status:** Draft v1.0  
**Powiązane dokumenty:** 03_architecture_overview, 05_module_interface_contracts, 12_itdoc_integration_spec

---

## 1. Przegląd schematu

Baza `workshop.db` (PostgreSQL) przechowuje wyłącznie dane **Warsztatu** — stan projektów klientów, wgrane briefy, wyniki mapowania, raporty i plany pracy. Baza `it_doc_matrix.db` (SQLite) pozostaje bez zmian.

```
workshop.db (PostgreSQL)
├── projects               ← projekty klientów
├── briefs                 ← wgrane pliki briefów + sparsowany tekst
├── mapping_results        ← wyniki mapowania brief→szablony
├── mapping_items          ← pojedyncze pozycje mapowania (per szablon)
├── estimation_reports     ← raporty kosztorysowe
├── report_phase_items     ← linie kosztorysu per faza
├── work_plans             ← plany pracy (po akceptacji)
├── work_packages          ← task-units dla AI-agentów
├── ingestion_jobs         ← zadania ingestii szablonów
├── llm_calls_log          ← log wywołań LLM (cache + audit)
└── app_settings           ← konfiguracja runtime (key-value)
```

---

## 2. Tabele — definicje

### 2.1 `projects`

```sql
CREATE TABLE projects (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name            TEXT NOT NULL,
    client_name     TEXT,
    description     TEXT,
    status          TEXT NOT NULL DEFAULT 'active'
                        CHECK (status IN ('active','on_hold','archived','completed','cancelled')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_projects_created ON projects(created_at DESC);
```

**Pola:**
| Kolumna | Typ | Opis |
|---------|-----|------|
| id | UUID | Klucz główny (auto-generowany) |
| name | TEXT | Nazwa projektu (np. "Projekt Fintech ABC S.A.") |
| client_name | TEXT | Opcjonalna nazwa klienta |
| description | TEXT | Notatki o projekcie |
| status | TEXT | `active` / `on_hold` / `archived` / `completed` / `cancelled` |

---

### 2.2 `briefs`

```sql
CREATE TABLE briefs (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id      UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    filename        TEXT NOT NULL,
    version         INTEGER NOT NULL DEFAULT 1,         -- wersjonowanie briefów (A03)
    parent_brief_id UUID REFERENCES briefs(id),         -- poprzednia wersja (NULL = v1)
    format          TEXT NOT NULL CHECK (format IN ('txt','md','pdf','docx','unknown')),
    raw_content     BYTEA,                              -- oryginał binarny (dla PDF/DOCX)
    parsed_text     TEXT,                               -- znormalizowany tekst UTF-8
    metadata        JSONB DEFAULT '{}',                 -- {author, pages, word_count, ...}
    parse_status    TEXT NOT NULL DEFAULT 'uploaded'
                        CHECK (parse_status IN ('uploaded', 'parsing', 'parsed', 'failed')),
    parse_error     TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_briefs_project ON briefs(project_id);
CREATE INDEX idx_briefs_status  ON briefs(parse_status);
CREATE INDEX idx_briefs_version ON briefs(project_id, filename, version);
-- Nowa wersja briefu = nowy wiersz z version++ i parent_brief_id = poprzednie ID
```

**`metadata` JSONB — przykład:**
```json
{
  "author": "Jan Kowalski",
  "pages": 4,
  "word_count": 1250,
  "detected_language": "pl",
  "source_encoding": "utf-8"
}
```

---

### 2.3 `mapping_results`

```sql
CREATE TABLE mapping_results (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    brief_id        UUID NOT NULL REFERENCES briefs(id) ON DELETE CASCADE,
    llm_model       TEXT,                           -- "gpt-4o", "claude-3-5-sonnet", ...
    extracted_entities JSONB DEFAULT '{}',          -- encje wyciągnięte przez LLM
    total_items     INTEGER DEFAULT 0,
    avg_confidence  NUMERIC(4,3),
    status          TEXT NOT NULL DEFAULT 'pending'
                        CHECK (status IN ('pending','running','done','failed')),
    error           TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at    TIMESTAMPTZ
);

CREATE INDEX idx_mapping_brief    ON mapping_results(brief_id);
CREATE INDEX idx_mapping_status   ON mapping_results(status);
```

**`extracted_entities` JSONB — przykład:**
```json
{
  "domains":    ["fintech", "cloud", "mobile"],
  "standards":  ["PCI DSS", "ISO/IEC 27001", "OWASP"],
  "regulations":["RODO", "KSC"],
  "phases":     [3, 5, 6, 13, 19],
  "keywords":   ["payment gateway", "API security", "audit log", "encryption"],
  "project_type": "greenfield_saas"
}
```

---

### 2.4 `mapping_items`

```sql
CREATE TABLE mapping_items (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    mapping_id      UUID NOT NULL REFERENCES mapping_results(id) ON DELETE CASCADE,
    doc_uid         TEXT NOT NULL,                  -- UID z it_doc_matrix.db
    doc_title       TEXT NOT NULL,
    doc_path        TEXT,
    phase_id        INTEGER,                        -- 1–23 z itdoc
    phase_name      TEXT,
    confidence      NUMERIC(4,3) NOT NULL,          -- 0.000–1.000
    match_reason    TEXT,                           -- opis uzasadnienia
    match_sources   JSONB DEFAULT '[]',             -- ["standard:PCI_DSS", "keyword:payment"]
    is_required     BOOLEAN DEFAULT FALSE,          -- wymagany przez standard/regulację
    manually_reviewed BOOLEAN DEFAULT FALSE,
    reviewed_by     TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_mitems_mapping    ON mapping_items(mapping_id);
CREATE INDEX idx_mitems_doc        ON mapping_items(doc_uid);
CREATE INDEX idx_mitems_confidence ON mapping_items(confidence DESC);
CREATE INDEX idx_mitems_phase      ON mapping_items(phase_id);
```

---

### 2.5 `estimation_reports`

```sql
CREATE TABLE estimation_reports (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    mapping_id      UUID NOT NULL REFERENCES mapping_results(id),
    project_id      UUID NOT NULL REFERENCES projects(id),
    total_docs      INTEGER NOT NULL DEFAULT 0,
    total_h_min     NUMERIC(8,1) NOT NULL DEFAULT 0,
    total_h_likely  NUMERIC(8,1) NOT NULL DEFAULT 0,
    total_h_max     NUMERIC(8,1) NOT NULL DEFAULT 0,
    currency        TEXT DEFAULT 'h',               -- roboczogodziny
    complexity_level TEXT CHECK (complexity_level IN ('low','medium','high','critical')),
    deduction_basis JSONB DEFAULT '[]',             -- [{type, description, weight}]
    status          TEXT NOT NULL DEFAULT 'draft'
                        CHECK (status IN ('draft','accepted','rejected')),
    accepted_at     TIMESTAMPTZ,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_reports_mapping ON estimation_reports(mapping_id);
CREATE INDEX idx_reports_project ON estimation_reports(project_id);
CREATE INDEX idx_reports_status  ON estimation_reports(status);
```

**`deduction_basis` JSONB — przykład podstaw dedukcji:**
```json
[
  {"type": "standard_coverage",  "description": "PCI DSS wymaga 12 obszarów kontrolnych → 47 szablonów", "weight": 0.35},
  {"type": "regulation_overlap", "description": "RODO i KSC nakładają się w 8 dokumentach bezpieczeństwa", "weight": 0.25},
  {"type": "phase_sequence",     "description": "Faza 3 (Architektura) musi poprzedzać fazę 5 (Development)", "weight": 0.20},
  {"type": "domain_complexity",  "description": "Domena fintech wymaga mnożnika 1.3x (regulacje + compliance)", "weight": 0.15},
  {"type": "uncertainty_buffer", "description": "12 dokumentów z confidence < 0.7 — bufor niepewności", "weight": 0.05}
]
```

> Wagi nie sumują się zawsze do 1.0 — zależą od warunków projektu. 
> Patrz dok.10 §5 po szczegóły normalizacji.

---

### 2.6 `report_phase_items`

```sql
CREATE TABLE report_phase_items (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_id       UUID NOT NULL REFERENCES estimation_reports(id) ON DELETE CASCADE,
    phase_id        INTEGER NOT NULL,
    phase_name      TEXT NOT NULL,
    doc_count       INTEGER NOT NULL DEFAULT 0,
    h_min           NUMERIC(6,1) NOT NULL DEFAULT 0,
    h_likely        NUMERIC(6,1) NOT NULL DEFAULT 0,
    h_max           NUMERIC(6,1) NOT NULL DEFAULT 0,
    is_critical_path BOOLEAN DEFAULT FALSE,
    notes           TEXT
);

CREATE INDEX idx_rphase_report ON report_phase_items(report_id);
CREATE INDEX idx_rphase_phase  ON report_phase_items(phase_id);
```

---

### 2.7 `work_plans`

```sql
CREATE TABLE work_plans (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_id       UUID NOT NULL REFERENCES estimation_reports(id),
    project_id      UUID NOT NULL REFERENCES projects(id),
    total_packages  INTEGER DEFAULT 0,
    total_packages_requested INTEGER,               -- oryginalna liczba z MappingResult (null = nieznana)
    status          TEXT NOT NULL DEFAULT 'draft'
                        CHECK (status IN ('draft','active','stale','archived')),
                        -- 'stale': zastąpiony po zmianie mappingu (patrz spec11 §10)
                        -- 'archived': manualnie przez PM
                        -- 'completed'/'cancelled' usunięte — zastąpione przez 'stale'/'archived'
    stale_reason    TEXT,                           -- powód unieważnienia (gdy status='stale')
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_wplans_report  ON work_plans(report_id);
CREATE INDEX idx_wplans_project ON work_plans(project_id);
```

---

### 2.8 `work_packages`

```sql
CREATE TABLE work_packages (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    plan_id         UUID NOT NULL REFERENCES work_plans(id) ON DELETE CASCADE,
    doc_uid         TEXT NOT NULL,                  -- UID z it_doc_matrix.db
    doc_title       TEXT NOT NULL,
    phase_id        INTEGER NOT NULL,
    phase_name      TEXT NOT NULL,
    sequence_order  INTEGER NOT NULL,               -- kolejność wykonania
    inputs_json     JSONB DEFAULT '[]',             -- z itdoc contracts
    outputs_json    JSONB DEFAULT '[]',
    gates_json      JSONB DEFAULT '[]',             -- warunki wejścia
    assignee_type   TEXT,                           -- "ai_agent_writer", "ai_agent_reviewer", "human"
    h_estimate      NUMERIC(5,1),
    status          TEXT NOT NULL DEFAULT 'pending'
                        CHECK (status IN ('pending','in_progress','done','blocked')),
    depends_on      UUID[],                         -- IDs poprzednich work_packages
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_wpkg_plan      ON work_packages(plan_id);
CREATE INDEX idx_wpkg_phase     ON work_packages(phase_id);
CREATE INDEX idx_wpkg_sequence  ON work_packages(sequence_order);
CREATE INDEX idx_wpkg_status    ON work_packages(status);
CREATE INDEX idx_wpkg_doc       ON work_packages(doc_uid);
```

---

### 2.9 `ingestion_jobs`

```sql
CREATE TABLE ingestion_jobs (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source_type     TEXT NOT NULL CHECK (source_type IN ('text','url','file')),
    source_content  TEXT,                           -- raw input
    source_url      TEXT,
    standard_code   TEXT,                           -- powiązany standard (opcjonalnie)
    generated_template TEXT,                        -- wygenerowany Markdown szablonu
    template_frontmatter JSONB DEFAULT '{}',        -- sparsowany YAML frontmatter
    status          TEXT NOT NULL DEFAULT 'pending'
                        CHECK (status IN ('pending','generating','review','approved','rejected')),
    rejection_reason TEXT,
    approved_path   TEXT,                           -- ścieżka do zapisanego pliku
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_ijobs_status   ON ingestion_jobs(status);
CREATE INDEX idx_ijobs_standard ON ingestion_jobs(standard_code);
```

---

### 2.10 `llm_calls_log`

```sql
CREATE TABLE llm_calls_log (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    provider        TEXT NOT NULL,                  -- "openai", "anthropic", "ollama"
    model           TEXT NOT NULL,
    operation       TEXT NOT NULL,                  -- "extract_entities", "generate_template", ...
    prompt_hash     TEXT,                           -- SHA256 promptu (do cache lookup)
    input_tokens    INTEGER,
    output_tokens   INTEGER,
    latency_ms      INTEGER,
    status          TEXT NOT NULL CHECK (status IN ('ok','error','cached')),
    error_message   TEXT,
    response_cached BOOLEAN DEFAULT FALSE,
    response_content TEXT,                          -- pełna odpowiedź LLM (dla cache replay)
    entity_id       UUID,                           -- powiązany rekord (mapping_id, job_id, ...)
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_llm_provider   ON llm_calls_log(provider, model);
CREATE INDEX idx_llm_operation  ON llm_calls_log(operation);
CREATE INDEX idx_llm_entity     ON llm_calls_log(entity_id);
CREATE INDEX idx_llm_hash       ON llm_calls_log(prompt_hash);  -- do cache lookup
CREATE INDEX idx_llm_cache      ON llm_calls_log(prompt_hash) WHERE status = 'ok';
```

---

### 2.11 `app_settings`

```sql
CREATE TABLE app_settings (
    key     TEXT PRIMARY KEY,
    value   TEXT NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Przykładowe wartości domyślne (opcjonalne):
INSERT INTO app_settings (key, value) VALUES
    ('default_llm_provider', 'openai'),
    ('default_confidence_threshold', '0.4'),
    ('max_mapping_items', '200'),
    ('estimation_h_per_point', '0.5');
```

---

### 2.12 `project_settings` (NOWA — A07: per-projekt config)

```sql
CREATE TABLE project_settings (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id  UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    key         TEXT NOT NULL,
    value       TEXT NOT NULL,
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (project_id, key)
);

CREATE INDEX idx_project_settings_project ON project_settings(project_id);
```

**Nadpisywalne klucze:** Każdy klucz z `app_settings` może być nadpisany per-projekt.
Przykład: `confidence_threshold=0.5` dla projektu fintech (więcej dokumentów), `estimation_h_per_point=0.8` dla projektu healthcare (wyższy rygor).

Rozwiązanie w serwisie:
```python
async def resolve_settings(project_id: UUID, key: str) -> str:
    """Zwraca wartość: project_settings → fallback app_settings."""
    per_project = await db.fetchval(
        "SELECT value FROM project_settings WHERE project_id=$1 AND key=$2",
        project_id, key
    )
    if per_project:
        return per_project
    return await db.fetchval("SELECT value FROM app_settings WHERE key=$1", key)
```

---

### 2.13 `audit_log` (NOWA — A08: kto co kiedy)

```sql
CREATE TABLE audit_log (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_type TEXT NOT NULL,  -- 'mapping_result' | 'estimation_report' | 'work_plan' | 'ingestion_job'
    entity_id   UUID NOT NULL,
    action      TEXT NOT NULL,  -- 'accept' | 'reject' | 'manual_review' | 'approve_template'
    actor       TEXT NOT NULL,  -- API key prefix (pierwsze 8 znaków, bez pełnego klucza)
    details     JSONB DEFAULT '{}',  -- {reason, changed_fields, ...}
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_audit_entity   ON audit_log(entity_type, entity_id);
CREATE INDEX idx_audit_actor    ON audit_log(actor);
CREATE INDEX idx_audit_created  ON audit_log(created_at DESC);
```

**Przykładowy wpis:**
```json
{
  "entity_type": "estimation_report",
  "entity_id": "f3a2...",
  "action": "accept",
  "actor": "sk-prod12",
  "details": {"previous_status": "draft", "comment": "Kosztorys zaakceptowany przez PM"},
  "created_at": "2026-03-11T14:30:00Z"
}
```

---

### 2.14 `webhook_subscriptions` (NOWA — A02: powiadomienia)

```sql
CREATE TABLE webhook_subscriptions (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id      UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    target_url      TEXT NOT NULL,
    events          TEXT[] NOT NULL DEFAULT '{}',
    -- eventy: 'mapping.done' | 'report.ready' | 'plan.created' | 'ingestion.approved'
    secret_hash     TEXT,           -- HMAC-SHA256 podpisu payloadu (opcjonalne)
    is_active       BOOLEAN NOT NULL DEFAULT true,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_webhooks_project ON webhook_subscriptions(project_id);
CREATE INDEX idx_webhooks_active  ON webhook_subscriptions(is_active) WHERE is_active = true;
```

**Przykładowe zdarzenia:**

| Event | Trigger | Payload |
|-------|---------|---------|
| `mapping.done` | `POST /brief/{id}/map` zakończone | `{brief_id, mapping_id, status, avg_confidence}` |
| `report.ready` | EstimationReport status="draft" | `{report_id, project_id, total_h_likely, complexity}` |
| `plan.created` | WorkPlan status="draft" | `{plan_id, report_id, total_packages}` |
| `ingestion.approved` | Side 1 job approved | `{job_id, doc_title, file_path}` |

---

## 3. Diagram relacji (ERD)

```
projects (1) ──< briefs (many)
briefs   (1) ──< briefs (many, self-ref: parent_brief_id = wersjonowanie)
briefs   (1) ──< mapping_results (many)
mapping_results (1) ──< mapping_items (many)
mapping_results (1) ──< estimation_reports (many)
estimation_reports (1) ──< report_phase_items (many)
estimation_reports (1) ──< work_plans (many)
work_plans (1) ──< work_packages (many)
projects (1) ──< project_settings (many)  ← NOWE

ingestion_jobs    (standalone)
llm_calls_log     (standalone, audit LLM)
app_settings      (standalone, config globalny)
project_settings  (per-projekt config)    ← NOWE
audit_log         (standalone, audit akcji) ← NOWE
webhook_subscriptions (per-projekt)       ← NOWE
```

---

## 4. Alembic migrations

Plik startowy `alembic.ini` + `env.py` z `DATABASE_URL` z `.env`.

Konwencja nazewnictwa wersji:
```
migrations/versions/
├── 0001_initial_schema.py          # Tabele 2.1-2.11 (oryginalne)
├── 0002_brief_versioning.py        # brief.version, parent_brief_id (A03)
├── 0003_project_settings.py        # project_settings table (A07)
├── 0004_audit_log.py               # audit_log table (A08)
├── 0005_webhooks.py                # webhook_subscriptions table (A02)
├── 0006_content_hash.py            # briefs.content_hash UNIQUE (B05)
├── 0007_retention_policy.py        # mapping_results.expires_at, retencja (B06)
├── 0008_ingestion_events.py        # ingestion_events table (C02)
├── 0009_llm_response_content.py    # llm_calls_log.response_content TEXT (D01)
├── 0010_audit_log_extended.py      # audit_log.request_id, indexes (D04)
└── 0011_custom_templates.py        # custom_templates table (V-03)
```

Uruchomienie:
```bash
alembic upgrade head          # zastosuj wszystkie migracje
alembic downgrade -1          # cofnij ostatnią
alembic revision --autogenerate -m "opis zmiany"  # nowa migracja
```

---

## 5. Polityka danych

| Zasada | Szczegóły |
|--------|-----------|
| **Izolacja od itdoc** | Żadna tabela workshop.db nie ma FK do it_doc_matrix.db. Powiązania przez `doc_uid` (TEXT) — soft reference. |
| **Kaskadowe usuwanie** | `briefs` → `mapping_results` → `mapping_items` (ON DELETE CASCADE). Projekt można usunąć w całości. |
| **Wersjonowanie briefów** | `briefs.version` + `parent_brief_id` — każdy remap tworzy nową wersję. Historia zachowana. |
| **Audyt LLM** | Każde wywołanie LLM logowane w `llm_calls_log` z hashm promptu — umożliwia cache i audyt kosztów. |
| **Audyt akcji** | Każda akcja accept/reject/approve logowana w `audit_log` z prefiksem API key aktora. |
| **Per-projekt config** | `project_settings` nadpisuje `app_settings` dla danego projektu. Fallback na globalne. |
| **Binarne pliki** | Oryginalne PDFy/DOCXy przechowywane jako BYTEA w `briefs.raw_content`. Limit: 50 MB per plik. |
| **JSONB vs TEXT** | Strukturalne dane (entities, sources, basis) jako JSONB — indeksowalne. Długie teksty (brief, template) jako TEXT. |
| **Webhooks** | `webhook_subscriptions` z HMAC podpisem — opcjonalne, per-projekt, filtrowanie po zdarzeniach. |
