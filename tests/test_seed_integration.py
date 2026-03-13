"""
test_seed_integration.py — Testy integracyjne: YAML → parser → INSERT → SQLite.

Cel: weryfikacja że pełny przepływ danych z YAML do DB działa poprawnie.
Każdy test używa izolowanej tymczasowej SQLite — zero wpływu na produkcyjną DB.

Hierarchia wg "Jak pisać testy.md": Krok 2 — Integration tests.
"""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# Fixtures: schematy tabel
# ---------------------------------------------------------------------------

@pytest.fixture
def base_dicts_db(tmp_path) -> Path:
    """Tymczasowa DB ze schematem dla wszystkich 6 słowników bazowych."""
    db = tmp_path / "seed_test.db"
    conn = sqlite3.connect(str(db))
    conn.executescript("""
        CREATE TABLE roles (
            role_code TEXT PRIMARY KEY,
            role_name_pl TEXT,
            role_name_en TEXT,
            description TEXT
        );
        CREATE TABLE phases (
            phase_number INTEGER PRIMARY KEY,
            phase_name_pl TEXT,
            phase_name_en TEXT,
            phase_category TEXT,
            is_iterative INTEGER,
            phase_description TEXT
        );
        CREATE TABLE industries (
            industry_code TEXT PRIMARY KEY,
            name_pl TEXT,
            name_en TEXT,
            category TEXT
        );
        CREATE TABLE document_categories (
            category_code TEXT PRIMARY KEY,
            category_name_pl TEXT,
            category_name_en TEXT,
            description TEXT,
            color_hex TEXT
        );
        CREATE TABLE relationship_types (
            rel_type_code TEXT PRIMARY KEY,
            rel_type_name_pl TEXT,
            rel_type_name_en TEXT,
            is_bidirectional INTEGER,
            description TEXT
        );
        CREATE TABLE quality_dimensions (
            dimension TEXT PRIMARY KEY,
            name TEXT,
            description TEXT,
            measurement_method TEXT,
            example_checks TEXT,
            good_threshold TEXT,
            target_threshold TEXT,
            tools TEXT
        );
    """)
    conn.commit()
    conn.close()
    return db


@pytest.fixture
def catalog_db(tmp_path) -> Path:
    """Tymczasowa DB ze schematem dla standards_catalog + tabela standards."""
    db = tmp_path / "catalog_test.db"
    conn = sqlite3.connect(str(db))
    conn.executescript("""
        CREATE TABLE standards (
            standard_code TEXT PRIMARY KEY,
            standard_name TEXT
        );
        CREATE TABLE standards_catalog (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            standard_code TEXT NOT NULL,
            doc_type_id   TEXT NOT NULL UNIQUE,
            doc_title     TEXT NOT NULL,
            is_required   INTEGER NOT NULL DEFAULT 1,
            category      TEXT,
            source_url    TEXT,
            notes         TEXT,
            created_at    TEXT DEFAULT (datetime('now'))
        );
        CREATE INDEX idx_sc_standard ON standards_catalog(standard_code);
    """)
    conn.commit()
    conn.close()
    return db


# ===========================================================================
# seed_base_dicts — integracja YAML → SQLite
# ===========================================================================

