#!/usr/bin/env python3
"""
review_mappings.py — Workflow ręcznego przeglądu mapowań standard→szablon.

Użycie:
  # Eksport do przeglądu (confidence < 0.4, nie ręcznie sprawdzone)
  python3 review_mappings.py --export-pending --threshold 0.4 > review.csv
  python3 review_mappings.py --export-pending --standard "ISO/IEC 27001" > iso_review.csv

  # Import po przeglądzie (ekspert ustawił approved=yes/no w CSV)
  python3 review_mappings.py --import-reviewed review.csv --dry-run
  python3 review_mappings.py --import-reviewed review.csv --apply

  # Statystyki
  python3 review_mappings.py --stats
"""

import argparse
import csv
import io
import sqlite3
import sys
from pathlib import Path
from typing import Dict, List, Optional

# ---------------------------------------------------------------------------
# DB path helpers
# ---------------------------------------------------------------------------

_SCRIPT_DIR = Path(__file__).parent
DB_PATH = _SCRIPT_DIR.parent.parent / "reports" / "it_doc_matrix.db"

# Reason codes that are already authoritative — excluded from pending export
AUDITED_REASONS = {"explicit_audit", "expert_reviewed", "primary_standard"}

CSV_FIELDNAMES = ["id", "doc_path", "standard_code", "confidence", "match_reason",
                  "evidence", "approved", "notes"]


# ---------------------------------------------------------------------------
# Core logic — callable with any sqlite3.Connection (including :memory:)
# ---------------------------------------------------------------------------

def export_pending(
    conn: sqlite3.Connection,
    threshold: float = 0.4,
    standard: Optional[str] = None,
    limit: Optional[int] = None,
) -> List[Dict]:
    """Return rows pending expert review as list of dicts.

    Args:
        conn: SQLite connection.
        threshold: Export rows where confidence < threshold.
        standard: If given, filter to this standard_code only.
        limit: Max rows to return (None = all).

    Returns:
        List of dicts with keys matching CSV_FIELDNAMES.
    """
    placeholders_reason = ",".join("?" for _ in AUDITED_REASONS)
    query = (  # nosec B608 -- f-string builds IN-placeholders ("?,?,?") only; all values bound via params
        f"SELECT id, doc_path, standard_code, confidence, match_reason, evidence "
        f"FROM doc_standard_mapping "
        f"WHERE confidence < ? "
        f"AND match_reason NOT IN ({placeholders_reason})"
    )
    params: list = [threshold, *AUDITED_REASONS]

    if standard:
        query += " AND standard_code = ?"
        params.append(standard)

    query += " ORDER BY standard_code ASC, confidence DESC"

    if limit is not None:
        query += f" LIMIT {int(limit)}"  # nosec B608 -- int() cast ensures numeric value

    rows = conn.execute(query, params).fetchall()

    result = []
    for row in rows:
        # Support both sqlite3.Row and plain tuple
        if hasattr(row, "keys"):
            d = dict(row)
        else:
            d = dict(zip(
                ["id", "doc_path", "standard_code", "confidence", "match_reason", "evidence"],
                row,
            ))
        d["approved"] = ""
        d["notes"] = ""
        d.setdefault("evidence", "")
        result.append(d)
    return result


def import_reviewed(
    conn: sqlite3.Connection,
    rows: List[Dict],
    dry_run: bool = False,
    keep_rejected: bool = False,
) -> Dict:
    """Apply expert decisions from a list of CSV rows.

    Args:
        conn: SQLite connection.
        rows: List of dicts (CSV rows).  Each must have 'id' and 'approved'.
        dry_run: If True simulate only, make no DB changes.
        keep_rejected: If True, UPDATE rejected rows (confidence=0, reason='rejected')
                       instead of DELETE.

    Returns:
        Dict with keys 'approved', 'rejected', 'skipped'.
    """
    counts = {"approved": 0, "rejected": 0, "skipped": 0}

    for row in rows:
        row_id = int(row["id"])
        approved = str(row.get("approved", "")).strip().lower()
        notes = str(row.get("notes", "")).strip()

        if approved == "yes":
            # Confidence: use value from CSV, floor at 0.8
            try:
                csv_conf = float(row.get("confidence", 0.0))
            except (ValueError, TypeError):
                csv_conf = 0.0
            new_conf = max(csv_conf, 0.8)
            evidence = f"expert approved: {notes}" if notes else "expert approved"

            if not dry_run:
                conn.execute(
                    "UPDATE doc_standard_mapping "
                    "SET match_reason='expert_reviewed', confidence=?, evidence=? "
                    "WHERE id=?",
                    (new_conf, evidence, row_id),
                )
            counts["approved"] += 1

        elif approved == "no":
            if not dry_run:
                if keep_rejected:
                    conn.execute(
                        "UPDATE doc_standard_mapping "
                        "SET match_reason='rejected', confidence=0.0 "
                        "WHERE id=?",
                        (row_id,),
                    )
                else:
                    conn.execute(
                        "DELETE FROM doc_standard_mapping WHERE id=?",
                        (row_id,),
                    )
            counts["rejected"] += 1

        else:
            counts["skipped"] += 1

    if not dry_run:
        conn.commit()

    return counts


