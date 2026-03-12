# ANALIZA RUNDA 3 — *(dokument roboczy)*

> **STATUS:** Wszystkie 40 znalezisk zaimplementowane. Ten plik to historyczny zapis analizy.

**Data:** 2025-07-13  
**Zakres:** Wszystkie dokumenty 01–16 systemu Warsztat  
**Metoda:** Analiza cross-dokumentowa, weryfikacja spójności schematów, audit gotowości do implementacji  
**Pominięto:** Znaleziska z Rund 1–2 (26 + 38 = 64 naprawione)

---

## Podsumowanie Rundy 3

| Kategoria | Znaleziska | 🔴 | 🟡 | 🟢 |
|-----------|-----------|-----|-----|-----|
| **I — Braki** | 14 | 4 | 7 | 3 |
| **J — Błędy założeń** | 11 | 3 | 6 | 2 |
| **K — Ryzyka implementacyjne** | 8 | 2 | 4 | 2 |
| **L — Propozycje rozwinięcia** | 7 | 0 | 3 | 4 |
| **RAZEM** | **40** | **9** | **20** | **11** |

---

## 1. BRAKI (I-XX) — czego nadal brakuje

---

### I-01 🔴 KRYTYCZNE — Brak schematu `BriefStatus` w OpenAPI

**Dotyczy:** dok.06 linia 447

**Opis:** Endpoint `GET /projects/{project_id}/briefs` odwołuje się do `$ref: '#/components/schemas/BriefStatus'`, ale schemat `BriefStatus` **nie istnieje** w sekcji `components/schemas`. Zdefiniowany jest jedynie `BriefUploadResult`. Klient API nie wie jaka jest struktura odpowiedzi list briefów.

**Rekomendacja:** Dodaj do dok.06 `components/schemas`:
```yaml
BriefStatus:
  type: object
  required: [id, project_id, filename, format, parse_status, created_at]
  properties:
    id:            { $ref: '#/components/schemas/UUID' }
    project_id:    { $ref: '#/components/schemas/UUID' }
    filename:      { type: string }
    version:       { type: integer }
    format:        { $ref: '#/components/schemas/BriefFormat' }
    word_count:    { type: integer, nullable: true }
    parse_status:  { type: string, enum: [pending, parsed, failed] }
    has_mapping:   { type: boolean }
    created_at:    { type: string, format: date-time }
```

---

### I-02 🔴 KRYTYCZNE — Brak schematu `DocumentEstimate` w OpenAPI

**Dotyczy:** dok.06 linie 1058–1059

**Opis:** Endpoint `GET /reports/compare` odwołuje się do `$ref: '#/components/schemas/DocumentEstimate'` w polach `added_docs` i `removed_docs`, ale schemat `DocumentEstimate` **nie jest zdefiniowany** nigdzie w OpenAPI. Jest opisany w dok.10 §2.4 jako klasa Python, ale nie jako schema OpenAPI.

**Rekomendacja:** Dodaj do dok.06 `components/schemas`:
```yaml
DocumentEstimate:
  type: object
  required: [doc_uid, doc_title, phase_id, h_estimate]
  properties:
    doc_uid:      { type: string }
    doc_title:    { type: string }
    doc_path:     { type: string, nullable: true }
    phase_id:     { type: integer }
    phase_name:   { type: string }
    doc_type:     { type: string }
    confidence:   { type: number, format: float }
    is_required:  { type: boolean }
    h_min:        { type: number, format: float }
    h_likely:     { type: number, format: float }
    h_max:        { type: number, format: float }
```

---

### I-03 🔴 KRYTYCZNE — Brak `project_id` w schemacie `MappingResult` OpenAPI

**Dotyczy:** dok.06 linie 173–189 vs dok.05 §2.2

**Opis:** Kontrakt w dok.05 §2.2 explicite definiuje `MappingResult.project_id: UUID` jako pole wyjściowe. Poprawka F-02 z Rundy 2 potwierdziła potrzebę tego pola. Jednak schemat `MappingResult` w dok.06 **nie zawiera** `project_id` wśród swoich `properties`. Endpoint `POST /reports/estimate/{brief_id}` potrzebuje `project_id` z mapowania aby utworzyć `EstimationReport` z poprawnym `project_id`.

**Rekomendacja:** Dodaj do `MappingResult` w dok.06:
```yaml
project_id: { $ref: '#/components/schemas/UUID' }
```
I dodaj `project_id` do `required` listy tego schematu.

---

### I-04 🔴 KRYTYCZNE — Brak kolumny `response_content` w `llm_calls_log` (cache nie zadziała)

**Dotyczy:** dok.04 §2.10 vs dok.07 §6 vs dok.15 §8 (D4)

