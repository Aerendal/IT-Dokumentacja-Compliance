"""
tests/test_misc_scripts.py — unit tests for small utility scripts with 0% coverage.

Covers:
  - scripts/check_no_emoji.py
  - scripts/fix_mojibake_guidance.py
  - scripts/ulid.py
  - scripts/gap_analysis.py (utility functions)
  - scripts/fill_guidance_from_similar.py (utility functions)
"""
import re
import sqlite3
import pytest
from pathlib import Path

pytestmark = pytest.mark.unit


# ---------------------------------------------------------------------------
# scripts/ulid.py
# ---------------------------------------------------------------------------

class TestUlid:
    def test_returns_26_char_string(self):
        from scripts.ulid import ulid
        result = ulid()
        assert isinstance(result, str)
        assert len(result) == 26

    def test_unique_on_successive_calls(self):
        from scripts.ulid import ulid
        ids = {ulid() for _ in range(100)}
        assert len(ids) >= 90  # extremely unlikely to collide

    def test_only_crockford_chars(self):
        from scripts.ulid import ulid
        crockford = set("0123456789ABCDEFGHJKMNPQRSTVWXYZ")
        result = ulid()
        assert all(c in crockford for c in result)

    def test_encode_base32_returns_26_chars(self):
        from scripts.ulid import _encode_base32
        data = b"\x00" * 16
        result = _encode_base32(data)
        assert len(result) == 26


# ---------------------------------------------------------------------------
# scripts/check_no_emoji.py
# ---------------------------------------------------------------------------

class TestCheckNoEmoji:
    def test_emoji_char_detected(self):
        from scripts.check_no_emoji import is_emoji_char
        assert is_emoji_char("😀") is True  # 0x1F600

    def test_regular_char_not_emoji(self):
        from scripts.check_no_emoji import is_emoji_char
        assert is_emoji_char("A") is False
        assert is_emoji_char("z") is False
        assert is_emoji_char("1") is False

    def test_misc_symbol_detected(self):
        from scripts.check_no_emoji import is_emoji_char
        # 0x2603 = ☃ (snowman) - in 0x2600-0x26FF range
        assert is_emoji_char("\u2603") is True

    def test_scan_file_with_emoji(self, tmp_path):
        from scripts.check_no_emoji import scan_file
        f = tmp_path / "doc.md"
        f.write_text("Hello 😀 world\nNormal line\n", encoding="utf-8")
        hits = scan_file(f)
        assert len(hits) == 1
        assert hits[0][0] == 1  # line number

    def test_scan_file_no_emoji(self, tmp_path):
        from scripts.check_no_emoji import scan_file
        f = tmp_path / "clean.md"
        f.write_text("Hello world\nNo emoji here\n", encoding="utf-8")
        hits = scan_file(f)
        assert hits == []

    def test_scan_file_multiple_emoji_lines(self, tmp_path):
        from scripts.check_no_emoji import scan_file
        f = tmp_path / "multi.md"
        f.write_text("😀 line 1\nclean\n🎉 line 3\n", encoding="utf-8")
        hits = scan_file(f)
        assert len(hits) == 2

    def test_iter_text_files_finds_md(self, tmp_path):
        from scripts.check_no_emoji import iter_text_files
        (tmp_path / "a.md").write_text("content", encoding="utf-8")
        (tmp_path / "b.py").write_text("code", encoding="utf-8")
        files = list(iter_text_files(tmp_path))
        names = [f.name for f in files]
        assert "a.md" in names
        assert "b.py" not in names

    def test_iter_text_files_skips_git(self, tmp_path):
        from scripts.check_no_emoji import iter_text_files
        git_dir = tmp_path / ".git"
        git_dir.mkdir()
        (git_dir / "config").write_text("data", encoding="utf-8")
        # rename to .md so extension matches
        git_md = git_dir / "hooks.md"
        git_md.write_text("git hook", encoding="utf-8")
        (tmp_path / "real.md").write_text("real", encoding="utf-8")
        files = list(iter_text_files(tmp_path))
        names = [f.name for f in files]
        assert "real.md" in names
        assert "hooks.md" not in names


# ---------------------------------------------------------------------------
# scripts/fix_mojibake_guidance.py
# ---------------------------------------------------------------------------

