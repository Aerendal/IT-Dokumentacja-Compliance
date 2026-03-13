"""
test_run_apis.py — Unit i integracyjne testy dla funkcji run() wydzielonych
z CLI w refaktorze Fazy 3B.

Cel: weryfikacja że run() działa niezależnie od CLI (testowalność bez CLI).
Testujemy z realną SQLite in-memory / tmp_db.

Hierarchia wg "Jak pisać testy.md": Krok 1 (unit) + Krok 2 (integration).
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# Fixture: minimalna DB
# ---------------------------------------------------------------------------

@pytest.fixture
def tmp_db(tmp_path) -> Path:
    """Tymczasowa SQLite z minimalnym schematem potrzebnym do testów."""
    db = tmp_path / "test.db"
    conn = sqlite3.connect(str(db))
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS docs (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            path    TEXT NOT NULL,
            title   TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS standards_catalog (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            standard_code TEXT NOT NULL,
            doc_type_id   TEXT NOT NULL,
            doc_title     TEXT NOT NULL,
            category      TEXT,
            is_required   INTEGER DEFAULT 1
        );
        CREATE TABLE IF NOT EXISTS doc_standard_mapping (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            doc_path      TEXT,
            standard_code TEXT,
            confidence    TEXT
        );
        CREATE TABLE IF NOT EXISTS template_violations (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            severity TEXT
        );
    """)
    conn.commit()
    conn.close()
    return db


@pytest.fixture
def tmp_db_with_data(tmp_db) -> Path:
    """DB z kilkoma wierszami danych — do testów analizy luk."""
    conn = sqlite3.connect(str(tmp_db))
    # Kilka dokumentów
    conn.executemany(
        "INSERT INTO docs (path, title) VALUES (?, ?)",
        [
            ("docs/security_policy.md", "Security Policy"),
            ("docs/incident_response.md", "Incident Response Plan"),
            ("docs/risk_assessment.md", "Risk Assessment Report"),
        ],
    )
    # Kilka wpisów katalogu
    conn.executemany(
        "INSERT INTO standards_catalog (standard_code, doc_type_id, doc_title, is_required) VALUES (?,?,?,?)",
        [
            ("ISO/IEC 27001", "isms_scope", "ISMS Scope Document", 1),
            ("ISO/IEC 27001", "risk_assessment", "Risk Assessment Report", 1),
            ("NIST CSF", "incident_response", "Incident Response Plan", 1),
        ],
    )
    conn.commit()
    conn.close()
    return tmp_db


@pytest.fixture
def tmp_db_with_mappings(tmp_db_with_data) -> Path:
    """DB z danymi + mapowaniami standardów."""
    conn = sqlite3.connect(str(tmp_db_with_data))
    conn.executemany(
        "INSERT INTO doc_standard_mapping (doc_path, standard_code, confidence) VALUES (?,?,?)",
        [
            ("docs/risk_assessment.md", "ISO/IEC 27001", "high"),
            ("docs/incident_response.md", "NIST CSF", "high"),
        ],
    )
    conn.commit()
    conn.close()
    return tmp_db_with_data


# ===========================================================================
# gap_analysis.run()
# ===========================================================================

