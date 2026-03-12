"""tests/test_db_module.py — testy jednostkowe modułu itdoc/db.py.

Test Scope Matrix (TESTING_METHODOLOGY):
  Module:   db.py
  RT:       2.10  (C=2 R=2 K=2 P=4 D=2 S=1 F=0)
  Class:    medium
  UT_min:   20  (2·B=2·10, PF=3)
  IT_min:   6   (DEP=1 → (1+1)·ceil(2.1)=6)
  CT_min:   6   (EP=3 · ceil(2.1/2)=2 → 6)
  Coverage: ≥58%

Aktualny stan (moduł db.py bezpośrednio): 0 unit testów → gap=20.
Poniższe testy używają in-memory DB lub tmpfile — bez dostępu do real DB.
"""

import sqlite3
from pathlib import Path

import pytest

from itdoc.db import (
    _DEFAULT_DB,
    _REQUIRED_TABLES,
    check_link_resolution_coverage,
    get_connection,
    open_connection,
    validate_schema,
)
from itdoc.exceptions import SchemaError


# ─── Fixtures ──────────────────────────────────────────────────────────────


@pytest.fixture()
def tmp_db(tmp_path):
    """Tymczasowy plik SQLite z minimalnym schematem."""
    db_path = tmp_path / "test.db"
    conn = sqlite3.connect(str(db_path))
    conn.executescript("""
        CREATE TABLE _schema_version (version TEXT);
        INSERT INTO _schema_version VALUES ('1.0.0');
        CREATE TABLE docs (doc_uid TEXT, title TEXT, path TEXT, title_norm TEXT,
                           origin TEXT, created_at_utc TEXT, updated_at_utc TEXT);
        INSERT INTO docs VALUES ('UID1','Test','core/t.md','test','core','2026','2026');
        CREATE TABLE sections (section_uid TEXT, doc_uid TEXT, heading_text TEXT,
            heading_norm TEXT, heading_level INTEGER, heading_path TEXT, anchor TEXT,
            ordinal INTEGER, status TEXT, text_fingerprint_sha256 TEXT,
            start_line INTEGER, end_line INTEGER);
        CREATE TABLE standards (standard_id INTEGER, standard_code TEXT, standard_name TEXT,
            standard_name_en TEXT, description TEXT, version TEXT, url TEXT, applicable_industries TEXT);
        INSERT INTO standards VALUES (1,'ISO/IEC 27001','Norma','IS','','2022','','');
        CREATE TABLE compliance_regulations (id INTEGER, regulation_code TEXT,
            regulation_name TEXT, jurisdiction TEXT, industry TEXT,
            key_requirements TEXT, penalty_info TEXT, data_engineering_impact TEXT);
        INSERT INTO compliance_regulations VALUES (1,'UODO-PL','Ustawa','PL','','','','');
        CREATE TABLE content_links (id INTEGER, from_doc TEXT, to_doc TEXT, link_type TEXT);
        INSERT INTO content_links VALUES (1,'a','b','requires');
        CREATE TABLE content_links_resolved (id INTEGER, content_link_id INTEGER,
            from_kind TEXT, from_uid TEXT, to_kind TEXT, to_uid TEXT, link_type TEXT,
            direction TEXT, rationale TEXT, strength TEXT, resolution_method TEXT,
            resolution_confidence REAL, notes TEXT);
        INSERT INTO content_links_resolved VALUES (1,1,'doc','UID1','doc','UID2','requires','forward','','required','explicit',1.0,'');
        CREATE TABLE rhythm_edges (edge_id INTEGER, from_node TEXT, to_node TEXT,
            rhythm_type TEXT, weight REAL, conditions TEXT, version_range TEXT, notes TEXT);
        INSERT INTO rhythm_edges VALUES (1,'UID1','UID2','triggers',0.9,'','','');
        CREATE TABLE contracts (contract_id INTEGER, scope_kind TEXT, scope_uid TEXT,
            version TEXT, inputs_json TEXT, outputs_json TEXT, gates_json TEXT,
            impact_json TEXT, owner TEXT, notes TEXT, created_at_utc TEXT, updated_at_utc TEXT);
        INSERT INTO contracts VALUES (1,'doc','UID1','1.0','[]','[]','[]','{}','x','','2026','2026');
        CREATE TABLE flags (id INTEGER, doc_uid TEXT, version TEXT, branch_id INTEGER, access_mask INTEGER);
        INSERT INTO flags VALUES (1,'UID1','1.0.0',1,0);
        INSERT INTO sections VALUES
            ('SEC1','UID1','Cel dokumentu','cel dokumentu',2,'cel-dokumentu','cel-dokumentu',
             1,'filled','abc123',10,20);
    """)
    conn.close()
    return db_path


