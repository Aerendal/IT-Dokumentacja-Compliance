# 14 — Testing Strategy

**Status:** Draft v1.0  
**Powiązane dokumenty:** 03_architecture_overview, 06_openapi_specification, 12_itdoc_integration_spec

---

## 1. Cel i zasady

Strategia testowania Warsztatu jest **spójna z istniejącą biblioteką itdoc** (pytest, markery, coverage). Rozszerza ją o testy specyficzne dla systemu async, bazy PostgreSQL i wywołań LLM.

**Zasady:**
1. LLM w testach **zawsze mockowany** — żadnych rzeczywistych wywołań API w testach automatycznych
2. PostgreSQL w testach integracyjnych przez **testcontainers** (izolowany kontener per test run)
3. Biblioteka itdoc w testach integracyjnych — rzeczywista baza **read-only** (fixture z istniejącym it_doc_matrix.db)
4. Testy deterministyczne — ten sam kod → te same wyniki
5. Markery spójne z istniejącym projektem: `unit`, `integration`, `slow`

---

## 2. Piramida testów

```
                    ┌───────────────┐
                    │   E2E (2-5)   │  Pełny przepływ: upload brief → work plan
                    │   @slow       │  ~30s każdy, realny PostgreSQL + mock LLM
                    └───────────────┘
               ┌──────────────────────────┐
               │   Integration (30-50)    │  DB + itdoc connector + parsery
               │   @integration           │  testcontainers PostgreSQL
               └──────────────────────────┘
          ┌──────────────────────────────────────┐
          │         Unit (100-150)               │  Logika bez DB/LLM
          │         @unit                        │  <1s każdy
          └──────────────────────────────────────┘
```

**Liczby docelowe:**
| Warstwa | Testy | Pokrycie |
|---------|-------|---------|
| Unit | ~130 | ≥ 80% kodu serwisów |
| Integration | ~45 | Wszystkie endpointy API |
| E2E | 5 | 4 happy path (jeden per Side) + 1 full flow |
| **Razem** | **~180** | **≥ 75% całości** |

---

## 3. Konfiguracja pytest

```toml
# pyproject.toml — rozszerzenie istniejącej konfiguracji

[tool.pytest.ini_options]
# Dołącz do istniejących markerów
markers = [
    "unit: testy jednostkowe bez DB i LLM (< 1s)",
    "integration: testy z PostgreSQL (testcontainers) i itdoc DB",
    "slow: testy E2E > 30s (pełny przepływ)",
]
asyncio_mode = "auto"          # pytest-asyncio auto mode dla async testów

# Pokrycie kodu warsztatu
addopts = "--cov=workshop/api --cov-report=term-missing --cov-fail-under=75"

testpaths = ["tests", "workshop/tests"]  # Istniejące + nowe testy warsztatu
```

---

## 4. Fixtures

### 4.1 Mock LLM Adapter

```python
# workshop/tests/fixtures/llm_fixtures.py

import pytest
from unittest.mock import AsyncMock, MagicMock
from workshop.api.services.llm_adapter import BaseLLMAdapter, ExtractedEntities


@pytest.fixture
def mock_llm_adapter():
    """
    Mock LLM Adapter — deterministyczne odpowiedzi.
    Używany we wszystkich testach unit i integration.
    """
    adapter = AsyncMock(spec=BaseLLMAdapter)
    adapter.provider_name = "mock"
    adapter.model_name = "mock-model-v1"
    
    # Domyślna odpowiedź extract_entities
    adapter.extract_entities = AsyncMock(return_value=ExtractedEntities(
        domains=["fintech", "cloud"],
        standards=["ISO/IEC 27001", "PCI DSS"],
        regulations=["RODO"],
        phases=[3, 5, 6, 13, 19],
        keywords=["payment", "API", "security", "audit"],
        project_type="greenfield_saas",
    ))
    
    # Domyślna odpowiedź generate_template
    adapter.generate_template = AsyncMock(return_value="""---
title: Test Szablon
category: security
phase_id: 13
standards:
  - ISO/IEC 27001
---

## Cel dokumentu

Opis celu.

## Zakres

Opis zakresu.
""")
    
    # Domyślna odpowiedź rerank_mapping
    adapter.rerank_mapping = AsyncMock(return_value=[])
    
    return adapter


@pytest.fixture
def mock_llm_adapter_error():
    """Mock LLM Adapter który rzuca LLMTimeoutError — do testowania obsługi błędów."""
    from workshop.api.services.llm_adapter import LLMTimeoutError
    adapter = AsyncMock(spec=BaseLLMAdapter)
    adapter.extract_entities = AsyncMock(side_effect=LLMTimeoutError("LLM timeout"))
    return adapter
```

