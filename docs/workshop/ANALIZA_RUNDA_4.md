# Analiza Rundy 4 — Część A: Obszary M, N, O

**Data:** 2025-01  
**Pliki źródłowe:** dok.03, dok.04, dok.05, dok.06, dok.13, dok.15  
**Poprzednie rundy naprawiły:** lru_cache/async, SQL injection, phase indexing, BriefStatus/DocumentEstimate, startup recovery, response_content, enums (projects/briefs/webhook), confidence_threshold=0.4, project_id w map()

---

## OBSZAR M — CI/CD i Deployment

#### M-01: Brak treści docker-compose.yml — healthcheck i kolejność startu nieokreślone
**Plik:** dok.03 §5, dok.15 §2 Faza 1  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** Struktura katalogów w dok.03 wymienia `docker-compose.yml`, a kryterium go/no-go Fazy 1 brzmi „Docker Compose startuje bez błędów", lecz **zawartość pliku nigdzie nie jest wyspecyfikowana**. Brak definicji: healthcheck dla serwisu `db`, `depends_on` z `condition: service_healthy`, sieci Docker, wolumenu read-only dla `itdoc`, zmiennych środowiskowych przesyłanych do kontenera FastAPI.  
**Wpływ:** FastAPI startuje zanim PostgreSQL jest gotowy → `asyncpg` rzuca `ConnectionRefusedError` przy pierwszym requeście; itdoc SQLite może być niedostępny bo wolumen nie jest zamontowany. Developmentowy onboarding niemożliwy bez dodatkowych instrukcji ustnych.  
**Naprawa:** Dodać do dok.03 lub osobnego dok.17 minimalny `docker-compose.yml`:

```yaml
services:
  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: workshop
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: workshop_db
    volumes:
      - pg_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U workshop -d workshop_db"]
      interval: 5s
      timeout: 5s
      retries: 10
    # NIE eksponuj portu 5432 na host (dok.13 §4)

  app:
    build: .
    env_file: .env
    ports:
      - "8000:8000"
    volumes:
      - ./itdoc_library:/app/itdoc_library:ro   # read-only (ADR-01)
    depends_on:
      db:
        condition: service_healthy
    command: >
      sh -c "alembic upgrade head && uvicorn api.main:app --host 0.0.0.0 --port 8000"

volumes:
  pg_data:
```

---

#### M-02: Brak rollback strategy dla migracji Alembic — co gdy 0008 się nie powiedzie
**Plik:** dok.04 §4  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** Dok.04 §4 wymienia 8 migracji (0001–0008) i polecenia `alembic upgrade head` / `alembic downgrade -1`, ale **brak jakiejkolwiek strategii rollback**: co zrobić gdy migracja 0008 (`quality_snapshots`) zakończy się błędem w połowie? Brak specyfikacji: czy migracje są transakcyjne, czy CI pipeline cofa deployment przy błędzie migracji, czy jest strategia blue-green lub pre-migration backup.  
**Wpływ:** Częściowo zastosowana migracja 0007 (`document_embeddings`) lub 0008 może zostawić schemat DB w niespójnym stanie → aplikacja nie startuje, brak możliwości automatycznego odtworzenia produkcji.  
**Naprawa:** Dodać do dok.04 §4 sekcję „Rollback strategy":

```markdown
## Polityka rollback migracji

1. **Każda migracja musi mieć `downgrade()`** — autogenerate nie gwarantuje poprawności;
   review wymagany przed merge.
2. **Backup przed migracją** (CI/CD step):
   `pg_dump workshop_db > backup_$(date +%Y%m%d_%H%M%S).sql`
3. **Przy błędzie upgrade** — CI pipeline wykonuje:
   `alembic downgrade <poprzednia_wersja>` i przywraca backup.
4. **Migracje 0007 (embeddings) i 0008 (quality_snapshots)** są opcjonalne —
   aplikacja musi startować bez nich (graceful degradation).
```

---

#### M-03: Alembic w CI — brak specyfikacji kiedy i przez kogo uruchamiane
**Plik:** dok.15 §2 Faza 1, dok.03 §6  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Dok.15 Faza 1 wymaga że „Alembic migrations przechodzą bez błędów" jako kryterium go/no-go, ale **nigdzie nie jest opisany pipeline CI**: czy migracje uruchamiają się w ramach `docker compose up` (entrypoint), osobnym step CI/CD, czy ręcznie przez administratora. Brak też informacji o osobnym użytkowniku Alembic z uprawnieniami DDL (`CREATE TABLE`, `ALTER`) oddzielonym od użytkownika runtime `workshop_app` (który w dok.13 §4 nie ma DDL).  
**Wpływ:** Użytkownik `workshop_app` z dok.13 §4 nie ma `CREATE TABLE` → `alembic upgrade head` uruchomiony przez aplikację zakończy się błędem `InsufficientPrivilege` w PostgreSQL.  
**Naprawa:** Dodać do dok.13 §4 sekcję:

```sql
-- Osobny użytkownik dla migracji (ma DDL)
CREATE USER workshop_migrator WITH PASSWORD '${MIGRATOR_PASSWORD}';
GRANT ALL PRIVILEGES ON DATABASE workshop_db TO workshop_migrator;
-- .env.migrations (tylko dla CI/CD step, nie aplikacja runtime):
ALEMBIC_DATABASE_URL=postgresql://workshop_migrator:${MIGRATOR_PASSWORD}@db:5432/workshop_db
```

CI pipeline: `step migrate: alembic -x data=true upgrade head` przed `step start: uvicorn`.

---

#### M-04: Secrets management — .env w Dockerze, brak Docker secrets / Vault dla produkcji
**Plik:** dok.13 §3  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Dok.13 §3 definiuje hierarchię konfiguracji: zmienne środowiskowe > `.env` > defaults. Plik `.env` jest montowany lub kopiowany do kontenera. Dla środowiska produkcyjnego brak jakiejkolwiek wzmianki o bezpieczniejszych mechanizmach: Docker secrets (`docker secret create`), HashiCorp Vault, AWS SSM Parameter Store, Kubernetes Secrets. Klucze `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `DATABASE_URL` z hasłem są przechowywane jako plain text w `.env` który może trafić do logów, `docker inspect`, `ps aux`.  
**Wpływ:** Wyciek klucza API OpenAI/Anthropic → koszty finansowe; wyciek `DATABASE_URL` → dostęp do danych klientów w PostgreSQL.  
**Naprawa:** Dodać do dok.13 §3 sekcję „Produkcja":

```markdown
### Środowisko produkcyjne — Docker secrets (Docker Swarm)

Zamiast `.env`, użyj Docker secrets:
```
docker secret create openai_api_key openai_key.txt
docker secret create workshop_api_keys keys.txt
```

W `config.py` dodaj fallback do `/run/secrets/<name>`:
```python
@field_validator('openai_api_key', mode='before')
def load_from_secret(cls, v):
    if not v:
        secret_path = Path("/run/secrets/openai_api_key")
        if secret_path.exists():
            return secret_path.read_text().strip()
    return v
```
```

---

#### M-05: Brak lokalnego setup guide krok po kroku
**Plik:** dok.03 §5, dok.15  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Żaden dokument nie zawiera kompletnej instrukcji „jak uruchomić system lokalnie od zera". Dok.03 pokazuje strukturę katalogów, dok.15 definiuje fazy implementacji, dok.13 pokazuje `.env.example`, ale **nie ma spójnego quick-start**: git clone → pip install → cp .env.example .env → docker compose up → alembic upgrade → test /health. Brak też informacji jak zamontować bibliotekę itdoc do Dockera.  
**Wpływ:** Nowy developer spędza godziny na konfiguracji; ryzyko pomyłek przy konfiguracji (np. zapomniana migracja, nieodpowiedni `ITDOC_DB_PATH`).  
**Naprawa:** Dodać do dok.03 lub README sekcję:

```markdown
## Quick Start (lokalne uruchomienie)

1. `cp workshop/.env.example workshop/.env` — uzupełnij OPENAI_API_KEY, WORKSHOP_API_KEYS
2. `ITDOC_DB_PATH=/ścieżka/do/it_doc_matrix.db` (lub umieść w `workshop/itdoc_library/`)
3. `docker compose up -d db` — uruchom PostgreSQL
4. `docker compose run --rm app alembic upgrade head` — zastosuj migracje
5. `docker compose up app` — uruchom FastAPI
6. `curl http://localhost:8000/health` — oczekiwane: `{"status":"ok","db":"ok","itdoc":{...}}`
7. `pytest tests/` — uruchom testy (wymaga testcontainers lub działającego DB)
```

---

## OBSZAR N — Monitoring i Observability

#### N-01: Brak structured JSON logging — tylko plain text w middleware
**Plik:** dok.13 §6  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** `SecurityAwareLoggingMiddleware` (dok.13 §6) loguje: `logger.info(f"{request.method} {request.url.path}")` — **plain text bez struktury**. Brak: formatu JSON, pola `timestamp`, `level`, `service`, `request_id`, `duration_ms`, `status_code`. Żaden dokument nie definiuje formatu logów ani biblioteki (`structlog`, `python-json-logger`).  
**Wpływ:** Logi niemożliwe do parsowania przez systemy jak Loki, Elasticsearch, Datadog. Debugowanie produkcyjnych błędów wymaga ręcznego grep'owania. Brak możliwości budowania dashboardów i alertów.  
**Naprawa:** Dodać do dok.13 §6 specyfikację:

```python
# Wymagany format logu (JSON per linia):
{
  "timestamp": "2025-01-14T10:30:00.123Z",
  "level": "INFO",
  "service": "workshop-api",
  "request_id": "req_a1b2c3d4",
  "method": "POST",
  "path": "/brief/upload",
  "status_code": 201,
  "duration_ms": 342,
  "api_key_prefix": "key_agen"  # pierwsze 8 znaków
}
# Biblioteka: python-json-logger (pip install python-json-logger)
# LUB structlog z JSONRenderer
```

---

#### N-02: Brak Correlation ID — request_id niespójny między modułami
**Plik:** dok.05 §4, dok.06 `ErrorResponse`  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** Schema `ErrorResponse` w dok.06 ma pole `request_id: "req_abc123"`, ale **nie ma specyfikacji jak `request_id` jest generowany** (UUID v4? losowy prefix?), **propagowany** między routerami i serwisami, **dołączany do logów** i **zwracany w nagłówku odpowiedzi**. Kod w dok.13 §6 i §8 nie przekazuje żadnego ID. Background task `_run_mapping_task` (dok.05 §8.1) działa całkowicie bez kontekstu request.  
**Wpływ:** Niemożliwe śledzenie jednego requestu przez logi wielu serwisów i background tasks. Klient zgłasza błąd z `request_id` z odpowiedzi, ale logi serwera nie zawierają tego ID.  
**Naprawa:** Dodać do dok.13 middleware generujący i propagujący request_id:

```python
import uuid
from contextvars import ContextVar

