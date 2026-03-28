import pytest
from pathlib import Path

pytestmark = pytest.mark.unit

from itdoc.fixes.markdown_model import parse, section_headings

VALID_DOC = """\
---
title: Test Doc
version: 1
---

# Main Title

## Cel dokumentu
Content here.

## Zakres i granice
Scope content.

## Wejścia i wyjścia
IO content.
"""

NO_FRONTMATTER_DOC = """\
# Just a title

## Cel dokumentu
Some content.
"""

FRONTMATTER_NO_TITLE_DOC = """\
---
version: 1
author: test
---

## Cel dokumentu
Content.
"""


def _write(tmp_path: Path, name: str, content: str) -> Path:
    p = tmp_path / name
    p.write_text(content, encoding="utf-8")
    return p


def test_parse_valid_doc(tmp_path):
    p = _write(tmp_path, "valid.md", VALID_DOC)
    doc = parse(p)
    assert doc.has_frontmatter is True
    assert doc.has_title_field is True
    assert doc.frontmatter_end_line >= 0
    assert len(doc.sections) >= 3


def test_parse_no_frontmatter(tmp_path):
    p = _write(tmp_path, "nofm.md", NO_FRONTMATTER_DOC)
    doc = parse(p)
    assert doc.has_frontmatter is False
    assert doc.has_title_field is False
    assert doc.frontmatter_end_line == -1


def test_parse_frontmatter_no_title(tmp_path):
    p = _write(tmp_path, "notitle.md", FRONTMATTER_NO_TITLE_DOC)
    doc = parse(p)
    assert doc.has_frontmatter is True
    assert doc.has_title_field is False


def test_section_headings_returns_correct_set(tmp_path):
    p = _write(tmp_path, "valid.md", VALID_DOC)
    doc = parse(p)
    headings = section_headings(doc)
    assert "## Cel dokumentu" in headings
    assert "## Zakres i granice" in headings
    assert "## Wejścia i wyjścia" in headings


def test_parse_reads_from_real_file(tmp_path):
    content = "---\ntitle: Real File\n---\n\n## Cel dokumentu\nHello.\n"
    p = _write(tmp_path, "real.md", content)
    doc = parse(p)
    assert doc.path == p
    assert "Real File" in doc.raw
    assert doc.has_frontmatter is True
