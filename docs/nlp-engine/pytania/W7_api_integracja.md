---
layer: W7
title: "Warstwa 7 — API i Integracja (FastAPI / Apache Thrift)"
phase: 7
status: planned
docs_version: 1.0.0
tags: [fastapi, thrift, endpoint, CI-CD, async, REST, mikroserwisy, integracja]
---

# Warstwa 7 — API i Integracja (FastAPI / Apache Thrift)

## Przegląd

Warstwa 7 eksponuje cały pipeline NLP (W1-W6) jako REST API i/lub interfejs Apache Thrift.
Zarządza asynchronicznym przetwarzaniem zadań NLP i integracją z systemami zewnętrznymi.

## Uzasadnienie istnienia warstwy

**Dlaczego ta warstwa jest potrzebna:**
W7 istnieje bo klienci systemu (systemy zewnętrzne, interfejsy użytkownika, inne mikroserwisy) nie mogą bezpośrednio importować kodu Python. API stanowi granicę systemową: wersjonowanie kontraktu REST (`/v1/`, `/v2/`) jest niezależne od wewnętrznej implementacji — W1 może zmienić model UDPipe bez zmiany kontraktu API. Asynchroniczność jest konieczna bo pełne przetwarzanie dokumentu przez W1–W6 może trwać 2-10 sekund; synchroniczny endpoint zwróciłby timeout dla dużych dokumentów.

**Co się sypie bez tej warstwy:**
- Klient musi uruchamiać skrypty Python bezpośrednio — niemożliwa integracja z zewnętrznymi systemami klienta (ERP, DMS, systemy prawne)
- Brak versioningu API: każda zmiana wewnętrzna może zepsuć integrację klienta bez ostrzeżenia
- Brak async: duże dokumenty (50+ stron) blokują wątek — HTTP timeout; klient nie wie czy przetwarzanie trwa czy się zawiesiło

**Zależności:**
- Wchodzi: żądania HTTP `POST /nlp/audit` z dokumentem
- Orchestruje: W1 → W6 → W5 → W8 pipeline
- Wychodzi do klienta: `{findings: AuditFinding[], summary: {risk_count, completeness_score}}`
- Wychodzi do W8: triggeruje `AuditEngine` per dokument

## Diagram przepływu danych

```
Klient (HTTP / Thrift)
       |
       v
  FastAPI Router
  +----------------------------------------------+
  |  POST /analyze   -> AsyncTask -> W1-W6        |
  |  GET  /status    -> status zadania            |
  |  POST /audit     -> W0 doc audit              |
  |  GET  /graph     -> Neo4j query W4            |
  +----------------------------------------------+
       |
  Background Worker (asyncio / Celery)
       |
       v
  Pipeline: W1 -> W6 -> W4 (Neo4j)
```

## Pytania źródłowe — sklasyfikowane

### 1. Architektura
- Jakie są zalety biblioteki Thrift w architekturze Multiservice?
- Jakie są zalety Apache Thrift w architekturze Multiservice?
- Jakie są granice W7 — co jest warstwą prezentacji/transportu a co logiką biznesową (należącą do W1–W6)?
- Jaki wzorzec stosuje W7 dla orkiestracji wywołań do warstw wewnętrznych — Chain of Responsibility, Facade?
- Jak W7 obsługuje asynchroniczne przetwarzanie długich dokumentów — polling, webhook, czy Server-Sent Events?
- Jaki jest diagram sekwencji dla żądania /analyze od klienta do W8 (compliance audit) i z powrotem?

### 2. Kontrakty danych
_brak pytań źródłowych w tej kategorii_
- Jaki jest schemat OpenAPI (JSON Schema) dla endpointu /analyze — pokaż wymagane i opcjonalne pola?
- Jak zdefiniować kontrakt dla nagłówka X-Request-ID — UUID v4 obowiązkowy czy opcjonalny?
- Jaki jest format błędu HTTP przy walidacji schematu wejściowego — RFC 7807 Problem Details?
- Jak zdefiniować kontrakt SLA — maksymalny czas odpowiedzi w ms per typ żądania i per wielkość dokumentu?
- Jak wygląda kompletna para request/response JSON dla endpointu /analyze z przykładowymi danymi?
- Jak endpoint /analyze obsługuje dokumenty Markdown z YAML front matter — czy metadane są parsowane i przekazywane downstream?
- Jak endpoint /analyze obsługuje dokumenty Markdown z YAML front matter — czy metadane są parsowane i przekazywane downstream?
- Jak zdefiniować kontrakt dla opcjonalnego pola metadata w ciele żądania /analyze — JSON Schema nullable object?
- Jak zdefiniować kontrakt AuditResponse w Pydantic — pola: document_type, violations, knowledge_gaps, applied_golden_standard, mermaid_diagram?
- Jak zdefiniować document_profile w modelu Pydantic — document_type z KlasyfikatorKontekstu, golden_standard_version, classification_confidence?
- Jak walidować że document_profile.document_type jest kompatybilny z dostępnymi GoldenStandardProfile w AuditEngine?

