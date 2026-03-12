#!/usr/bin/env python3
"""
compliance_check.py — Zunifikowany punkt wejścia dla narzędzi compliance.

Subkomendy:
  check-schema      Walidacja schematu szablonów (validate_template_schema.py)
  coverage-report   Raport pokrycia standardów (compliance_coverage_report.py)
  backfill          Backfill confidence mapowań (backfill_mapping_confidence.py)
  full-audit        Wszystkie powyższe sekwencyjnie z podsumowaniem

Użycie:
  python3 compliance_check.py check-schema [--strict] [--db PATH]
  python3 compliance_check.py coverage-report [--format html|json|csv] [--db PATH]
  python3 compliance_check.py backfill [--apply] [--dry-run] [--db PATH]
  python3 compliance_check.py full-audit [--apply] [--db PATH] [--ci]
"""
import argparse
import logging
import subprocess
import sys
import sqlite3
from pathlib import Path

from itdoc._batch import batch_continue

_log = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent.parent
DB_DEFAULT = BASE_DIR / "reports" / "it_doc_matrix.db"
SCRIPTS_DIR = Path(__file__).parent
MAINTENANCE_DIR = SCRIPTS_DIR / "maintenance"


def get_db_stats(db_path: Path) -> dict:
    """
    Quick DB stats for the summary:
    - total_mappings
    - null_confidence
    - error_violations (from template_violations)
    - warning_violations
    Returns dict.
    """
    stats = {
        "total_mappings": 0,
        "null_confidence": 0,
        "error_violations": 0,
        "warning_violations": 0,
    }
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        try:
            cur.execute("SELECT COUNT(*) FROM doc_standard_mapping")
            stats["total_mappings"] = cur.fetchone()[0]
        except sqlite3.OperationalError as exc:
            _log.debug("doc_standard_mapping table unavailable: %s", exc)  # table may not exist

        try:
            cur.execute("SELECT COUNT(*) FROM doc_standard_mapping WHERE confidence IS NULL")
            stats["null_confidence"] = cur.fetchone()[0]
        except sqlite3.OperationalError as exc:
            _log.debug("doc_standard_mapping.confidence column unavailable: %s", exc)  # table may not exist

        try:
            cur.execute("SELECT COUNT(*) FROM template_violations WHERE severity='ERROR'")
            stats["error_violations"] = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM template_violations WHERE severity='WARNING'")
            stats["warning_violations"] = cur.fetchone()[0]
        except sqlite3.OperationalError as exc:
            _log.debug("template_violations table unavailable: %s", exc)  # optional table
    finally:
        conn.close()
    return stats


def run_check_schema(db_path: Path, strict: bool = False) -> dict:
    """
    Runs validate_template_schema.py --report [--strict] --db PATH
    Returns: {'violations_error': N, 'violations_warning': N, 'exit_code': 0|1}
    """
    cmd = [sys.executable, str(SCRIPTS_DIR / "validate_template_schema.py"),
           "--report", "--db", str(db_path)]
    if strict:
        cmd.append("--strict")

    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout + result.stderr

    violations_error = 0
    violations_warning = 0
    for line in output.splitlines():
        line_lower = line.lower()
        if "error" in line_lower:
            import re
            m = re.search(r"(\d+)", line)
            if m:
                violations_error = int(m.group(1))
        if "warning" in line_lower:
            import re
            m = re.search(r"(\d+)", line)
            if m:
                violations_warning = int(m.group(1))

    return {
        "violations_error": violations_error,
        "violations_warning": violations_warning,
        "exit_code": result.returncode,
    }


def run_coverage_report(db_path: Path, fmt: str = "html") -> dict:
    """
    Runs compliance_coverage_report.py --format FMT --db PATH
    Returns: {'output_file': PATH, 'exit_code': 0|1}
    """
    cmd = [sys.executable, str(SCRIPTS_DIR / "compliance_coverage_report.py"),
           "--format", fmt, "--db", str(db_path)]

    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout + result.stderr

    output_file = ""
    for line in output.splitlines():
        if "report" in line.lower() or "output" in line.lower() or ".html" in line or ".json" in line or ".csv" in line:
            parts = line.split()
            for part in parts:
                if part.endswith((".html", ".json", ".csv")):
                    output_file = part
                    break

    return {
        "output_file": output_file,
        "exit_code": result.returncode,
    }


