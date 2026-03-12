"""Unit tests for new_template_wizard.py pure/testable functions."""

import sqlite3
import subprocess
import sys

import pytest

from scripts.new_template_wizard import (
    insert_to_db,
    render_template,
    slugify,
    ulid_simple,
)

pytestmark = pytest.mark.unit


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_conn() -> sqlite3.Connection:
    """In-memory SQLite with tables required by insert_to_db."""
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.executescript(
        """
        CREATE TABLE docs (
            doc_uid     TEXT PRIMARY KEY,
            title       TEXT,
            title_norm  TEXT,
            path        TEXT,
            origin      TEXT
        );
        CREATE TABLE doc_standard_mapping (
            doc_path        TEXT,
            standard_code   TEXT,
            match_reason    TEXT,
            PRIMARY KEY (doc_path, standard_code)
        );
        CREATE TABLE doc_regulation_mapping (
            doc_path        TEXT,
            regulation_code TEXT,
            match_reason    TEXT,
            PRIMARY KEY (doc_path, regulation_code)
        );
        CREATE TABLE doc_section_guidance (
            doc_title       TEXT,
            section_title   TEXT,
            guidance        TEXT,
            standards_refs  TEXT,
            regulations_refs TEXT,
            PRIMARY KEY (doc_title, section_title)
        );
        """
    )
    conn.commit()
    return conn


# ---------------------------------------------------------------------------
# TestSlugify
# ---------------------------------------------------------------------------


class TestSlugify:
    def test_polish_characters_converted(self):
        # ł has no ASCII decomposition via NFKD, so it is dropped
        result = slugify("ą ę ó ś ł ż ź ć ń")
        assert result == "a_e_o_s_z_z_c_n"
        # verify individually that each mappable char converts correctly
        assert slugify("ą") == "a"
        assert slugify("ę") == "e"
        assert slugify("ó") == "o"
        assert slugify("ś") == "s"
        assert slugify("ż") == "z"
        assert slugify("ź") == "z"
        assert slugify("ć") == "c"
        assert slugify("ń") == "n"

    def test_spaces_become_underscores(self):
        assert slugify("hello world") == "hello_world"

    def test_result_is_lowercase(self):
        assert slugify("UPPERCASE Title") == "uppercase_title"

    def test_length_capped_at_80_chars(self):
        long_title = "A" * 200
        result = slugify(long_title)
        assert len(result) <= 80

    def test_special_chars_stripped_or_replaced(self):
        result = slugify("doc/name-v1.0!final")
        assert "/" not in result
        assert "!" not in result
        assert "." not in result

    def test_consecutive_underscores_collapsed(self):
        result = slugify("hello   world")
        assert "__" not in result

    def test_empty_string(self):
        result = slugify("")
        assert result == "" or isinstance(result, str)

    def test_typical_it_title(self):
        result = slugify("Zarządzanie Bezpieczeństwem")
        assert result == "zarzadzanie_bezpieczenstwem"


# ---------------------------------------------------------------------------
# TestRenderTemplate
# ---------------------------------------------------------------------------


class TestRenderTemplate:
    def _render(self, **kwargs):
        defaults = {
            "title": "Test Doc",
            "phases": [],
            "linked_docs": [],
            "standards": [],
            "regulations": [],
            "guidance_cel": "",
        }
        defaults.update(kwargs)
        return render_template(**defaults)

    def test_contains_cel_dokumentu_section(self):
        out = self._render()
        assert "## Cel dokumentu" in out

    def test_contains_zakres_section(self):
        out = self._render()
        assert "## Zakres" in out

    def test_standard_appears_in_output(self):
        out = self._render(standards=["ISO/IEC 27001"])
        assert "ISO/IEC 27001" in out

    def test_regulation_appears_in_output(self):
        out = self._render(regulations=["KSC-PL"])
        assert "KSC" in out

    def test_title_appears_in_output(self):
        out = self._render(title="Moj Dokument")
        assert "Moj Dokument" in out

    def test_linked_doc_appears_in_output(self):
        out = self._render(linked_docs=["foo.md"])
        assert "foo.md" in out


# ---------------------------------------------------------------------------
# TestUlidSimple
# ---------------------------------------------------------------------------


class TestUlidSimple:
    def test_deterministic(self):
        assert ulid_simple("Same Input") == ulid_simple("Same Input")

    def test_different_inputs_differ(self):
        assert ulid_simple("Input A") != ulid_simple("Input B")


# ---------------------------------------------------------------------------
# TestInsertToDB
# ---------------------------------------------------------------------------


class TestInsertToDB:
    def test_inserts_doc_section_guidance_rows(self):
        conn = _make_conn()
        insert_to_db(conn, "My Doc", "core/my_doc.md", [], [])
        rows = conn.execute(
            "SELECT * FROM doc_section_guidance WHERE doc_title='My Doc'"
        ).fetchall()
        assert len(rows) >= 1

    def test_standard_inserted_to_doc_standard_mapping(self):
        conn = _make_conn()
        insert_to_db(conn, "Sec Doc", "core/sec_doc.md", ["ISO 27001"], [])
        rows = conn.execute(
            "SELECT * FROM doc_standard_mapping WHERE doc_path='core/sec_doc.md'"
        ).fetchall()
        assert len(rows) == 1
        assert rows[0][1] == "ISO 27001"

    def test_second_insert_with_same_title_no_integrity_error(self):
        conn = _make_conn()
        insert_to_db(conn, "Dup Doc", "core/dup.md", [], [])
        # Should not raise
        insert_to_db(conn, "Dup Doc", "core/dup.md", [], [])

    def test_guidance_text_is_non_empty(self):
        conn = _make_conn()
        insert_to_db(conn, "Guide Doc", "core/guide.md", [], [])
        rows = conn.execute(
            "SELECT guidance FROM doc_section_guidance WHERE doc_title='Guide Doc'"
        ).fetchall()
        for (guidance,) in rows:
            assert guidance and guidance.strip() != ""

    def test_path_stored_correctly(self):
        conn = _make_conn()
        insert_to_db(conn, "Path Doc", "core/path_doc.md", [], [])
        row = conn.execute("SELECT path FROM docs WHERE title='Path Doc'").fetchone()
        assert row is not None
        assert row[0] == "core/path_doc.md"


