# 05 — Module Interface Contracts

**Status:** Draft v1.0  
**Powiązane dokumenty:** 03_architecture_overview, 06_openapi_specification, 12_itdoc_integration_spec

---

## 1. Zasada kontraktów

Każdy z 4 modułów Warsztatu (Sides) oraz 3 serwisów współdzielonych (LLM Adapter, Brief Parser, itdoc Connector) definiuje **formalny kontrakt** — zestaw typów wejścia, wyjścia i warunków błędu. Implementacja może się zmieniać; kontrakt jest stabilny.

Kontrakty opisane są w formacie:
- **Input:** dane wejściowe (typy Pydantic)
- **Output:** dane wyjściowe
- **Preconditions:** co musi być prawdą przed wywołaniem
- **Postconditions:** gwarancje po wywołaniu
- **Errors:** kody błędów + gdy są rzucane

---

## 2. Kontrakty modułów głównych

### 2.1 Side 1 — Template Ingestion

#### `POST /ingestion/spec` → `IngestionJob`

```
Input: IngestionSpec {
    source_type: "text" | "url" | "file"
    content:     str | None       # tekst jeśli source_type="text"
    url:         HttpUrl | None   # URL jeśli source_type="url"
    file:        UploadFile | None # plik jeśli source_type="file"
    standard_code: str | None     # opcjonalne powiązanie ze standardem
    hint_title:    str | None     # opcjonalny podpowiedź tytułu szablonu
}

Output: IngestionJob {
    id:     UUID
    status: "pending"
    created_at: datetime
}

Preconditions:
  - content LUB url LUB file musi być podane (nie wszystkie null)
  - Jeśli source_type="url": URL musi być dostępny HTTP 200
  - Rozmiar file ≤ 10 MB

Postconditions:
  - Job istnieje w bazie ze statusem "pending"
  - Zadanie generowania szablonu zostało zakolejkowane

Errors:
  422 Unprocessable Entity — brak wymaganego pola
  400 Bad Request          — URL niedostępny lub plik zbyt duży
  503 Service Unavailable  — LLM provider niedostępny
```

#### `GET /ingestion/{job_id}` → `IngestionJobDetail`

```
Input: job_id: UUID

Output (HTTP 200): IngestionJobDetail {
    job_id:               UUID
    status:               "pending"|"generating"|"review"|"approved"|"rejected"
    draft_content:        str | None    # Markdown szablonu (gdy status="review")
    standard_code:        str | None
    template_frontmatter: dict | None   # sparsowany YAML
    rejection_reason:     str | None
    approved_path:        str | None
    created_at:           datetime
    reviewed_at:          datetime | None
    updated_at:           datetime
}

Errors:
  404 Not Found — job_id nie istnieje
```

#### `POST /ingestion/{job_id}/approve` → `IngestionApproveResult`

```
Input: job_id: UUID
       ApproveRequest {
           save_path: str | None    # opcjonalna ścieżka zapisu (default: auto)
           index_for_mapping: bool = true  # czy dodać do local_templates_index?
       }

Preconditions:
  - Job musi mieć status="review"
  - draft_content musi być niepusty
  - Plik docelowy NIE może istnieć (no overwrite)

Logika:
  1. Sprawdź że job status = "review"
  2. Wstaw do custom_templates (title, phase_id, content, source_job_id)
  3. Zaktualizuj ingestion_jobs.status = "approved"
  4. Zwróć custom_template_id

Postconditions:
  - Plik Markdown zapisany na dysku w `workshop/data/generated_templates/`
  - Job status = "approved", approved_path = ścieżka pliku
  - Jeśli index_for_mapping=true:
      * Szablon dodany do `local_templates_index` (tabela w PostgreSQL lub plik JSON)
      * SemanticMapper może używać go jako dodatkowego źródła obok itdoc.db
  - Plik NIE jest importowany do it_doc_matrix.db (zasada read-only)

Output (HTTP 201 Created):
{
    "custom_template_id": "uuid",
    "doc_uid": "custom:{uuid}",
    "message": "Template approved and available for mapping"
}

Errors:
  409 Conflict  — job nie w statusie "review"
  409 Conflict  — plik docelowy już istnieje
  404 Not Found — job_id nie istnieje
```