### 3. Implementacja
- Czy Multiservice oferuje narzędzia do automatyzacji ekstrakcji danych?
- Przejdźmy do Fazy 7 i zaprojektujmy API dla grafu.
- Czy warto użyć Apache Thrift do komunikacji między mikroserwisami?
- Pokaż implementację IntentClassifier dla aktów mowy w spaCy..
- Jak rozszerzyć IntentClassifier o rozpoznawanie aktów zaprzeczenia?
- Jakie 6 komend diagnostycznych dodałeś do whitelisty SystemExecutor?
- Jakie to 6 komend diagnostycznych w whiteliscie SystemExecutor?
- Pokaż implementację FastAPI routera /analyze z walidacją Pydantic i przekazaniem do orchestratora?
- Jak zaimplementować middleware do rate limitingu (np. slowapi) w FastAPI dla /analyze?
- Jak zaimplementować circuit breaker dla wywołań do downstream W5 — biblioteka tenacity czy własna implementacja?
- Jak skonfigurować Uvicorn z kilkoma workerami i współdzielonym dostępem do zasobów wewnętrznych?
- Jak zaimplementować endpoint /health zwracający status każdej warstwy wewnętrznej (W1–W8)?
- Jak zaimplementować obsługę Apache Thrift po stronie serwera — generowany stub czy ręczny handler?
- Jak zaimplementować structured logging (JSON) w FastAPI z correlation ID per request?
- Jakie parametry przyjmuje endpoint /audit — surowy tekst, JSON z metadanymi dokumentu, czy plik multipart/form-data?
- Jak paginować wyniki /audit gdy dokument ma setki naruszeń — cursor-based czy offset pagination?
- Jak zaimplementować asynchroniczny endpoint /audit używając FastAPI BackgroundTasks lub asyncio?
- Jak zabezpieczyć /audit przed nieautoryzowanym dostępem — Bearer token, API Key, czy mTLS?
- Jak wdrożyć /audit jako kontener Docker — Dockerfile, health check, uwicorn workers?
- Jak skonfigurować reverse proxy (Nginx/Traefik) przed /audit — timeout, max body size, TLS termination?
- Pokaż jak zintegrować document_profile z AuditResponse w FastAPI — endpoint /audit pobiera dokument, wywołuje KlasyfikatorKontekstu, konstruuje AuditResponse?
- Jak endpoint /audit zwraca document_profile w odpowiedzi — pole `profile` z document_type, golden_standard i confidence?
- Stwórzmy punkt wejścia `python -m audit` dla CI/CD — jak audit/__main__.py rejestruje te same handlery co FastAPI endpoint /audit ale bez serwera HTTP?
- Jak współdzielić logikę między audit/__main__.py (CLI) a endpointem /audit (FastAPI) — wspólna klasa AuditService używana przez obie warstwy wejścia?

### 4. Testowanie
- Gdzie w procesie CI/CD uruchomić te testy?
- Stwórzmy teraz czerwony test integracyjny dla endpointu API..
- Pokaż przykład testu integracyjnego POST /analyze i statusu zadania..
- Jak napisać test integracyjny dla /analyze który mockuje W5 (silnik wnioskowania) i weryfikuje kontrakt JSON?
- Jak testować rate limiting — czy test powinien wysłać N+1 żądań i sprawdzić 429 Too Many Requests?
- Jak napisać test dla circuit breaker — wymuś timeout downstream i sprawdź że API zwraca 503 a nie wiesza?
- Jak testować wersjonowanie API — czy v1 i v2 endpointy zwracają różne schematy przy tym samym wejściu?
- Jak zmierzyć czas odpowiedzi /analyze dla dokumentu 10 kB, 100 kB, 1 MB — pokaż benchmark test?
- Jak napisać test smoke dla health endpoint po deployu — czy wszystkie warstwy raportują status OK?

