"""tests/test_seed_seeding.py

Testy integracyjne dla seed_document_types.py i seed_standards.py.
Wzorzec: tworzy tymczasowe SQLite, monkeypatchuje DB_PATH i sprawdza wynik INSERT.
"""

import sqlite3

import pytest

import scripts.seed_document_types as sdt
import scripts.seed_standards as ss


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


def _make_standards_db(path) -> sqlite3.Connection:
    """Tworzy minimalne SQLite z tabelami wymaganymi przez seed_standards."""
    conn = sqlite3.connect(str(path))
    conn.execute("""
        CREATE TABLE standards (
            standard_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            standard_code TEXT UNIQUE,
            standard_name TEXT,
            standard_name_en TEXT,
            version TEXT,
            description TEXT,
            applicable_industries TEXT,
            url TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE compliance_regulations (
            regulation_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            regulation_code TEXT UNIQUE,
            regulation_name TEXT,
            jurisdiction    TEXT,
            industry        TEXT,
            key_requirements TEXT,
            data_engineering_impact TEXT,
            penalty_info    TEXT
        )
    """)
    conn.commit()
    return conn


def _make_full_doctype_db(path) -> sqlite3.Connection:
    """Tworzy document_types z pełnym schematem (type_code + name_pl + name_en + ...)."""
    conn = sqlite3.connect(str(path))
    conn.execute("""
        CREATE TABLE document_types (
            type_code TEXT PRIMARY KEY,
            name_pl TEXT,
            name_en TEXT,
            type_description TEXT,
            typical_owner TEXT,
            typical_format TEXT,
            template_available INTEGER
        )
    """)
    conn.commit()
    return conn


def _make_partial_doctype_db(path) -> sqlite3.Connection:
    """Tworzy document_types bez name_en (testuje ścieżkę OR w kodzie)."""
    conn = sqlite3.connect(str(path))
    conn.execute("""
        CREATE TABLE document_types (
            type_code TEXT PRIMARY KEY,
            name_pl TEXT,
            template_available INTEGER,
            type_description TEXT,
            typical_owner TEXT,
            typical_format TEXT
        )
    """)
    conn.commit()
    return conn


def _make_minimal_doctype_db(path) -> sqlite3.Connection:
    """Tworzy document_types z tylko code/name/description (minimalna ścieżka)."""
    conn = sqlite3.connect(str(path))
    conn.execute("""
        CREATE TABLE document_types (
            code TEXT PRIMARY KEY,
            name TEXT,
            description TEXT
        )
    """)
    conn.commit()
    return conn


# ---------------------------------------------------------------------------
# seed_standards: seed_standards()
# ---------------------------------------------------------------------------


class TestSeedStandards:
    def test_inserts_expected_count(self, tmp_path):
        db_path = tmp_path / "test.db"
        conn = _make_standards_db(db_path)
        ss.seed_standards(conn)
        count = conn.execute("SELECT COUNT(*) FROM standards").fetchone()[0]
        assert count == len(ss.INTERNATIONAL_STANDARDS)
        assert count > 0
        conn.close()

    def test_standard_codes_are_nonempty(self, tmp_path):
        db_path = tmp_path / "test.db"
        conn = _make_standards_db(db_path)
        ss.seed_standards(conn)
        codes = conn.execute("SELECT standard_code FROM standards").fetchall()
        for row in codes:
            assert row[0] and row[0].strip()
        conn.close()

    def test_idempotent_via_delete_insert(self, tmp_path):
        db_path = tmp_path / "test.db"
        conn = _make_standards_db(db_path)
        ss.seed_standards(conn)
        count_first = conn.execute("SELECT COUNT(*) FROM standards").fetchone()[0]
        ss.seed_standards(conn)
        count_second = conn.execute("SELECT COUNT(*) FROM standards").fetchone()[0]
        assert count_first == count_second
        conn.close()

    def test_dry_run_does_not_commit(self, tmp_path):
        db_path = tmp_path / "test.db"
        conn = _make_standards_db(db_path)
        ss.seed_standards(conn, dry_run=True)
        # dry_run doesn't call conn.commit() — rows in current transaction but not persisted
        # Reopen to verify nothing persisted
        conn.rollback()
        count = conn.execute("SELECT COUNT(*) FROM standards").fetchone()[0]
        assert count == 0
        conn.close()

    def test_iso27001_is_present(self, tmp_path):
        db_path = tmp_path / "test.db"
        conn = _make_standards_db(db_path)
        ss.seed_standards(conn)
        row = conn.execute(
            "SELECT standard_code FROM standards WHERE standard_code = 'ISO/IEC 27001'"
        ).fetchone()
        assert row is not None
        conn.close()


# ---------------------------------------------------------------------------
# seed_standards: seed_regulations()
# ---------------------------------------------------------------------------