def stats(conn: sqlite3.Connection) -> Dict:
    """Return mapping statistics as a dict.

    Returns:
        Dict with keys:
          'total' (int),
          'by_reason' (dict reason→count),
          'by_confidence_tier' (dict tier_label→count),
          'pending_review' (int).
    """
    total = conn.execute("SELECT COUNT(*) FROM doc_standard_mapping").fetchone()[0]

    reason_rows = conn.execute(
        "SELECT match_reason, COUNT(*) FROM doc_standard_mapping GROUP BY match_reason"
    ).fetchall()
    by_reason = {r[0] if r[0] else "": r[1] for r in reason_rows}

    tiers = [
        (">=0.9",  "SELECT COUNT(*) FROM doc_standard_mapping WHERE confidence >= 0.9"),
        (">=0.7",  "SELECT COUNT(*) FROM doc_standard_mapping WHERE confidence >= 0.7 AND confidence < 0.9"),
        (">=0.5",  "SELECT COUNT(*) FROM doc_standard_mapping WHERE confidence >= 0.5 AND confidence < 0.7"),
        (">=0.3",  "SELECT COUNT(*) FROM doc_standard_mapping WHERE confidence >= 0.3 AND confidence < 0.5"),
        ("<0.3",   "SELECT COUNT(*) FROM doc_standard_mapping WHERE confidence < 0.3"),
    ]
    by_confidence_tier = {}
    for label, query in tiers:
        by_confidence_tier[label] = conn.execute(query).fetchone()[0]

    audited_placeholders = ",".join("?" for _ in AUDITED_REASONS)
    pending_review = conn.execute(  # nosec B608 -- f-string builds IN-placeholders only; values bound via params
        f"SELECT COUNT(*) FROM doc_standard_mapping "
        f"WHERE confidence < 0.4 AND match_reason NOT IN ({audited_placeholders})",
        list(AUDITED_REASONS),
    ).fetchone()[0]

    return {
        "total": total,
        "by_reason": by_reason,
        "by_confidence_tier": by_confidence_tier,
        "pending_review": pending_review,
    }


# ---------------------------------------------------------------------------
# CSV helpers
# ---------------------------------------------------------------------------

def rows_to_csv(rows: List[Dict], out=None) -> Optional[str]:
    """Write rows as CSV to `out` (file-like) or return string if out is None."""
    return_str = out is None
    if return_str:
        out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=CSV_FIELDNAMES, extrasaction="ignore",
                            lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    if return_str:
        return out.getvalue()
    return None


def read_csv(path: str) -> List[Dict]:
    """Read CSV file and return list of dicts."""
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ---------------------------------------------------------------------------
# CLI rendering
# ---------------------------------------------------------------------------

def _format_stats(s: Dict) -> str:
    total = s["total"]
    lines = [
        "Mapping Review Statistics",
        "=========================",
        f"Total mappings:  {total:>10,}",
    ]
    for reason, count in sorted(s["by_reason"].items(), key=lambda x: -x[1]):
        pct = (count / total * 100) if total else 0.0
        lines.append(f"  {reason:<30} {count:>8,}  ({pct:.1f}%)")
    lines.append("")
    lines.append("By confidence tier:")
    for label, count in s["by_confidence_tier"].items():
        pct = (count / total * 100) if total else 0.0
        lines.append(f"  {label:<8}  {count:>8,}  ({pct:.1f}%)")
    lines.append("")
    lines.append(f"Pending review (confidence < 0.4, not audited): {s['pending_review']:,}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# main / CLI
# ---------------------------------------------------------------------------

def _open_db(db_path: Optional[Path] = None) -> sqlite3.Connection:
    path = Path(db_path) if db_path else DB_PATH
    if not path.exists():
        sys.exit(f"ERROR: DB not found: {path}")
    conn = sqlite3.connect(str(path), timeout=30)
    return conn


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="review_mappings.py — bulk expert review of standard→template mappings"
    )
    parser.add_argument("--db", metavar="PATH", help="Override DB path")

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--export-pending", action="store_true")
    mode.add_argument("--import-reviewed", metavar="FILE")
    mode.add_argument("--stats", action="store_true")

    # export options
    parser.add_argument("--threshold", type=float, default=0.4,
                        help="Confidence threshold for export (default: 0.4)")
    parser.add_argument("--standard", metavar="CODE",
                        help="Filter export to one standard_code")
    parser.add_argument("--limit", type=int, default=None,
                        help="Max rows to export")
    parser.add_argument("--output", metavar="PATH",
                        help="Write CSV to file instead of stdout")

    # import options
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would happen, no writes")
    parser.add_argument("--apply", action="store_true",
                        help="Actually write changes")
    parser.add_argument("--keep-rejected", action="store_true",
                        help="UPDATE rejected rows instead of DELETE")

    args = parser.parse_args(argv)

    conn = _open_db(args.db)

    try:
        if args.export_pending:
            rows = export_pending(
                conn,
                threshold=args.threshold,
                standard=args.standard,
                limit=args.limit,
            )
            if args.output:
                with open(args.output, "w", newline="", encoding="utf-8") as f:
                    rows_to_csv(rows, out=f)
                print(f"Exported {len(rows)} rows → {args.output}", file=sys.stderr)
            else:
                csv_text = rows_to_csv(rows)
                sys.stdout.write(csv_text)
                print(f"\n# {len(rows)} rows exported.", file=sys.stderr)

        elif args.import_reviewed:
            if not args.dry_run and not args.apply:
                sys.exit("ERROR: specify --dry-run or --apply")
            rows = read_csv(args.import_reviewed)
            counts = import_reviewed(
                conn,
                rows,
                dry_run=args.dry_run,
                keep_rejected=args.keep_rejected,
            )
            mode_label = "DRY RUN — " if args.dry_run else ""
            print(
                f"{mode_label}approved: {counts['approved']}, "
                f"rejected: {counts['rejected']}, "
                f"skipped: {counts['skipped']}"
            )

        elif args.stats:
            s = stats(conn)
            print(_format_stats(s))

    finally:
        conn.close()


if __name__ == "__main__":
    main()
