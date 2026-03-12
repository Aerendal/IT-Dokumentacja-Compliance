"""tests/test_compliance_report.py

Unit tests for scripts/compliance_coverage_report.py.
All tests use in-memory SQLite — no real DB required.
"""

import csv
import io
import json
import sqlite3
from pathlib import Path

import pytest

pytestmark = pytest.mark.unit

# Make sure the scripts package is importable regardless of working directory
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from compliance_coverage_report import (
    compute_control_metrics,
    compute_regulation_metrics,
    compute_standard_metrics,
    generate_csv_report,
    generate_json_report,
    generate_text_report,
    _filter_gaps,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def conn():
    """In-memory SQLite with minimal schema and seed data."""
    c = sqlite3.connect(":memory:")
    c.executescript("""
    CREATE TABLE standards (
        standard_code TEXT PRIMARY KEY,
        standard_name TEXT,
        description TEXT,
        applicable_industries TEXT,
        url TEXT,
        version TEXT
    );
    CREATE TABLE compliance_regulations (
        regulation_code TEXT PRIMARY KEY,
        regulation_name TEXT,
        key_requirements TEXT,
        jurisdiction TEXT,
        industry TEXT,
        penalty_info TEXT
    );
    CREATE TABLE doc_standard_mapping (
        id INTEGER PRIMARY KEY,
        doc_path TEXT,
        standard_code TEXT,
        match_reason TEXT,
        confidence REAL
    );
    CREATE TABLE doc_section_guidance (
        id INTEGER PRIMARY KEY,
        doc_title TEXT,
        section_title TEXT,
        guidance TEXT,
        standards_refs TEXT,
        regulations_refs TEXT
    );
    CREATE TABLE guidance_standard_links (
        guidance_id INTEGER,
        standard_code TEXT,
        PRIMARY KEY(guidance_id, standard_code)
    );
    CREATE TABLE guidance_regulation_links (
        guidance_id INTEGER,
        regulation_code TEXT,
        PRIMARY KEY(guidance_id, regulation_code)
    );

    INSERT INTO standards VALUES
        ('ISO/IEC 27001', 'ISMS', 'Security management', 'IT', '', '2022');
    INSERT INTO standards VALUES
        ('NIST CSF', 'NIST Framework', 'Cyber security', 'IT', '', '2.0');
    INSERT INTO compliance_regulations VALUES
        ('RODO', 'GDPR PL', 'Data protection', 'Polska', 'All', 'Fine');
    INSERT INTO compliance_regulations VALUES
        ('KSC-PL', 'Krajowy System Cyberbezpieczenstwa', 'Cyber', 'Polska', 'IT', 'None');
    """)
    c.commit()
    return c


# ---------------------------------------------------------------------------
# Tests: compute_standard_metrics
# ---------------------------------------------------------------------------

def test_compute_standard_metrics_empty(conn):
    """No mappings → all counts are zero."""
    m = compute_standard_metrics(conn, "ISO/IEC 27001")
    assert m["total_mappings"] == 0
    assert m["high_conf_50"] == 0
    assert m["high_conf_70"] == 0
    assert m["high_conf_90"] == 0
    assert m["guidance_sections"] == 0


def test_compute_standard_metrics_with_data(conn):
    """Insert 3 mappings with conf 0.3, 0.6, 0.8 — verify counts."""
    conn.executescript("""
        INSERT INTO doc_standard_mapping VALUES (1, 'doc1.md', 'ISO/IEC 27001', 'keyword_match', 0.3);
        INSERT INTO doc_standard_mapping VALUES (2, 'doc2.md', 'ISO/IEC 27001', 'keyword_match', 0.6);
        INSERT INTO doc_standard_mapping VALUES (3, 'doc3.md', 'ISO/IEC 27001', 'keyword_match', 0.8);
    """)
    m = compute_standard_metrics(conn, "ISO/IEC 27001")
    assert m["total_mappings"] == 3
    assert m["high_conf_50"] == 2   # 0.6 and 0.8
    assert m["high_conf_70"] == 1   # only 0.8
    assert m["high_conf_90"] == 0   # none


def test_high_confidence_threshold(conn):
    """Threshold boundaries: exactly 0.5, 0.7, 0.9 should count as high."""
    conn.executescript("""
        INSERT INTO doc_standard_mapping VALUES (10, 'a.md', 'NIST CSF', 'k', 0.5);
        INSERT INTO doc_standard_mapping VALUES (11, 'b.md', 'NIST CSF', 'k', 0.7);
        INSERT INTO doc_standard_mapping VALUES (12, 'c.md', 'NIST CSF', 'k', 0.9);
        INSERT INTO doc_standard_mapping VALUES (13, 'd.md', 'NIST CSF', 'k', 0.49);
        INSERT INTO doc_standard_mapping VALUES (14, 'e.md', 'NIST CSF', 'k', 0.69);
        INSERT INTO doc_standard_mapping VALUES (15, 'f.md', 'NIST CSF', 'k', 0.89);
    """)
    m = compute_standard_metrics(conn, "NIST CSF")
    assert m["total_mappings"] == 6
    # >=0.5: 0.5, 0.69, 0.7, 0.89, 0.9  → 5
    assert m["high_conf_50"] == 5
    # >=0.7: 0.7, 0.89, 0.9             → 3
    assert m["high_conf_70"] == 3
    # >=0.9: 0.9 only                   → 1
    assert m["high_conf_90"] == 1


def test_compute_standard_metrics_other_standard_not_counted(conn):
    """Mappings for a different standard should not affect counts."""
    conn.executescript("""
        INSERT INTO doc_standard_mapping VALUES (20, 'x.md', 'NIST CSF', 'k', 0.9);
    """)
    m = compute_standard_metrics(conn, "ISO/IEC 27001")
    assert m["total_mappings"] == 0


def test_compute_standard_metrics_guidance_sections(conn):
    """guidance_sections counts rows in guidance_standard_links."""
    conn.executescript("""
        INSERT INTO doc_section_guidance VALUES (1, 'DocA', 'Sec1', 'g1', '', '');
        INSERT INTO doc_section_guidance VALUES (2, 'DocA', 'Sec2', 'g2', '', '');
        INSERT INTO doc_section_guidance VALUES (3, 'DocB', 'Sec1', 'g3', '', '');
        INSERT INTO guidance_standard_links VALUES (1, 'ISO/IEC 27001');
        INSERT INTO guidance_standard_links VALUES (2, 'ISO/IEC 27001');
        INSERT INTO guidance_standard_links VALUES (3, 'NIST CSF');
    """)
    m_iso = compute_standard_metrics(conn, "ISO/IEC 27001")
    assert m_iso["guidance_sections"] == 2
    m_nist = compute_standard_metrics(conn, "NIST CSF")
    assert m_nist["guidance_sections"] == 1


# ---------------------------------------------------------------------------
# Tests: compute_regulation_metrics
# ---------------------------------------------------------------------------

def test_compute_regulation_metrics_empty(conn):
    """No guidance links → zeros."""
    m = compute_regulation_metrics(conn, "RODO")
    assert m["guidance_sections"] == 0
    assert m["unique_docs"] == 0


def test_compute_regulation_metrics_with_data(conn):
    """Insert guidance rows + links → verify counts."""
    conn.executescript("""
        INSERT INTO doc_section_guidance VALUES (1, 'DocA', 'Sec1', 'g1', '', '');
        INSERT INTO doc_section_guidance VALUES (2, 'DocA', 'Sec2', 'g2', '', '');
        INSERT INTO doc_section_guidance VALUES (3, 'DocB', 'Sec1', 'g3', '', '');
        INSERT INTO guidance_regulation_links VALUES (1, 'RODO');
        INSERT INTO guidance_regulation_links VALUES (2, 'RODO');
        INSERT INTO guidance_regulation_links VALUES (3, 'RODO');
    """)
    m = compute_regulation_metrics(conn, "RODO")
    assert m["guidance_sections"] == 3
    assert m["unique_docs"] == 2   # DocA and DocB


# ---------------------------------------------------------------------------
# Tests: generate_json_report
# ---------------------------------------------------------------------------

def test_generate_json_report_structure(conn):
    """Returned dict must have required top-level keys."""
    data = generate_json_report(conn,
                                [{"standard_code": "ISO/IEC 27001", "standard_name": "ISMS"}],
                                [{"regulation_code": "RODO", "regulation_name": "GDPR PL"}])
    assert "standards" in data
    assert "regulations" in data
    assert "generated_at" in data
    assert "total_templates" in data


def test_generate_json_report_standard_fields(conn):
    """Each standard entry must include required fields."""
    conn.executescript("""
        INSERT INTO doc_standard_mapping VALUES (1, 'a.md', 'ISO/IEC 27001', 'k', 0.8);
    """)
    data = generate_json_report(conn,
                                [{"standard_code": "ISO/IEC 27001", "standard_name": "ISMS"}],
                                [])
    std = data["standards"][0]
    assert "standard_code" in std
    assert "name" in std
    assert "total_mappings" in std
    assert "high_conf_50" in std
    assert "high_conf_70" in std
    assert "high_conf_90" in std
    assert "guidance_sections" in std
    assert "coverage_pct_50" in std
    assert std["total_mappings"] == 1
    assert std["high_conf_50"] == 1


def test_generate_json_report_is_serialisable(conn):
    """generate_json_report output must be JSON-serialisable."""
    data = generate_json_report(conn,
                                [{"standard_code": "NIST CSF", "standard_name": "NIST"}],
                                [{"regulation_code": "KSC-PL", "regulation_name": "KSC"}])
    serialised = json.dumps(data)
    parsed = json.loads(serialised)
    assert parsed["standards"][0]["standard_code"] == "NIST CSF"


# ---------------------------------------------------------------------------
# Tests: generate_text_report
# ---------------------------------------------------------------------------

def test_generate_text_report_contains_standard_name(conn):
    """Text output should include the standard name."""
    text = generate_text_report(conn,
                                [{"standard_code": "ISO/IEC 27001", "standard_name": "ISMS"}],
                                [])
    assert "ISMS" in text


def test_generate_text_report_contains_regulation(conn):
    """Text output should include the regulation code."""
    text = generate_text_report(conn, [],
                                [{"regulation_code": "RODO", "regulation_name": "GDPR PL"}])
    assert "RODO" in text


# ---------------------------------------------------------------------------
# Tests: gap filtering
# ---------------------------------------------------------------------------

def test_show_gaps_filters_correctly(conn):
    """_filter_gaps: standards with low coverage should be kept; high coverage removed."""
    conn.executescript("""
        -- 10 docs total
        INSERT INTO doc_standard_mapping VALUES (1,  'd1.md',  'ISO/IEC 27001', 'k', 0.9);
        INSERT INTO doc_standard_mapping VALUES (2,  'd2.md',  'ISO/IEC 27001', 'k', 0.9);
        INSERT INTO doc_standard_mapping VALUES (3,  'd3.md',  'ISO/IEC 27001', 'k', 0.9);
        INSERT INTO doc_standard_mapping VALUES (4,  'd4.md',  'ISO/IEC 27001', 'k', 0.9);
        INSERT INTO doc_standard_mapping VALUES (5,  'd5.md',  'ISO/IEC 27001', 'k', 0.9);
        INSERT INTO doc_standard_mapping VALUES (6,  'd6.md',  'ISO/IEC 27001', 'k', 0.9);
        INSERT INTO doc_standard_mapping VALUES (7,  'd7.md',  'NIST CSF',      'k', 0.1);
        INSERT INTO doc_standard_mapping VALUES (8,  'd8.md',  'NIST CSF',      'k', 0.1);
        INSERT INTO doc_standard_mapping VALUES (9,  'd9.md',  'NIST CSF',      'k', 0.1);
        INSERT INTO doc_standard_mapping VALUES (10, 'd10.md', 'NIST CSF',      'k', 0.1);
    """)
    # 10 total docs; ISO has 6 high-conf (60%) → above 0.5; NIST has 0 high-conf → gap
    standards = [
        {"standard_code": "ISO/IEC 27001", "standard_name": "ISMS"},
        {"standard_code": "NIST CSF",      "standard_name": "NIST Framework"},
    ]
    filtered_std, _ = _filter_gaps(conn, standards, [], min_confidence=0.5)
    codes = [s["standard_code"] for s in filtered_std]
    assert "ISO/IEC 27001" not in codes
    assert "NIST CSF" in codes


# ---------------------------------------------------------------------------
# Tests: generate_csv_report
# ---------------------------------------------------------------------------

def test_csv_output_has_headers(conn):
    """Standards CSV must start with the correct column headers."""
    std_csv, reg_csv = generate_csv_report(conn,
                                           [{"standard_code": "ISO/IEC 27001", "standard_name": "ISMS"}],
                                           [{"regulation_code": "RODO", "regulation_name": "GDPR PL"}])
    reader = csv.reader(io.StringIO(std_csv))
    header = next(reader)
    assert header == ["standard_code", "standard_name", "total_mappings",
                      "high_conf_50", "high_conf_70", "high_conf_90", "guidance_sections"]


def test_csv_regulations_has_headers(conn):
    """Regulations CSV must start with the correct column headers."""
    _, reg_csv = generate_csv_report(conn, [],
                                     [{"regulation_code": "RODO", "regulation_name": "GDPR PL"}])
    reader = csv.reader(io.StringIO(reg_csv))
    header = next(reader)
    assert header == ["regulation_code", "regulation_name", "guidance_sections", "unique_docs"]


# ---------------------------------------------------------------------------
# Integration tests (require real DB at reports/it_doc_matrix.db)
# ---------------------------------------------------------------------------

@pytest.mark.integration
class TestComplianceE2E:
    """Integration tests: require real DB at reports/it_doc_matrix.db"""

    @pytest.fixture
    def real_conn(self):
        db = Path('reports/it_doc_matrix.db')
        if not db.exists():
            pytest.skip("Real DB not available")
        return sqlite3.connect(str(db))

    def test_no_null_confidence_keyword_match(self, real_conn):
        """After backfill: zero keyword_match rows with NULL confidence"""
        cur = real_conn.cursor()
        cur.execute("SELECT COUNT(*) FROM doc_standard_mapping WHERE confidence IS NULL AND match_reason='keyword_match'")
        assert cur.fetchone()[0] == 0

    def test_guidance_standard_links_populated(self, real_conn):
        """guidance_standard_links has >1M rows"""
        cur = real_conn.cursor()
        cur.execute("SELECT COUNT(*) FROM guidance_standard_links")
        assert cur.fetchone()[0] > 1_000_000

    def test_iso27001_has_substantial_mappings(self, real_conn):
        """ISO/IEC 27001 has >500 total mappings and at least some with confidence >= 0.3"""
        from scripts.compliance_coverage_report import compute_standard_metrics
        metrics = compute_standard_metrics(real_conn, 'ISO/IEC 27001', min_confidence=0.5)
        # Total mappings must be substantial
        assert metrics['total_mappings'] >= 500
        # At least some with confidence >= 0.3 (keyword_match_scored + candidate_match)
        cur = real_conn.cursor()
        cur.execute(
            "SELECT COUNT(*) FROM doc_standard_mapping WHERE standard_code='ISO/IEC 27001' AND confidence >= 0.3"
        )
        assert cur.fetchone()[0] >= 100

    def test_compliance_report_json_valid(self):
        """compliance_report.json exists and has correct structure"""
        report_path = Path('reports/compliance_report.json')
        if not report_path.exists():
            pytest.skip("Report not generated yet")
        data = json.loads(report_path.read_text())
        assert 'standards' in data
        assert 'regulations' in data
        assert len(data['standards']) > 0

    def test_template_violations_table_exists(self, real_conn):
        """template_violations table exists in DB"""
        cur = real_conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='template_violations'")
        assert cur.fetchone() is not None


# ---------------------------------------------------------------------------
# Tests: compute_control_metrics
# ---------------------------------------------------------------------------

class TestControlMetrics:

    @pytest.fixture
    def conn(self):
        c = sqlite3.connect(":memory:")
        c.executescript("""
        CREATE TABLE standard_controls (
            id INTEGER PRIMARY KEY, standard_code TEXT, control_id TEXT,
            control_name TEXT, theme TEXT, description TEXT
        );
        CREATE TABLE doc_control_mapping (
            id INTEGER PRIMARY KEY, doc_path TEXT, standard_code TEXT,
            control_id TEXT, confidence REAL
        );
        INSERT INTO standard_controls VALUES (1,'ISO/IEC 27001','A.5.1','Policies','Organizational','...');
        INSERT INTO standard_controls VALUES (2,'ISO/IEC 27001','A.5.2','Roles','Organizational','...');
        INSERT INTO standard_controls VALUES (3,'ISO/IEC 27001','A.8.1','Endpoints','Technological','...');
        INSERT INTO doc_control_mapping VALUES (1,'core/a.md','ISO/IEC 27001','A.5.1',0.3);
        INSERT INTO doc_control_mapping VALUES (2,'core/b.md','ISO/IEC 27001','A.5.1',0.4);
        INSERT INTO doc_control_mapping VALUES (3,'core/c.md','ISO/IEC 27001','A.5.1',0.5);
        INSERT INTO doc_control_mapping VALUES (4,'core/d.md','ISO/IEC 27001','A.5.1',0.6);
        INSERT INTO doc_control_mapping VALUES (5,'core/e.md','ISO/IEC 27001','A.5.1',0.7);
        INSERT INTO doc_control_mapping VALUES (6,'core/f.md','ISO/IEC 27001','A.5.1',0.8);
        INSERT INTO doc_control_mapping VALUES (7,'core/g.md','ISO/IEC 27001','A.5.1',0.9);
        INSERT INTO doc_control_mapping VALUES (8,'core/h.md','ISO/IEC 27001','A.5.1',1.0);
        INSERT INTO doc_control_mapping VALUES (9,'core/i.md','ISO/IEC 27001','A.5.1',0.5);
        INSERT INTO doc_control_mapping VALUES (10,'core/j.md','ISO/IEC 27001','A.5.1',0.6);
        INSERT INTO doc_control_mapping VALUES (11,'core/k.md','ISO/IEC 27001','A.5.2',0.3);
        """)
        c.commit()
        return c

    def test_returns_all_controls(self, conn):
        """Result has one entry per control in standard_controls."""
        result = compute_control_metrics(conn, "ISO/IEC 27001")
        assert len(result) == 3

    def test_high_tier_threshold(self, conn):
        """A.5.1 has 10 templates → tier='high'."""
        result = compute_control_metrics(conn, "ISO/IEC 27001")
        a51 = next(r for r in result if r["control_id"] == "A.5.1")
        assert a51["template_count"] == 10
        assert a51["coverage_tier"] == "high"

    def test_low_tier_threshold(self, conn):
        """A.5.2 has 1 template → tier='low'."""
        result = compute_control_metrics(conn, "ISO/IEC 27001")
        a52 = next(r for r in result if r["control_id"] == "A.5.2")
        assert a52["template_count"] == 1
        assert a52["coverage_tier"] == "low"

    def test_none_tier_no_templates(self, conn):
        """A.8.1 has 0 templates → tier='none' and template_count=0."""
        result = compute_control_metrics(conn, "ISO/IEC 27001")
        a81 = next(r for r in result if r["control_id"] == "A.8.1")
        assert a81["template_count"] == 0
        assert a81["coverage_tier"] == "none"

    def test_avg_confidence_calculated(self, conn):
        """A.5.1 avg_confidence matches expected value."""
        result = compute_control_metrics(conn, "ISO/IEC 27001")
        a51 = next(r for r in result if r["control_id"] == "A.5.1")
        # 0.3+0.4+0.5+0.6+0.7+0.8+0.9+1.0+0.5+0.6 = 6.3 / 10 = 0.63
        assert a51["avg_confidence"] == pytest.approx(0.63, abs=0.001)

    def test_sorted_by_theme_and_id(self, conn):
        """Results are sorted theme ASC, control_id ASC."""
        result = compute_control_metrics(conn, "ISO/IEC 27001")
        themes = [r["theme"] for r in result]
        assert themes == sorted(themes)
        # Within same theme, control_id is sorted
        org_ids = [r["control_id"] for r in result if r["theme"] == "Organizational"]
        assert org_ids == sorted(org_ids)

    def test_nonexistent_standard_returns_empty(self, conn):
        """standard_code='FAKE' returns empty list."""
        result = compute_control_metrics(conn, "FAKE")
        assert result == []

    def test_control_names_present(self, conn):
        """All result dicts have 'control_name' key."""
        result = compute_control_metrics(conn, "ISO/IEC 27001")
        for item in result:
            assert "control_name" in item
            assert item["control_name"]
