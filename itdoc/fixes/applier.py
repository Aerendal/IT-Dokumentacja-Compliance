"""
Applies a FixPlan to files on disk.

For each safe change in the plan:
  - insert_section: appends missing required section with placeholder content
  - strip_emoji: removes emoji characters from the file
  - report_only: skipped (no write)

All writes go through io_safe.safe_write() for atomic backup + hash logging.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from itdoc.fixes.io_safe import WriteResult, safe_write
from itdoc.fixes.rules import SECTION_PLACEHOLDERS, _strip_emoji


@dataclass
class ApplyResult:
    """Result of applying a FixPlan."""
    changed_files: list[str] = field(default_factory=list)
    skipped_files: list[str] = field(default_factory=list)   # report_only or unsafe
    errors: list[tuple[str, str]] = field(default_factory=list)
    write_results: list[WriteResult] = field(default_factory=list)
    diff_lines_by_file: dict[str, list[str]] = field(default_factory=dict)


def apply_insert_section(content: str, section: str, placeholder: str) -> str:
    """
    Append a missing section to the end of a Markdown document.
    Ensures a blank line before the new section heading.
    Returns the modified content.
    """
    stripped = content.rstrip('\n')
    return stripped + f"\n\n{section}\n{placeholder}"


def apply_strip_emoji(content: str) -> str:
    """Remove all emoji characters from content."""
    return _strip_emoji(content)


def apply_plan(
    plan: "FixPlan",
    *,
    only_safe: bool = True,
    backup_dir: Optional[Path] = None,
) -> ApplyResult:
    """
    Apply a FixPlan to files on disk.

    Args:
        plan: the FixPlan to apply
        only_safe: if True, skip changes where safe_autofix=False
        backup_dir: directory for backups (default: reports/autofix_backups)
    """
    from itdoc.fixes.planner import FixPlan  # noqa: F401 (type reference)

    if backup_dir is None:
        backup_dir = Path("reports/autofix_backups")

    result = ApplyResult()

    by_file = plan.by_file()

    for file_path_str, changes in sorted(by_file.items()):
        file_path = Path(file_path_str)

        if not file_path.exists():
            result.errors.append((file_path_str, "File not found"))
            continue

        applicable = []
        for c in changes:
            if c.action == "report_only":
                continue
            if only_safe and not c.safe_autofix:
                continue
            applicable.append(c)

        if not applicable:
            result.skipped_files.append(file_path_str)
            continue

        try:
            content = file_path.read_text(encoding='utf-8', errors='replace')
            new_content = content

            for change in applicable:
                if change.action == "insert_section":
                    section = change.detail.get("section", "")
                    placeholder = change.detail.get("placeholder", SECTION_PLACEHOLDERS.get(section, "<!-- TODO -->\n"))
                    new_content = apply_insert_section(new_content, section, placeholder)

                elif change.action == "strip_emoji":
                    new_content = apply_strip_emoji(new_content)

            write_result = safe_write(file_path, new_content, backup_dir)
            result.write_results.append(write_result)

            if write_result.changed:
                result.changed_files.append(file_path_str)
                if write_result.diff_lines:
                    result.diff_lines_by_file[file_path_str] = write_result.diff_lines
            else:
                result.skipped_files.append(file_path_str)

        except Exception as e:
            result.errors.append((file_path_str, str(e)))

    return result
