"""tests/conftest.py — wspólne fixtures dla wszystkich testów.

Fixtures:
  db_conn            — in-memory SQLite z minimalnym schematem (unit tests)
  real_db_conn       — alias: real_legacy_db_conn (kompatybilność wsteczna)
  real_legacy_db_conn — połączenie z reports/it_doc_matrix.db (skip jeśli brak lub zły profil)
  real_current_db_conn — połączenie z reports/it_doc_matrix_clean.db (skip jeśli brak/zły profil)
  sample_template_path — ścieżka do istniejącego szablonu core/ (skip jeśli brak)
  templates_root     — ścieżka do generated_templates/ (skip jeśli brak)
  core_dir           — ścieżka do generated_templates/core/ (skip jeśli brak)
  satellite_dir      — ścieżka do generated_templates/satellite/ (skip jeśli brak)
  alignment_log_path — ścieżka do reports/alignment_log.csv (skip jeśli brak)
  repo_root          — katalog główny repo (Path)
"""

import sqlite3
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).parent.parent
_DB_PATH = _REPO_ROOT / "reports" / "it_doc_matrix.db"
_CLEAN_DB_PATH = _REPO_ROOT / "reports" / "it_doc_matrix_clean.db"
_CORE_DIR = _REPO_ROOT / "generated_templates" / "core"
_SAT_DIR = _REPO_ROOT / "generated_templates" / "satellite"
_ALIGNMENT_LOG = _REPO_ROOT / "reports" / "alignment_log.csv"


def _require_db_profile(path: Path, expected: str) -> sqlite3.Connection:
    """Otwiera DB i sprawdza profil. Skip jeśli brak pliku lub zły profil.

    TECHNICAL DEBT NOTE:
    Integration tests require two real SQLite databases (legacy-runtime and
    current-snapshot profile) that are not committed to the repo (gitignored,
    too large / generated). This shim is the intentional skip gate.

    Safe to remove when: a lightweight reproducible DB fixture replaces the
    real runtime assets for integration testing.
    Owner: repo maintainer. See docs/OPEN_DECISIONS.md OD-002.
    """
    if not path.exists():
        pytest.skip(f"DB not found: {path}")
    conn = sqlite3.connect(str(path), timeout=30)
    conn.row_factory = sqlite3.Row
    from itdoc.schema_profile import detect_schema_profile
    detected = detect_schema_profile(conn)
    if detected.profile != expected:
        conn.close()
        pytest.skip(
            f"DB profile mismatch for {path.name}: "
            f"expected={expected}, got={detected.profile}"
        )
    return conn