**Opis:** Decyzja D4 w dok.15 mówi: „Pełna odpowiedź — umożliwia replay bez LLM". Dok.07 §6 opisuje cache: `_get_cached_response()` zwraca `str | None`. Ale tabela `llm_calls_log` (dok.04 §2.10) **nie ma kolumny na response content**. Przechowuje jedynie `prompt_hash` i metadata. Bez kolumny `response_content TEXT` cache jest bezużyteczny — system może sprawdzić czy prompt był już wywoływany, ale nie odtworzyć odpowiedzi.

**Rekomendacja:** Dodaj do tabeli `llm_calls_log` w dok.04:
```sql
response_content TEXT,          -- pełna odpowiedź LLM (dla cache replay)
```
Oraz indeks: `CREATE INDEX idx_llm_cache ON llm_calls_log(prompt_hash) WHERE status = 'ok';`

---

### I-05 🟡 WAŻNE — Brak response bodies dla błędów w wielu endpointach OpenAPI

**Dotyczy:** dok.06 linie 697–700, 722–724

**Opis:** Wiele endpointów ma odpowiedzi błędów zdefiniowane jedynie jako `description:` bez `content:` z body:
- `POST /brief/upload`: 404, 413, 415, 422 — brak body schematu
- `POST /brief/{id}/map`: 409, 503, 429 — brak body schematu
- `GET /brief/{id}/mapping`: 404 — brak body

Dok.05 §4 definiuje spójny format `ErrorResponse`, ale nie jest on konsekwentnie referencjonowany.

**Rekomendacja:** Dla każdej odpowiedzi błędu w dok.06 dodaj:
```yaml
content:
  application/json:
    schema: { $ref: '#/components/schemas/ErrorResponse' }
```

---

### I-06 🟡 WAŻNE — Brak response schema dla `POST /projects/import`

**Dotyczy:** dok.06 linia 1039

**Opis:** Endpoint importu projektu z ZIP definiuje tylko `'201': {description: Zaimportowany projekt}` bez `content:` — klient nie wie co dostaje w odpowiedzi. Powinien zwracać `Project` (analogicznie do POST /projects).

**Rekomendacja:**
```yaml
'201':
  description: Zaimportowany projekt
  content:
    application/json:
      schema: { $ref: '#/components/schemas/Project' }
```

---

### I-07 🟡 WAŻNE — Brak specyfikacji orchestracji webhook dispatch ↔ async mapping

**Dotyczy:** dok.05 §2.2 (async mapping) + §8 (webhook delivery)

**Opis:** Webhook events `mapping.done` i `mapping.failed` mają triggerować się po zakończeniu mapowania. Async mapping działa jako `asyncio.create_task`. Ale **nigdzie** nie opisano jak task mapowania wywołuje webhook dispatch service po zakończeniu. Brak specyfikacji:
- Kto tworzy instancję `WebhookDispatcher`?
- Jak task tła go wywoła (DI, global registry, event bus)?
- Jak dispatcher dowiaduje się do jakich subskrypcji wysłać (query po project_id)?

**Rekomendacja:** Dodaj do dok.05 sekcję §8.1 opisującą:
```python
# Po zakończeniu background mapping task:
async def _on_mapping_complete(mapping_result: MappingResult):
    subs = await webhook_repo.get_active_subscriptions(
        project_id=mapping_result.project_id,
        event="mapping.done" if mapping_result.status == "done" else "mapping.failed"
    )
    for sub in subs:
        await webhook_dispatcher.enqueue(sub, payload={...})
```

---

### I-08 🟡 WAŻNE — Brak specyfikacji algorytmów `merge_entities` i `deduplicate_entities`

**Dotyczy:** dok.09 §2

**Opis:** Kod SemanticMapper dla briefów multi-chunk wywołuje `merge_entities(all_entities, chunk_entities)` i `deduplicate_entities(all_entities)`, ale te funkcje nie mają specyfikacji:
- Jak rozwiązywane są konflikty `project_type`? (chunk 1 → "greenfield_saas", chunk 2 → "migration")
- Jak deduplikowane są `standards`? (case-insensitive? alias-aware?)
- Czy `phases` to union czy intersection?

**Rekomendacja:** Dodaj do dok.09 §2 specyfikację:
```python
def merge_entities(base: ExtractedEntities, new: ExtractedEntities) -> ExtractedEntities:
    """Union po listach, last-wins po skalarach (project_type)."""
    return ExtractedEntities(
        domains=list(set(base.domains + new.domains)),
        standards=list(set(base.standards + new.standards)),
        regulations=list(set(base.regulations + new.regulations)),
        phases=sorted(set(base.phases + new.phases)),
        keywords=list(set(base.keywords + new.keywords))[:20],
        project_type=new.project_type or base.project_type,  # last-wins
    )
```

---

### I-09 🟡 WAŻNE — Brak pagination dla `GET /planning/{plan_id}/packages`

**Dotyczy:** dok.06 linie 924–950

