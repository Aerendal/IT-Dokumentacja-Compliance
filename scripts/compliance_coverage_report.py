"""scripts/compliance_coverage_report.py

Compliance Coverage Report — generates coverage metrics per standard and regulation.

Usage:
    python3 scripts/compliance_coverage_report.py [options]

Options:
    --standard CODE       Report for a single standard only
    --regulation CODE     Report for a single regulation only
    --format {text,csv,json,html}  Output format (default: text)
    --output PATH         Output file path (default: stdout for text, auto for others)
    --show-gaps           Show only standards/regulations with coverage < min_confidence
    --min-confidence F    Threshold for "covered" (default: 0.5)
    --db PATH             Path to SQLite DB (default: reports/it_doc_matrix.db)
"""

import argparse
import csv
import io
import json
import sqlite3
from datetime import datetime
from pathlib import Path

_REPO_ROOT = Path(__file__).parent.parent
_DEFAULT_DB = _REPO_ROOT / "reports" / "it_doc_matrix.db"


# ---------------------------------------------------------------------------
# Core metric functions (importable / testable)
# ---------------------------------------------------------------------------

def compute_standard_metrics(conn: sqlite3.Connection, standard_code: str,
                              min_confidence: float = 0.5) -> dict:
    """Return coverage metrics for a single standard.

    Returns dict with keys:
        total_mappings, high_conf_50, high_conf_70, high_conf_90, guidance_sections
    """
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM doc_standard_mapping WHERE standard_code = ?",
                (standard_code,))
    total_mappings = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM doc_standard_mapping WHERE standard_code = ? AND confidence >= 0.5",
                (standard_code,))
    high_conf_50 = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM doc_standard_mapping WHERE standard_code = ? AND confidence >= 0.7",
                (standard_code,))
    high_conf_70 = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM doc_standard_mapping WHERE standard_code = ? AND confidence >= 0.9",
                (standard_code,))
    high_conf_90 = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM guidance_standard_links WHERE standard_code = ?",
                (standard_code,))
    guidance_sections = cur.fetchone()[0]

    return {
        "standard_code": standard_code,
        "total_mappings": total_mappings,
        "high_conf_50": high_conf_50,
        "high_conf_70": high_conf_70,
        "high_conf_90": high_conf_90,
        "guidance_sections": guidance_sections,
    }


def compute_regulation_metrics(conn: sqlite3.Connection, regulation_code: str) -> dict:
    """Return coverage metrics for a single regulation.

    Returns dict with keys:
        regulation_code, guidance_sections, unique_docs
    """
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM guidance_regulation_links WHERE regulation_code = ?",
                (regulation_code,))
    guidance_sections = cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(DISTINCT g.doc_title)
        FROM guidance_regulation_links gl
        JOIN doc_section_guidance g ON gl.guidance_id = g.id
        WHERE gl.regulation_code = ?
    """, (regulation_code,))
    unique_docs = cur.fetchone()[0]

    return {
        "regulation_code": regulation_code,
        "guidance_sections": guidance_sections,
        "unique_docs": unique_docs,
    }


def compute_control_metrics(conn: sqlite3.Connection, standard_code: str) -> list[dict]:
    """Return per-control coverage metrics for a standard.

    Returns list of dicts:
        control_id, control_name, theme, template_count,
        avg_confidence, max_confidence, coverage_tier
    Sorted by theme ASC, control_id ASC.
    Tier: none=0, low=1-2, medium=3-9, high>=10.
    Returns [] if standard_controls table does not exist.
    """
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT sc.control_id, sc.control_name, sc.theme,
                   COUNT(dcm.id) as template_count,
                   ROUND(AVG(dcm.confidence), 3) as avg_confidence,
                   ROUND(MAX(dcm.confidence), 3) as max_confidence
            FROM standard_controls sc
            LEFT JOIN doc_control_mapping dcm
                ON sc.control_id = dcm.control_id AND sc.standard_code = dcm.standard_code
            WHERE sc.standard_code = ?
            GROUP BY sc.control_id, sc.control_name, sc.theme
            ORDER BY sc.theme ASC, sc.control_id ASC
        """, (standard_code,))
        rows = cur.fetchall()
    except sqlite3.OperationalError:
        return []

    result = []
    for row in rows:
        control_id, control_name, theme, template_count, avg_conf, max_conf = row
        if template_count == 0:
            tier = "none"
        elif template_count <= 2:
            tier = "low"
        elif template_count <= 9:
            tier = "medium"
        else:
            tier = "high"
        result.append({
            "control_id": control_id,
            "control_name": control_name,
            "theme": theme,
            "template_count": template_count,
            "avg_confidence": avg_conf,
            "max_confidence": max_conf,
            "coverage_tier": tier,
        })
    return result


