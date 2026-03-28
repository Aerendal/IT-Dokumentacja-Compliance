#!/usr/bin/env python3
"""
fix_docs.py — Autofix engine for IT documentation templates.

Usage:
  Analyze (no writes):
    python scripts/fix_docs.py --root generated_templates/demo_case_01 --mode analyze --output reports/fix_plan.json

  Dry-run (diffs but no writes):
    python scripts/fix_docs.py --root generated_templates/demo_case_01 --mode dry-run --output reports/fix_plan.json --write-diff reports/fix_diff.txt

  Apply safe fixes:
    python scripts/fix_docs.py --root generated_templates/demo_case_01 --mode apply --output reports/fix_plan.json --only-safe
"""
import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Autofix structural violations in Markdown documentation templates.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--root", required=True, type=Path,
        help="Root directory to scan for .md files",
    )
    parser.add_argument(
        "--mode", required=True, choices=["analyze", "dry-run", "apply"],
        help="Operation mode: analyze (no writes), dry-run (diffs only), apply (write safe fixes)",
    )
    parser.add_argument(
        "--output", required=True, type=Path,
        help="Path for the JSON fix plan output",
    )
    parser.add_argument(
        "--write-diff", type=Path, default=None, dest="write_diff",
        help="Path to write a unified diff report (optional)",
    )
    parser.add_argument(
        "--only-safe", action="store_true", default=True, dest="only_safe",
        help="Only apply changes marked safe_autofix=True (default: True)",
    )
    parser.add_argument(
        "--backup-dir", type=Path, default=Path("reports/autofix_backups"), dest="backup_dir",
        help="Directory for file backups before apply (default: reports/autofix_backups)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", default=False,
        help="Print file-level detail in summary",
    )
    args = parser.parse_args()

    if not args.root.exists():
        print(f"ERROR: Root directory does not exist: {args.root}", file=sys.stderr)
        return 1

    from itdoc.fixes.engine import run
    try:
        run(
            root=args.root,
            mode=args.mode,
            output_plan=args.output,
            write_diff=args.write_diff,
            only_safe=args.only_safe,
            backup_dir=args.backup_dir,
            verbose=args.verbose,
        )
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