**Opis:** Endpoint work packages nie ma parametrów paginacji (`page`, `per_page`). Dla dużych projektów (200+ dokumentów) odpowiedź może być bardzo duża. Inne list endpoints (briefs, reports, plans) mają paginację.

**Rekomendacja:** Dodaj parametry `page` i `per_page` (analogicznie do `/projects/{id}/briefs`), header `X-Total-Count`, i wrapper `{items: [...], total: int}`.

---

### I-10 🟡 WAŻNE — Brak 422 response w PATCH work package status

**Dotyczy:** dok.06 linie 952–981 vs dok.05 §7

**Opis:** Dok.05 §7 definiuje state machine z niedozwolonymi przejściami (np. `done → in_progress`) i mówi: „dekorator validate_status_transition rzuca HTTP 422". Ale endpoint PATCH w dok.06 definiuje tylko odpowiedzi 200 i 404 — brak 422.

**Rekomendacja:** Dodaj:
```yaml
"422":
  description: Niedozwolone przejście statusu
  content:
    application/json:
      schema: { $ref: '#/components/schemas/ErrorResponse' }
```

---

### I-11 🟡 WAŻNE — Brak specyfikacji populacji pola `reviewed_by`

**Dotyczy:** dok.04 §2.4 vs dok.05 §2.2 vs dok.06

**Opis:** Tabela `mapping_items` ma kolumnę `reviewed_by TEXT`, ale:
- `MappingItemUpdate` (dok.05/06) nie zawiera pola `reviewed_by`
- Nie opisano skąd ta wartość ma pochodzić (z X-API-Key? z body?)
- Pole nie jest w schemacie OpenAPI MappingItem ani MappingItemUpdate

**Rekomendacja:** Dodaj `reviewed_by` do schematu `MappingItemUpdate` (opcjonalny `str`) lub zdokumentuj automatyczne wypełnianie z prefixu X-API-Key (pierwsze 8 znaków, jak w audit_log).

---

### I-12 🟢 DROBNE — Brak named schema dla WebhookSubscription

**Dotyczy:** dok.06 linie 496–560

**Opis:** Endpointy webhook używają inline schemas zamiast referencji do nazwanego schematu. Utrudnia to generowanie kodu klienta i dokumentację.

**Rekomendacja:** Wyciągnij do named schema `WebhookSubscription` i `WebhookSubscriptionCreate` w `components/schemas`.

---

### I-13 🟢 DROBNE — Brak specification dla retencji danych w `llm_calls_log`

**Dotyczy:** dok.04 §2.10, dok.07 §6

**Opis:** Tabela `llm_calls_log` rośnie z każdym wywołaniem LLM. Brak specyfikacji polityki retencji:
- Jak długo przechowywać logi?
- Czy cache entries (status='cached') mają TTL?
- Kto czyści stare rekordy?

**Rekomendacja:** Dodaj do dok.04 §5 politykę retencji: `DELETE FROM llm_calls_log WHERE created_at < now() - interval '90 days' AND status != 'cached'` jako scheduled job lub migration.

---

### I-14 🟢 DROBNE — Brak specyfikacji formatu `parse_duration_ms` w `briefs.metadata`

**Dotyczy:** dok.08 §8 vs dok.04 §2.2

**Opis:** Dok.08 §8 wymienia `parse_duration_ms` jako metrykę logowaną w `briefs.metadata` JSONB, ale nie jest jasne kto ją mierzy (BriefParser wewnętrznie czy warstwa routera). Nie ma specyfikacji jak `BriefParser.parse()` ma raportować czas.

**Rekomendacja:** Dodaj do `BriefParser.parse()` w dok.08: `metadata["parse_duration_ms"] = elapsed_ms` mierzony wewnątrz metody. Opcjonalnie zwróć w `ParsedBrief.metadata`.

---

## 2. BŁĘDY ZAŁOŻEŃ (J-XX)

---

### J-01 🔴 KRYTYCZNE — Enum `projects.status` niespójny między DB a OpenAPI PATCH

**Dotyczy:** dok.04 §2.1 linia 39–40 vs dok.06 linia 403

**Opis:** Rozbieżność wartości enum:
| Źródło | Dozwolone wartości |
|--------|-------------------|
| DB CHECK (dok.04) | `active`, `archived`, `cancelled` |
| PATCH body (dok.06) | `active`, `on_hold`, `cancelled`, `completed` |

**Konsekwencje:**
- PATCH z `status: "on_hold"` → DB CHECK constraint violation → 500 Internal Server Error
- PATCH z `status: "completed"` → j.w.
- PATCH z `status: "archived"` → nie jest dozwolone przez OpenAPI (brak w enum) choć jest w DB

**Rekomendacja:** Ujednolicić. Jeśli potrzebne są 5 statusów, zmienić CHECK w dok.04:
```sql
CHECK (status IN ('active', 'on_hold', 'archived', 'completed', 'cancelled'))
```
I zaktualizować enum w dok.06 PATCH + GET Schema.

