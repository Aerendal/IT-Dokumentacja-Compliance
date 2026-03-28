import pytest
from pathlib import Path

pytestmark = pytest.mark.unit

from itdoc.fixes.markdown_model import parse, MarkdownDoc
from itdoc.fixes.rules import analyze, RULES, REQUIRED_SECTIONS


def _make_doc(tmp_path: Path, name: str, content: str):
    p = tmp_path / name
    p.write_text(content, encoding="utf-8")
    return parse(p)


VALID_CONTENT = """\
---
title: Valid Doc
---

## Cel dokumentu
Good content.

## Zakres i granice
Scope.

## Wejścia i wyjścia
IO.
"""


def test_analyze_valid_doc_no_findings(tmp_path):
    doc = _make_doc(tmp_path, "valid.md", VALID_CONTENT)
    findings = analyze(doc)
    assert findings == []


def test_analyze_missing_one_section(tmp_path):
    content = """\
---
title: Missing Section
---

## Cel dokumentu
Content.

## Zakres i granice
Scope.
"""
    doc = _make_doc(tmp_path, "missing.md", content)
    findings = analyze(doc)
    rule_ids = [f.rule.rule_id for f in findings]
    assert "DOC.SECTION.MISSING" in rule_ids
    details = [f.detail.get("section") for f in findings if f.rule.rule_id == "DOC.SECTION.MISSING"]
    assert "## Wejścia i wyjścia" in details


def test_analyze_missing_all_three_sections(tmp_path):
    content = "---\ntitle: No Sections\n---\n\nJust some text.\n"
    doc = _make_doc(tmp_path, "nosec.md", content)
    findings = analyze(doc)
    missing = [f for f in findings if f.rule.rule_id == "DOC.SECTION.MISSING"]
    assert len(missing) == 3


def test_analyze_no_frontmatter(tmp_path):
    content = "## Cel dokumentu\nContent.\n\n## Zakres i granice\nX.\n\n## Wejścia i wyjścia\nY.\n"
    doc = _make_doc(tmp_path, "nofm.md", content)
    findings = analyze(doc)
    rule_ids = [f.rule.rule_id for f in findings]
    assert "DOC.FRONTMATTER.MISSING" in rule_ids
    fm_findings = [f for f in findings if f.rule.rule_id == "DOC.FRONTMATTER.MISSING"]
    assert fm_findings[0].rule.safe_autofix is False


def test_analyze_frontmatter_no_title(tmp_path):
    content = "---\nauthor: someone\n---\n\n## Cel dokumentu\nX.\n\n## Zakres i granice\nY.\n\n## Wejścia i wyjścia\nZ.\n"
    doc = _make_doc(tmp_path, "notitle.md", content)
    findings = analyze(doc)
    rule_ids = [f.rule.rule_id for f in findings]
    assert "DOC.FRONTMATTER.NO_TITLE" in rule_ids


def test_analyze_emoji_forbidden(tmp_path):
    content = "---\ntitle: Emoji Doc\n---\n\n## Cel dokumentu\nHello 🎉\n\n## Zakres i granice\nX.\n\n## Wejścia i wyjścia\nY.\n"
    doc = _make_doc(tmp_path, "emoji.md", content)
    findings = analyze(doc)
    rule_ids = [f.rule.rule_id for f in findings]
    assert "DOC.EMOJI.FORBIDDEN" in rule_ids
    emoji_findings = [f for f in findings if f.rule.rule_id == "DOC.EMOJI.FORBIDDEN"]
    assert emoji_findings[0].rule.safe_autofix is True


def test_rules_dict_contains_all_four_rule_ids():
    expected = {"DOC.SECTION.MISSING", "DOC.EMOJI.FORBIDDEN", "DOC.FRONTMATTER.MISSING", "DOC.FRONTMATTER.NO_TITLE"}
    assert expected.issubset(set(RULES.keys()))
