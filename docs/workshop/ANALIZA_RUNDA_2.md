# Raport Analityczny — Runda 2
## System "Warsztat" (AI Documentation Workshop)

**Data:** 2025-01-14  
**Zakres:** Dokumenty 01–16, cross-referencyjna analiza spójności  
**Analityk:** AI Architect  

---

## Podsumowanie znalezisk

| Kategoria | 🔴 Krytyczne | 🟡 Ważne | 🟢 Drobne | Razem |
|-----------|-------------|---------|---------|-------|
| **E — Braki** | 3 | 5 | 4 | 12 |
| **F — Błędy założeń** | 3 | 4 | 2 | 9 |
| **G — Problemy wykonalności** | 2 | 4 | 2 | 8 |
| **H — Propozycje rozwinięcia** | 0 | 4 | 5 | 9 |
| **Razem** | **8** | **17** | **13** | **38** |

---

## E — BRAKI (czego brakuje)

---

### E-01 🔴 KRYTYCZNE — Brak specyfikacji asynchronicznego przetwarzania mapowania

**Dotyczy:** dok.05, dok.06, dok.09

**Problem:**  
`POST /brief/{id}/map` zwraca HTTP 202 (Accepted) w OpenAPI (dok.06, linia 536), co sugeruje przetwarzanie asynchroniczne. Jednak:
- Kontrakt w dok.05 §2.2 definiuje zwracanie pełnego `MappingResult` synchronicznie (z `status: "done"|"failed"`)
- Nie ma specyfikacji mechanizmu background task (Celery? `asyncio.create_task`? ARQ?)
- Nie ma endpointu do pollingu statusu — `GET /brief/{id}/mapping` zwraca wynik, ale nie ma pola "processing" ani ETA
- Przy wielochunkowym briefie (word_count > 3000) mapowanie może trwać > 60 sekund (wiele wywołań LLM)

**Rekomendacja:**  
Dodać do dok.05 i dok.06:
1. Mechanizm background task (rekomendacja: `asyncio.create_task` + in-memory registry dla v1)
2. Status `"running"` w odpowiedzi 202 (jest w OpenAPI schema, ale nie w kontrakcie dok.05)
3. Endpoint pollingowy lub zmiana `GET /brief/{id}/mapping` aby zwracał `{status: "running"}` gdy przetwarzanie trwa
4. Opcjonalny `Retry-After` header w 202 response

---

### E-02 🔴 KRYTYCZNE — Brak endpointów listujących (briefs, reports per projekt)

**Dotyczy:** dok.06

**Problem:**  
OpenAPI definiuje `GET /projects` (lista projektów) ale brakuje:
- `GET /projects/{project_id}/briefs` — lista briefów per projekt
- `GET /projects/{project_id}/reports` — lista raportów per projekt  
- `GET /projects/{project_id}/plans` — lista planów per projekt

Bez tych endpointów AI Agent (P1) nie może:
- Sprawdzić historii briefów i mapowań
- Pobrać listy raportów do akceptacji
- Zobaczyć wszystkich planów pracy

Jedyny sposób to zapamiętać UUID z oryginalnego POST response — co jest kruche.

**Rekomendacja:**  
Dodać do dok.06 endpointy:
```yaml
GET /projects/{project_id}/briefs?status=parsed&page=1&per_page=20
GET /projects/{project_id}/reports?status=draft
GET /projects/{project_id}/plans
```
Dodać paginację (`page`, `per_page`, `total_count` w response header) do istniejących list (`GET /ingestion/jobs`, `GET /planning/{plan_id}/packages`).

---

### E-03 🔴 KRYTYCZNE — Brak specyfikacji dostarczania webhooków

**Dotyczy:** dok.04, dok.05

**Problem:**  
Tabela `webhook_subscriptions` (dok.04 §2.14) definiuje zdarzenia (`mapping.done`, `report.ready`, etc.) ale nie istnieje żaden dokument opisujący:
- Mechanizm dostarczania (HTTP POST z JSON payload)
- Politykę retry (ile prób, backoff)
- Timeout na dostarczenie
- Podpis HMAC (pole `secret_hash` istnieje w tabeli, ale nie ma specyfikacji algorytmu)
- Rejestrację webhooka (brak endpointu `POST /webhooks` w OpenAPI)
- Format payload per event type

**Rekomendacja:**  
Dodać sekcję "Webhook Delivery Spec" do dok.05 lub osobny dokument:
- Delivery: HTTP POST z `Content-Type: application/json`
- Podpis: `X-Workshop-Signature: sha256=HMAC(secret, body)`
- Retry: 3 próby, exponential backoff (5s, 30s, 300s)
- Timeout: 10s per attempt
- Endpointy CRUD w OpenAPI: `POST/GET/DELETE /projects/{id}/webhooks`

---

### E-04 🟡 WAŻNE — Brak specyfikacji walidacji przejść stanów (state machine)

**Dotyczy:** dok.04, dok.05, dok.06