---

### J-02 🔴 KRYTYCZNE — Numeracja faz: 0-based vs 1-based kolizja

**Dotyczy:** dok.02 §1.4 vs dok.07 §5.1 vs dok.06 vs dok.11 §3 vs dok.10 §4

**Opis:** Krytyczna niespójność numerowania faz SDLC:

| Źródło | Numeracja | Zakres |
|--------|-----------|--------|
| dok.02 §1.4 (lista faz) | 1-based | 1–23 (23 fazy) |
| dok.07 §5.1 (LLM prompt) | 0-based | 0–23 (24 fazy: "0=Conception…23=Phase24") |
| dok.06 MappingItem.phase_id | 1-based | `minimum: 1, maximum: 23` |
| dok.11 PHASE_DEFAULT_CONTRACTS | 0-based | klucze: 0,1,2,3,4,5,12,18,22,23 |
| dok.10 CRITICAL_PHASES | niejasne | `{2, 3, 5, 6, 13, 19}` |
| dok.04 mapping_items komentarz | 1-based | "1–23 z itdoc" |
| itdoc DB phases.rowid | 1-based | 1–24 (rowid naturalny) |

LLM prompt mówi agentowi aby zwrócił numery 0–23. OpenAPI waliduje minimum=1, maximum=23. PHASE_DEFAULT_CONTRACTS indeksuje po 0. Jeśli LLM zwróci `phase: 0` (Conception wg promptu), API odrzuci go jako < 1.

**Rekomendacja:** Ustal jednolite mapowanie. Rekomendacja: **1-based (1–24)** spójnie z itdoc DB `phases.rowid`. Zmień:
1. LLM prompt w dok.07 §5.1: numery 1–24
2. PHASE_DEFAULT_CONTRACTS w dok.11: klucze 1–24
3. OpenAPI MappingItem.phase_id: `minimum: 1, maximum: 24`
4. CRITICAL_PHASES w dok.10: zweryfikuj wartości

---

### J-03 🔴 KRYTYCZNE — `ParsedBrief` nie ma `project_id`, a `SemanticMapper` go oczekuje

**Dotyczy:** dok.08 §2 vs dok.09 §7

**Opis:** W dok.09 §7 SemanticMapper.map() zwraca `MappingResult(project_id=brief.project_id, ...)`. Ale `ParsedBrief` (dok.08 §2) nie posiada pola `project_id` — ma tylko `text, metadata, chunks, format, char_count, word_count`.

Klasa `ParsedBrief` jest tworzona przez `BriefParser.parse()` który nie ma dostępu do informacji o projekcie (parsuje surowy plik).

**Rekomendacja:** `project_id` powinien być przekazywany jako osobny parametr do `SemanticMapper.map()`:
```python
async def map(
    self,
    brief: ParsedBrief,
    project_id: UUID,  # ← z tabeli briefs (pobrany przez router)
    confidence_threshold: float = 0.4,
    ...
) -> MappingResult:
```

---

### J-04 🟡 WAŻNE — `briefs.parse_status` enum niezgodny z OpenAPI filter

**Dotyczy:** dok.04 §2.2 linia 73–74 vs dok.06 linia 434

**Opis:**
| Źródło | Dozwolone wartości |
|--------|-------------------|
| DB CHECK (dok.04) | `pending`, `parsed`, `failed` |
| OpenAPI filter enum (dok.06) | `uploaded`, `parsing`, `parsed`, `failed` |

Wartości `uploaded` i `parsing` nie istnieją w DB. Filtrowanie po nich da zawsze pustą listę. Wartość `pending` istnieje w DB ale nie w filtrze API.

**Rekomendacja:** Ujednolicić do jednego zestawu. Jeśli potrzebne są 4 stany (progresja uploadu), zmienić CHECK w dok.04:
```sql
CHECK (parse_status IN ('uploaded', 'parsing', 'parsed', 'failed'))
```
Lub jeśli wystarczą 3, usunąć `uploaded`/`parsing` z dok.06 i zastąpić przez `pending`.

---

### J-05 🟡 WAŻNE — Nazwa kolumny DB `callback_url`/`active` niezgodna z API `target_url`/`is_active`

**Dotyczy:** dok.04 §2.14 vs dok.05 §8 vs dok.06

**Opis:** Dwie kolumny mają różne nazwy w DB vs API:
| DB (dok.04) | API (dok.05/06) |
|------------|----------------|
| `callback_url` | `target_url` |
| `active` | `is_active` |

ORM musi mapować te nazwy, co może powodować subtlene bugi jeśli ktoś zapomni o aliasie.

**Rekomendacja:** Zmień kolumny w dok.04 na `target_url` i `is_active` — spójne z API. Lub dodaj komentarz w dok.04 o wymaganym aliasie w ORM.

---

### J-06 🟡 WAŻNE — `confidence_threshold` domyślne — 4 sprzeczne wartości

