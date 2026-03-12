# Analiza Runda 5 — Część A: Obszary S i T

**Data analizy:** 2025-07  
**Analityk:** Senior Engineer (AI Copilot)  
**Pliki bazowe:** dok.05 (module_interface_contracts), dok.06 (openapi_specification), dok.14 (testing_strategy), dok.01 (vision_and_scope), dok.04 (data_model_postgresql)  
**Kontekst:** Analiza przeprowadzona po naprawach Rund 1–4. Bada nowe luki w spójności API oraz pokryciu testami.

---

## OBSZAR S — Spójność designu API

---

#### S-01: Niespójna konwencja nazewnictwa zasobów (singular vs plural)

**Plik:** dok.06 §paths  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Prefixy ścieżek mieszają singular i plural bez żadnej reguły:
- `/projects/` — plural ✓  
- `/brief/` — singular ✗ (powinno być `/briefs/`)  
- `/reports/` — plural ✓  
- `/planning/` — rzeczownik odczasownikowy ✗ (powinno być `/plans/`)  
- `/ingestion/` — rzeczownik odczasownikowy ✗ (powinno być `/ingestion-jobs/` lub `/jobs/`)  

Dodatkowo `/planning/create/{report_id}` łączy prefiks zasobu z akcją (`create`), co jest wzorcem RPC, nie REST.

**Wpływ:** SDK klientów generowane z OpenAPI będą miały niekonspójne nazwy klas. Programiści integrujący API muszą zapamiętywać wyjątki dla każdego zasobu. Trudniejszy onboarding.

**Naprawa:**  
Ustandaryzuj na plural nouns dla zasobów REST:
```
/brief/upload            → /briefs/upload  (lub /briefs z POST bez /upload)
/brief/{id}/map          → /briefs/{id}/map
/brief/{id}/mapping      → /briefs/{id}/mapping
/planning/create/{id}    → /plans  (POST /plans z body {report_id: ...})
/planning/{plan_id}      → /plans/{plan_id}
/ingestion/spec          → /ingestion/specs  (lub /templates/ingestion-jobs)
```
Alternatywnie: udokumentuj w dok.06 §conventions wyraźną decyzję o mieszaniu form z uzasadnieniem (np. backward compat z istniejącymi klientami).

---

#### S-02a: Brak GET dla pojedynczego WebhookSubscription

**Plik:** dok.06 §/projects/{project_id}/webhooks  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Dla zasobu `WebhookSubscription` zdefiniowane są tylko:
- `POST /projects/{project_id}/webhooks` — utwórz
- `GET /projects/{project_id}/webhooks` — lista
- `DELETE /projects/{project_id}/webhooks/{webhook_id}` — usuń

Brakuje: `GET /projects/{project_id}/webhooks/{webhook_id}` — pobierz pojedynczy webhook.

**Wpływ:** Klient, który chce zweryfikować konfigurację konkretnego webhooka (URL, zdarzenia, status ostatniej dostawy), musi pobrać całą listę i filtrować po ID. Przy wielu subskrypcjach to nieefektywne. Niemożliwa jest też weryfikacja stanu po `POST`.

**Naprawa:**  
Dodaj do dok.06:
```yaml
  /projects/{project_id}/webhooks/{webhook_id}:
    get:
      tags: [Core]
      summary: Pobierz szczegóły subskrypcji webhook
      parameters:
        - {name: project_id, in: path, required: true, schema: {type: string, format: uuid}}
        - {name: webhook_id, in: path, required: true, schema: {type: string, format: uuid}}
      responses:
        "200":
          description: Subskrypcja webhook
          content:
            application/json:
              schema: {$ref: '#/components/schemas/WebhookSubscription'}
        "404": {description: Nie znaleziono, content: {application/json: {schema: {$ref: '#/components/schemas/ErrorResponse'}}}}
    delete: ...  # istniejący
```

---

#### S-02b: Brak DELETE dla anulowania mapowania w toku

**Plik:** dok.06 §/brief/{brief_id}/mapping, dok.05 §2.1  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Nie istnieje endpoint do anulowania aktywnego mapowania (status=`running`). Dok.05 §2.1 definiuje state machine: `pending → running → done/failed`, ale nie ma ścieżki `running → cancelled`. Jeśli mapowanie utknie lub użytkownik chce je przerwać, nie ma żadnego mechanizmu kontroli.

**Wpływ:** Operator nie może anulować zawieszonych jobów bez bezpośredniej interwencji w bazie danych. Przy wiele briefów z mapowaniami `running` system uniemożliwia nowe uruchomienia (409 Conflict). Startup recovery resetuje do `failed` dopiero przy restarcie serwisu.

**Naprawa:**  
Dodaj do dok.06 i dok.05:
```yaml
  /brief/{brief_id}/mapping:
    delete:
      summary: Anuluj mapowanie w toku
      responses:
        "204": {description: Mapowanie anulowane}
        "409": {description: Mapowanie już zakończone (done/failed) — nie można anulować}
        "404": {description: Brak aktywnego mapowania}
```
W dok.05 state machine dodaj: `running → cancelled` (tylko przez DELETE endpoint).

---

#### S-02c: Brak GET dla pojedynczego WorkPackage

**Plik:** dok.06 §/planning/{plan_id}/packages  
**Priorytet:** 🟢 DROBNE  
**Problem:** Dostępna jest tylko lista pakietów `GET /planning/{plan_id}/packages`, ale brakuje endpointu dla pojedynczego pakietu: `GET /planning/{plan_id}/packages/{package_id}`. PATCH na status istnieje, ale agent AI aktualizujący status pakietu musi najpierw pobrać całą listę.

**Wpływ:** AI-agenty wykonujące work packages muszą pobierać pełną listę pakietów planu (może być 100+), żeby zidentyfikować swój kontekst (inputs_json, outputs_json, gates_json). Generuje nadmiarowy transfer danych.

**Naprawa:**  
Dodaj do dok.06:
```yaml
  /planning/{plan_id}/packages/{package_id}:
    get:
      summary: Pobierz szczegóły work package
      responses:
        "200":
          content:
            application/json:
              schema: {$ref: '#/components/schemas/WorkPackage'}
        "404": {description: Pakiet nie znaleziony}
```

---

#### S-03: Niespójna paginacja w endpointach listowania

**Plik:** dok.06 §paths  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Trzy różne wzorce paginacji w jednej specyfikacji:

| Endpoint | Wzorzec paginacji | Problem |
|---|---|---|
| `GET /projects` | brak paginacji (zwraca array) | ❌ Brak limitu |
| `GET /projects/{id}/webhooks` | brak paginacji (zwraca array) | ❌ Brak limitu |
| `GET /ingestion/jobs` | `limit` (query param, default 20) | ❌ Niespójny z innymi |
| `GET /projects/{id}/briefs` | `page` + `per_page` | ✅ Wzorzec A |
| `GET /projects/{id}/reports` | `page` + `per_page` | ✅ Wzorzec A |
| `GET /projects/{id}/plans` | `page` + `per_page` | ✅ Wzorzec A |
| `GET /planning/{id}/packages` | `page` + `per_page` | ✅ Wzorzec A |

**Wpływ:** `GET /projects` bez paginacji — przy wielu projektach zwróci cały zbiór. `GET /ingestion/jobs` z `limit` bez `page` uniemożliwia iterację po wszystkich stronach. Klienci API muszą implementować różną logikę dla różnych endpointów.

**Naprawa:**  
Ujednolicić WSZYSTKIE listy na wzorzec `page` + `per_page`:
1. `GET /projects` — dodaj `page`, `per_page`, zwracaj `{items: [...], total: int}` zamiast array
2. `GET /projects/{id}/webhooks` — dodaj `page`, `per_page`, zmień schemat odpowiedzi z `array` na `{items: [...], total: int}`
3. `GET /ingestion/jobs` — zastąp `limit` parametrami `page` + `per_page`, zmień odpowiedź na `{items: [...], total: int}`

---

#### S-04: Brak kodów 401/403 we WSZYSTKICH chronionych endpointach

**Plik:** dok.06 §paths, §securitySchemes  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** Spec definiuje globalny `security: [{ApiKeyHeader: []}]`, ale **żaden** endpoint nie dokumentuje odpowiedzi błędu autoryzacji:
- Brak `"401"` (brakujący/nieprawidłowy klucz API) w jakimkolwiek endpoincie
- Brak `"403"` (dostęp do zasobu innego projektu — scenariusz BOLA) w jakimkolwiek endpoincie

Jedynym wyjątkiem jest test w dok.14 (`test_upload_requires_api_key`) weryfikujący kod 403, ale sam spec nie dokumentuje tej odpowiedzi.