**Problem:**  
Kilka encji ma statusy (briefs.parse_status, mapping_results.status, estimation_reports.status, work_plans.status, work_packages.status, ingestion_jobs.status) ale nie ma specyfikacji dozwolonych przejść. Na przykład:
- Czy `work_package` może przejść z `done` → `in_progress` (rework)?
- Czy `work_plan` może przejść z `completed` → `active` (reopen)?
- Czy `ingestion_job` z `rejected` → `review` (ponowna ocena)?
- Endpoint `PATCH /planning/{plan_id}/packages/{id}/status` przyjmuje dowolny status — brak walidacji przejścia

**Rekomendacja:**  
Dodać do dok.05 diagram stanów per encja. Minimalnie:
```
work_package: pending → in_progress → done | blocked
              blocked → pending (po usunięciu blokera)
              NIEDOZWOLONE: done → in_progress (wymaga nowego planu)

ingestion_job: pending → generating → review → approved | rejected
               NIEDOZWOLONE: approved → rejected
```
W implementacji: dekorator/guard `validate_transition(current, target)`.

---

### E-05 🟡 WAŻNE — Brak Docker Compose specification

**Dotyczy:** dok.03, dok.13, dok.15

**Problem:**  
Wszystkie dokumenty odwołują się do Docker Compose (dok.03 §5, dok.13 §4, dok.15 §2) jako metody uruchomienia, ale żaden nie definiuje:
- Serwisy (fastapi, db, opcjonalnie ollama)
- Wolumeny (itdoc read-only mount, postgres data)
- Sieci (izolacja PostgreSQL)
- Healthchecks kontenerów
- Zmienne środowiskowe w kontenerze

**Rekomendacja:**  
Dodać sekcję do dok.03 lub dok.13 z minimalnym `docker-compose.yml`:
```yaml
services:
  api:
    build: .
    volumes:
      - ../:/app/itdoc_library:ro
    depends_on:
      db: {condition: service_healthy}
  db:
    image: postgres:16-alpine
    healthcheck: ...
```

---

### E-06 🟡 WAŻNE — Brak endpoint DELETE/PATCH na projektach

**Dotyczy:** dok.06

**Problem:**  
OpenAPI definiuje `POST /projects` i `GET /projects/{id}` ale brak:
- `PATCH /projects/{id}` — zmiana nazwy, statusu, opisu
- `DELETE /projects/{id}` — usunięcie projektu (z kaskadą)

Projekt może mieć status `cancelled` (dok.04 §2.1) ale nie ma sposobu na ustawienie tego statusu przez API.

**Rekomendacja:**  
Dodać do dok.06:
```yaml
PATCH /projects/{project_id}:  # {name?, status?, description?}
DELETE /projects/{project_id}: # CASCADE na briefs→mappings→reports→plans
```

---

### E-07 🟡 WAŻNE — Brak specyfikacji `_infer_doc_type()` i `_domain_multiplier()`

**Dotyczy:** dok.10

**Problem:**  
Estimation Engine (dok.10 §2.4) używa dwóch funkcji krytycznych dla wyliczeń:
- `_infer_doc_type(doc_title, doc_path)` — brak algorytmu; jak mapujemy tytuł "Plan audytu bezpieczeństwa" na klucz `"audit"` z `DOCUMENT_TYPE_POINTS`? Pattern matching? Substring? LLM?
- `_domain_multiplier(domains: list[str])` — jak agregować wiele domen? `max()`? `mean()`? Jeśli brief ma `["fintech", "healthcare"]` to mnożnik = 1.3 czy 1.4 czy 1.3*1.4=1.82?

Deweloper musi zgadywać implementację tych funkcji.

**Rekomendacja:**  
Dodać do dok.10:
```python
def _infer_doc_type(title: str, path: str | None) -> str:
    """Matching: sprawdź czy dowolny klucz z DOCUMENT_TYPE_POINTS
    jest substringiem title.lower(). Kolejność priorytetu jak w słowniku.
    Fallback: 'default'."""

def _domain_multiplier(domains: list[str]) -> float:
    """Bierz max() z mnożników. ['fintech','healthcare'] → 1.4"""
```

---

### E-08 🟡 WAŻNE — Brak obsługi częściowych wyników LLM

**Dotyczy:** dok.09, dok.15

**Problem:**  
Roadmap (dok.15 §8, decyzja D3) rekomenduje "częściowe wyniki z `status='partial'`" gdy LLM timeout nastąpi w trakcie mapowania. Ale:
- Status `"partial"` nie istnieje w schemacie mapping_results (dok.04: enum `pending|running|done|failed`)
- Status `"partial"` nie istnieje w OpenAPI MappingResult schema (dok.06)
- Dok.09 (SemanticMapper) nie implementuje logiki częściowych wyników
- Nie jest jasne co jest "częściowe" — wyniki z 2/5 chunków? Z keyword fallback bez LLM?

**Rekomendacja:**  
Wybrać jedną ścieżkę i udokumentować:
- **Opcja A:** Dodać `status='partial'` do schematu DB i OpenAPI + `partial_reason` field
- **Opcja B:** Przy timeout zwracać `status='done'` z niższym `avg_confidence` i flagą w metadata

---