### 4.2 PostgreSQL testcontainer

```python
# workshop/tests/fixtures/db_fixtures.py

import pytest
import pytest_asyncio
from testcontainers.postgres import PostgresContainer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from alembic import command
from alembic.config import Config


@pytest.fixture(scope="session")
def postgres_container():
    """Uruchamia kontener PostgreSQL dla całej sesji testowej."""
    with PostgresContainer("postgres:16-alpine") as pg:
        yield pg


@pytest_asyncio.fixture(scope="function")
async def db_session(postgres_container):
    """Świeża sesja DB dla każdego testu (rollback po teście)."""
    url = postgres_container.get_connection_url().replace("postgresql://", "postgresql+asyncpg://")
    engine = create_async_engine(url, echo=False)
    
    # Uruchom migracje Alembic
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", url.replace("+asyncpg", ""))
    command.upgrade(alembic_cfg, "head")
    
    async with engine.begin() as conn:
        async with AsyncSession(conn) as session:
            yield session
            await session.rollback()  # Cofnij po każdym teście
    
    await engine.dispose()
```

### 4.3 itdoc Connector (read-only, z prawdziwą bazą)

```python
# workshop/tests/fixtures/itdoc_fixtures.py

import pytest
import sqlite3
from pathlib import Path
from workshop.api.services.itdoc_connector import ItdocConnector


ITDOC_DB_PATH = Path(__file__).parent.parent.parent.parent / "it_doc_matrix.db"


# Sprawdź czy tabela standardów istnieje w it_doc_matrix.db
def _check_standards_table() -> bool:
    try:
        with sqlite3.connect(ITDOC_DB_PATH) as conn:
            conn.execute("SELECT 1 FROM doc_standard_mapping LIMIT 1")
            return True
    except sqlite3.OperationalError:
        return False
HAS_STANDARDS_TABLE = _check_standards_table()


@pytest.fixture(scope="session")
def itdoc_connector(settings_with_itdoc):
    """
    Prawdziwy ItdocConnector z read-only dostępem do it_doc_matrix.db.
    Używany tylko w testach @integration i @slow.
    
    Wymaga że it_doc_matrix.db istnieje w katalogu projektu.
    """
    if not ITDOC_DB_PATH.exists():
        pytest.skip("it_doc_matrix.db nie istnieje — pomijam testy integracji z itdoc")
    return ItdocConnector(settings_with_itdoc)
```

### 4.4 Sample brief fixtures

```python
# workshop/tests/fixtures/brief_fixtures.py

SAMPLE_BRIEF_TXT = """
Projekt: System płatności online dla banku ABC

Zakres projektu:
Budowa systemu płatności online obsługującego transakcje kartowe Visa/Mastercard
z pełną obsługą PCI DSS. System będzie przetwarzał dane osobowe zgodnie z RODO.

Wymagania bezpieczeństwa:
- Szyfrowanie TLS 1.3 dla wszystkich połączeń
- Rejestr dostępów i audyt zgodny z ISO/IEC 27001
- Testy penetracyjne przed wdrożeniem

Technologia:
Python/FastAPI backend, PostgreSQL, AWS Cloud (EC2, RDS, S3).
"""

SAMPLE_BRIEF_SHORT = "Małe narzędzie wewnętrzne do raportowania."

@pytest.fixture
def sample_brief_txt() -> bytes:
    return SAMPLE_BRIEF_TXT.encode("utf-8")

@pytest.fixture
def sample_brief_short() -> bytes:
    return SAMPLE_BRIEF_SHORT.encode("utf-8")
```

---

## 5. Testy jednostkowe (unit)

### 5.1 BriefParser