**Wpływ:**
1. Generatory SDK (FastAPI auto-docs, Swagger UI, Redoc) nie pokazują możliwości odpowiedzi błędów autoryzacji — klienci API nie wiedzą jak obsłużyć te przypadki
2. Niezdefiniowanie 403 dla BOLA oznacza brak kontraktu dla ownership checks (dodanych w R4)
3. Audyt bezpieczeństwa API wykaże niekompletność specyfikacji

**Naprawa:**  
Dodaj w `components` współdzielone odpowiedzi i dodaj je do KAŻDEGO chronionego endpointu:
```yaml
components:
  responses:
    Unauthorized:
      description: Brakujący lub nieprawidłowy X-API-Key
      content:
        application/json:
          schema: {$ref: '#/components/schemas/ErrorResponse'}
    Forbidden:
      description: Brak dostępu do zasobu (inny projekt lub niewystarczające uprawnienia)
      content:
        application/json:
          schema: {$ref: '#/components/schemas/ErrorResponse'}
```
Dodaj do każdego chronionego endpointu:
```yaml
        "401": {$ref: '#/components/responses/Unauthorized'}
        "403": {$ref: '#/components/responses/Forbidden'}
```

---

#### S-05a: Brak kodów 5xx we WSZYSTKICH endpointach

**Plik:** dok.06 §paths  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** Żaden endpoint nie definiuje odpowiedzi `"500" Internal Server Error`. Jedyne kody 5xx w specyfikacji:
- `"503"` w `POST /ingestion/spec` (LLM niedostępny)
- `"503"` w `POST /brief/{brief_id}/map` (LLM niedostępny)  

Brakuje:
- `"500"` na wszystkich endpointach (nieoczekiwany błąd serwera)
- `"503"` na endpointach zależnych od bazy danych (DB unavailable)
- `"504"` na endpointach z timeoutami LLM (np. `/reports/estimate`)

**Wpływ:** Klienci API nie mogą prawidłowo obsłużyć awarii serwera — nie wiedzą czego oczekiwać przy błędach infrastruktury. Monitoring i circuit breakers po stronie klienta mają niepełne informacje. Niezgodność z best practices OpenAPI (RFC 7231).

**Naprawa:**  
Dodaj w `components` wspólną odpowiedź 500:
```yaml
components:
  responses:
    InternalServerError:
      description: Nieoczekiwany błąd serwera
      content:
        application/json:
          schema: {$ref: '#/components/schemas/ErrorResponse'}
```
Dodaj `"500": {$ref: '#/components/responses/InternalServerError'}` do KAŻDEGO endpointu. Dla endpointów zależnych od LLM (map, estimate, ingestion) dodaj `"503"` z opisem.

---

#### S-05b: Niespójny schemat odpowiedzi błędów 4xx

**Plik:** dok.06 §paths (linie 814-827, 853-866)  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Część odpowiedzi błędów pomija `content:` z `ErrorResponse`, podając tylko `description`:

```yaml
# Wzorzec A (prawidłowy — z schematem):
"404": {description: Nie znaleziono, content: {application/json: {schema: {$ref: '#/components/schemas/ErrorResponse'}}}}

# Wzorzec B (nieprawidłowy — bez schematu):
"404": {description: Projekt nie znaleziony}   # brak content!
"413": {description: Plik za duży}             # brak content!
```

Endpointy z niekompletnymi odpowiedziami błędów: `POST /brief/upload` (404, 413, 415, 422 bez content), `POST /brief/{id}/map` (404, 503 bez content), `GET /planning/{id}/packages` (404 bez content), `GET /planning/{id}/gantt` (404 bez content), `GET /reports/{id}` (404 bez content).

**Wpływ:** Generatory klientów (np. openapi-generator) tworzą klientów, którzy nie próbują deserializować ciała błędu — obsługa błędów po stronie klienta jest utrudniona. Niezgodność wewnętrzna w samej specyfikacji.

**Naprawa:**  
Dla WSZYSTKICH odpowiedzi 4xx dodać `content:`:
```yaml
"404":
  description: Brief nie znaleziony
  content:
    application/json:
      schema: {$ref: '#/components/schemas/ErrorResponse'}
```
Przejrzeć i ustandaryzować WSZYSTKIE kody błędów w dok.06 (ok. 15 miejsc do poprawki).

---

#### S-06: Brak wersjonowania API — brak planu dla breaking changes

**Plik:** dok.06 §info, §servers  
**Priorytet:** 🟡 WAŻNE  
**Problem:**
- Brak prefiksu `/v1/` w URL-ach endpointów (np. `/projects` zamiast `/v1/projects`)
- `info.version: "1.0.0"` w spec, ale serwer to `http://localhost:8000` bez prefiksu wersji
- Brak sekcji w dok.06 (ani dok.01) opisującej strategię wersjonowania API: czy przez URL (`/v2/`), header (`Accept: application/vnd.workshop.v2+json`), czy query param (`?version=2`)
- Brak polityki deprecation (jak długo stare wersje będą wspierane)

**Wpływ:** Pierwsza breaking change (np. zmiana schematu `EstimationReport`, usunięcie pola) wymusi albo złamanie istniejących klientów, albo szybkie łatanie bez planu. Przy braku prefiksu wersji URL-e nie mogą koegzystować `/v1/` i `/v2/` na tym samym serwerze.

**Naprawa:**  
Opcja A (URL prefix — najprostsza): Zmień wszystkie endpointy na `/v1/projects`, `/v1/brief`, etc. i zaktualizuj `servers.url` na `http://localhost:8000/v1`.  
Opcja B (dodaj notatkę o strategii): Jeśli decyzja o braku prefiksu jest świadoma, dodaj w dok.06 §info i w dok.01 §API sekcję:
```
## Wersjonowanie API
Wersja 1.0 nie używa prefiksu URL (/v1/). Breaking changes będą wersjonowane
przez nowy prefiks URL (/v2/) z minimalnym 6-miesięcznym okresem wspólnego
działania obu wersji.
```

---

#### S-07: Endpoint eksportu ZIP — brak obsługi błędów i nagłówka Content-Disposition

**Plik:** dok.06 §/projects/{project_id}/export  
**Priorytet:** 🟢 DROBNE  
**Problem:** Endpoint `GET /projects/{project_id}/export` zwracający `application/zip`:
1. Brak nagłówka `Content-Disposition` w odpowiedzi 200 — klient nie wie jak nazwać pobrany plik
2. Brak odpowiedzi błędów: nie ma `"404"` (projekt nie istnieje), `"409"` (projekt pusty — brak danych do eksportu), `"5xx"`
3. Brak informacji o timeoucie dla dużych projektów (eksport może trwać kilka sekund)

**Wpływ:** Przeglądarka/klient HTTP nie nadaje nazwy plikowi ZIP automatycznie. Przy próbie eksportu nieistniejącego projektu zachowanie jest nieokreślone w specyfikacji.

**Naprawa:**  
```yaml
  /projects/{project_id}/export:
    get:
      responses:
        '200':
          description: Archiwum ZIP
          headers:
            Content-Disposition:
              schema: {type: string}
              example: 'attachment; filename="project-{id}-export.zip"'
          content:
            application/zip:
              schema: {type: string, format: binary}
        "404":
          description: Projekt nie znaleziony
          content:
            application/json:
              schema: {$ref: '#/components/schemas/ErrorResponse'}
        "409":
          description: Projekt nie ma danych do eksportu
          content:
            application/json:
              schema: {$ref: '#/components/schemas/ErrorResponse'}
```

---

## OBSZAR T — Luki w strategii testowania

---

#### T-01a: Brak testów jednostkowych dla `_extract_json()` — 3 ścieżki fallback

**Plik:** dok.14 §5, dok.08 §3.5 (brief_parser_spec)  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** Dok.08 §3.5 definiuje `_extract_json()` z trzema ścieżkami:
1. Próba 1: czysty JSON (`json.loads(text)`)
2. Próba 2: Markdown code block (```` ```json {...} ``` ````)
3. Próba 3: first `{` to last `}` extraction

Dok.14 zawiera `TestBriefParser` (§5.1) z testami ogólnymi (format, parse, chunks), ale **żaden** test nie weryfikuje `_extract_json()` — ani happy path dla każdej z 3 strategii, ani path gdzie wszystkie 3 zawodzą (oczekiwany `LLMResponseParseError`).

**Wpływ:** Zmiany w helperze `_extract_json()` (np. regexie dla markdown) nie są wykrywane przez testy. Strategia 3 (greedy `{...}`) jest szczególnie podatna na błędy przy zagnieżdżonym JSON — brak testu dla edge case'ów.

**Naprawa:**  
Dodaj do dok.14 §5.1:
```python
class TestExtractJson:
    def test_clean_json(self): ...          # Próba 1 — czysty JSON
    def test_markdown_code_block(self): ... # Próba 2 — ```json {...} ```
    def test_greedy_extraction(self): ...   # Próba 3 — first { to last }
    def test_nested_json_greedy(self): ...  # Edge case: zagnieżdżone obiekty
    def test_all_fail_raises(self): ...     # Oczekiwany LLMResponseParseError
    def test_empty_string_raises(self): ... # Edge case: pusty string
```

