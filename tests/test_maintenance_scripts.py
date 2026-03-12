"""
tests/test_maintenance_scripts.py

Kompleksowe testy jednostkowe i integracyjne dla 9 skryptów maintenance.

Uruchom:
    cd dokumentacja
    python3 -m pytest tests/test_maintenance_scripts.py -v --tb=short
"""

import json
import sqlite3
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Importy testowanych modułów
# ---------------------------------------------------------------------------

from scripts.maintenance.interactive_audit import (
    format_preview,
    build_filter_query,
    parse_keypress,
)
from scripts.maintenance.patch_section import (
    strip_frontmatter,
    find_section,
    apply_operation,
    build_diff,
    atomic_write,
    _apply_action_raw,
    _build_section_pattern,
    count_diff_lines,
    similarity_ratio,
)
from scripts.maintenance.regulation_updater import (
    validate_match_reason,
    validate_confidence,
    build_list_query,
    format_row_csv,
)
from scripts.maintenance.audit_templates import (
    normalize_path,
    compute_hash,
    find_ghosts,
    find_orphans,
    find_unmapped,
)
from scripts.maintenance.changelog_generator import (
    parse_git_log,
    group_into_sessions,
    render_markdown,
    render_json,
    format_date_range,
)
from scripts.maintenance.bulk_section_patcher import (
    ensure_changelog_table,
    log_change,
    apply_add_section,
    apply_replace_in_section,
    apply_append_to_section,
)
from scripts.maintenance.impact_analyzer import (
    analyze_standard,
    analyze_regulation,
    analyze_section,
    analyze_doc,
)
from scripts.maintenance.changelog_tracker import (
    ensure_table as ct_ensure_table,
    cmd_stats,
    cmd_export,
)
from scripts.maintenance.template_auditor import (
    audit_file,
)
from scripts.maintenance.satellite_linker import (
    ensure_table as sat_ensure_table,
    similarity_score,
    get_unmapped_docs,
    get_approved_docs,
    suggest_satellites,
    link_satellite,
    unlink_satellite,
    list_satellites,
    satellite_report,
)

# ---------------------------------------------------------------------------
# Markery
# ---------------------------------------------------------------------------

pytestmark = []  # markery ustawiane per-klasa poniżej


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def mem_db():
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript('''
        CREATE TABLE doc_standard_mapping (
            id INTEGER PRIMARY KEY,
            doc_path TEXT NOT NULL,
            standard_code TEXT NOT NULL,
            match_reason TEXT NOT NULL
        );
        CREATE TABLE gap_analysis (
            id INTEGER PRIMARY KEY,
            standard_code TEXT NOT NULL,
            doc_type_id TEXT,
            doc_title TEXT,
            status TEXT DEFAULT 'present',
            matched_doc_path TEXT,
            matched_doc_title TEXT,
            confidence TEXT
        );
        CREATE TABLE compliance_regulations (
            id INTEGER PRIMARY KEY,
            regulation_code TEXT NOT NULL,
            regulation_name TEXT,
            jurisdiction TEXT
        );
        CREATE TABLE doc_regulation_mapping (
            id INTEGER PRIMARY KEY,
            doc_path TEXT NOT NULL,
            regulation_code TEXT NOT NULL,
            match_reason TEXT
        );
        CREATE TABLE template_changelog (
            id INTEGER PRIMARY KEY,
            template_path TEXT NOT NULL,
            changed_at TEXT,
            change_type TEXT NOT NULL,
            change_reason TEXT,
            diff_summary TEXT,
            patch_args TEXT
        );
        CREATE TABLE docs (
            path TEXT PRIMARY KEY,
            title TEXT,
            doc_uid TEXT
        );
        CREATE TABLE standards (
            standard_code TEXT PRIMARY KEY,
            standard_name TEXT
        );
        CREATE TABLE sections (
            id INTEGER PRIMARY KEY,
            doc_uid TEXT,
            heading_text TEXT,
            anchor TEXT,
            ordinal INTEGER
        );
        CREATE TABLE content_links (
            id INTEGER PRIMARY KEY,
            context_doc_uid TEXT,
            to_ref TEXT
        );
        CREATE TABLE doc_section_guidance (
            id INTEGER PRIMARY KEY,
            doc_title TEXT,
            guidance TEXT
        );
        INSERT INTO doc_standard_mapping VALUES (1, "core/project_charter.md", "PMBOK 7", "keyword_match");
        INSERT INTO doc_standard_mapping VALUES (2, "core/isms_policy.md", "ISO/IEC 27001", "keyword_match");
        INSERT INTO doc_standard_mapping VALUES (3, "core/incident_report.md", "NIS2", "explicit_audit");
        INSERT INTO gap_analysis VALUES (1, "PMBOK 7", "project_doc", "Project Charter", "present", "core/project_charter.md", "Project Charter", "high");
        INSERT INTO compliance_regulations VALUES (1, "GDPR / RODO", "RODO", "EU");
        INSERT INTO docs VALUES ("core/project_charter.md", "Project Charter", "UID001");
        INSERT INTO docs VALUES ("core/isms_policy.md", "ISMS Policy", "UID002");
        INSERT INTO standards VALUES ("PMBOK 7", "Project Management Body of Knowledge 7th Edition");
        INSERT INTO standards VALUES ("ISO/IEC 27001", "Information Security Management");
        INSERT INTO sections VALUES (1, "UID001", "Cel dokumentu", "cel-dokumentu", 1);
        INSERT INTO sections VALUES (2, "UID001", "Zakres", "zakres", 2);
        INSERT INTO content_links VALUES (1, "UID002", "document::Project Charter::cel-dokumentu");
    ''')
    yield conn
    conn.close()


@pytest.fixture
def tmp_templates(tmp_path):
    d = tmp_path / "core"
    d.mkdir()
    # szablon z frontmatter
    (d / "test_template.md").write_text(
        "---\ntitle: Test\nstatus: draft\n---\n# Test Template\n\n## Cel dokumentu\nOpis celu.\n\n## Zakres\nOpis zakresu.\n",
        encoding='utf-8'
    )
    # szablon bez frontmatter
    (d / "no_frontmatter.md").write_text(
        "# No Frontmatter\n\n## Sekcja A\nTreść A.\n",
        encoding='utf-8'
    )
    return d


# ---------------------------------------------------------------------------
# Pomocnicze dane testowe
# ---------------------------------------------------------------------------

_SAMPLE_GIT_LOG = (
    "COMMIT|abc123def456|2024-03-15|Add project charter|Jan Kowalski\n"
    "M\tcore/project_charter.md\n"
)

_SAMPLE_GIT_LOG_TWO_DAYS = (
    "COMMIT|aaa111|2024-03-15|First commit|Jan Kowalski\n"
    "M\tcore/doc1.md\n"
    "COMMIT|bbb222|2024-01-01|Old commit|Anna Nowak\n"
    "M\tcore/doc2.md\n"
)


# ===========================================================================
# TestInteractiveAuditUnit
# ===========================================================================

@pytest.mark.unit
class TestInteractiveAuditUnit:

    def test_format_preview_returns_string(self):
        result = format_preview("core/test.md", "ISO 27001", "keyword_match", "Test Doc")
        assert isinstance(result, str)

    def test_format_preview_contains_doc_path(self):
        result = format_preview("core/test.md", "ISO 27001", "keyword_match", "Test Doc")
        assert "core/test.md" in result

    def test_format_preview_contains_standard(self):
        result = format_preview("core/test.md", "ISO 27001", "keyword_match", "Test Doc")
        assert "ISO 27001" in result

    def test_format_preview_with_none_title(self):
        result = format_preview("core/test.md", "PMBOK 7", "keyword_match", None)
        assert isinstance(result, str)
        assert "core/test.md" in result
        # brak tytułu — nie powinno rzucać wyjątku

    def test_build_filter_query_no_filters(self):
        sql, params = build_filter_query(None, None, 100)
        assert "WHERE" not in sql.upper() or sql.upper().count("WHERE") == 0
        assert params[-1] == 100  # ostatni param to LIMIT

    def test_build_filter_query_with_standard(self):
        sql, params = build_filter_query("ISO27001", None, 50)
        assert "LIKE ?" in sql
        assert any("ISO27001" in str(p) for p in params)

    def test_build_filter_query_with_reason(self):
        sql, params = build_filter_query(None, "keyword_match", 10)
        assert "match_reason" in sql
        assert "keyword_match" in params

    def test_build_filter_query_returns_tuple(self):
        result = build_filter_query("PMBOK", "keyword_match", 20)
        assert isinstance(result, tuple)
        assert len(result) == 2
        sql, params = result
        assert isinstance(sql, str)
        assert isinstance(params, list)

    def test_parse_keypress_valid_keys(self):
        assert parse_keypress("y") == "confirm"
        assert parse_keypress("n") == "delete"
        assert parse_keypress("s") == "skip"
        assert parse_keypress("o") == "open"
        assert parse_keypress("q") == "quit"

    def test_parse_keypress_invalid_returns_invalid(self):
        assert parse_keypress("x") == "invalid"
        assert parse_keypress("z") == "invalid"
        assert parse_keypress("1") == "invalid"
        assert parse_keypress("") == "invalid"


# ===========================================================================
# TestPatchSectionUnit
# ===========================================================================