@pytest.fixture()
def empty_db(tmp_path):
    """Tymczasowy plik SQLite całkowicie pusty (brak tabel)."""
    db_path = tmp_path / "empty.db"
    sqlite3.connect(str(db_path)).close()
    return db_path


# ─── get_connection ─────────────────────────────────────────────────────────


class TestGetConnection:
    """CT-DB-01 … CT-DB-06 — kontrakt funkcji get_connection()."""

    def test_returns_connection(self, tmp_db):
        conn = open_connection(tmp_db)
        assert conn is not None
        conn.close()

    def test_row_factory_set(self, tmp_db):
        conn = open_connection(tmp_db)
        row = conn.execute("SELECT version FROM _schema_version").fetchone()
        assert hasattr(row, "keys"), "row_factory powinno być sqlite3.Row"
        conn.close()

    def test_raises_filenotfound_when_missing(self, tmp_path):
        with pytest.raises(FileNotFoundError):
            with get_connection(tmp_path / "nonexistent.db"):
                pass

    def test_is_context_manager(self, tmp_db):
        """get_connection() działa jako context manager — automatyczne zamknięcie."""
        with get_connection(tmp_db) as conn:
            assert conn is not None
            row = conn.execute("SELECT version FROM _schema_version").fetchone()
            assert row is not None

    def test_default_db_path_defined(self):
        assert _DEFAULT_DB is not None
        assert isinstance(_DEFAULT_DB, Path)

    def test_accepts_path_object(self, tmp_db):
        conn = open_connection(tmp_db)
        conn.close()

    def test_accepts_string_path(self, tmp_db):
        conn = open_connection(str(tmp_db))
        conn.close()

    def test_wal_mode_set(self, tmp_db):
        conn = open_connection(tmp_db)
        mode = conn.execute("PRAGMA journal_mode").fetchone()[0]
        conn.close()
        assert mode in ("wal", "memory")  # in-mem może zwrócić "memory"


# ─── validate_schema ────────────────────────────────────────────────────────


class TestValidateSchema:
    """CT-DB-07 … CT-DB-14 — kontrakt funkcji validate_schema()."""

    def test_returns_list(self, tmp_db):
        conn = open_connection(tmp_db)
        result = validate_schema(conn)
        conn.close()
        assert isinstance(result, list)

    def test_full_schema_no_errors(self, tmp_db):
        conn = open_connection(tmp_db)
        errors = validate_schema(conn)
        conn.close()
        assert errors == []

    def test_missing_table_reported(self, empty_db):
        conn = open_connection(empty_db)
        errors = validate_schema(conn)
        conn.close()
        # Każda wymagana tabela powinna być wymieniona jako błąd
        assert len(errors) >= len(_REQUIRED_TABLES)

    def test_error_strings_are_descriptive(self, empty_db):
        conn = open_connection(empty_db)
        errors = validate_schema(conn)
        conn.close()
        for err in errors:
            assert isinstance(err, str)
            assert len(err) > 5  # Nie pusty string

    def test_empty_table_reported(self, tmp_path):
        """Tabela obecna ale pusta → błąd."""
        db_path = tmp_path / "partial.db"
        conn = sqlite3.connect(str(db_path))
        # Stwórz wszystkie wymagane tabele, ale docs niech będzie pusta
        for t in _REQUIRED_TABLES:
            conn.execute(f"CREATE TABLE [{t}] (id INTEGER)")
        conn.commit()
        conn.close()

        conn = open_connection(db_path)
        errors = validate_schema(conn)
        conn.close()
        assert any("pusta" in e.lower() or "empty" in e.lower() or t in e
                   for e in errors for t in _REQUIRED_TABLES), \
            f"Oczekiwano błędu o pustej tabeli, got: {errors}"

    def test_validate_schema_idempotent(self, tmp_db):
        """Dwukrotne wywołanie zwraca ten sam wynik."""
        conn = open_connection(tmp_db)
        r1 = validate_schema(conn)
        r2 = validate_schema(conn)
        conn.close()
        assert r1 == r2

    # Punkt rozszerzenia (pro-funkcjonalna mitygacja)
    def test_error_list_is_mutable(self, tmp_db):
        """Lista błędów powinna być modyfikowalna (możliwość hookowania)."""
        conn = open_connection(tmp_db)
        errors = validate_schema(conn)
        conn.close()
        errors.append("custom_check_failed")  # nie powinno rzucić
        assert "custom_check_failed" in errors