---

#### T-01b: Brak testów dla `validate_webhook_url()` (SSRF prevention)

**Plik:** dok.14 §5–6, dok.05 §8  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** Dok.05 §8 opisuje `validate_webhook_url()` jako walidację SSRF z blokowaniem adresów prywatnych (localhost, 127.x.x.x, 10.x, 172.16-31.x, 192.168.x). Dok.14 **nie zawiera żadnego testu** tej funkcji.

Brakuje testów dla:
- `http://localhost:8080/hook` → odrzucony
- `http://127.0.0.1/hook` → odrzucony
- `http://10.0.0.1/hook` → odrzucony
- `http://[::1]/hook` (IPv6 loopback) → odrzucony
- `http://169.254.169.254/latest/meta-data` (AWS metadata) → odrzucony
- `https://example.com/webhook` → zaakceptowany

**Wpływ:** SSRF to podatność klasy CRITICAL (OWASP A10). Brak testów oznacza ryzyko regresji przy jakiejkolwiek zmianie walidatora. Bypass SSRF przez IPv6 lub AWS metadata endpoint może pozostać niezauważony.

**Naprawa:**  
Dodaj do dok.14 nową sekcję §5.4 (lub rozszerz §5.1):
```python
@pytest.mark.unit
class TestValidateWebhookUrl:
    def test_localhost_blocked(self): ...
    def test_127_blocked(self): ...
    def test_private_10_blocked(self): ...
    def test_ipv6_loopback_blocked(self): ...
    def test_aws_metadata_blocked(self): ...
    def test_valid_https_accepted(self): ...
    def test_http_allowed_if_configured(self): ...  # configurowalność
```

---

#### T-01c: Brak testów dla `RequestIDMiddleware`

**Plik:** dok.14 §5–6, dok.05 §3.4  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Dok.05 §3.4 definiuje `RequestIDMiddleware` jako komponent propagujący `X-Request-ID` przez cały call stack. Dok.14 nie zawiera żadnego testu tego middleware.

Brakuje testów:
- Request bez `X-Request-ID` → middleware generuje UUID i dodaje do response
- Request z `X-Request-ID` → middleware propaguje istniejący ID
- Request-ID dostępny w logach (przez contextvars)
- Dwa równoczesne requesty mają różne Request-ID

**Wpływ:** Middleware odpowiada za tracability całego systemu. Regresja (np. contextvars leak między requestami) jest niewidoczna bez testów — może prowadzić do pomylonych ID w logach przy concurrency.

**Naprawa:**  
Dodaj do dok.14 §6 (testy integracyjne):
```python
@pytest.mark.integration
class TestRequestIDMiddleware:
    async def test_generates_request_id_when_missing(self, client): ...
    async def test_propagates_existing_request_id(self, client): ...
    async def test_different_requests_different_ids(self, client): ...
    async def test_request_id_in_error_response(self, client): ...
```

---

#### T-01d: Brak testów dla `content_hash` deduplication i `ON DELETE CASCADE`

**Plik:** dok.14 §5–6, dok.04 (data_model)  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Dok.04 definiuje `content_hash UNIQUE` na tabeli `briefs` (deduplication) oraz `ON DELETE CASCADE` dla relacji `projects → briefs → mapping_results → ...`. Dok.14 nie zawiera testów dla żadnej z tych constraints.

Brakuje:
- Test duplikatu brief (ten sam content_hash) → 409 Conflict (nie duplikat w DB)
- Test `ON DELETE CASCADE`: usunięcie projektu kasuje briefs, mappings, reports, plans
- Test `SELECT FOR UPDATE` race condition: dwa równoczesne `POST /brief/{id}/map` → jeden dostaje 409

**Wpływ:** Brak testu CASCADE oznacza ryzyko nieaktualnych danych po usunięciu projektu (orphaned records). Brak testu content_hash oznacza ryzyko regresji przy zmianie hash algorytmu.

**Naprawa:**  
Dodaj do dok.14 §6:
```python
@pytest.mark.integration
class TestDatabaseConstraints:
    async def test_duplicate_content_hash_returns_409(self, client, project_id): ...
    async def test_delete_project_cascades_to_briefs(self, db_session): ...
    async def test_delete_project_cascades_to_mappings(self, db_session): ...
    async def test_select_for_update_prevents_duplicate_mapping(self, client): ...
        # Użyj asyncio.gather z dwoma równoczesnym POST /brief/{id}/map
        # Jeden powinien dostać 202, drugi 409
```

---

#### T-02: Brak contract tests między modułami

**Plik:** dok.14 (cały), dok.05 §5 (sekwencja przepływu)  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** Dok.05 §5 definiuje przepływ danych: `BriefParser → ParsedBrief → SemanticMapper → MappingResult → EstimationEngine → EstimationReport → WorkPlanner → WorkPlan`. Dok.14 testuje każdy moduł izolowanie (unit testy), ale **nie ma żadnych contract tests** weryfikujących że wyjście jednego modułu zawiera WSZYSTKIE pola których oczekuje następny.

Konkretne luki:
- `ParsedBrief.chunks` (lista stringów) — czy SemanticMapper naprawdę dostaje `chunks`? Dok.05 §3.2 definiuje `ParsedBrief` z `chunks: list[str]`, ale `TestSemanticMapper` używa `sample_brief_parsed` fixture bez weryfikacji schematu
- `MappingResult.items[].phase_id` — czy EstimationEngine zakłada istnienie `phase_id`?
- `EstimationReport.by_phase` — czy WorkPlanner korzysta z `by_phase[].is_critical_path`?

**Wpływ:** Jeśli BriefParser zmieni format `ParsedBrief` (np. usunie pole `chunks`), SemanticMapper może działać nieprawidłowo ale testy unit każdego modułu osobno nie wykryją problemu. Błędy wychodzą dopiero na E2E.

**Naprawa:**  
Dodaj do dok.14 §6 nowy blok:
```python
@pytest.mark.integration
class TestModuleContracts:
    """Testy kontraktowe: weryfikuje że OUTPUT modułu A zawiera
       wszystkie pola oczekiwane przez INPUT modułu B."""

    async def test_parsed_brief_satisfies_semantic_mapper_contract(self, ...):
        """ParsedBrief musi mieć: text, chunks (≥1), word_count."""
        brief = await parser.parse(SAMPLE_BRIEF_TXT, "txt")
        assert hasattr(brief, 'chunks') and len(brief.chunks) >= 1
        assert hasattr(brief, 'word_count') and brief.word_count > 0

    async def test_mapping_result_satisfies_estimation_engine_contract(self, ...):
        """MappingResult.items muszą mieć: phase_id, confidence, is_required."""
        ...

    async def test_estimation_report_satisfies_work_planner_contract(self, ...):
        """EstimationReport musi mieć: by_phase[].phase_id, by_phase[].is_critical_path."""
        ...
```

---

#### T-03: Brak testów wydajnościowych dla SLA z dok.01

**Plik:** dok.14 (cały), dok.01 §5  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Dok.01 §5 definiuje metryki SLA:
- Czas od uploadu do `MappingResult`: **< 30 s** (przy GPT-4o)
- Czas generowania `WorkPackage` plan: **< 10 s** (operacja DB-only)

Dok.14 nie zawiera żadnych testów wydajnościowych. Brakuje zarówno:
1. Testów granicznych (czy pojedyncze wywołanie mieści się w SLA?)
2. Testów obciążeniowych (locust/k6 — ile concurrent users system obsługuje?)

**Wpływ:** SLA zdefiniowane w dok.01 są niesprawdzalne. Regresja wydajności (np. N+1 query, brak indeksu) nie jest wykrywana w CI. Przy oddaniu systemu do klienta brak dowodu spełnienia wymagań.

**Naprawa:**  
Dodaj do dok.14 nową sekcję §10 Performance Tests:
```python
@pytest.mark.slow
class TestPerformanceSLA:
    async def test_mapping_completes_within_sla(self, client, mock_llm_adapter):
        """Mapowanie < 30s dla briefu 5000 słów z mock LLM."""
        start = time.time()
        # ... uruchom mapowanie i czekaj na done
        assert time.time() - start < 30.0

    async def test_planning_completes_within_sla(self, client, accepted_report):
        """Generowanie planu pracy < 10s (DB-only, bez LLM)."""
        start = time.time()
        # POST /planning/create/{report_id}
        assert time.time() - start < 10.0
```
Opcjonalnie: dodaj `workshop/tests/performance/locustfile.py` z scenariuszem obciążeniowym.

---

#### T-04: Niekompletne testy security