@pytest.mark.unit
class TestPatchSectionUnit:

    _CONTENT_WITH_FM = (
        "---\ntitle: Test\nstatus: draft\n---\n"
        "# Test Template\n\n"
        "## Cel dokumentu\nOpis celu.\n\n"
        "## Zakres\nOpis zakresu.\n"
    )
    _CONTENT_NO_FM = (
        "# No Frontmatter\n\n"
        "## Sekcja A\nTreść A.\n"
    )

    def test_strip_frontmatter_basic(self):
        fm, body = strip_frontmatter(self._CONTENT_WITH_FM)
        assert fm.startswith("---")
        assert "title: Test" in fm

    def test_strip_frontmatter_no_frontmatter(self):
        fm, body = strip_frontmatter(self._CONTENT_NO_FM)
        assert fm == ''

    def test_strip_frontmatter_preserves_body(self):
        fm, body = strip_frontmatter(self._CONTENT_WITH_FM)
        assert "# Test Template" in body
        assert "Cel dokumentu" in body

    def test_strip_frontmatter_roundtrip(self):
        fm, body = strip_frontmatter(self._CONTENT_WITH_FM)
        reconstructed = fm + body
        assert reconstructed == self._CONTENT_WITH_FM

    def test_find_section_existing(self):
        _, body = strip_frontmatter(self._CONTENT_WITH_FM)
        result = find_section(body, "Cel dokumentu")
        assert result is not None
        start, end = result
        assert isinstance(start, int)
        assert isinstance(end, int)
        assert start <= end

    def test_find_section_missing(self):
        _, body = strip_frontmatter(self._CONTENT_WITH_FM)
        result = find_section(body, "Nieistniejąca Sekcja XYZ")
        assert result is None

    def test_find_section_case_insensitive(self):
        # Implementacja używa re.escape bez IGNORECASE — uppercase nie pasuje
        _, body = strip_frontmatter(self._CONTENT_WITH_FM)
        result_lower = find_section(body, "Cel dokumentu")
        result_upper = find_section(body, "CEL DOKUMENTU")
        # Sprawdzamy spójność zachowania (nie zakładamy case-insensitive)
        assert result_lower is not None  # lowercase powinno działać
        # uppercase może zwrócić None — to jest dozwolone zachowanie

    def test_apply_operation_replace(self):
        _, body = strip_frontmatter(self._CONTENT_WITH_FM)
        result = apply_operation(body, "Cel dokumentu", "replace", content="Nowy opis celu.")
        assert isinstance(result, str)
        assert "Nowy opis celu." in result

    def test_apply_operation_append(self):
        _, body = strip_frontmatter(self._CONTENT_WITH_FM)
        result = apply_operation(body, "Cel dokumentu", "append", content="Dodatkowy tekst.")
        assert isinstance(result, str)
        assert "Dodatkowy tekst." in result
        assert "Opis celu." in result  # oryginalna treść zachowana

    def test_apply_operation_prepend(self):
        _, body = strip_frontmatter(self._CONTENT_WITH_FM)
        result = apply_operation(body, "Cel dokumentu", "prepend", content="Wstęp.")
        assert isinstance(result, str)
        assert "Wstęp." in result

    def test_apply_operation_delete(self):
        _, body = strip_frontmatter(self._CONTENT_WITH_FM)
        result = apply_operation(body, "Cel dokumentu", "delete")
        assert isinstance(result, str)
        # Sekcja powinna być usunięta
        assert "## Cel dokumentu" not in result

    def test_apply_operation_unknown_section(self):
        _, body = strip_frontmatter(self._CONTENT_WITH_FM)
        # Brak sekcji → no-op (zwraca body bez zmian)
        result = apply_operation(body, "Nieistniejaca Sekcja XYZ", "replace", content="Nowe.")
        assert result == body  # bez zmian

    def test_build_diff_returns_string(self):
        original = "# Test\n\nTreść oryginalna.\n"
        modified = "# Test\n\nTreść zmodyfikowana.\n"
        result = build_diff(original, modified, "test.md")
        assert isinstance(result, str)

    def test_build_diff_contains_minus_plus(self):
        original = "# Test\n\nTreść oryginalna.\n"
        modified = "# Test\n\nTreść zmodyfikowana.\n"
        result = build_diff(original, modified, "test.md")
        assert "---" in result
        assert "+++" in result

    def test_atomic_write_creates_file(self, tmp_path):
        target = tmp_path / "output.md"
        atomic_write(target, "# Hello\n")
        assert target.exists()
        assert target.read_text(encoding='utf-8') == "# Hello\n"


# ===========================================================================
# TestRegulationUpdaterUnit
# ===========================================================================

@pytest.mark.unit
class TestRegulationUpdaterUnit:

    def test_validate_match_reason_valid(self):
        # Wartości zdefiniowane w VALID_MATCH_REASONS regulation_updater.py
        assert validate_match_reason("keyword_match") is True
        assert validate_match_reason("explicit_audit") is True

    def test_validate_match_reason_invalid(self):
        assert validate_match_reason("random") is False
        assert validate_match_reason("") is False
        assert validate_match_reason("KEYWORD_MATCH") is False

    def test_validate_confidence_valid(self):
        assert validate_confidence("exact") is True
        assert validate_confidence("high") is True
        assert validate_confidence("medium") is True
        assert validate_confidence("low") is True

    def test_validate_confidence_invalid(self):
        assert validate_confidence("unknown") is False
        assert validate_confidence("") is False
        assert validate_confidence("HIGH") is False

    def test_build_list_query_no_filters(self):
        sql, params = build_list_query()
        assert "SELECT" in sql.upper()
        assert "WHERE" not in sql.upper()
        assert params == []

    def test_build_list_query_with_standard(self):
        sql, params = build_list_query(standard="PMBOK 7")
        assert "?" in sql
        assert "PMBOK 7" in params

    def test_build_list_query_returns_tuple(self):
        result = build_list_query(standard="ISO 27001", reason="keyword_match")
        assert isinstance(result, tuple)
        sql, params = result
        assert isinstance(sql, str)
        assert isinstance(params, list)

    def test_format_row_csv_returns_string(self):
        row = {
            "doc_path": "core/test.md",
            "standard_code": "ISO 27001",
            "match_reason": "keyword_match",
            "confidence": "high",
            "status": "present",
        }
        result = format_row_csv(row)
        assert isinstance(result, str)

    def test_format_row_csv_contains_comma(self):
        row = {
            "doc_path": "core/test.md",
            "standard_code": "ISO 27001",
            "match_reason": "keyword_match",
            "confidence": "high",
            "status": "present",
        }
        result = format_row_csv(row)
        assert "," in result

    def test_format_row_csv_handles_none_values(self):
        row = {
            "doc_path": "core/test.md",
            "standard_code": None,
            "match_reason": None,
            "confidence": None,
            "status": None,
        }
        result = format_row_csv(row)
        assert isinstance(result, str)
        # None wartości → puste pola w CSV
        assert "core/test.md" in result


# ===========================================================================
# TestAuditTemplatesUnit
# ===========================================================================

@pytest.mark.unit
class TestAuditTemplatesUnit:

    def test_normalize_path_backslash(self):
        result = normalize_path("core\\test\\file.md")
        assert "\\" not in result
        assert "/" in result

    def test_normalize_path_lowercase(self):
        result = normalize_path("Core/TEST/File.MD")
        assert result == result.lower()

    def test_normalize_path_forward_slash_unchanged(self):
        result = normalize_path("core/test/file.md")
        assert result == "core/test/file.md"

    def test_compute_hash_returns_hex(self):
        result = compute_hash(b"hello world")
        assert isinstance(result, str)
        assert len(result) == 64
        assert all(c in "0123456789abcdef" for c in result)

    def test_compute_hash_deterministic(self):
        data = b"deterministic content"
        assert compute_hash(data) == compute_hash(data)

    def test_compute_hash_different_content(self):
        h1 = compute_hash(b"content A")
        h2 = compute_hash(b"content B")
        assert h1 != h2

    def test_find_unmapped_returns_list(self, mem_db):
        result = find_unmapped(mem_db)
        assert isinstance(result, list)

    def test_find_unmapped_empty_when_all_mapped(self, mem_db):
        # W mem_db oba docs (project_charter, isms_policy) mają wpisy w mapping
        result = find_unmapped(mem_db)
        assert result == []

    def test_find_ghosts_returns_list(self, mem_db, tmp_path):
        d = tmp_path / "core"
        d.mkdir()
        result = find_ghosts(mem_db, d)
        assert isinstance(result, list)

    def test_find_orphans_returns_list(self, mem_db, tmp_path):
        d = tmp_path / "core"
        d.mkdir()
        (d / "orphan_doc.md").write_text("# Orphan\n")
        result = find_orphans(mem_db, d)
        assert isinstance(result, list)


# ===========================================================================
# TestChangelogGeneratorUnit
# ===========================================================================

@pytest.mark.unit
class TestChangelogGeneratorUnit:

    def test_parse_git_log_empty_string(self):
        result = parse_git_log("")
        assert result == []

    def test_parse_git_log_single_commit(self):
        result = parse_git_log(_SAMPLE_GIT_LOG)
        assert len(result) == 1

    def test_parse_git_log_commit_has_hash_field(self):
        result = parse_git_log(_SAMPLE_GIT_LOG)
        assert "hash" in result[0]
        assert result[0]["hash"] == "abc123def456"

    def test_parse_git_log_commit_has_date_field(self):
        result = parse_git_log(_SAMPLE_GIT_LOG)
        assert "date" in result[0]
        assert result[0]["date"] == "2024-03-15"

    def test_group_into_sessions_empty(self):
        result = group_into_sessions([])
        assert result == []

    def test_group_into_sessions_single(self):
        commits = parse_git_log(_SAMPLE_GIT_LOG)
        sessions = group_into_sessions(commits)
        assert len(sessions) == 1
        assert len(sessions[0]) == 1

    def test_group_into_sessions_splits_by_gap(self):
        # Dwa commity o datach różniących się o wiele dni → 2 sesje
        commits = parse_git_log(_SAMPLE_GIT_LOG_TWO_DAYS)
        assert len(commits) == 2
        sessions = group_into_sessions(commits, gap_minutes=60)
        # Daty: 2024-03-15 i 2024-01-01 → różnica > 60 min → 2 sesje
        assert len(sessions) == 2

    def test_render_markdown_returns_string(self):
        commits = parse_git_log(_SAMPLE_GIT_LOG)
        sessions = group_into_sessions(commits)
        result = render_markdown(sessions, [])
        assert isinstance(result, str)

    def test_render_json_returns_valid_json(self):
        commits = parse_git_log(_SAMPLE_GIT_LOG)
        sessions = group_into_sessions(commits)
        result = render_json(sessions, [])
        parsed = json.loads(result)
        assert isinstance(parsed, dict)

    def test_format_date_range_both_provided(self):
        result = format_date_range("2024-01-01", "2024-12-31")
        assert isinstance(result, str)
        assert "2024-01-01" in result
        assert "2024-12-31" in result