request_id_var: ContextVar[str] = ContextVar('request_id', default='')

class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        rid = request.headers.get("X-Request-ID") or f"req_{uuid.uuid4().hex[:8]}"
        request_id_var.set(rid)
        response = await call_next(request)
        response.headers["X-Request-ID"] = rid
        return response

# W loggerze: logger.info("...", extra={"request_id": request_id_var.get()})
# W background tasks: przekazuj request_id jako argument do asyncio.create_task(...)
```

---

#### N-03: Brak endpointów Prometheus /metrics — zero specyfikacji metryk
**Plik:** dok.03, dok.13, dok.15  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Żaden z dokumentów nie wspomina o eksporcie metryk Prometheus ani OpenMetrics. Brak endpointu `/metrics`, brak listy zbieranych metryk, brak biblioteki (`prometheus-fastapi-instrumentator`). System ma kluczowe metryki do monitorowania: czas mapowania, liczba wywołań LLM, rozmiar kolejki background tasks, empty_rate mapowań, wskaźnik błędów per endpoint.  
**Wpływ:** Brak możliwości monitorowania stanu systemu w produkcji. Problemy (degradacja jakości mapowania, LLM timeout burst) są niewidoczne do momentu zgłoszenia błędu przez użytkownika.  
**Naprawa:** Dodać do dok.13 (lub nowego dok.17) sekcję:

```python
# pyproject.toml: prometheus-fastapi-instrumentator>=7.0

from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram, Counter, Gauge

# Metryki aplikacyjne (ponad domyślne HTTP):
mapping_duration = Histogram("mapping_duration_seconds", "Czas mapowania briefu",
                              buckets=[1, 5, 10, 30, 60, 120])
llm_calls_total  = Counter("llm_calls_total", "Wywołania LLM", ["provider", "operation", "status"])
empty_mapping_rate = Gauge("empty_mapping_rate", "Odsetek pustych mapowań (ostatnie 100)")
webhook_queue_depth = Gauge("webhook_queue_depth", "Liczba oczekujących webhooków")

Instrumentator().instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)
# /metrics dostępny bez X-API-Key (ale ograniczony do sieci wewnętrznej przez firewall)
```

---

#### N-04: /health nie sprawdza statusu LLM provider
**Plik:** dok.06 `/health`, dok.15 §2 kryterium go/no-go  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Endpoint `/health` w dok.06 zwraca `db: ok/error` i rozbudowany status `itdoc`, ale **brak sprawdzenia LLM provider**. Jeśli `LLM_PROVIDER=openai` a klucz jest nieważny lub OpenAI ma outage, `/health` nadal zwraca `{"status": "ok"}`. Kryterium go/no-go Fazy 1 (dok.15) sprawdza tylko DB i itdoc.  
**Wpływ:** Load balancer uznaje serwis za zdrowy mimo że 100% requestów do `/brief/{id}/map` zakończy się błędem 503. Trudne diagnozy operacyjne.  
**Naprawa:** Dodać do schematu `/health` w dok.06:

```yaml
llm:
  type: object
  properties:
    status:
      type: string
      enum: [ok, degraded, error, disabled]
    provider:
      type: string
      example: "openai"
    model:
      type: string
      example: "gpt-4o"
    last_check_ms:
      type: integer
    error_message:
      type: string
      nullable: true
```

Implementacja: przy starcie i co 60s (background task) wykonaj tanią operację ping (np. `models.list()` dla OpenAI lub `GET /api/tags` dla Ollama). Cache wynik — nie sprawdzaj przy każdym `/health` requeście.

---

#### N-05: Brak distributed tracing (OpenTelemetry) — background tasks nieśledzone
**Plik:** dok.03 ADR-04, dok.05 §2.2  
**Priorytet:** 🟡 WAŻNE  
**Problem:** System wykonuje długie asynchroniczne operacje: mapping background task (asyncio.create_task), LLM calls (zewnętrzne API), itdoc queries (run_in_executor), webhook dispatch. **Brak OpenTelemetry tracingu** — niemożliwe śledzenie przyczyny wolnych requestów (czy wolno działa LLM, DB, itdoc, czy scorer?). Żaden dokument nie wspomina o OTEL.  
**Wpływ:** Przy problemie produkcyjnym (mapowanie zajmuje 120s zamiast 30s) niemożliwe ustalenie gdzie jest bottleneck bez dodatkowych logów debugowania.  
**Naprawa:** Dodać do dok.13 rekomendację (opcjonalne, ale specyfikowane):

```python
# pyproject.toml: opentelemetry-instrumentation-fastapi, opentelemetry-instrumentation-sqlalchemy
# Minimalna konfiguracja OTEL SDK z eksportem do Jaeger lub OTLP:
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
FastAPIInstrumentor.instrument_app(app)
SQLAlchemyInstrumentor().instrument(engine=engine)
# Span manualny dla LLM calls i itdoc.run_in_executor
```

---

#### N-06: Brak definicji progów alertów — metryki bez SLO
**Plik:** dok.15 §2–5, dok.16 (referenced)  
**Priorytet:** 🟢 DROBNE  
**Problem:** Dok.15 definiuje kryteria go/no-go na poziomie testów (np. `empty_rate < 20%`), ale **brak operacyjnych SLO i progów alertów** dla działającego systemu. Nie zdefiniowano: max akceptowalny czas mapowania, max error rate per endpoint, max queue depth background tasks, próg alertu dla `avg_confidence` poniżej którego jakość mapowania jest niedopuszczalna.  
**Wpływ:** Brak możliwości skonfigurowania alertów w Prometheus/Grafana/PagerDuty. Degradacja jakości systemu jest niewidoczna operacyjnie.  
**Naprawa:** Dodać do dok.13 lub nowego dok.17 tabelę SLO:

```markdown
| Metryka                    | Próg WARNING  | Próg CRITICAL | Akcja                    |
|----------------------------|---------------|----------------|--------------------------|
| mapping_duration_seconds   | p95 > 60s     | p95 > 120s     | Zwiększ LLM_TIMEOUT      |
| llm_error_rate (5m window) | > 5%          | > 20%          | Sprawdź LLM provider     |
| empty_mapping_rate         | > 15%         | > 30%          | Sprawdź itdoc DB         |
| webhook_queue_depth        | > 50          | > 200          | Sprawdź delivery errors  |
| db_connection_pool_usage   | > 70%         | > 90%          | Zwiększ pool_size        |
```

---

## OBSZAR O — Multi-tenancy i Security

#### O-01: Brak globalnego rate limiting API — tylko LLM semaphore
**Plik:** dok.13 §7, §8  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** Dok.13 §7 definiuje rate limiting tylko dla równoległych wywołań LLM (semaphore na 3 callsy). Dok.13 §8 definiuje per-projekt rate limiting dla mapowania, ale tylko opcjonalnie i tylko dla jednego endpointu. **Brak globalnego rate limitingu HTTP** — żaden endpoint API nie ma limitu requestów per klucz API lub per IP. Atakujący (lub błędny agent) z ważnym kluczem może zasypać serwis tysiącami requestów do `POST /brief/upload` lub `POST /brief/{id}/map`.  
**Wpływ:** DoS atakujący z ważnym kluczem API; przypadkowy loop w AI agencie → wyczerpanie DB connection pool, dysk pełen briefami, LLM semaphore blokuje wszystkich użytkowników.  
**Naprawa:** Dodać do dok.13 §7:

```python
# pyproject.toml: slowapi>=0.1.9

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Na endpointach intensywnych:
@router.post("/upload")
@limiter.limit("20/minute")          # max 20 uploadów/min per IP/key
async def upload_brief(...): ...