class TestGapAnalysisRun:
    """Testy dla gap_analysis.run() — testowalne bez CLI."""

    def test_run_empty_db_no_exception(self, tmp_db):
        """run() z pustą DB nie rzuca wyjątku."""
        from scripts.gap_analysis import run
        run(tmp_db, verbose=False)  # nie powinno rzucić

    def test_run_creates_gap_analysis_table(self, tmp_db):
        """run() tworzy tabelę gap_analysis jeśli nie istnieje."""
        from scripts.gap_analysis import run
        run(tmp_db, verbose=False)
        conn = sqlite3.connect(str(tmp_db))
        tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
        assert "gap_analysis" in tables
        conn.close()

    def test_run_with_catalog_data_populates_gap_analysis(self, tmp_db_with_data):
        """run() z danymi wstawia wyniki do gap_analysis."""
        from scripts.gap_analysis import run
        run(tmp_db_with_data, verbose=False)
        conn = sqlite3.connect(str(tmp_db_with_data))
        count = conn.execute("SELECT COUNT(*) FROM gap_analysis").fetchone()[0]
        conn.close()
        assert count > 0, "gap_analysis musi zawierać wyniki po run()"

    def test_run_marks_matched_doc_as_present(self, tmp_db_with_mappings):
        """Dokument pasujący do katalogu ma status 'present'."""
        from scripts.gap_analysis import run
        run(tmp_db_with_mappings, verbose=False)
        conn = sqlite3.connect(str(tmp_db_with_mappings))
        present_count = conn.execute(
            "SELECT COUNT(*) FROM gap_analysis WHERE status = 'present'"
        ).fetchone()[0]
        conn.close()
        assert present_count > 0, "Co najmniej jeden dokument musi być oznaczony jako 'present'"

    def test_run_idempotent(self, tmp_db_with_data):
        """Dwa wywołania run() nie powodują duplikatów w gap_analysis."""
        from scripts.gap_analysis import run
        run(tmp_db_with_data, verbose=False)
        conn = sqlite3.connect(str(tmp_db_with_data))
        count1 = conn.execute("SELECT COUNT(*) FROM gap_analysis").fetchone()[0]
        conn.close()

        run(tmp_db_with_data, verbose=False)  # drugie wywołanie
        conn = sqlite3.connect(str(tmp_db_with_data))
        count2 = conn.execute("SELECT COUNT(*) FROM gap_analysis").fetchone()[0]
        conn.close()

        assert count1 == count2, (
            f"Ponowne run() nie może duplikować wierszy: {count1} != {count2}"
        )

    def test_run_nonexistent_db_raises(self, tmp_path):
        """run() z nieistniejącym plikiem DB rzuca FileNotFoundError."""
        from scripts.gap_analysis import run
        nonexistent = tmp_path / "nie_ma_mnie.db"
        with pytest.raises(FileNotFoundError):
            run(nonexistent, verbose=False)


# ===========================================================================
# compliance_check.get_db_stats()
# ===========================================================================

class TestGetDbStats:
    """Testy dla compliance_check.get_db_stats() — testowalne bez CLI."""

    def test_empty_db_returns_zero_stats(self, tmp_db):
        """Pusta DB → stats z zerami, bez wyjątku."""
        from scripts.compliance_check import get_db_stats
        result = get_db_stats(tmp_db)
        assert isinstance(result, dict)
        assert result["total_mappings"] == 0
        assert result["null_confidence"] == 0
        assert result["error_violations"] == 0
        assert result["warning_violations"] == 0

    def test_returns_required_keys(self, tmp_db):
        """Wynik zawiera oczekiwane klucze."""
        from scripts.compliance_check import get_db_stats
        result = get_db_stats(tmp_db)
        assert "total_mappings" in result
        assert "null_confidence" in result
        assert "error_violations" in result
        assert "warning_violations" in result

    def test_counts_mappings_correctly(self, tmp_db):
        """Zlicza wiersze z doc_standard_mapping."""
        conn = sqlite3.connect(str(tmp_db))
        conn.executemany(
            "INSERT INTO doc_standard_mapping (doc_path, standard_code, confidence) VALUES (?,?,?)",
            [
                ("a.md", "ISO/IEC 27001", "high"),
                ("b.md", "NIST CSF", None),
            ],
        )
        conn.commit()
        conn.close()

        from scripts.compliance_check import get_db_stats
        result = get_db_stats(tmp_db)
        assert result["total_mappings"] == 2
        assert result["null_confidence"] == 1  # b.md ma confidence=None

    def test_counts_violations_by_severity(self, tmp_db):
        """Zlicza template_violations wg severity."""
        conn = sqlite3.connect(str(tmp_db))
        conn.executemany(
            "INSERT INTO template_violations (severity) VALUES (?)",
            [("ERROR",), ("ERROR",), ("WARNING",)],
        )
        conn.commit()
        conn.close()

        from scripts.compliance_check import get_db_stats
        result = get_db_stats(tmp_db)
        assert result["error_violations"] == 2
        assert result["warning_violations"] == 1

    def test_missing_table_handled_gracefully(self, tmp_path):
        """DB bez tabeli doc_standard_mapping → zwraca 0, nie rzuca."""
        # Tworzy DB z tylko template_violations (brak doc_standard_mapping)
        db = tmp_path / "minimal.db"
        conn = sqlite3.connect(str(db))
        conn.execute("CREATE TABLE template_violations (id INTEGER PRIMARY KEY, severity TEXT)")
        conn.commit()
        conn.close()

        from scripts.compliance_check import get_db_stats
        result = get_db_stats(db)
        assert result["total_mappings"] == 0  # brak tabeli → 0, nie wyjątek

    def test_nonexistent_db_raises(self, tmp_path):
        """Nieistniejący plik DB → FileNotFoundError."""
        from scripts.compliance_check import get_db_stats
        with pytest.raises(FileNotFoundError):
            get_db_stats(tmp_path / "nie_ma_mnie.db")