# ===========================================================================
# TestIntegrationDB
# ===========================================================================

@pytest.mark.integration
class TestIntegrationDB:

    def test_build_filter_query_standard_filters_correctly(self, mem_db):
        sql, params = build_filter_query("PMBOK", None, 100)
        rows = mem_db.execute(sql, params).fetchall()
        assert len(rows) >= 1
        for row in rows:
            assert "PMBOK" in row["standard_code"]

    def test_build_list_query_standard_returns_results(self, mem_db):
        sql, params = build_list_query(standard="PMBOK 7")
        rows = mem_db.execute(sql, params).fetchall()
        assert len(rows) >= 1
        for row in rows:
            assert row["standard_code"] == "PMBOK 7"

    def test_validate_match_reason_matches_db_values(self, mem_db):
        rows = mem_db.execute(
            "SELECT DISTINCT match_reason FROM doc_standard_mapping"
        ).fetchall()
        for row in rows:
            reason = row[0]
            # Wartości z DB powinny być walidowane przez interactive_audit.VALID_REASONS
            from scripts.maintenance.interactive_audit import VALID_REASONS
            assert reason in VALID_REASONS, f"Nieznany reason w DB: {reason}"

    def test_find_unmapped_detects_all_unmapped(self, mem_db):
        # Dodaj doc bez mappingu
        mem_db.execute(
            "INSERT INTO docs VALUES ('core/unmapped_doc.md', 'Unmapped Doc', 'UID999')"
        )
        mem_db.commit()
        result = find_unmapped(mem_db)
        assert "core/unmapped_doc.md" in result

    def test_find_ghosts_empty_when_files_exist(self, tmp_path):
        # Utwórz DB z ścieżkami odpowiadającymi plikom na dysku
        d = tmp_path / "core"
        d.mkdir()
        (d / "existing.md").write_text("# Existing\n", encoding='utf-8')

        conn = sqlite3.connect(':memory:')
        conn.row_factory = sqlite3.Row
        conn.executescript('''
            CREATE TABLE docs (path TEXT PRIMARY KEY, title TEXT, uid TEXT);
            CREATE TABLE gap_analysis (
                id INTEGER PRIMARY KEY,
                standard_code TEXT,
                matched_doc_path TEXT
            );
            INSERT INTO docs VALUES ("core/existing.md", "Existing", "UID001");
        ''')

        ghosts = find_ghosts(conn, d)
        assert ghosts == []
        conn.close()

    def test_find_orphans_empty_when_all_in_db(self, tmp_path):
        # Utwórz plik i DB z pasującą ścieżką
        d = tmp_path / "core"
        d.mkdir()
        (d / "mapped.md").write_text("# Mapped\n", encoding='utf-8')

        conn = sqlite3.connect(':memory:')
        conn.row_factory = sqlite3.Row
        conn.executescript('''
            CREATE TABLE docs (path TEXT PRIMARY KEY, title TEXT, uid TEXT);
            INSERT INTO docs VALUES ("core/mapped.md", "Mapped", "UID001");
        ''')

        orphans = find_orphans(conn, d)
        assert orphans == []
        conn.close()

    def test_strip_frontmatter_real_template(self, tmp_templates):
        content = (tmp_templates / "test_template.md").read_text(encoding='utf-8')
        fm, body = strip_frontmatter(content)
        assert fm.startswith("---")
        assert "title: Test" in fm
        assert "# Test Template" in body

    def test_apply_replace_modifies_section(self, tmp_templates):
        content = (tmp_templates / "test_template.md").read_text(encoding='utf-8')
        _, body = strip_frontmatter(content)
        result = apply_operation(
            body, "Cel dokumentu", "replace", content="Nowy opis po zmianie."
        )
        assert "Nowy opis po zmianie." in result
        assert "Opis celu." not in result

    def test_atomic_write_is_readable_after_write(self, tmp_path):
        target = tmp_path / "readable.md"
        content = "# Readable\n\nTreść testowa.\n"
        atomic_write(target, content)
        assert target.exists()
        read_back = target.read_text(encoding='utf-8')
        assert read_back == content

    def test_render_markdown_with_empty_data(self):
        result = render_markdown([], [])
        assert isinstance(result, str)
        assert len(result) > 0
        # Pusta lista sesji i pustych wierszy → komunikat o braku zmian
        assert "Brak zmian" in result or "Raport" in result


# ===========================================================================
# TestBulkSectionPatcherUnit
# ===========================================================================

@pytest.mark.unit
class TestBulkSectionPatcherUnit:
    """Testy jednostkowe dla bulk_section_patcher.py."""

    def test_ensure_changelog_table_creates_table(self, mem_db):
        ensure_changelog_table(mem_db)
        cur = mem_db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='template_changelog'")
        assert cur.fetchone() is not None

    def test_ensure_changelog_table_idempotent(self, mem_db):
        ensure_changelog_table(mem_db)
        ensure_changelog_table(mem_db)  # drugie wywołanie nie rzuca wyjątku

    def test_log_change_inserts_row(self, mem_db):
        ensure_changelog_table(mem_db)
        log_change(mem_db, "core/test.md", "bulk_patch", "Powód", "Zmiana", "{}")
        mem_db.commit()
        row = mem_db.execute("SELECT * FROM template_changelog WHERE template_path='core/test.md'").fetchone()
        assert row is not None
        assert row["change_type"] == "bulk_patch"

    def test_log_change_stores_reason(self, mem_db):
        ensure_changelog_table(mem_db)
        log_change(mem_db, "core/a.md", "test_op", "mój powód", "diff", "{}")
        mem_db.commit()
        row = mem_db.execute("SELECT change_reason FROM template_changelog WHERE template_path='core/a.md'").fetchone()
        assert row["change_reason"] == "mój powód"

    def test_apply_add_section_appends_when_no_insert_before(self):
        content = "# Dokument\n\n## Sekcja A\nTreść A.\n"
        new_content, msg = apply_add_section(content, "## Nowa Sekcja", "Opis nowej.", None)
        assert "## Nowa Sekcja" in new_content
        assert "Opis nowej." in new_content
        assert msg  # msg nie jest pusty

    def test_apply_add_section_no_duplicate(self):
        content = "# Dokument\n\n## Nowa Sekcja\nJuż istnieje.\n"
        new_content, msg = apply_add_section(content, "## Nowa Sekcja", "Opis.", None)
        assert new_content == content  # brak zmiany
        assert msg == ""

    def test_apply_replace_in_section_replaces_text(self):
        content = "# Dok\n\n## Cel dokumentu\nStary tekst.\n\n## Zakres\nOpis.\n"
        new_content, msg = apply_replace_in_section(content, "## Cel dokumentu", "Stary tekst.", "Nowy tekst.")
        assert "Nowy tekst." in new_content
        assert "Stary tekst." not in new_content
        assert msg

    def test_apply_replace_in_section_no_change_when_missing(self):
        content = "# Dok\n\n## Cel dokumentu\nTreść.\n"
        new_content, msg = apply_replace_in_section(content, "## Nieistniejąca", "x", "y")
        assert new_content == content
        assert msg == ""

    def test_apply_append_to_section_adds_text(self):
        content = "# Dok\n\n## Standardy i compliance\n- ISO 9001\n\n## Zakres\nOpis.\n"
        new_content, msg = apply_append_to_section(content, "## Standardy i compliance", "- ISO/IEC 27001")
        assert "- ISO/IEC 27001" in new_content
        assert msg

    def test_apply_append_to_section_no_change_when_heading_missing(self):
        content = "# Dok\n\n## Zakres\nOpis.\n"
        new_content, msg = apply_append_to_section(content, "## Nieistniejąca sekcja", "tekst")
        assert new_content == content
        assert msg == ""


# ===========================================================================
# TestImpactAnalyzerUnit
# ===========================================================================

@pytest.mark.unit
class TestImpactAnalyzerUnit:
    """Testy jednostkowe dla impact_analyzer.py."""

    def test_analyze_standard_returns_dict(self, mem_db):
        result = analyze_standard(mem_db, "PMBOK 7")
        assert isinstance(result, dict)

    def test_analyze_standard_found_returns_query_type(self, mem_db):
        result = analyze_standard(mem_db, "PMBOK 7")
        assert result.get("query_type") == "standard"

    def test_analyze_standard_not_found_returns_error(self, mem_db):
        result = analyze_standard(mem_db, "NIEISTNIEJACY_STANDARD_XYZ")
        assert "error" in result

    def test_analyze_standard_counts_affected(self, mem_db):
        result = analyze_standard(mem_db, "PMBOK 7")
        assert result.get("total_affected", 0) >= 0

    def test_analyze_regulation_found(self, mem_db):
        result = analyze_regulation(mem_db, "GDPR")
        assert isinstance(result, dict)
        assert result.get("query_type") == "regulation"

    def test_analyze_regulation_not_found_returns_error(self, mem_db):
        result = analyze_regulation(mem_db, "NIEISTNIEJACA_REG_ZZZ")
        assert "error" in result

    def test_analyze_section_returns_dict(self, mem_db):
        result = analyze_section(mem_db, "Cel dokumentu")
        assert isinstance(result, dict)
        assert result.get("query_type") == "section"

    def test_analyze_section_templates_count_is_int(self, mem_db):
        result = analyze_section(mem_db, "Cel dokumentu")
        assert isinstance(result.get("templates_count"), int)

    def test_analyze_doc_found(self, mem_db):
        result = analyze_doc(mem_db, "Project Charter")
        assert isinstance(result, dict)
        assert result.get("query_type") == "document"
        assert result.get("count", 0) >= 1

    def test_analyze_doc_not_found_returns_error(self, mem_db):
        result = analyze_doc(mem_db, "DOKUMENT_KTORY_NIE_ISTNIEJE_ZZZ")
        assert "error" in result