def run_backfill(db_path: Path, apply: bool = False) -> dict:
    """
    Runs backfill_mapping_confidence.py --dry-run or --apply --db PATH
    Returns: {'rows_updated': N, 'exit_code': 0|1}
    """
    flag = "--apply" if apply else "--dry-run"
    cmd = [sys.executable, str(MAINTENANCE_DIR / "backfill_mapping_confidence.py"),
           flag, "--db", str(db_path)]

    result = subprocess.run(cmd, capture_output=True, text=True)
    output = result.stdout + result.stderr

    rows_updated = 0
    import re
    for line in output.splitlines():
        m = re.search(r"(\d+)\s*(rows?|row)", line, re.IGNORECASE)
        if m:
            rows_updated = int(m.group(1))
            break

    return {
        "rows_updated": rows_updated,
        "exit_code": result.returncode,
    }


def run_full_audit(db_path: Path, apply_backfill: bool = False, ci_mode: bool = False) -> int:
    """
    Runs all checks sequentially, prints summary table.
    Returns exit code: 0=OK, 1=failures (in --ci mode)
    """
    print("Running compliance full audit…")

    schema_result = run_check_schema(db_path)
    cov_result = run_coverage_report(db_path)
    bf_result = run_backfill(db_path, apply=apply_backfill)
    stats = get_db_stats(db_path)

    err = schema_result["violations_error"]
    warn = schema_result["violations_warning"]
    total = stats["total_mappings"]
    null_conf = stats["null_confidence"]

    # Compute ISO/IEC 27001 coverage if available
    coverage_pct = 0.0
    coverage_retrieved = False
    with batch_continue("iso27001 coverage query", logger=_log):
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("""
            SELECT COUNT(*) FROM doc_standard_mapping m
            JOIN standards s ON m.standard_id = s.id
            WHERE s.code LIKE '%27001%' AND m.confidence >= 0.5
        """)
        covered = cur.fetchone()[0]
        cur.execute("""
            SELECT COUNT(*) FROM standards WHERE code LIKE '%27001%'
        """)
        total_controls = cur.fetchone()[0]
        if total_controls > 0:
            coverage_pct = covered / total_controls * 100
        coverage_retrieved = True
        conn.close()

    err_icon = "✅" if err == 0 else "❌"
    warn_icon = "✅" if warn == 0 else "⚠️"
    cov_icon = "✅" if coverage_pct >= 5.0 else "⚠️"
    map_icon = "✅" if total > 0 else "⚠️"
    null_icon = "✅" if null_conf == 0 else "⚠️"

    print("╔══════════════════════════════════════════╗")
    print("║     COMPLIANCE FULL AUDIT SUMMARY        ║")
    print("╠══════════════════════════════════════════╣")
    print(f"║ Schema violations (ERROR):  {err:5d}    {err_icon:<5}║")
    print(f"║ Schema violations (WARNING):{warn:5d}    {warn_icon:<5}║")
    print(f"║ ISO/IEC 27001 coverage ≥0.5:{coverage_pct:4.1f}%   {cov_icon:<5}║")
    print(f"║ Mappings with confidence:   {total:5d}    {map_icon:<5}║")
    print(f"║ NULL confidence rows:       {null_conf:5d}    {null_icon:<5}║")
    print("╚══════════════════════════════════════════╝")

    if ci_mode:
        if err > 0 or (coverage_retrieved and coverage_pct < 5.0):
            print("EXIT: FAILED (1)")
            return 1

    print("EXIT: OK (0)")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Compliance check CLI")
    sub = parser.add_subparsers(dest="command")

    # check-schema subcommand
    p_schema = sub.add_parser("check-schema")
    p_schema.add_argument("--strict", action="store_true")
    p_schema.add_argument("--db", default=str(DB_DEFAULT))

    # coverage-report subcommand
    p_cov = sub.add_parser("coverage-report")
    p_cov.add_argument("--format", choices=["html", "json", "csv"], default="html")
    p_cov.add_argument("--db", default=str(DB_DEFAULT))

    # backfill subcommand
    p_bf = sub.add_parser("backfill")
    p_bf.add_argument("--apply", action="store_true")
    p_bf.add_argument("--dry-run", action="store_true", dest="dry_run")
    p_bf.add_argument("--db", default=str(DB_DEFAULT))

    # full-audit subcommand
    p_audit = sub.add_parser("full-audit")
    p_audit.add_argument("--apply", action="store_true")
    p_audit.add_argument("--ci", action="store_true")
    p_audit.add_argument("--db", default=str(DB_DEFAULT))

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        sys.exit(1)

    if args.command == "check-schema":
        result = run_check_schema(Path(args.db), strict=args.strict)
        sys.exit(result["exit_code"])
    elif args.command == "coverage-report":
        result = run_coverage_report(Path(args.db), fmt=args.format)
        sys.exit(result["exit_code"])
    elif args.command == "backfill":
        result = run_backfill(Path(args.db), apply=args.apply)
        sys.exit(result["exit_code"])
    elif args.command == "full-audit":
        sys.exit(run_full_audit(Path(args.db), apply_backfill=args.apply, ci_mode=args.ci))


if __name__ == "__main__":
    main()
