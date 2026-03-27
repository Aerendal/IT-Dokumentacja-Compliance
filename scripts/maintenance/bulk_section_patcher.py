#!/usr/bin/env python3
"""
scripts/maintenance/bulk_section_patcher.py

Masowa aktualizacja sekcji w szablonach IT Dokumentacja.

Filtruje szablony wg kryteriów i stosuje patch (nowa sekcja, zmieniony tekst,
nowa referencja do standardu). Obsługuje dry-run i loguje do template_changelog.

Użycie:
  # Dry-run — pokaż co by się zmieniło
  python3 scripts/maintenance/bulk_section_patcher.py \\
      --filter-standard ISO/IEC 27001 \\
      --add-section "## Nowa sekcja" --section-content "Treść sekcji..." \\
      --dry-run

  # Faktyczny run — zaktualizuj pliki
  python3 scripts/maintenance/bulk_section_patcher.py \\
      --filter-glob "core/security_*.md" \\
      --replace-in-section "## Wymagania bezpieczeństwa" \\
      --old-text "TODO: wypełnić" --new-text "Patrz ISO/IEC 27001 klauzula 6.1" \\
      --reason "Aktualizacja po ISO 27001:2022"

  # Dodaj referencję do standardu w sekcji Standardy i compliance
  python3 scripts/maintenance/bulk_section_patcher.py \\
      --filter-regulation KSC-PL \\
      --append-to-section "## Standardy i compliance" \\
      --append-text "- KSC-PL: Ustawa o KSC — wymagania cyberbezpieczeństwa" \\
      --reason "Dodano KSC-PL po nowelizacji 2024"
"""

import argparse
import fnmatch
import json
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
DB_PATH = BASE_DIR / "reports" / "it_doc_matrix.db"
TEMPLATES_DIR = BASE_DIR / "generated_templates"


def connect() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def ensure_changelog_table(conn: sqlite3.Connection):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS template_changelog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            template_path TEXT NOT NULL,
            changed_at TEXT NOT NULL,
            change_type TEXT NOT NULL,
            change_reason TEXT,
            diff_summary TEXT,
            patch_args TEXT
        )
    """)
    conn.commit()


def log_change(conn: sqlite3.Connection, path: str, change_type: str,
               reason: str, diff_summary: str, patch_args: str):
    conn.execute("""
        INSERT INTO template_changelog (template_path, changed_at, change_type, change_reason, diff_summary, patch_args)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (path, datetime.now(timezone.utc).isoformat(), change_type, reason, diff_summary, patch_args))


def collect_targets(conn: sqlite3.Connection, args) -> list[str]:
    """Return list of relative doc paths matching the given filters."""
    cur = conn.cursor()

    if args.filter_standard:
        cur.execute("""
            SELECT DISTINCT doc_path FROM doc_standard_mapping
            WHERE standard_code LIKE ?
        """, (f"%{args.filter_standard}%",))
        paths = {r[0] for r in cur.fetchall()}
    elif args.filter_regulation:
        cur.execute("""
            SELECT DISTINCT doc_path FROM doc_regulation_mapping
            WHERE regulation_code LIKE ?
        """, (f"%{args.filter_regulation}%",))
        paths = {r[0] for r in cur.fetchall()}
    elif args.filter_isic:
        # docs table doesn't have isic directly; look at docs that contain isic keyword in path
        cur.execute("SELECT path FROM docs")
        paths = {r[0] for r in cur.fetchall()}
    else:
        cur.execute("SELECT path FROM docs WHERE path IS NOT NULL")
        paths = {r[0] for r in cur.fetchall()}

    # Apply glob filter if given
    if args.filter_glob:
        pattern = args.filter_glob
        paths = {p for p in paths if fnmatch.fnmatch(p, pattern) or fnmatch.fnmatch(Path(p).name, pattern)}

    # Apply title-contains filter
    if args.filter_title:
        cur.execute("SELECT path, title FROM docs WHERE path IS NOT NULL")
        title_map = {r[0]: r[1] for r in cur.fetchall()}
        paths = {p for p in paths if args.filter_title.lower() in (title_map.get(p) or "").lower()}

    return sorted(paths)


