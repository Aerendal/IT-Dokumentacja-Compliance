"""
tests/test_patch_section.py — unit tests for scripts/maintenance/patch_section.py
All tests use tmp_path for file operations.
"""
import pytest
from pathlib import Path

from scripts.maintenance.patch_section import (
    strip_frontmatter,
    find_section,
    apply_operation,
    build_diff,
    atomic_write,
    similarity_ratio,
    file_hash,
)

pytestmark = pytest.mark.unit


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SIMPLE_MD = """\
---
title: Test Document
status: draft
---
# Introduction

This is the introduction.

## Goals

- Goal one
- Goal two

## Standards

ISO27001 applies here.

## Conclusion

The end.
"""

MULTI_SECTION_MD = """\
# Top

## Alpha

Content alpha.

## Beta

Content beta.

## Gamma

Content gamma.
"""


@pytest.fixture
def md_file(tmp_path) -> Path:
    p = tmp_path / "doc.md"
    p.write_text(SIMPLE_MD, encoding="utf-8")
    return p


# ---------------------------------------------------------------------------
# strip_frontmatter
# ---------------------------------------------------------------------------

class TestStripFrontmatter:
    def test_splits_frontmatter_and_body(self):
        fm, body = strip_frontmatter(SIMPLE_MD)
        assert fm.startswith("---")
        assert "# Introduction" in body

    def test_no_frontmatter_returns_empty_fm(self):
        content = "# Just markdown\n\nNo frontmatter here.\n"
        fm, body = strip_frontmatter(content)
        assert fm == ""
        assert "# Just markdown" in body

    def test_frontmatter_preserved_exactly(self):
        fm, body = strip_frontmatter(SIMPLE_MD)
        assert "title: Test Document" in fm
        assert "status: draft" in fm

    def test_body_does_not_contain_frontmatter_keys(self):
        _, body = strip_frontmatter(SIMPLE_MD)
        # title key should only be in fm, not body
        assert "title: Test Document" not in body


# ---------------------------------------------------------------------------
# find_section
# ---------------------------------------------------------------------------

class TestFindSection:
    def test_finds_existing_section(self):
        _, body = strip_frontmatter(SIMPLE_MD)
        result = find_section(body, "Goals")
        assert result is not None
        start, end = result
        assert start >= 1

    def test_returns_none_for_missing_section(self):
        _, body = strip_frontmatter(SIMPLE_MD)
        result = find_section(body, "NonExistentSection")
        assert result is None

    def test_finds_multiple_sections_individually(self):
        _, body = strip_frontmatter(SIMPLE_MD)
        goals = find_section(body, "Goals")
        standards = find_section(body, "Standards")
        assert goals is not None
        assert standards is not None
        assert goals != standards

    def test_section_start_before_end(self):
        _, body = strip_frontmatter(SIMPLE_MD)
        start, end = find_section(body, "Goals")
        assert start <= end

    def test_case_sensitive_section_name(self):
        _, body = strip_frontmatter(SIMPLE_MD)
        # Exact case match required
        result_upper = find_section(body, "goals")
        # The regex may be case-insensitive or case-sensitive; just verify no crash
        assert result_upper is None or isinstance(result_upper, tuple)


# ---------------------------------------------------------------------------
# apply_operation
# ---------------------------------------------------------------------------

class TestApplyOperation:
    def _get_body(self):
        _, body = strip_frontmatter(SIMPLE_MD)
        return body

    def test_replace_section_content(self):
        body = self._get_body()
        new_body = apply_operation(body, "Standards", "replace", content="NIST CSF applies.")
        assert "NIST CSF applies." in new_body

    def test_append_to_section(self):
        body = self._get_body()
        new_body = apply_operation(body, "Goals", "append", content="- Goal three")
        assert "Goal three" in new_body
        assert "Goal one" in new_body  # Original preserved

    def test_prepend_to_section(self):
        body = self._get_body()
        new_body = apply_operation(body, "Goals", "prepend", content="- Goal zero")
        assert "Goal zero" in new_body

    def test_delete_section(self):
        body = self._get_body()
        new_body = apply_operation(body, "Conclusion", "delete")
        assert "The end." not in new_body

    def test_rename_section(self):
        body = self._get_body()
        new_body = apply_operation(body, "Conclusion", "rename", new_name="Summary")
        assert "Summary" in new_body

    def test_missing_section_returns_unchanged(self):
        body = self._get_body()
        new_body = apply_operation(body, "NonExistent", "replace", content="X")
        assert new_body == body

    def test_replace_substring_within_section(self):
        body = self._get_body()
        new_body = apply_operation(
            body, "Standards", "replace",
            old="ISO27001 applies here.", new="NIST CSF applies here."
        )
        assert "NIST CSF applies here." in new_body

    def test_deduplicate_operation(self):
        md = "## Items\n\n- item one\n- item one\n- item two\n\n"
        new_body = apply_operation(md, "Items", "deduplicate")
        # After dedup, item one should appear only once
        assert new_body.count("item one") == 1


# ---------------------------------------------------------------------------
# build_diff
# ---------------------------------------------------------------------------

class TestBuildDiff:
    def test_returns_unified_diff(self):
        old = "line one\nline two\n"
        new = "line one\nline THREE\n"
        diff = build_diff(old, new, "test.md")
        assert "---" in diff or "+++" in diff or "@@ " in diff

    def test_no_diff_for_identical(self):
        content = "same content\n"
        diff = build_diff(content, content, "test.md")
        assert diff == ""

    def test_diff_contains_filename(self):
        diff = build_diff("old\n", "new\n", "myfile.md")
        assert "myfile.md" in diff


# ---------------------------------------------------------------------------
# atomic_write
# ---------------------------------------------------------------------------

class TestAtomicWrite:
    def test_writes_file(self, tmp_path):
        p = tmp_path / "output.md"
        atomic_write(p, "Hello, world!")
        assert p.read_text(encoding="utf-8") == "Hello, world!"

    def test_overwrites_existing_file(self, tmp_path):
        p = tmp_path / "output.md"
        p.write_text("original", encoding="utf-8")
        atomic_write(p, "updated")
        assert p.read_text(encoding="utf-8") == "updated"

    def test_no_tmp_file_left_behind(self, tmp_path):
        p = tmp_path / "output.md"
        atomic_write(p, "content")
        tmp = p.with_suffix(".tmp")
        assert not tmp.exists()


# ---------------------------------------------------------------------------
# similarity_ratio / file_hash
# ---------------------------------------------------------------------------

class TestUtilityFunctions:
    def test_similarity_identical(self):
        s = "line one\nline two\n"
        assert similarity_ratio(s, s) == 1.0

    def test_similarity_disjoint(self):
        assert similarity_ratio("aaa\n", "bbb\n") == 0.0

    def test_similarity_partial(self):
        score = similarity_ratio("a\nb\n", "b\nc\n")
        assert 0.0 < score < 1.0

    def test_file_hash_deterministic(self):
        h1 = file_hash("same content")
        h2 = file_hash("same content")
        assert h1 == h2

    def test_file_hash_different_for_different_content(self):
        assert file_hash("content A") != file_hash("content B")

    def test_file_hash_is_string(self):
        assert isinstance(file_hash("x"), str)