class TestSeedRegulations:
    def test_inserts_expected_count(self, tmp_path):
        db_path = tmp_path / "test.db"
        conn = _make_standards_db(db_path)
        ss.seed_regulations(conn)
        count = conn.execute("SELECT COUNT(*) FROM compliance_regulations").fetchone()[0]
        assert count == len(ss.POLISH_REGULATIONS)
        assert count > 0
        conn.close()

    def test_regulation_codes_unique(self, tmp_path):
        db_path = tmp_path / "test.db"
        conn = _make_standards_db(db_path)
        ss.seed_regulations(conn)
        codes = [r[0] for r in conn.execute("SELECT regulation_code FROM compliance_regulations")]
        assert len(codes) == len(set(codes)), "Kody regulacji muszą być unikalne"
        conn.close()

    def test_rodo_is_present(self, tmp_path):
        db_path = tmp_path / "test.db"
        conn = _make_standards_db(db_path)
        ss.seed_regulations(conn)
        row = conn.execute(
            "SELECT regulation_code FROM compliance_regulations WHERE regulation_code = 'UODO-PL'"
        ).fetchone()
        assert row is not None, "UODO-PL (RODO) regulacja powinna być w zestawie"
        conn.close()

    def test_idempotent_via_delete_insert(self, tmp_path):
        db_path = tmp_path / "test.db"
        conn = _make_standards_db(db_path)
        ss.seed_regulations(conn)
        count_first = conn.execute("SELECT COUNT(*) FROM compliance_regulations").fetchone()[0]
        ss.seed_regulations(conn)
        count_second = conn.execute("SELECT COUNT(*) FROM compliance_regulations").fetchone()[0]
        assert count_first == count_second
        conn.close()


# ---------------------------------------------------------------------------
# seed_standards: main()
# ---------------------------------------------------------------------------


class TestSeedStandardsMain:
    def test_main_seeds_both_tables(self, tmp_path, monkeypatch):
        db_path = tmp_path / "test.db"
        _make_standards_db(db_path).close()
        monkeypatch.setattr(ss, "DB_PATH", db_path)
        ss.main()
        conn = sqlite3.connect(str(db_path))
        std_count = conn.execute("SELECT COUNT(*) FROM standards").fetchone()[0]
        reg_count = conn.execute("SELECT COUNT(*) FROM compliance_regulations").fetchone()[0]
        conn.close()
        assert std_count == len(ss.INTERNATIONAL_STANDARDS)
        assert reg_count == len(ss.POLISH_REGULATIONS)


# ---------------------------------------------------------------------------
# seed_document_types: main() — różne schematy tabel
# ---------------------------------------------------------------------------


class TestSeedDocumentTypes:
    def test_full_schema_inserts_all(self, tmp_path, monkeypatch):
        """Ścieżka: type_code + name_pl + name_en + pełne kolumny."""
        db_path = tmp_path / "test.db"
        _make_full_doctype_db(db_path).close()
        monkeypatch.setattr(sdt, "DB_PATH", db_path)
        sdt.main()
        conn = sqlite3.connect(str(db_path))
        count = conn.execute("SELECT COUNT(*) FROM document_types").fetchone()[0]
        conn.close()
        assert count == len(sdt.DOCUMENT_TYPES)

    def test_partial_schema_inserts_all(self, tmp_path, monkeypatch):
        """Ścieżka: type_code + name_pl bez name_en."""
        db_path = tmp_path / "test.db"
        _make_partial_doctype_db(db_path).close()
        monkeypatch.setattr(sdt, "DB_PATH", db_path)
        sdt.main()
        conn = sqlite3.connect(str(db_path))
        count = conn.execute("SELECT COUNT(*) FROM document_types").fetchone()[0]
        conn.close()
        assert count == len(sdt.DOCUMENT_TYPES)

    def test_minimal_schema_inserts_all(self, tmp_path, monkeypatch):
        """Ścieżka: minimalna — tylko code/name/description."""
        db_path = tmp_path / "test.db"
        _make_minimal_doctype_db(db_path).close()
        monkeypatch.setattr(sdt, "DB_PATH", db_path)
        sdt.main()
        conn = sqlite3.connect(str(db_path))
        count = conn.execute("SELECT COUNT(*) FROM document_types").fetchone()[0]
        conn.close()
        assert count == len(sdt.DOCUMENT_TYPES)

    def test_idempotent_insert_or_ignore(self, tmp_path, monkeypatch):
        """Drugi import nie duplikuje wierszy — INSERT OR IGNORE."""
        db_path = tmp_path / "test.db"
        _make_full_doctype_db(db_path).close()
        monkeypatch.setattr(sdt, "DB_PATH", db_path)
        sdt.main()
        count_first = sqlite3.connect(str(db_path)).execute(
            "SELECT COUNT(*) FROM document_types"
        ).fetchone()[0]
        sdt.main()
        count_second = sqlite3.connect(str(db_path)).execute(
            "SELECT COUNT(*) FROM document_types"
        ).fetchone()[0]
        assert count_first == count_second

    def test_policy_type_code_present(self, tmp_path, monkeypatch):
        db_path = tmp_path / "test.db"
        _make_full_doctype_db(db_path).close()
        monkeypatch.setattr(sdt, "DB_PATH", db_path)
        sdt.main()
        conn = sqlite3.connect(str(db_path))
        row = conn.execute(
            "SELECT type_code, name_pl FROM document_types WHERE type_code='POLICY'"
        ).fetchone()
        conn.close()
        assert row is not None
        assert row[1] == "Polityka"

    def test_document_types_constant_has_20_entries(self):
        """DOCUMENT_TYPES musi mieć 20 typów — kontrakt dla innych testów."""
        assert len(sdt.DOCUMENT_TYPES) == 20