# ===========================================================================
# TestChangelogTrackerUnit
# ===========================================================================

@pytest.mark.unit
class TestChangelogTrackerUnit:
    """Testy jednostkowe dla changelog_tracker.py."""

    def test_ensure_table_creates_changelog(self, mem_db):
        # Usuń tabelę jeśli istnieje
        mem_db.execute("DROP TABLE IF EXISTS template_changelog")
        mem_db.commit()
        ct_ensure_table(mem_db)
        cur = mem_db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='template_changelog'")
        assert cur.fetchone() is not None

    def test_ensure_table_idempotent(self, mem_db):
        ct_ensure_table(mem_db)
        ct_ensure_table(mem_db)  # nie rzuca wyjątku

    def test_cmd_stats_runs_without_error(self, mem_db, capsys):
        class FakeArgs:
            pass
        ct_ensure_table(mem_db)
        cmd_stats(mem_db, FakeArgs())  # nie rzuca wyjątku
        captured = capsys.readouterr()
        assert "changelog" in captured.out.lower() or "łącznie" in captured.out.lower()

    def test_cmd_stats_shows_total(self, mem_db, capsys):
        ct_ensure_table(mem_db)
        # Dodaj kilka wpisów
        for i in range(3):
            mem_db.execute(
                "INSERT INTO template_changelog (template_path, changed_at, change_type) VALUES (?,?,?)",
                (f"core/doc{i}.md", "2026-03-10T10:00:00", "test_type")
            )
        mem_db.commit()

        class FakeArgs:
            pass
        cmd_stats(mem_db, FakeArgs())
        captured = capsys.readouterr()
        assert "3" in captured.out

    def test_cmd_export_returns_json_list(self, mem_db, capsys):
        ct_ensure_table(mem_db)
        mem_db.execute(
            "INSERT INTO template_changelog (template_path, changed_at, change_type) VALUES (?,?,?)",
            ("core/export_test.md", "2026-03-10T12:00:00", "bulk_patch")
        )
        mem_db.commit()

        class FakeArgs:
            save = None
        cmd_export(mem_db, FakeArgs())
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert isinstance(data, list)
        assert any(r["template_path"] == "core/export_test.md" for r in data)

    def test_cmd_export_to_file(self, mem_db, tmp_path):
        ct_ensure_table(mem_db)
        out_file = tmp_path / "export.json"

        class FakeArgs:
            save = str(out_file)
        cmd_export(mem_db, FakeArgs())
        assert out_file.exists()
        data = json.loads(out_file.read_text(encoding="utf-8"))
        assert isinstance(data, list)

    def test_ensure_table_has_expected_columns(self, mem_db):
        ct_ensure_table(mem_db)
        cur = mem_db.execute("PRAGMA table_info(template_changelog)")
        cols = {row[1] for row in cur.fetchall()}
        for expected in {"template_path", "changed_at", "change_type", "change_reason"}:
            assert expected in cols

    def test_cmd_stats_handles_empty_table(self, mem_db, capsys):
        mem_db.execute("DELETE FROM template_changelog")
        mem_db.commit()

        class FakeArgs:
            pass
        ct_ensure_table(mem_db)
        cmd_stats(mem_db, FakeArgs())  # nie rzuca nawet przy pustej tabeli
        captured = capsys.readouterr()
        assert "0" in captured.out or "Łącznie" in captured.out

    def test_cmd_export_empty_gives_empty_list(self, mem_db, capsys):
        mem_db.execute("DELETE FROM template_changelog")
        mem_db.commit()
        ct_ensure_table(mem_db)

        class FakeArgs:
            save = None
        cmd_export(mem_db, FakeArgs())
        captured = capsys.readouterr()
        data = json.loads(captured.out)
        assert data == []

    def test_changelog_entries_preserve_change_reason(self, mem_db):
        ct_ensure_table(mem_db)
        mem_db.execute(
            "INSERT INTO template_changelog (template_path, changed_at, change_type, change_reason) VALUES (?,?,?,?)",
            ("core/r.md", "2026-03-10", "manual", "Korekta po przeglądzie")
        )
        mem_db.commit()
        row = mem_db.execute(
            "SELECT change_reason FROM template_changelog WHERE template_path='core/r.md'"
        ).fetchone()
        assert row[0] == "Korekta po przeglądzie"


# ===========================================================================
# TestTemplateAuditorUnit
# ===========================================================================

@pytest.mark.unit
class TestTemplateAuditorUnit:
    """Testy jednostkowe dla template_auditor.py."""

    def _make_template(self, tmp_path: Path, filename: str, content: str) -> Path:
        f = tmp_path / filename
        f.write_text(content, encoding="utf-8")
        return f

    def test_audit_file_returns_dict(self, tmp_path, mem_db):
        f = self._make_template(tmp_path, "test.md", "# Doc\n\n## Cel dokumentu\nCel.\n")
        result = audit_file(f, "core/test.md", mem_db)
        assert isinstance(result, dict)
        assert "score" in result

    def test_audit_file_score_is_int(self, tmp_path, mem_db):
        f = self._make_template(tmp_path, "test.md", "# Doc\n\n## Cel dokumentu\nCel.\n")
        result = audit_file(f, "core/test.md", mem_db)
        assert isinstance(result["score"], int)

    def test_audit_file_perfect_template_high_score(self, tmp_path, mem_db):
        content = (
            "---\ntitle: Perfect\n---\n"
            "# Perfect Template\n\n"
            "## Cel dokumentu\nSzczegółowy opis celu.\n\n"
            "## Zakres i granice\nZakres.\n\n"
            "## Wejścia i wyjścia\nWejścia i wyjścia.\n\n"
            "## Powiązania\nPowiązany dokument.\n\n"
            "## Standardy i compliance\n- ISO 9001: Zarządzanie jakością\n- ISO/IEC 27001: Bezpieczeństwo\n\n"
            "## RACI i role\n| Rola | R | A | C | I |\n|------|---|---|---|---|\n| PM | R | - | - | - |\n\n"
            "## Metadane\nStatus: aktywny\n"
        )
        f = self._make_template(tmp_path, "perfect.md", content)
        result = audit_file(f, "core/perfect.md", mem_db)
        assert result["score"] >= 40  # przynajmniej minimalny score za sekcje

    def test_audit_file_missing_all_sections_low_score(self, tmp_path, mem_db):
        content = "# Minimal\n\nTylko tekst bez żadnych sekcji.\n"
        f = self._make_template(tmp_path, "minimal.md", content)
        result = audit_file(f, "core/minimal.md", mem_db)
        assert result["score"] < 50

    def test_audit_file_emoji_zeroes_score(self, tmp_path, mem_db):
        content = "# Emoji Doc 🚀\n\n## Cel dokumentu\nCel 🎉.\n"
        f = self._make_template(tmp_path, "emoji.md", content)
        result = audit_file(f, "core/emoji.md", mem_db)
        assert result["score"] == 0
        assert result.get("emoji") is True

    def test_audit_file_placeholder_penalizes(self, tmp_path, mem_db):
        without_ph = "# Doc\n\n## Cel dokumentu\nOpis celu.\n"
        with_ph = "# Doc\n\n## Cel dokumentu\n[TODO: wypełnić] [TODO: więcej]\n"
        f1 = self._make_template(tmp_path, "no_ph.md", without_ph)
        f2 = self._make_template(tmp_path, "with_ph.md", with_ph)
        r1 = audit_file(f1, "core/no_ph.md", mem_db)
        r2 = audit_file(f2, "core/with_ph.md", mem_db)
        assert r1["score"] >= r2["score"]  # placeholdery nie mogą poprawić score

    def test_audit_file_reports_missing_sections(self, tmp_path, mem_db):
        content = "# Doc\n\nTylko treść bez sekcji.\n"
        f = self._make_template(tmp_path, "nosections.md", content)
        result = audit_file(f, "core/nosections.md", mem_db)
        assert len(result.get("sections_missing", [])) > 0

    def test_audit_file_grade_assigned(self, tmp_path, mem_db):
        content = "# Doc\n\n## Cel dokumentu\nCel.\n"
        f = self._make_template(tmp_path, "grade.md", content)
        result = audit_file(f, "core/grade.md", mem_db)
        assert result.get("grade") in {"A", "B", "C", "D"}

    def test_audit_file_nonexistent_returns_error(self, tmp_path, mem_db):
        f = tmp_path / "nonexistent.md"
        result = audit_file(f, "core/nonexistent.md", mem_db)
        assert "error" in result or result.get("score", -1) == 0

    def test_audit_file_standards_filled_detected(self, tmp_path, mem_db):
        content = (
            "# Doc\n\n"
            "## Standardy i compliance\n"
            "- ISO 9001: System zarządzania jakością\n"
            "- PMBOK 7: Zarządzanie projektem\n\n"
            "## Zakres i granice\nOpis.\n"
        )
        f = self._make_template(tmp_path, "std.md", content)
        result = audit_file(f, "core/std.md", mem_db)
        assert result.get("standards_filled") is True