def _get_standards_with_controls(conn: sqlite3.Connection) -> list[str]:
    """Return list of standard_codes that have entries in standard_controls table."""
    try:
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT standard_code FROM standard_controls ORDER BY standard_code")
        return [r[0] for r in cur.fetchall()]
    except sqlite3.OperationalError:
        return []


def _get_standards(conn: sqlite3.Connection, standard_code: str | None = None) -> list[dict]:
    cur = conn.cursor()
    if standard_code:
        cur.execute("SELECT standard_code, standard_name FROM standards WHERE standard_code = ?",
                    (standard_code,))
    else:
        cur.execute("SELECT standard_code, standard_name FROM standards ORDER BY standard_code")
    return [{"standard_code": r[0], "standard_name": r[1]} for r in cur.fetchall()]


def _get_regulations(conn: sqlite3.Connection, regulation_code: str | None = None) -> list[dict]:
    cur = conn.cursor()
    if regulation_code:
        cur.execute("SELECT regulation_code, regulation_name FROM compliance_regulations WHERE regulation_code = ?",
                    (regulation_code,))
    else:
        cur.execute("SELECT regulation_code, regulation_name FROM compliance_regulations ORDER BY regulation_code")
    return [{"regulation_code": r[0], "regulation_name": r[1]} for r in cur.fetchall()]


def _total_docs(conn: sqlite3.Connection) -> int:
    cur = conn.cursor()
    cur.execute("SELECT COUNT(DISTINCT doc_path) FROM doc_standard_mapping")
    row = cur.fetchone()
    return row[0] if row else 0


# ---------------------------------------------------------------------------
# Report generators
# ---------------------------------------------------------------------------

def generate_json_report(conn: sqlite3.Connection,
                         standards: list[dict],
                         regulations: list[dict],
                         min_confidence: float = 0.5) -> dict:
    """Return the full report as a Python dict (JSON-serialisable)."""
    total_templates = _total_docs(conn)

    std_rows = []
    for s in standards:
        m = compute_standard_metrics(conn, s["standard_code"], min_confidence)
        m["name"] = s["standard_name"]
        coverage = m["high_conf_50"] / total_templates if total_templates else 0
        m["coverage_pct_50"] = round(coverage * 100, 2)
        std_rows.append(m)

    reg_rows = []
    for r in regulations:
        m = compute_regulation_metrics(conn, r["regulation_code"])
        m["name"] = r["regulation_name"]
        reg_rows.append(m)

    control_metrics: dict[str, list[dict]] = {}
    for code in _get_standards_with_controls(conn):
        control_metrics[code] = compute_control_metrics(conn, code)

    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "total_templates": total_templates,
        "standards": std_rows,
        "regulations": reg_rows,
        "control_metrics": control_metrics,
    }


def generate_text_report(conn: sqlite3.Connection,
                         standards: list[dict],
                         regulations: list[dict],
                         min_confidence: float = 0.5) -> str:
    """Return the full report as a formatted text string."""
    total_templates = _total_docs(conn)
    lines: list[str] = []

    lines.append("=" * 80)
    lines.append("Compliance Coverage Report")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Total unique documents in library: {total_templates:,}")
    lines.append("=" * 80)

    # Standards table
    lines.append("\nStandards Coverage:")
    hdr = f"{'Standard Code':<22} {'Standard Name':<40} {'Total':>7} {'>=0.5':>7} {'>=0.7':>7} {'>=0.9':>7} {'Guidance':>9}"
    sep = "-" * len(hdr)
    lines.append(sep)
    lines.append(hdr)
    lines.append(sep)
    for s in standards:
        m = compute_standard_metrics(conn, s["standard_code"], min_confidence)
        name = s["standard_name"][:38]
        lines.append(
            f"{s['standard_code']:<22} {name:<40} "
            f"{m['total_mappings']:>7,} {m['high_conf_50']:>7,} "
            f"{m['high_conf_70']:>7,} {m['high_conf_90']:>7,} "
            f"{m['guidance_sections']:>9,}"
        )
    lines.append(sep)

    # Regulations table
    lines.append("\nRegulations Coverage:")
    hdr2 = f"{'Regulation Code':<22} {'Regulation Name':<40} {'Guidance':>9} {'Unique Docs':>12}"
    sep2 = "-" * len(hdr2)
    lines.append(sep2)
    lines.append(hdr2)
    lines.append(sep2)
    for r in regulations:
        m = compute_regulation_metrics(conn, r["regulation_code"])
        name = r["regulation_name"][:38]
        lines.append(
            f"{r['regulation_code']:<22} {name:<40} "
            f"{m['guidance_sections']:>9,} {m['unique_docs']:>12,}"
        )
    lines.append(sep2)

    return "\n".join(lines)