### E-09 🟢 DROBNE — Brak specyfikacji logowania strukturalnego

**Dotyczy:** dok.13

**Problem:**  
Dok.13 §6 definiuje middleware logujący requesty ale brakuje:
- Formatu logów (JSON structured? Plain text?)
- Poziomów logowania per komponent
- Korelacji logów (request_id propagation)
- Konfiguracji log level przez .env

**Rekomendacja:**  
Dodać do dok.13: `LOG_FORMAT=json`, `LOG_LEVEL=INFO`, middleware propagujący `X-Request-ID` lub generujący `request_id` w response headers.

---

### E-10 🟢 DROBNE — Brak PHASE_DEFAULT_CONTRACTS dla faz 4–23

**Dotyczy:** dok.11

**Problem:**  
Dok.11 §3 Etap 3 definiuje fallback kontrakty tylko dla faz 1–3 z komentarzem `# ... (pełna tabela dla wszystkich 23 faz)`. Deweloper musi sam wymyślić domyślne inputs/outputs/gates dla 20 faz, co jest istotne bo tabela `contracts` w itdoc DB nie istnieje.

**Rekomendacja:**  
Uzupełnić słownik `PHASE_DEFAULT_CONTRACTS` w dok.11 przynajmniej dla faz krytycznych (2, 3, 5, 6, 13, 19) z konkretnymi wartościami inputs/outputs/gates.

---

### E-11 🟢 DROBNE — Brak STANDARD_ALIASES pełnej listy

**Dotyczy:** dok.09

**Problem:**  
Dok.09 §2 definiuje 7 aliasów z komentarzem `# ... (~150 aliasów)`. Deweloper nie ma źródła do ekstrakcji pozostałych ~143 aliasów.

**Rekomendacja:**  
Dodać plik `workshop/data/standard_aliases.json` z pełną mapą. Alternatywnie: algorytm normalizacji (lowercase + strip whitespace + usunięcie separatorów) + fuzzy matching na tabeli `standards` z itdoc.

---

### E-12 🟢 DROBNE — Brak specyfikacji audit_log populacji

**Dotyczy:** dok.04, dok.05

**Problem:**  
Tabela `audit_log` (dok.04 §2.13) jest zdefiniowana ale żaden kontrakt w dok.05 nie określa KIEDY wpisy są tworzone. Brak dekoratora/middleware automatyzującego zapis.

**Rekomendacja:**  
Dodać do dok.05 sekcję "Audit Points":
- `POST /reports/{id}/accept` → audit_log(entity_type='estimation_report', action='accept')
- `POST /reports/{id}/reject` → audit_log(entity_type='estimation_report', action='reject')
- `POST /ingestion/{id}/approve` → audit_log(entity_type='ingestion_job', action='approve_template')
- `PUT /brief/{id}/mapping/{item_id}` → audit_log(entity_type='mapping_item', action='manual_review')

---

## F — BŁĘDY ZAŁOŻEŃ

---

### F-01 🔴 KRYTYCZNE — Niespójność 23 vs 24 faz SDLC

**Dotyczy:** dok.02, dok.04, dok.05, dok.06, dok.07, dok.10, dok.11, dok.12, dok.15

**Problem:**  
Fundamentalna rozbieżność w liczbie faz SDLC:

| Dokument | Liczba faz | Kontekst |
|----------|-----------|----------|
| dok.02 §1.4 | **23** | Lista faz z nazwami |
| dok.03 §3 | **23** | "grupuje po 23 fazach SDLC" |
| dok.04 §2.4 | **1–23** | `mapping_items.phase_id` komentarz |
| dok.05 §3.3 | **23** | "Pełna lista 23 faz SDLC" |
| dok.05 §2.1 | **1-24** | `local_templates_index.phase_id` komentarz |
| dok.06 | **1–23** | `MappingItem.phase_id: {maximum: 23}` |
| dok.07 §5.1 | **1-23** | Prompt template: "numery 1-23" |
| dok.10 §4 | **23** | "23 fazy z itdoc" |
| dok.12 §0 | **24** | "tabela `phases` ma 24 wiersze" |
| dok.15 Faza 0 | **24** | "get_phases() zwraca 24 fazy" |

**Faktyczny stan:** Tabela `phases` w `it_doc_matrix.db` ma **24 wiersze** (potwierdzone w dok.12 §0 i dok.16 §1.2).

**Konsekwencje:**
- OpenAPI walidacja `phase_id maximum: 23` odrzuci fazę 24
- Prompt LLM instruuje "numery 1-23" więc LLM nigdy nie zasugeruje fazy 24
- `CRITICAL_PHASES` w dok.10 pomija potencjalnie ważne fazy
- Testy mogą failować (`assert len(phases) == 23` vs faktyczne 24)

**Rekomendacja:**  
1. Sprawdzić jaka jest 24. faza w tabeli `phases` (nazwa, ordinal)
2. Zaktualizować WSZYSTKIE dokumenty do jednej prawdy (prawdopodobnie 24)
3. Zmienić OpenAPI: `phase_id maximum: 24`
4. Zmienić prompt LLM: dodać fazę 24
5. Dodać test: `assert len(phases) == get_actual_phase_count()` (nie hardcodowany)