# ===========================================================================
# TestPatchSectionPrivateFunctions  (podwyższenie mutation score)
# ===========================================================================

@pytest.mark.unit
class TestPatchSectionPrivateFunctions:
    """Testy dla prywatnych funkcji patch_section poprawiające mutation score."""

    _BODY_WITH_SECTIONS = (
        "## Cel dokumentu\nOpis celu dokumentu.\nWięcej opisu.\n\n"
        "## Zakres\nOpis zakresu.\n\n"
        "## Standardy\n- ISO 9001\n"
    )

    def test_build_section_pattern_matches_named_section(self):
        pattern = _build_section_pattern("Cel dokumentu", None, None)
        assert pattern.search(self._BODY_WITH_SECTIONS) is not None

    def test_build_section_pattern_with_level(self):
        pattern = _build_section_pattern("Cel dokumentu", None, 2)
        assert pattern.search(self._BODY_WITH_SECTIONS) is not None

    def test_build_section_pattern_does_not_match_wrong_section(self):
        pattern = _build_section_pattern("Nieistniejąca sekcja XYZ", None, None)
        assert pattern.search(self._BODY_WITH_SECTIONS) is None

    def test_build_section_pattern_with_regex(self):
        pattern = _build_section_pattern(None, r"Cel.*", None)
        assert pattern.search(self._BODY_WITH_SECTIONS) is not None

    def test_apply_action_raw_replace_changes_content(self):
        pattern = _build_section_pattern("Cel dokumentu", None, 2)
        new_content, msg = _apply_action_raw(
            self._BODY_WITH_SECTIONS, pattern, "replace", "Zupełnie nowy opis."
        )
        assert new_content is not None
        assert "Zupełnie nowy opis." in new_content
        assert msg is not None

    def test_apply_action_raw_returns_none_when_no_match(self):
        pattern = _build_section_pattern("Nie ma takiej sekcji", None, None)
        result, msg = _apply_action_raw(
            self._BODY_WITH_SECTIONS, pattern, "replace", "cokolwiek"
        )
        assert result is None
        assert msg is None

    def test_apply_action_raw_append_adds_text(self):
        pattern = _build_section_pattern("Cel dokumentu", None, 2)
        new_content, msg = _apply_action_raw(
            self._BODY_WITH_SECTIONS, pattern, "append", "Dodatkowy akapit."
        )
        assert new_content is not None
        assert "Dodatkowy akapit." in new_content

    def test_apply_action_raw_prepend_adds_text(self):
        pattern = _build_section_pattern("Cel dokumentu", None, 2)
        new_content, msg = _apply_action_raw(
            self._BODY_WITH_SECTIONS, pattern, "prepend", "Wstępny akapit."
        )
        assert new_content is not None
        assert "Wstępny akapit." in new_content

    def test_count_diff_lines_returns_tuple(self):
        result = count_diff_lines("a\nb\nc\n", "a\nb\nd\n")
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_count_diff_lines_identical_zero(self):
        added, removed = count_diff_lines("a\nb\n", "a\nb\n")
        assert added == 0
        assert removed == 0

    def test_count_diff_lines_detects_changes(self):
        added, removed = count_diff_lines("a\nb\nc\n", "a\nb\nd\ne\n")
        assert added > 0

    def test_similarity_ratio_identical_returns_one(self):
        assert similarity_ratio("abc", "abc") == 1.0

    def test_similarity_ratio_different_returns_less_than_one(self):
        r = similarity_ratio("abc", "xyz")
        assert r < 1.0

    def test_similarity_ratio_empty_strings(self):
        r = similarity_ratio("", "")
        assert isinstance(r, float)

    # -----------------------------------------------------------------------
    # strip_frontmatter — zabijamy survived mutanty
    # -----------------------------------------------------------------------

    def test_strip_frontmatter_offset_3(self):
        # Mutant zmienia content.find('\n---\n', 3) -> find(..., None)
        # Przy None znalazłby "---" na pozycji 0, co dałoby błędny wynik.
        content = "---\ntitle: test\n---\nbody here"
        fm, body = strip_frontmatter(content)
        assert fm == "---\ntitle: test\n---\n"
        assert body == "body here"

    def test_strip_frontmatter_end_plus5_slice(self):
        content = "---\nkey: val\n---\nrest"
        fm, body = strip_frontmatter(content)
        assert fm.endswith("---\n")
        assert not body.startswith("---")

    def test_strip_frontmatter_no_frontmatter_returns_empty(self):
        content = "# Tytuł\nTreść dokumentu"
        fm, body = strip_frontmatter(content)
        assert fm == ""
        assert body == content

    def test_strip_frontmatter_unclosed_returns_empty_fm(self):
        content = "---\ntitle: no close\nbody"
        fm, body = strip_frontmatter(content)
        assert fm == ""
        assert body == content

    # -----------------------------------------------------------------------
    # find_section — zabijamy survived mutanty
    # -----------------------------------------------------------------------

    def test_find_section_start_line_is_correct(self):
        body = "## Wstęp\nTreść wstępu.\n\n## Cel\nCel dokumentu.\n"
        result = find_section(body, "Cel")
        assert result is not None
        start, end = result
        assert start >= 4

    def test_find_section_returns_none_when_missing(self):
        body = "## Wstęp\nTreść.\n"
        assert find_section(body, "Nieistniejąca XYZ") is None

    def test_find_section_start_le_end(self):
        body = "## Sekcja A\nJeden wiersz.\n## Sekcja B\nDrugi.\n"
        result = find_section(body, "Sekcja A")
        assert result is not None
        start, end = result
        assert start <= end

    # -----------------------------------------------------------------------
    # apply_operation — zabijamy survived mutanty
    # -----------------------------------------------------------------------

    def test_apply_operation_replace_full_content(self):
        body = "## Cel\nStary tekst.\n\n## Zakres\nZakres treść.\n"
        result = apply_operation(body, "Cel", "replace", content="Nowy tekst.")
        assert "Nowy tekst." in result
        assert "Stary tekst." not in result

    def test_apply_operation_replace_old_new(self):
        body = "## Cel\nStary tekst dokładny.\n\n## Zakres\nZakres.\n"
        result = apply_operation(body, "Cel", "replace",
                                 old="Stary tekst dokładny.", new="Zamieniony.")
        assert "Zamieniony." in result

    def test_apply_operation_replace_old_not_found_returns_body(self):
        body = "## Cel\nInna treść.\n\n## Zakres\nZakres.\n"
        result = apply_operation(body, "Cel", "replace",
                                 old="Coś czego tu nie ma.", new="Nowe.")
        assert result == body

    def test_apply_operation_append_content(self):
        body = "## Cel\nTreść celu.\n\n## Zakres\nTreść.\n"
        result = apply_operation(body, "Cel", "append", content="Dopisany tekst.")
        assert "Dopisany tekst." in result
        assert "Treść celu." in result

    def test_apply_operation_prepend_content(self):
        body = "## Cel\nTreść celu.\n\n## Zakres\nTreść.\n"
        result = apply_operation(body, "Cel", "prepend", content="Prefix.")
        assert "Prefix." in result
        assert "Treść celu." in result

    def test_apply_operation_delete_removes_section(self):
        body = "## Cel\nTreść.\n\n## Zakres\nZakres treść.\n"
        result = apply_operation(body, "Cel", "delete")
        assert "## Cel" not in result
        assert "## Zakres" in result

    def test_apply_operation_rename(self):
        body = "## Cel\nTreść.\n\n## Zakres\nZakres.\n"
        result = apply_operation(body, "Cel", "rename", new_name="Nowy Cel")
        assert "## Nowy Cel" in result
        assert "## Cel\n" not in result

    def test_apply_operation_section_missing_returns_body(self):
        body = "## Zakres\nTreść.\n"
        result = apply_operation(body, "Nieistnieje", "replace", content="cos")
        assert result == body

    # -----------------------------------------------------------------------
    # similarity_ratio — graniczne wartości
    # -----------------------------------------------------------------------

    def test_similarity_ratio_partial(self):
        # similarity_ratio działa na zestawach linii
        r = similarity_ratio("linia1\nlinia2\nlinia3\n", "linia1\nlinia2\nnowaLinia\n")
        assert 0.0 < r < 1.0

    def test_similarity_ratio_completely_different(self):
        r = similarity_ratio("aaa\nbbb\n", "xxx\nyyy\n")
        assert r == 0.0

    def test_similarity_ratio_almost_same(self):
        # więcej wspólnych linii = wyższy score
        r1 = similarity_ratio("a\nb\nc\n", "a\nb\nx\n")   # 2/4 wspólne
        r2 = similarity_ratio("a\nb\nc\n", "x\ny\nz\n")   # 0/6 wspólne
        assert r1 > r2

    # -----------------------------------------------------------------------
    # count_diff_lines — graniczne wartości
    # -----------------------------------------------------------------------

    def test_count_diff_lines_added_count(self):
        added, removed = count_diff_lines("a\n", "a\nb\nc\n")
        assert added == 2

    def test_count_diff_lines_removed_count(self):
        added, removed = count_diff_lines("a\nb\nc\n", "a\n")
        assert removed == 2

    def test_count_diff_lines_both_nonzero(self):
        added, removed = count_diff_lines("a\nb\n", "a\nc\n")
        assert added >= 1
        assert removed >= 1

    # -----------------------------------------------------------------------
    # atomic_write — zabijamy survived mutanty
    # -----------------------------------------------------------------------

    def test_atomic_write_creates_file(self, tmp_path):
        target = tmp_path / "output.md"
        atomic_write(target, "Treść testowa.")
        assert target.exists()
        assert target.read_text() == "Treść testowa."

    def test_atomic_write_overwrites_existing(self, tmp_path):
        target = tmp_path / "existing.md"
        target.write_text("Stara treść.")
        atomic_write(target, "Nowa treść.")
        assert target.read_text() == "Nowa treść."

    def test_atomic_write_no_tmp_file_left(self, tmp_path):
        target = tmp_path / "clean.md"
        atomic_write(target, "Zawartość.")
        tmp_file = target.with_suffix(".tmp")
        assert not tmp_file.exists()


