#!/usr/bin/env python3
"""
changelog_generator.py

Generator raportow zmian dla biblioteki szablonow.
Integruje logi Git z tabela template_changelog z bazy SQLite.
Jezeli Git jest niedostepny, pracuje wylacznie z template_changelog.

Uzycie:
    python3 changelog_generator.py --since 2026-03-01 --format markdown
    python3 changelog_generator.py --since 2026-03-01 --format json > changelog.json
    python3 changelog_generator.py --last-n-days 7 --format markdown
    python3 changelog_generator.py --since 2026-01-01 --until 2026-03-31 --format csv
"""

import argparse
import csv
import io
import json
import os
import sqlite3
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict
from typing import Optional, List, Dict, Any

# ---------------------------------------------------------------------------
# Stale
# ---------------------------------------------------------------------------

VERSION = "1.0.0"

PROJECT_ROOT = Path(__file__).parent.parent.parent
DEFAULT_DB = PROJECT_ROOT / "reports" / "it_doc_matrix.db"
DEFAULT_TEMPLATES_DIR = PROJECT_ROOT / "generated_templates" / "core"

STATUS_LABELS = {
    "A": "Dodano",
    "M": "Zmieniono",
    "D": "Usunieto",
    "R": "Przemianowano",
}


# ---------------------------------------------------------------------------
# Narzedzia pomocnicze
# ---------------------------------------------------------------------------

def log_info(msg: str) -> None:
    print(f"[INFO] {msg}", file=sys.stderr)


def log_warn(msg: str) -> None:
    print(f"[WARN] {msg}", file=sys.stderr)