**Plik:** dok.14 §5–7  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** Dok.14 zawiera jeden test security (`test_upload_requires_api_key` → 403), ale R4 dodał wiele mechanizmów bezpieczeństwa które nie mają testów:

| Mechanizm | Dodany w | Test w dok.14 |
|---|---|---|
| Rate limiting (429 po przekroczeniu limitu) | R4 | ❌ Brak |
| SSRF prevention w webhook URL | R4 | ❌ Brak (patrz T-01b) |
| BOLA — zasób innego projektu → 403 | R4 | ❌ Brak |
| Input size limit — plik > 50MB → 413 | R2/R3 | ❌ Brak |
| Auth — brakujący X-API-Key → 403 | R1 | ✅ Tylko upload |

**Wpływ:** Mechanizmy bezpieczeństwa bez testów regresyjnych są podatne na silent breakage. BOLA bez testu oznacza że przypadkowy bug w ownership check może przejść przez CI.

**Naprawa:**  
Dodaj do dok.14 nową sekcję §11 Security Tests:
```python
@pytest.mark.integration
class TestSecurity:
    async def test_rate_limit_returns_429(self, client):
        """Wyślij N+1 requestów powyżej limitu → ostatni dostaje 429."""
        ...

    async def test_bola_different_project_returns_403(self, client):
        """Brief projektu A niedostępny dla projektu B."""
        ...

    async def test_file_size_limit_returns_413(self, client, project_id):
        """Plik > 50MB → 413 Payload Too Large."""
        ...

    async def test_all_endpoints_require_api_key(self, client):
        """Każdy chroniony endpoint bez X-API-Key → 403."""
        protected = ["/projects", "/brief/upload", ...]
        for url in protected:
            resp = await client.get(url)
            assert resp.status_code == 403
```

---

#### T-05: Brak testów async/concurrency i startup recovery

**Plik:** dok.14 §5–7, dok.05 §2.1 i §8.2  
**Priorytet:** 🟡 WAŻNE  
**Problem:** System ma wiele miejsc z potencjalnymi problemami współbieżności opisanymi w dok.05, ale dok.14 nie testuje żadnego z nich:

1. **Duplicate mapping (409):** Dwa równoczesne `POST /brief/{id}/map` — jeden musi dostać 409, nie duplikat w DB. Dok.05 §2.1 opisuje SELECT FOR UPDATE, ale brak testu concurrency.

2. **Startup recovery:** Dok.05 §8.2 opisuje że przy starcie serwisu wszystkie `mapping_results.status = 'running'` są resetowane do `'failed'`. Brak testu tego mechanizmu.

3. **Webhook retry:** Dok.05 §8 opisuje retry przy nieudanej dostawie webhooka. Brak testu że po HTTP 500 z endpointu klienta system ponawia próbę.

**Wpływ:** Bez testów concurrency problemy race condition mogą wystąpić na produkcji przy ruchu. Startup recovery bez testu może nie działać po refactoringu — zombie records blokują nowe operacje na briefach.

**Naprawa:**  
Dodaj do dok.14 §7 (E2E) lub §6:
```python
@pytest.mark.integration
class TestConcurrency:
    async def test_concurrent_map_same_brief_returns_409(self, client, brief_id):
        tasks = [client.post(f"/brief/{brief_id}/map", ...) for _ in range(2)]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        codes = [r.status_code for r in results]
        assert sorted(codes) == [202, 409]

@pytest.mark.integration
class TestStartupRecovery:
    async def test_zombie_mapping_reset_on_startup(self, db_session, app):
        # Wstaw rekord z status='running'
        # Uruchom startup handler
        # Sprawdź że status='failed'
        ...
```

---

#### T-06: Brak testów dla 3-tierowych ścieżek fallback SemanticMapper

**Plik:** dok.14 §5.3 (TestSemanticMapper), dok.05 §§ LLM integration  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Dok.05 opisuje 3-etapową strategię mapowania:
1. **Tier 1** — LLM `extract_entities` → pełne mapowanie semantyczne
2. **Tier 2** — keyword fallback (gdy LLM niedostępny lub timeout) → mapowanie keyword-based  
3. **Tier 3** — phase fallback (gdy brak kluczy) → mapowanie po fazach SDLC

Dok.14 §5.3 (`TestSemanticMapper`) zawiera tylko 4 testy:
- `test_map_returns_mapping_result` (Tier 1 z mock LLM)
- `test_confidence_threshold_filters`
- `test_max_results_respected`
- `test_llm_error_propagates` (sprawdza wyjątek, ale nie czy fallback działa)

Brakuje testów Tier 2 i Tier 3, oraz testu że `metadata.processing_notes` zawiera `partial_llm_timeout: true` przy degraded mode.

**Wpływ:** Jeśli Tier 2 lub Tier 3 przestanie działać (np. bug po refactoringu), system zwróci pusty wynik mapowania bez żadnego ostrzeżenia w testach CI. To najważniejsza resilience feature systemu.

**Naprawa:**  
Rozszerz dok.14 §5.3:
```python
@pytest.mark.unit
class TestSemanticMapperFallback:

    async def test_tier1_llm_available(self, mapper, mock_llm_adapter, ...):
        """Tier 1: LLM dostępny → pełne mapowanie semantyczne."""
        result = await mapper.map(sample_brief)
        assert result.status == "done"
        assert result.metadata is None or not result.metadata.get("partial_llm_timeout")

    async def test_tier2_keyword_fallback_when_llm_unavailable(self, mapper_no_llm, ...):
        """Tier 2: LLM niedostępny → keyword fallback, status='done',
           metadata.processing_notes zawiera fallback_mode='keyword'."""
        result = await mapper_no_llm.map(sample_brief)
        assert result.status == "done"
        assert result.metadata["processing_notes"].get("fallback_mode") == "keyword"

    async def test_tier3_phase_fallback_when_no_keywords(self, mapper_no_llm, empty_brief, ...):
        """Tier 3: Brak LLM i brak kluczowych terminów → fallback na fazy SDLC."""
        result = await mapper_no_llm.map(empty_brief)
        assert result.status == "done"
        assert result.total_items > 0  # Przynajmniej fazy bazowe

    async def test_partial_llm_timeout_sets_processing_note(self, mapper_timeout_llm, ...):
        """LLM timeout w trakcie → status='done', partial_llm_timeout=true."""
        result = await mapper_timeout_llm.map(sample_brief)
        assert result.metadata["processing_notes"].get("partial_llm_timeout") is True
```

---

## Podsumowanie znalezisk

### Obszar S — API Design

| ID | Tytuł | Priorytet |
|---|---|---|
| S-01 | Niespójna konwencja nazewnictwa zasobów (singular/plural) | 🟡 WAŻNE |
| S-02a | Brak GET dla pojedynczego WebhookSubscription | 🟡 WAŻNE |
| S-02b | Brak DELETE/cancel dla mapowania w toku | 🟡 WAŻNE |
| S-02c | Brak GET dla pojedynczego WorkPackage | 🟢 DROBNE |
| S-03 | Niespójna paginacja — 3 różne wzorce | 🟡 WAŻNE |
| S-04 | Brak 401/403 we wszystkich chronionych endpointach | 🔴 KRYTYCZNE |
| S-05a | Brak 5xx we wszystkich endpointach | 🔴 KRYTYCZNE |
| S-05b | Niespójny schemat 4xx — część bez `content:` | 🟡 WAŻNE |
| S-06 | Brak wersjonowania API — brak strategii dla breaking changes | 🟡 WAŻNE |
| S-07 | Export ZIP — brak Content-Disposition i obsługi błędów | 🟢 DROBNE |

### Obszar T — Testing Strategy

| ID | Tytuł | Priorytet |
|---|---|---|
| T-01a | Brak testów `_extract_json()` — 3 fallback strategie | 🔴 KRYTYCZNE |
| T-01b | Brak testów `validate_webhook_url()` (SSRF prevention) | 🔴 KRYTYCZNE |
| T-01c | Brak testów `RequestIDMiddleware` | 🟡 WAŻNE |
| T-01d | Brak testów `content_hash` dedup i `ON DELETE CASCADE` | 🟡 WAŻNE |
| T-02 | Brak contract tests między modułami | 🔴 KRYTYCZNE |
| T-03 | Brak testów wydajnościowych dla SLA z dok.01 | 🟡 WAŻNE |
| T-04 | Niekompletne testy security (rate limit, BOLA, input size) | 🔴 KRYTYCZNE |
| T-05 | Brak testów async/concurrency i startup recovery | 🟡 WAŻNE |
| T-06 | Brak testów dla 3-tierowych ścieżek fallback SemanticMapper | 🟡 WAŻNE |

**Łącznie:** 19 znalezisk (10 × S, 9 × T)  
**Krytyczne:** 6 (S-04, S-05a, T-01a, T-01b, T-02, T-04)  
**Ważne:** 10  
**Drobne:** 3  
# Analiza Runda 5 — Część B: Obszary U, V, W