#### `POST /ingestion/{job_id}/reject` → `IngestionJobDetail`

```
Input: job_id: UUID
       RejectRequest {
           reason: str | None   # opcjonalne uzasadnienie odrzucenia
       }

Preconditions:
  - Job musi mieć status="review" (NIEDOZWOLONE: approved → rejected)

Logika:
  - Zaktualizuj ingestion_jobs.status = "rejected"
  - Jeśli reason podany: zapisz w rejection_reason

Output (HTTP 200):
{
    "status": "rejected"
}

Errors:
  409 Conflict  — job nie w statusie "review"
  404 Not Found — job_id nie istnieje
```

> ⚠️ **WAŻNE — Gunicorn/Uvicorn workers (Side 1 Ingestion):**
> `asyncio.create_task()` używany w `generate_template_async()` działa TYLKO w ramach jednego procesu.
> Przy uruchomieniu z wieloma workerami (`gunicorn -w N`, `N>1`):
> - Task zginie przy restarcie workera
> - Status job pozostanie na "generating" — wymagany ręczny reset przez admin
>
> **Dla v1:** uruchom z `--workers=1` (single worker).  
> **Dla v2+:** zastąp `asyncio.create_task` kolejką Celery/RQ z brokerem Redis (identycznie jak Side 2).
>
> Konfiguracja v1 (docker-compose):
> ```
>   command: uvicorn workshop.main:app --host 0.0.0.0 --port 8000 --workers 1
> ```

#### Mechanizm `local_templates_index` (rozwiązanie A05)

Szablony zatwierdzone przez Side 1 są niewidoczne dla `itdoc.db`, ale mogą być indeksowane lokalnie w PostgreSQL i przeszukiwane przez SemanticMapper jako trzecie źródło:

```sql
-- Tabela indeksu lokalnych szablonów (Alembic migration 0006)
CREATE TABLE local_templates_index (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ingestion_job_id UUID NOT NULL REFERENCES ingestion_jobs(id),
    doc_title       TEXT NOT NULL,
    file_path       TEXT NOT NULL UNIQUE,
    standard_code   TEXT,          -- opcjonalne powiązanie ze standardem
    phase_id        INTEGER,       -- faza SDLC (1-24)
    keywords        TEXT[],        -- słowa kluczowe wyekstrahowane z treści
    content_hash    TEXT NOT NULL, -- SHA256 pliku
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

SemanticMapper wywołuje `connector.find_by_keyword()` AND odpytuje `local_templates_index` gdy `INDEX_LOCAL_TEMPLATES=true`. Oba wyniki są mergowane przed scoringiem.

---

### 2.2 Side 2 — Brief Mapper

#### `POST /brief/upload` → `BriefUploadResult`

```
Input: UploadFile (multipart/form-data)
       project_id: UUID (query param)

Output: BriefUploadResult {
    brief_id:    UUID
    filename:    str
    format:      "txt"|"md"|"pdf"|"docx"|"unknown"
    word_count:  int
    parse_status:"uploaded"|"parsing"|"parsed"|"failed"
    parse_error: str | None
}

Preconditions:
  - project_id musi istnieć
  - Plik ≤ 50 MB
  - Format wykrywany auto (MIME + rozszerzenie)

Postconditions:
  - Brief zapisany w bazie (raw_content + parsed_text)
  - parsed_text jest UTF-8, pozbawiony binarnych artefaktów

Errors:
  404 Not Found           — project_id nie istnieje
  415 Unsupported Media   — format nie obsługiwany
  413 Payload Too Large   — plik > 50 MB
  422 Unprocessable       — nie można sparsować (uszkodzony PDF etc.)