```python
# workshop/tests/unit/test_brief_parser.py

@pytest.mark.unit
class TestBriefParser:
    
    def test_detect_format_txt(self, parser, sample_brief_txt):
        assert parser.detect_format("brief.txt", sample_brief_txt) == "txt"
    
    def test_detect_format_md_by_extension(self, parser):
        md_content = b"# Header\n\nContent"
        assert parser.detect_format("brief.md", md_content) == "md"
    
    def test_parse_txt_returns_normalized_text(self, parser, sample_brief_txt):
        result = parser.parse(sample_brief_txt, "txt")
        assert isinstance(result.text, str)
        assert len(result.text) > 0
        assert "\x00" not in result.text
        assert result.word_count > 0
    
    def test_parse_creates_chunks(self, parser):
        long_text = "word " * 5000  # Długi tekst
        result = parser.parse(long_text.encode(), "txt")
        assert len(result.chunks) > 1
        assert all(len(c) <= parser.CHUNK_MAX_CHARS for c in result.chunks)
    
    def test_parse_empty_raises(self, parser):
        with pytest.raises(ParseError):
            parser.parse(b"", "txt")
    
    def test_normalize_removes_null_bytes(self, parser):
        text_with_nulls = b"Hello\x00World"
        result = parser.parse(text_with_nulls, "txt")
        assert "\x00" not in result.text
    
    def test_detect_language_polish(self, parser):
        pl_text = "Ąęóśżźćń lorem ipsum dolor"
        lang = parser._detect_language(pl_text)
        assert lang == "pl"
    
    def test_file_too_large_raises(self, parser):
        huge_content = b"x" * (51 * 1024 * 1024)  # 51 MB
        with pytest.raises(FileTooLargeError):
            parser.parse(huge_content, "txt")
```

### 5.2 EstimationEngine

```python
# workshop/tests/unit/test_estimation_engine.py

@pytest.mark.unit
class TestEstimationEngine:
    
    def test_points_to_hours_returns_tuple(self, engine):
        h_min, h_likely, h_max = engine.points_to_hours(4.0)
        assert h_min < h_likely < h_max
        assert h_likely == pytest.approx(4.0 * 0.5)  # 2.0h
    
    def test_classify_complexity_low(self, engine):
        assert engine.classify_complexity(50.0, 20) == "low"
    
    def test_classify_complexity_critical(self, engine):
        assert engine.classify_complexity(700.0, 250) == "critical"
    
    async def test_critical_phases_included(self, engine, mock_mapping_result):
        report = await engine.calculate(mock_mapping_result)
        critical = [p for p in report.by_phase if p.is_critical_path]
        critical_ids = {p.phase_id for p in critical}
        assert 13 in critical_ids  # Security zawsze na critical path
    
    async def test_deduction_basis_not_empty(self, engine, mock_mapping_result):
        report = await engine.calculate(mock_mapping_result)
        assert len(report.deduction_basis) >= 1
    
    async def test_total_h_min_less_than_max(self, engine, mock_mapping_result):
        report = await engine.calculate(mock_mapping_result)
        assert report.total_h_min <= report.total_h_likely <= report.total_h_max
```

### 5.3 SemanticMapper (z mock LLM)

```python
# workshop/tests/unit/test_semantic_mapper.py

@pytest.mark.unit
class TestSemanticMapper:
    
    async def test_map_returns_mapping_result(self, mapper, mock_itdoc_connector, mock_llm_adapter, sample_brief_parsed):
        result = await mapper.map(sample_brief_parsed)
        assert result.status == "done"
        assert result.total_items >= 0
    
    async def test_confidence_threshold_filters(self, mapper, sample_brief_parsed):
        result = await mapper.map(sample_brief_parsed, confidence_threshold=0.99)
        assert all(item.confidence >= 0.99 for item in result.items)
    
    async def test_max_results_respected(self, mapper, sample_brief_parsed):
        result = await mapper.map(sample_brief_parsed, max_results=10)
        assert result.total_items <= 10
    
    async def test_llm_error_propagates(self, mapper_with_error_llm, sample_brief_parsed):
        with pytest.raises(LLMTimeoutError):
            await mapper_with_error_llm.map(sample_brief_parsed)
```

---

## 6. Testy integracyjne