---

### F-02 🔴 KRYTYCZNE — `MappingResult` nie posiada `project_id` — EstimationEngine crashnie

**Dotyczy:** dok.05, dok.09, dok.10

**Problem:**  
Estimation Engine (dok.10 §6, linia 351) odwołuje się do:
```python
project_id=mapping.project_id,   # przekazywane z MappingResult
```

Ale `MappingResult` (dok.05 §2.2, dok.09 §7) **nie ma pola `project_id`**. Ma jedynie `brief_id`. Pole `project_id` jest dostępne tylko przez join: `mapping_results.brief_id → briefs.project_id`.

**Konsekwencje:**  
- `AttributeError: 'MappingResult' object has no attribute 'project_id'` w runtime
- `EstimationReport` nie może być poprawnie zapisany (wymaga `project_id` jako FK)

**Rekomendacja:**  
Wybrać jedno podejście:
- **Opcja A (prostsza):** Dodać `project_id` do `MappingResult` — resolver pobiera z briefs przy tworzeniu
- **Opcja B (czystsza):** `EstimationEngine.calculate()` przyjmuje dodatkowy parametr `project_id: UUID`; router resolwuje z DB: `SELECT project_id FROM briefs WHERE id = (SELECT brief_id FROM mapping_results WHERE id = ?)`

---

### F-03 🔴 KRYTYCZNE — `doc_uid` w workshop to stringify(integer), nie semantyczny UID

**Dotyczy:** dok.04, dok.09, dok.11, dok.12

**Problem:**  
Specyfikacje (dok.09 §9 example, dok.11 §5 example) pokazują `doc_uid` jako semantyczne stringi:
```json
"doc_uid": "core_security_audit_0042"
```

Ale faktyczna baza `it_doc_matrix.db` ma kolumnę `documents.doc_id` (INTEGER, nie TEXT). Connector w dok.12 §3.6 konwertuje:
```python
doc_uid=str(r[0]),       # doc_id jako string uid
```

Więc faktyczny `doc_uid` to `"42"`, nie `"core_security_audit_0042"`. To powoduje:
- Jaccard scoring na `doc_uid` jest bezwartościowy (integer string vs keywords)
- Przykłady w dokumentacji są mylące dla dewelopera
- Debugowanie będzie utrudnione (UUID-like identifiers w DB ale `"42"` z itdoc)

**Rekomendacja:**  
1. Zweryfikować strukturę kolumny `doc_id` w `it_doc_matrix.db`
2. Jeśli `doc_id` to integer — zaktualizować wszystkie przykłady w dok.09, dok.11 do prawdziwego formatu
3. Rozważyć composite UID: `f"{branch_name}_{phase_id}_{doc_id}"` dla czytelności
4. Dodać konwencję nazewnictwa `doc_uid` do dok.12 §2

---

### F-04 🟡 WAŻNE — Contradykcja ADR-01 vs populate_itdoc_db.py

**Dotyczy:** dok.03, dok.16

**Problem:**  
ADR-01 w dok.03 §7 mówi jasno:
> "Warsztat **nigdy nie pisze** do `it_doc_matrix.db` ani nie modyfikuje plików szablonów."

Ale dok.16 §3 definiuje skrypt `populate_itdoc_db.py` który INSERT-uje do `it_doc_matrix.db`:
> "To jedyne «zapisy» do it_doc_matrix.db które są dozwolone: CREATE VIEW + INSERT do pustych tabel."

Te dwa stanowiska są wzajemnie sprzeczne. Deweloper nie wie, która zasada obowiązuje.

**Rekomendacja:**  
Zaktualizować ADR-01 w dok.03 aby explicite wydzielić wyjątek:
> "Warsztat (runtime) nigdy nie pisze do it_doc_matrix.db. **Wyjątek:** skrypt maintenance `populate_itdoc_db.py` (offline, jednorazowy) może INSERT OR IGNORE do pustych tabel. Nigdy UPDATE/DELETE."

Dodać tę samą adnotację do dok.16.

---

### F-05 🟡 WAŻNE — OpenAPI RejectRequest na `/reports/{id}/reject` brakuje requestBody

**Dotyczy:** dok.05, dok.06

**Problem:**  
Kontrakt w dok.05 §2.3 definiuje:
```
Input: RejectRequest { reason: str | None }
```

Ale OpenAPI (dok.06, linie 681–697) endpoint `/reports/{report_id}/reject` **nie ma `requestBody`**. Jednocześnie schema `RejectRequest` (dok.06, linia 118) ma `reason` jako **required**.

Potrójny konflikt:
1. Dok.05: `reason` jest `str | None` (opcjonalny)
2. Dok.06 schema: `reason` jest `required`  
3. Dok.06 endpoint: brak `requestBody`

**Rekomendacja:**  
Dodać do OpenAPI endpoint `/reports/{report_id}/reject`:
```yaml
requestBody:
  content:
    application/json:
      schema: { $ref: '#/components/schemas/RejectRequest' }
```
I ujednolicić: `reason` jako opcjonalny (`nullable: true`, usunąć z `required`).

