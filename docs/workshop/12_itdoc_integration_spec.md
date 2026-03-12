# 12 — itdoc Integration Spec

**Status:** Draft v1.1 — zaktualizowano po audycie bazy (stan faktyczny it_doc_matrix.db)  
**Powiązane dokumenty:** 02_system_state_description, 03_architecture_overview, 05_module_interface_contracts, 16_data_strategy

---

## 0. Stan faktyczny it_doc_matrix.db (WAŻNE — przeczytaj przed implementacją)

Empiryczna weryfikacja bazy ujawniła że kluczowe tabele są puste lub nie istnieją:

| Tabela | Stan | Implikacja dla Connector |
|--------|------|-------------------------|
| `doc_standard_mapping` | **NIE ISTNIEJE** | `find_by_standard()` rzuci `OperationalError` |
| `contracts` | **NIE ISTNIEJE** | `get_contract()` rzuci `OperationalError` |
| `rhythm_edges` | **0 wierszy** | `rhythm_upstream()` zawsze zwróci `[]` |
| `standards` | **0 wierszy** | brak danych o standardach |
| `document_standards` | **0 wierszy** | brak mapowań |
| `compliance_regulations` | **0 wierszy** | brak mapowań regulacji |
| `document_phases` | **0 wierszy** | ale tabela `phases` ma 24 wiersze (inna tabela!) |
| `documents.path` | **kolumna nie istnieje** | tylko `doc_id, branch_id, phase_id, flag, title` |
| `documents` | **7 205 wierszy** ✅ | Zaindeksowanych z 7941 plików Markdown (7203 core + 738 satellite); ~736 satellite bez wpisów w DB |
| `document_phase_mapping` | **7 205 wierszy** ✅ | |
| `phases` | **24 wiersze** ✅ | (uwaga: nie `document_phases`) |
| `branches` | **12 wierszy** ✅ | |
| `industries` | **90 wierszy** ✅ | |

**Konsekwencja:** Wszystkie metody muszą implementować **dwupoziomowy fallback**:
1. Spróbuj pierwotne zapytanie itdoc API
2. Jeśli `OperationalError`/`sqlite3.Error` (brakująca tabela) → użyj fallback query na dostępnych tabelach
3. Jeśli wynik pusty → użyj `find_by_keyword()` na `documents.title`

Patrz **dok.16 Data Strategy** po strategię długoterminową (populate vs. embeddings).

---

## 1. Zasada nadrzędna

> **Biblioteka `itdoc` jest używana wyłącznie w trybie read-only.**  
> Warsztat nigdy nie zapisuje, nie modyfikuje i nie usuwa niczego w:
> - `it_doc_matrix.db` (SQLite)
> - `generated_templates/` (pliki Markdown szablonów)
> - `itdoc/*.py` (kod biblioteki)

Naruszenie tej zasady invaliduje gwarancje biblioteki i może spowodować niespójność danych.

---

## 2. ItdocConnector — wrapper read-only

### Konwencja doc_uid
`doc_uid` w Warsztacie = `str(documents.doc_id)`, gdzie `doc_id` to INTEGER PRIMARY KEY.
Przykłady prawidłowych doc_uid: `"1"`, `"42"`, `"1500"`.
**NIE** używać formatów semantycznych (np. `"security_audit_42"`).

Cała komunikacja z biblioteką odbywa się przez `ItdocConnector` — dedykowaną klasę Warsztatu, która:
1. Opakowuje synchroniczne wywołania itdoc w `asyncio.run_in_executor` (itdoc jest sync, Warsztat jest async)
2. Izoluje błędy biblioteki itdoc do własnych wyjątków Warsztatu
3. Cachuje wyniki statyczne (fazy, lista standardów) — te dane rzadko się zmieniają