@router.post("/{brief_id}/map")
@limiter.limit("10/minute")          # max 10 mapowań/min
async def map_brief(...): ...
```

---

#### O-02: Brak specyfikacji CORS — `main.py` ma „CORS" w komentarzu ale bez konfiguracji
**Plik:** dok.03 §5 (main.py komentarz), dok.13  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Dok.03 §5 opisuje `main.py` jako „App factory, CORS, middleware, health check", ale **żaden dokument nie specyfikuje konfiguracji CORS**: dozwolone origins, metody, nagłówki. Dla systemu single-tenant działającego lokalnie brak CORS byłby bezpieczny, ale brak dokumentacji oznacza ryzyko że implementator ustawi `allow_origins=["*"]` co w połączeniu z API key w nagłówku może umożliwić ataki CSRF z przeglądarki.  
**Wpływ:** Jeśli API jest dostępne z przeglądarki (np. przyszły frontend), `allow_origins=["*"]` z `allow_headers=["*"]` umożliwia każdej stronie wykonanie requestów z X-API-Key jeśli klucz wycieknie do frontendu.  
**Naprawa:** Dodać do dok.13 §1:

```python
# workshop/api/main.py — konfiguracja CORS
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    # Single-tenant v1: tylko localhost (dev) lub konkretna domena (prod)
    allow_origins=settings.cors_allowed_origins,  # domyślnie: ["http://localhost:3000"]
    allow_credentials=False,        # NIE allow_credentials=True — nie używamy cookies
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["X-API-Key", "Content-Type"],
)
# .env: CORS_ALLOWED_ORIGINS=http://localhost:3000,https://workshop.example.com
```

---

#### O-03: SSRF — webhook target_url bez walidacji wewnętrznych adresów
**Plik:** dok.04 §2.14, dok.05 §8  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** `POST /projects/{id}/webhooks` przyjmuje `target_url` (dok.05 §8) bez walidacji czy nie wskazuje na wewnętrzną infrastrukturę. Atakujący z ważnym kluczem API może ustawić `target_url=http://db:5432/`, `http://169.254.169.254/latest/meta-data/` (AWS IMDS), `http://localhost:8000/internal` — system wyśle HTTP POST na ten adres przy każdym zdarzeniu mapping.done.  
**Wpływ:** Odczyt metadanych AWS/GCP (kradzież credentials); probing wewnętrznej sieci Docker; potencjalny SSRF do usług nieeksponowanych na zewnątrz.  
**Naprawa:** Dodać do dok.05 §8 walidację `target_url` przy zapisie:

```python
import ipaddress, socket
from urllib.parse import urlparse

BLOCKED_RANGES = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("169.254.0.0/16"),  # link-local / AWS IMDS
    ipaddress.ip_network("127.0.0.0/8"),
]

def validate_webhook_url(url: str) -> None:
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError("Tylko HTTP/HTTPS dozwolone")
    host = parsed.hostname
    try:
        ip = ipaddress.ip_address(socket.gethostbyname(host))
        if any(ip in net for net in BLOCKED_RANGES):
            raise ValueError(f"Adres wewnętrzny niedozwolony: {ip}")
    except socket.gaierror:
        raise ValueError(f"Nie można rozwiązać hosta: {host}")
```

---

#### O-04: SSRF — ingestion URL (source_type="url") bez walidacji
**Plik:** dok.05 §2.1, dok.06 `/ingestion/spec`  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** `POST /ingestion/spec` z `source_type="url"` pobiera dokument z podanego URL i przekazuje jego treść do LLM. Brak walidacji że URL nie wskazuje na wewnętrzne zasoby. W odróżnieniu od webhooków (gdzie serwer wysyła POST), tutaj serwer wykonuje GET i **odpowiedź jest czytana i przetwarzana** — co oznacza że wewnętrzne dane (np. `http://db:5432/`, `http://app:8000/health`) mogą trafić do LLM i być logowane w `llm_calls_log`.  
**Wpływ:** Exfiltration wewnętrznych danych przez LLM logs; dostęp do niezabezpieczonych serwisów wewnętrznych; w przypadku Ollama (`http://ollama:11434`) atakujący może sterować modelem LLM.  
**Naprawa:** Zastosować tę samą funkcję `validate_webhook_url()` z O-03 przed wykonaniem HTTP GET na podanym URL. Dodać do prekondycji w dok.05 §2.1: „URL nie może wskazywać na adresy RFC 1918, link-local, loopback."

---

#### O-05: Brak BOLA — brak weryfikacji własności zasobu między projektami
**Plik:** dok.05 §2.2, dok.06 paths  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** Endpointy takie jak `GET /brief/{brief_id}/mapping`, `GET /reports/{report_id}`, `GET /planning/{plan_id}/packages` przyjmują UUID zasobu **bez weryfikacji czy zasób należy do projektu aktualnie uwierzytelnionego klienta**. Wszystkie klucze API w `WORKSHOP_API_KEYS` mają identyczne uprawnienia (brak ról/projektów per klucz). Agent projektu A z ważnym kluczem może odczytać mapowanie projektu B jeśli zgadnie lub zna UUID.  
**Wpływ:** Naruszenie OWASP API Security Top 10 — A1: BOLA (Broken Object Level Authorization). Wyciек danych klientów między projektami.  
**Naprawa:** Dodać do dok.13 §2 koncepcję klucza per projekt:

```python
# Opcja 1 (v1 quickfix): klucz API zawiera project_id w prefiksie
# WORKSHOP_API_KEYS=proj_<project_uuid>_<random_secret>
# Walidacja: extract project_id z klucza → sprawdź w requeście

# Opcja 2 (właściwa): row-level check w każdym endpoincie:
async def verify_brief_ownership(brief_id: UUID, db: AsyncSession) -> Brief:
    brief = await db.get(Brief, brief_id)
    if not brief:
        raise HTTPException(404)
    # Jeśli mamy project_id z klucza API:
    if api_key_project_id and brief.project_id != api_key_project_id:
        raise HTTPException(403, "Brak dostępu do zasobu innego projektu")
    return brief
```

---

#### O-06: Niespójność confidence_threshold — 0.6 w OpenAPI vs 0.4 w kontraktach i .env
**Plik:** dok.06 `MapRequest`, dok.05 §2.2, dok.13 §3 `.env.example`  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Niespójność wartości domyślnej `confidence_threshold` między dokumentami (niezwiązana z naprawą z poprzednich rund która dotyczyła innego miejsca):
- `dok.06` `MapRequest.confidence_threshold`: `default: 0.6`
- `dok.05` §2.2 `MapRequest`: `confidence_threshold: float = 0.4`
- `dok.13` `.env.example`: `CONFIDENCE_THRESHOLD_DEFAULT=0.4`
- `dok.06` `EstimateRequest.confidence_threshold`: `default: 0.6`

Implementacja użyje wartości z kodu (0.4 lub 0.6?), a OpenAPI Swagger UI pokaże 0.6 jako default — co wprowadzi w błąd użytkowników API.  
**Wpływ:** AI agent korzystający ze Swagger UI ustawi threshold 0.6 zamiast 0.4 → mniej szablonów w wynikach mapowania → gorsze raporty.  
**Naprawa:** Ujednolicić we wszystkich miejscach na `0.4` (zgodnie z naprawą z poprzednich rund). W `dok.06` poprawić:

```yaml
MapRequest:
  properties:
    confidence_threshold:
      type: number
      format: float
      default: 0.4      # ← było: 0.6
      minimum: 0.0
      maximum: 1.0

EstimateRequest:
  properties:
    confidence_threshold:
      type: number
      format: float
      default: 0.4      # ← było: 0.6
```

---

#### O-07: Błąd struktury YAML — WorkPackage schema jest pusta, właściwości wewnątrz WebhookSubscription
**Plik:** dok.06 linie 343–398  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:** W `components/schemas` definicja `WorkPackage:` (linia 343) jest **pustym obiektem** zakończonym natychmiast przez `WebhookSubscriptionCreate:`. Faktyczne właściwości WorkPackage (`required: [id, plan_id, doc_uid, ...]`, `properties: id, plan_id, doc_uid...`) zostały przez błąd wcięcia YAML umieszczone **wewnątrz** `WebhookSubscription.allOf` jako dodatkowy element (`type: object` na linii 375). Oznacza to że `WebhookSubscription` schema zawiera właściwości pracy (sequence_order, inputs_json, gates_json, assignee_type) zamiast danych webhooka — i jest walidowany błędnie.  
**Wpływ:** Walidatory OpenAPI (Swagger, Redoc, Postman) generują błędne schematy dla obu typów. Wygenerowany kod klienta (np. z openapi-generator) będzie błędny dla WorkPackage i WebhookSubscription.  
**Naprawa:** W `dok.06` oddzielić definicje:

```yaml
    WorkPackage:
      type: object
      required: [id, plan_id, doc_uid, doc_title, phase_id, sequence_order, status]
      properties:
        id:             { $ref: '#/components/schemas/UUID' }
        plan_id:        { $ref: '#/components/schemas/UUID' }
        doc_uid:        { type: string }
        doc_title:      { type: string }
        phase_id:       { type: integer }
        phase_name:     { type: string }
        sequence_order: { type: integer }
        inputs_json:    { type: array, items: { type: string } }
        outputs_json:   { type: array, items: { type: string } }
        gates_json:     { type: array, items: { type: string } }
        assignee_type:
          type: string
          enum: [ai_agent_writer, ai_agent_reviewer, human]
          nullable: true
        h_estimate:  { type: number, format: float, nullable: true }
        status:
          type: string
          enum: [pending, in_progress, done, blocked]
        depends_on:  { type: array, items: { $ref: '#/components/schemas/UUID' } }
        created_at:  { type: string, format: date-time }
        updated_at:  { type: string, format: date-time }

    WebhookSubscriptionCreate:
      type: object
      required: [target_url, events]
      properties:
        target_url: { type: string, format: uri }
        events:
          type: array
          items:
            type: string
            enum: [mapping.done, mapping.failed, report.ready, report.accepted, plan.ready, ingestion.review]
        secret: { type: string, nullable: true }

    WebhookSubscription:
      allOf:
        - $ref: '#/components/schemas/WebhookSubscriptionCreate'
        - type: object
          required: [id, project_id, is_active, created_at]
          properties:
            id:         { $ref: '#/components/schemas/UUID' }
            project_id: { $ref: '#/components/schemas/UUID' }
            is_active:  { type: boolean }
            created_at: { type: string, format: date-time }
```

---

