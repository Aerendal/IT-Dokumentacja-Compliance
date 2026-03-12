# 13 — Security & Config Spec

**Status:** Draft v1.0  
**Powiązane dokumenty:** 03_architecture_overview, 12_itdoc_integration_spec, 15_implementation_roadmap

---

## 1. Model bezpieczeństwa

Warsztat jest systemem **single-tenant** (v1) działającym lokalnie lub w zamkniętej sieci. Nie jest przeznaczony do publicznego dostępu przez internet. Model bezpieczeństwa zakłada:

- API Key jako jedyna forma uwierzytelnienia (HTTP header `X-API-Key`)
- Brak zarządzania użytkownikami / rolami w v1
- Wszystkie dane klientów (briefy, raporty) przechowywane lokalnie w PostgreSQL
- Klucze API LLM nigdy nie są logowane ani zwracane przez API
- Biblioteka itdoc montowana read-only w Docker

---

## 2. API Key Authentication

### Implementacja

```python
# workshop/api/security.py

from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)


async def verify_api_key(
    api_key: str = Security(API_KEY_HEADER),
    settings: Settings = Depends(get_settings),
) -> str:
    """
    Dependency do wstrzyknięcia w routery (poza /health).
    
    Raises:
      403 Forbidden — brak klucza lub klucz nieprawidłowy
    """
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Brakuje nagłówka X-API-Key"
        )
    
    if api_key not in settings.api_keys:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Nieprawidłowy klucz API"
        )
    
    return api_key
```

### Konfiguracja kluczy

```ini
# .env
# Wiele kluczy oddzielonych przecinkiem (różne klienty/agenty)
WORKSHOP_API_KEYS=key_agent_primary_abc123,key_pm_secondary_def456
```

```python
# workshop/api/config.py

class Settings(BaseSettings):
    workshop_api_keys: str = ""  # "key1,key2,key3"
    
    @property
    def api_keys(self) -> set[str]:
        return {k.strip() for k in self.workshop_api_keys.split(",") if k.strip()}
```

### Użycie w routerach

```python
# Zabezpieczony router
router = APIRouter(
    prefix="/brief",
    tags=["brief"],
    dependencies=[Depends(verify_api_key)]  # Wszystkie endpointy routera wymagają klucza
)

# Wyjątek: /health jest publiczny
@app.get("/health")  # Bez dependency verify_api_key
async def health_check():
    ...
```

---

## 3. Zarządzanie sekretami

### Hierarchia konfiguracji (priorytet malejący)

```
1. Zmienne środowiskowe systemu (najwyższy priorytet)
2. Plik .env (dla devu lokalnego)
3. Wartości domyślne z Settings (najniższy priorytet)
```

### Plik .env.example

```ini
# ═══════════════════════════════════════════
# AI DOCUMENTATION WORKSHOP — Konfiguracja
# Skopiuj jako .env i uzupełnij wartości
# NIGDY nie commituj .env do repozytorium!
# ═══════════════════════════════════════════

# ── Aplikacja ──────────────────────────────
WORKSHOP_ENV=development          # development | production
WORKSHOP_DEBUG=false
WORKSHOP_API_KEYS=zmień_mnie_1,zmień_mnie_2
WORKSHOP_PORT=8000
WORKSHOP_HOST=0.0.0.0

# ── Baza danych (PostgreSQL) ───────────────
DATABASE_URL=postgresql+asyncpg://workshop:haslo@localhost:5432/workshop_db
# Dla Docker Compose: postgresql+asyncpg://workshop:haslo@db:5432/workshop_db

# ── Biblioteka itdoc (read-only) ──────────
ITDOC_DB_PATH=/app/itdoc_library/it_doc_matrix.db

# ── LLM Provider ──────────────────────────
LLM_PROVIDER=openai               # openai | anthropic | ollama

# OpenAI (jeśli LLM_PROVIDER=openai)
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o               # gpt-4o | gpt-4o-mini

# Anthropic (jeśli LLM_PROVIDER=anthropic)
ANTHROPIC_API_KEY=sk-ant-...
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022

# Ollama (jeśli LLM_PROVIDER=ollama)
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# ── LLM Cache ──────────────────────────────
LLM_CACHE_ENABLED=true
LLM_CACHE_TTL_HOURS=24
LLM_RERANKING_ENABLED=false       # Włącz dla lepszej precision (kosztowniejsze)

# ── Mapowanie ──────────────────────────────
CONFIDENCE_THRESHOLD_DEFAULT=0.4
MAX_MAPPING_RESULTS=200
RHYTHM_DEPTH=1

# ── Wycena ─────────────────────────────────
ESTIMATION_H_PER_POINT=0.5

# ── Bezpieczeństwo plików ──────────────────
MAX_BRIEF_FILE_SIZE_MB=50
MAX_INGESTION_FILE_SIZE_MB=10
```