**Data:** 2025-01-27  
**Analizowane pliki:** dok.07, dok.08, dok.09, dok.10, dok.11, dok.12, dok.16  
**Poprzednie rundy:** R1–R4 (naprawione — patrz kontekst zadania)

---

## OBSZAR U — Kompletność konfiguracji i środowiska

---

#### U-01: Duplikat RHYTHM_DEPTH z różnymi wartościami domyślnymi

**Plik:** dok.09 §8, dok.11 §7  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
Dwie zmienne realizują ten sam koncept głębokości ekspansji rhythm, ale mają różne nazwy i wartości:
- `RHYTHM_DEPTH=1` (dok.09 §8) — używana w SemanticMapper przy `rhythm_downstream`
- `RHYTHM_DEPTH_PLANNING=2` (dok.11 §7) — używana w WorkPlanner przy `rhythm_upstream`

Brak dokumentacji uzasadnienia dlaczego mapper używa depth=1, a planner depth=2. Deweloper może pomylić obie zmienne lub użyć jednej tam gdzie powinna być druga.

**Wpływ:**  
- Mapowanie może pomijać zależności (depth=1 gdy powinno być 2 lub odwrotnie)  
- Przy wdrożeniu operacyjnym zmiana jednej zmiennej może mieć nieoczekiwany wpływ na drugi moduł  
- Brak spójności utrudnia konfigurację

**Naprawa:**  
W sekcji konfiguracji dok.09 i dok.11 dodać wyjaśnienie:  
> `RHYTHM_DEPTH=1` — tylko bezpośrednie zależności, wystarczające dla rozszerzenia zbioru kandydatów mapowania  
> `RHYTHM_DEPTH_PLANNING=2` — głębsze śledzenie dla poprawnego sekwencjonowania zadań

Rozważyć ujednolicenie nazwy: `RHYTHM_DEPTH_MAPPING` i `RHYTHM_DEPTH_PLANNING` (zamiast obecnej niesymetrycznej pary `RHYTHM_DEPTH` / `RHYTHM_DEPTH_PLANNING`).

---

#### U-02: OPENAI_TIMEOUT odczytywany z .env, ale hardkodowany w kodzie

**Plik:** dok.07 §3.1, §8  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
W sekcji konfiguracji (§8) zdefiniowano `OPENAI_TIMEOUT=30`. Jednakże w kodzie implementacji OpenAIAdapter (§3.1) timeout jest hardkodowany:

```python
response = await self._client.chat.completions.create(
    ...
    timeout=30,   # ← wartość hardkodowana, nie z settings
)
```

`settings.openai_timeout` (o ile taki atrybut jest zdefiniowany w `Settings`) nie jest używany. Dodatkowo dla `AnthropicAdapter` i `OllamaAdapter` brak jakiegokolwiek timeout w specyfikacji kodu ani w sekcji konfiguracji (.env).

**Wpływ:**  
- Zmiana `OPENAI_TIMEOUT` w .env nie ma efektu — aplikacja zawsze używa 30s  
- Ollama lokalnie może działać wolno (heavy model) — brak konfigurowalnego timeout powoduje długie oczekiwanie lub wiszące requesty  
- Środowiska produkcyjne nie mogą dostosować timeoutów bez edycji kodu

**Naprawa:**  
W dok.07 §3.1–§3.3 poprawić kod każdego adaptera:
```python
# OpenAI
timeout=settings.openai_timeout  # odczytaj z Settings

# Anthropic — dodać w §3.2
ANTHROPIC_TIMEOUT=60              # sekundy, do .env

# Ollama — dodać w §3.3
OLLAMA_TIMEOUT=120                # lokalny model może być wolny
```
Zaktualizować §8 o `ANTHROPIC_TIMEOUT` i `OLLAMA_TIMEOUT`.

---

#### U-03: CHUNK_MAX_CHARS — stała klasy zamiast env var, metoda _get_chunk_size() nie jest wywoływana

**Plik:** dok.08 §2, §4 (Etap 4)  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
`BriefParser` definiuje `CHUNK_MAX_CHARS = 12_000` i `CHUNK_MAX_CHARS_OLLAMA = 7_000` jako stałe klasy (nie env vars). Metoda `_get_chunk_size(provider)` jest zdefiniowana (§2), ale w kodzie `_chunk()` (§3 Etap 4) używana jest bezpośrednio stała klasy:

```python
def _chunk(self, text: str) -> list[str]:
    ...
    chunk_size = self.CHUNK_MAX_CHARS   # ← zawsze 12_000, ignoruje provider!
```

Metoda `_get_chunk_size()` nigdy nie jest wywoływana. Przy `LLM_PROVIDER=ollama` chunki będą za duże (12_000 zamiast 7_000 znaków), co może przekroczyć context window modelu.

**Wpływ:**  
- Przy Ollama: chunki 12_000 znaków + prompt (~300 tokenów) przekraczają domyślne 4096 tokenów Llama3.2 — LLM obcina odpowiedź lub zwraca błąd  
- Brak konfiguracji przez env var uniemożliwia dostosowanie bez edycji kodu  
- Ostrzeżenie opisane w specyfikacji (§3 Etap 4) jest ignorowane przez implementację

**Naprawa:**  
W dok.08 §3 Etap 4 poprawić wywołanie:
```python
def _chunk(self, text: str, provider: str = "openai") -> list[str]:
    chunk_size = self._get_chunk_size(provider)
```
Dodać `CHUNK_MAX_CHARS` i `CHUNK_MAX_CHARS_OLLAMA` do sekcji konfiguracji dok.08 jako konfigurowalne env vars. Zaktualizować sygnaturę `parse()` aby przyjmowała `provider` i przekazywała do `_chunk()`.

---

#### U-04: MIN_EXPECTED_DOCS hardkodowane — brak env var dla progu partial

**Plik:** dok.09 §9 (Statusy MappingResult)  
**Priorytet:** 🟢 DROBNE  
**Problem:**  
W tabeli statusów MappingResult zdefiniowano:  
> `partial` — `mapped_count > 0` AND `mapped_count < MIN_EXPECTED_DOCS` gdzie `MIN_EXPECTED_DOCS = 3`

`MIN_EXPECTED_DOCS = 3` jest wbudowane jako stała w specyfikacji, nie pojawia się w sekcji konfiguracji (§8). Nie ma env var `MIN_EXPECTED_DOCS`. Dla prostych projektów (1–2 dokumenty) próg 3 jest zbyt wysoki i status będzie fałszywie `partial`.

**Wpływ:**  
- Projekty dokumentacyjne małego zakresu będą zawsze oznaczone jako `partial` nawet gdy wynik jest poprawny  
- Brak możliwości konfiguracji per środowisko

**Naprawa:**  
Dodać do sekcji §8 dok.09:
```ini
MIN_EXPECTED_DOCS=3       # min docs dla statusu 'done' (vs 'partial')
```
Zaktualizować opis statusów aby jasno wskazywał że jest to konfigurowalny próg.

---

#### U-05: Niespójność limitu keywords między dok.09 a dok.12

**Plik:** dok.09 §3 (ścieżka B), dok.12 §3.6  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
SemanticMapper wywołuje `find_by_keyword(keywords=entities.keywords[:30], limit=150)` (dok.09 §3). Implementacja `find_by_keyword` w ItdocConnector (dok.12 §3.6) zawiera `safe_kws = keywords[:20]` — obcina do 20 bez ostrzeżenia.

Efektywny limit to 20 (narzucony przez implementację), podczas gdy spec mówi 30. Brak env var kontrolującego ten limit. `KEYWORD_FALLBACK_LIMIT=150` (limit wyników) i rzeczywisty limit keywords (20 vs 30) to dwie różne wartości kontrolujące wydajność, obie niespójne.

**Wpływ:**  
- Ostatnie 10 z 30 keywords z briefu jest cicho ignorowanych — potencjalnie trafne dokumenty nie są znajdywane  
- PM nie ma informacji że niektóre keywords zostały pominięte

**Naprawa:**  
Ujednolicić do `keywords[:20]` w dok.09 §3 (lub podnieść limit w dok.12 §3.6 do 30 i udokumentować). Dodać env var:
```ini
KEYWORD_SEARCH_MAX_TERMS=20    # max keywords przekazywanych do find_by_keyword
```

---

#### U-06: Brak env var dla MAX_FILE_SIZE_MB (BriefParser)

**Plik:** dok.08 §2  
**Priorytet:** 🟢 DROBNE  
**Problem:**  
`BriefParser.MAX_FILE_SIZE = 50 * 1024 * 1024` (50 MB) jest hardkodowaną stałą klasy. Nie ma zmiennej środowiskowej `BRIEF_MAX_FILE_SIZE_MB`. Nie pojawia się w żadnej sekcji konfiguracji.