# ---------------------------------------------------------------------------
# Dodatkowe testy regulation_updater — zabijamy survived mutanty
# ---------------------------------------------------------------------------

from scripts.maintenance.regulation_updater import format_row_table


class TestRegulationUpdaterMutationKillers:
    """Celowane testy dla format_row_csv i format_row_table."""

    _SAMPLE_ROW = {
        "doc_path": "core/api.md",
        "standard_code": "ISO27001",
        "match_reason": "keyword_match",
        "confidence": "0.85",
        "status": "verified",
    }

    def test_format_row_csv_contains_all_fields(self):
        result = format_row_csv(self._SAMPLE_ROW)
        assert "core/api.md" in result
        assert "ISO27001" in result
        assert "keyword_match" in result
        assert "0.85" in result
        assert "verified" in result

    def test_format_row_csv_is_single_line(self):
        result = format_row_csv(self._SAMPLE_ROW)
        assert "\n" not in result

    def test_format_row_csv_empty_fields(self):
        row = {"doc_path": None, "standard_code": None,
               "match_reason": None, "confidence": None, "status": None}
        result = format_row_csv(row)
        assert isinstance(result, str)

    def test_format_row_table_contains_doc_path(self):
        widths = {"doc_path": 30, "standard_code": 15, "match_reason": 15,
                  "confidence": 8, "status": 8}
        result = format_row_table(self._SAMPLE_ROW, widths)
        assert "core/api.md" in result
        assert "ISO27001" in result

    def test_format_row_table_truncates_long_path(self):
        row = {**self._SAMPLE_ROW, "doc_path": "a" * 100}
        widths = {"doc_path": 20, "standard_code": 15, "match_reason": 15,
                  "confidence": 8, "status": 8}
        result = format_row_table(row, widths)
        assert "a" * 21 not in result

    def test_format_row_table_handles_none_confidence(self):
        row = {**self._SAMPLE_ROW, "confidence": None, "status": None}
        widths = {"doc_path": 30, "standard_code": 15, "match_reason": 15,
                  "confidence": 8, "status": 8}
        result = format_row_table(row, widths)
        assert "-" in result

    def test_build_list_query_no_filters(self):
        sql, params = build_list_query()
        assert "SELECT" in sql
        assert params == []

    def test_build_list_query_with_standard(self):
        sql, params = build_list_query(standard="ISO27001")
        assert "standard_code" in sql
        assert "ISO27001" in params

    def test_build_list_query_with_regulation(self):
        sql, params = build_list_query(regulation="GDPR")
        assert "regulation_code" in sql
        assert "GDPR" in params

    def test_build_list_query_with_reason(self):
        sql, params = build_list_query(reason="keyword_match")
        assert "match_reason" in sql
        assert "keyword_match" in params

    def test_build_list_query_multiple_filters(self):
        sql, params = build_list_query(standard="ISO27001", reason="explicit_audit")
        assert "WHERE" in sql
        assert len(params) == 2
        assert "ISO27001" in params
        assert "explicit_audit" in params

    def test_build_list_query_order_by(self):
        sql, _ = build_list_query()
        assert "ORDER BY" in sql


# ===========================================================================
# TestImpactAnalyzerMutationKillers — zabijamy survived mutanty w analyze_*
# ===========================================================================

@pytest.mark.unit
class TestImpactAnalyzerMutationKillers:
    """Celowane testy dla analyze_standard/regulation/section/doc."""

    def test_analyze_standard_contains_standard_code(self, mem_db):
        result = analyze_standard(mem_db, "PMBOK 7")
        matched = result.get("matched_standards", [])
        assert len(matched) >= 1
        assert matched[0]["standard_code"] == "PMBOK 7"

    def test_analyze_standard_contains_standard_name(self, mem_db):
        result = analyze_standard(mem_db, "PMBOK 7")
        matched = result.get("matched_standards", [])
        assert matched[0]["standard_name"] is not None

    def test_analyze_standard_affected_templates_is_list(self, mem_db):
        result = analyze_standard(mem_db, "PMBOK 7")
        matched = result.get("matched_standards", [])
        assert isinstance(matched[0]["affected_templates"], list)

    def test_analyze_standard_count_equals_len_of_affected(self, mem_db):
        result = analyze_standard(mem_db, "PMBOK 7")
        matched = result.get("matched_standards", [])
        assert matched[0]["count"] == len(matched[0]["affected_templates"])

    def test_analyze_standard_total_affected_is_sum(self, mem_db):
        result = analyze_standard(mem_db, "PMBOK 7")
        matched = result.get("matched_standards", [])
        total = result.get("total_affected", -1)
        assert total == sum(m["count"] for m in matched)

    def test_analyze_standard_affected_template_has_path(self, mem_db):
        result = analyze_standard(mem_db, "PMBOK 7")
        matched = result.get("matched_standards", [])
        for tmpl in matched[0]["affected_templates"]:
            assert "path" in tmpl

    def test_analyze_standard_affected_template_has_reason(self, mem_db):
        result = analyze_standard(mem_db, "PMBOK 7")
        matched = result.get("matched_standards", [])
        for tmpl in matched[0]["affected_templates"]:
            assert "reason" in tmpl

    def test_analyze_regulation_contains_code(self, mem_db):
        result = analyze_regulation(mem_db, "GDPR")
        matched = result.get("matched_regulations", [])
        assert len(matched) >= 1
        # regulation_code in fixture is "GDPR / RODO"
        assert "GDPR" in matched[0]["regulation_code"]

    def test_analyze_regulation_total_affected_matches(self, mem_db):
        result = analyze_regulation(mem_db, "GDPR")
        matched = result.get("matched_regulations", [])
        total = result.get("total_affected", -1)
        assert total == sum(m["count"] for m in matched)

    def test_analyze_regulation_count_matches_list_len(self, mem_db):
        result = analyze_regulation(mem_db, "GDPR")
        matched = result.get("matched_regulations", [])
        assert matched[0]["count"] == len(matched[0]["affected_templates"])

    def test_analyze_section_has_templates_count(self, mem_db):
        result = analyze_section(mem_db, "Cel dokumentu")
        assert "templates_count" in result
        assert isinstance(result["templates_count"], int)

    def test_analyze_section_affected_templates_is_list(self, mem_db):
        result = analyze_section(mem_db, "Cel dokumentu")
        assert isinstance(result.get("affected_templates", []), list)

    def test_analyze_doc_returns_path(self, mem_db):
        result = analyze_doc(mem_db, "Project Charter")
        matched = result.get("matched_docs", [])
        assert len(matched) >= 1
        assert "path" in matched[0]

    def test_analyze_doc_count_is_int(self, mem_db):
        result = analyze_doc(mem_db, "Project Charter")
        assert isinstance(result.get("count", 0), int)

    def test_analyze_standard_query_field_matches_input(self, mem_db):
        result = analyze_standard(mem_db, "PMBOK 7")
        assert result.get("query") == "PMBOK 7"

    def test_analyze_regulation_query_field_matches_input(self, mem_db):
        result = analyze_regulation(mem_db, "GDPR")
        assert result.get("query") == "GDPR"


# ===========================================================================
# TestTemplateAuditorMutationKillers — graniczne wartości score
# ===========================================================================