def log_err(msg: str) -> None:
    print(f"[BLAD] {msg}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Funkcje top-level (exportowane do testow)
# ---------------------------------------------------------------------------

def parse_git_log(output: str) -> List[Dict[str, Any]]:
    """
    Parsuje stdout polecenia:
      git log --no-merges --name-status --pretty=format:COMMIT|%H|%cd|%s|%an --date=short

    Zwraca liste slownikow:
      {"hash": str, "date": str, "subject": str, "author": str, "files": [...]}
    Kazdy element "files": {"status": str, "path": str, "old_path": str|None}
    """
    commits: List[Dict[str, Any]] = []
    current: Optional[Dict[str, Any]] = None

    for line in output.splitlines():
        line = line.rstrip()
        if line.startswith("COMMIT|"):
            if current is not None:
                commits.append(current)
            parts = line.split("|", 4)
            current = {
                "hash":    parts[1] if len(parts) > 1 else "",
                "date":    parts[2] if len(parts) > 2 else "",
                "subject": parts[3] if len(parts) > 3 else "",
                "author":  parts[4] if len(parts) > 4 else "",
                "files":   [],
            }
        elif current is not None and line:
            parts = line.split("\t")
            if len(parts) >= 2:
                status_raw = parts[0]
                if status_raw.startswith("R") and len(parts) >= 3:
                    current["files"].append({
                        "status":   "R",
                        "path":     parts[2],
                        "old_path": parts[1],
                    })
                else:
                    status = status_raw[0] if status_raw else "?"
                    current["files"].append({
                        "status":   status,
                        "path":     parts[1],
                        "old_path": None,
                    })

    if current is not None:
        commits.append(current)

    return commits


def group_into_sessions(
    commits: List[Dict[str, Any]],
    gap_minutes: int = 60,
) -> List[List[Dict[str, Any]]]:
    """
    Grupuje commity w sesje robocze.
    Dwa kolejne commity naleza do tej samej sesji jesli roznica dat
    jest <= gap_minutes minut (porownanie na poziomie dnia YYYY-MM-DD).
    """
    if not commits:
        return []

    sessions: List[List[Dict[str, Any]]] = []
    current_session: List[Dict[str, Any]] = [commits[0]]

    for commit in commits[1:]:
        try:
            prev_date = datetime.strptime(current_session[-1]["date"], "%Y-%m-%d")
            curr_date = datetime.strptime(commit["date"], "%Y-%m-%d")
            diff_minutes = abs((prev_date - curr_date).total_seconds() / 60)
        except (ValueError, KeyError):
            diff_minutes = gap_minutes + 1

        if diff_minutes <= gap_minutes:
            current_session.append(commit)
        else:
            sessions.append(current_session)
            current_session = [commit]

    sessions.append(current_session)
    return sessions


def format_date_range(since: Optional[str], until: Optional[str]) -> str:
    """
    Formatuje zakres dat do czytelnego stringa.
    Przyjmuje format YYYY-MM-DD lub None.
    """
    if since and until:
        return f"{since} — {until}"
    elif since:
        return f"od {since}"
    elif until:
        return f"do {until}"
    else:
        return "caly dostepny okres"


def render_markdown(
    sessions: List[List[Dict[str, Any]]],
    changelog_rows: List[Dict[str, Any]],
) -> str:
    """
    Renderuje raport Markdown.
    - sessions: wynik group_into_sessions (commity Git)
    - changelog_rows: rekordy z tabeli template_changelog
    """
    lines: List[str] = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines.append("# Raport Zmian Biblioteki Szablonow\n")
    lines.append(f"**Wygenerowano:** {now}\n")

    # Podsumowanie Git
    total_commits = sum(len(s) for s in sessions)
    total_files = sum(len(c["files"]) for s in sessions for c in s)
    lines.append("## Podsumowanie\n")
    lines.append(f"- Sesje robocze (Git): **{len(sessions)}**")
    lines.append(f"- Commity: **{total_commits}**")
    lines.append(f"- Zmiany plikow (Git): **{total_files}**")
    lines.append(f"- Rekordy template_changelog: **{len(changelog_rows)}**\n")

    # Zmiany z template_changelog
    if changelog_rows:
        lines.append("## Zmiany z template_changelog\n")
        lines.append("| Data | Szablon | Typ | Powod |")
        lines.append("|------|---------|-----|-------|")
        for row in changelog_rows:
            date = (row.get("changed_at") or "")[:10]
            path = row.get("template_path", "")
            ctype = row.get("change_type", "")
            reason = (row.get("change_reason") or "").replace("|", "\\|")
            lines.append(f"| {date} | `{path}` | {ctype} | {reason} |")
        lines.append("")

    # Szczegolowy dziennik Git
    if sessions:
        lines.append("---\n")
        lines.append("## Szczegolowy dziennik zmian (Git)\n")
        for s_idx, session in enumerate(sessions, 1):
            if len(sessions) > 1:
                lines.append(f"### Sesja {s_idx}\n")
            for commit in session:
                lines.append(
                    f"#### {commit['date']} — {commit['subject']} "
                    f"({commit['author']})"
                )
                lines.append(f"*Commit: `{commit['hash'][:8]}`*\n")
                for f in commit["files"]:
                    status = f["status"]
                    label = STATUS_LABELS.get(status, status)
                    if status == "R":
                        lines.append(
                            f"- **Przemianowano**: z `{f['old_path']}` na `{f['path']}`"
                        )
                    else:
                        lines.append(f"- **{label}**: `{f['path']}`")
                lines.append("")

    if not sessions and not changelog_rows:
        lines.append("*Brak zmian w zadanym okresie.*\n")

    return "\n".join(lines)


def render_json(
    sessions: List[List[Dict[str, Any]]],
    changelog_rows: List[Dict[str, Any]],
) -> str:
    """
    Renderuje raport JSON.
    - sessions: wynik group_into_sessions
    - changelog_rows: rekordy z template_changelog
    """
    output = {
        "generated_at": datetime.now().isoformat(),
        "sessions_count": len(sessions),
        "commits_count": sum(len(s) for s in sessions),
        "changelog_rows_count": len(changelog_rows),
        "sessions": sessions,
        "changelog_rows": changelog_rows,
    }
    return json.dumps(output, ensure_ascii=False, indent=2)


def render_csv(
    sessions: List[List[Dict[str, Any]]],
    changelog_rows: List[Dict[str, Any]],
) -> str:
    """Renderuje raport CSV (polaczone dane Git i template_changelog)."""
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["source", "date", "path", "type", "reason", "commit_hash", "author"])

    for session in sessions:
        for commit in session:
            for f in commit["files"]:
                writer.writerow([
                    "git",
                    commit["date"],
                    f["path"],
                    STATUS_LABELS.get(f["status"], f["status"]),
                    commit["subject"],
                    commit["hash"][:8],
                    commit["author"],
                ])

    for row in changelog_rows:
        writer.writerow([
            "template_changelog",
            (row.get("changed_at") or "")[:10],
            row.get("template_path", ""),
            row.get("change_type", ""),
            row.get("change_reason", ""),
            "",
            "",
        ])

    return buf.getvalue()


# ---------------------------------------------------------------------------
# Git — pobieranie commitow
# ---------------------------------------------------------------------------

def _run_git(args: List[str], cwd: Optional[str] = None) -> Optional[str]:
    """
    Wykonuje polecenie git. Zwraca stdout lub None jesli Git niedostepny/blad.
    Nigdy nie rzuca wyjatku — zapewnia graceful degradation.
    """
    try:
        result = subprocess.run(
            ["git"] + args,
            capture_output=True,
            text=True,
            check=True,
            cwd=cwd,
        )
        return result.stdout
    except (subprocess.CalledProcessError, FileNotFoundError, OSError):
        return None


