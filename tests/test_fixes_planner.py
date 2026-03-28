import pytest
import json
from pathlib import Path

pytestmark = pytest.mark.unit

from itdoc.fixes.planner import build_plan, save_plan, load_plan, FixPlan, Change

VALID_MD = """\
---
title: Valid Doc
---

## Cel dokumentu
Content.

## Zakres i granice
Scope.

## Wejścia i wyjścia
IO.
"""

BROKEN_MD = "# No frontmatter\n\nMissing required sections.\n"


def _setup_dir(tmp_path: Path) -> Path:
    d = tmp_path / "docs"
    d.mkdir()
    (d / "valid.md").write_text(VALID_MD, encoding="utf-8")
    (d / "broken.md").write_text(BROKEN_MD, encoding="utf-8")
    return d


def test_build_plan_counts(tmp_path):
    d = _setup_dir(tmp_path)
    plan = build_plan(d, mode="analyze")
    assert plan.total_files == 2
    assert isinstance(plan.changes, list)
    # broken.md has frontmatter missing + 3 sections missing = 4 changes
    broken_changes = [c for c in plan.changes if "broken.md" in c.file]
    assert len(broken_changes) >= 1


def test_build_plan_valid_file_no_changes(tmp_path):
    d = _setup_dir(tmp_path)
    plan = build_plan(d, mode="analyze")
    valid_changes = [c for c in plan.changes if "valid.md" in c.file]
    assert valid_changes == []


def test_save_plan_writes_valid_json(tmp_path):
    d = _setup_dir(tmp_path)
    plan = build_plan(d, mode="analyze")
    out = tmp_path / "plan.json"
    save_plan(plan, out)
    assert out.exists()
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["schema_version"] == "1.0"
    assert "changes" in data
    assert isinstance(data["changes"], list)


def test_load_plan_round_trips(tmp_path):
    d = _setup_dir(tmp_path)
    plan = build_plan(d, mode="dry-run")
    out = tmp_path / "plan_rt.json"
    save_plan(plan, out)
    loaded = load_plan(out)
    assert loaded.schema_version == plan.schema_version
    assert loaded.run_id == plan.run_id
    assert loaded.total_files == plan.total_files
    assert len(loaded.changes) == len(plan.changes)


def test_safe_changes_only_safe(tmp_path):
    d = _setup_dir(tmp_path)
    plan = build_plan(d, mode="analyze")
    safe = plan.safe_changes()
    assert all(c.safe_autofix is True for c in safe)


def test_unsafe_changes_only_unsafe(tmp_path):
    d = _setup_dir(tmp_path)
    plan = build_plan(d, mode="analyze")
    unsafe = plan.unsafe_changes()
    assert all(c.safe_autofix is False for c in unsafe)
    # broken.md has DOC.FRONTMATTER.MISSING which is safe_autofix=False
    assert len(unsafe) >= 1