### 5. Obsługa błędów
_brak pytań źródłowych w tej kategorii_
- Jak obsłużyć 503 Service Unavailable gdy downstream W5 (silnik wnioskowania) nie odpowiada?
- Jaki HTTP status code zwrócić gdy dokument wejściowy przekracza maksymalny limit rozmiaru?
- Jak logować błędy walidacji schematu wejściowego bez ujawniania treści dokumentu w logach HTTP?
- Co zwrócić klientowi gdy pipeline przetwarza poprawnie ale zwraca 0 wyników — 200 z pustą listą czy inny status?
- Jak obsłużyć błąd deserializacji JSON — RFC 7807 z informacją o konkretnym polu które nie pasuje do schematu?

### 6. Integracja z innymi warstwami
- Jak zintegrować RapidMiner z Multiservice do analizy NKJP?
- Jak zintegrować RapidMiner z Multiservice do analizy korpusu?
- Jak zintegrować wyniki z Multiservice z bazą Neo4j?
- Jak zaprojektować FastAPI do obsługi asynchronicznych zadań NLP?
- Przejdźmy do Fazy 7 i stwórzmy API w FastAPI..
- Pokaż jak zdefiniować interfejs Apache Thrift dla potoku NLP..
- Stwórzmy endpoint FastAPI i połączmy go z naszym pipeline..
- Stwórzmy teraz endpoint /analyze w FastAPI łączący wszystkie moduły..
- Pokaż jak zintegrować akcję COMMAND z systemem operacyjnym..
- Jak zintegrować akcję COMMAND z endpointem FastAPI?
- Zintegrujmy endpoint FastAPI z pełnym potokiem analizy intencji..
- Pokaż kod api.py z endpointem /audit dla FastAPI.
- Jak endpoint /analyze przekazuje pole document_type (wynik KlasyfikatorKontekstu) do warstw W5 i W8?
- Czy klient API może explicite podać document_type w żądaniu i pominąć KlasyfikatorKontekstu?
- Jak zintegrować audit_cli.py z FastAPI — endpoint POST /audit/batch który uruchamia ten sam pipeline co CLI i zwraca identyczny JSON?
- Jak skonfigurować krok w audit.yml do smoke testu endpointu /audit po deploymencie — curl POST z przykładowym dokumentem i weryfikacja exit code?

### 7. Pułapki i ryzyka
_brak pytań źródłowych w tej kategorii_
- Co się dzieje gdy klient wysyła żądanie z niepoprawnym Content-Type (nie application/json)?
- Jak uniknąć desynchronizacji wersji API gdy klient używa v1 a serwer zaktualizował schemat do v2?
- Jakie jest ryzyko wycieku danych wrażliwych (treść umów, dane osobowe) w logach HTTP przy debugowaniu?
- Co się dzieje gdy Apache Thrift zgłosi TimeoutException przy wywołaniu W5 z W8 podczas audytu?
- Jak obsłużyć partial response gdy pipeline przetwarza duży dokument i połączenie HTTP się urywa w trakcie?
- Czy FastAPI automatycznie waliduje schemat wejściowy — co dzieje się przy polu null gdy schemat wymaga string?
- Jak zapobiec przeciążeniu endpointu /analyze gdy jeden klient wysyła tysiące żądań bez rate limitingu?

## Pytania uzupełniające
- **Pułapka 3:** FastAPI deserializuje request body do Pydantic model — błąd walidacji zwraca 422, nie 400; klienci API (np. systemy klientów) mogą nie obsługiwać 422 i traktować to jako sukces po stronie sieci.
- **Pułapka 4:** Synchroniczne wywołanie pipeline NLP w handlerze HTTP — przy 30s timeout serwer HTTP zwróci 504, ale pipeline NLP nadal przetwarza w tle, blokując zasoby.
- **Pułapka 5:** CORS bez jawnej listy dozwolonych origin — `allow_origins=["*"]` w FastAPI to luka bezpieczeństwa dla endpointów API płatnych serwisów.
- **Pułapka 6:** Wersjonowanie API przez URL (`/v1/analyze`) vs header (`Accept-Version`) — zmiana konwencji łamie wszystkich klientów jednocześnie; decyzja musi być podjęta przed pierwszym publicznym deploymentem.

### 1. Architektura

- Jak podzielić odpowiedzialność między FastAPI router a pipeline orchestrator?
- Czy używać Celery do kolejkowania zadań czy asyncio background tasks?
- Jak zdefiniować interfejs Apache Thrift .thrift dla potoku NLP?
- Jakie są trade-offs między FastAPI (REST) a Thrift (RPC) dla tego projektu?
- Jak zaprojektować graceful degradation gdy Neo4j jest niedostępny?

