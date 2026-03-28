"""
Human-readable reporting for fix plans and apply results.
"""
from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from itdoc.fixes.planner import FixPlan, Change


_SEP = "=" * 72
_SEP2 = "-" * 72


def print_plan_summary(plan: "FixPlan", *, verbose: bool = False) -> None:
    """
    Print a human-readable summary of a FixPlan to stdout.
    """
    safe = plan.safe_changes()
    unsafe = plan.unsafe_changes()

    print(_SEP)
    print(f"Fix Plan Summary — {plan.run_id}")
    print(_SEP)
    print(f"  Mode          : {plan.mode}")
    print(f"  Root          : {plan.root}")
    print(f"  Files scanned : {plan.total_files}")
    print(f"  Total changes : {len(plan.changes)}")
    print(f"  Safe (auto)   : {len(safe)}")
    print(f"  Review needed : {len(unsafe)}")
    print()

    if not plan.changes:
        print("  ✓ No changes needed.")
        print(_SEP)
        return

    # Count by rule_id
    from collections import Counter
    by_rule: Counter = Counter(c.rule_id for c in plan.changes)
    print("Changes by rule:")
    for rule_id, count in sorted(by_rule.items()):
        marker = "✓" if any(c.safe_autofix for c in plan.changes if c.rule_id == rule_id) else "⚠"
        print(f"  {marker} {rule_id:<35} {count:>4}  {'(safe autofix)' if marker == '✓' else '(review required)'}")
    print()

    if verbose:
        print("File-level detail:")
        print(_SEP2)
        for file_path, changes in sorted(plan.by_file().items()):
            print(f"  {file_path}")
            for c in changes:
                safe_tag = "[safe]" if c.safe_autofix else "[review]"
                detail_str = _format_detail(c)
                print(f"    {safe_tag:10} {c.rule_id:<35} {detail_str}")
        print()

    print(_SEP)


def _format_detail(change: "Change") -> str:
    """Format a change detail dict as a short string."""
    d = change.detail
    if "section" in d:
        return f"section='{d['section']}'"
    if "message" in d:
        return d["message"][:60]
    if "error" in d:
        return f"error: {d['error'][:50]}"
    return str(d)[:60]


def write_diff_report(diff_lines_by_file: dict[str, list[str]], output: Path) -> None:
    """
    Write a unified-diff style report to a file.

    Args:
        diff_lines_by_file: mapping of file_path -> list of diff lines
        output: path to write the report
    """
    output.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"Autofix Diff Report\n",
        f"{_SEP}\n",
    ]
    for file_path, diff_lines in sorted(diff_lines_by_file.items()):
        if diff_lines:
            lines.append(f"\n--- {file_path} ---\n")
            lines.extend(diff_lines)
    output.write_text(''.join(lines), encoding='utf-8')


def format_apply_summary(
    changed_files: list[str],
    skipped_files: list[str],
    errors: list[tuple[str, str]],
) -> str:
    """
    Format a summary string after applying a fix plan.
    """
    lines = [
        f"{_SEP}",
        f"Apply Summary",
        f"{_SEP}",
        f"  Applied : {len(changed_files)} file(s)",
        f"  Skipped : {len(skipped_files)} file(s) (no change / unsafe)",
        f"  Errors  : {len(errors)}",
    ]
    if changed_files:
        lines.append("\nChanged:")
        for f in changed_files:
            lines.append(f"  ✓ {f}")
    if errors:
        lines.append("\nErrors:")
        for f, err in errors:
            lines.append(f"  ✗ {f}: {err}")
    lines.append(_SEP)
    return '\n'.join(lines)