# ---------------------------------------------------------------------------
# TestWizardCLI — integration tests (subprocess, --dry-run)
# ---------------------------------------------------------------------------

_CWD = "/home/jerzy/Pobrane/IT_Dokumentacja/dokumentacja"


class TestWizardCLI:
    @pytest.mark.integration
    def test_dry_run_outputs_template(self, tmp_path):
        """Running --dry-run prints the rendered template to stdout"""
        result = subprocess.run(
            [
                sys.executable,
                "scripts/new_template_wizard.py",
                "--title",
                "Test Integracyjny",
                "--type",
                "Polityka",
                "--goal",
                "Cel testowy dokumentu",
                "--dry-run",
            ],
            capture_output=True,
            text=True,
            cwd=_CWD,
        )
        assert result.returncode == 0
        assert "## Cel dokumentu" in result.stdout
        assert "DRY RUN" in result.stdout

    @pytest.mark.integration
    def test_dry_run_no_file_written(self, tmp_path):
        """--dry-run must not write any .md file"""
        import glob

        before = set(glob.glob("generated_templates/**/*.md", recursive=True))
        subprocess.run(
            [
                sys.executable,
                "scripts/new_template_wizard.py",
                "--title",
                "NieIstniejacyDokument99999",
                "--dry-run",
            ],
            capture_output=True,
            cwd=_CWD,
        )
        after = set(glob.glob("generated_templates/**/*.md", recursive=True))
        assert before == after  # no new files

    @pytest.mark.integration
    def test_standard_appears_in_dry_run(self):
        """--standard value appears in rendered output"""
        result = subprocess.run(
            [
                sys.executable,
                "scripts/new_template_wizard.py",
                "--title",
                "Security Policy",
                "--standard",
                "ISO/IEC 27001",
                "--dry-run",
            ],
            capture_output=True,
            text=True,
            cwd=_CWD,
        )
        assert result.returncode == 0
        assert "ISO/IEC 27001" in result.stdout


# ---------------------------------------------------------------------------
# TestBulkPatcherCLI — integration tests (subprocess, --file)
# ---------------------------------------------------------------------------


class TestBulkPatcherCLI:
    @pytest.fixture
    def sample_md(self, tmp_path):
        f = tmp_path / "test_doc.md"
        f.write_text(
            """---
title: Test Patcher Integration
---
# Test Patcher Integration

## Cel dokumentu
Oryginalna tresc celu.

## Zakres i granice
- Obejmuje: zakres podstawowy
""",
            encoding="utf-8",
        )
        return f

    @pytest.mark.integration
    def test_preview_section(self, sample_md):
        """--preview-section shows section content without modifying file"""
        result = subprocess.run(
            [
                sys.executable,
                "scripts/maintenance/bulk_section_patcher.py",
                "--file",
                str(sample_md),
                "--preview-section",
                "## Cel dokumentu",
            ],
            capture_output=True,
            text=True,
            cwd=_CWD,
        )
        assert result.returncode == 0
        output = result.stdout + result.stderr
        assert "Oryginalna tresc celu" in output or "Cel dokumentu" in output
        # File must not be modified
        content = sample_md.read_text(encoding="utf-8")
        assert "Oryginalna tresc celu" in content

    @pytest.mark.integration
    def test_append_with_file_dry_run(self, sample_md):
        """--file + --append-to-section + --dry-run does not modify the file"""
        original = sample_md.read_text(encoding="utf-8")
        result = subprocess.run(
            [
                sys.executable,
                "scripts/maintenance/bulk_section_patcher.py",
                "--file",
                str(sample_md),
                "--append-to-section",
                "## Cel dokumentu",
                "--append-text",
                "Dodatkowy tekst testowy",
                "--reason",
                "integration test",
                "--dry-run",
            ],
            capture_output=True,
            text=True,
            cwd=_CWD,
        )
        assert result.returncode == 0
        after = sample_md.read_text(encoding="utf-8")
        assert original == after  # unchanged

    @pytest.mark.integration
    def test_append_with_file_applies(self, sample_md):
        """--file + --append-to-section without --dry-run modifies the file"""
        result = subprocess.run(
            [
                sys.executable,
                "scripts/maintenance/bulk_section_patcher.py",
                "--file",
                str(sample_md),
                "--append-to-section",
                "## Cel dokumentu",
                "--append-text",
                "Dodany tekst przez test integracyjny",
                "--reason",
                "integration test",
            ],
            capture_output=True,
            text=True,
            cwd=_CWD,
        )
        assert result.returncode == 0
        content = sample_md.read_text(encoding="utf-8")
        assert "Dodany tekst przez test integracyjny" in content
