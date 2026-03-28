import pytest
from pathlib import Path

pytestmark = pytest.mark.unit

from itdoc.fixes.applier import apply_insert_section, apply_strip_emoji, apply_plan, ApplyResult
from itdoc.fixes.planner import build_plan


CONTENT_NO_SECTION = """\
---
title: Missing Sections
---

Some intro text.
"""

CONTENT_WITH_EMOJI = """\
---
title: Emoji File
---

## Cel dokumentu
Hello 🎉 World 🚀
"""


def test_apply_insert_section_appends_at_end():
    content = "---\ntitle: Test\n---\n\n## Existing Section\nContent.\n"
    result = apply_insert_section(content, "## Cel dokumentu", "<!-- TODO: Opisz cel dokumentu -->\n")
    assert "## Cel dokumentu" in result
    assert result.index("## Cel dokumentu") > result.index("## Existing Section")


def test_apply_insert_section_blank_line_before_heading():
    content = "Some text."
    result = apply_insert_section(content, "## New Section", "placeholder\n")
    # Should have \n\n before the new heading
    assert "\n\n## New Section" in result


def test_apply_insert_section_once_appends_correctly():
    content = "---\ntitle: X\n---\n\nBody.\n"
    result = apply_insert_section(content, "## Cel dokumentu", "<!-- TODO -->\n")
    assert result.count("## Cel dokumentu") == 1
    assert "<!-- TODO -->" in result


def test_apply_strip_emoji_removes_emoji():
    text = "Hello 🎉 World 🚀 end"
    result = apply_strip_emoji(text)
    assert "🎉" not in result
    assert "🚀" not in result
    assert "Hello" in result
    assert "World" in result
    assert "end" in result


def test_apply_strip_emoji_no_emoji_unchanged():
    text = "Plain text without any emoji."
    result = apply_strip_emoji(text)
    assert result == text


def test_apply_plan_section_missing_changes_file(tmp_path):
    md = tmp_path / "broken.md"
    md.write_text(CONTENT_NO_SECTION, encoding="utf-8")
    plan = build_plan(tmp_path, mode="apply")
    backup_dir = tmp_path / "backups"
    result = apply_plan(plan, only_safe=True, backup_dir=backup_dir)
    changed_basenames = [Path(f).name for f in result.changed_files]
    assert "broken.md" in changed_basenames


def test_apply_plan_backup_created(tmp_path):
    md = tmp_path / "broken.md"
    md.write_text(CONTENT_NO_SECTION, encoding="utf-8")
    plan = build_plan(tmp_path, mode="apply")
    backup_dir = tmp_path / "backups"
    result = apply_plan(plan, only_safe=True, backup_dir=backup_dir)
    assert backup_dir.exists()
    backups = list(backup_dir.iterdir())
    assert len(backups) >= 1
