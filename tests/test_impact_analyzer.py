"""Tests for scripts/maintenance/impact_analyzer.py."""
import pytest
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.maintenance.impact_analyzer import (
    analyze_standard, analyze_regulation, analyze_section, analyze_doc
)

pytestmark = pytest.mark.unit


@pytest.fixture
def mem_conn():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row

    conn.executescript("""
        CREATE TABLE standards (
            standard_code TEXT PRIMARY KEY,
            standard_name TEXT
        );
        CREATE TABLE compliance_regulations (
            regulation_code TEXT PRIMARY KEY,
            regulation_name TEXT
        );
        CREATE TABLE docs (
            doc_uid TEXT PRIMARY KEY,
            title TEXT,
            path TEXT
        );
        CREATE TABLE doc_standard_mapping (
            doc_path TEXT,
            standard_code TEXT,
            match_reason TEXT
        );
        CREATE TABLE doc_regulation_mapping (
            doc_path TEXT,
            regulation_code TEXT,
            match_reason TEXT
        );
        CREATE TABLE sections (
            section_uid TEXT PRIMARY KEY,
            doc_uid TEXT,
            heading_text TEXT,
            anchor TEXT,
            ordinal INTEGER
        );
        CREATE TABLE content_links (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            context_doc_uid TEXT,
            to_ref TEXT
        );
    """)

    conn.executemany("INSERT INTO standards VALUES (?,?)", [
        ("ISO/IEC 27001", "Information Security Management"),
        ("ISO 9001", "Quality Management Systems"),
    ])
    conn.executemany("INSERT INTO compliance_regulations VALUES (?,?)", [
        ("RODO", "Rozporządzenie o Ochronie Danych Osobowych"),
        ("KSC-PL", "Ustawa o Krajowym Systemie Cyberbezpieczeństwa"),
    ])
    conn.executemany("INSERT INTO docs VALUES (?,?,?)", [
        ("uid-001", "Security Policy Document", "core/security_policy.md"),
        ("uid-002", "Access Control Guide", "core/access_control.md"),
        ("uid-003", "Data Privacy Policy", "compliance/data_privacy.md"),
    ])
    conn.executemany("INSERT INTO doc_standard_mapping VALUES (?,?,?)", [
        ("core/security_policy.md", "ISO/IEC 27001", "title match"),
        ("core/access_control.md", "ISO/IEC 27001", "keyword match"),
    ])
    conn.executemany("INSERT INTO doc_regulation_mapping VALUES (?,?,?)", [
        ("compliance/data_privacy.md", "RODO", "direct reference"),
        ("core/security_policy.md", "KSC-PL", "compliance section"),
    ])
    conn.executemany("INSERT INTO sections VALUES (?,?,?,?,?)", [
        ("sec-001", "uid-001", "Standardy i compliance", "#standardy", 1),
        ("sec-002", "uid-001", "Zakres stosowania", "#zakres", 2),
        ("sec-003", "uid-002", "Standardy i compliance", "#standardy", 1),
    ])
    conn.executemany("INSERT INTO content_links VALUES (NULL,?,?)", [
        ("uid-002", "document::Security Policy Document::section-1"),
        ("uid-003", "document::Access Control Guide::section-1"),
    ])
    conn.commit()
    return conn


class TestAnalyzeStandard:
    def test_found_standard(self, mem_conn):
        result = analyze_standard(mem_conn, "ISO/IEC 27001")
        assert result.get("query_type") == "standard"
        assert result.get("total_affected") == 2
        assert len(result["matched_standards"]) == 1
        assert result["matched_standards"][0]["count"] == 2

    def test_standard_not_found(self, mem_conn):
        result = analyze_standard(mem_conn, "NONEXISTENT-STD-999")
        assert "error" in result
        assert "NONEXISTENT-STD-999" in result["error"]

    def test_partial_match(self, mem_conn):
        result = analyze_standard(mem_conn, "27001")
        assert result.get("query_type") == "standard"
        assert result.get("total_affected") >= 1

    def test_result_structure(self, mem_conn):
        result = analyze_standard(mem_conn, "ISO/IEC 27001")
        assert "query" in result
        assert "matched_standards" in result
        assert result["query"] == "ISO/IEC 27001"


class TestAnalyzeRegulation:
    def test_found_regulation(self, mem_conn):
        result = analyze_regulation(mem_conn, "RODO")
        assert result.get("query_type") == "regulation"
        assert result.get("total_affected") == 1

    def test_regulation_not_found(self, mem_conn):
        result = analyze_regulation(mem_conn, "GDPR-NONEXISTENT")
        assert "error" in result

    def test_result_has_affected_templates(self, mem_conn):
        result = analyze_regulation(mem_conn, "RODO")
        assert len(result["matched_regulations"]) == 1
        reg = result["matched_regulations"][0]
        assert reg["regulation_code"] == "RODO"
        assert len(reg["affected_templates"]) == 1

    def test_ksc_regulation(self, mem_conn):
        result = analyze_regulation(mem_conn, "KSC-PL")
        assert result.get("total_affected") == 1
        assert result["matched_regulations"][0]["regulation_name"] is not None


class TestAnalyzeSection:
    def test_found_section(self, mem_conn):
        result = analyze_section(mem_conn, "Standardy i compliance")
        assert result.get("query_type") == "section"
        assert result.get("templates_count") == 2

    def test_section_not_found(self, mem_conn):
        result = analyze_section(mem_conn, "NonExistentSection XYZ 999")
        assert result.get("templates_count") == 0
        assert result.get("query_type") == "section"

    def test_result_has_note(self, mem_conn):
        result = analyze_section(mem_conn, "Standardy")
        assert "note" in result
        assert isinstance(result["note"], str)

    def test_content_links_count(self, mem_conn):
        result = analyze_section(mem_conn, "Standardy i compliance")
        assert "content_links_referencing" in result
        assert isinstance(result["content_links_referencing"], int)

    def test_templates_list_structure(self, mem_conn):
        result = analyze_section(mem_conn, "Standardy")
        for tpl in result["templates_with_section"]:
            assert "path" in tpl
            assert "heading" in tpl


class TestAnalyzeDoc:
    def test_found_doc(self, mem_conn):
        result = analyze_doc(mem_conn, "Security Policy")
        assert result.get("query_type") == "document"
        assert result.get("count") >= 1

    def test_doc_not_found(self, mem_conn):
        result = analyze_doc(mem_conn, "NonExistentDocumentXYZ999")
        assert "error" in result

    def test_result_has_links(self, mem_conn):
        result = analyze_doc(mem_conn, "Security Policy")
        doc = result["matched_docs"][0]
        assert "incoming_links" in doc
        assert "outgoing_links" in doc

    def test_result_has_standards(self, mem_conn):
        result = analyze_doc(mem_conn, "Security Policy")
        doc = result["matched_docs"][0]
        assert "standards" in doc
        assert "ISO/IEC 27001" in doc["standards"]

    def test_result_has_sections(self, mem_conn):
        result = analyze_doc(mem_conn, "Security Policy")
        doc = result["matched_docs"][0]
        assert "sections" in doc
        assert any(s["heading"] == "Standardy i compliance" for s in doc["sections"])

    def test_partial_title_match(self, mem_conn):
        result = analyze_doc(mem_conn, "Policy")
        assert result.get("count") >= 1