#### O-08: Brak limitu rozmiaru JSON body — tylko pliki mają limit
**Plik:** dok.13 §5, dok.06 paths  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Dok.13 §5 definiuje walidację rozmiaru tylko dla file uploads (`MAX_BRIEF_FILE_SIZE_MB`, `MAX_INGESTION_FILE_SIZE_MB`). Endpointy przyjmujące JSON body (`POST /projects`, `PATCH /projects/{id}`, `POST /brief/{id}/map` z MapRequest, `POST /reports/estimate/{brief_id}`) **nie mają limitu rozmiaru**. Atakujący może wysłać request z 100 MB JSON body do `POST /projects/import` lub `POST /ingestion/spec` z `content` będącym 50 MB tekstem.  
**Wpływ:** OOM (Out of Memory) w kontenerze FastAPI przy deserializacji gigantycznego JSON; DoS przez wyczerpanie pamięci RAM.  
**Naprawa:** Dodać do dok.13 §5 konfigurację Starlette:

```python
# workshop/api/main.py
from starlette.middleware.trustedhost import TrustedHostMiddleware

# Starlette nie ma wbudowanego MAX_BODY_SIZE, użyj middleware:
class MaxBodySizeMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_body_size: int = 10 * 1024 * 1024):  # 10 MB default
        super().__init__(app)
        self.max_body_size = max_body_size

    async def dispatch(self, request: Request, call_next):
        content_length = request.headers.get("content-length")
        if content_length and int(content_length) > self.max_body_size:
            return Response("Payload Too Large", status_code=413)
        return await call_next(request)

# Wyjątek: /brief/upload i /ingestion/spec mają własne (wyższe) limity z §5
# JSON endpoints: 10 MB; /projects/import: 200 MB (dok.05 §9)
```

---

#### O-09: Excessive Data Exposure — export projektu domyślnie zawiera raw_content briefów
**Plik:** dok.05 §9, dok.06 `/projects/{project_id}/export`  
**Priorytet:** 🟡 WAŻNE  
**Problem:** Dok.05 §9 definiuje `GET /projects/{id}/export` z parametrem `?exclude_raw_content=true` domyślnie `false`. Oznacza to że **domyślny eksport zawiera pełne binarne dane briefów** (PDFy, DOCXy klientów) przechowywane jako `BYTEA` w tabeli `briefs`. Pliki mogą zawierać PII, dane finansowe, poufne informacje strategiczne. Parametr `exclude_raw_content` nie jest widoczny w OpenAPI spec (dok.06) który definiuje endpoint `/projects/{project_id}/export` bez żadnych parametrów query.  
**Wpływ:** Przypadkowy eksport projektu (np. przez AI agenta) wycieka wrażliwe dokumenty klientów; naruszenie RODO (dane osobowe w briefach); brak zgodności z polityką minimalizacji danych.  
**Naprawa:**
1. Zmienić domyślną wartość: `exclude_raw_content=true` (opt-in do eksportu danych surowych)
2. Dodać parametr do OpenAPI spec w dok.06:

```yaml
/projects/{project_id}/export:
  get:
    parameters:
      - name: project_id
        in: path
        required: true
        schema: { type: string, format: uuid }
      - name: exclude_raw_content
        in: query
        schema:
          type: boolean
          default: true    # ← zmiana z false na true (privacy-by-default)
        description: >
          Wyklucz surowe pliki briefów (raw_content) z eksportu.
          Domyślnie true — eksport zawiera tylko metadane i przetworzone wyniki.
          Ustaw false aby dołączyć oryginalne pliki (wymaga osobnego potwierdzenia).
```

---

## Podsumowanie znalezisk

| ID | Obszar | Priorytet | Krótki opis |
|----|--------|-----------|-------------|
| M-01 | CI/CD | 🔴 | Brak zawartości docker-compose.yml (healthcheck, depends_on, volumes) |
| M-02 | CI/CD | 🔴 | Brak rollback strategy dla migracji Alembic |
| M-03 | CI/CD | 🟡 | Brak specyfikacji kiedy uruchamiane są migracje w CI i brak DDL usera |
| M-04 | CI/CD | 🟡 | Secrets wyłącznie przez .env — brak Docker secrets / Vault dla prod |
| M-05 | CI/CD | 🟡 | Brak quick start guide krok po kroku |
| N-01 | Monitoring | 🔴 | Tylko plain-text logging, brak structured JSON |
| N-02 | Monitoring | 🔴 | Brak Correlation ID / X-Request-ID propagacji |
| N-03 | Monitoring | 🟡 | Brak endpointu /metrics (Prometheus) |
| N-04 | Monitoring | 🟡 | /health nie sprawdza statusu LLM provider |
| N-05 | Monitoring | 🟡 | Brak distributed tracing (OpenTelemetry) |
| N-06 | Monitoring | 🟢 | Brak progów SLO i alertów dla kluczowych metryk |
| O-01 | Security | 🔴 | Brak globalnego rate limiting API (tylko LLM semaphore) |
| O-02 | Security | 🟡 | Brak specyfikacji CORS konfiguracji |
| O-03 | Security | 🔴 | SSRF — webhook target_url bez walidacji adresów wewnętrznych |
| O-04 | Security | 🔴 | SSRF — ingestion URL bez walidacji adresów wewnętrznych |
| O-05 | Security | 🔴 | Brak BOLA — brak weryfikacji własności zasobu między projektami |
| O-06 | Security | 🟡 | Niespójność confidence_threshold: 0.6 w OpenAPI vs 0.4 w kontraktach |
| O-07 | Security | 🔴 | WorkPackage schema pusta w OpenAPI YAML (błąd struktury YAML) |
| O-08 | Security | 🟡 | Brak limitu rozmiaru JSON body (tylko file uploads mają limit) |
| O-09 | Security | 🟡 | Export domyślnie zawiera raw_content briefów (naruszenie privacy-by-default) |

**Łącznie: 20 znalezisk** (5× M, 6× N, 9× O)  
**Krytyczne 🔴: 9** | **Ważne 🟡: 9** | **Drobne 🟢: 2**

---

# Analiza Runda 4 — Część B: Obszary P, Q, R

**Data:** 2025-07-15  
**Analityk:** Copilot Senior Engineer  
**Pliki źródłowe:** dok.04, dok.05, dok.08, dok.09, dok.10, dok.11, dok.14  
**Kontekst:** Nowe problemy (nie naprawione w rundach 1–3)

---

## Legenda priorytetów

| Symbol | Znaczenie |
|--------|-----------|
| 🔴 KRYTYCZNE | Błąd powodujący utratę danych, race condition lub crash w produkcji |
| 🟡 WAŻNE | Błąd logiczny lub luka w specyfikacji z realnym wpływem na działanie |
| 🟢 DROBNE | Niejednoznaczność, dług techniczny, potencjalny problem w edge case |

---

## OBSZAR P — Operacje asynchroniczne (P-01…P-07)

---

#### P-01: asyncio.create_task nie przeżywa restartu workera w środowisku multi-process

**Plik:** dok.05 §2.2 (Side 2 — Brief Mapper, tryb asynchroniczny)  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:**  
Spec definiuje `asyncio.create_task + in-memory registry dla v1` jako mechanizm obsługi długich mapowań. Przy uruchomieniu `gunicorn -w 4` (4 procesy) lub `uvicorn --workers 4` każdy worker ma odrębną pętlę event loop i odrębną pamięć. Task uruchomiony w workerze A jest niewidoczny dla workera B. Gdy worker A zostanie zrestartowany (OOM, SIGTERM, crash LLM socket), task przepada bez oznaczenia `mapping_results.status='failed'`. Klient polluje `GET /brief/{id}/mapping` w nieskończoność i nigdy nie dostanie finalnego statusu.

**Wpływ:**  
- Zombie rekordy `mapping_results` ze statusem `'running'` blokują retry (spec wymaga HTTP 409 jeśli istnieje `status='running'` dla tego `brief_id`).  
- Klient nie może ponowić mapowania bez ręcznej interwencji w DB.  
- In-memory registry jest czyszczony przy każdym restarcie procesu, więc status jest permanentnie utracony.

**Naprawa:**  
Dodać do spec. zasadę: `asyncio.create_task` jest dozwolone **wyłącznie** w środowisku single-worker (`uvicorn --workers 1`). Dla multi-worker (produkcja) wymagany jest zewnętrzny broker zadań (Celery + Redis lub RQ). Dodać sekcję w dok.05 §2.2 z decyzją architektoniczną:
```
v1 (MVP, single worker):   asyncio.create_task
v2 (produkcja, >1 worker): Celery task z brokerem Redis
```
Dodać mechanizm startup recovery analogiczny do webhook (dok.04 §2.14):
```sql
UPDATE mapping_results SET status='failed', error='worker_crash'
WHERE status='running'
  AND created_at < now() - interval '10 minutes';
```

---

#### P-02: Brak globalnego timeoutu dla pipeline wielochunkowego LLM

**Plik:** dok.05 §3.1, dok.09 §2  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
Kontrakt `BaseLLMAdapter.extract_entities()` definiuje `LLMTimeoutError` po >30s per wywołanie. Ale dla briefu z wieloma chunkami (dok.09 §2) każdy chunk jest przetwarzany osobno sekwencyjnie: 5 chunków × 30s timeout = 150s całkowitego czasu. Nie ma specyfikacji maksymalnego czasu całego pipeline'u mapowania. Dla dużego briefu (50 stron, 10 chunków) + LLM Reranking (kolejne wywołanie) operacja może trwać >5 minut bez żadnego sygnału postępu dla klienta (poza `status: "running"`).

**Wpływ:**  
- Gunicorn domyślnie ubija workera po 30s (worker timeout). Długi pipeline zostanie przerwany w połowie przetwarzania.  
- Klient widzi `status: "running"` do osiągnięcia gunicorn timeout, potem zasób znika.  
- Brak `progress_percent` per chunk w polling response.

