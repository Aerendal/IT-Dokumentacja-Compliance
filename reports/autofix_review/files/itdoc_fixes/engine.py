"""
Orchestration engine for the autofix pipeline.

Modes:
  analyze  — scan files, build plan, save JSON, print summary (no write)
  dry-run  — same as analyze + compute diffs (no write)
  apply    — analyze + apply safe changes with backup
"""
from __future__ import annotations
from pathlib import Path
from typing import Optional

from itdoc.fixes.planner import FixPlan, build_plan, save_plan
from itdoc.fixes.report import print_plan_summary, write_diff_report, format_apply_summary


def run(
    root: Path,
    mode: str,
    output_plan: Path,
    *,
    write_diff: Optional[Path] = None,
    only_safe: bool = True,
    backup_dir: Optional[Path] = None,
    verbose: bool = False,
) -> FixPlan:
    """
    Run the autofix engine.

    Args:
        root: directory to scan for .md files
        mode: "analyze", "dry-run", or "apply"
        output_plan: path to write the JSON fix plan
        write_diff: optional path to write a unified diff report
        only_safe: if mode=apply, only apply safe_autofix=True changes
        backup_dir: backup directory for mode=apply
        verbose: print file-level detail in summary

    Returns:
        The generated FixPlan
    """
    if mode not in ("analyze", "dry-run", "apply"):
        raise ValueError(f"Invalid mode: {mode!r}. Must be analyze, dry-run, or apply.")

    # Step 1: Build plan (no file writes)
    plan = build_plan(root, mode)
    save_plan(plan, output_plan)
    print_plan_summary(plan, verbose=verbose)

    # Step 2: For dry-run, compute diffs without writing
    if mode == "dry-run":
        _print_dry_run_diffs(plan, write_diff)

    # Step 3: For apply, write changes
    elif mode == "apply":
        from itdoc.fixes.applier import apply_plan
        apply_result = apply_plan(plan, only_safe=only_safe, backup_dir=backup_dir)
        print(format_apply_summary(
            apply_result.changed_files,
            apply_result.skipped_files,
            apply_result.errors,
        ))
        if write_diff and apply_result.diff_lines_by_file:
            write_diff_report(apply_result.diff_lines_by_file, write_diff)
            print(f"Diff written to: {write_diff}")

    return plan


def _print_dry_run_diffs(plan: FixPlan, write_diff: Optional[Path]) -> None:
    """
    For dry-run: simulate changes and show diffs without writing.
    """
    from itdoc.fixes.applier import apply_insert_section, apply_strip_emoji
    from itdoc.fixes.rules import SECTION_PLACEHOLDERS
    import difflib

    diff_by_file: dict[str, list[str]] = {}

    for file_path_str, changes in sorted(plan.by_file().items()):
        file_path = Path(file_path_str)
        if not file_path.exists():
            continue

        applicable = [c for c in changes if c.safe_autofix and c.action != "report_only"]
        if not applicable:
            continue

        original = file_path.read_text(encoding='utf-8', errors='replace')
        new_content = original

        for change in applicable:
            if change.action == "insert_section":
                section = change.detail.get("section", "")
                placeholder = change.detail.get("placeholder", SECTION_PLACEHOLDERS.get(section, "<!-- TODO -->\n"))
                new_content = apply_insert_section(new_content, section, placeholder)
            elif change.action == "strip_emoji":
                new_content = apply_strip_emoji(new_content)

        diff_lines = list(difflib.unified_diff(
            original.splitlines(keepends=True),
            new_content.splitlines(keepends=True),
            fromfile=f"a/{file_path_str}",
            tofile=f"b/{file_path_str}",
        ))

        if diff_lines:
            diff_by_file[file_path_str] = diff_lines
            print(f"\nDiff: {file_path_str}")
            for line in diff_lines[:30]:
                print(line, end='')
            if len(diff_lines) > 30:
                print(f"  ... ({len(diff_lines) - 30} more lines)")

    if write_diff and diff_by_file:
        write_diff_report(diff_by_file, write_diff)
        print(f"\nFull diff written to: {write_diff}")