@pytest.fixture()
def db_conn():
    """In-memory SQLite z minimalnym schematem potrzebnym do testów jednostkowych."""
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.executescript("""
        CREATE TABLE _schema_version (version TEXT, applied_at TEXT);
        INSERT INTO _schema_version VALUES ('1.0.0', '2026-01-01');

        CREATE TABLE docs (
            doc_uid TEXT PRIMARY KEY,
            title TEXT,
            title_norm TEXT,
            path TEXT,
            origin TEXT,
            created_at_utc TEXT,
            updated_at_utc TEXT
        );
        INSERT INTO docs VALUES
            ('UID001', 'Test Doc A', 'test doc a', 'core/test_a.md', 'core', '2026-01-01', '2026-01-01'),
            ('UID002', 'Test Doc B', 'test doc b', 'core/test_b.md', 'core', '2026-01-01', '2026-01-01');

        CREATE TABLE sections (
            section_uid TEXT PRIMARY KEY,
            doc_uid TEXT,
            heading_text TEXT,
            heading_norm TEXT,
            heading_level INTEGER,
            heading_path TEXT,
            anchor TEXT,
            ordinal INTEGER,
            status TEXT,
            text_fingerprint_sha256 TEXT,
            start_line INTEGER,
            end_line INTEGER
        );
        INSERT INTO sections VALUES
            ('SEC001', 'UID001', 'Cel dokumentu', 'cel dokumentu', 2, 'cel-dokumentu', 'cel-dokumentu', 1, 'filled', 'abc', 10, 20),
            ('SEC002', 'UID002', 'Zakres i granice', 'zakres i granice', 2, 'zakres-i-granice', 'zakres-i-granice', 1, 'filled', 'def', 5, 15);

        CREATE TABLE standards (
            standard_id INTEGER PRIMARY KEY,
            standard_code TEXT,
            standard_name TEXT,
            standard_name_en TEXT,
            description TEXT,
            version TEXT,
            url TEXT,
            applicable_industries TEXT
        );
        INSERT INTO standards VALUES
            (1, 'ISO/IEC 27001', 'Systemy zarządzania bezpieczeństwem informacji', 'Information security management systems', '', '2022', '', ''),
            (2, 'ITIL 4', 'ITIL 4 Service Management', 'ITIL 4', '', '4', '', '');

        CREATE TABLE compliance_regulations (
            id INTEGER PRIMARY KEY,
            regulation_code TEXT,
            regulation_name TEXT,
            jurisdiction TEXT,
            industry TEXT,
            key_requirements TEXT,
            penalty_info TEXT,
            data_engineering_impact TEXT
        );
        INSERT INTO compliance_regulations VALUES
            (1, 'UODO-PL', 'Ustawa o ochronie danych osobowych', 'PL', 'all', '', '', '');

        CREATE TABLE doc_standard_mapping (
            id INTEGER PRIMARY KEY,
            doc_path TEXT,
            standard_code TEXT,
            match_reason TEXT
        );
        INSERT INTO doc_standard_mapping VALUES
            (1, 'core/test_a.md', 'ISO/IEC 27001', 'keyword:security');

        CREATE TABLE doc_regulation_mapping (
            id INTEGER PRIMARY KEY,
            doc_path TEXT,
            regulation_code TEXT,
            match_reason TEXT
        );
        INSERT INTO doc_regulation_mapping VALUES
            (1, 'core/test_a.md', 'UODO-PL', 'keyword:personal_data');

        CREATE TABLE content_links (
            id INTEGER PRIMARY KEY,
            from_doc TEXT,
            to_doc TEXT,
            link_type TEXT
        );
        INSERT INTO content_links VALUES
            (1, 'core/test_a.md', 'core/test_b.md', 'requires');

        CREATE TABLE content_links_resolved (
            id INTEGER PRIMARY KEY,
            content_link_id INTEGER,
            from_kind TEXT,
            from_uid TEXT,
            to_kind TEXT,
            to_uid TEXT,
            link_type TEXT,
            direction TEXT,
            rationale TEXT,
            strength TEXT,
            resolution_method TEXT,
            resolution_confidence REAL,
            notes TEXT
        );
        INSERT INTO content_links_resolved VALUES
            (1, 1, 'doc', 'UID001', 'doc', 'UID002', 'requires', 'forward', '', 'required', 'explicit', 1.0, '');

        CREATE TABLE rhythm_edges (
            edge_id INTEGER PRIMARY KEY,
            from_node TEXT,
            to_node TEXT,
            rhythm_type TEXT,
            weight REAL,
            conditions TEXT,
            version_range TEXT,
            notes TEXT
        );
        INSERT INTO rhythm_edges VALUES
            (1, 'UID001', 'UID002', 'triggers', 0.9, '', '', '');

        CREATE TABLE contracts (
            contract_id INTEGER PRIMARY KEY,
            scope_kind TEXT,
            scope_uid TEXT,
            version TEXT,
            inputs_json TEXT,
            outputs_json TEXT,
            gates_json TEXT,
            impact_json TEXT,
            owner TEXT,
            notes TEXT,
            created_at_utc TEXT,
            updated_at_utc TEXT
        );
        INSERT INTO contracts VALUES
            (1, 'doc', 'UID001', '1.0', '["req_a"]', '["out_a"]', '[]', '{}', 'owner', '', '2026-01-01', '2026-01-01'),
            (2, 'doc', 'UID002', '1.0', '[]', '["out_b"]', '[]', '{}', 'owner', '', '2026-01-01', '2026-01-01');

        CREATE TABLE flags (
            id INTEGER PRIMARY KEY,
            doc_uid TEXT,
            version TEXT,
            branch_id INTEGER,
            access_mask INTEGER
        );
        INSERT INTO flags VALUES (1, 'UID001', '1.0.0', 1, 0), (2, 'UID002', '1.0.0', 1, 0);

        CREATE TABLE gap_analysis (
            id INTEGER PRIMARY KEY,
            standard_code TEXT,
            matched_doc_path TEXT,
            doc_title TEXT,
            status TEXT,
            confidence TEXT
        );
        INSERT INTO gap_analysis VALUES
            (1, 'ISO/IEC 27001', 'core/test_a.md', 'Test Doc A', 'present', 'exact'),
            (2, 'PMBOK 7', 'core/test_b.md', 'Test Doc B', 'present', 'high');
    """)
    yield conn
    conn.close()


@pytest.fixture()
def real_legacy_db_conn():
    """Połączenie z reports/it_doc_matrix.db (legacy-runtime). Skip jeśli brak lub zły profil."""
    conn = _require_db_profile(_DB_PATH, "legacy-runtime")
    yield conn
    conn.close()


@pytest.fixture()
def real_current_db_conn():
    """Połączenie z reports/it_doc_matrix_clean.db (current-snapshot). Skip jeśli brak lub zły profil."""
    conn = _require_db_profile(_CLEAN_DB_PATH, "current-snapshot")
    yield conn
    conn.close()


@pytest.fixture()
def real_db_conn(real_legacy_db_conn):
    """Alias kompatybilności wstecznej → real_legacy_db_conn."""
    yield real_legacy_db_conn


@pytest.fixture()
def repo_root() -> Path:
    """Katalog główny repozytorium."""
    return _REPO_ROOT


@pytest.fixture()
def templates_root():
    """Ścieżka do generated_templates/. Skip jeśli brak."""
    path = _REPO_ROOT / "generated_templates"
    if not path.exists():
        pytest.skip("generated_templates/ missing")
    return path


@pytest.fixture()
def core_dir(templates_root):
    """Ścieżka do generated_templates/core/. Skip jeśli brak."""
    path = templates_root / "core"
    if not path.exists():
        pytest.skip("generated_templates/core/ missing")
    return path


@pytest.fixture()
def satellite_dir(templates_root):
    """Ścieżka do generated_templates/satellite/. Skip jeśli brak."""
    path = templates_root / "satellite"
    if not path.exists():
        pytest.skip("generated_templates/satellite/ missing")
    return path


@pytest.fixture()
def alignment_log_path():
    """Ścieżka do reports/alignment_log.csv. Skip jeśli brak."""
    if not _ALIGNMENT_LOG.exists():
        pytest.skip("reports/alignment_log.csv missing")
    return _ALIGNMENT_LOG


@pytest.fixture()
def sample_template_path():
    """Ścieżka do pierwszego szablonu z core/. Pomija test jeśli katalog pusty."""
    if not _CORE_DIR.exists():
        pytest.skip(f"Template dir not found: {_CORE_DIR}")
    templates = sorted(_CORE_DIR.glob("*.md"))
    if not templates:
        pytest.skip("Brak szablonów w core/")
    return templates[0]
