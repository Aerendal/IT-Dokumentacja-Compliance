"""
Safe atomic file writer for autofix engine.
Guarantees: temp write → backup original → atomic rename → hash log.
Never overwrites a file without first creating a backup.
"""
from __future__ import annotations
import hashlib
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import difflib


@dataclass
class WriteResult:
    path: Path
    hash_before: str    # SHA-256 hex of original content
    hash_after: str     # SHA-256 hex of new content
    backup_path: Path   # where the original was backed up
    diff_lines: list[str]  # unified diff lines (may be empty if no change)
    changed: bool       # True if new_content != original


def _sha256(content: str) -> str:
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def safe_write(path: Path, new_content: str, backup_dir: Path) -> WriteResult:
    """
    Atomically write new_content to path, with backup.

    Steps:
    1. Read original + compute hash_before
    2. If content unchanged, return WriteResult(changed=False)
    3. Write new_content to a temp file (same directory)
    4. Copy original to backup_dir/
    5. Rename temp → path (atomic on same filesystem)
    6. Compute hash_after + unified diff
    """
    backup_dir.mkdir(parents=True, exist_ok=True)

    # Read original
    original = path.read_text(encoding='utf-8', errors='replace')
    hash_before = _sha256(original)
    hash_after = _sha256(new_content)

    # Build backup path: backup_dir / relative-to-cwd path with / replaced
    safe_name = str(path).replace('/', '__').replace('\\', '__')
    backup_path = backup_dir / safe_name

    changed = original != new_content

    # Compute diff regardless (useful for dry-run reporting)
    diff_lines = list(difflib.unified_diff(
        original.splitlines(keepends=True),
        new_content.splitlines(keepends=True),
        fromfile=f'a/{path}',
        tofile=f'b/{path}',
    ))

    if not changed:
        return WriteResult(
            path=path,
            hash_before=hash_before,
            hash_after=hash_after,
            backup_path=backup_path,
            diff_lines=[],
            changed=False,
        )

    # Write to temp file first
    tmp_fd, tmp_path_str = tempfile.mkstemp(dir=path.parent, suffix='.tmp')
    tmp_path = Path(tmp_path_str)
    try:
        with open(tmp_fd, 'w', encoding='utf-8') as f:
            f.write(new_content)

        # Backup original
        shutil.copy2(str(path), str(backup_path))

        # Atomic rename
        tmp_path.replace(path)
    except Exception:
        # Clean up temp if something went wrong
        if tmp_path.exists():
            tmp_path.unlink()
        raise

    return WriteResult(
        path=path,
        hash_before=hash_before,
        hash_after=hash_after,
        backup_path=backup_path,
        diff_lines=diff_lines,
        changed=True,
    )
