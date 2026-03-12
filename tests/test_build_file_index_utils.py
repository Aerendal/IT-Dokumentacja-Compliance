"""
tests/test_build_file_index_utils.py — unit tests for pure utility functions
in scripts/build_file_index.py.

Covers: normalize_title_norm, infer_source, extract_title
"""
import sys
import unittest.mock
import pytest

pytestmark = pytest.mark.unit

# build_file_index.py does `from ulid import ulid` (sibling module on scripts/ path).
# Mock it at module level so the import succeeds in the test context.
if 'ulid' not in sys.modules:
    _mock_ulid_mod = unittest.mock.MagicMock()
    _mock_ulid_mod.ulid = lambda: "01FAKEULIDFORTEST00000000"
    sys.modules['ulid'] = _mock_ulid_mod


class TestNormalizeTitleNorm:
    def test_empty_string_returns_empty(self):
        from scripts.build_file_index import normalize_title_norm
        assert normalize_title_norm("") == ""

    def test_none_like_empty_handled(self):
        from scripts.build_file_index import normalize_title_norm
        # None is coerced via (s or "")
        assert normalize_title_norm(None) == ""  # type: ignore[arg-type]

    def test_strips_whitespace(self):
        from scripts.build_file_index import normalize_title_norm
        assert normalize_title_norm("  Hello World  ") == "hello world"

    def test_lowercases(self):
        from scripts.build_file_index import normalize_title_norm
        assert normalize_title_norm("UPPERCASE") == "uppercase"

    def test_removes_numeric_prefix_dot(self):
        from scripts.build_file_index import normalize_title_norm
        assert normalize_title_norm("1. Tytuł dokumentu") == "tytuł dokumentu"

    def test_removes_numeric_prefix_paren(self):
        from scripts.build_file_index import normalize_title_norm
        assert normalize_title_norm("2) Second item") == "second item"

    def test_removes_multilevel_numeric_prefix(self):
        from scripts.build_file_index import normalize_title_norm
        # Pattern matches "1. " "2. " etc but not "1.2." without space
        assert normalize_title_norm("1. 2. Section name") == "section name"

    def test_removes_emoji(self):
        from scripts.build_file_index import normalize_title_norm
        result = normalize_title_norm("🔒 Security Policy")
        assert "🔒" not in result
        assert "security policy" in result

    def test_collapses_whitespace(self):
        from scripts.build_file_index import normalize_title_norm
        assert normalize_title_norm("hello   world") == "hello world"

    def test_plain_title_unchanged(self):
        from scripts.build_file_index import normalize_title_norm
        assert normalize_title_norm("incident report") == "incident report"


class TestInferSource:
    def test_core_prefix(self):
        from scripts.build_file_index import infer_source
        assert infer_source("core/some/doc.md") == "core"

    def test_imported_template_prefix(self):
        from scripts.build_file_index import infer_source
        path = "imported/files(13)/templates/doc.md"
        assert infer_source(path) == "imported_template"

    def test_imported_other_prefix(self):
        from scripts.build_file_index import infer_source
        assert infer_source("imported/other/doc.md") == "imported_other"

    def test_unknown_prefix(self):
        from scripts.build_file_index import infer_source
        assert infer_source("something/else.md") == "unknown"

    def test_backslash_normalized(self):
        from scripts.build_file_index import infer_source
        assert infer_source("core\\subdir\\doc.md") == "core"

    def test_empty_path_unknown(self):
        from scripts.build_file_index import infer_source
        assert infer_source("") == "unknown"


class TestExtractTitle:
    def test_yaml_frontmatter_title(self):
        from scripts.build_file_index import extract_title
        text = '---\ntitle: "My Document"\nauthor: Alice\n---\n# Other heading\n'
        assert extract_title(text) == "My Document"

    def test_yaml_frontmatter_single_quotes(self):
        from scripts.build_file_index import extract_title
        text = "---\ntitle: 'Another Doc'\n---\n"
        assert extract_title(text) == "Another Doc"

    def test_yaml_frontmatter_no_quotes(self):
        from scripts.build_file_index import extract_title
        text = "---\ntitle: Plain Title\n---\n"
        assert extract_title(text) == "Plain Title"

    def test_h1_fallback(self):
        from scripts.build_file_index import extract_title
        text = "# My H1 Title\n\nSome content here."
        assert extract_title(text) == "My H1 Title"

    def test_returns_none_when_no_title(self):
        from scripts.build_file_index import extract_title
        text = "Just some plain text without heading or frontmatter."
        assert extract_title(text) is None

    def test_frontmatter_takes_priority_over_h1(self):
        from scripts.build_file_index import extract_title
        text = "---\ntitle: FM Title\n---\n# H1 Title\n"
        assert extract_title(text) == "FM Title"

    def test_empty_text_returns_none(self):
        from scripts.build_file_index import extract_title
        assert extract_title("") is None

    def test_frontmatter_unclosed_falls_back_to_h1(self):
        from scripts.build_file_index import extract_title
        text = "---\ntitle: FM Title\n# H1 Title\n"
        # No closing ---, so frontmatter is not recognized
        assert extract_title(text) == "H1 Title"