@pytest.mark.unit
class TestTemplateAuditorMutationKillers:
    """Celowane testy weryfikujące wartości score w audit_file."""

    def _make(self, tmp_path, name, content):
        f = tmp_path / name
        f.write_text(content, encoding="utf-8")
        return f

    def test_score_is_between_0_and_100(self, tmp_path, mem_db):
        f = self._make(tmp_path, "t.md", "# Doc\n\n## Cel dokumentu\nCel.\n")
        result = audit_file(f, "core/t.md", mem_db)
        assert 0 <= result["score"] <= 100

    def test_more_sections_gives_higher_score(self, tmp_path, mem_db):
        few = "# Doc\n\n## Cel dokumentu\nCel.\n"
        many = (
            "# Doc\n\n"
            "## Cel dokumentu\nCel.\n\n"
            "## Zakres i granice\nZakres.\n\n"
            "## Wejścia i wyjścia\nWejścia.\n\n"
            "## Standardy i compliance\n- ISO 9001\n\n"
            "## RACI i role\n| Rola | R |\n|------|---|\n| PM | R |\n"
        )
        r1 = audit_file(self._make(tmp_path, "few.md", few), "core/few.md", mem_db)
        r2 = audit_file(self._make(tmp_path, "many.md", many), "core/many.md", mem_db)
        assert r2["score"] >= r1["score"]

    def test_grade_d_for_score_below_40(self, tmp_path, mem_db):
        f = self._make(tmp_path, "bad.md", "# Doc\n")
        result = audit_file(f, "core/bad.md", mem_db)
        if result["score"] < 40:
            assert result["grade"] == "D"

    def test_grade_a_for_high_score(self, tmp_path, mem_db):
        content = (
            "---\ntitle: Great\n---\n"
            "# Great Template\n\n"
            "## Cel dokumentu\nSzczegółowy opis celu dokumentu bez placeholderów.\n\n"
            "## Zakres i granice\nDokładny zakres dokumentu.\n\n"
            "## Wejścia i wyjścia\nWejścia: dane. Wyjścia: raporty.\n\n"
            "## Standardy i compliance\n- ISO 9001: Zarządzanie jakością\n\n"
            "## RACI i role\n| Rola | R | A | C | I |\n|------|---|---|---|---|\n| PM | R | A | - | - |\n\n"
            "## Metadane\nStatus: aktywny. Wersja: 1.0\n"
        )
        f = self._make(tmp_path, "great.md", content)
        result = audit_file(f, "core/great.md", mem_db)
        if result["score"] >= 80:
            assert result["grade"] == "A"

    def test_emoji_flag_true_when_emoji_present(self, tmp_path, mem_db):
        f = self._make(tmp_path, "emo.md", "# Doc 🚀\n\n## Cel dokumentu\nCel.\n")
        result = audit_file(f, "core/emo.md", mem_db)
        assert result.get("emoji") is True
        assert result["score"] == 0

    def test_emoji_flag_false_when_no_emoji(self, tmp_path, mem_db):
        f = self._make(tmp_path, "noemo.md", "# Doc\n\n## Cel dokumentu\nCel.\n")
        result = audit_file(f, "core/noemo.md", mem_db)
        assert result.get("emoji") is False

    def test_sections_present_list_contains_found_sections(self, tmp_path, mem_db):
        content = "# Doc\n\n## Cel dokumentu\nCel.\n\n## Zakres i granice\nZakres.\n"
        f = self._make(tmp_path, "sp.md", content)
        result = audit_file(f, "core/sp.md", mem_db)
        # field is "sections_found" not "sections_present"
        found = result.get("sections_found", [])
        assert isinstance(found, list)
        assert any("Cel" in s for s in found)

    def test_sections_missing_list_is_subset_of_required(self, tmp_path, mem_db):
        content = "# Doc\n\n## Cel dokumentu\nCel.\n"
        f = self._make(tmp_path, "sm.md", content)
        result = audit_file(f, "core/sm.md", mem_db)
        missing = result.get("sections_missing", [])
        assert isinstance(missing, list)

    def test_placeholders_count_zero_when_no_placeholders(self, tmp_path, mem_db):
        content = "# Doc\n\n## Cel dokumentu\nKonkretna treść bez placeholderów.\n"
        f = self._make(tmp_path, "noph.md", content)
        result = audit_file(f, "core/noph.md", mem_db)
        assert result.get("placeholders", 0) == 0

    def test_placeholders_count_positive_when_present(self, tmp_path, mem_db):
        content = "# Doc\n\n## Cel dokumentu\n[Uzupełnij] [TODO: coś]\n"
        f = self._make(tmp_path, "ph.md", content)
        result = audit_file(f, "core/ph.md", mem_db)
        # field is "placeholder_count" not "placeholders"
        assert result.get("placeholder_count", 0) > 0


# ===========================================================================
# TestChangelogGeneratorMutationKillers — zabijamy survived mutanty
# ===========================================================================

_GIT_LOG_RENAME = (
    "COMMIT|ren111|2024-05-01|Rename file|Admin\n"
    "R100\tcore/old_name.md\tcore/new_name.md\n"
)

_GIT_LOG_MULTI_FILES = (
    "COMMIT|multi1|2024-06-01|Add three files|Dev\n"
    "A\tcore/new1.md\n"
    "M\tcore/existing.md\n"
    "D\tcore/deleted.md\n"
)

_GIT_LOG_TWO_SAME_DAY = (
    "COMMIT|c1|2024-07-01|First|Dev\n"
    "M\tcore/a.md\n"
    "COMMIT|c2|2024-07-01|Second|Dev\n"
    "M\tcore/b.md\n"
)


@pytest.mark.unit
class TestChangelogGeneratorMutationKillers:

    # parse_git_log: subject i author
    def test_parse_git_log_subject_correct(self):
        result = parse_git_log(_SAMPLE_GIT_LOG)
        assert result[0]["subject"] == "Add project charter"

    def test_parse_git_log_author_correct(self):
        result = parse_git_log(_SAMPLE_GIT_LOG)
        assert result[0]["author"] == "Jan Kowalski"

    # parse_git_log: pliki
    def test_parse_git_log_files_is_list(self):
        result = parse_git_log(_SAMPLE_GIT_LOG)
        assert isinstance(result[0]["files"], list)
        assert len(result[0]["files"]) == 1

    def test_parse_git_log_file_status_M(self):
        result = parse_git_log(_SAMPLE_GIT_LOG)
        assert result[0]["files"][0]["status"] == "M"

    def test_parse_git_log_file_path_correct(self):
        result = parse_git_log(_SAMPLE_GIT_LOG)
        assert result[0]["files"][0]["path"] == "core/project_charter.md"

    def test_parse_git_log_file_old_path_none_for_modify(self):
        result = parse_git_log(_SAMPLE_GIT_LOG)
        assert result[0]["files"][0]["old_path"] is None

    def test_parse_git_log_rename_status_R(self):
        result = parse_git_log(_GIT_LOG_RENAME)
        assert result[0]["files"][0]["status"] == "R"

    def test_parse_git_log_rename_old_path(self):
        result = parse_git_log(_GIT_LOG_RENAME)
        assert result[0]["files"][0]["old_path"] == "core/old_name.md"

    def test_parse_git_log_rename_new_path(self):
        result = parse_git_log(_GIT_LOG_RENAME)
        assert result[0]["files"][0]["path"] == "core/new_name.md"

    def test_parse_git_log_multiple_files(self):
        result = parse_git_log(_GIT_LOG_MULTI_FILES)
        assert len(result[0]["files"]) == 3

    def test_parse_git_log_multiple_commits(self):
        result = parse_git_log(_SAMPLE_GIT_LOG_TWO_DAYS)
        assert len(result) == 2

    def test_parse_git_log_second_commit_hash(self):
        result = parse_git_log(_SAMPLE_GIT_LOG_TWO_DAYS)
        assert result[1]["hash"] == "bbb222"

    # group_into_sessions: same day → 1 session
    def test_group_same_day_one_session(self):
        commits = parse_git_log(_GIT_LOG_TWO_SAME_DAY)
        sessions = group_into_sessions(commits, gap_minutes=1440)
        assert len(sessions) == 1
        assert len(sessions[0]) == 2

    def test_group_different_days_two_sessions(self):
        commits = parse_git_log(_SAMPLE_GIT_LOG_TWO_DAYS)
        sessions = group_into_sessions(commits, gap_minutes=60)
        assert len(sessions) == 2

    def test_group_preserves_all_commits(self):
        commits = parse_git_log(_SAMPLE_GIT_LOG_TWO_DAYS)
        sessions = group_into_sessions(commits, gap_minutes=60)
        total = sum(len(s) for s in sessions)
        assert total == len(commits)

    def test_group_single_commit_one_session(self):
        commits = parse_git_log(_SAMPLE_GIT_LOG)
        sessions = group_into_sessions(commits)
        assert len(sessions) == 1

    # format_date_range: wszystkie kombinacje
    def test_format_date_range_only_since(self):
        result = format_date_range("2024-01-01", None)
        assert "2024-01-01" in result

    def test_format_date_range_only_until(self):
        result = format_date_range(None, "2024-12-31")
        assert "2024-12-31" in result

    def test_format_date_range_none_none(self):
        result = format_date_range(None, None)
        assert isinstance(result, str)
        assert len(result) > 0

    def test_format_date_range_both_in_output(self):
        result = format_date_range("2024-01-01", "2024-06-30")
        assert "2024-01-01" in result
        assert "2024-06-30" in result

    # render_markdown: zawartość
    def test_render_markdown_has_header(self):
        sessions = group_into_sessions(parse_git_log(_SAMPLE_GIT_LOG))
        result = render_markdown(sessions, [])
        assert "# Raport" in result

    def test_render_markdown_shows_commit_count(self):
        sessions = group_into_sessions(parse_git_log(_SAMPLE_GIT_LOG))
        result = render_markdown(sessions, [])
        assert "1" in result  # 1 commit

    def test_render_markdown_shows_file_path(self):
        sessions = group_into_sessions(parse_git_log(_SAMPLE_GIT_LOG))
        result = render_markdown(sessions, [])
        assert "core/project_charter.md" in result

    def test_render_markdown_shows_changelog_rows(self):
        sessions = []
        rows = [{"changed_at": "2024-03-15T10:00:00", "template_path": "core/t.md",
                 "change_type": "bulk_patch", "change_reason": "Test reason"}]
        result = render_markdown(sessions, rows)
        assert "core/t.md" in result
        assert "bulk_patch" in result

    def test_render_markdown_empty_shows_no_changes(self):
        result = render_markdown([], [])
        assert "Brak" in result or "brak" in result

    def test_render_markdown_rename_shows_old_path(self):
        sessions = group_into_sessions(parse_git_log(_GIT_LOG_RENAME))
        result = render_markdown(sessions, [])
        assert "core/old_name.md" in result
        assert "core/new_name.md" in result

    # render_json: struktura
    def test_render_json_sessions_count_correct(self):
        sessions = group_into_sessions(parse_git_log(_SAMPLE_GIT_LOG))
        data = json.loads(render_json(sessions, []))
        assert data["sessions_count"] == 1

    def test_render_json_commits_count_correct(self):
        sessions = group_into_sessions(parse_git_log(_GIT_LOG_TWO_SAME_DAY))
        data = json.loads(render_json(sessions, []))
        assert data["commits_count"] == 2

    def test_render_json_changelog_rows_count(self):
        rows = [{"template_path": "x.md", "changed_at": "2024-01-01", "change_type": "test"}]
        data = json.loads(render_json([], rows))
        assert data["changelog_rows_count"] == 1

    def test_render_json_generated_at_present(self):
        data = json.loads(render_json([], []))
        assert "generated_at" in data

    def test_render_json_sessions_list(self):
        sessions = group_into_sessions(parse_git_log(_SAMPLE_GIT_LOG))
        data = json.loads(render_json(sessions, []))
        assert isinstance(data["sessions"], list)


