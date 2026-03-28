#!/usr/bin/env python3
"""
apply_fix_plan.py — Apply a fix plan to files on disk.

Usage:
  Apply only safe fixes (recommended):
    python scripts/apply_fix_plan.py --plan reports/fix_plan.json --only-safe

  Apply all changes (including review-required):
    python scripts/apply_fix_plan.py --plan reports/fix_plan.json

  With custom backup directory:
    python scripts/apply_fix_plan.py --plan reports/fix_plan.json --only-safe --backup-dir reports/my_backups
"""
import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Apply a fix plan to documentation template files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--plan", required=True, type=Path,
        help="Path to the fix plan JSON file",
    )
    parser.add_argument(
        "--only-safe", action="store_true", default=True, dest="only_safe",
        help="Only apply changes marked safe_autofix=True (default: True)",
    )
    parser.add_argument(
        "--backup-dir", type=Path, default=Path("reports/autofix_backups"), dest="backup_dir",
        help="Directory for file backups (default: reports/autofix_backups)",
    )
    parser.add_argument(
        "--write-diff", type=Path, default=None, dest="write_diff",
        help="Write diff report to this path after applying",
    )
    parser.add_argument(
        "--write-result", type=Path, default=None, dest="write_result",
        help="Write apply result as JSON to this path",
    )
    args = parser.parse_args()

    if not args.plan.exists():
        print(f"ERROR: Plan file not found: {args.plan}", file=sys.stderr)
        return 1

    from itdoc.fixes.planner import load_plan
    from itdoc.fixes.applier import apply_plan
    from itdoc.fixes.report import format_apply_summary, write_diff_report

    plan = load_plan(args.plan)

    safe_count = len(plan.safe_changes())
    unsafe_count = len(plan.unsafe_changes())
    print(f"Plan: {len(plan.changes)} total changes ({safe_count} safe, {unsafe_count} review-required)")
    if args.only_safe:
        print(f"Mode: --only-safe (applying {safe_count} changes)")
    else:
        print(f"Mode: ALL changes ({len(plan.changes)} changes)")

    result = apply_plan(plan, only_safe=args.only_safe, backup_dir=args.backup_dir)

    print(format_apply_summary(result.changed_files, result.skipped_files, result.errors))

    if args.write_diff and result.diff_lines_by_file:
        write_diff_report(result.diff_lines_by_file, args.write_diff)
        print(f"Diff written to: {args.write_diff}")

    if args.write_result:
        import json
        args.write_result.parent.mkdir(parents=True, exist_ok=True)
        args.write_result.write_text(
            json.dumps(result.to_dict(run_id=plan.run_id), ensure_ascii=False, indent=2),
            encoding='utf-8'
        )
        print(f"Result JSON written to: {args.write_result}")

    # Exit 1 if any errors
    return 1 if result.errors else 0


if __name__ == "__main__":
    sys.exit(main())