---

### F-06 🟡 WAŻNE — ApproveRequest brak pola `index_for_mapping` w OpenAPI

**Dotyczy:** dok.05, dok.06

**Problem:**  
Kontrakt dok.05 §2.1 definiuje `ApproveRequest` z polem:
```
index_for_mapping: bool = true  # czy dodać do local_templates_index?
```

Ale OpenAPI schema `ApproveRequest` (dok.06, linia 111–115) ma tylko `save_path`. Pole `index_for_mapping` jest pominięte.

**Konsekwencja:**  
Klient API nie może kontrolować czy zatwierdzony szablon trafia do indeksu. Funcjonalność `local_templates_index` jest nieosiągalna przez API.

**Rekomendacja:**  
Dodać do OpenAPI `ApproveRequest`:
```yaml
index_for_mapping: { type: boolean, default: true }
```

---

### F-07 🟡 WAŻNE — Keyword fallback przy domyślnym progu daje za niskie confidence

**Dotyczy:** dok.09

**Problem:**  
Analiza scoringu z dok.09 §4 przy samym keyword fallback (bez danych w tabelach mapowań):
- `source_score` = 1 unikalny typ / 6.0 = **0.167** (tylko `keyword_fallback`)
- `keyword_score` = realistycznie **0.05–0.15** (Jaccard na tytułach jest niski)
- `phase_score` = **0.2** (jeśli faza się zgadza) lub **0.0**

Sumaryczny confidence: **0.2–0.52**. Domyślny próg `CONFIDENCE_THRESHOLD_DEFAULT=0.6`.

**Konsekwencja:**  
W aktualnym stanie bazy (bez tabel mapowań), **większość kandydatów z keyword fallback będzie poniżej progu 0.6** i zostanie odfiltrowana. `MappingResult.total_items` będzie bliskie 0 mimo że `find_by_keyword()` zwraca wyniki.

**Rekomendacja:**  
1. Zwiększyć wagę `keyword_fallback` w source_score (np. 0.2 zamiast 1/6=0.167)
2. LUB zmniejszyć domyślny `CONFIDENCE_THRESHOLD_DEFAULT` do 0.4 dla MVP
3. LUB dodać mechanizm auto-adjustu progu: jeśli wynik < 10 items → retry z threshold -= 0.1
4. Dodać tę kalkulację do dok.09 jako "Uwaga implementacyjna"

---

### F-08 🟢 DROBNE — Testowy `test_critical_phases_included` używa `await` w sync def

**Dotyczy:** dok.14

**Problem:**  
Dok.14 §5.2 (linia 303–307):
```python
def test_critical_phases_included(self, engine, mock_mapping_result):
    report = await engine.calculate(mock_mapping_result)  # ← await w sync def!
```

Trzy testy EstimationEngine (`test_critical_phases`, `test_deduction_basis`, `test_total_h`) są zdefiniowane jako `def` ale używają `await`. W pytest-asyncio `asyncio_mode = "auto"` to nadal wymaga `async def`.

**Rekomendacja:**  
Zmienić na `async def test_critical_phases_included(...)`.

---

### F-09 🟢 DROBNE — Testowy expect `len(phases) == 23` sprzeczny z faktycznym stanem

**Dotyczy:** dok.14

**Problem:**  
Dok.14 §6 (linia 389):
```python
async def test_get_phases_returns_23(self, itdoc_connector):
    phases = await itdoc_connector.get_phases()
    assert len(phases) == 23
```

Ale tabela `phases` ma 24 wiersze (dok.12, dok.16). Test będzie failował.

**Rekomendacja:**  
Zmienić na `assert len(phases) >= 23` lub `assert len(phases) == 24` (po ustaleniu faktycznej liczby).

---

## G — PROBLEMY WYKONALNOŚCI

---

### G-01 🔴 KRYTYCZNE — SQL injection w `find_by_keyword()`

**Dotyczy:** dok.12

**Problem:**  
Dok.12 §3.6 buduje SQL query przez f-string interpolację:
```python
conditions = " OR ".join(
    f"LOWER(d.title) LIKE LOWER('%{kw.replace(\"'\", \"''\")}%')"
    for kw in keywords[:20]
)
```

Zamiana `'` na `''` to **niewystarczające** zabezpieczenie. Atakujący (lub LLM generujący keywords z briefu) może wstrzyknąć:
- `kw = "test') OR 1=1--"` → po escape nadal niebezpieczne
- Keywords pochodzą z LLM `extract_entities()` — LLM może zwrócić dowolny tekst

Dodatkowo, `phase_filter` i `branch_filter` używają nievalidowanych integerów w f-stringach:
```python
phase_filter = f"AND dpm.phase_id = {phase_id}"
```

**Rekomendacja:**  
Użyć parametryzowanych zapytań:
```python
conditions = " OR ".join("LOWER(d.title) LIKE LOWER(?)" for _ in keywords[:20])
params = [f"%{kw}%" for kw in keywords[:20]]
# + (phase_id,) jeśli potrzebny
cursor = conn.execute(sql, params)
```

