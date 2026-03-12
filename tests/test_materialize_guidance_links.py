"""tests/test_materialize_guidance_links.py — testy jednostkowe dla materialize_guidance_links.py

Testy używają wyłącznie bazy in-memory (NIE rzeczywistej DB).
"""

import sqlite3
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.unit

# Dodaj katalog scripts/maintenance do sys.path aby móc importować skrypt bezpośrednio
_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts" / "maintenance"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from materialize_guidance_links import materialize, _ensure_schema  # noqa: E402


# ---------------------------------------------------------------------------
# Fixture
# ---------------------------------------------------------------------------

@pytest.fixture
def conn():
    c = sqlite3.connect(":memory:")
    c.execute(
        "CREATE TABLE doc_section_guidance ("
        "id INTEGER PRIMARY KEY, "
        "doc_title TEXT, "
        "section_title TEXT, "
        "guidance TEXT, "
        "standards_refs TEXT, "
        "regulations_refs TEXT)"
    )
    c.execute(
        "CREATE TABLE guidance_standard_links ("
        "guidance_id INTEGER, "
        "standard_code TEXT, "
        "PRIMARY KEY(guidance_id, standard_code))"
    )
    c.execute(
        "CREATE TABLE guidance_regulation_links ("
        "guidance_id INTEGER, "
        "regulation_code TEXT, "
        "PRIMARY KEY(guidance_id, regulation_code))"
    )
    c.commit()
    return c


# ---------------------------------------------------------------------------
# Testy
# ---------------------------------------------------------------------------

def test_single_standard_ref(conn):
    """Jeden wiersz z jednym standardem → 1 wiersz w guidance_standard_links."""
    conn.execute(
        "INSERT INTO doc_section_guidance (id, standards_refs) VALUES (1, ?)",
        ('["ISO 27001"]',),
    )
    conn.commit()

    result = materialize(conn)

    rows = conn.execute("SELECT * FROM guidance_standard_links").fetchall()
    assert len(rows) == 1
    assert rows[0] == (1, "ISO 27001")
    assert result["std_inserted"] == 1
    assert len(result["json_errors"]) == 0


def test_multiple_standards(conn):
    """Jeden wiersz z dwoma standardami → 2 wiersze."""
    conn.execute(
        "INSERT INTO doc_section_guidance (id, standards_refs) VALUES (1, ?)",
        ('["ISO 27001", "NIST CSF"]',),
    )
    conn.commit()

    result = materialize(conn)

    rows = conn.execute(
        "SELECT standard_code FROM guidance_standard_links ORDER BY standard_code"
    ).fetchall()
    codes = [r[0] for r in rows]
    assert codes == ["ISO 27001", "NIST CSF"]
    assert result["std_inserted"] == 2


def test_null_refs_skipped(conn):
    """NULL w standards_refs → 0 wierszy, brak błędów."""
    conn.execute(
        "INSERT INTO doc_section_guidance (id, standards_refs, regulations_refs) VALUES (1, NULL, NULL)",
    )
    conn.commit()

    result = materialize(conn)

    count = conn.execute("SELECT COUNT(*) FROM guidance_standard_links").fetchone()[0]
    assert count == 0
    assert len(result["json_errors"]) == 0


def test_empty_array_skipped(conn):
    """Pusty JSON array '[]' → 0 wierszy."""
    conn.execute(
        "INSERT INTO doc_section_guidance (id, standards_refs) VALUES (1, '[]')",
    )
    conn.commit()

    result = materialize(conn)

    count = conn.execute("SELECT COUNT(*) FROM guidance_standard_links").fetchone()[0]
    assert count == 0
    assert result["std_inserted"] == 0


def test_invalid_json_skipped(conn):
    """Nieprawidłowy JSON → 0 wierszy, json_errors == 1."""
    conn.execute(
        "INSERT INTO doc_section_guidance (id, standards_refs) VALUES (1, 'not valid json')",
    )
    conn.commit()

    result = materialize(conn)

    count = conn.execute("SELECT COUNT(*) FROM guidance_standard_links").fetchone()[0]
    assert count == 0
    assert len(result["json_errors"]) == 1


def test_regulation_refs(conn):
    """regulations_refs='["RODO"]' → 1 wiersz w guidance_regulation_links."""
    conn.execute(
        "INSERT INTO doc_section_guidance (id, regulations_refs) VALUES (1, ?)",
        ('["RODO"]',),
    )
    conn.commit()

    result = materialize(conn)

    rows = conn.execute("SELECT * FROM guidance_regulation_links").fetchall()
    assert len(rows) == 1
    assert rows[0] == (1, "RODO")
    assert result["reg_inserted"] == 1


def test_idempotent(conn):
    """Podwójne uruchomienie nie duplikuje wierszy (TRUNCATE + reinsert)."""
    conn.execute(
        "INSERT INTO doc_section_guidance (id, standards_refs, regulations_refs) VALUES (1, ?, ?)",
        ('["ISO 27001", "NIST CSF"]', '["RODO"]'),
    )
    conn.commit()

    # Pierwsze uruchomienie
    r1 = materialize(conn)
    std_count_1 = conn.execute("SELECT COUNT(*) FROM guidance_standard_links").fetchone()[0]
    reg_count_1 = conn.execute("SELECT COUNT(*) FROM guidance_regulation_links").fetchone()[0]

    # Drugie uruchomienie
    r2 = materialize(conn)
    std_count_2 = conn.execute("SELECT COUNT(*) FROM guidance_standard_links").fetchone()[0]
    reg_count_2 = conn.execute("SELECT COUNT(*) FROM guidance_regulation_links").fetchone()[0]

    assert std_count_1 == std_count_2 == 2
    assert reg_count_1 == reg_count_2 == 1
    assert r1["std_inserted"] == r2["std_inserted"]


def test_dry_run_does_not_write(conn):
    """--dry-run nie zapisuje nic do tabel."""
    conn.execute(
        "INSERT INTO doc_section_guidance (id, standards_refs) VALUES (1, ?)",
        ('["ISO 27001"]',),
    )
    conn.commit()

    result = materialize(conn, dry_run=True)

    count = conn.execute("SELECT COUNT(*) FROM guidance_standard_links").fetchone()[0]
    assert count == 0
    assert result["std_inserted"] == 1  # policzono, ale nie zapisano


def test_standards_only_skips_regulations(conn):
    """--standards-only nie wypełnia guidance_regulation_links."""
    conn.execute(
        "INSERT INTO doc_section_guidance (id, standards_refs, regulations_refs) VALUES (1, ?, ?)",
        ('["ISO 27001"]', '["RODO"]'),
    )
    conn.commit()

    result = materialize(conn, standards_only=True)

    std_count = conn.execute("SELECT COUNT(*) FROM guidance_standard_links").fetchone()[0]
    reg_count = conn.execute("SELECT COUNT(*) FROM guidance_regulation_links").fetchone()[0]
    assert std_count == 1
    assert reg_count == 0
    assert result["reg_inserted"] == 0