# ─── check_link_resolution_coverage ────────────────────────────────────────


class TestCheckLinkResolutionCoverage:
    """CT-DB-15 … CT-DB-20 — kontrakt check_link_resolution_coverage()."""

    def test_returns_float(self, tmp_db):
        conn = open_connection(tmp_db)
        result = check_link_resolution_coverage(conn)
        conn.close()
        assert isinstance(result, float)

    def test_full_coverage_returns_1(self, tmp_db):
        """1 link → 1 resolved → coverage = 1.0."""
        conn = open_connection(tmp_db)
        cov = check_link_resolution_coverage(conn)
        conn.close()
        assert cov == 1.0

    def test_partial_coverage(self, tmp_path):
        db_path = tmp_path / "partial.db"
        conn_rw = sqlite3.connect(str(db_path))
        conn_rw.executescript("""
            CREATE TABLE content_links (id INTEGER);
            INSERT INTO content_links VALUES (1),(2),(3);
            CREATE TABLE content_links_resolved (id INTEGER);
            INSERT INTO content_links_resolved VALUES (1);
        """)
        conn_rw.close()

        conn = open_connection(db_path)
        cov = check_link_resolution_coverage(conn)
        conn.close()
        assert abs(cov - 1/3) < 0.001

    def test_zero_links_returns_zero(self, tmp_path):
        db_path = tmp_path / "zero.db"
        conn_rw = sqlite3.connect(str(db_path))
        conn_rw.executescript("""
            CREATE TABLE content_links (id INTEGER);
            CREATE TABLE content_links_resolved (id INTEGER);
        """)
        conn_rw.close()

        conn = open_connection(db_path)
        cov = check_link_resolution_coverage(conn)
        conn.close()
        assert cov == 0.0

    def test_raises_schema_error_when_table_missing(self, empty_db):
        conn = open_connection(empty_db)
        with pytest.raises(SchemaError):
            check_link_resolution_coverage(conn)
        conn.close()

    def test_result_in_range_zero_to_one(self, tmp_db):
        conn = open_connection(tmp_db)
        cov = check_link_resolution_coverage(conn)
        conn.close()
        assert 0.0 <= cov <= 1.0


# ─── EP Extensions: on_error= callback ────────────────────────────────────────


class TestEPValidateSchemaOnError:
    """EP: validate_schema(conn, on_error=) — callback wywoływany dla każdego błędu."""

    def test_on_error_called_for_missing_table(self, tmp_db):
        """on_error jest wywoływany gdy tabela brakuje."""
        import sqlite3
        conn = sqlite3.connect(":memory:")
        conn.row_factory = sqlite3.Row
        # Tylko jedna tabela — pozostałe brakują
        conn.execute("CREATE TABLE docs (id INTEGER)")
        conn.execute("INSERT INTO docs VALUES (1)")

        collected = []
        errors = validate_schema(conn, on_error=collected.append)
        conn.close()

        assert len(collected) > 0
        assert collected == errors  # callback i wynik są spójne

    def test_on_error_not_called_when_schema_ok(self, tmp_db):
        """on_error NIE jest wywoływany gdy schemat jest OK."""
        from itdoc.db import _open_connection
        conn = _open_connection(tmp_db)
        collected = []
        errors = validate_schema(conn, on_error=collected.append)
        conn.close()

        assert errors == []
        assert collected == []

    def test_on_error_none_still_returns_errors(self):
        """on_error=None (domyślny) — błędy są zwracane normalnie."""
        import sqlite3
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE docs (id INTEGER)")
        conn.execute("INSERT INTO docs VALUES (1)")

        errors = validate_schema(conn, on_error=None)
        conn.close()
        assert len(errors) > 0

    def test_on_error_receives_string_messages(self, tmp_db):
        """Każda wiadomość przekazana do on_error jest stringiem."""
        import sqlite3
        conn = sqlite3.connect(":memory:")
        conn.execute("CREATE TABLE docs (id INTEGER)")
        conn.execute("INSERT INTO docs VALUES (1)")

        received = []
        validate_schema(conn, on_error=received.append)
        conn.close()

        for msg in received:
            assert isinstance(msg, str), f"on_error otrzymał non-string: {msg!r}"