---

### G-02 🔴 KRYTYCZNE — Alembic migration synchroniczna w async fixture

**Dotyczy:** dok.14

**Problem:**  
Dok.14 §4.2 (linia 158–169):
```python
@pytest_asyncio.fixture(scope="function")
async def db_session(postgres_container):
    ...
    command.upgrade(alembic_cfg, "head")  # ← SYNCHRONICZNE! Blokuje event loop
    ...
```

`alembic.command.upgrade()` jest synchroniczna i wykonuje operacje DB. W async fixture to zablokuje event loop, co może powodować timeouty w testach.

**Rekomendacja:**  
Przenieść Alembic migration do `scope="session"` fixture (synchronicznej) lub użyć `run_in_executor`:
```python
await asyncio.get_event_loop().run_in_executor(
    None, lambda: command.upgrade(alembic_cfg, "head")
)
```

---

### G-03 🟡 WAŻNE — Brak obsługi duplikatów doc_uid w work_packages przy wielu fazach

**Dotyczy:** dok.11

**Problem:**  
Jeden dokument z itdoc może być zmapowany do **wielu faz** (przez `document_phase_mapping`). W `MappingResult.items` ten sam `doc_uid` może pojawić się wielokrotnie z różnymi `phase_id`.

WorkPlanner (dok.11 §4) buduje:
```python
doc_map = {d.doc_uid: d for d in all_docs}  # ← nadpisuje duplikaty!
```

Jeśli `doc_uid="42"` występuje z `phase_id=5` i `phase_id=13`, w `doc_map` zostanie tylko ostatni.

**Rekomendacja:**  
Zmienić klucz na `(doc_uid, phase_id)`:
```python
doc_map = {(d.doc_uid, d.phase_id): d for d in all_docs}
```
Lub zdeduplikować wcześniej (w EstimationEngine) i wybrać fazę z wyższą confidence.

---

### G-04 🟡 WAŻNE — `CHUNK_MAX_CHARS = 12_000` może przekraczać token limit Ollama

**Dotyczy:** dok.08, dok.07

**Problem:**  
BriefParser (dok.08 §2) ustawia `CHUNK_MAX_CHARS = 12_000` (~3000 tokenów). Ale:
- Ollama z modelem llama3.2 (7B) ma domyślnie **context window 4096 tokens**
- 12000 znaków polskiego tekstu to **~4000-5000 tokenów** (polskie słowa są dłuższe)
- Prompt `extract_entities.txt` (dok.07 §5.1) dodaje ~300 tokenów instrukcji
- Łącznie: ~4300-5300 tokenów → przekracza context window Ollama

**Rekomendacja:**  
1. Dodać konfigurację `CHUNK_MAX_CHARS` per provider do Settings
2. Dodać do dok.07 walidację: jeśli provider=ollama i chunk > 8000 chars → podziel na mniejsze
3. Alternatywnie: w OllamaAdapter dodać `num_ctx: 8192` w parametrach

---

### G-05 🟡 WAŻNE — Brak concurrency control na mapowaniu

**Dotyczy:** dok.05, dok.09

**Problem:**  
Co się stanie gdy dwa żądania `POST /brief/{id}/map` trafią jednocześnie (np. AI Agent retry)?
- Oba utworzą nowy `mapping_results` rekord
- Oba wywołają LLM (podwójny koszt)
- W `mapping_results` będą dwa rekordy z `status=done` dla tego samego briefu
- `POST /reports/estimate/{brief_id}` (dok.05 §2.3) mówi: "używane jest mapowanie z najnowszym created_at" — ale race condition między INSERT-ami

**Rekomendacja:**  
Dodać do dok.05 kontrakt idempotentności:
```
Precondition: Jeśli istnieje mapping_results ze status='running' dla tego brief_id → 409 Conflict
```
W implementacji: `SELECT ... FOR UPDATE` lub distributed lock.

---

### G-06 🟡 WAŻNE — WorkPlanner nie radzi sobie z doc_path=None

**Dotyczy:** dok.11, dok.12

**Problem:**  
Assignee resolver (dok.11 §3 Etap 4) buduje:
```python
text = f"{doc_title} {doc_path}".lower()
```

Ale `doc_path` jest zawsze `None` w aktualnym stanie bazy (dok.12: "kolumna `documents.path` nie istnieje"). Więc `text = "plan audytu bezpieczeństwa None"`, co zawiera literalny string "None".

**Konsekwencja:**  
`"None"` w tekście nie wpływa na matching (żaden pattern nie zawiera "none"), ale jest nieprawidłowe semantycznie. Gorszy scenariusz: jeśli doc_path zostanie dodany w przyszłości i zawiera "approval" w ścieżce, zmieni się assignee.

**Rekomendacja:**  
```python
text = f"{doc_title} {doc_path or ''}".lower()
```

---

### G-07 🟢 DROBNE — Chunking overlap nie resetuje current_len poprawnie

**Dotyczy:** dok.08