### 2. Kontrakty danych

- Jaki jest schemat request body dla POST /analyze — pola: text, language, options?
- Jaki jest schemat response dla POST /analyze — task_id, status, result?
- Jak walidować wejście — max długość tekstu, obsługiwane języki, wymagane pola?
- Jaki jest schemat błędu (error response) — fields: code, message, detail?
- Jak wersjonować API — /v1/analyze vs /v2/analyze?

### 3. Implementacja

- Jak zaimplementować POST /analyze endpoint z async przetwarzaniem?
- Jak zaimplementować GET /status sprawdzający postęp zadania?
- Jak połączyć endpoint /analyze z pełnym potokiem W1-W6?
- Jak zdefiniować interfejs .thrift dla operacji analyze(text) -> AnalysisResult?
- Jak zaimplementować endpoint /audit wywołujący W0 (doc_auditor)?

### 4. Testowanie

- Jak napisać test integracyjny POST /analyze — sprawdzić status 200 i strukturę odpowiedzi?
- Jak testować asynchroniczne zadania — mock background worker?
- Jak pisać testy kontraktowe dla API (OpenAPI schema validation)?
- Jak testować endpoint pod obciążeniem — 100 równoległych żądań?
- Gdzie w CI/CD uruchomić testy integracyjne API?
#### Kompletna hierarchia TDD
- Napisz czerwony test TDD dla `POST /nlp/audit` — `test_audit_returns_findings()`: żądanie z dokumentem → oczekiwany status 200 i lista `AuditFinding`.
- Zaimplementuj Fazę GREEN dla endpointu `POST /nlp/audit` — minimalna wersja: przyjmij tekst, wywołaj `InferenceEngine.run()`, zwróć JSON.
- Jak zrefaktoryzować endpoint `/nlp/audit` po GREEN — dodać walidację Pydantic, obsługę błędów HTTP 422 i rate limiting?
- Zrefaktoryzuj endpoint API — wydzielić `AuditRequestValidator`, `PipelineOrchestrator`, `ResponseFormatter` jako osobne klasy z testami jednostkowymi.
- Jak napisać test jednostkowy dla `AuditRequestValidator.validate()` — sprawdzić odrzucenie żądania bez pola `document_text`?
- Jak zbudować oracle dataset dla API — 10 dokumentów kontraktowych + oczekiwany `AuditFinding[]` per dokument — zapiąć w CI?
- Jak zmierzyć Mutation Score dla walidacji API — które gałęzie obsługi błędów są najtrudniejsze do pokrycia?
- Jak napisać test własnościowy (Hypothesis) dla API — dla każdego poprawnego dokumentu odpowiedź powinna być deterministyczna (ten sam dokument → te same findings)?
- Jak wykryć regresję API po deployu — automatyczny smoke test: wyślij 3 znane dokumenty → sprawdź że wyniki nie zmieniły się vs baseline?
- Stwórz test regresyjny API — golden file: 5 dokumentów + oczekiwany JSON response; CI fail przy zmianie kształtu odpowiedzi.
- Jak przetestować pełne API E2E — `POST /nlp/audit` z dokumentem SRS → sprawdź że response zawiera CONS-02 i RISK-01 findings z doc_ref?

### 5. Obsługa błędów

- Co zwrócić gdy tekst wejściowy jest pusty lub za długi (>10000 znaków)?
- Jak obsługiwać timeout przetwarzania (pipeline trwa >30s)?
- Co zwrócić gdy Neo4j jest niedostępny — 503 czy degraded response?
- Jak logować błędy pipeline per request_id dla debugowania?
- Jak obsługiwać równoczesne żądania bez race condition w StateMatrix (W5)?
- Jak API obsługuje request z `Content-Type: application/json` ale ciałem które nie jest validnym JSON?
- Co zwrócić gdy downstream serwis (W1–W6) zwraca 500 — propagować błąd czy zwrócić częściowy wynik z ostrzeżeniem?

### 6. Integracja z innymi warstwami

- Jak W7 wywołuje W1 — bezpośrednio czy przez dependency injection?
- Jak W7 przekazuje wyniki pipeline do W8 (AuditEngine)?
- Czy W7 ma własną bazę do przechowywania wyników zadań, czy używa Neo4j (W4)?
- Jak W0 (doc audit CLI) integruje się z W7 API — czy obie ścieżki są niezależne?
- Jak W7 obsługuje częściowe niepowodzenie pipeline — gdy W3 jest niedostępne a W1 i W2 działają?
- Jak W7 wersjonuje kontrakt API przy jednoczesnym wsparciu v1 i v2 klientów?
- Jak weryfikować że response W7 jest spójny z wynikami W8 (compliance audit)?