**Naprawa:**  
Dodać do spec. pole `MAX_MAPPING_PIPELINE_TIMEOUT_S=120` (konfigurowalne). Polling endpoint `GET /brief/{id}/mapping` powinien zwracać granularny postęp:
```json
{"status": "running", "progress_percent": 40, "chunks_done": 2, "chunks_total": 5}
```
Gunicorn worker timeout w `.env` musi być ustawiony na >120s: `GUNICORN_TIMEOUT=180`.

---

#### P-03: Brak specyfikacji granicy zastosowania asyncio vs. Celery

**Plik:** dok.05 §2.2, dok.04 §6 (retencja llm_calls_log)  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
Spec wymienia `asyncio.create_task` (mapowanie briefów) i wspomina `Celery beat task` (retencja llm_calls_log, dok.04 §6) w tym samym systemie, bez zdefiniowania jasnej granicy: *kiedy task w tle = asyncio, kiedy = Celery?* Deweloper implementujący system nie wie, czy retencja logów LLM powinna być w Celery beat czy FastAPI `lifespan`.

**Wpływ:**  
- Ryzyko implementacji retencji w `asyncio.create_task` (nie przeżyje restartu) lub w Celery (wymaga dodatkowej infrastruktury Redis niezmienionej w spec).  
- Brak Celery w `requirements.txt` / `pyproject.toml` – deweloper może nie wiedzieć, że jest wymagany.

**Naprawa:**  
Dodać sekcję architektoniczną w dok.03 lub dok.05 z tabelą decyzyjną:
```
Typ zadania              | Mechanizm         | Uzasadnienie
-------------------------|-------------------|-----------------------------
Mapowanie briefu (async) | asyncio.create_task (v1) / Celery (v2) | blokuje HTTP
Retencja llm_calls_log   | Celery beat (cron)| nie jest czas-krytyczne
Wysyłanie webhooków      | asyncio / Celery  | retry logic wymagany
```

---

#### P-04: Brak idempotency dla `POST /brief/upload` — duplikaty przy ponownym wgraniu

**Plik:** dok.04 §2.2, dok.05 §2.2  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
Tabela `briefs` (dok.04 §2.2) nie zawiera pola `content_hash` (w odróżnieniu od `mapping_results`). Brak UNIQUE constraint na `(project_id, content_hash)`. Wgranie tego samego pliku dwa razy tworzy dwa rekordy `briefs` z identyczną treścią. Kontrakt `POST /brief/upload` (dok.05 §2.2) nie definiuje zachowania idempotentnego.

**Wpływ:**  
- Klient ponownie wgrywający brief (np. po błędzie sieciowym) tworzy duplikat w DB.  
- Obie wersje briefa mogą zostać zmapowane osobno, generując dwa `estimation_reports` dla tego samego projektu.  
- Koszt LLM podwojony bez ostrzeżenia.

**Naprawa:**  
Dodać pole `content_hash TEXT` do `briefs` (migracja 0009):
```sql
ALTER TABLE briefs ADD COLUMN content_hash TEXT;
CREATE UNIQUE INDEX idx_briefs_project_hash
  ON briefs(project_id, content_hash) WHERE parse_status != 'failed';
```
W kontrakcie `POST /brief/upload` dodać: *"jeśli brief o tym samym content_hash istnieje w projekcie → zwróć HTTP 200 z istniejącym rekordem + nagłówek `X-Existing-Brief: true`"*.

---

#### P-05: Niespójność mechanizmów powiadamiania o statusie mapowania

**Plik:** dok.05 §2.2, dok.04 §2.14  
**Priorytet:** 🟢 DROBNE  
**Problem:**  
Spec definiuje **trzy** równoległe mechanizmy powiadamiania o zakończeniu mapowania:
1. **Polling** — `GET /brief/{id}/mapping` (dok.05 §2.2)  
2. **Webhook** — event `mapping.done` (dok.04 §2.14)  
3. **Retry-After header** — w odpowiedzi 202 (dok.05 §2.2)

Brak specyfikacji: czy webhook i polling są wzajemnie wykluczające się? Czy webhook może być ustawiony bez skonfigurowanego polling endpointu? Czy `Retry-After: 10` jest liniowy czy eksponencjalny?

**Wpływ:**  
- Klient implementujący obie metody jednocześnie może zduplikować processing po stronie klienta.  
- Brak spójności w zachowaniu gdy webhook delivery fail → klient musi fallbackować do pollingu, ale nie ma o tym informacji w specyfikacji.

**Naprawa:**  
Dodać sekcję "Powiadamianie klientów" w dok.05 §2.2 z jasną hierarchią: *webhook (preferowany) → polling (fallback)*. Określić `Retry-After` strategy (np. `min(10 * attempt, 60)` sekundy).

---

#### P-06: Status "partial" przy LLM timeout — niezdefiniowany próg akceptacji

**Plik:** dok.05 §2.2 (Tryb asynchroniczny, Status "partial")  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
Spec definiuje: *"Jeśli LLM timeout nastąpi w trakcie → status='done' + metadata.processing_notes={'partial_llm_timeout': true}"*. Ale nie określa:
- Ile chunków musi być przetworzonych, żeby uznać wynik za "partial done" zamiast "failed"?
- Co jeśli timeout nastąpi na **pierwszym** chunku (0 entities extracted)? Wtedy `extracted_entities` jest pusty i `MappingResult` z `total_items=0` będzie oznaczone jako `status='done'` — co jest mylące.
- Czy `avg_confidence=0.0` + `total_items=0` + `status='done'` powinno wyzwalać webhook `mapping.done`?

**Wpływ:**  
- Klient dostaje `status='done'` z `total_items=0` i nie wie czy to brak dopasowań czy niekompletne przetwarzanie.  
- EstimationEngine próbuje wyliczyć kosztorys → `InsufficientMappingError` zamiast oczekiwanego wyniku.

**Naprawa:**  
Dodać regułę: *"partial_llm_timeout → status='done' TYLKO gdy co najmniej 1 chunk został przetworzony pomyślnie. W przeciwnym razie status='failed'."* Dodać pole `chunks_processed: int` do `MappingResult.metadata`.

---

#### P-07: `asyncio.get_event_loop()` deprecated w Python 3.10+

**Plik:** dok.08 §9 (BriefParser w async context)  
**Priorytet:** 🟢 DROBNE  
**Problem:**  
Spec zawiera:
```python
parsed_brief = await asyncio.get_event_loop().run_in_executor(
    None, parser.parse, content, detected_format
)
```
`asyncio.get_event_loop()` jest deprecated od Python 3.10 i w kontekście async coroutine emituje `DeprecationWarning` (Python 3.10+) lub rzuca `RuntimeError` w Python 3.12+, gdy nie ma aktywnej pętli.

**Wpływ:**  
- Crash na Python 3.12+ podczas parsowania PDF/DOCX.  
- DeprecationWarning zaśmiecający logi w Python 3.10–3.11.

**Naprawa:**  
Zastąpić przez:
```python
parsed_brief = await asyncio.get_running_loop().run_in_executor(
    None, parser.parse, content, detected_format
)
```

---

## OBSZAR Q — Edge cases logiki biznesowej (Q-01…Q-09)

---

#### Q-01: `find_by_keyword(keywords=[], ...)` — nieokreślone zachowanie dla pustej listy

**Plik:** dok.09 §3 (ŚCIEŻKA B: Keyword fallback)  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
Gdy LLM zwróci `ExtractedEntities` z pustą listą `keywords=[]` (co jest możliwe — kontrakt postconditions w dok.05 §3.1 gwarantuje tylko "co najmniej jedno niepuste pole", nie keywords), ŚCIEŻKA B wywołuje:
```python
fallback_docs = await connector.find_by_keyword(keywords=[], limit=150)
```
Kontrakt `find_by_keyword` (dok.12) nie specyfikuje zachowania dla pustej listy keywords. Implementacja oparta na `LIKE '%keyword%'` zapytaniu dla pustej listy może: (a) nie zwrócić nic, (b) zwrócić wszystkie dokumenty, (c) rzucić błąd SQL.

**Wpływ:**  
- Jeśli (b): `SemanticMapper` dostaje 150 losowych dokumentów bez semantic relevance — fałszywe mapowanie.  
- Jeśli (c): cały pipeline mapowania kończy się błędem.  
- ŚCIEŻKA C (phase fallback) może nie aktywować się gdy `entities.phases=[]` też jest puste.

**Naprawa:**  
Dodać guard w `_query_itdoc`:
```python
if entities.keywords:
    fallback_docs = await connector.find_by_keyword(keywords=entities.keywords[:30], limit=150)
else:
    fallback_docs = []  # Nie wywołuj find_by_keyword z pustą listą
```
Zaktualizować postconditions kontraktu w dok.12 dla `find_by_keyword(keywords=[])`.

---

#### Q-02: LLM zwraca Markdown zamiast JSON — brak specyfikacji parsowania odpowiedzi

**Plik:** dok.05 §3.1 (BaseLLMAdapter.extract_entities), dok.09 §2  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:**  
Modele GPT-4o i Claude często owijają odpowiedź JSON w blok Markdown:
```
```json
{"domains": ["fintech"], ...}
```
```
Kontrakt `BaseLLMAdapter` nie specyfikuje jak parsować odpowiedź LLM — zakłada że odpowiedź jest czystym JSON. Brak specyfikacji: czy adapter próbuje strip Markdown fence? Czy retryuje z innymi instrukcjami w prompcie? Czy rzuca `LLMProviderError`?