```python
# workshop/api/services/itdoc_connector.py

import asyncio
import sqlite3
from typing import TYPE_CHECKING
from pathlib import Path

from itdoc import get_connection, find_by_standard, find_by_regulation
from itdoc import get_contract, rhythm_upstream, rhythm_downstream
from itdoc.exceptions import ItDocError, QueryError

from ..config import Settings
from ..models.brief import DocRef, DocContract, Phase


class ItdocConnector:
    """
    Read-only wrapper na Python API biblioteki itdoc.
    Thread-safe: każde wywołanie otwiera własny context manager get_connection().
    """
    
    def __init__(self, settings: Settings):
        self._db_path = settings.itdoc_db_path  # ścieżka do it_doc_matrix.db
        self._executor = None  # używa default ThreadPoolExecutor event loop
    
    async def _run_sync(self, func, *args, **kwargs):
        """Uruchamia synchroniczną funkcję itdoc w thread executor."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            self._executor,
            lambda: func(*args, **kwargs)
        )
    
    async def health_check(self) -> bool:
        """Sprawdza dostępność it_doc_matrix.db. Używane przez /health endpoint."""
        try:
            def _check():
                from itdoc import validate_schema
                with get_connection(self._db_path) as conn:
                    return validate_schema(conn)
            return await self._run_sync(_check)
        except Exception:
            return False
```

---

## 3. Implementacje metod

### 3.1 find_by_standard

```python
async def find_by_standard(self, standard_code: str) -> list[DocRef]:
    """
    Mapuje standard_code → lista dokumentów z biblioteki.
    Używa itdoc.find_by_standard() w context manager.
    
    Obsługa błędów:
    - ItDocError → ItdocQueryError (własny wyjątek warsztatu)
    - Pusty wynik → zwraca [] (nie rzuca wyjątku)
    """
    def _query():
        with get_connection(self._db_path) as conn:
            results = find_by_standard(conn, standard_code)
            return [
                DocRef(
                    doc_uid=r["doc_uid"],
                    title=r["title"],
                    path=r.get("path"),
                    phase_id=r.get("phase_id", 0),
                    phase_name=r.get("phase_name", "Unknown"),
                )
                for r in results
            ]
    
    try:
        return await self._run_sync(_query)
    except (QueryError, ItDocError) as e:
        raise ItdocQueryError(f"find_by_standard({standard_code}) failed: {e}") from e
    except (sqlite3.OperationalError, sqlite3.Error) as e:
        # Tabela doc_standard_mapping może nie istnieć w aktualnej wersji DB
        # Graceful degradation: zwróć [] zamiast crashować, SemanticMapper użyje fallback
        import logging
        logging.getLogger(__name__).warning(
            f"find_by_standard({standard_code}): tabela niedostępna ({e}). Używam fallback."
        )
        return []
```

### 3.2 find_by_regulation

```python
async def find_by_regulation(self, regulation_code: str) -> list[DocRef]:
    """Analogicznie do find_by_standard"""
    def _query():
        with get_connection(self._db_path) as conn:
            results = find_by_regulation(conn, regulation_code)
            return [DocRef(...) for r in results]
    
    try:
        return await self._run_sync(_query)
    except (QueryError, ItDocError) as e:
        raise ItdocConnectorError(str(e)) from e
    except (sqlite3.OperationalError, sqlite3.Error) as e:
        import logging
        logging.getLogger(__name__).warning(
            f"find_by_regulation({regulation_code}): tabela niedostępna ({e}). Używam fallback."
        )
        return []
```

### 3.3 get_contract

```python
async def get_contract(self, doc_uid: str) -> DocContract | None:
    """
    Pobiera kontrakt dokumentu (inputs/outputs/gates).
    
    Ważne: tabela contracts w it_doc_matrix.db jest częściowo pusta (stub).
    Zwraca None jeśli kontrakt nie istnieje lub jest pusty — 
    WorkPlanner obsługuje ten przypadek przez fallback PHASE_DEFAULT_CONTRACTS.
    """
    def _query():
        with get_connection(self._db_path) as conn:
            contract = get_contract(conn, doc_uid)
            if not contract:
                return None
            # Parsuj JSON pola z kontraktu
            inputs  = json.loads(contract.get("inputs_json",  "[]") or "[]")
            outputs = json.loads(contract.get("outputs_json", "[]") or "[]")
            gates   = json.loads(contract.get("gates_json",   "[]") or "[]")
            
            if not inputs and not outputs and not gates:
                return None  # Stub — traktuj jako brak kontraktu
            
            return DocContract(inputs=inputs, outputs=outputs, gates=gates)
    
    try:
        return await self._run_sync(_query)
    except (QueryError, ItDocError):
        return None  # Graceful degradation — kontrakt to nice-to-have
    except (sqlite3.OperationalError, sqlite3.Error):
        # Tabela contracts nie istnieje w aktualnej wersji DB — bezpieczny fallback
        return None
```