def generate_csv_report(conn: sqlite3.Connection,
                        standards: list[dict],
                        regulations: list[dict],
                        min_confidence: float = 0.5) -> tuple[str, str]:
    """Return (standards_csv, regulations_csv) as strings."""
    # Standards CSV
    std_buf = io.StringIO()
    std_writer = csv.writer(std_buf)
    std_writer.writerow([
        "standard_code", "standard_name", "total_mappings",
        "high_conf_50", "high_conf_70", "high_conf_90", "guidance_sections"
    ])
    for s in standards:
        m = compute_standard_metrics(conn, s["standard_code"], min_confidence)
        std_writer.writerow([
            s["standard_code"], s["standard_name"],
            m["total_mappings"], m["high_conf_50"], m["high_conf_70"],
            m["high_conf_90"], m["guidance_sections"],
        ])

    # Regulations CSV
    reg_buf = io.StringIO()
    reg_writer = csv.writer(reg_buf)
    reg_writer.writerow(["regulation_code", "regulation_name", "guidance_sections", "unique_docs"])
    for r in regulations:
        m = compute_regulation_metrics(conn, r["regulation_code"])
        reg_writer.writerow([
            r["regulation_code"], r["regulation_name"],
            m["guidance_sections"], m["unique_docs"],
        ])

    return std_buf.getvalue(), reg_buf.getvalue()


def _coverage_color(ratio: float) -> str:
    if ratio >= 0.5:
        return "#2e7d32"   # green
    elif ratio >= 0.2:
        return "#f57c00"   # orange/yellow
    else:
        return "#c62828"   # red