**Dotyczy:** dok.05 §2.2 / dok.06 / dok.09 §7–8 / dok.13

**Opis:** Domyślna wartość progu confidence:
| Źródło | Wartość |
|--------|---------|
| dok.05 MapRequest default | 0.6 |
| dok.06 MapRequest schema default | 0.6 |
| dok.09 SemanticMapper.map() default | 0.4 |
| dok.09 .env CONFIDENCE_THRESHOLD_DEFAULT | 0.4 |
| dok.13 .env.example | 0.6 |
| dok.04 app_settings INSERT | 0.6 |

Z Rundy 2 (F-07) zmieniono na 0.4 w dok.09, ale nie zaktualizowano dok.05, dok.06, dok.13, dok.04.

**Rekomendacja:** Ustal jedno źródło prawdy. Rekomendacja: `0.4` dla MVP (jak w dok.09 z uzasadnieniem stanu bazy). Zaktualizować:
- dok.05 §2.2: `confidence_threshold: float = 0.4`
- dok.06 MapRequest: `default: 0.4`
- dok.13 .env.example: `CONFIDENCE_THRESHOLD_DEFAULT=0.4`
- dok.04 app_settings INSERT: `('default_confidence_threshold', '0.4')`

---

### J-07 🟡 WAŻNE — PHASE_DEFAULT_CONTRACTS: komentarz numeracyjny niespójny z kluczami

**Dotyczy:** dok.11 §3

**Opis:** Komentarze w PHASE_DEFAULT_CONTRACTS nie zgadzają się z kluczami:
- Klucz `0` → komentarz `# Phase 1 — Vision/Initiation` (1-based nazwa, 0-based klucz)
- Klucz `12` → komentarz `# Phase 13 — Testing`
- Klucz `18` → komentarz `# Phase 19 — Deployment`
- Klucz `22` → komentarz `# Phase 23 — Maintenance`
- Klucz `23` → komentarz `# Phase 24 — Retirement/Closure`

Ale: faza 18 w dok.02 to "Governance", nie "Deployment". Faza 19 to "Compliance", nie "Deployment". Mapping kluczy do nazw jest **niepoprawny**, co oznacza że kontrakty fallback zostaną przypisane do ZŁYCH faz.

**Rekomendacja:** Zweryfikować mapowanie kluczy z listą faz w dok.02 §1.4 i poprawić. Najlepsza opcja: używaj 1-based numeracji spójnej z `phases.rowid` z itdoc DB.

---

### J-08 🟡 WAŻNE — Liczba szablonów: 7941 vs 7205

**Dotyczy:** dok.01, dok.02 vs dok.12 §0

**Opis:**
- dok.01/02: „7 941 szablonów" (core 7203 + satellite 741 = 7944)
- dok.12: `documents` table ma **7 205 wierszy**

Rozstrzał ~736 dokumentów. Prawdopodobnie: core templates = pliki .md, ale documents table nie indeksuje satellite. Implikacja: SemanticMapper nigdy nie zwróci ~736 szablonów satellite bo ich nie ma w DB.

**Rekomendacja:** Dodaj wyjaśnienie do dok.02 i dok.12: „7941 szablonów plików Markdown, z czego 7205 jest zaindeksowanych w tabeli `documents`; 736 szablonów satellite nie ma wpisów w DB i jest niedostępnych dla SemanticMapper bez dodatkowej indeksacji."

---

### J-09 🟡 WAŻNE — WorkPlanner.create_plan() — bug: `phase_id` undefined in loop

**Dotyczy:** dok.11 §4 linia 287

**Opis:** Kod:
```python
for sequence_order, doc_uid in enumerate(ordered_uids, start=1):
    doc_est = doc_map.get((doc_uid, phase_id))  # ← phase_id UNDEFINED!
```
Zmienna `phase_id` nie jest zdefiniowana w tej pętli. `ordered_uids` to flat list stringów. Lookup w `doc_map` z kluczem `(doc_uid, phase_id)` nie zadziała bo `phase_id` jest nieznane w tym kontekście.

**Rekomendacja:** Zmień `doc_map` na dict indeksowany tylko po `doc_uid` (z dedup na wyższej confidence), LUB zmień `ordered_uids` na listę tupli `(doc_uid, phase_id)` aby zachować composite key.

---

### J-10 🟢 DROBNE — `estimation_reports.status` brak przejścia `accepted → rejected`

**Dotyczy:** dok.05 §7 vs dok.05 §2.3

**Opis:** State machine w §7: `NIEDOZWOLONE: accepted → rejected`. Ale w praktyce PM może chcieć cofnąć decyzję (np. po odkryciu błędu w danych). Brak ścieżki wycofania akceptacji bez tworzenia nowego raportu.