```python
# workshop/tests/integration/test_api_brief.py

@pytest.mark.integration
class TestBriefAPI:
    
    async def test_upload_brief_txt(self, client, project_id):
        response = await client.post(
            f"/brief/upload?project_id={project_id}",
            files={"file": ("brief.txt", SAMPLE_BRIEF_TXT, "text/plain")},
            headers={"X-API-Key": "test_key"}
        )
        assert response.status_code == 201
        data = response.json()
        assert data["format"] == "txt"
        assert data["parse_status"] == "parsed"
        assert data["word_count"] > 0
    
    async def test_upload_requires_api_key(self, client, project_id):
        response = await client.post(f"/brief/upload?project_id={project_id}",
                                     files={"file": ("b.txt", b"x", "text/plain")})
        assert response.status_code == 403
    
    async def test_map_brief_returns_result(self, client, uploaded_brief_id):
        response = await client.post(
            f"/brief/{uploaded_brief_id}/map",
            json={"confidence_threshold": 0.5},
            headers={"X-API-Key": "test_key"}
        )
        assert response.status_code == 202
        assert response.json()["status"] in ("running", "done")


@pytest.mark.integration
class TestItdocConnectorIntegration:
    
    async def test_find_by_standard_graceful_empty(self, itdoc_connector):
        """find_by_standard() nie rzuca wyjątku gdy tabela nie istnieje — zwraca []."""
        results = await itdoc_connector.find_by_standard("ISO/IEC 27001")
        assert isinstance(results, list)  # nie rzuca OperationalError
        # results może być [] gdy tabela doc_standard_mapping nie istnieje

    @pytest.mark.skipif(
        not HAS_STANDARDS_TABLE,
        reason="Tabela doc_standard_mapping nie istnieje w aktualnej wersji it_doc_matrix.db"
    )
    async def test_find_by_standard_returns_results(self, itdoc_connector):
        results = await itdoc_connector.find_by_standard("ISO/IEC 27001")
        assert len(results) > 0
    
    async def test_get_phases_returns_24(self, itdoc_connector):
        phases = await itdoc_connector.get_phases()
        assert len(phases) == 24
    
    async def test_connector_has_no_write_methods(self, itdoc_connector):
        public_methods = [m for m in dir(itdoc_connector) if not m.startswith("_")]
        write_keywords = ["insert", "update", "delete", "write", "save", "create", "drop"]
        violations = [m for m in public_methods if any(w in m for w in write_keywords)]
        assert violations == []
```

---

## 7. Testy E2E (slow)

```python
# workshop/tests/e2e/test_full_flow.py

@pytest.mark.slow
class TestFullFlow:
    
    async def test_brief_to_work_plan(
        self, client, postgres_db, mock_llm_adapter
    ):
        """
        Pełny przepływ: upload brief → map → estimate → accept → plan
        Używa realnego PostgreSQL (testcontainer) i mock LLM.
        """
        # 1. Utwórz projekt
        project = (await client.post("/projects", json={"name": "Test E2E"})).json()
        project_id = project["id"]
        
        # 2. Upload brief
        upload = (await client.post(
            f"/brief/upload?project_id={project_id}",
            files={"file": ("brief.txt", SAMPLE_BRIEF_TXT, "text/plain")},
            headers={"X-API-Key": "test_key"}
        )).json()
        brief_id = upload["brief_id"]
        assert upload["parse_status"] == "parsed"
        
        # 3. Map brief
        map_result = (await client.post(
            f"/brief/{brief_id}/map",
            json={"confidence_threshold": 0.5},
            headers={"X-API-Key": "test_key"}
        )).json()
        assert map_result["status"] == "done"
        assert map_result["total_items"] > 0
        
        # 4. Generuj kosztorys
        report = (await client.post(
            f"/reports/estimate/{brief_id}",
            headers={"X-API-Key": "test_key"}
        )).json()
        assert report["status"] == "draft"
        assert report["total_docs"] > 0
        assert report["total_h_likely"] > 0
        assert len(report["deduction_basis"]) >= 1
        
        # 5. Zaakceptuj raport
        accepted = (await client.post(
            f"/reports/{report['id']}/accept",
            headers={"X-API-Key": "test_key"}
        )).json()
        assert accepted["status"] == "accepted"
        
        # 6. Utwórz plan pracy
        plan = (await client.post(
            f"/planning/create/{report['id']}",
            headers={"X-API-Key": "test_key"}
        )).json()
        assert plan["total_packages"] > 0
        
        # 7. Pobierz work packages
        packages = (await client.get(
            f"/planning/{plan['id']}/packages",
            headers={"X-API-Key": "test_key"}
        )).json()
        assert len(packages) == plan["total_packages"]
        assert all(p["sequence_order"] > 0 for p in packages)
        assert all(p["assignee_type"] in ["ai_agent_writer", "ai_agent_reviewer", "human"]
                   for p in packages)
```

---

## 8. Uruchamianie testów