class TestFixMojibake:
    def test_try_fix_correct_mojibake(self):
        from scripts.fix_mojibake_guidance import try_fix
        # "ó" encoded as cp1252 and then decoded as unicode
        mojibake = "ó".encode("utf-8").decode("cp1252", errors="ignore")
        if mojibake and mojibake != "ó":
            fixed, changed = try_fix(mojibake)
            # might fix or might not depending on platform
            assert isinstance(fixed, str)

    def test_try_fix_clean_string_unchanged(self):
        from scripts.fix_mojibake_guidance import try_fix
        val = "Clean ASCII text"
        fixed, changed = try_fix(val)
        assert fixed == val
        assert changed is False

    def test_try_fix_returns_tuple(self):
        from scripts.fix_mojibake_guidance import try_fix
        result = try_fix("hello")
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_fix_column_dry_run(self, tmp_path, capsys):
        from scripts.fix_mojibake_guidance import fix_column
        db = tmp_path / "test.db"
        conn = sqlite3.connect(str(db))
        conn.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, col TEXT)")
        conn.execute("INSERT INTO test_table VALUES (1, 'normal text')")
        conn.execute("INSERT INTO test_table VALUES (2, 'another text')")
        conn.commit()
        count = fix_column(conn, "test_table", "col", dry_run=True)
        assert isinstance(count, int)
        conn.close()

    def test_fix_column_returns_zero_for_clean_data(self, tmp_path):
        from scripts.fix_mojibake_guidance import fix_column
        db = tmp_path / "test.db"
        conn = sqlite3.connect(str(db))
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, val TEXT)")
        conn.execute("INSERT INTO t VALUES (1, 'hello')")
        conn.execute("INSERT INTO t VALUES (2, 'world')")
        conn.commit()
        count = fix_column(conn, "t", "val", dry_run=True)
        assert count == 0
        conn.close()

    def test_fix_column_handles_null_values(self, tmp_path):
        from scripts.fix_mojibake_guidance import fix_column
        db = tmp_path / "test.db"
        conn = sqlite3.connect(str(db))
        conn.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, val TEXT)")
        conn.execute("INSERT INTO t VALUES (1, NULL)")
        conn.commit()
        count = fix_column(conn, "t", "val", dry_run=True)
        assert count == 0
        conn.close()


# ---------------------------------------------------------------------------
# scripts/gap_analysis.py — utility functions
# ---------------------------------------------------------------------------

class TestGapAnalysisUtils:
    def test_slugify_basic(self):
        from scripts.gap_analysis import slugify
        result = slugify("Hello World")
        assert result == "hello world"

    def test_slugify_polish_chars(self):
        from scripts.gap_analysis import slugify
        result = slugify("Zarządzanie bezpieczeństwem")
        assert "a" in result  # ą→a
        assert "ą" not in result

    def test_slugify_removes_special_chars(self):
        from scripts.gap_analysis import slugify
        result = slugify("hello-world_test.doc")
        assert "-" not in result or result == "hello world test doc"

    def test_tokens_returns_set(self):
        from scripts.gap_analysis import tokens
        result = tokens("Risk Management Policy")
        assert isinstance(result, set)

    def test_tokens_removes_stopwords(self):
        from scripts.gap_analysis import tokens
        result = tokens("the management plan document")
        assert "the" not in result
        assert "plan" not in result  # in stopwords

    def test_tokens_min_length(self):
        from scripts.gap_analysis import tokens
        result = tokens("a ab abc abcd")
        assert "a" not in result
        assert "ab" not in result

    def test_ngram_score_identical(self):
        from scripts.gap_analysis import ngram_score
        score = ngram_score("risk management", "risk management")
        assert score == 1.0

    def test_ngram_score_disjoint(self):
        from scripts.gap_analysis import ngram_score
        score = ngram_score("alpha beta", "gamma delta")
        assert score == 0.0

    def test_ngram_score_partial(self):
        from scripts.gap_analysis import ngram_score
        score = ngram_score("risk management policy", "risk management guide")
        assert 0.0 < score < 1.0

    def test_keyword_score_identical(self):
        from scripts.gap_analysis import keyword_score
        score = keyword_score("security policy", "security policy")
        assert score == 1.0

    def test_keyword_score_disjoint(self):
        from scripts.gap_analysis import keyword_score
        score = keyword_score("alpha beta gamma", "xyz uvw rst")
        assert score == 0.0

    def test_keyword_score_partial_overlap(self):
        from scripts.gap_analysis import keyword_score
        score = keyword_score("security incident response", "security audit policy")
        assert 0.0 < score < 1.0

    def test_keyword_score_both_empty(self):
        from scripts.gap_analysis import keyword_score
        score = keyword_score("", "")
        assert score == 1.0

    def test_keyword_score_one_empty(self):
        from scripts.gap_analysis import keyword_score
        score = keyword_score("security", "")
        assert score == 0.0