**Problem:**  
Dok.08 §3 Etap 4, algorytm chunkingu:
```python
if current_len + len(para) + 2 > self.CHUNK_MAX_CHARS:
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
        current_chunk = [current_chunk[-1]] if current_chunk else []
        current_len = len(current_chunk[0]) if current_chunk else 0
```

Po overlap, `current_len` jest ustawiony na długość overlap paragrafu. Ale następnie **ten sam `para`** (który nie zmieścił się) nie jest dodawany — pętla przechodzi do `current_chunk.append(para)` poniżej if-a. Jeśli `para` jest dłuższy niż `CHUNK_MAX_CHARS`, wejdzie w nieskończoną logikę (overlap + za długi akapit = ciągłe flushing).

**Rekomendacja:**  
Dodać obsługę akapitów dłuższych niż `CHUNK_MAX_CHARS`:
```python
if len(para) > self.CHUNK_MAX_CHARS:
    # Podziel na zdania
    sentences = re.split(r'(?<=[.!?])\s+', para)
    ...
```

---

### G-08 🟢 DROBNE — `get_documents_by_phase` nie sortuje po relevance

**Dotyczy:** dok.12

**Problem:**  
Dok.12 §3.7 `get_documents_by_phase()` zwraca dokumenty posortowane wg `dpm.priority ASC`. Ale `priority` to wewnętrzny priorytet tabeli, nie relevance do briefu. Wszystkie 7205 dokumentów mają phase_id → przy braku keyword filter zwraca do 50 losowo-priorytetyzowanych dokumentów per faza.

Przy phase fallback (dok.09 §3) z 5 fazami → do 250 kandydatów o niskiej relevance.

**Rekomendacja:**  
Dodać opcjonalny `keywords` filter do `get_documents_by_phase()` aby intersectować z keyword matching:
```python
async def get_documents_by_phase(
    self, phase_id: int, keywords: list[str] | None = None, ...
)
```

---

## H — PROPOZYCJE ROZWINIĘCIA

---

### H-01 🟡 WAŻNE — Plugin system dla LLM adapters (beyond Strategy)

**Dotyczy:** dok.07

**Problem aktualny:** Dodanie nowego providera LLM wymaga edycji `create_llm_adapter()` i dodania nowej klasy w kodzie źródłowym.

**Propozycja:**  
Zamienić factory na entry_points-based discovery:
```toml
# pyproject.toml
[project.entry-points."workshop.llm_adapters"]
openai = "workshop.api.services.llm_openai:OpenAIAdapter"
anthropic = "workshop.api.services.llm_anthropic:AnthropicAdapter"
custom = "my_package:MyAdapter"
```
```python
def create_llm_adapter(settings: Settings) -> BaseLLMAdapter:
    adapters = entry_points(group="workshop.llm_adapters")
    adapter_cls = adapters[settings.llm_provider].load()
    return adapter_cls(settings)
```

**Korzyść:** Użytkownik może dodać adapter (np. Google Gemini, AWS Bedrock) przez pip install bez modyfikacji kodu Workshop.

---

### H-02 🟡 WAŻNE — Configurable scoring weights per projekt

**Dotyczy:** dok.09, dok.10

**Problem aktualny:** Wagi scoringu (source_score, keyword_score, phase_score) i mnożniki wyceny (domain, required) są hardcoded. Różne projekty wymagają różnych wag.

**Propozycja:**  
Wykorzystać istniejącą tabelę `project_settings` (dok.04 §2.12):
```python
# Konfigurowalne przez project_settings lub app_settings:
SCORING_WEIGHTS = {
    "source_weight": 0.5,    # waga source_score  
    "keyword_weight": 0.3,   # waga keyword_score
    "phase_weight": 0.2,     # waga phase_score
}

ESTIMATION_MULTIPLIERS = {
    "confidence_high": 1.0,
    "confidence_medium": 0.9,
    "required_by_standard": 1.2,
}
```
Resolver `resolve_settings(project_id, "scoring_weights")` zwraca JSON z project_settings → fallback na globalne.

**Korzyść:** PM może dostosować wycenę per projekt bez zmiany kodu.

---

### H-03 🟡 WAŻNE — Export/Import projektu (portability)

**Dotyczy:** dok.04, dok.06

**Propozycja:**  
Dodać endpointy:
```yaml
GET /projects/{id}/export → ZIP {project.json, briefs/, mappings/, reports/, plans/}
POST /projects/import     ← ZIP → nowy projekt z danymi
```

**Korzyść:**  
- Backup/restore projektów
- Migracja między instancjami Workshop
- Archiwizacja zakończonych projektów
- Udostępnianie kosztorysów jako standalone artefakty

---

### H-04 🟡 WAŻNE — Comparison mode (porównanie mapowań/kosztorysów)

**Dotyczy:** dok.06, dok.09, dok.10

**Propozycja:**  
Dodać endpointy:
```yaml
GET /reports/compare?report_id_a=X&report_id_b=Y
```
Zwraca diff:
```json
{
  "added_docs": [...],
  "removed_docs": [...],
  "changed_estimates": [{doc_uid, h_before, h_after}],
  "total_h_delta": {min: -10, likely: +15, max: +30}
}
```

