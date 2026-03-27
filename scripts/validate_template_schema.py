#!/usr/bin/env python3
"""validate_template_schema.py — validate YAML frontmatter and required sections in .md templates."""

import argparse
import re
import sqlite3
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "## Cel dokumentu",
    "## Zakres i granice",
    "## Wejścia i wyjścia",
]

VIOLATION_SEVERITY = {
    "FRONTMATTER_MISSING": "ERROR",
    "FRONTMATTER_NO_TITLE": "WARNING",
    "SECTION_MISSING": "ERROR",
    "EMPTY_SECTION": "WARNING",
}

DEFAULT_TEMPLATES_DIR = "generated_templates/core"
DEFAULT_DB_PATH = "reports/it_doc_matrix.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS template_violations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    template_path TEXT NOT NULL,
    violation_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    source_dir TEXT,
    found_at TEXT DEFAULT (datetime('now'))
)
"""

MIGRATE_ADD_SOURCE_DIR_SQL = """
ALTER TABLE template_violations ADD COLUMN source_dir TEXT
"""


def parse_frontmatter(content: str) -> tuple[bool, bool]:
    """Return (has_frontmatter, has_title)."""
    if not content.startswith("---"):
        return False, False
    end = content.find("\n---", 3)
    if end == -1:
        return False, False
    fm_block = content[3:end]
    has_title = bool(re.search(r"^\s*title\s*:", fm_block, re.MULTILINE))
    return True, has_title


def check_sections(content: str) -> list[tuple[str, str]]:
    """Return list of (violation_type, section_heading) tuples."""
    violations = []
    # Strip frontmatter before section checks
    body = content
    if content.startswith("---"):
        end = content.find("\n---", 3)
        if end != -1:
            body = content[end + 4:]

    for section in REQUIRED_SECTIONS:
        pattern = re.compile(r"^" + re.escape(section) + r"\s*$", re.MULTILINE)
        match = pattern.search(body)
        if not match:
            violations.append(("SECTION_MISSING", section))
        else:
            # Find content between this heading and the next ## heading
            after = body[match.end():]
            next_heading = re.search(r"^##", after, re.MULTILINE)
            if next_heading:
                content_block = after[: next_heading.start()]
            else:
                content_block = after
            if not content_block.strip():
                violations.append(("EMPTY_SECTION", section))
    return violations


def validate_file(path: Path) -> list[dict]:
    """Validate a single file and return list of violation dicts."""
    violations = []
    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        violations.append(
            {
                "template_path": str(path),
                "violation_type": "FRONTMATTER_MISSING",
                "severity": "ERROR",
                "detail": f"Cannot read file: {exc}",
            }
        )
        return violations

    has_fm, has_title = parse_frontmatter(content)

    if not has_fm:
        violations.append(
            {
                "template_path": str(path),
                "violation_type": "FRONTMATTER_MISSING",
                "severity": VIOLATION_SEVERITY["FRONTMATTER_MISSING"],
                "detail": "File does not start with YAML frontmatter (---)",
            }
        )
    elif not has_title:
        violations.append(
            {
                "template_path": str(path),
                "violation_type": "FRONTMATTER_NO_TITLE",
                "severity": VIOLATION_SEVERITY["FRONTMATTER_NO_TITLE"],
                "detail": "Frontmatter exists but 'title:' field is missing",
            }
        )

    for vtype, section in check_sections(content):
        violations.append(
            {
                "template_path": str(path),
                "violation_type": vtype,
                "severity": VIOLATION_SEVERITY[vtype],
                "detail": f"Section: {section}",
            }
        )

    return violations


def scan_directory(templates_dir: Path) -> tuple[int, list[dict]]:
    """Scan all .md files in templates_dir. Return (total_files, all_violations)."""
    md_files = sorted(templates_dir.glob("*.md"))
    all_violations: list[dict] = []
    for md_file in md_files:
        all_violations.extend(validate_file(md_file))
    return len(md_files), all_violations


def write_to_db(db_path: Path, violations: list[dict], source_dir: str) -> None:
    conn = sqlite3.connect(db_path)
    try:
        conn.execute(CREATE_TABLE_SQL)
        # Migrate: add source_dir column if missing (safe to ignore if already exists)
        try:
            conn.execute(MIGRATE_ADD_SOURCE_DIR_SQL)
            conn.commit()
        except sqlite3.OperationalError:
            pass  # column already exists
        # Scoped delete — only remove rows for this source_dir
        conn.execute("DELETE FROM template_violations WHERE source_dir = ?", (source_dir,))
        conn.executemany(
            "INSERT INTO template_violations (template_path, violation_type, severity, source_dir)"
            " VALUES (?, ?, ?, ?)",
            [(v["template_path"], v["violation_type"], v["severity"], source_dir) for v in violations],
        )
        conn.commit()
    finally:
        conn.close()


def print_report(total_files: int, violations: list[dict]) -> None:
    files_with_violations = len({v["template_path"] for v in violations})

    errors = [v for v in violations if v["severity"] == "ERROR"]
    warnings = [v for v in violations if v["severity"] == "WARNING"]

    def count_by_type(vlist: list[dict]) -> dict[str, int]:
        counts: dict[str, int] = {}
        for v in vlist:
            counts[v["violation_type"]] = counts.get(v["violation_type"], 0) + 1
        return counts

    error_counts = count_by_type(errors)
    warning_counts = count_by_type(warnings)

    print("Schema Validation Report")
    print("========================")
    print(f"Templates scanned: {total_files}")
    print(f"Templates with violations: {files_with_violations}")
    print()

    print("ERROR violations:")
    error_types = ["FRONTMATTER_MISSING", "SECTION_MISSING"]
    for vtype in error_types:
        count = error_counts.get(vtype, 0)
        print(f"  {vtype}: {count} files")

    print()
    print("WARNING violations:")
    warning_types = ["EMPTY_SECTION", "FRONTMATTER_NO_TITLE"]
    for vtype in warning_types:
        count = warning_counts.get(vtype, 0)
        print(f"  {vtype}: {count} files")

    print()
    print("Run with --file PATH to see details for a specific file.")


def print_file_violations(path: Path, violations: list[dict]) -> None:
    if not violations:
        print(f"OK: {path} — no violations found.")
        return
    print(f"Violations in {path}:")
    for v in violations:
        print(f"  [{v['severity']}] {v['violation_type']}: {v.get('detail', '')}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate .md template schema (frontmatter + required sections)."
    )
    parser.add_argument("--report", action="store_true", help="Print violations report (default behavior)")
    parser.add_argument("--file", metavar="PATH", help="Validate a single file only (no DB write)")
    parser.add_argument("--strict", action="store_true", help="Exit 1 if any ERROR violations found")
    parser.add_argument(
        "--dir",
        metavar="PATH",
        default=DEFAULT_TEMPLATES_DIR,
        help=f"Templates directory (default: {DEFAULT_TEMPLATES_DIR})",
    )
    parser.add_argument(
        "--db",
        metavar="PATH",
        default=DEFAULT_DB_PATH,
        help=f"SQLite DB path (default: {DEFAULT_DB_PATH})",
    )
    args = parser.parse_args()

    if args.file:
        target = Path(args.file)
        violations = validate_file(target)
        print_file_violations(target, violations)
        if args.strict and any(v["severity"] == "ERROR" for v in violations):
            return 1
        return 0

    templates_dir = Path(args.dir)
    if not templates_dir.exists():
        print(f"ERROR: Templates directory not found: {templates_dir}", file=sys.stderr)
        return 1

    total_files, all_violations = scan_directory(templates_dir)

    db_path = Path(args.db)
    if db_path.exists():
        write_to_db(db_path, all_violations, str(templates_dir))
    else:
        print(f"WARNING: DB not found at {db_path}, skipping DB write.", file=sys.stderr)

    print_report(total_files, all_violations)

    if args.strict and any(v["severity"] == "ERROR" for v in all_violations):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