class TestSeedBaseDictsIntegration:
    """Integracja: YAML loaders → INSERT → SQLite."""

    def _run_seed(self, db_path: Path, monkeypatch) -> None:
        """Uruchamia seed_base_dicts.main() z podmienioną ścieżką DB."""
        import scripts.seed_base_dicts as sbd
        monkeypatch.setattr(sbd, "DB_PATH", db_path)
        sbd.main()

    def test_roles_table_seeded(self, base_dicts_db, monkeypatch):
        """Tabela roles ma ≥ 40 wierszy po seed."""
        self._run_seed(base_dicts_db, monkeypatch)
        conn = sqlite3.connect(str(base_dicts_db))
        count = conn.execute("SELECT COUNT(*) FROM roles").fetchone()[0]
        conn.close()
        assert count >= 40, f"Oczekiwano ≥ 40 ról, mamy {count}"

    def test_phases_table_seeded(self, base_dicts_db, monkeypatch):
        """Tabela phases ma ≥ 23 wierszy po seed."""
        self._run_seed(base_dicts_db, monkeypatch)
        conn = sqlite3.connect(str(base_dicts_db))
        count = conn.execute("SELECT COUNT(*) FROM phases").fetchone()[0]
        conn.close()
        assert count >= 23

    def test_industries_table_seeded(self, base_dicts_db, monkeypatch):
        """Tabela industries ma ≥ 30 wierszy po seed."""
        self._run_seed(base_dicts_db, monkeypatch)
        conn = sqlite3.connect(str(base_dicts_db))
        count = conn.execute("SELECT COUNT(*) FROM industries").fetchone()[0]
        conn.close()
        assert count >= 30

    def test_document_categories_seeded(self, base_dicts_db, monkeypatch):
        """Tabela document_categories ma ≥ 15 wierszy po seed."""
        self._run_seed(base_dicts_db, monkeypatch)
        conn = sqlite3.connect(str(base_dicts_db))
        count = conn.execute("SELECT COUNT(*) FROM document_categories").fetchone()[0]
        conn.close()
        assert count >= 15

    def test_relationship_types_seeded(self, base_dicts_db, monkeypatch):
        """Tabela relationship_types ma ≥ 10 wierszy po seed."""
        self._run_seed(base_dicts_db, monkeypatch)
        conn = sqlite3.connect(str(base_dicts_db))
        count = conn.execute("SELECT COUNT(*) FROM relationship_types").fetchone()[0]
        conn.close()
        assert count >= 10

    def test_quality_dimensions_seeded(self, base_dicts_db, monkeypatch):
        """Tabela quality_dimensions ma ≥ 8 wierszy po seed."""
        self._run_seed(base_dicts_db, monkeypatch)
        conn = sqlite3.connect(str(base_dicts_db))
        count = conn.execute("SELECT COUNT(*) FROM quality_dimensions").fetchone()[0]
        conn.close()
        assert count >= 8

    def test_roles_role_code_not_null(self, base_dicts_db, monkeypatch):
        """role_code nie może być NULL — klucz główny."""
        self._run_seed(base_dicts_db, monkeypatch)
        conn = sqlite3.connect(str(base_dicts_db))
        nulls = conn.execute("SELECT COUNT(*) FROM roles WHERE role_code IS NULL").fetchone()[0]
        conn.close()
        assert nulls == 0

    def test_seed_idempotent(self, base_dicts_db, monkeypatch):
        """Dwa wywołania seed nie duplikują wierszy (INSERT OR IGNORE)."""
        self._run_seed(base_dicts_db, monkeypatch)
        conn = sqlite3.connect(str(base_dicts_db))
        count1 = conn.execute("SELECT COUNT(*) FROM roles").fetchone()[0]
        conn.close()

        self._run_seed(base_dicts_db, monkeypatch)
        conn = sqlite3.connect(str(base_dicts_db))
        count2 = conn.execute("SELECT COUNT(*) FROM roles").fetchone()[0]
        conn.close()

        assert count1 == count2, (
            f"Ponowny seed nie może duplikować: {count1} != {count2}"
        )

    def test_all_6_tables_populated_in_single_run(self, base_dicts_db, monkeypatch):
        """Jeden wywołanie seed_base_dicts zasila wszystkie 6 tabel."""
        self._run_seed(base_dicts_db, monkeypatch)
        conn = sqlite3.connect(str(base_dicts_db))
        tables = {
            "roles": 40,
            "phases": 23,
            "industries": 30,
            "document_categories": 15,
            "relationship_types": 10,
            "quality_dimensions": 8,
        }
        for table, min_count in tables.items():
            count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]  # noqa: S608
            assert count >= min_count, f"{table}: oczekiwano ≥ {min_count}, mamy {count}"
        conn.close()


