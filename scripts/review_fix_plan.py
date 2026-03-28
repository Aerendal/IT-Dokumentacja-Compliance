#!/usr/bin/env python3
"""
review_fix_plan.py — Display a fix plan JSON in human-readable format.

Usage:
  python scripts/review_fix_plan.py --plan reports/fix_plan.json
  python scripts/review_fix_plan.py --plan reports/fix_plan.json --verbose
  python scripts/review_fix_plan.py --plan reports/fix_plan.json --filter safe
  python scripts/review_fix_plan.py --plan reports/fix_plan.json --filter review
"""
import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Display a fix plan JSON in human-readable format.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--plan", required=True, type=Path,
        help="Path to the fix plan JSON file",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", default=False,
        help="Print file-level detail",
    )
    parser.add_argument(
        "--filter", choices=["all", "safe", "review"], default="all", dest="filter_mode",
        help="Filter changes: all (default), safe (only safe_autofix=True), review (only review required)",
    )
    args = parser.parse_args()

    if not args.plan.exists():
        print(f"ERROR: Plan file not found: {args.plan}", file=sys.stderr)
        return 1

    from itdoc.fixes.planner import load_plan
    from itdoc.fixes.report import print_plan_summary

    plan = load_plan(args.plan)

    # Apply filter
    if args.filter_mode == "safe":
        plan.changes = plan.safe_changes()
        print(f"[filter: safe_autofix=True — {len(plan.changes)} changes]\n")
    elif args.filter_mode == "review":
        plan.changes = plan.unsafe_changes()
        print(f"[filter: review_required — {len(plan.changes)} changes]\n")

    print_plan_summary(plan, verbose=args.verbose)
    return 0


if __name__ == "__main__":
    sys.exit(main())