### Walidacja przy starcie

```python
# workshop/api/config.py

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    # Wymagane — aplikacja nie startuje bez nich
    database_url:         str
    itdoc_db_path:        str
    workshop_api_keys:    str
    llm_provider:         str
    
    # Walidacja po inicjalizacji
    @model_validator(mode='after')
    def validate_required_secrets(self) -> 'Settings':
        if not self.api_keys:
            raise ValueError("WORKSHOP_API_KEYS nie może być puste")
        
        if self.llm_provider == "openai" and not self.openai_api_key:
            raise ValueError("LLM_PROVIDER=openai wymaga ustawienia OPENAI_API_KEY")
        
        if self.llm_provider == "anthropic" and not self.anthropic_api_key:
            raise ValueError("LLM_PROVIDER=anthropic wymaga ustawienia ANTHROPIC_API_KEY")
        
        if not Path(self.itdoc_db_path).exists():
            raise ValueError(f"Nie znaleziono bazy itdoc: {self.itdoc_db_path}")
        
        return self
```

---

## 4. PostgreSQL — zabezpieczenia

### Polityka uprawnień użytkownika DB

```sql
-- Utwórz dedykowanego użytkownika z minimalnymi uprawnieniami
CREATE USER workshop_app WITH PASSWORD 'silne_haslo';
CREATE DATABASE workshop_db OWNER workshop_app;

-- Uprawnienia: tylko do własnej bazy
GRANT CONNECT ON DATABASE workshop_db TO workshop_app;
GRANT USAGE ON SCHEMA public TO workshop_app;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO workshop_app;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO workshop_app;

-- Brak uprawnień do: CREATE TABLE, DROP, ALTER (Alembic używa osobnego migratora)
```

### Zabezpieczenia połączenia

```ini
# W Docker Compose: PostgreSQL dostępny tylko wewnątrz sieci Docker
# Nie mapuj portu 5432 na host jeśli nie jest potrzebny zewnętrznie
# docker-compose.yml: NIE dodawaj "ports: - "5432:5432"" dla serwisu db

# W .env:
DATABASE_URL=postgresql+asyncpg://workshop_app:haslo@db:5432/workshop_db
# "db" = nazwa serwisu Docker, niedostępna spoza sieci Docker
```

---

## 5. Bezpieczeństwo przesyłania plików

```python
# workshop/api/routers/brief.py

ALLOWED_CONTENT_TYPES = {
    "text/plain",
    "text/markdown",
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}

ALLOWED_EXTENSIONS = {".txt", ".md", ".pdf", ".docx"}

async def validate_upload(file: UploadFile, settings: Settings) -> bytes:
    """
    Walidacja pliku przed parsowaniem.
    Chroni przed: zbyt dużymi plikami, złośliwymi typami plików.
    """
    
    # 1. Sprawdź rozszerzenie
    ext = Path(file.filename or "").suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(415, f"Nieobsługiwane rozszerzenie: {ext}")
    
    # 2. Odczytaj plik z limitem rozmiaru
    content = await file.read(settings.max_brief_file_size_mb * 1024 * 1024 + 1)
    if len(content) > settings.max_brief_file_size_mb * 1024 * 1024:
        raise HTTPException(413, f"Plik przekracza limit {settings.max_brief_file_size_mb} MB")
    
    # 3. Sprawdź MIME na podstawie magic bytes (nie Content-Type z requestu!)
    detected_mime = magic.from_buffer(content[:1024], mime=True)
    if detected_mime not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(415, f"Wykryty nieobsługiwany typ MIME: {detected_mime}")
    
    return content
```