**Rekomendacja:** Albo dodaj explicit path `accepted → revoked` (nowy status), albo udokumentuj workaround: „po akceptacji jedyną opcją korekty jest wygenerowanie nowego raportu z `force_rerun=true`".

---

### J-11 🟢 DROBNE — `doc_path` nigdzie nie istnieje w itdoc DB

**Dotyczy:** dok.12 §0 vs dok.04, dok.09, dok.10

**Opis:** Dok.12 §0 explicite stwierdza: „`documents.path` — kolumna nie istnieje". Mimo to wiele schematów zawiera pole `doc_path`:
- dok.04 mapping_items: `doc_path TEXT`
- dok.06 MappingItem: `doc_path: { type: string, nullable: true }`
- dok.09 RawCandidate: `doc_path: str | None`
- dok.10 _infer_doc_type: przyjmuje `doc_path`

Pole `doc_path` będzie **zawsze NULL** w obecnym stanie bazy. Scoring Jaccard w dok.09 §4 analizuje `candidate.doc_path.split('/')` na wartości None.

**Rekomendacja:** Nie usuwać pola (przydatne gdy DB zostanie wzbogacona), ale:
1. W dok.09 §4: guard `(candidate.doc_path or "").replace(...)` (już jest ale niespójny)
2. W dok.10: `_infer_doc_type` powinien działać poprawnie z `doc_path=None`
3. Udokumentować w dok.12: „doc_path jest rezerwowane na przyszłość; aktualnie zawsze None"

---

## 3. MOŻLIWOŚCI WYKONANIA (K-XX)

---

### K-01 🔴 KRYTYCZNE — `asyncio.create_task` nie przetrwa crashu procesu

**Dotyczy:** dok.05 §2.2

**Opis:** Async mapping używa `asyncio.create_task` + in-memory registry. Jeśli proces FastAPI zostanie zrestartowany (OOM, deploy, crash):
1. Wszystkie running tasks są utracone
2. Rekordy `mapping_results` pozostają ze statusem `running` na zawsze (zombie records)
3. Klient polling `GET /brief/{id}/mapping` nigdy nie zobaczy zakończenia
4. Webhook `mapping.done` nigdy nie będzie wysłany

**Rekomendacja:**
- **v1 minimum:** Dodaj startup job sprawdzający `SELECT * FROM mapping_results WHERE status='running'` → ustaw na `failed` z `error='interrupted by restart'`
- **v2:** Migracja na task queue (Celery, arq, SAQ) z persystencją w DB/Redis

---

### K-02 🔴 KRYTYCZNE — Test integracyjny `test_find_by_standard_iso27001` zawsze padnie

**Dotyczy:** dok.14 §6 vs dok.12 §0

**Opis:** Test (dok.14 §6):
```python
async def test_find_by_standard_iso27001(self, itdoc_connector):
    results = await itdoc_connector.find_by_standard("ISO/IEC 27001")
    assert len(results) > 0  # ← ZAWSZE FAILUJE
```
Dok.12 §0 potwierdza: tabela `doc_standard_mapping` **nie istnieje**. `find_by_standard()` zwróci `[]`.

**Rekomendacja:** Zmień test na:
```python
async def test_find_by_standard_graceful_empty(self, itdoc_connector):
    results = await itdoc_connector.find_by_standard("ISO/IEC 27001")
    assert isinstance(results, list)  # Nie rzuca wyjątku, zwraca []
```
Dodaj osobny test warunkowy `@pytest.mark.skipif(not HAS_STANDARDS_TABLE)`.

---

### K-03 🟡 WAŻNE — ZIP export może zużyć nadmiar pamięci

**Dotyczy:** dok.06 `/projects/{project_id}/export`

**Opis:** Export obejmuje: project.json + briefs/ (z `raw_content BYTEA` — do 50MB per brief) + mappings/ + reports/ + plans/. Dla projektu z 5 briefami PDF → potencjalnie 250MB w pamięci podczas budowy ZIP.

**Rekomendacja:**
- Użyj streaming ZIP (`zipfile.ZipFile` z `io.BytesIO` per chunk lub `StreamingResponse`)
- Dodaj limit: max 100MB eksportu; powyżej → HTTP 413
- Opcjonalnie: `?exclude_raw_content=true` do eksportu bez binarnych plików

---

### K-04 🟡 WAŻNE — `BriefParser.parse()` synchroniczny w async context

**Dotyczy:** dok.08 §2–3

**Opis:** `BriefParser` jest klasą synchroniczną (`def parse`, `def detect_format`). Parsowanie PDF 50MB przez pdfplumber może trwać sekundy — blokując event loop. Dok.12 używa `run_in_executor` dla itdoc (sync lib), ale analogiczny wzorzec nie jest opisany dla BriefParser.

**Rekomendacja:** Dodaj do dok.08: „BriefParser.parse() uruchamiany przez `asyncio.run_in_executor(None, parser.parse, content, format)` w routerze Side 2, analogicznie do ItdocConnector."