```

#### `POST /brief/{brief_id}/map` → `MappingResult`

```
Input: brief_id: UUID
       MapRequest {
           confidence_threshold: float = 0.4     # min confidence do włączenia
           max_results:          int   = 200      # max szablonów w wyniku
           force_rerun:          bool  = False    # przebiegnij ponownie mimo cache
       }

Output: MappingResult {
    id:                UUID
    brief_id:          UUID
    project_id:        UUID
    llm_model:         str
    extracted_entities: ExtractedEntities {
        domains:    list[str]
        standards:  list[str]
        regulations:list[str]
        phases:     list[int]
        keywords:   list[str]
        project_type: str | None
    }
    items:             list[MappingItem] {
        doc_uid:       str
        doc_title:     str
        phase_id:      int
        phase_name:    str
        confidence:    float        # 0.0–1.0
        match_reason:  str
        match_sources: list[str]    # ["standard:PCI_DSS", "keyword:payment"]
        is_required:   bool
    }
    total_items:       int
    avg_confidence:    float
    status:            "pending"|"running"|"done"|"failed"
    metadata:          MappingMetadata {
        processing_notes: dict | None   # np. {"partial_llm_timeout": true}
    } | None
}

### Tryb asynchroniczny (background task)

Dla długich briefów (word_count > 1500 lub wywołań LLM > 1):
- Endpoint zwraca **HTTP 202 Accepted** z body `{mapping_id, status: "running"}`
- Przetwarzanie trwa w tle (`asyncio.create_task` + in-memory registry dla v1)
- Klient może pollować status przez `GET /brief/{id}/mapping`

**Odpowiedź 202:**
```json
{
  "mapping_id": "<uuid>",
  "status": "running",
  "estimated_seconds": 30
}
```

**Odpowiedź 200 (synchroniczna, brief < 500 słów, LLM disabled):**
`MappingResult` z pełnymi wynikami.

**Polling:** `GET /brief/{id}/mapping` zwraca:
- `{status: "running", progress_percent: 65}` gdy trwa
- Pełny `MappingResult` gdy done/failed

**Retry-After:** Nagłówek `Retry-After: 10` w odpowiedzi 202.

**Status "partial":** Jeśli LLM timeout nastąpi w trakcie:
- Status = `"done"`, ale `metadata.processing_notes` zawiera `"partial_llm_timeout: true"`
- `avg_confidence` może być niższy niż przy pełnym przetwarzaniu

Preconditions:
  - brief_id musi istnieć
  - parse_status briefa musi być "parsed"
  - LLM provider musi być skonfigurowany
  - Jeśli istnieje mapping_results rekord ze status='running' dla tego 
    brief_id → zwróć HTTP 409 Conflict z body:
    {
      "error": "mapping_in_progress",
      "message": "Brief jest już przetwarzany. Sprawdź GET /brief/{id}/mapping.",
      "running_mapping_id": "<uuid>"
    }
    Implementacja: SELECT id FROM mapping_results WHERE brief_id=? AND status='running' LIMIT 1

Postconditions:
  - Wynik persystowany w mapping_results + mapping_items
  - Jeśli force_rerun=False i wynik istnieje: zwraca cache

Errors:
  404 Not Found      — brief_id nie istnieje
  409 Conflict       — brief nie sparsowany (parse_status != "parsed")
  503 Unavailable    — LLM timeout lub błąd API
  429 Too Many Req.  — rate limit LLM providera
```

#### `PUT /brief/{brief_id}/mapping/{item_id}` → `MappingItem`

```
Input: brief_id: UUID, item_id: UUID
       MappingItemUpdate {
           confidence:       float | None
           is_required:      bool  | None
           manually_reviewed:bool  = True
           reviewed_by:      str   | None  # opcjonalny identyfikator recenzenta (np. prefix X-API-Key)
       }

Preconditions:
  - item musi należeć do briefa

Postconditions:
  - manually_reviewed = True
  - confidence / is_required zaktualizowane
  - reviewed_by ustawiony (jeśli nie podano, system używa pierwszych 8 znaków X-API-Key)