# ===========================================================================
# build_standards_catalog — integracja YAML → SQLite
# ===========================================================================

class TestBuildStandardsCatalogIntegration:
    """Integracja: standards_catalog.yaml → load_catalog() → SQLite."""

    def _run_catalog(self, db_path: Path) -> None:
        """Wywołuje build_standards_catalog.main() z --db tmp_path --replace."""
        orig_argv = sys.argv[:]
        sys.argv = ["build_standards_catalog.py", "--db", str(db_path), "--replace"]
        try:
            from scripts.build_standards_catalog import main
            main()
        finally:
            sys.argv = orig_argv

    def test_catalog_inserted(self, catalog_db):
        """295 wpisów katalogu standardów trafia do DB."""
        self._run_catalog(catalog_db)
        conn = sqlite3.connect(str(catalog_db))
        count = conn.execute("SELECT COUNT(*) FROM standards_catalog").fetchone()[0]
        conn.close()
        assert count >= 295, f"Oczekiwano ≥ 295 wpisów, mamy {count}"

    def test_all_44_standards_represented(self, catalog_db):
        """Każdy z 44 standardów ma ≥ 1 wpis w katalogu."""
        self._run_catalog(catalog_db)
        conn = sqlite3.connect(str(catalog_db))
        count = conn.execute(
            "SELECT COUNT(DISTINCT standard_code) FROM standards_catalog"
        ).fetchone()[0]
        conn.close()
        assert count >= 44

    def test_doc_type_id_unique(self, catalog_db):
        """doc_type_id jest UNIQUE w tabeli standards_catalog."""
        self._run_catalog(catalog_db)
        conn = sqlite3.connect(str(catalog_db))
        duplicates = conn.execute("""
            SELECT doc_type_id, COUNT(*) AS cnt
            FROM standards_catalog
            GROUP BY doc_type_id
            HAVING cnt > 1
        """).fetchall()
        conn.close()
        assert not duplicates, f"Zduplikowane doc_type_id: {duplicates[:5]}"

    def test_is_required_is_0_or_1(self, catalog_db):
        """is_required musi być 0 lub 1 (nie NULL, nie inny)."""
        self._run_catalog(catalog_db)
        conn = sqlite3.connect(str(catalog_db))
        invalid = conn.execute("""
            SELECT COUNT(*) FROM standards_catalog
            WHERE is_required NOT IN (0, 1)
        """).fetchone()[0]
        conn.close()
        assert invalid == 0

    def test_replace_flag_no_duplicates(self, catalog_db):
        """Drugi wywołanie z --replace nie duplikuje wpisów."""
        self._run_catalog(catalog_db)
        conn = sqlite3.connect(str(catalog_db))
        count1 = conn.execute("SELECT COUNT(*) FROM standards_catalog").fetchone()[0]
        conn.close()

        self._run_catalog(catalog_db)
        conn = sqlite3.connect(str(catalog_db))
        count2 = conn.execute("SELECT COUNT(*) FROM standards_catalog").fetchone()[0]
        conn.close()

        assert count1 == count2, f"Po --replace duplikaty: {count1} != {count2}"

    def test_create_table_and_load_catalog_directly(self, tmp_path):
        """Testuje create_table() + load_catalog() bez main(), z czystą DB."""
        db = tmp_path / "direct_test.db"
        conn = sqlite3.connect(str(db))

        from scripts.build_standards_catalog import create_table, load_catalog
        create_table(conn)

        stats = load_catalog(conn, replace=False)

        total = sum(stats.values())
        assert total >= 295, f"load_catalog() musi zwrócić ≥ 295 wstawionych, mamy {total}"
        assert "ISO/IEC 27001" in stats
        assert stats["ISO/IEC 27001"] > 0
        conn.close()