---

### K-05 🟡 WAŻNE — `FLOAT4[]` w Alembic wymaga specjalnej obsługi

**Dotyczy:** dok.16 §5.3

**Opis:** Tabela `document_embeddings` używa `FLOAT4[] NOT NULL` — PostgreSQL array type. Alembic autogenerate nie generuje poprawnych migracji dla natywnych typów array. Opcjonalne użycie `pgvector` wymaga instalacji extension.

**Rekomendacja:** W dok.16 dodaj:
```python
# W migration 0007_embeddings:
from sqlalchemy import Column, Text, ARRAY, Float
from sqlalchemy.dialects.postgresql import TIMESTAMP

op.create_table('document_embeddings',
    sa.Column('doc_uid', sa.Text(), primary_key=True),
    sa.Column('embedding', ARRAY(Float), nullable=False),
    ...
)
```
I notatkę: „Migracja wymaga PostgreSQL ≥ 12 dla ARRAY type. pgvector jest opcjonalny."

---

### K-06 🟡 WAŻNE — Compare reports bez limitów może być wolne

**Dotyczy:** dok.06 `/reports/compare`

**Opis:** Endpoint wymaga pobrania dwóch pełnych raportów z ich `report_phase_items` i `mapping_items` aby zbudować diff. Dla raportów z 200 docs każdy → 400 mapping items + 48 phase items. Brak limitu ile raportów użytkownik może porównywać i brak cache.

**Rekomendacja:**
- Ogranicz do raportów tego samego projektu (`project_id` check)
- Cache wyników porównania (hash dwóch report_id → cached diff)
- Rozważ lazy loading: najpierw totals diff, potem `?include_details=true`

---

### K-07 🟢 DROBNE — Webhook retry state nie jest persystowany

**Dotyczy:** dok.05 §8

**Opis:** Polityka retry (3 próby, exponential backoff) wymaga śledzenia ile prób już było. Przy `asyncio.create_task` te dane żyją w pamięci — crash procesu = utrata stanu retry. Webhook może nie być dostarczony ani zdezaktywowany.

**Rekomendacja:** Dodaj tabelę `webhook_delivery_log` lub kolumnę `last_attempt_at`, `attempt_count` w `webhook_subscriptions`. Startup recovery job sprawdza pending deliveries.

---

### K-08 🟢 DROBNE — Brak specyfikacji timeoutu dla ZIP import

**Dotyczy:** dok.06 `POST /projects/import`

**Opis:** Import projektu z ZIP może zawierać setki rekordów do wstawienia (briefs, mappings, items, reports, plans, packages). Brak limitu rozmiaru ZIP, brak timeoutu, brak transakcji specyfikacji (atomowy import czy partial?).

**Rekomendacja:** Dodaj do dok.05/06:
- Max ZIP size: 200MB
- Import w jednej transakcji DB (atomowy: albo wszystko albo nic)
- Timeout: 120s
- Walidacja struktury ZIP przed importem

---

## 4. PROPOZYCJE ROZWINIĘCIA (L-XX)

---

### L-01 🟡 WAŻNE — Dry-run mode dla estimation i planning

**Dotyczy:** dok.05 §2.3, §2.4

**Opis:** POST /reports/estimate i POST /planning/create tworzą rekordy w DB. Brak trybu podglądu bez persystencji. PM nie może zobaczyć kosztorysu „na próbę" z innymi parametrami bez tworzenia draftu.

**Rekomendacja:** Dodaj `?dry_run=true` query param:
- Nie tworzy rekordu w DB
- Zwraca taki sam kształt odpowiedzi ale z `id: null`
- Pozwala testować różne `confidence_threshold` i `include_phases` bez zaśmiecania DB

---

### L-02 🟡 WAŻNE — Cache layer dla wyników mapowania (content-hash based)

**Dotyczy:** dok.09

**Opis:** Mapowanie jest najdroższą operacją (LLM call). `force_rerun=False` sprawdza czy istnieje wynik, ale nie porównuje content. Jeśli ten sam brief jest wgrywany ponownie (np. po fix literówki) — nowy `brief_id`, nowe mapowanie, nowy koszt.

**Rekomendacja:** Dodaj `content_hash = SHA256(parsed_text + confidence_threshold + max_results)` do `mapping_results`. Przy `force_rerun=False`: sprawdź czy istnieje wynik z takim samym `content_hash` (cross-brief cache). Oszczędza LLM calls.

---

### L-03 🟡 WAŻNE — Health endpoint: informacja o stanie danych itdoc

**Dotyczy:** dok.06 `/health`

**Opis:** Aktualny `/health` zwraca `itdoc: ok/error`. Nie mówi jakie tabele są dostępne — operator nie wie czy system działa w trybie fallback (keyword-only) czy pełnym (standards + regulations + rhythm).