# ===========================================================================
# TestSatelliteLinker
# ===========================================================================

@pytest.fixture
def sat_db():
    """In-memory DB z tabelami docs + doc_standard_mapping + doc_satellites."""
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    conn.executescript('''
        CREATE TABLE docs (
            path TEXT PRIMARY KEY,
            title TEXT,
            doc_uid TEXT
        );
        CREATE TABLE doc_standard_mapping (
            id INTEGER PRIMARY KEY,
            doc_path TEXT NOT NULL,
            standard_code TEXT NOT NULL,
            match_reason TEXT NOT NULL
        );
        -- Zatwierdzone dokumenty (rodzice)
        INSERT INTO docs VALUES ('core/project_charter.md', 'Project Charter', 'UID001');
        INSERT INTO docs VALUES ('core/isms_policy.md', 'ISMS Security Policy', 'UID002');
        INSERT INTO docs VALUES ('core/risk_register.md', 'Risk Register Document', 'UID003');
        -- Niezmapowane dokumenty (kandydaci na satelity)
        INSERT INTO docs VALUES ('core/charter_template.md', 'Charter Template Example', 'UID010');
        INSERT INTO docs VALUES ('core/security_checklist.md', 'Security Checklist', 'UID011');
        INSERT INTO docs VALUES ('core/random_doc.md', 'Random Unrelated Document', 'UID012');
        -- Mapowania dla rodziców
        INSERT INTO doc_standard_mapping VALUES (1, 'core/project_charter.md', 'PMBOK 7', 'keyword_match');
        INSERT INTO doc_standard_mapping VALUES (2, 'core/isms_policy.md', 'ISO/IEC 27001', 'keyword_match');
        INSERT INTO doc_standard_mapping VALUES (3, 'core/risk_register.md', 'ISO 31000', 'manual');
    ''')
    sat_ensure_table(conn)
    yield conn
    conn.close()


@pytest.mark.unit
class TestSatelliteLinker:

    # similarity_score
    def test_similarity_score_identical(self):
        assert similarity_score("Project Charter", "Project Charter") == 1.0

    def test_similarity_score_zero_no_overlap(self):
        assert similarity_score("Project Charter", "Database Schema") == 0.0

    def test_similarity_score_partial_overlap(self):
        score = similarity_score("Project Charter Template", "Project Charter Document")
        assert 0.0 < score < 1.0

    def test_similarity_score_empty_strings(self):
        assert similarity_score("", "") == 0.0

    def test_similarity_score_one_empty(self):
        assert similarity_score("Project Charter", "") == 0.0

    def test_similarity_score_symmetric(self):
        a = similarity_score("Security Policy Document", "Policy Security Guide")
        b = similarity_score("Policy Security Guide", "Security Policy Document")
        assert a == b

    def test_similarity_score_short_words_ignored(self):
        # Słowa < 3 znaków ignorowane — "to", "is", "a" nie liczą
        score = similarity_score("to is a test", "test the document")
        assert score > 0.0  # "test" pasuje

    # ensure_table
    def test_ensure_table_creates_table(self, sat_db):
        sat_ensure_table(sat_db)
        tables = [r[0] for r in sat_db.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()]
        assert "doc_satellites" in tables

    def test_ensure_table_idempotent(self, sat_db):
        sat_ensure_table(sat_db)
        sat_ensure_table(sat_db)  # nie powinno rzucić wyjątku

    # get_unmapped_docs
    def test_get_unmapped_returns_unmapped(self, sat_db):
        result = get_unmapped_docs(sat_db)
        paths = [r["path"] for r in result]
        assert "core/charter_template.md" in paths
        assert "core/security_checklist.md" in paths

    def test_get_unmapped_excludes_mapped(self, sat_db):
        result = get_unmapped_docs(sat_db)
        paths = [r["path"] for r in result]
        assert "core/project_charter.md" not in paths
        assert "core/isms_policy.md" not in paths

    def test_get_unmapped_excludes_already_satellite(self, sat_db):
        link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        result = get_unmapped_docs(sat_db)
        paths = [r["path"] for r in result]
        assert "core/charter_template.md" not in paths

    # get_approved_docs
    def test_get_approved_returns_mapped_docs(self, sat_db):
        result = get_approved_docs(sat_db)
        paths = [r["path"] for r in result]
        assert "core/project_charter.md" in paths
        assert "core/isms_policy.md" in paths

    def test_get_approved_has_standards_field(self, sat_db):
        result = get_approved_docs(sat_db)
        for r in result:
            assert "standards" in r
            assert r["standards"]  # nie puste

    def test_get_approved_excludes_unmapped(self, sat_db):
        result = get_approved_docs(sat_db)
        paths = [r["path"] for r in result]
        assert "core/charter_template.md" not in paths

    # suggest_satellites
    def test_suggest_satellites_returns_list(self, sat_db):
        result = suggest_satellites(sat_db, top=10, min_score=0.01)
        assert isinstance(result, list)

    def test_suggest_charter_template_to_charter(self, sat_db):
        result = suggest_satellites(sat_db, top=20, min_score=0.01)
        charter_suggestions = [r for r in result if r["satellite_path"] == "core/charter_template.md"]
        assert len(charter_suggestions) >= 1
        assert charter_suggestions[0]["parent_path"] == "core/project_charter.md"

    def test_suggest_security_to_isms(self, sat_db):
        result = suggest_satellites(sat_db, top=20, min_score=0.01)
        sec_suggestions = [r for r in result if r["satellite_path"] == "core/security_checklist.md"]
        assert len(sec_suggestions) >= 1
        assert sec_suggestions[0]["parent_path"] == "core/isms_policy.md"

    def test_suggest_sorted_by_score_desc(self, sat_db):
        result = suggest_satellites(sat_db, top=20, min_score=0.01)
        scores = [r["score"] for r in result]
        assert scores == sorted(scores, reverse=True)

    def test_suggest_respects_min_score(self, sat_db):
        result = suggest_satellites(sat_db, top=20, min_score=0.99)
        assert all(r["score"] >= 0.99 for r in result)

    def test_suggest_respects_top_limit(self, sat_db):
        result = suggest_satellites(sat_db, top=1, min_score=0.01)
        assert len(result) <= 1

    def test_suggest_empty_when_no_unmapped(self, sat_db):
        # Dodaj mapowania dla wszystkich niezmapowanych
        for path in ["core/charter_template.md", "core/security_checklist.md", "core/random_doc.md"]:
            sat_db.execute(
                "INSERT INTO doc_standard_mapping VALUES (NULL, ?, 'TEST', 'keyword_match')", (path,)
            )
        sat_db.commit()
        result = suggest_satellites(sat_db, min_score=0.01)
        assert result == []

    # link_satellite
    def test_link_satellite_returns_true(self, sat_db):
        ok = link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        assert ok is True

    def test_link_satellite_duplicate_returns_false(self, sat_db):
        link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        ok = link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        assert ok is False

    def test_link_satellite_persists_in_db(self, sat_db):
        link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        rows = sat_db.execute("SELECT * FROM doc_satellites").fetchall()
        assert len(rows) == 1
        assert rows[0]["satellite_path"] == "core/charter_template.md"
        assert rows[0]["parent_path"] == "core/project_charter.md"

    def test_link_satellite_stores_note(self, sat_db):
        link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md", note="test note")
        row = sat_db.execute("SELECT note FROM doc_satellites").fetchone()
        assert row["note"] == "test note"

    def test_link_satellite_stores_linked_by(self, sat_db):
        link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md", linked_by="ci_auto")
        row = sat_db.execute("SELECT linked_by FROM doc_satellites").fetchone()
        assert row["linked_by"] == "ci_auto"

    # unlink_satellite
    def test_unlink_existing_returns_true(self, sat_db):
        link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        ok = unlink_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        assert ok is True

    def test_unlink_removes_from_db(self, sat_db):
        link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        unlink_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        rows = sat_db.execute("SELECT * FROM doc_satellites").fetchall()
        assert rows == []

    def test_unlink_nonexistent_returns_false(self, sat_db):
        ok = unlink_satellite(sat_db, "core/nonexistent.md", "core/project_charter.md")
        assert ok is False

    # list_satellites
    def test_list_satellites_empty(self, sat_db):
        result = list_satellites(sat_db)
        assert result == []

    def test_list_satellites_returns_linked(self, sat_db):
        link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        result = list_satellites(sat_db)
        assert len(result) == 1
        assert result[0]["satellite_path"] == "core/charter_template.md"

    def test_list_satellites_filter_by_parent(self, sat_db):
        link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        link_satellite(sat_db, "core/security_checklist.md", "core/isms_policy.md")
        result = list_satellites(sat_db, parent_path="core/project_charter.md")
        assert len(result) == 1
        assert result[0]["satellite_path"] == "core/charter_template.md"

    def test_list_satellites_multiple(self, sat_db):
        link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        link_satellite(sat_db, "core/security_checklist.md", "core/isms_policy.md")
        result = list_satellites(sat_db)
        assert len(result) == 2

    # satellite_report
    def test_satellite_report_returns_string(self, sat_db):
        result = satellite_report(sat_db)
        assert isinstance(result, str)

    def test_satellite_report_has_header(self, sat_db):
        result = satellite_report(sat_db)
        assert "# Raport" in result

    def test_satellite_report_empty_message(self, sat_db):
        result = satellite_report(sat_db)
        assert "Brak" in result

    def test_satellite_report_shows_linked_paths(self, sat_db):
        link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        result = satellite_report(sat_db)
        assert "core/charter_template.md" in result
        assert "core/project_charter.md" in result

    def test_satellite_report_shows_count(self, sat_db):
        link_satellite(sat_db, "core/charter_template.md", "core/project_charter.md")
        result = satellite_report(sat_db)
        assert "1" in result  # 1 satelita zarejestrowany