> **Nota:** Jeśli `reviewed_by` nie podano, system może użyć pierwszych 8 znaków X-API-Key jako domyślnego.

Errors:
  404 Not Found — item_id nie istnieje lub nie należy do briefa
  422 Unprocessable — confidence poza zakresem 0.0–1.0
```

---

### 2.3 Side 3 — Report Engine

#### `POST /reports/estimate/{brief_id}` → `EstimationReport`

```
Input: brief_id: UUID
       EstimateRequest {
           confidence_threshold: float = 0.4
           include_phases:       list[int] | None   # None = wszystkie
       }

Output: EstimationReport {
    id:               UUID
    mapping_id:       UUID        # ← ID mapowania będącego podstawą wyceny
    project_id:       UUID
    total_docs:       int
    total_h_min:      float
    total_h_likely:   float
    total_h_max:      float
    complexity_level: "low"|"medium"|"high"|"critical"
    by_phase:         list[PhaseEstimate] {
        phase_id:         int
        phase_name:       str
        doc_count:        int
        h_min:            float
        h_likely:         float
        h_max:            float
        is_critical_path: bool
        documents:        list[{doc_uid, doc_title, h_estimate, confidence}]
    }
    deduction_basis:  list[DeductionPoint] {
        type:        str           # "standard_coverage", "phase_sequence", ...
        description: str           # czytelne uzasadnienie
        weight:      float         # waga znormalizowana (suma ≤ 1.0)
    }
    status:           "draft"
    created_at:       datetime
}

Preconditions:
  - brief_id musi mieć zakończone mapowanie (mapping status="done")
  - Jeśli istnieje wiele wyników mapowania dla tego samego brief_id
    (np. po force_rerun), używane jest mapowanie z najnowszym created_at
    i status="done". Wcześniejsze mapowania są ignorowane.

Postconditions:
  - Raport persystowany z status="draft"
  - by_phase pokrywa wszystkie fazy z ≥ 1 dokumentem

Errors:
  404 Not Found    — brief_id nie istnieje
  409 Conflict     — brak zakończonego mapowania
  422 Unprocessable — brak mapowań z confidence ≥ threshold

**Dry-run mode:** `?dry_run=true` — oblicza wynik ale NIE zapisuje do DB.
- Zwraca taki sam kształt odpowiedzi z `id: null` i `dry_run: true`
- Przydatne do testowania różnych `confidence_threshold` bez tworzenia draftów
```

#### `POST /reports/{report_id}/accept` → `EstimationReport`

```
Input: report_id: UUID

Preconditions:
  - status musi być "draft"

Postconditions:
  - status = "accepted"
  - accepted_at = now()
  - Odblokowany Side 4 (Work Planner może tworzyć plan)

Errors:
  404 Not Found — report_id nie istnieje
  409 Conflict  — raport już zaakceptowany lub odrzucony
```

#### `POST /reports/{report_id}/reject` → `EstimationReport`

```
Input: report_id: UUID
       RejectRequest {
           reason: str | None   # opcjonalna notatka PM
       }

Preconditions:
  - status musi być "draft"

Postconditions:
  - status = "rejected"
  - Side 4 nie może tworzyć planu dla odrzuconego raportu

Errors:
  404 Not Found — report_id nie istnieje
  409 Conflict  — raport już zaakceptowany (nie można odrzucić po akceptacji)
```

---

### 2.4 Side 4 — Work Planner

#### `POST /planning/create/{report_id}` → `WorkPlan`

```
Input: report_id: UUID

Output: WorkPlan {
    id:              UUID
    report_id:       UUID
    project_id:      UUID
    total_packages:  int
    status:          "draft"
    created_at:      datetime
}

Preconditions:
  - report_id musi mieć status="accepted"
  - Nie może istnieć aktywny plan dla tego raportu

Postconditions:
  - work_packages wypełnione z pełną sekwencją
  - Kolejność z rhythm_edges z it_doc_matrix.db
  - depends_on[] wypełnione per pakiet
  - assignee_type przypisany na podstawie RACI