def generate_html_report(conn: sqlite3.Connection,
                         standards: list[dict],
                         regulations: list[dict],
                         min_confidence: float = 0.5) -> str:
    """Return the full report as an HTML string with inline styles."""
    total_templates = _total_docs(conn)

    std_rows_html: list[str] = []
    for s in standards:
        m = compute_standard_metrics(conn, s["standard_code"], min_confidence)
        ratio = m["high_conf_50"] / total_templates if total_templates else 0
        color = _coverage_color(ratio)
        pct = f"{ratio * 100:.1f}%"
        std_rows_html.append(
            f'<tr>'
            f'<td>{s["standard_code"]}</td>'
            f'<td>{s["standard_name"]}</td>'
            f'<td style="text-align:right">{m["total_mappings"]:,}</td>'
            f'<td style="text-align:right;color:{color};font-weight:bold">{m["high_conf_50"]:,}</td>'
            f'<td style="text-align:right">{m["high_conf_70"]:,}</td>'
            f'<td style="text-align:right">{m["high_conf_90"]:,}</td>'
            f'<td style="text-align:right">{m["guidance_sections"]:,}</td>'
            f'<td style="text-align:right;color:{color};font-weight:bold">{pct}</td>'
            f'</tr>'
        )

    reg_rows_html: list[str] = []
    for r in regulations:
        m = compute_regulation_metrics(conn, r["regulation_code"])
        reg_rows_html.append(
            f'<tr>'
            f'<td>{r["regulation_code"]}</td>'
            f'<td>{r["regulation_name"]}</td>'
            f'<td style="text-align:right">{m["guidance_sections"]:,}</td>'
            f'<td style="text-align:right">{m["unique_docs"]:,}</td>'
            f'</tr>'
        )

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    table_style = (
        'style="border-collapse:collapse;width:100%;font-family:sans-serif;font-size:13px"'
    )
    th_style = (
        'style="background:#1565c0;color:white;padding:8px 12px;text-align:left;'
        'border:1px solid #ccc"'
    )
    td_style = 'style="padding:6px 12px;border:1px solid #ddd"'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Compliance Coverage Report</title>
  <style>
    body {{ font-family: sans-serif; margin: 24px; background: #fafafa; color: #222; }}
    h1 {{ color: #1565c0; }}
    h2 {{ color: #0d47a1; margin-top: 32px; }}
    .summary {{ background: #e3f2fd; border-left: 4px solid #1565c0;
                padding: 12px 20px; margin-bottom: 24px; border-radius: 4px; }}
    table {{ border-collapse: collapse; width: 100%; font-size: 13px; }}
    th {{ background: #1565c0; color: white; padding: 8px 12px;
          text-align: left; border: 1px solid #ccc; }}
    td {{ padding: 6px 12px; border: 1px solid #ddd; }}
    tr:nth-child(even) {{ background: #f5f5f5; }}
    .tier-none {{ background-color: #ffcccc; }}
    .tier-low  {{ background-color: #ffd9a0; }}
    .tier-medium {{ background-color: #ffffcc; }}
    .tier-high {{ background-color: #ccffcc; }}
  </style>
</head>
<body>
  <h1>Compliance Coverage Report</h1>
  <div class="summary">
    <strong>Generated:</strong> {generated_at}<br>
    <strong>Total unique documents in library:</strong> {total_templates:,}<br>
    <strong>Standards tracked:</strong> {len(standards)}<br>
    <strong>Regulations tracked:</strong> {len(regulations)}
  </div>

  <h2>Standards Coverage</h2>
  <table>
    <thead>
      <tr>
        <th>Code</th><th>Name</th><th>Total Mappings</th>
        <th>&ge;0.5 conf</th><th>&ge;0.7 conf</th><th>&ge;0.9 conf</th>
        <th>Guidance Sections</th><th>Coverage %</th>
      </tr>
    </thead>
    <tbody>
      {''.join(std_rows_html)}
    </tbody>
  </table>

  <h2>Regulations Coverage</h2>
  <table>
    <thead>
      <tr>
        <th>Code</th><th>Name</th><th>Guidance Sections</th><th>Unique Docs</th>
      </tr>
    </thead>
    <tbody>
      {''.join(reg_rows_html)}
    </tbody>
  </table>

  {_build_control_sections_html(conn)}
</body>
</html>
"""
    return html


def _build_control_sections_html(conn: sqlite3.Connection) -> str:
    """Build HTML sections for per-control coverage breakdown."""
    sections: list[str] = []
    for standard_code in _get_standards_with_controls(conn):
        metrics = compute_control_metrics(conn, standard_code)
        if not metrics:
            continue
        total = len(metrics)
        with_coverage = sum(1 for m in metrics if m["template_count"] > 0)
        no_coverage = total - with_coverage
        pct_covered = round(with_coverage / total * 100, 1) if total else 0
        pct_none = round(no_coverage / total * 100, 1) if total else 0

        rows_html = []
        for m in metrics:
            tier = m["coverage_tier"]
            avg = m["avg_confidence"] if m["avg_confidence"] is not None else "-"
            rows_html.append(
                f'<tr class="tier-{tier}">'
                f'<td>{m["control_id"]}</td>'
                f'<td>{m["control_name"]}</td>'
                f'<td>{m["theme"]}</td>'
                f'<td style="text-align:right">{m["template_count"]}</td>'
                f'<td style="text-align:right">{avg}</td>'
                f'<td>{tier}</td>'
                f'</tr>'
            )

        sections.append(f"""
  <h2>Per-Control Coverage: {standard_code}</h2>
  <p>Total controls: {total} | With coverage: {with_coverage} ({pct_covered}%) | No coverage: {no_coverage} ({pct_none}%)</p>
  <table>
    <thead>
      <tr><th>Control ID</th><th>Name</th><th>Theme</th><th>Templates</th><th>Avg Conf</th><th>Tier</th></tr>
    </thead>
    <tbody>
      {''.join(rows_html)}
    </tbody>
  </table>""")

    return "\n".join(sections)


# ---------------------------------------------------------------------------
# Gap filtering helper
# ---------------------------------------------------------------------------

def _filter_gaps(conn: sqlite3.Connection, standards: list[dict],
                 regulations: list[dict], min_confidence: float) -> tuple[list[dict], list[dict]]:
    """Keep only entries with coverage below min_confidence threshold."""
    total = _total_docs(conn)

    filtered_std = []
    for s in standards:
        m = compute_standard_metrics(conn, s["standard_code"], min_confidence)
        ratio = m["high_conf_50"] / total if total else 0
        if ratio < min_confidence:
            filtered_std.append(s)

    filtered_reg = []
    for r in regulations:
        m = compute_regulation_metrics(conn, r["regulation_code"])
        if m["guidance_sections"] == 0:
            filtered_reg.append(r)

    return filtered_std, filtered_reg


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Generate Compliance Coverage Report from it_doc_matrix.db"
    )
    parser.add_argument("--standard", metavar="CODE", help="Report for single standard")
    parser.add_argument("--regulation", metavar="CODE", help="Report for single regulation")
    parser.add_argument("--format", dest="fmt", choices=["text", "csv", "json", "html"],
                        default="text")
    parser.add_argument("--output", metavar="PATH", help="Output file (default: stdout/auto)")
    parser.add_argument("--show-gaps", action="store_true",
                        help="Show only standards/regulations with low coverage")
    parser.add_argument("--min-confidence", type=float, default=0.5,
                        metavar="F", help="Coverage threshold (default: 0.5)")
    parser.add_argument("--db", default=str(_DEFAULT_DB), metavar="PATH",
                        help="Path to SQLite database")
    args = parser.parse_args(argv)

    conn = sqlite3.connect(args.db)

    standards = _get_standards(conn, args.standard)
    regulations = _get_regulations(conn, args.regulation)

    if args.show_gaps:
        standards, regulations = _filter_gaps(conn, standards, regulations, args.min_confidence)

    reports_dir = Path(args.db).parent

    if args.fmt == "text":
        text = generate_text_report(conn, standards, regulations, args.min_confidence)
        if args.output:
            Path(args.output).write_text(text, encoding="utf-8")
            print(f"Report written to {args.output}")
        else:
            print(text)

    elif args.fmt == "json":
        data = generate_json_report(conn, standards, regulations, args.min_confidence)
        out_path = args.output or str(reports_dir / "compliance_report.json")
        Path(out_path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        # Also write controls CSV
        ctrl_path = reports_dir / "compliance_report_controls.csv"
        ctrl_buf = io.StringIO()
        ctrl_writer = csv.writer(ctrl_buf)
        ctrl_writer.writerow([
            "standard_code", "control_id", "control_name", "theme",
            "template_count", "avg_confidence", "coverage_tier"
        ])
        for code in _get_standards_with_controls(conn):
            for m in compute_control_metrics(conn, code):
                ctrl_writer.writerow([
                    code, m["control_id"], m["control_name"], m["theme"],
                    m["template_count"], m["avg_confidence"], m["coverage_tier"],
                ])
        ctrl_path.write_text(ctrl_buf.getvalue(), encoding="utf-8")
        print(f"JSON report written to {out_path}")

    elif args.fmt == "csv":
        std_csv, reg_csv = generate_csv_report(conn, standards, regulations, args.min_confidence)
        if args.output:
            base = Path(args.output).stem
            parent = Path(args.output).parent
            std_path = parent / f"{base}_standards.csv"
            reg_path = parent / f"{base}_regulations.csv"
        else:
            std_path = reports_dir / "compliance_report_standards.csv"
            reg_path = reports_dir / "compliance_report_regulations.csv"
        std_path.write_text(std_csv, encoding="utf-8")
        reg_path.write_text(reg_csv, encoding="utf-8")

        # Per-control CSV
        ctrl_path = reports_dir / "compliance_report_controls.csv"
        ctrl_buf = io.StringIO()
        ctrl_writer = csv.writer(ctrl_buf)
        ctrl_writer.writerow([
            "standard_code", "control_id", "control_name", "theme",
            "template_count", "avg_confidence", "coverage_tier"
        ])
        for code in _get_standards_with_controls(conn):
            for m in compute_control_metrics(conn, code):
                ctrl_writer.writerow([
                    code, m["control_id"], m["control_name"], m["theme"],
                    m["template_count"], m["avg_confidence"], m["coverage_tier"],
                ])
        ctrl_path.write_text(ctrl_buf.getvalue(), encoding="utf-8")
        print(f"CSV reports written to:\n  {std_path}\n  {reg_path}\n  {ctrl_path}")

    elif args.fmt == "html":
        html = generate_html_report(conn, standards, regulations, args.min_confidence)
        out_path = args.output or str(reports_dir / "compliance_report.html")
        Path(out_path).write_text(html, encoding="utf-8")
        # Also write controls CSV when generating HTML
        ctrl_path = reports_dir / "compliance_report_controls.csv"
        ctrl_buf = io.StringIO()
        ctrl_writer = csv.writer(ctrl_buf)
        ctrl_writer.writerow([
            "standard_code", "control_id", "control_name", "theme",
            "template_count", "avg_confidence", "coverage_tier"
        ])
        for code in _get_standards_with_controls(conn):
            for m in compute_control_metrics(conn, code):
                ctrl_writer.writerow([
                    code, m["control_id"], m["control_name"], m["theme"],
                    m["template_count"], m["avg_confidence"], m["coverage_tier"],
                ])
        ctrl_path.write_text(ctrl_buf.getvalue(), encoding="utf-8")
        print(f"HTML report written to {out_path}")

    conn.close()


if __name__ == "__main__":
    main()