**Rekomendacja:** Rozszerz `/health`:
```json
{
  "status": "ok",
  "db": "ok",
  "itdoc": {
    "status": "degraded",
    "documents": 7205,
    "standards_available": false,
    "rhythm_edges_count": 0,
    "contracts_available": false,
    "mapping_mode": "keyword_fallback"
  }
}
```

---

### L-04 🟢 DROBNE — Rate limiting per projekt

**Dotyczy:** dok.13 §7

**Opis:** Aktualny rate limit to semaphore na LLM calls (global). Jeden projekt z dużym briefem może zablokować LLM dla pozostałych.

**Rekomendacja:** Dodaj `project_settings` klucz `rate_limit.mapping_per_hour = 10` (domyślnie bez limitu). Sprawdzaj w routerze: `SELECT count(*) FROM mapping_results WHERE project_id=? AND created_at > now() - interval '1 hour'`.

---

### L-05 🟢 DROBNE — Progressive enhancement metrics

**Dotyczy:** dok.16 §7

**Opis:** Dok.16 definiuje metryki jakości (precision@10, recall, empty_rate), ale brak mechanizmu automatycznego śledzenia jak te metryki zmieniają się w czasie (np. po populate_standards, po włączeniu embeddings).

**Rekomendacja:** Dodaj tabelę `mapping_quality_snapshots`:
```sql
CREATE TABLE mapping_quality_snapshots (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    measured_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    precision_at_10 NUMERIC(4,3),
    recall NUMERIC(4,3),
    avg_confidence NUMERIC(4,3),
    empty_rate NUMERIC(4,3),
    config_snapshot JSONB,  -- {embedding_enabled, standards_count, ...}
    notes TEXT
);
```

---

### L-06 🟢 DROBNE — Metryki biznesowe systemu

**Dotyczy:** cały system

**Opis:** System nie zbiera metryk biznesowej wartości. Brak danych do odpowiedzi na pytania: „Ile czasu zaoszczędziliśmy?", „Jaki jest ROI systemu?", „Ile projektów przetworzyliśmy?"

**Rekomendacja:** Zbieraj w `app_metrics` lub dashboardzie:
| Metryka | Źródło |
|---------|--------|
| Projekty utworzone/miesiąc | `COUNT(projects WHERE created_at > ...)` |
| Czas brief→mapping (p50/p95) | `mapping_results.completed_at - briefs.created_at` |
| Koszt LLM per mapowanie | `SUM(input_tokens+output_tokens) FROM llm_calls_log WHERE entity_id=?` |
| Report acceptance rate | `accepted / (accepted + rejected)` |
| Average project complexity | `AVG(complexity_level::int)` |
| Work packages completed/total | `done / total per plan` |

---

### L-07 🟢 DROBNE — Dodanie dry-run do WorkPlanner

**Dotyczy:** dok.11, dok.06

**Opis:** PM może chcieć zobaczyć plan pracy przed akceptacją raportu — np. aby ocenić czy podział na task-units jest sensowny zanim zablokuje dalsze modyfikacje.

**Rekomendacja:** Endpoint `POST /planning/preview/{report_id}?dry_run=true`:
- Nie wymaga statusu `accepted` na raporcie
- Nie tworzy rekordów w DB
- Zwraca `WorkPlan` z `packages[]` w formacie identycznym jak `POST /planning/create`
- Oznaczony jako `status: "preview"` (nie "draft")

---

## Podsumowanie priorytetów implementacyjnych

### Blokujące implementację (naprawić PRZED kodowaniem):

| ID | Problem | Wpływ |
|----|---------|-------|
| **J-02** | Fazy 0-based vs 1-based | LLM zwróci złe phase_id, walidacja API odrzuci |
| **J-01** | Project status enum mismatch | PATCH rzuci 500 |
| **J-03** | ParsedBrief bez project_id | SemanticMapper crash: AttributeError |
| **I-01** | Brak BriefStatus schema | Codegen API client nie wygeneruje kodu |
| **I-02** | Brak DocumentEstimate schema | j.w. |
| **I-04** | Brak response_content w cache | LLM cache nie działa = podwójne koszty |
| **K-01** | asyncio crash = zombie records | Running tasks nigdy nie zakończą się |
| **K-02** | Test always fails | CI pipeline broken od startu |

### Ważne (naprawić w trakcie implementacji):

| ID | Problem |
|----|---------|
| **I-03** | MappingResult.project_id brak w OpenAPI |
| **I-05** | Error bodies missing w OpenAPI |
| **J-04** | parse_status enum mismatch |
| **J-05** | Webhook kolumny callback_url/active vs API |
| **J-06** | confidence_threshold 4 sprzeczne wartości |
| **J-07** | PHASE_DEFAULT_CONTRACTS złe mapowanie faz |
| **J-09** | WorkPlanner phase_id undefined bug |

---

*Raport wygenerowany automatycznie. Runda 3 z 3.*