Errors:
  404 Not Found — report_id nie istnieje
  409 Conflict  — raport nie zaakceptowany LUB plan już istnieje

**Dry-run mode:** `?dry_run=true` — oblicza wynik ale NIE zapisuje do DB.
- Zwraca taki sam kształt odpowiedzi z `id: null` i `dry_run: true`
- Przydatne do testowania różnych `confidence_threshold` bez tworzenia draftów
```

#### `GET /planning/{plan_id}/packages` → `list[WorkPackage]`

```
Input: plan_id: UUID
       status:        str | None    # "pending"|"in_progress"|"done"|"blocked"
       phase_id:      int | None
       assignee_type: str | None    # "ai_agent_writer"|"human"|"reviewer"

Output: list[WorkPackage] {
    id:             UUID
    plan_id:        UUID
    doc_uid:        str
    doc_title:      str
    phase_id:       int
    phase_name:     str
    sequence_order: int
    inputs_json:    list[str]       # z itdoc contracts
    outputs_json:   list[str]
    gates_json:     list[str]
    assignee_type:  str
    h_estimate:     float | None
    status:         str
    depends_on:     list[UUID]
}

Errors:
  404 Not Found — plan_id nie istnieje
```

---

## 3. Kontrakty serwisów współdzielonych

### 3.1 LLM Adapter

```python
class BaseLLMAdapter(Protocol):

    async def extract_entities(
        self,
        text: str,
        max_tokens: int = 2000
    ) -> ExtractedEntities:
        """
        Preconditions:
          - text nie może być pusty
          - text ≤ 100 000 znaków
        Postconditions:
          - Zwraca ExtractedEntities z co najmniej jednym niepustym polem
          - Wynik logowany w llm_calls_log
        Errors:
          LLMTimeoutError    — brak odpowiedzi > 30s
          LLMRateLimitError  — 429 od providera
          LLMProviderError   — inne błędy API
        """

    async def generate_template(
        self,
        spec_text: str,
        standard_code: str | None = None,
        hint_title: str | None = None
    ) -> str:
        """
        Preconditions:
          - spec_text nie może być pusty
        Postconditions:
          - Zwraca poprawny Markdown z YAML frontmatter
          - Frontmatter zawiera: title, category, phase, standards[]
        Errors:
          LLMTimeoutError, LLMProviderError
        """

    async def rerank_mapping(
        self,
        brief_text: str,
        candidates: list[MappingCandidate],
        max_candidates: int = 50
    ) -> list[ScoredCandidate]:
        """
        Postconditions:
          - Zwraca listę posortowaną malejąco wg score
          - score ∈ [0.0, 1.0]
          - len(result) ≤ max_candidates
        """
```

---

### 3.2 Brief Parser

```python
class BriefParser:

    def detect_format(self, filename: str, content: bytes) -> str:
        """
        Postconditions:
          - Zwraca jeden z: "txt", "md", "pdf", "docx", "unknown"
          - Wykrywa na podstawie MIME type + rozszerzenia (MIME ma priorytet)
        """

    def parse(self, content: bytes, format: str) -> ParsedBrief:
        """
        Input:  surowe bajty pliku + format
        Output: ParsedBrief {
            text:      str          # znormalizowany tekst UTF-8
            metadata:  dict         # {author, pages, word_count, ...}
            chunks:    list[str]    # podzielony na chunki ≤ 4000 tokenów
        }
        Preconditions:
          - content nie może być pusty
          - format != "unknown"
        Postconditions:
          - text jest UTF-8 bez null bytes, stripped whitespace
          - word_count ≥ 1
          - chunks ma ≥ 1 element
        Errors:
          ParseError — plik uszkodzony lub zaszyfrowany
          UnsupportedFormatError — format = "unknown"
        """