**Wpływ:**  
- `json.loads(response)` rzuca `JSONDecodeError` → `LLMProviderError` → status mapowania `'failed'`.  
- Błąd jest nie-deterministyczny: ten sam prompt może raz zwrócić czysty JSON, raz Markdown (zależnie od temperatury modelu).  
- Wyprodukowanie `JSONDecodeError` jako `LLMProviderError` maskuje prawdziwy problem (parser, nie sieć).

**Naprawa:**  
Dodać do specyfikacji `BaseLLMAdapter` sekcję "Response Parsing Strategy":
```python
def _parse_llm_json(response: str) -> dict:
    # 1. Spróbuj bezpośrednio json.loads()
    # 2. Jeśli błąd: wyciągnij blok ```json...``` (regex)
    # 3. Jeśli błąd: spróbuj naprawić common JSON issues (trailing comma, single quotes)
    # 4. Jeśli błąd: rzuć LLMParseError (nowy wyjątek odróżniony od LLMProviderError)
```
Dodać `LLMParseError` do hierachii wyjątków w dok.05 §3.1.

---

#### Q-03: `mapping_results=[]` — `InsufficientMappingError` nie ma zdefiniowanej obsługi HTTP

**Plik:** dok.10 §6 (EstimationEngine.calculate), dok.05 §2.3  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
`EstimationEngine.calculate()` rzuca `InsufficientMappingError` gdy `items=[]`. Kontrakt `POST /reports/estimate/{brief_id}` (dok.05 §2.3) definiuje:
```
422 Unprocessable — brak mapowań z confidence ≥ threshold
```
Ale `InsufficientMappingError` może być wywołany z dwóch różnych powodów:
1. `mapping.items=[]` bo threshold za wysoki → 422 (użytkownik powinien obniżyć threshold)
2. `mapping.items=[]` bo `mapping.total_items=0` (brak jakichkolwiek wyników) → powinno być inna treść błędu

Brak rozróżnienia w specyfikacji błędu. Obie sytuacje zwrócą identyczne HTTP 422 z różnymi przyczynami.

**Wpływ:**  
- Klient dostaje 422 i nie wie: obniżyć threshold czy rerunować mapowanie?  
- `InsufficientMappingError` nie jest zdefiniowany w hierarchii wyjątków (dok.05 §3.1 definiuje tylko `LLMTimeoutError`, `LLMRateLimitError`, `LLMProviderError`).

**Naprawa:**  
Dodać do kontraktu 422 response body:
```json
{"error": "insufficient_mapping", "reason": "threshold_too_high|no_mapping_results",
 "current_threshold": 0.6, "available_items": 3, "suggestion": "Obniż próg do 0.3"}
```

---

#### Q-04: Race condition w `POST /brief/{id}/map` — TOCTOU na `status='running'`

**Plik:** dok.05 §2.2 (Preconditions, conflict detection)  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:**  
Spec definiuje deduplication przez:
```sql
SELECT id FROM mapping_results WHERE brief_id=? AND status='running' LIMIT 1
```
Jest to klasyczny TOCTOU (Time Of Check to Time Of Use) race condition. Dwa równoczesne requesty `POST /brief/{id}/map`:
1. Worker A: SELECT → brak running → INSERT status='running'
2. Worker B: SELECT → brak running (A jeszcze nie skończył INSERT) → INSERT status='running'

Wynik: dwa rekordy `mapping_results` ze statusem `'running'` dla tego samego `brief_id`. Dwa równoległe wywołania LLM, dwa duplikaty wyników.

**Wpływ:**  
- Zduplikowane koszty LLM.  
- Wyścig aktualizacji status='done' — jeden rekord wygrywa, drugi pozostaje 'running' (zombie).  
- Polling może zwrócić inny rekord niż ten który widział klient w odpowiedzi 202.

**Naprawa:**  
Zastąpić SELECT+INSERT przez atomową operację z advisory lock lub INSERT+conflict:
```sql
INSERT INTO mapping_results (brief_id, status, ...)
VALUES (?, 'running', ...)
ON CONFLICT DO NOTHING
RETURNING id;
-- Jeśli zwraca NULL → 409 (inny INSERT wygrał)
```
Lub użyć PostgreSQL advisory lock:
```sql
SELECT pg_try_advisory_xact_lock(hashtext(?::text))
-- Jeśli false → 409
```

---

#### Q-05: Cykl w grafie zależności WorkPlanner — cichy błąd bez logowania

**Plik:** dok.11 §3.2 (Topologiczne sortowanie)  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
`_topological_sort()` obsługuje cykle przez: *"Obsługa cykli: pozostałe nieprzetworzone docs dodaj na koniec (wg fazy)"*. To podejście:
1. Nie loguje faktu wykrycia cyklu
2. Nie zwraca informacji o cyklu w odpowiedzi API
3. Produkuje plan z arbitralną kolejnością dla dokumentów w cyklu

Komentarz w kodzie sam potwierdza: *"rhythm_edges mogą mieć cykle"* — jest to więc realne zagrożenie.

**Wpływ:**  
- `WorkPlan` z błędną kolejnością dokumentów (cykliczne zależności → dokument X zależy od Y, Y zależy od X → jeden z nich zostanie wstawiony jako "pending" bez zrealizowanej zależności).  
- Klient/AI-agent dostaje plan, który nie może być wykonany sekwencyjnie.  
- Brak alertu dla administratora systemu.

**Naprawa:**  
Dodać detekcję i raportowanie cyklu:
```python
cycles_detected = [uid for uid in doc_uids if uid not in result]
if cycles_detected:
    logger.warning(f"Cycle detected in dependency graph: {cycles_detected}")
# W WorkPlan.metadata:
plan_metadata = {"cycles_detected": cycles_detected, "cycle_resolution": "phase_order_fallback"}
```
Zwracać `cycles_detected` w `WorkPlan` response body.

---

#### Q-06: `_parse_text` — silent corruption dla Windows-1252 i GBK

**Plik:** dok.08 §3 (Etap 2: Ekstrakcja tekstu, TXT/MD)  
**Priorytet:** 🟢 DROBNE  
**Problem:**  
Spec definiuje fallback encoding chain: `utf-8 → utf-8-sig → latin-1`. Kodowanie `latin-1` (ISO-8859-1) **nigdy nie rzuca** `UnicodeDecodeError` — dekoduje każdy bajt 0x00–0xFF do odpowiadającego mu znaku Unicode. To oznacza, że plik w Windows-1252 (popularne w Polsce), Shift-JIS lub GBK zostanie "zdekodowany" przez latin-1 z błędnymi znakami (np. Windows-1252 `\x9c` → latin-1 `ś` zamiast `œ`) bez żadnego ostrzeżenia.

**Wpływ:**  
- Brief z polskim tekstem w Windows-1252 będzie sparsowany ze zniekształconymi znakami.  
- LLM będzie przetwarzał zmojibakowany tekst, co obniża jakość ekstrakcji encji.  
- Brak ostrzeżenia w `briefs.metadata` o potencjalnym problemie z kodowaniem.

**Naprawa:**  
Zastąpić latin-1 przez `chardet`/`charset-normalizer`:
```python
import chardet
detected = chardet.detect(content)
if detected["confidence"] > 0.7:
    try:
        text = content.decode(detected["encoding"])
        metadata["encoding"] = detected["encoding"]
    except UnicodeDecodeError:
        pass  # fallback
# Ostatni fallback (z ostrzeżeniem):
text = content.decode("latin-1", errors="replace")
metadata["encoding_warning"] = "forced_latin1"
```

---

#### Q-07: EstimationReport nieaktualny po `force_rerun` — brak mechanizmu "stale report"

**Plik:** dok.05 §2.2, §2.3; dok.04 §2.5  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
Sekwencja krytyczna:
1. `POST /brief/{id}/map` → MappingResult A (87 docs)
2. `POST /reports/estimate/{brief_id}` → EstimationReport X (87 docs, zaakceptowany)
3. `POST /brief/{id}/map` z `force_rerun=True` → MappingResult B (55 docs — LLM zwrócił mniej)
4. `POST /planning/create/{X.id}` — plan oparty na zaakceptowanym X

Spec (dok.05 §2.3) używa "najnowsze mapowanie z status='done'" do generowania raportu, ale zaakceptowany raport X nadal wskazuje na MappingResult A. Tworzy się plan z 87 dokumentami, ale aktualne mapowanie wskazuje 55 — niespójność.

**Wpływ:**  
- WorkPlan zawiera dokumenty których nie ma w aktualnym mapowaniu.  
- Klient nie jest powiadamiany że zaakceptowany raport jest nieaktualny.

**Naprawa:**  
Dodać w spec. regułę: *"force_rerun po akceptacji raportu → automatycznie ustawia raport status='rejected' z powodem 'superseded_by_new_mapping'"*. Dodać pole `superseded_by_mapping_id` do `estimation_reports`.

---

#### Q-08: `_infer_doc_type` — klucz "test" nie istnieje w `DOCUMENT_TYPE_POINTS`

**Plik:** dok.10 §2.5 (`_infer_doc_type`)  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
Implementacja szuka kluczy `["audit", "specification", "architecture", "test", "report", "plan", "policy"]` w tytule dokumentu. Klucz `"test"` **nie istnieje** w `DOCUMENT_TYPE_POINTS` (dok.10 §2.1) — są tam `"test_plan"` i `"test_report"`. Dla tytułu "Test Cases Register":
```python
if "test" in title_lower:
    return "test"  # ← nie ma w DOCUMENT_TYPE_POINTS!
```
`DOCUMENT_TYPE_POINTS.get("test", DOCUMENT_TYPE_POINTS["default"])` zwróci `3.0` (default) zamiast `4.0` (test_plan) lub `3.0` (test_report).