**Wpływ:**  
- Środowiska z ograniczonymi zasobami (np. mała instancja cloud) nie mogą obniżyć limitu  
- Środowiska z dużymi briefami (pliki PDF projektów enterprise) nie mogą podnieść limitu bez edycji kodu

**Naprawa:**  
W dok.08 dodać sekcję konfiguracji (analogiczną do dok.09 §8):
```ini
BRIEF_MAX_FILE_SIZE_MB=50      # max rozmiar pliku briefu w MB
```
Zaktualizować `BriefParser.__init__` aby odczytywał z `settings.brief_max_file_size_mb`.

---

## OBSZAR V — Luki w logice biznesowej

---

#### V-01: Brak walidacji statusu projektu w EstimationEngine i SemanticMapper

**Plik:** dok.09 §7, dok.10 §6  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:**  
`SemanticMapper.map()` (dok.09 §7) i `EstimationEngine.calculate()` (dok.10 §6) przyjmują `project_id` (przekazywany z briefu), ale żaden z nich nie sprawdza statusu projektu przed wykonaniem kosztownych operacji LLM i kalkulacji.

Scenariusz: projekt zmienił status na `archived` lub `cancelled` między wgraniem briefu a uruchomieniem mapowania (które może być asynchroniczne, w kolejce). Mapowanie zostanie ukończone dla anulowanego projektu, konsumując tokeny LLM i generując raport który nikt nie potrzebuje.

W specyfikacji brak jakiejkolwiek wzmianki o guard na status projektu.

**Wpływ:**  
- Zbędne koszty API (LLM tokeny)  
- Możliwe tworzenie `EstimationReport` dla `cancelled` projektów — dane w DB, ale projekt nieaktywny  
- `WorkPlanner` może wystartować na podstawie raportu z anulowanego projektu

**Naprawa:**  
W dok.09 §7 (`SemanticMapper.map`) dodać guard na początku:
```python
# Guard: sprawdź status projektu przed kosztownym LLM
project = await project_repo.get(project_id)
if project.status in ("archived", "cancelled"):
    raise ProjectNotActiveError(
        f"Projekt {project_id} ma status '{project.status}' — mapowanie niedozwolone."
    )
```
Analogicznie w dok.10 §6. Opisać w dok.09 i dok.10 listę dozwolonych statusów projektu (np. `active`, `in_progress`).

---

#### V-02: Brak mechanizmu invalidacji WorkPlan po zmianie kosztorysu

**Plik:** dok.10 §6, dok.11 §4  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:**  
`WorkPlanner.create_plan(report)` tworzy `WorkPlan` na podstawie `EstimationReport`. Nie istnieje mechanizm obsługujący sytuację gdy:
1. Klient zaakceptuje kosztorys → plan zostaje utworzony
2. Klient zmieni zdanie i zażąda nowego kosztorysu (np. ograniczy scope)
3. PM uruchamia nowy `EstimationEngine.calculate()` → nowy `EstimationReport`
4. **Stary `WorkPlan` nadal istnieje w bazie i nie jest invalidowany**

Dwa aktywne WorkPlany dla tego samego projektu to stan niespójny. Brak pola `superseded_by` lub statusu `cancelled` dla WorkPlan. Brak cascade-logic: `EstimationReport.status=superseded` → `WorkPlan.status=cancelled`.

**Wpływ:**  
- PM i AI agenci widzą dwa różne plany pracy — który jest aktualny?  
- WorkPackages ze starego planu mogą być wykonywane równolegle z nowym planem  
- Raportowanie godzin i postępu jest błędne

**Naprawa:**  
W dok.11 §4 opisać logikę state machine dla WorkPlan:
- Dodać do `WorkPlan` pole `superseded_by: UUID | None`  
- Przy `POST /planning` (create_plan): jeśli istnieje aktywny plan dla projektu → automatycznie ustaw jego status na `cancelled`, wypełnij `superseded_by`  
- W dok.10 §6 dodać: po zaakceptowaniu nowego raportu, istniejące plany projektu zmieniają status na `cancelled`

---

#### V-03: Brak tabeli custom_templates — gdzie ląduje zatwierdzony szablon ingestii?

**Plik:** dok.07 §2 (`generate_template`), dok.12 §1, dok.16  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:**  
Side 1 (ingestia) umożliwia Knowledge Engineerowi wgranie specyfikacji i wygenerowanie szablonu przez LLM (`generate_template`). Zgodnie z flow:
1. POST /ingestion/spec → LLM generuje szablon Markdown
2. POST /ingestion/{job_id}/approve → szablon "zatwierdzony"

Po zatwierdzeniu **nie wiadomo gdzie szablon ląduje**:
- `it_doc_matrix.db` jest **read-only** (ADR-01, dok.12 §1) — zapis niemożliwy  
- W dok.16 brak tabeli `custom_templates` lub `ingested_templates` w PostgreSQL  
- Żaden ze specyfikowanych dokumentów nie opisuje schematu tej tabeli  
- `SemanticMapper` operuje wyłącznie na `it_doc_matrix.db` — custom templates byłyby niewidoczne

**Wpływ:**  
- Zatwierdzone szablony znikają w próżni — brak persystencji  
- Side 2 (mapowanie) nigdy nie znajdzie własnoręcznie stworzonych szablonów  
- Cały przepływ Side 1 → Side 2 jest niezdefiniowany i niefunkcjonalny

**Naprawa:**  
W dok.16 (lub w dok.04 — schemat DB) zdefiniować tabelę:
```sql
CREATE TABLE custom_templates (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id      UUID REFERENCES projects(id) ON DELETE CASCADE,
    ingestion_job_id UUID NOT NULL,
    title           TEXT NOT NULL,
    category        TEXT,
    phase_id        INTEGER,
    content_md      TEXT NOT NULL,       -- pełna treść szablonu Markdown
    frontmatter_json JSONB,              -- sparsowany YAML frontmatter
    status          TEXT DEFAULT 'draft',-- draft | approved | deprecated
    created_by      UUID REFERENCES users(id),
    created_at      TIMESTAMPTZ DEFAULT now(),
    approved_at     TIMESTAMPTZ
);
```
Opisać mechanizm zapisu w specyfikacji endpointu approve.

---

#### V-04: SemanticMapper nie przeszukuje custom_templates (PostgreSQL)

**Plik:** dok.09 §3, dok.16 §3  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:**  
`SemanticMapper._query_itdoc()` korzysta wyłącznie z `ItdocConnector` (wrapper na `it_doc_matrix.db` — SQLite, read-only). Nie ma żadnej ścieżki wyszukiwania dla szablonów stworzonych przez ingestię (Side 1) przechowywanych w PostgreSQL.

Nawet jeśli tabela `custom_templates` zostałaby zdefiniowana w PostgreSQL (naprawka V-03), SemanticMapper jej nie przeszukuje. Biblioteka itdoc nie wie o szablonach custom.

**Wpływ:**  
- Szablony stworzone przez Knowledge Engineerów są całkowicie niewidoczne dla mechanizmu mapowania  
- Business value Side 1 (ingestia) = zero, dopóki nie ma ścieżki do Side 2

**Naprawa:**  
W dok.09 §3 dodać **Ścieżkę D** (Custom Templates):
```python
# ŚCIEŻKA D: Custom templates z PostgreSQL
custom_docs = await self._custom_template_repo.find_by_project(
    project_id=project_id,
    keywords=entities.keywords
)
for doc in custom_docs:
    _add_candidate(candidates, doc, source="custom_template")
```
Dodać `source_score` dla `custom_template` w tabeli hierarchii źródeł (rekomendacja: 0.45 — wyżej niż keyword fallback bo są specjalnie stworzone dla projektu).

---

#### V-05: Brak mechanizmu wersjonowania doc_uid w WorkPackage

**Plik:** dok.11 §2, dok.12 §1  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
`WorkPackage.doc_uid` (dok.11 §2) odwołuje się do `str(documents.doc_id)` z `it_doc_matrix.db` (np. `"42"`). Biblioteka itdoc jest zewnętrzną read-only bazą, która może być aktualizowana (nowe wersje biblioteki — zmienione szablony, przepisane dokumenty, nowe doc_id).

Brak pola `doc_version` lub `doc_snapshot_at` w `WorkPackage`. Po aktualizacji biblioteki itdoc:
- `doc_uid="42"` może wskazywać na inny dokument lub nie istnieć  
- Istniejące `WorkPackage` są "phantom references"  
- `EstimationReport` z poprzedniej wersji biblioteki może mieć inną wycenę

**Wpływ:**  
- Historyczne plany pracy tracą spójność po aktualizacji biblioteki  
- Audyt "ile godzin poświęcono na dokument X" wskazuje błędny dokument  
- Niemożliwość odtworzenia stanu planu z datą przeszłą