```

---

### 3.3 itdoc Connector

```python
class ItdocConnector:
    """
    Wrapper read-only na Python API biblioteki itdoc.
    NIGDY nie modyfikuje it_doc_matrix.db.
    Wszystkie metody uruchamiane przez run_in_executor
    (itdoc jest synchroniczne, Warsztat jest async).
    """

    async def find_by_standard(self, standard_code: str) -> list[DocRef]:
        """
        Postconditions:
          - Zwraca listę DocRef z: doc_uid, title, path, phase_id
          - Pusta lista gdy standard_code nie istnieje w DB
        """

    async def find_by_regulation(self, regulation_code: str) -> list[DocRef]:
        """Analogicznie do find_by_standard"""

    async def get_contract(self, doc_uid: str) -> DocContract | None:
        """
        Output: DocContract {
            inputs:  list[str]
            outputs: list[str]
            gates:   list[str]
            impact:  dict
        }
        Zwraca None jeśli kontrakt nie istnieje (tabela contracts jest stub)
        """

    async def rhythm_upstream(self, doc_uid: str, depth: int = 1) -> list[DocRef]:
        """Dokumenty wymagane przed doc_uid (poprzedzające)"""

    async def rhythm_downstream(self, doc_uid: str, depth: int = 1) -> list[DocRef]:
        """Dokumenty zależne od doc_uid (następujące)"""

    async def get_phases(self) -> list[Phase]:
        """Pełna lista 24 faz SDLC z ordinal"""
```

---

## 4. Kody błędów — tabela zbiorcza

| Kod HTTP | Klasa wyjątku | Znaczenie |
|----------|--------------|-----------|
| 400 | `BadRequestError` | Nieprawidłowe dane wejściowe (np. URL niedostępny) |
| 404 | `NotFoundError` | Zasób nie istnieje (projekt, brief, raport, plan) |
| 409 | `ConflictError` | Stan zasobu uniemożliwia operację (np. brief nie sparsowany) |
| 413 | `PayloadTooLargeError` | Plik przekracza limit rozmiaru |
| 415 | `UnsupportedMediaError` | Nieobsługiwany format pliku |
| 422 | `ValidationError` | Błąd walidacji Pydantic |
| 429 | `RateLimitError` | Rate limit LLM providera |
| 503 | `ServiceUnavailableError` | LLM provider niedostępny |
| 500 | `InternalError` | Nieoczekiwany błąd serwera |

**Format odpowiedzi błędu (spójny dla wszystkich endpointów):**
```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "Brief 3f7a... nie istnieje",
    "detail": null,
    "request_id": "req_abc123"
  }
}
```

---

## §6 — Audit Log Points

Następujące akcje MUSZĄ tworzyć wpisy w tabeli `audit_log`:

| Endpoint | entity_type | action | actor_type |
|----------|-------------|--------|------------|
| `POST /reports/{id}/accept` | `estimation_report` | `accept` | `pm` |
| `POST /reports/{id}/reject` | `estimation_report` | `reject` | `pm` |
| `POST /ingestion/{id}/approve` | `ingestion_job` | `approve_template` | `pm` |
| `POST /ingestion/{id}/reject` | `ingestion_job` | `reject_template` | `pm` |
| `PUT /brief/{id}/mapping/{item_id}` | `mapping_item` | `manual_review` | `pm` |
| `DELETE /projects/{id}` | `project` | `delete` | `system` |
| `POST /brief/{id}/map` (zakończone) | `mapping_result` | `mapping_complete` | `system` |

Implementacja: dekorator `@audit_log(entity_type, action)` lub middleware per endpoint.

---

## 5. Sekwencja przepływu danych (happy path)

```
AI Agent / PM
     │
     │ POST /brief/upload (plik .pdf)
     ▼
[Side 2] BriefParser.parse() → ParsedBrief
     │
     │ POST /brief/{id}/map
     ▼
[Side 2] LLMAdapter.extract_entities() → ExtractedEntities
     │
[Side 2] ItdocConnector.find_by_standard() × N standardów
[Side 2] ItdocConnector.rhythm_downstream() × kluczowe szablony
     │