def get_git_commits(
    target_dir: str,
    since: Optional[str] = None,
    until: Optional[str] = None,
    repo_root: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Pobiera commity z Git dla podanego katalogu i zakresu dat.
    Zwraca pusta liste jesli Git jest niedostepny.
    """
    git_args = [
        "log", "--no-merges", "--name-status",
        "--pretty=format:COMMIT|%H|%cd|%s|%an",
        "--date=short",
    ]
    if since:
        git_args.append(f"--since={since}")
    if until:
        git_args.append(f"--until={until}")
    git_args += ["--", target_dir]

    output = _run_git(git_args, cwd=repo_root)
    if output is None:
        log_warn("Git niedostepny lub brak repo — uzywam tylko template_changelog.")
        return []

    return parse_git_log(output.strip())


def _get_repo_root(path: str) -> Optional[str]:
    """Zwraca katalog glowny repo Git lub None."""
    output = _run_git(["rev-parse", "--show-toplevel"], cwd=path)
    return output.strip() if output else None


# ---------------------------------------------------------------------------
# template_changelog — pobieranie
# ---------------------------------------------------------------------------

def fetch_changelog_rows(
    db_path: str,
    since: Optional[str] = None,
    until: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Pobiera rekordy z template_changelog w zadanym zakresie dat.
    Zwraca pusta liste jesli baza niedostepna lub tabela nie istnieje.
    """
    if not os.path.exists(db_path):
        return []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        query = "SELECT * FROM template_changelog WHERE 1=1"
        params: List[str] = []
        if since:
            query += " AND changed_at >= ?"
            params.append(since)
        if until:
            query += " AND changed_at <= ?"
            params.append(until + "T23:59:59")
        query += " ORDER BY changed_at DESC"
        rows = conn.execute(query, params).fetchall()
        result = [dict(row) for row in rows]
        conn.close()
        return result
    except sqlite3.Error as exc:
        log_warn(f"Nie mozna odczytac template_changelog: {exc}")
        return []


# ---------------------------------------------------------------------------
# Glowna logika
# ---------------------------------------------------------------------------

def generate_changelog(
    db_path: str,
    templates_dir: Path,
    since: Optional[str],
    until: Optional[str],
    output_format: str,
) -> str:
    """
    Glowna funkcja generujaca raport.
    Zwraca wygenerowana tresc jako string.
    """
    # Ustal zakres dat
    repo_root = _get_repo_root(str(templates_dir))

    commits = get_git_commits(
        target_dir=str(templates_dir),
        since=since,
        until=until,
        repo_root=repo_root or str(templates_dir),
    )

    sessions = group_into_sessions(commits, gap_minutes=60)

    changelog_rows = fetch_changelog_rows(db_path, since=since, until=until)

    if output_format == "json":
        return render_json(sessions, changelog_rows)
    elif output_format == "csv":
        return render_csv(sessions, changelog_rows)
    else:
        return render_markdown(sessions, changelog_rows)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generator raportow zmian dla biblioteki szablonow.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--db",
        default=str(DEFAULT_DB),
        help="Sciezka do bazy SQLite (zawiera template_changelog)",
    )
    parser.add_argument(
        "--templates-dir",
        default=str(DEFAULT_TEMPLATES_DIR),
        help="Katalog szablonow do analizy Git",
    )
    parser.add_argument(
        "--since",
        metavar="DATE",
        help="Data poczatkowa filtru (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--until",
        metavar="DATE",
        help="Data koncowa filtru (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--last-n-days",
        type=int,
        metavar="N",
        help="Pokaz zmiany z ostatnich N dni (zastepuje --since)",
    )
    parser.add_argument(
        "--format",
        choices=["markdown", "json", "csv"],
        default="markdown",
        help="Format wyjscia",
    )
    parser.add_argument(
        "--out",
        metavar="PLIK",
        help="Plik wyjsciowy (domyslnie: stdout)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    since = args.since
    until = args.until

    if args.last_n_days is not None:
        cutoff = datetime.now() - timedelta(days=args.last_n_days)
        since = cutoff.strftime("%Y-%m-%d")

    date_range = format_date_range(since, until)
    log_info(f"Zakres dat: {date_range}")
    log_info(f"Format: {args.format}")

    content = generate_changelog(
        db_path=args.db,
        templates_dir=Path(args.templates_dir),
        since=since,
        until=until,
        output_format=args.format,
    )

    if args.out:
        Path(args.out).write_text(content, encoding="utf-8")
        log_info(f"Zapisano do: {args.out}")
    else:
        print(content)


if __name__ == "__main__":
    main()