**Korzyść:**  
- Po re-mapie z innym progiem → PM widzi co się zmieniło
- Porównanie mapowania z/bez LLM reranking
- Uzasadnienie zmian wobec klienta

---

### H-05 🟢 DROBNE — Adapter dla Brief Parser (plugin format handlers)

**Dotyczy:** dok.08

**Propozycja:**  
Zamienić if/elif chain na registry:
```python
class BriefParser:
    _handlers: dict[str, Callable] = {
        "txt": _parse_text,
        "md": _parse_text,
        "pdf": _parse_pdf,
        "docx": _parse_docx,
    }

    def register_handler(self, format: str, handler: Callable): ...
```

**Korzyść:** Łatwe dodanie `.odt`, `.rtf`, `.html`, `.xlsx` bez modyfikacji istniejącego kodu.

---

### H-06 🟢 DROBNE — Dry-run mode dla POST /brief/{id}/map

**Dotyczy:** dok.06, dok.09

**Propozycja:**  
Dodać query param `dry_run=true`:
```yaml
POST /brief/{id}/map?dry_run=true
```
Zwraca `MappingResult` ale **nie zapisuje** do DB. Przydatne do:
- Testowania z różnymi progami confidence bez zanieczyszczania historii
- Pre-flight check przed kosztownym LLM call (zwraca extracted_entities + szacowaną liczbę candidates)

---

### H-07 🟢 DROBNE — Tagging projektów (metadata organizacyjna)

**Dotyczy:** dok.04, dok.06

**Propozycja:**  
Dodać pole `tags JSONB DEFAULT '[]'` do tabeli `projects`:
```sql
ALTER TABLE projects ADD COLUMN tags JSONB DEFAULT '[]';
-- tags: ["fintech", "2025-Q1", "klient:ABC"]
```
I filtrowanie: `GET /projects?tag=fintech`

**Korzyść:** Organizacja projektów bez modyfikacji schematu. Śledzenie per klient, kwartał, domena.

---

### H-08 🟢 DROBNE — Metryki Prometheus/OpenTelemetry

**Dotyczy:** dok.03, dok.13

**Propozycja:**  
Dodać endpoint `GET /metrics` (Prometheus format) z:
- `workshop_llm_calls_total{provider, model, operation, status}`
- `workshop_llm_latency_seconds{provider}`
- `workshop_mapping_confidence_histogram`
- `workshop_active_plans_gauge`

**Korzyść:** Monitoring w Grafana, alerting na LLM errors, śledzenie kosztów LLM.

---

### H-09 🟢 DROBNE — Template preview w Side 1 przed approve

**Dotyczy:** dok.05, dok.06

**Propozycja:**  
Dodać endpoint:
```yaml
POST /ingestion/{job_id}/preview
```
Zwraca rendered Markdown preview (HTML) z highlighted sekcjami wymagającymi uwagi. Obecnie `GET /ingestion/{job_id}` zwraca raw Markdown w polu `generated_template` — ale PM nie widzi jak będzie wyglądał.

---

## Podsumowanie priorytetów wdrożenia

### Natychmiast (przed implementacją):

| # | Znalezisko | Priorytet |
|---|-----------|-----------|
| F-01 | Ustalić 23 vs 24 fazy — zaktualizować WSZYSTKIE dokumenty | 🔴 |
| F-02 | Dodać `project_id` do MappingResult lub zmienić sygnaturę EstimationEngine | 🔴 |
| G-01 | SQL injection w find_by_keyword → parametryzowane zapytania | 🔴 |
| F-05 | Dodać requestBody do /reports/reject w OpenAPI + ujednolicić `reason` opcjonalność | 🔴 |
| F-06 | Dodać `index_for_mapping` do ApproveRequest w OpenAPI | 🟡 |

### Przed Fazą 2:

| # | Znalezisko | Priorytet |
|---|-----------|-----------|
| E-01 | Specyfikacja async mapowania (background task + polling) | 🔴 |
| F-07 | Obniżyć default threshold lub zwiększyć keyword_fallback weight | 🟡 |
| G-04 | CHUNK_MAX_CHARS per provider (Ollama) | 🟡 |
| G-05 | Concurrency guard na POST /brief/{id}/map | 🟡 |

### Przed Fazą 4:

| # | Znalezisko | Priorytet |
|---|-----------|-----------|
| F-03 | Ustalić format doc_uid (integer string vs semantic) | 🔴 |
| G-03 | Duplikaty doc_uid w work_packages | 🟡 |
| E-10 | Uzupełnić PHASE_DEFAULT_CONTRACTS dla faz 4-23/24 | 🟡 |

### Dług techniczny (po MVP):

| # | Znalezisko | Priorytet |
|---|-----------|-----------|
| E-02 | Endpointy listujące (briefs, reports per projekt) | 🔴 |
| E-03 | Webhook delivery specification | 🔴 |
| E-04 | State machine validation | 🟡 |
| E-05 | Docker Compose specification | 🟡 |
| F-04 | Rozwiązać contradykcję ADR-01 vs populate | 🟡 |