---

## 6. Logowanie (bez sekretów)

```python
# workshop/api/middleware/logging.py

class SecurityAwareLoggingMiddleware(BaseHTTPMiddleware):
    """
    Loguje requesty/response bez wrażliwych danych.
    
    Nigdy nie loguje:
    - X-API-Key
    - OPENAI_API_KEY, ANTHROPIC_API_KEY
    - Zawartości plików briefów
    - Treści odpowiedzi LLM
    """
    
    SENSITIVE_HEADERS = {"x-api-key", "authorization"}
    
    async def dispatch(self, request: Request, call_next):
        # Filtruj wrażliwe nagłówki z logów
        safe_headers = {
            k: "***" if k.lower() in self.SENSITIVE_HEADERS else v
            for k, v in request.headers.items()
        }
        
        logger.info(f"{request.method} {request.url.path}", extra={"headers": safe_headers})
        
        response = await call_next(request)
        logger.info(f"Response: {response.status_code}")
        return response
```

---

## 7. Rate limiting (LLM calls)

```python
# workshop/api/services/llm_adapter.py

from asyncio import Semaphore

class BaseLLMAdapter(ABC):
    
    def __init__(self, settings: Settings):
        # Semaphore ogranicza współbieżne wywołania LLM
        self._semaphore = Semaphore(settings.llm_max_concurrent_calls or 3)
    
    async def _call_with_semaphore(self, func, *args, **kwargs):
        async with self._semaphore:
            return await func(*args, **kwargs)
```

```ini
# .env
LLM_MAX_CONCURRENT_CALLS=3      # Max 3 równoległe wywołania LLM
```

---

## 8. .gitignore — obowiązkowe wpisy

```gitignore
# workshop/ — wrażliwe pliki
workshop/.env
workshop/.env.local
workshop/.env.production
workshop/**/*.pem
workshop/**/*.key
workshop/data/briefs/          # Wgrane pliki briefów (dane klientów)
workshop/data/exports/         # Wygenerowane raporty

# Nigdy nie commituj
*.env
.env*
!.env.example                  # .env.example JEST commitowany
```

---

## 10. Centralna tabela zmiennych środowiskowych

Wszystkie zmienne env używane przez warsztat — w tym zmienne zdefiniowane w innych modułach:

| Zmienna | Domyślna | Moduł | Opis |
|---------|----------|-------|------|
| `WORKSHOP_ENV` | `development` | Core | Środowisko: `development` \| `production` |
| `WORKSHOP_DEBUG` | `false` | Core | Tryb debug |
| `WORKSHOP_API_KEYS` | — | Auth | Klucze API oddzielone przecinkiem |
| `WORKSHOP_PORT` | `8000` | Core | Port serwisu |
| `WORKSHOP_HOST` | `0.0.0.0` | Core | Host serwisu |
| `DATABASE_URL` | — | Core | URL bazy danych (runtime, ograniczone prawa) |
| `DATABASE_URL_ADMIN` | — | Alembic | URL DB dla migracji (pełne prawa DDL) |
| `ITDOC_DB_PATH` | — | ItdocConnector | Ścieżka do `it_doc_matrix.db` (read-only) |
| `LLM_PROVIDER` | `openai` | LLMAdapter | Provider LLM: `openai` \| `anthropic` \| `ollama` |
| `OPENAI_API_KEY` | — | LLMAdapter | Klucz API OpenAI |
| `OPENAI_MODEL` | `gpt-4o` | LLMAdapter | Model OpenAI |
| `ANTHROPIC_API_KEY` | — | LLMAdapter | Klucz API Anthropic |
| `ANTHROPIC_MODEL` | `claude-3-5-sonnet-20241022` | LLMAdapter | Model Anthropic |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | LLMAdapter | URL serwisu Ollama |
| `OLLAMA_MODEL` | `llama3.2` | LLMAdapter | Model Ollama |
| `LLM_TIMEOUT_SECONDS` | `60` | LLMAdapter | Timeout dla pojedynczego wywołania LLM |
| `LLM_CACHE_ENABLED` | `true` | LLMAdapter | Włącz cache odpowiedzi LLM |
| `LLM_CACHE_TTL_HOURS` | `24` | LLMAdapter | TTL wpisów cache (godziny) |
| `LLM_RERANKING_ENABLED` | `false` | LLMAdapter | Reranking wyników (kosztowniejsze) |
| `LLM_MAX_CONCURRENT_CALLS` | `3` | LLMAdapter | Max równoległych wywołań LLM (semaphore) |
| `CONFIDENCE_THRESHOLD_DEFAULT` | `0.4` | SemanticMapper | Domyślny próg confidence |
| `MAX_MAPPING_RESULTS` | `200` | SemanticMapper | Max wyników mapowania |
| `RHYTHM_DEPTH` | `1` | SemanticMapper | Głębokość ekspansji rhythm |
| `WORKSHOP_MAX_KEYWORDS` | `30` | SemanticMapper | Max keywords do `find_by_keyword` |
| `WORKSHOP_MIN_EXPECTED_DOCS` | `3` | SemanticMapper | Próg dla `status=partial` |
| `ESTIMATION_H_PER_POINT` | `0.5` | EstimationEngine | Przelicznik punktów złożoności na godziny |
| `WORKSHOP_MAX_DOCS_ESTIMATION` | `500` | EstimationEngine | Max dokumentów w jednym raporcie |
| `MAX_BRIEF_FILE_SIZE_MB` | `50` | BriefParser | Max rozmiar pliku briefu |
| `WORKSHOP_MAX_UPLOAD_SIZE_MB` | `10` | BriefParser | Max rozmiar uploadu briefu (ingestia) |
| `MAX_INGESTION_FILE_SIZE_MB` | `10` | IngestionService | Max rozmiar pliku ingestii |
| `INGESTION_ALLOWED_DOMAINS` | `""` | IngestionService | Allowlist domen URL (puste = blokuj RFC1918) |
| `RHYTHM_DEPTH_PLANNING` | `2` | WorkPlanner | Głębokość ekspansji rhythm_upstream w planie |
| `ENABLE_PHASE_ORDERING` | `true` | WorkPlanner | Wymuszaj kolejność faz SDLC |
| `HUMAN_ASSIGNEE_PATTERNS` | `audit,approval,...` | WorkPlanner | Wzorce dokumentów przypisywanych człowiekowi |
| `WORKSHOP_ENFORCE_OWNERSHIP` | `true` | Auth | Weryfikuj własność zasobu (wyłącz w dev) |
| `WORKSHOP_SECRET_KEY` | — | Auth | Klucz podpisu JWT (min 32 bajty losowe) |
| `WORKSHOP_SECRET_BACKEND` | `file` | Secrets | Backend sekretów: `file` \| `vault` \| `aws` |

> **Zasada konfigurowalności:** Wszystkie stałe z prefixem `WORKSHOP_` mogą być nadpisane
> przez zmienne środowiskowe. Wartości domyślne są bezpieczne dla środowiska production.
> Zmienne bez wartości domyślnej (`—`) są wymagane — aplikacja nie wystartuje bez nich.
> Weryfikacja odbywa się w `Settings.validate_required_secrets()` przy starcie.