**Wpływ:**  
- Dla "Plan testów akceptacyjnych": zwróci "plan" (5.0 pkt × H_PER_POINT) zamiast "test_plan" (4.0 pkt) — **przeszacowanie o 25%**.  
- Dla "Raport z testów": zwróci "report" — brak w DOCUMENT_TYPE_POINTS — fallback do "default" (3.0 pkt, taki sam wynik, ale z innego klucza).  
- Niespójność między `DOCUMENT_TYPE_POINTS` a priorytetową listą kluczy w `_infer_doc_type`.

**Naprawa:**  
Zsynchronizować listy:
```python
PRIORITY_KEYS = ["risk_assessment", "audit", "compliance", "architecture",
                 "test_plan", "test_report", "specification", "design",
                 "strategy", "roadmap", "requirements", "policy",
                 "procedure", "runbook", "checklist", "report", "plan", "log"]
```
Klucze składane (`test_plan`) sprawdzać jako pierwsze (specificity-first).

---

#### Q-09: `ASSIGNEE_RULES` — brak wzorca dla dokumentów "security"

**Plik:** dok.11 §3.4 (`ASSIGNEE_RULES`)  
**Priorytet:** 🟢 DROBNE  
**Problem:**  
Lista `ASSIGNEE_RULES` nie zawiera wzorca `"security"` → dla tytułów jak "Security Policy", "Security Plan" pierwszym pasującym wzorcem jest `"policy"` (→ `ai_agent_writer`) lub `"plan"` (→ `ai_agent_writer`). Tymczasem "Security Plan" to dokument o wysokim rygory wymagający eksperta ludzkiego (podobnie do "Architecture Plan").

**Wpływ:**  
- `WorkPackage` dla dokumentów bezpieczeństwa niepoprawnie przypisany do `ai_agent_writer` zamiast `human`.  
- Plan pracy zaniedba potrzebę zaangażowania Security Architekta.

**Naprawa:**  
Dodać wzorzec przed `"plan"`:
```python
("security_plan",   "human"),
("security_policy", "human"),
("incident_response", "human"),
```
Lub dodać wyżej na liście: `("security", "human")` — przed `"policy"` i `"plan"`.

---

## OBSZAR R — Spójność danych i transakcje (R-01…R-09)

---

#### R-01: Brak atomowości operacji `POST /brief/upload` — partial write przy błędzie parsowania

**Plik:** dok.05 §2.2 (Postconditions POST /brief/upload)  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
Spec definiuje dwuetapową operację: (1) zapis do `briefs` z `parse_status='parsing'`, (2) parsowanie i aktualizacja do `parse_status='parsed'`. Brak specyfikacji transakcyjności. Jeśli etap 2 zawiedzie po etapie 1 (np. `pdfplumber` crash, OOM, SIGKILL), rekord `briefs` pozostaje w stanie `'parsing'` — bez możliwości automatycznego powrotu do `'failed'`. Nie ma mechanizmu "startup recovery" analogicznego do webhook (dok.04 §2.14).

**Wpływ:**  
- Rekord `briefs` z `parse_status='parsing'` blokuje ewentualne retry klienta (klient nie wie czy czekać czy ponowić upload).  
- `POST /brief/{id}/map` wymaga `parse_status='parsed'` — zwróci 409 dla "stuck parsing" briefa.  
- Nagromadzenie zombie records w produkcji.

**Naprawa:**  
Dodać do lifespan startup recovery:
```sql
UPDATE briefs SET parse_status='failed', parse_error='interrupted_parsing'
WHERE parse_status='parsing'
  AND created_at < now() - interval '15 minutes';
```
Alternatywnie: cała operacja upload+parse w jednej transakcji (zapis raw_content + synchroniczne parsowanie przed commitem).

---

#### R-02: Brak `ON DELETE CASCADE` w relacjach `estimation_reports` i `work_plans`

**Plik:** dok.04 §2.5, §2.7  
**Priorytet:** 🔴 KRYTYCZNE  
**Problem:**  
```sql
-- estimation_reports:
mapping_id UUID NOT NULL REFERENCES mapping_results(id),  -- BRAK ON DELETE CASCADE
project_id UUID NOT NULL REFERENCES projects(id),         -- BRAK ON DELETE CASCADE

-- work_plans:
report_id  UUID NOT NULL REFERENCES estimation_reports(id), -- BRAK ON DELETE CASCADE
project_id UUID NOT NULL REFERENCES projects(id),           -- BRAK ON DELETE CASCADE
```
Spec deklaruje w dok.04 §5: *"Projekt można usunąć w całości"* dzięki kaskadzie `projects → briefs → mapping_results → mapping_items`. Ale łańcuch zatrzymuje się na `mapping_results` — `estimation_reports` i `work_plans` **nie** mają CASCADE, więc próba usunięcia projektu lub mapping_results z istniejącymi raportami/planami rzuci `ForeignKeyViolation`.

**Wpływ:**  
- `DELETE FROM projects WHERE id=?` zakończy się błędem 500 gdy projekt ma raporty lub plany.  
- `DELETE FROM mapping_results WHERE id=?` (np. cleanup) — identyczny problem.  
- Orphan records po ominięciu FK (np. przez TRUNCATE lub bezpośredni SQL).

**Naprawa:**  
Dodać migrację 0010 z poprawką FK:
```sql
ALTER TABLE estimation_reports
  DROP CONSTRAINT estimation_reports_mapping_id_fkey,
  ADD CONSTRAINT estimation_reports_mapping_id_fkey
    FOREIGN KEY (mapping_id) REFERENCES mapping_results(id) ON DELETE CASCADE;

ALTER TABLE work_plans
  DROP CONSTRAINT work_plans_report_id_fkey,
  ADD CONSTRAINT work_plans_report_id_fkey
    FOREIGN KEY (report_id) REFERENCES estimation_reports(id) ON DELETE CASCADE;
```

---

#### R-03: Zombie `mapping_results='running'` — brak startup recovery

**Plik:** dok.04 §2.3, dok.05 §2.2  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
Spec definiuje startup recovery dla webhooks (dok.04 §2.14) ale **brak** analogicznego mechanizmu dla `mapping_results`. Po krachu procesu (P-01), rekordy `mapping_results` ze statusem `'running'` blokują retry (HTTP 409). Spec nie definiuje:
- Jaki czas oczekiwania zanim `'running'` jest uznane za zombie?
- Kto resetuje status (startup hook? cron? manual API)?

**Wpływ:**  
- Produkcja po deployu zawsze ma "stuck" rekordy dla briefów przetwarzanych w momencie deployu.  
- Klient musi kontaktować się z administratorem aby manualnie zresetować status.

**Naprawa:**  
Dodać do FastAPI `lifespan` startup handler:
```python
async def startup_recovery():
    await db.execute("""
        UPDATE mapping_results SET status='failed', error='process_crash_recovery'
        WHERE status='running'
          AND created_at < now() - interval '10 minutes'
    """)
```
Dodać specyfikację w dok.04 §2.3 i dok.05 §2.2.

---

#### R-04: Brak UNIQUE constraint na `mapping_results.content_hash` — duplikaty przy race condition

**Plik:** dok.04 §2.3, dok.09 §11  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
Tabela `mapping_results` zawiera `content_hash TEXT` z indeksem `idx_mapping_cache` (dla lookup), ale bez `UNIQUE` constraint. Cache lookup (dok.09 §11) używa:
```sql
SELECT * FROM mapping_results WHERE content_hash=? AND status='done' ORDER BY created_at DESC LIMIT 1
```
Przy race condition (P-04) dwa równoległe `INSERT` tworzą dwa rekordy z tym samym `content_hash`. Oba kończą status='done'. Cache lookup zwróci zawsze jeden (najnowszy), ale niepotrzebne koszty LLM i duplikaty.

Dodatkowo: SQL w dok.09 §11 używa placeholder `?` (SQLite style) zamiast `$1` (PostgreSQL style) — błąd w specyfikacji.

**Wpływ:**  
- Nieskuteczne cache — dwa mapowania tego samego briefu nie korzystają z cache.  
- `JSONDecodeError` lub błąd przy cachowaniu.  
- SQL placeholder `?` nie działa z `asyncpg` → runtime error.

**Naprawa:**  
```sql
-- Migracja: dodaj UNIQUE
CREATE UNIQUE INDEX idx_mapping_cache_unique
  ON mapping_results(content_hash) WHERE status='done';
```
Poprawić SQL w dok.09 §11: `content_hash=$1 AND status='done'` (parametr pozycyjny PostgreSQL).

---

#### R-05: `work_packages.depends_on UUID[]` — brak integralności referencyjnej

**Plik:** dok.04 §2.8  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
```sql
depends_on UUID[]  -- IDs poprzednich work_packages
```
PostgreSQL **nie obsługuje** FK constraint na elementach tablicy. Usunięcie `work_package` A nie czyści referencji do A w polu `depends_on` innych pakietów. Orphan UUID references prowadzą do błędów logicznych gdy aplikacja iteruje po `depends_on` zakładając że każdy UUID wskazuje na istniejący rekord.

**Wpływ:**  
- `GET /planning/{plan_id}/packages` z join na `depends_on` zwróci niekompletne dane.  
- Nie da się łatwo znaleźć orphan references bez custom SQL.  
- Trudność w cascade delete planu: DELETE work_packages per sequence_order może zostawić orphan references.

**Naprawa:**  
Alternatywy:
1. Normalizacja do tabeli relacyjnej (zalecane):
```sql
CREATE TABLE work_package_deps (
    package_id   UUID NOT NULL REFERENCES work_packages(id) ON DELETE CASCADE,
    depends_on   UUID NOT NULL REFERENCES work_packages(id) ON DELETE CASCADE,
    PRIMARY KEY (package_id, depends_on)
);
```
2. Jeśli UUID[] jest zachowane — dodać `ON DELETE` trigger czyszczący orphan UUIDs.