**Naprawa:**  
W dok.11 §2 dodać do `WorkPackage`:
```python
doc_title_snapshot: str   # tytuł w momencie tworzenia planu (snapshot)
doc_phase_snapshot: int   # phase_id w momencie tworzenia planu
itdoc_db_version:   str | None  # wersja biblioteki itdoc (hash lub semver)
```
W dok.12 §5 opisać zmienną `ITDOC_DB_VERSION` (hash pliku lub data modyfikacji).

---

#### V-06: EstimationEngine — brak limitu dokumentów i pagination raportu

**Plik:** dok.10 §6  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
`EstimationEngine.calculate()` iteruje przez wszystkie `mapping.items` w pamięci bez żadnego limitu:
```python
doc_estimates = [
    self.estimate_document(item, ...)
    for item in items       # może być setki dokumentów
]
```

Przy projekcie enterprise z 500+ dokumentami:
- Cała lista `DocumentEstimate` ładowana do RAM jednorazowo  
- `EstimationReport.by_phase` może zawierać tysiące rekordów w JSON response  
- Brak pagination endpointu ani limitu w specyfikacji  
- `classify_complexity` zwraca `"critical"` dla `total_docs >= 200`, ale samo obliczenie 500 doc-estimates nie jest asynchronicznie raportowane (brak progressu)

**Wpływ:**  
- Memory spike przy dużych projektach — potencjalne OOM na małych instancjach  
- Ogromny JSON response (potencjalnie >1 MB) dla `GET /estimation/{id}`  
- Timeout HTTP przy wolnej sieci  
- PM nie widzi postępu dla długich obliczeń

**Naprawa:**  
W dok.10 §6 dodać:
1. `MAX_ESTIMATION_DOCS = 500` jako env var `MAX_ESTIMATION_DOCS`
2. Warning gdy `len(items) > MAX_ESTIMATION_DOCS` + skrócony raport z adnotacją
3. Dla endpoint `GET /estimation/{id}`: pagination dla `by_phase[*].documents` (`?page=1&per_page=50`)

---

## OBSZAR W — Integracja Side 1 (Ingestia) z resztą systemu

---

#### W-01: Cały przepływ Side 1 end-to-end nie jest opisany w żadnym dokumencie

**Plik:** dok.07 §2 (`generate_template`), brak dedykowanego doc dla Side 1  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:**  
Zadanie wymienia "Side 1 ingestia" jako funkcję systemu, a dok.07 zawiera metodę `generate_template`. Jednak w żadnym z przeanalizowanych dokumentów (dok.07–dok.12, dok.16) nie ma:
- Definicji endpointu `POST /ingestion/spec`
- Definicji endpointu `POST /ingestion/{job_id}/approve`
- Schematu tabeli `ingestion_jobs` (lub odpowiednika)
- Opisu state machine dla job'a ingestii
- Opisu jak wygenerowany szablon jest walidowany przed zatwierdzeniem

Dok.07 opisuje metodę `generate_template` w interfejsie `BaseLLMAdapter`, ale nie ma specyfikacji jak jest wywoływana ani co się dzieje z wynikiem.

**Wpływ:**  
- Niemożliwe jest zaimplementowanie Side 1 na podstawie istniejących specyfikacji  
- Brak definicji endpointów → brak OpenAPI schema → brak kontraktu dla frontendu  
- Tabela `ingestion_jobs` nie jest nigdzie zdefiniowana (ani w dok.04, ani dok.16)

**Naprawa:**  
Stworzyć nowy dokument `13_ingestion_spec.md` (lub rozszerzyć istniejący) opisujący:
- Endpointy Side 1 (POST /ingestion/spec, GET /ingestion/{id}, POST /ingestion/{id}/approve, POST /ingestion/{id}/reject)
- Schemat tabeli `ingestion_jobs` w PostgreSQL
- State machine: `pending → processing → review → approved | rejected`
- Integrację z LLMAdapter.generate_template()
- Miejsce zapisu zatwierdzonego szablonu (tabela `custom_templates` — patrz V-03)

---

#### W-02: Pole `industry` w merge_entities nie istnieje w ExtractedEntities (dok.07)

**Plik:** dok.07 §2, dok.09 §2  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:**  
W `merge_entities` (dok.09 §2) odwołuje się do pola `industry`:
```python
industry=new.industry or base.industry,
```
Oraz w `deduplicate_entities`:
```python
industry=entities.industry,
```

Jednak dataclass `ExtractedEntities` w dok.07 §2 **nie ma pola `industry`**:
```python
@dataclass
class ExtractedEntities:
    domains:      list[str]
    standards:    list[str]
    regulations:  list[str]
    phases:       list[int]
    keywords:     list[str]
    project_type: str | None = None
    # brak: industry!
```

Kod z dok.09 nie skompiluje się / nie zadziała poprawnie — `AttributeError: 'ExtractedEntities' object has no attribute 'industry'`.

**Wpływ:**  
- Błąd runtime przy każdym wywołaniu `merge_entities` dla briefu z wieloma chunkami  
- Niezgodność interfejsów między dok.07 (definicja) a dok.09 (użycie)  
- Prawdopodobnie zrodzi się niejasność: czy `industry` to alias dla `domains`, czy osobne pole?

**Naprawa:**  
W dok.07 §2 dodać pole `industry` do `ExtractedEntities`:
```python
@dataclass
class ExtractedEntities:
    domains:      list[str]
    standards:    list[str]
    regulations:  list[str]
    phases:       list[int]
    keywords:     list[str]
    project_type: str | None = None
    industry:     str | None = None   # ← DODAĆ
```
Zaktualizować prompt `extract_entities.txt` (dok.07 §5.1) aby LLM zwracał pole `industry` w JSON. Np. branża: `"fintech"`, `"healthcare"`, `"government"`, `"retail"`, itp.

---

#### W-03: Niejednoznaczność phase_id (0-based vs 1-based) w CRITICAL_PHASES

**Plik:** dok.10 §4  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
W dok.10 §4 zdefiniowano:
```python
CRITICAL_PHASES = {3, 4, 6, 7, 14, 20}
# Wartości 1-based odpowiadające LLM phase_id.
```

Jednak `organize_by_phases()` iteruje po `phase_estimates` i sprawdza:
```python
is_critical = any(d.is_required for d in docs) or phase.phase_id in CRITICAL_PHASES
```

`phase.phase_id` pochodzi z `get_phases()` (dok.12 §3.5), która zwraca `rowid` z tabeli `phases` w SQLite. SQLite rowid zaczyna się od 1 (1-based). Jednak dok.09 §3 (ścieżka C) wykonuje `db_phase_id = phase_id - 1` konwertując 1-based LLM output → 0-based DB.

**Niespójność:** `CRITICAL_PHASES` ma komentarz "1-based", ale `phase.phase_id` z `get_phases()` to też rowid (1-based). Na pozór OK. Jednak doc.09 §3 sugeruje że DB używa 0-based. To stwarza ryzyko pomyłki przy rozszerzaniu kodu.

**Wpływ:**  
- Jeśli ktoś zaktualizuje kod i przyjmie że `phase_id` jest 0-based (jak sugeruje dok.09), `CRITICAL_PHASES` wskaże złe fazy — np. faza 3 (Architecture) stanie się fazą 4 (Design) przez off-by-one  
- Trudne do debugowania błędy w critical path estimation

**Naprawa:**  
W dok.10 §4 wyjaśnić explicite:
> `phase.phase_id` używane w `organize_by_phases` pochodzi z `ItdocConnector.get_phases()` → `rowid` z tabeli `phases` → **1-based**. `CRITICAL_PHASES = {3, 4, 6, 7, 14, 20}` to wartości 1-based (pokrywają się z LLM output).

Dodać stałą z dokumentacją:
```python
# 1-based phase IDs (zgodne z it_doc_matrix.db phases.rowid oraz LLM output)
CRITICAL_PHASES: frozenset[int] = frozenset({3, 4, 6, 7, 14, 20})
```

---

#### W-04: LLM reranking — next() bez fallback (KeyError/StopIteration risk)

**Plik:** dok.09 §5  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
W kodzie LLM rerankingu:
```python
for item in reranked:
    original = next(c for c in top_100 if c.doc_uid == item.doc_uid)
    original.confidence = round(0.6 * original.confidence + 0.4 * item.score, 3)
```

`next(generator)` bez wartości domyślnej rzuci `StopIteration` jeśli LLM zwróci `doc_uid` którego nie ma w `top_100` (np. LLM "hallucynuje" nieistniejący doc_uid, lub zwraca doc_uid spoza przekazanego zestawu kandydatów).

Brak walidacji czy `item.doc_uid` z odpowiedzi LLM należy do przekazanego zestawu. Brak sanitizacji odpowiedzi rerankingu.