### 7. Pułapki i ryzyka

- **Pułapka 1:** Synchroniczne przetwarzanie NLP w handlerze FastAPI blokuje event loop — zawsze używać background_tasks lub Celery.
- **Pułapka 2:** Brak rate limitingu = jeden klient może zapchać cały pipeline. Wdrożyć slowapi lub Nginx rate limit.
- **Pułapka 3:** Thrift i FastAPI mają różne modele błędów — ujednolicenie error handling jest konieczne zanim wdrożysz oba.
- **Pułapka 3:** FastAPI zwraca 422 (nie 400) dla błędów walidacji — klienci nieobsługujący 422 mogą traktować to jako sukces po stronie sieci.
- **Pułapka 4:** Synchroniczne wywołanie pipeline NLP w handlerze HTTP — przy timeoucie 30s serwer zwraca 504, ale pipeline nadal przetwarza w tle blokując zasoby.
- **Pułapka 5:** `allow_origins=["*"]` w FastAPI to luka CORS dla płatnych endpointów API.
- **Pułapka 6:** Wersjonowanie API przez URL (`/v1/`) vs header — decyzja musi być podjęta przed pierwszym publicznym deploymentem; zmiana konwencji łamie wszystkich klientów.

## Kryteria akceptacji

| Metryka | Minimum |
|---|---|
| Czas odpowiedzi POST /analyze (< 1000 znaków) | < 5 s |
| Throughput przy 10 równoległych żądaniach | >= 5 req/s |
| HTTP 200 dla prawidłowych żądań | 100% |
| Pokrycie testów integracyjnych endpointów | >= 80% |
| Czas uruchomienia serwisu (cold start) | < 10 s |

## Pytania o idempotentność i deterministyczność

- Czy dwa identyczne POST /analyze z tym samym tekstem dają identyczne wyniki?
- Czy task_id jest unikalny i niemutowalny po utworzeniu?
- Jak zapewnić, że retry żądania nie tworzy duplikatów w Neo4j?

## Pytania o migrację i wersjonowanie

- Jak wersjonować API endpoint bez łamania istniejących klientów?
- Jak migrować .thrift IDL gdy dodajemy nowe pola do AnalysisResult?
- Jak obsłużyć deprecation starego endpointu z odpowiednim wyprzedzeniem?

## Pytania o audytowalność

- Jak każde żądanie do API jest logowane z request_id, user_id, timestamp?
- Jak przechowywać pełny ślad żądanie -> pipeline steps -> wynik dla celów dowodowych?
- Jak wygenerować raport "co system zwrócił klientowi X dla tekstu Y w dacie Z"?

---

## Rozszerzalność i skalowanie

### Skalowanie throughput API

- Jak API zachowuje się przy 10 / 100 / 1000 równoległych żądaniach — gdzie jest punkt nasycenia?
- Jak zaimplementować horizontal scaling — kilka instancji FastAPI za load balancerem?
- Jak Neo4j (W4) zachowuje się przy 1000 równoległych read queries z W7?
- Jak zaimplementować circuit breaker dla W7 → W4 (Neo4j) przy przeciążeniu?
- Jak testować API pod obciążeniem — locust, k6, czy pytest-benchmark?

### Stopniowe rozszerzanie API (nie łamiące)

- Jak dodać nowy endpoint `/v2/analyze-deep` bez deprecacji `/v1/analyze`?
- Jak zaimplementować feature flags — włączanie nowych funkcji pipeline bez nowego deploy?
- Jak wersjonować `.thrift` IDL — backward-compatible zmiany vs breaking changes?
- Jak zaimplementować `OPTIONS /analyze` zwracający capabilities aktualnej wersji?
- Jak stopniowo włączać nowe warstwy (W2, W3, W4) do odpowiedzi API bez łamania klientów?

### Inkrementalne wdrożenia

- Jak zaimplementować canary deployment — 10% ruchu na nową wersję pipeline?
- Jak monitorować regresję po wdrożeniu — automatyczny A/B test wyników W1 v1 vs v2?
- Jak rollbackować do poprzedniej wersji pipeline bez utraty wyników zbuforowanych w Neo4j?
- Jak obsługiwać graceful shutdown — nie przerywać przetwarzania w toku przy restarcie?