[Side 2] ConfidenceScorer → MappingResult (N items, avg_confidence)
     │
     │ POST /reports/estimate/{brief_id}
     ▼
[Side 3] EstimationEngine.calculate() → EstimationReport (draft)
     │
     │ POST /reports/{id}/accept  (PM akceptuje)
     ▼
     │ POST /planning/create/{report_id}
     ▼
[Side 4] ItdocConnector.rhythm_upstream/downstream() → kolejność
[Side 4] ItdocConnector.get_contract() × każdy dokument → inputs/outputs
[Side 4] RACIResolver → assignee_type per pakiet
     │
     │ GET /planning/{plan_id}/packages
     ▼
WorkPackage[] → AI-agenci wykonują pracę
```

---

## §7 — State Machine — Dozwolone przejścia

### work_package.status
```
pending → in_progress → done
pending → blocked
blocked → pending      (po usunięciu blokera)
in_progress → blocked  (zablokowanie w trakcie)
NIEDOZWOLONE: done → in_progress  (wymaga nowego planu)
NIEDOZWOLONE: done → blocked
```

### ingestion_job.status
```
pending → generating → review → approved
                     → rejected
NIEDOZWOLONE: approved → rejected (nieodwracalne zatwierdzenie)
NIEDOZWOLONE: rejected → approved (wymaga nowego job)
```

### mapping_results.status
```
pending → running → done
running → failed
NIEDOZWOLONE: done → running (re-mapowanie tworzy nowy rekord)
```

### estimation_reports.status
```
draft → accepted
draft → rejected
NIEDOZWOLONE: accepted → rejected
```

> **Korekta po akceptacji:** Jeśli PM chce zmienić zaakceptowany raport, workaround to
> wygenerowanie nowego raportu z `POST /reports/estimate/{brief_id}?force_rerun=true`.
> Stary raport zostaje w historii z status=accepted. Nowy jest draft do ponownej akceptacji.

Implementacja: dekorator `validate_status_transition(entity, current, target)` rzuca HTTP 422 przy niedozwolonym przejściu.

---

## §8 — Webhook Delivery Specification

### Mechanizm dostarczania

HTTP POST z `Content-Type: application/json` na `target_url` z tabeli `webhook_subscriptions`.

### Format payload
```json
{
  "event": "mapping.done",
  "project_id": "<uuid>",
  "resource_id": "<uuid>",
  "timestamp": "2025-01-14T10:30:00Z",
  "data": { }
}
```

### Podpis HMAC
Header: `X-Workshop-Signature: sha256=<HMAC-SHA256(secret_hash, body_bytes)>`

### Polityka retry
- 3 próby, exponential backoff: 5s → 30s → 300s
- Timeout per próbę: 10 sekund
- Po 3 nieudanych próbach: `webhook_subscriptions.is_active = false` (circuit breaker)

### Endpointy CRUD (OpenAPI: `/projects/{id}/webhooks`)
```
POST   /projects/{id}/webhooks          — subskrypcja
GET    /projects/{id}/webhooks          — lista subskrypcji
DELETE /projects/{id}/webhooks/{wh_id}  — usunięcie
```

### Zdarzenia (event types)
| Event | Trigger |
|-------|---------|
| `mapping.done` | SemanticMapper zakończył przetwarzanie |
| `mapping.failed` | SemanticMapper zakończył błędem |
| `report.ready` | EstimationReport wygenerowany (status=draft) |
| `report.accepted` | PM zaakceptował raport |
| `plan.ready` | WorkPlanner wygenerował plan |
| `ingestion.review` | Szablon gotowy do review |

---

### §8.1 — Orchestracja: Mapping Task → Webhook Dispatch

Po zakończeniu background mapping task (asyncio.create_task), task MUSI wywołać webhook dispatch:

```python
async def _run_mapping_task(
    brief_id: UUID,
    project_id: UUID,
    mapper: SemanticMapper,
    webhook_dispatcher: WebhookDispatcher,
    db: AsyncSession,
):
    try:
        result = await mapper.map(brief=parsed_brief, project_id=project_id)
        await db.execute(
            "UPDATE mapping_results SET status='done', ... WHERE id=?", [result.id]
        )
        event = "mapping.done"
    except Exception as e:
        await db.execute(
            "UPDATE mapping_results SET status='failed', error_message=? WHERE id=?",
            [str(e), mapping_id]
        )
        event = "mapping.failed"
    finally:
        # Wyślij webhook do wszystkich aktywnych subskrypcji projektu
        subs = await db.execute(
            "SELECT * FROM webhook_subscriptions WHERE project_id=? AND is_active=true AND ?=ANY(events)",
            [project_id, event]
        )
        for sub in subs:
            await webhook_dispatcher.enqueue(sub, payload={
                "event": event,
                "project_id": str(project_id),
                "resource_id": str(mapping_id),
                "timestamp": datetime.utcnow().isoformat(),
            })