### 3.4 rhythm_upstream / rhythm_downstream

```python
async def rhythm_upstream(self, doc_uid: str, depth: int = 1) -> list[DocRef]:
    """Dokumenty wymagane przed doc_uid."""
    def _query():
        with get_connection(self._db_path) as conn:
            results = rhythm_upstream(conn, doc_uid, depth=depth)
            return [DocRef(doc_uid=r["node"], ...) for r in results]
    
    try:
        return await self._run_sync(_query)
    except (QueryError, ItDocError):
        return []  # Graceful degradation — brak zależności to gorszy plan, nie błąd
    except (sqlite3.OperationalError, sqlite3.Error):
        return []  # rhythm_edges może być pusta — zwróć [] zamiast crashować

async def rhythm_downstream(self, doc_uid: str, depth: int = 1) -> list[DocRef]:
    """Dokumenty zależne od doc_uid (następujące)."""
    # Analogicznie
```

### 3.5 get_phases

```python
# @lru_cache NIE działa poprawnie z async coroutines (cachuje obiekt coroutine, nie wynik).
# Zamiast tego używamy ręcznej cache jako atrybutu instancji:

async def get_phases(self) -> list[Phase]:
    """
    Pobiera wszystkie fazy SDLC z itdoc, posortowane wg ordinal.
    Cachowane w _phases_cache — fazy nie zmieniają się w runtime.
    
    UWAGA: Aktualnie tabela `document_phases` jest pusta.
    Faktyczna tabela faz to `phases` (24 wiersze): (phase_id, name, ordinal)
    """
    if self._phases_cache is not None:
        return self._phases_cache
    
    def _query():
        with get_connection(self._db_path) as conn:
            # Próbuj document_phases (docelowa) — fallback na phases (aktualna)
            try:
                cursor = conn.execute(
                    "SELECT phase_id, phase_name, ordinal FROM document_phases ORDER BY ordinal"
                )
                rows = cursor.fetchall()
            except sqlite3.OperationalError:
                rows = []
            
            if not rows:
                # Fallback na tabelę phases (faktycznie wypełniona w aktualnej DB)
                cursor = conn.execute(
                    "SELECT rowid as phase_id, name as phase_name, ordinal FROM phases ORDER BY ordinal"
                )
                rows = cursor.fetchall()
            
            return [Phase(phase_id=r[0], phase_name=r[1], ordinal=r[2]) for r in rows]
    
    result = await self._run_sync(_query)
    self._phases_cache = result   # cache na czas życia obiektu
    return result

# W __init__ ItdocConnector dodaj: self._phases_cache: list[Phase] | None = None
```

### 3.6 find_by_keyword (NOWA METODA — fallback discovery)

```python
async def find_by_keyword(
    self,
    keywords: list[str],
    phase_id: int | None = None,
    branch_id: int | None = None,
    limit: int = 100,
) -> list[DocRef]:
    """
    Fallback document discovery — szuka dokumentów po tytułach gdy
    find_by_standard/find_by_regulation nie zwrócą wyników (puste tabele mapowań).
    
    Używa istniejących tabel: documents + document_phase_mapping + phases.
    
    Args:
        keywords: Lista słów kluczowych z briefu (z LLM entities)
        phase_id: Opcjonalne filtrowanie do konkretnej fazy
        branch_id: Opcjonalne filtrowanie do branch (Backend/Frontend/QA itp.)
        limit: Maks. liczba wyników
    
    Returns:
        Lista DocRef posortowana wg liczby dopasowań keywords w tytule
    """
    # BEZPIECZEŃSTWO: keywords mogą pochodzić z LLM — używamy parametryzowanych zapytań
    def _query():
        with get_connection(self._db_path) as conn:
            if not keywords:
                return []
            
            safe_kws = keywords[:20]
            placeholders = " OR ".join("LOWER(d.title) LIKE LOWER(?)" for _ in safe_kws)
            params: list = [f"%{kw}%" for kw in safe_kws]
            
            sql = f"""
                SELECT DISTINCT
                    d.doc_id,
                    d.title,
                    d.phase_id,
                    d.branch_id,
                    dpm.priority,
                    p.name as phase_name
                FROM documents d
                JOIN document_phase_mapping dpm ON d.doc_id = dpm.doc_id
                LEFT JOIN phases p ON d.phase_id = p.rowid
                WHERE ({placeholders})
"""
            
            if phase_id is not None:
                sql += "                AND dpm.phase_id = ?\n"
                params.append(phase_id)
            
            if branch_id is not None:
                sql += "                AND d.branch_id = ?\n"
                params.append(branch_id)
            
            sql += f"                ORDER BY dpm.priority ASC\n                LIMIT {limit}\n            "
            
            cursor = conn.execute(sql, params)
            return [
                DocRef(
                    doc_uid=str(r[0]),       # doc_id jako string uid
                    title=r[1],
                    path=None,               # brak kolumny path w aktualnej DB
                    phase_id=r[2] or 0,
                    phase_name=r[5] or "Unknown",
                    source="keyword_fallback",  # oznaczenie źródła
                )
                for r in cursor.fetchall()
            ]
    
    try:
        return await self._run_sync(_query)
    except (sqlite3.OperationalError, sqlite3.Error) as e:
        import logging
        logging.getLogger(__name__).error(f"find_by_keyword failed: {e}")
        return []
```