def apply_add_section(content: str, heading: str, section_content: str,
                      insert_before: str | None) -> tuple[str, str]:
    """Add a new section if not already present."""
    # Check if section already exists
    heading_clean = heading.lstrip('#').strip()
    if re.search(rf'^{re.escape(heading)}\b', content, re.MULTILINE):
        return content, ""  # already exists

    new_block = f"\n{heading}\n\n{section_content.strip()}\n"

    if insert_before:
        m = re.search(rf'^{re.escape(insert_before)}\b', content, re.MULTILINE)
        if m:
            pos = m.start()
            content = content[:pos] + new_block + "\n" + content[pos:]
            return content, f"Dodano sekcję '{heading}' przed '{insert_before}'"
    # Append at end
    content = content.rstrip() + "\n" + new_block
    return content, f"Dodano sekcję '{heading}' na końcu pliku"


def apply_replace_in_section(content: str, section_heading: str,
                              old_text: str, new_text: str) -> tuple[str, str]:
    """Replace old_text with new_text within a given section."""
    # Find the section bounds
    m_start = re.search(rf'^{re.escape(section_heading)}\b', content, re.MULTILINE)
    if not m_start:
        return content, ""

    section_start = m_start.start()
    # Find next ## heading
    m_end = re.search(r'^#{1,3} ', content[m_start.end():], re.MULTILINE)
    section_end = m_start.end() + m_end.start() if m_end else len(content)

    section_body = content[section_start:section_end]
    if old_text not in section_body:
        return content, ""

    new_body = section_body.replace(old_text, new_text, 1)
    return content[:section_start] + new_body + content[section_end:], \
           f"Zamieniono tekst w sekcji '{section_heading}'"


def apply_append_to_section(content: str, section_heading: str,
                             append_text: str) -> tuple[str, str]:
    """Append text at the end of the named section (before next heading)."""
    m_start = re.search(rf'^{re.escape(section_heading)}\b', content, re.MULTILINE)
    if not m_start:
        return content, ""

    m_end = re.search(r'^#{1,3} ', content[m_start.end():], re.MULTILINE)
    section_end = m_start.end() + m_end.start() if m_end else len(content)

    insert_pos = section_end
    # Back up to last non-blank line in section
    section_body = content[m_start.start():section_end]
    stripped = section_body.rstrip()
    insert_pos = m_start.start() + len(stripped)

    new_content = content[:insert_pos] + "\n" + append_text.strip() + "\n" + content[insert_pos:]
    return new_content, f"Dołączono tekst do sekcji '{section_heading}'"


def list_headings(content: str) -> list[str]:
    """Return all ## headings found in content."""
    return re.findall(r'^#{1,3} .+', content, re.MULTILINE)


def preview_section(content: str, heading: str) -> str:
    """Return the content of a named section, or an error message with available headings."""
    m_start = re.search(rf'^{re.escape(heading)}\b', content, re.MULTILINE)
    if not m_start:
        headings = list_headings(content)
        available = ", ".join(headings) if headings else "(brak naglowkow)"
        return f'Sekcja nie znaleziona. Dostepne sekcje:\n  {available}'

    m_end = re.search(r'^#{1,3} ', content[m_start.end():], re.MULTILINE)
    section_end = m_start.end() + m_end.start() if m_end else len(content)
    return content[m_start.start():section_end].rstrip()