```

**Dependency Injection:** `WebhookDispatcher` jest wstrzykiwany przez FastAPI DI do routera,
a router przekazuje go jako argument do `asyncio.create_task(...)`.

---

## §8.2 — Startup Recovery

Przy starcie aplikacji (`lifespan` event w FastAPI) należy wykonać:

```python
async def on_startup():
    # 1. Reset zombie mapping tasks (przerwane przez crash/restart)
    await db.execute("""
        UPDATE mapping_results 
        SET status = 'failed', 
            error_message = 'Interrupted by service restart'
        WHERE status = 'running'
    """)
    
    # 2. Log count of recovered tasks
    count = await db.fetchval("SELECT COUNT(*) FROM mapping_results WHERE status='failed' AND error_message LIKE 'Interrupted%'")
    logger.warning(f"Startup recovery: reset {count} zombie mapping tasks")
```

Dotyczy też webhooków (K-07): przy starcie sprawdź pending webhook deliveries.

---

## §9 — Kontrakty projektowe (import/export/compare)

### Kontrakt GET /projects/{id}/export

**Limity:**
- Max rozmiar eksportu: 100MB (HTTP 413 jeśli przekroczony)
- Query param `?exclude_raw_content=true` (domyślnie `false`) — wyklucza raw_content z briefów

**Implementacja (streaming):**
```python
import io, zipfile
from starlette.responses import StreamingResponse

async def export_project(project_id: UUID, exclude_raw: bool = False):
    async def generate_zip():
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zf:
            # Dodaj pliki strumieniowo
            zf.writestr("project.json", await get_project_json(project_id))
            for brief in await get_briefs(project_id):
                data = brief.raw_content if not exclude_raw else b""
                zf.writestr(f"briefs/{brief.id}.json", brief.to_json(include_raw=not exclude_raw))
        buf.seek(0)
        yield buf.getvalue()

    return StreamingResponse(generate_zip(), media_type="application/zip")
```

---

### Kontrakt POST /projects/import

**Limity i bezpieczeństwo:**
- Max rozmiar ZIP: 200MB (HTTP 413)
- Timeout importu: 120 sekund
- Import atomowy: całość w jednej transakcji DB (albo wszystko albo nic)
- Walidacja struktury ZIP przed importem: sprawdź obecność `project.json`
- Sanityzacja nazw plików: zapobiegaj path traversal (`../`)

---

### Kontrakt GET /reports/compare

**Walidacja:**
1. Oba raporty muszą należeć do tego samego project_id (HTTP 422 jeśli różne)
2. Lazy loading: domyślnie `?include_details=false` zwraca tylko totals diff
3. `?include_details=true` — dołącza added_docs/removed_docs/changed_estimates

**Performance:**
- Cache diff (Redis lub in-memory LRU) przez 5 minut: klucz = `compare:{min(a,b)}:{max(a,b)}`
- Limit: max 500 items w diff (HTTP 413 jeśli przekroczony z `detail_truncated: true`)