---

#### R-06: Błąd w SQL retencji `llm_calls_log` — odwołanie do nieistniejącej kolumny

**Plik:** dok.04 §6 (Retencja danych llm_calls_log)  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
SQL retencji w dok.04 §6 zawiera:
```sql
DELETE FROM llm_calls_log
WHERE created_at < now() - interval '30 days'
  AND status = 'cached'
  AND id NOT IN (
    SELECT DISTINCT llm_call_id FROM mapping_results   -- ← kolumna nie istnieje!
    WHERE created_at > now() - interval '30 days'
  );
```
Tabela `mapping_results` (dok.04 §2.3) nie zawiera kolumny `llm_call_id`. Kolumny: `id, brief_id, llm_model, extracted_entities, total_items, avg_confidence, status, error, content_hash, created_at, completed_at`. Ten SQL rzuci `OperationalError: column "llm_call_id" does not exist` przy każdym uruchomieniu.

**Wpływ:**  
- Scheduled job retencji zawsze kończy się błędem.  
- `llm_calls_log` rośnie bez ograniczeń → degradacja wydajności lookup hash.  
- Administrator nie widzi błędu jeśli Celery task nie ma alertingów.

**Naprawa:**  
Powiązanie `llm_calls_log` z `mapping_results` odbywa się przez `entity_id`:
```sql
DELETE FROM llm_calls_log
WHERE created_at < now() - interval '30 days'
  AND status = 'cached'
  AND entity_id NOT IN (
    SELECT id FROM mapping_results
    WHERE created_at > now() - interval '30 days'
  );
```
Alternatywnie: dodać kolumnę `llm_call_id UUID REFERENCES llm_calls_log(id)` do `mapping_results` (migracja).

---

#### R-07: Brak transakcyjności `WorkPlanner.create_plan` — partial write przy błędzie

**Plik:** dok.11 §4 (WorkPlanner.create_plan)  
**Priorytet:** 🟡 WAŻNE  
**Problem:**  
`create_plan()` wykonuje: INSERT do `work_plans` (step 0), następnie N × INSERT do `work_packages` (step 4). Jeśli dowolny `INSERT work_package` zawiedzie (np. `_enrich_with_contracts` rzuca wyjątek, DB timeout, błąd constraint), `work_plans` rekord istnieje ze statusem `'draft'` ale bez żadnych pakietów lub z niekompletnym zestawem. Spec nie definiuje transakcji obejmującej całą operację.

**Wpływ:**  
- `GET /planning/{plan_id}/packages` zwraca pustą lub niepełną listę dla "drafted" planu.  
- `POST /planning/create/{report_id}` zwróci 409 ("plan już istnieje") przy retry, choć istniejący plan jest niekompletny.  
- `work_plans.total_packages` może nie zgadzać się z faktyczną liczbą `work_packages`.

**Naprawa:**  
Dodać do spec. i implementacji:
```python
async with db.transaction():  # asyncpg: begin/rollback automatycznie
    plan = await db.insert("work_plans", ...)
    for pkg_data in packages:
        await db.insert("work_packages", ...)
# Jeśli cokolwiek rzuci wyjątek → całość rollback
```

---

#### R-08: Brak strategii backup PostgreSQL — ryzyko utraty danych produkcyjnych

**Plik:** dok.04 (cały dokument)  
**Priorytet:** 🟢 DROBNE  
**Problem:**  
Dokument definiuje schemat, migracje, politykę danych, retencję — ale nie zawiera żadnej wzmianki o backup strategy. Brak specyfikacji:
- Częstotliwości pg_dump (daily full? hourly incremental?)
- Point-in-Time Recovery (PITR) przez WAL archiving  
- RPO (Recovery Point Objective) / RTO (Recovery Time Objective)
- Przechowywania backupów (S3? lokalne? retencja 30/90 dni?)

Tabela `briefs` przechowuje `raw_content BYTEA` (oryginalne PDFy klientów) — bez backup są permanentnie utracone po awarii dysku.

**Wpływ:**  
- Brak backupu `raw_content` → utrata oryginalnych dokumentów klientów.  
- Brak PITR → przy korupcji DB nie można odtworzyć stanu sprzed błędu.

**Naprawa:**  
Dodać sekcję "Backup & Recovery" w dok.04 §8:
```
- pg_dump: daily full backup, retencja 30 dni (S3 / offsite)
- WAL archiving: streaming replication dla PITR
- RPO: ≤ 1h (WAL archiving), ≤ 24h (pg_dump)
- RTO: ≤ 4h (restore z pg_dump), ≤ 30 min (promote replica)
- briefs.raw_content: limit 50 MB/plik, rozważyć externalny object store (S3)
```

---

#### R-09: Brak specyfikacji migracji danych dla istniejących rekordów

**Plik:** dok.04 §4 (Alembic migrations)  
**Priorytet:** 🟢 DROBNE  
**Problem:**  
Spec definiuje schema migrations (DDL) przez Alembic, ale nie zawiera data migrations (DML) dla istniejących rekordów. Przykłady:
- **Migracja 0006** (`mapping_content_hash`): dodaje `content_hash` do `mapping_results`. Istniejące rekordy będą miały `content_hash=NULL`. Cache lookup `WHERE content_hash=$1 AND status='done'` nigdy nie trafi na stare rekordy — efektywny cache reset.
- **Migracja 0002** (`brief_versioning`): dodaje `version INTEGER NOT NULL DEFAULT 1`. Istniejące briefs dostaną `version=1`, ale `parent_brief_id=NULL` — poprawne, ale brak walidacji.
- **Migracja 0003** (`project_settings`): jeśli `app_settings` ma inne wartości default niż hardcoded defaults w kodzie, po migracji zachowanie może się zmienić.

**Wpływ:**  
- Cache mapowań staje się nieskuteczne po upgrade (wymagane przeindeksowanie).  
- Trudność w walidacji poprawności danych po migracji.

**Naprawa:**  
Dodać sekcję "Data Migration Notes" do każdej migracji Alembic. Dla migracji 0006:
```python
# W pliku 0006_mapping_content_hash.py:
def upgrade():
    op.add_column("mapping_results", sa.Column("content_hash", sa.Text()))
    # Backfill note: istniejące rekordy zachowują content_hash=NULL (świadome)
    # Cache będzie stopniowo wypełniany przy kolejnych mapowaniach
    # Opcjonalnie: przelicz SHA256 dla istniejących rekordów (kosztowne, nie wymagane)
```

---

## Podsumowanie znalezisk

| ID | Tytuł | Priorytet | Obszar |
|----|-------|-----------|--------|
| P-01 | asyncio.create_task nie przeżywa restartu workera | 🔴 KRYTYCZNE | Async |
| P-02 | Brak globalnego timeoutu pipeline wielochunkowego | 🟡 WAŻNE | Async |
| P-03 | Brak granicy asyncio vs Celery | 🟡 WAŻNE | Async |
| P-04 | Brak idempotency POST /brief/upload | 🟡 WAŻNE | Async |
| P-05 | Niespójność polling/webhook/Retry-After | 🟢 DROBNE | Async |
| P-06 | Status "partial" — niezdefiniowany próg akceptacji | 🟡 WAŻNE | Async |
| P-07 | asyncio.get_event_loop() deprecated w Python 3.12+ | 🟢 DROBNE | Async |
| Q-01 | find_by_keyword(keywords=[]) — nieokreślone zachowanie | 🟡 WAŻNE | Edge case |
| Q-02 | LLM zwraca Markdown zamiast JSON — brak parsera | 🔴 KRYTYCZNE | Edge case |
| Q-03 | InsufficientMappingError bez zdefiniowanej obsługi HTTP | 🟡 WAŻNE | Edge case |
| Q-04 | Race condition TOCTOU na POST /brief/{id}/map | 🔴 KRYTYCZNE | Edge case |
| Q-05 | Cykl w grafie WorkPlanner — cichy błąd bez logowania | 🟡 WAŻNE | Edge case |
| Q-06 | _parse_text: latin-1 silent corruption dla Win-1252 | 🟢 DROBNE | Edge case |
| Q-07 | EstimationReport nieaktualny po force_rerun | 🟡 WAŻNE | Edge case |
| Q-08 | _infer_doc_type: klucz "test" nie w DOCUMENT_TYPE_POINTS | 🟡 WAŻNE | Edge case |
| Q-09 | ASSIGNEE_RULES: brak wzorca "security" | 🟢 DROBNE | Edge case |
| R-01 | Brak atomowości POST /brief/upload — partial write | 🟡 WAŻNE | Dane |
| R-02 | Brak ON DELETE CASCADE w estimation_reports/work_plans | 🔴 KRYTYCZNE | Dane |
| R-03 | Zombie mapping_results='running' — brak startup recovery | 🟡 WAŻNE | Dane |
| R-04 | Brak UNIQUE na mapping_results.content_hash + błąd SQL | 🟡 WAŻNE | Dane |
| R-05 | work_packages.depends_on UUID[] bez integralności FK | 🟡 WAŻNE | Dane |
| R-06 | Błąd SQL retencji llm_calls_log — nieistniejąca kolumna | 🟡 WAŻNE | Dane |
| R-07 | Brak transakcyjności WorkPlanner.create_plan | 🟡 WAŻNE | Dane |
| R-08 | Brak strategii backup PostgreSQL | 🟢 DROBNE | Dane |
| R-09 | Brak data migrations dla istniejących rekordów | 🟢 DROBNE | Dane |

**Łącznie:** 25 znalezisk | 🔴 4 KRYTYCZNE · 🟡 15 WAŻNYCH · 🟢 6 DROBNYCH