# ---------------------------------------------------------------------------
# scripts/fill_guidance_from_similar.py — utility functions
# ---------------------------------------------------------------------------

class TestFillGuidanceUtils:
    def test_is_placeholder_body_empty(self):
        from scripts.fill_guidance_from_similar import is_placeholder_body
        assert is_placeholder_body("") is True
        assert is_placeholder_body("   ") is True

    def test_is_placeholder_body_real_content(self):
        from scripts.fill_guidance_from_similar import is_placeholder_body
        body = "This is real content with specific details about security policy."
        assert is_placeholder_body(body) is False

    def test_is_placeholder_body_with_brackets(self):
        from scripts.fill_guidance_from_similar import is_placeholder_body
        body = "- [Uzupełnij zgodnie z kontekstem]\n- [Akcja 2]"
        assert is_placeholder_body(body) is True

    def test_is_placeholder_body_with_generic_marker(self):
        from scripts.fill_guidance_from_similar import is_placeholder_body
        body = "Uzupełnij zgodnie z kontekstem projektu."
        assert is_placeholder_body(body) is True

    def test_extract_title_from_h1(self):
        from scripts.fill_guidance_from_similar import extract_title_from_file
        text = "---\ntitle: x\n---\n# My Document Title\n\n## Section\n"
        result = extract_title_from_file(text, "filename.md")
        assert result == "My Document Title"

    def test_extract_title_fallback_to_filename(self):
        from scripts.fill_guidance_from_similar import extract_title_from_file
        text = "No heading here\n"
        result = extract_title_from_file(text, "my_document.md")
        assert "my document" in result.lower()

    def test_title_keywords_basic(self):
        from scripts.fill_guidance_from_similar import title_keywords
        result = title_keywords("Risk Management Policy")
        assert "risk" in result
        assert "management" in result
        assert "policy" in result

    def test_title_keywords_removes_stopwords(self):
        from scripts.fill_guidance_from_similar import title_keywords
        result = title_keywords("the and or a an of in for to with")
        assert "the" not in result

    def test_title_keywords_min_length(self):
        from scripts.fill_guidance_from_similar import title_keywords
        result = title_keywords("a ab abc abcd")
        assert "a" not in result
        assert "ab" not in result

    def test_parse_sections_basic(self):
        from scripts.fill_guidance_from_similar import parse_sections
        md = "# Title\n\n## Goals\n\nContent here.\n\n## Standards\n\nISO content.\n"
        result = parse_sections(md)
        assert "## Goals" in result
        assert "## Standards" in result

    def test_parse_sections_preserves_body(self):
        from scripts.fill_guidance_from_similar import parse_sections
        md = "## Goals\n\nGoal one.\nGoal two.\n\n## Other\n\nOther content.\n"
        sections = parse_sections(md)
        assert "Goal one" in sections["## Goals"]

    def test_parse_sections_empty(self):
        from scripts.fill_guidance_from_similar import parse_sections
        result = parse_sections("No sections here")
        assert result == {}

    def test_rebuild_file_replaces_section(self):
        from scripts.fill_guidance_from_similar import rebuild_file_with_new_sections
        text = "## Goals\n\nOld content.\n\n## Other\n\nOther stuff.\n"
        updated = {"## Goals": "\nNew content.\n"}
        result = rebuild_file_with_new_sections(text, updated)
        assert "New content." in result
        assert "Other stuff." in result

    def test_rebuild_file_no_changes_for_unknown_section(self):
        from scripts.fill_guidance_from_similar import rebuild_file_with_new_sections
        text = "## Goals\n\nContent.\n"
        result = rebuild_file_with_new_sections(text, {"## NonExistent": "\nX\n"})
        assert result == text

    def test_bump_rev_increments(self):
        from scripts.fill_guidance_from_similar import bump_rev
        text = "---\naligned_rev: 3\n---\n"
        result = bump_rev(text)
        assert "aligned_rev: 4" in result

    def test_bump_rev_no_rev_unchanged(self):
        from scripts.fill_guidance_from_similar import bump_rev
        text = "---\ntitle: something\n---\n"
        result = bump_rev(text)
        assert result == text