def patch_file(filepath: Path, args) -> tuple[bool, str]:
    """Apply the patch to a single file. Returns (changed, diff_summary)."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        return False, f"Błąd odczytu: {e}"

    original = content
    summary_parts = []

    if args.add_section:
        content, msg = apply_add_section(
            content, args.add_section,
            args.section_content or "",
            args.insert_before
        )
        if msg:
            summary_parts.append(msg)

    if args.replace_in_section and args.old_text and args.new_text:
        content, msg = apply_replace_in_section(
            content, args.replace_in_section, args.old_text, args.new_text
        )
        if msg:
            summary_parts.append(msg)
        elif not re.search(rf'^{re.escape(args.replace_in_section)}\b', content, re.MULTILINE):
            _warn_section_not_found(content, args.replace_in_section, filepath)

    if args.append_to_section and args.append_text:
        content, msg = apply_append_to_section(
            content, args.append_to_section, args.append_text
        )
        if msg:
            summary_parts.append(msg)
        elif not re.search(rf'^{re.escape(args.append_to_section)}\b', content, re.MULTILINE):
            _warn_section_not_found(content, args.append_to_section, filepath)

    if content == original or not summary_parts:
        return False, ""

    filepath.write_text(content, encoding="utf-8")
    return True, "; ".join(summary_parts)


def _warn_section_not_found(content: str, heading: str, filepath: Path):
    """Print a warning to stderr when a section is not found in the file."""
    headings = list_headings(content)
    available = ", ".join(headings) if headings else "(brak naglowkow)"
    print(
        f'OSTRZEZENIE: Sekcja "{heading}" nie znaleziona w {filepath}\n'
        f'  Dostepne sekcje: {available}',
        file=sys.stderr,
    )


def _try_connect_db():
    """Connect to DB if available, return None otherwise."""
    try:
        if not DB_PATH.exists():
            return None
        return connect()
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Masowa aktualizacja sekcji w szablonach IT Dokumentacja"
    )

    # Single-file target
    parser.add_argument("--file", metavar="PATH",
                        help="Przetwórz pojedynczy plik zamiast kolekcji z DB")

    # Filters
    filt = parser.add_argument_group("Filtry szablonów")
    filt.add_argument("--filter-standard", metavar="CODE",
                      help="Filtruj po kodzie standardu (np. 'ISO/IEC 27001')")
    filt.add_argument("--filter-regulation", metavar="CODE",
                      help="Filtruj po kodzie regulacji (np. 'KSC-PL')")
    filt.add_argument("--filter-glob", metavar="PATTERN",
                      help="Filtruj po wzorcu ścieżki (np. 'core/security_*.md')")
    filt.add_argument("--filter-title", metavar="TEXT",
                      help="Filtruj po fragmencie tytułu dokumentu")
    filt.add_argument("--filter-isic", metavar="CODE",
                      help="Filtruj po kodzie ISIC (wymaga kolumny isic w tabeli docs; obecnie filtruje po path)")

    # Patch operations (mutually exclusive with --preview-section)
    ops = parser.add_argument_group("Operacje patch")
    ops.add_argument("--add-section", metavar="HEADING",
                     help="Dodaj nową sekcję (np. '## Nowa sekcja')")
    ops.add_argument("--section-content", metavar="TEXT",
                     help="Treść nowej sekcji (używaj z --add-section)")
    ops.add_argument("--insert-before", metavar="HEADING",
                     help="Wstaw przed tym nagłówkiem (opcjonalne)")
    ops.add_argument("--replace-in-section", metavar="HEADING",
                     help="Zamień tekst w tej sekcji (wymaga --old-text i --new-text)")
    ops.add_argument("--old-text", metavar="TEXT", help="Tekst do zamiany")
    ops.add_argument("--new-text", metavar="TEXT", help="Nowy tekst")
    ops.add_argument("--append-to-section", metavar="HEADING",
                     help="Dołącz tekst na końcu tej sekcji (wymaga --append-text)")
    ops.add_argument("--append-text", metavar="TEXT", help="Tekst do dołączenia")

    # Preview mode
    ops.add_argument("--preview-section", metavar="HEADING",
                     help="Pokaż zawartość sekcji bez modyfikacji (wyklucza operacje patch)")

    # Run options
    parser.add_argument("--reason", metavar="TEXT", default="",
                        help="Powód zmiany (zapisywany w template_changelog)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Pokaż co by się zmieniło bez faktycznej modyfikacji")
    parser.add_argument("--limit", type=int, default=0,
                        help="Ogranicz do N plików (do testowania)")
    parser.add_argument("--confirm", action="store_true",
                        help="Zapytaj o potwierdzenie przed masową operacją (bez --file)")

    args = parser.parse_args()

    # --preview-section is mutually exclusive with patch operations
    if args.preview_section and any([args.add_section, args.replace_in_section, args.append_to_section]):
        parser.error("--preview-section nie może być użyty razem z operacjami patch")

    # Validate: at least one operation or preview
    if not args.preview_section and not any([args.add_section, args.replace_in_section, args.append_to_section]):
        parser.error("Podaj co najmniej jedną operację: --add-section, --replace-in-section, --append-to-section lub --preview-section")

    # ------------------------------------------------------------------ #
    # --file mode: operate on a single file directly                       #
    # ------------------------------------------------------------------ #
    if args.file:
        filepath = Path(args.file)
        if not filepath.exists():
            print(f"Blad: plik nie istnieje: {filepath}", file=sys.stderr)
            return 1

        if args.preview_section:
            try:
                content = filepath.read_text(encoding="utf-8")
            except Exception as e:
                print(f"Blad odczytu: {e}", file=sys.stderr)
                return 1
            print(preview_section(content, args.preview_section))
            return 0

        if args.dry_run:
            print(f"[DRY-RUN] Plik: {filepath}")
            try:
                content = filepath.read_text(encoding="utf-8")
            except Exception as e:
                print(f"Blad odczytu: {e}", file=sys.stderr)
                return 1
            original = content
            if args.add_section:
                content, _ = apply_add_section(content, args.add_section,
                                               args.section_content or "", args.insert_before)
            if args.replace_in_section and args.old_text:
                content, _ = apply_replace_in_section(content, args.replace_in_section,
                                                       args.old_text, args.new_text or "")
            if args.append_to_section and args.append_text:
                content, _ = apply_append_to_section(content, args.append_to_section,
                                                      args.append_text)
            if content != original:
                print(f"  [ZMIANA] {filepath}")
            else:
                print(f"  [BEZ ZMIAN] {filepath}")
            return 0

        ok, summary = patch_file(filepath, args)
        if ok:
            print(f"Zmieniono: {filepath}")
            conn = _try_connect_db()
            if conn is not None:
                try:
                    ensure_changelog_table(conn)
                    patch_args_json = json.dumps(vars(args), ensure_ascii=False)
                    log_change(conn, str(filepath), "bulk_patch", args.reason, summary, patch_args_json)
                    conn.commit()
                finally:
                    conn.close()
        else:
            print(f"Bez zmian: {filepath}")
        return 0

    # ------------------------------------------------------------------ #
    # Bulk mode: collect targets from DB                                   #
    # ------------------------------------------------------------------ #
    conn = connect()
    ensure_changelog_table(conn)

    # --preview-section in bulk mode: show from first matched file
    if args.preview_section:
        targets = collect_targets(conn, args)
        conn.close()
        if not targets:
            print("Brak szablonów spełniających kryteria filtrów.")
            return 1
        filepath = TEMPLATES_DIR / targets[0]
        if not filepath.exists():
            print(f"Blad: plik nie istnieje: {filepath}", file=sys.stderr)
            return 1
        try:
            content = filepath.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Blad odczytu: {e}", file=sys.stderr)
            return 1
        print(f"Plik: {filepath}")
        print(preview_section(content, args.preview_section))
        return 0

    targets = collect_targets(conn, args)
    if not targets:
        print("Brak szablonów spełniających kryteria filtrów.")
        conn.close()
        return 1

    if args.limit:
        targets = targets[:args.limit]

    # --confirm: ask user before applying bulk changes
    if args.confirm and not args.dry_run:
        print(f"Znaleziono {len(targets)} plikow. Zastosowac zmiany? [y/N]: ", end="", flush=True)
        answer = input()
        if answer.strip().lower() != "y":
            print("Anulowano.")
            conn.close()
            return 0

    print(f"Znaleziono {len(targets)} szablonów do sprawdzenia.")
    if args.dry_run:
        print("[DRY-RUN] Żadne pliki nie będą modyfikowane.\n")

    changed = 0
    unchanged = 0
    errors = 0
    patch_args_json = json.dumps(vars(args), ensure_ascii=False)

    for rel_path in targets:
        filepath = TEMPLATES_DIR / rel_path
        if not filepath.exists():
            errors += 1
            continue

        if args.dry_run:
            # Simulate without writing
            try:
                content = filepath.read_text(encoding="utf-8")
            except Exception:
                errors += 1
                continue
            original = content
            if args.add_section:
                content, msg = apply_add_section(content, args.add_section,
                                                  args.section_content or "", args.insert_before)
            if args.replace_in_section and args.old_text:
                content, msg = apply_replace_in_section(content, args.replace_in_section,
                                                         args.old_text, args.new_text or "")
            if args.append_to_section and args.append_text:
                content, msg = apply_append_to_section(content, args.append_to_section,
                                                        args.append_text)
            if content != original:
                changed += 1
                print(f"  [ZMIANA] {rel_path}")
            else:
                unchanged += 1
        else:
            ok, summary = patch_file(filepath, args)
            if ok:
                changed += 1
                log_change(conn, rel_path, "bulk_patch", args.reason, summary, patch_args_json)
                if changed % 500 == 0:
                    conn.commit()
                    print(f"  {changed} zmienionych...")
            else:
                unchanged += 1

    if not args.dry_run:
        conn.commit()
    conn.close()

    print(f"\nPodsumowanie:")
    print(f"  Zmienione: {changed}")
    print(f"  Bez zmian: {unchanged}")
    print(f"  Błędy:     {errors}")
    if not args.dry_run and changed:
        print(f"\nZalogowano {changed} zmian do template_changelog.")
        print("Uruchom reindex_sections.py + resolve_content_links_extended.py po zakończeniu.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