### 3.7 get_documents_by_phase (NOWA METODA — phase-based discovery)

```python
async def get_documents_by_phase(
    self,
    phase_id: int,
    branch_id: int | None = None,
    limit: int = 50,
) -> list[DocRef]:
    """
    Zwraca dokumenty przypisane do danej fazy SDLC.
    Używa istniejącej tabeli document_phase_mapping.
    
    Przydatne gdy brief wskazuje konkretne fazy projektu.
    """
    def _query():
        with get_connection(self._db_path) as conn:
            params: list = [phase_id]
            sql = f"""
                SELECT d.doc_id, d.title, d.phase_id, d.branch_id, p.name
                FROM documents d
                JOIN document_phase_mapping dpm ON d.doc_id = dpm.doc_id
                LEFT JOIN phases p ON d.phase_id = p.rowid
                WHERE dpm.phase_id = ?
"""
            if branch_id is not None:
                sql += "                AND d.branch_id = ?\n"
                params.append(branch_id)
            sql += f"                ORDER BY dpm.priority ASC\n                LIMIT {limit}\n            "
            cursor = conn.execute(sql, params)
            return [
                DocRef(
                    doc_uid=str(r[0]),
                    title=r[1],
                    path=None,
                    phase_id=r[2] or phase_id,
                    phase_name=r[4] or "Unknown",
                    source="phase_lookup",
                )
                for r in cursor.fetchall()
            ]
    
    try:
        return await self._run_sync(_query)
    except (sqlite3.OperationalError, sqlite3.Error):
        return []
```

---

## 4. Obsługa błędów itdoc

```python
# workshop/api/services/itdoc_connector.py

class ItdocConnectorError(Exception):
    """Bazowy wyjątek dla błędów integracji z itdoc."""

class ItdocQueryError(ItdocConnectorError):
    """Błąd zapytania do it_doc_matrix.db."""

class ItdocSchemaError(ItdocConnectorError):
    """Schemat bazy niezgodny z oczekiwanym przez Warsztat."""
```

**Strategia obsługi błędów (zaktualizowana):**

| Metoda | Przy `OperationalError` (brak tabeli) | Przy pustym wyniku | Uzasadnienie |
|--------|--------------------------------------|--------------------|-------------|
| `find_by_standard` | Zwraca `[]` + warning log | `[]` → fallback w SemanticMapper | Tabela może nie istnieć |
| `find_by_regulation` | Zwraca `[]` + warning log | `[]` → fallback w SemanticMapper | j.w. |
| `get_contract` | Zwraca `None` | `None` → PHASE_DEFAULT_CONTRACTS | Tabela nie istnieje |
| `rhythm_upstream` | Zwraca `[]` | `[]` → plan bez zależności | rhythm_edges puste |
| `rhythm_downstream` | Zwraca `[]` | `[]` | j.w. |
| `get_phases` | Fallback na `phases` table | Rzuca `ItdocConnectorError` | Bez faz system nie działa |
| `find_by_keyword` | Zwraca `[]` + error log | `[]` | Metoda fallback — nie może crashować |
| `health_check` | Zwraca `False` | — | Tylko monitoring |

---

## 5. Konfiguracja ścieżki do bazy