```bash
# Testy unit (szybkie, bez zewnętrznych zależności)
pytest workshop/tests/ -m unit

# Testy integracyjne (wymagają Docker dla PostgreSQL)
pytest workshop/tests/ -m integration

# Testy E2E (powolne, pełny przepływ)
pytest workshop/tests/ -m slow

# Wszystkie testy
pytest workshop/tests/

# Z pokryciem kodu
pytest workshop/tests/ --cov=workshop/api --cov-report=html

# Integracja z istniejącymi testami projektu
pytest tests/ workshop/tests/ -m "unit or integration" --ignore=tests/test_pipeline_integration.py
```

---

## 9. Makefile targets (rozszerzenie)

```makefile
# Dodaj do istniejącego Makefile:

workshop-test:
	pytest workshop/tests/ -m "unit or integration"

workshop-test-unit:
	pytest workshop/tests/ -m unit -v

workshop-test-e2e:
	pytest workshop/tests/ -m slow -v

workshop-lint:
	flake8 workshop/ --max-line-length=100

workshop-check: workshop-lint workshop-test
```

---

## 10. E2E Scenariusze — kompletna lista

Pięć scenariuszy pokrywających happy paths i kluczowe error paths:

### S1 — Fintech greenfield (happy path, pełny flow)

```python
# brief: projekt fintech greenfield z PCI DSS + RODO
# oczekiwany wynik:
SAMPLE_FINTECH_BRIEF = """
Tworzymy platformę płatniczą SaaS dla e-commerce. Wymagamy zgodności z PCI DSS i RODO.
Architektura mikroserwisów na AWS, 3 zespoły (Backend, Frontend, DevOps).
Fazy: Discovery, Architecture, Security, Testing, Compliance, Deployment.
"""
expected_min_docs = 25
expected_phases = {3, 4, 6, 13, 19}  # Architecture, Design, Security, Security, Compliance
expected_confidence_avg_min = 0.60
```

### S2 — Internal tool (skromny brief, małe wyjście)

```python
# brief: prosty tool wewnętrzny bez compliance
SAMPLE_INTERNAL_BRIEF = """
Narzędzie do zarządzania urlopami dla 50-osobowej firmy. REST API + React.
Brak specjalnych wymagań regulacyjnych.
"""
expected_max_docs = 15
expected_domains = ["internal_tool"]
expected_complexity = "low"  # total_h_likely < 80
```

### S3 — Empty/invalid brief (error path)

```python
# brief: zbyt krótki lub bez treści
SAMPLE_EMPTY_BRIEF = "Projekt IT."

async def test_empty_brief_returns_insufficient(client, ...):
    # Upload
    brief_id = (await client.post("/brief/upload", files={"file": ("b.txt", SAMPLE_EMPTY_BRIEF.encode())})).json()["brief_id"]
    # Map
    result = (await client.post(f"/brief/{brief_id}/map")).json()
    assert result["status"] in ("insufficient", "done")
    # Jeśli insufficient → EstimationEngine musi rzucić InsufficientMappingError (422)
    resp = await client.post(f"/reports/estimate/{brief_id}")
    assert resp.status_code == 422
```

### S4 — LLM-free mode (keyword-only fallback)

```python
# Konfiguracja: LLM_ENABLED=false
# Mapping powinien działać z obniżoną jakością

async def test_llm_free_mode_returns_result(client, settings_override):
    with settings_override(llm_enabled=False):
        brief_id = upload_brief(client, SAMPLE_FINTECH_BRIEF)
        result = (await client.post(f"/brief/{brief_id}/map")).json()
        assert result["status"] in ("done", "llm_free")
        # Keyword fallback musi zwrócić cokolwiek, nie crashować
        assert isinstance(result["items"], list)
```

### S5 — Plan rebuild po zmianie mappingu

```python
async def test_plan_rebuild_on_mapping_change(client, ...):
    # Full flow do planu
    brief_id, report_id, plan_id_v1 = await _full_flow_to_plan(client, SAMPLE_FINTECH_BRIEF)

    # PM zmienia threshold i re-mapuje
    await client.post(f"/brief/{brief_id}/map", json={"confidence_threshold": 0.3})

    # Stary plan powinien być stale
    old_plan = (await client.get(f"/planning/{plan_id_v1}")).json()
    assert old_plan["status"] == "stale"

    # Nowy plan powinien istnieć
    new_plans = (await client.get(f"/planning/?report_id={report_id}")).json()
    active = [p for p in new_plans if p["status"] == "active"]
    assert len(active) == 1
    assert active[0]["id"] != str(plan_id_v1)
```
