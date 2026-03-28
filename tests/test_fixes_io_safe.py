import pytest
import hashlib
from pathlib import Path

pytestmark = pytest.mark.unit

from itdoc.fixes.io_safe import safe_write, WriteResult


def _sha256(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def _make_file(tmp_path: Path, name: str, content: str) -> Path:
    p = tmp_path / name
    p.write_text(content, encoding="utf-8")
    return p


def test_safe_write_changed_true_when_content_differs(tmp_path):
    p = _make_file(tmp_path, "test.md", "original content\n")
    backup_dir = tmp_path / "backups"
    result = safe_write(p, "new content\n", backup_dir)
    assert result.changed is True


def test_safe_write_changed_false_when_content_same(tmp_path):
    p = _make_file(tmp_path, "test.md", "same content\n")
    backup_dir = tmp_path / "backups"
    result = safe_write(p, "same content\n", backup_dir)
    assert result.changed is False


def test_safe_write_backup_created(tmp_path):
    p = _make_file(tmp_path, "test.md", "original\n")
    backup_dir = tmp_path / "backups"
    result = safe_write(p, "modified\n", backup_dir)
    assert result.backup_path.exists()


def test_safe_write_hash_before_not_equals_after_when_changed(tmp_path):
    p = _make_file(tmp_path, "test.md", "before\n")
    backup_dir = tmp_path / "backups"
    result = safe_write(p, "after\n", backup_dir)
    assert result.hash_before != result.hash_after


def test_safe_write_hash_before_equals_after_when_unchanged(tmp_path):
    content = "unchanged\n"
    p = _make_file(tmp_path, "test.md", content)
    backup_dir = tmp_path / "backups"
    result = safe_write(p, content, backup_dir)
    assert result.hash_before == result.hash_after


def test_safe_write_file_content_replaced(tmp_path):
    p = _make_file(tmp_path, "test.md", "old content\n")
    backup_dir = tmp_path / "backups"
    safe_write(p, "new content\n", backup_dir)
    assert p.read_text(encoding="utf-8") == "new content\n"


def test_safe_write_diff_lines_non_empty_when_changed(tmp_path):
    p = _make_file(tmp_path, "test.md", "line 1\nline 2\n")
    backup_dir = tmp_path / "backups"
    result = safe_write(p, "line 1\nline 2 modified\n", backup_dir)
    assert len(result.diff_lines) > 0


def test_safe_write_diff_lines_empty_when_unchanged(tmp_path):
    content = "same\n"
    p = _make_file(tmp_path, "test.md", content)
    backup_dir = tmp_path / "backups"
    result = safe_write(p, content, backup_dir)
    assert result.diff_lines == []