```ini
# .env
ITDOC_DB_PATH=/path/to/dokumentacja/it_doc_matrix.db

# W Docker Compose: mount wolumenu
# volumes:
#   - /home/user/dokumentacja:/app/itdoc_library:ro   (read-only mount!)
# ITDOC_DB_PATH=/app/itdoc_library/it_doc_matrix.db
```

**Weryfikacja przy starcie aplikacji:**

```python
# workshop/api/main.py — lifespan event

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: weryfikuj dostępność biblioteki itdoc
    connector = ItdocConnector(settings)
    
    if not await connector.health_check():
        raise RuntimeError(
            f"Nie można połączyć się z bazą itdoc: {settings.itdoc_db_path}\n"
            "Sprawdź ścieżkę ITDOC_DB_PATH w pliku .env"
        )
    
    # Sprawdź schemat
    def _check_schema():
        with get_connection(settings.itdoc_db_path) as conn:
            from itdoc import validate_schema
            return validate_schema(conn)
    
    loop = asyncio.get_event_loop()
    schema_ok = await loop.run_in_executor(None, _check_schema)
    if not schema_ok:
        raise RuntimeError("Schemat it_doc_matrix.db niezgodny z oczekiwanym przez Warsztat")
    
    print(f"✓ itdoc library connected: {settings.itdoc_db_path}")
    
    yield  # Aplikacja działa
    
    # Shutdown: cleanup
```

---

## 6. Listy dozwolonych operacji (whitelist)

Poniższe operacje są **dozwolone** przez `ItdocConnector`:

| Operacja | itdoc function | SQL (read-only) | Stan aktualny |
|----------|---------------|-----------------|---------------|
| Znajdź wg standardu | `find_by_standard()` | SELECT z `doc_standard_mapping` | ⚠️ tabela nie istnieje → `[]` |
| Znajdź wg regulacji | `find_by_regulation()` | SELECT z `doc_regulation_mapping` | ⚠️ tabela nie istnieje → `[]` |
| Pobierz kontrakt | `get_contract()` | SELECT z `contracts` | ⚠️ tabela nie istnieje → `None` |
| Upstream deps | `rhythm_upstream()` | SELECT z `rhythm_edges` | ⚠️ tabela pusta → `[]` |
| Downstream deps | `rhythm_downstream()` | SELECT z `rhythm_edges` | ⚠️ tabela pusta → `[]` |
| Lista faz | Direct SQL SELECT | SELECT z `phases` (fallback z `document_phases`) | ✅ 24 fazy |
| Keyword search | `find_by_keyword()` | SELECT z `documents` + `document_phase_mapping` | ✅ 7 205 doc |
| Phase documents | `get_documents_by_phase()` | SELECT z `documents` + `document_phase_mapping` | ✅ 7 205 doc |
| Health check | `validate_schema()` | PRAGMA table_info() | ✅ |

**Zabronione** (nigdy nie implementować):

```python
# ❌ ZABRONIONE — poniższy kod NIE może istnieć w ItdocConnector
conn.execute("INSERT INTO docs ...")
conn.execute("UPDATE docs ...")
conn.execute("DELETE FROM docs ...")
shutil.copy(src, "generated_templates/...")
open("generated_templates/...", "w")
```

---

## 7. Testowanie integracji (patrz też dok. 14)

```python
# tests/integration/test_itdoc_connector.py

@pytest.mark.integration
async def test_find_by_standard_returns_docs(connector):
    """Weryfikuje że find_by_standard zwraca niepustą listę dla znanych standardów."""
    results = await connector.find_by_standard("ISO/IEC 27001")
    assert len(results) > 0
    assert all(r.doc_uid for r in results)

@pytest.mark.integration
async def test_connector_is_readonly(connector):
    """Weryfikuje że connector nie ma metod zapisu."""
    write_methods = [m for m in dir(connector) if any(
        w in m for w in ["insert", "update", "delete", "write", "save", "create"]
    )]
    assert write_methods == [], f"Znaleziono potencjalne metody zapisu: {write_methods}"

@pytest.mark.integration
async def test_get_contract_returns_none_for_stub(connector):
    """Weryfikuje że graceful None zwracane dla pustych kontraktów."""
    # Zakładamy że niektóre doc_uid mają puste kontrakty (znana właściwość biblioteki)
    result = await connector.get_contract("some_uid_with_empty_contract")
    assert result is None  # Nie rzuca wyjątku
```