**Wpływ:**  
- Nieobsłużony `StopIteration` crashuje mapowanie  
- Przy włączonym `LLM_RERANKING_ENABLED=true` każde mapowanie jest podatne na LLM hallucynacje  
- Błąd trudny do debugowania — traceback wskazuje na integrację LLM, nie na dane wejściowe

**Naprawa:**  
W dok.09 §5 poprawić pętlę:
```python
top_100_map = {c.doc_uid: c for c in top_100}
for item in reranked:
    original = top_100_map.get(item.doc_uid)
    if original is None:
        # LLM hallucynacja — ignoruj wynik rerankingu dla tego doc_uid
        logger.warning(f"LLM rerank: unknown doc_uid={item.doc_uid}, skipping")
        continue
    original.confidence = round(0.6 * original.confidence + 0.4 * item.score, 3)
    original.match_reason += f"; LLM rerank: {item.reason}"
```

---

#### W-05: Brak endpointu GET /projects/{id}/summary — PM nie ma widoku zagregowanego

**Plik:** dok.09 §7, dok.10 §6, dok.11 §4 — brak endpointu podsumowania  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
Persona P2 (Project Manager) musi sprawdzić stan projektu: ile briefów wgranych, status mapowania, aktualny kosztorys, status planu. Brak dedykowanego endpointu agregującego te informacje.

PM musi wykonać co najmniej 4 oddzielne zapytania:
- `GET /projects/{id}` — status projektu
- `GET /briefs?project_id={id}` — lista briefów
- `GET /mapping?project_id={id}` — status mapowania
- `GET /estimation?project_id={id}` — kosztorys
- `GET /planning?project_id={id}` — plan pracy

Żaden z dokumentów (dok.09, dok.10, dok.11) nie wspomina o widoku zbiorczym.

**Wpływ:**  
- Degradacja UX dla PM — kilka callów zamiast jednego  
- Brak możliwości szybkiego dashboardu projektu  
- Frontend musi składać dane z wielu endpointów, ryzyko race conditions

**Naprawa:**  
Dodać do specyfikacji (np. dok.05 lub osobny dok. endpointów) endpoint:
```
GET /projects/{id}/summary
```
Zwracający:
```json
{
  "project_id": "...",
  "status": "active",
  "briefs_count": 3,
  "latest_brief_id": "...",
  "latest_mapping": {"id": "...", "status": "done", "total_items": 87},
  "latest_estimation": {"id": "...", "status": "accepted", "total_h_likely": 261.0},
  "latest_plan": {"id": "...", "status": "draft", "total_packages": 87}
}
```

---

#### W-06: Cross-brief cache content_hash — sekurite: możliwość cache poisoning

**Plik:** dok.09 §11  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
SemanticMapper implementuje cross-brief cache (dok.09 §11):
```python
content_hash = sha256(f"{parsed_text}:{threshold}:{max_results}".encode()).hexdigest()
cached = await db.fetchrow(
    "SELECT * FROM mapping_results WHERE content_hash=$1 AND status='done' "
    "ORDER BY created_at DESC LIMIT 1",
    [content_hash]
)
if cached:
    return MappingResult(**cached, brief_id=current_brief_id, project_id=project_id)
```

**Problem 1:** Cache jest **cross-project** — jeśli dwa projekty różnych klientów mają identyczny brief_text, wynik mapowania z projektu A zostanie zwrócony dla projektu B. `project_id` w zwróconym wyniku jest podmieniane na bieżący, ale `mapping_id` pochodzi z obcego projektu — potencjalny wyciek kontekstu.

**Problem 2:** `confidence_threshold` i `max_results` mogą być różne per projekt (dok.09 §10 — project_settings). Cache ignoruje project-specific scoring weights.

**Wpływ:**  
- Klient B widzi mapowanie wygenerowane w kontekście projektu klienta A  
- Scoring weights skonfigurowane dla projektu A mogą być nieoptymalne dla projektu B  
- Potencjalne naruszenie izolacji danych między klientami (multi-tenant)

**Naprawa:**  
W dok.09 §11 zmodyfikować hash:
```python
# Włącz project_id do hashu aby zapewnić izolację projektów
content_hash = sha256(
    f"{project_id}:{parsed_text}:{threshold}:{max_results}".encode()
).hexdigest()
```
Lub ograniczyć cache do `WHERE content_hash=$1 AND project_id=$2` (dodać filtr projektu w zapytaniu SQL). Opisać decyzję o scope cache w dokumentacji.

---

#### W-07: LIMIT w find_by_keyword hardkodowany przez string formatting (SQL injection risk residual)

**Plik:** dok.12 §3.6  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
W `find_by_keyword` (dok.12 §3.6) parametr `limit` jest wstrzykiwany przez string formatting:
```python
sql += f"                LIMIT {limit}\n            "
```

Wszystkie parametry WHERE są poprawnie sparametryzowane (używają `?`), ale `limit` jest wstawiany bezpośrednio do SQL. Choć `limit` to `int` (z type annotation `limit: int = 100`), brak walidacji czy rzeczywiście jest intem w runtime (Python duck typing).

Analogicznie w `get_documents_by_phase` §3.7:
```python
sql += f"                LIMIT {limit}\n            "
```

**Wpływ:**  
- Jeśli limit pochodzi z request params i nie jest walidowany jako int przed wywołaniem connectora, możliwy SQL injection fragment (np. `limit="100; DROP TABLE documents;"`)  
- Niespójność z resztą kodu który używa parametryzowanych zapytań

**Naprawa:**  
W dok.12 §3.6 i §3.7 dodać walidację:
```python
# Walidacja limit przed użyciem w SQL
safe_limit = max(1, min(int(limit), 1000))   # clip do [1, 1000]
sql += f"LIMIT {safe_limit}\n"
```
Lub zastąpić przez parametryzowany `?` — SQLite obsługuje parametryzowany LIMIT od wersji 3.x.

---

## Podsumowanie znalezisk

| ID | Obszar | Priorytet | Tytuł skrócony |
|----|--------|-----------|----------------|
| U-01 | Konfiguracja | 🟡 WAŻNE | Duplikat RHYTHM_DEPTH z różnymi wartościami |
| U-02 | Konfiguracja | 🟡 WAŻNE | OPENAI_TIMEOUT hardkodowany, brak timeoutów Anthropic/Ollama |
| U-03 | Konfiguracja | 🟡 WAŻNE | CHUNK_MAX_CHARS — stała klasy, _get_chunk_size() nie wywoływana |
| U-04 | Konfiguracja | 🟢 DROBNE | MIN_EXPECTED_DOCS brak env var |
| U-05 | Konfiguracja | 🟡 WAŻNE | Niespójność limitu keywords: 30 (spec) vs 20 (impl) |
| U-06 | Konfiguracja | 🟢 DROBNE | MAX_FILE_SIZE_MB hardkodowane bez env var |
| V-01 | Logika biznesowa | 🔴 KRYTYCZNE | Brak walidacji statusu projektu w Mapper i Engine |
| V-02 | Logika biznesowa | 🔴 KRYTYCZNE | Brak invalidacji WorkPlan po nowym kosztorysie |
| V-03 | Logika biznesowa | 🔴 KRYTYCZNE | Brak tabeli custom_templates — zatwierdzony szablon ląduje w próżni |
| V-04 | Logika biznesowa | 🔴 KRYTYCZNE | SemanticMapper nie przeszukuje custom_templates (PostgreSQL) |
| V-05 | Logika biznesowa | 🟡 WAŻNE | Brak wersjonowania doc_uid w WorkPackage |
| V-06 | Logika biznesowa | 🟡 WAŻNE | EstimationEngine — brak limitu dokumentów, brak pagination |
| W-01 | Integracja Side 1 | 🔴 KRYTYCZNE | Brak specyfikacji endpointów Side 1 (ingestion) |
| W-02 | Integracja | 🔴 KRYTYCZNE | Pole `industry` w merge_entities nie istnieje w ExtractedEntities |
| W-03 | Integracja | 🟡 WAŻNE | Niejednoznaczność phase_id 0-based vs 1-based w CRITICAL_PHASES |
| W-04 | Integracja | 🟡 WAŻNE | LLM reranking next() bez fallback — StopIteration risk |
| W-05 | Integracja | 🟡 WAŻNE | Brak GET /projects/{id}/summary dla PM |
| W-06 | Integracja | 🟡 WAŻNE | Cross-brief cache — brak izolacji projektów (cache poisoning) |
| W-07 | Integracja | 🟡 WAŻNE | LIMIT w find_by_keyword przez string formatting (nie parametryzowany) |

**Łącznie: 19 znalezisk** (5× 🔴 KRYTYCZNE, 12× 🟡 WAŻNE, 2× 🟢 DROBNE)

---

*Generowane przez: AI Documentation Workshop — Analiza Runda 5 Część B*  
*Następna runda: weryfikacja napraw z Rundy 5A + implementacja rekomendacji priorytetów KRYTYCZNYCH*
---
