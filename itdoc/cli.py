"""itdoc.cli — minimalistyczny interfejs CLI/TUI.

Zasada: workspace powitalny jest pusty (zero szumu).
Zlozonosc w CLI, nie w UI.

Uzycie:
    python -m itdoc                         # minimalne info (bez bannerow)
    python -m itdoc find --standard CODE    # znajdz szablony po standardzie
    python -m itdoc find --regulation CODE  # znajdz szablony po regulacji
    python -m itdoc contract UID            # pokaz kontrakt dokumentu
    python -m itdoc validate PATH           # waliduj plik .md
    python -m itdoc db-check                # sprawdz integralnosc DB
    python -m itdoc rhythm UID [--depth N]  # pokaz upstream/downstream
"""

import argparse
import json
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Optional

from itdoc.db import get_connection, validate_schema
from itdoc.exceptions import ItDocError, QueryError, TemplateError
from itdoc.query import (
    find_by_regulation,
    find_by_standard,
    get_contract,
    rhythm_downstream,
    rhythm_upstream,
)
from itdoc.template import load_template, validate_template


@contextmanager
def _db(db_path: Optional[str] = None):
    """Context manager — otwiera polaczenie lub rzuca ItDocError gdy DB brak."""
    try:
        with get_connection(Path(db_path) if db_path else None) as conn:
            yield conn
    except FileNotFoundError as e:
        raise ItDocError(str(e)) from e


def cmd_find(args) -> int:
    """Find templates by standard code (--standard) or regulation code (--regulation)."""
    try:
        with _db(args.db) as conn:
            if args.standard:
                results = find_by_standard(conn, args.standard)
                label = f"standard={args.standard!r}"
            else:
                results = find_by_regulation(conn, args.regulation)
                label = f"regulation={args.regulation!r}"
    except QueryError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    if not results:
        print(f"(brak wynikow dla {label})")
        return 0

    limit = args.limit
    shown = results[:limit]
    for r in shown:
        path = r.get("doc_path") or "(brak sciezki)"
        title = r.get("title") or ""
        code = r.get("standard_code") or r.get("regulation_code") or ""
        print(f"{path}  [{code}]  {title}")

    if len(results) > limit:
        print(f"... i {len(results) - limit} wiecej (uzyj --limit N)")
    return 0


def cmd_contract(args) -> int:
    """Print the interface contract (inputs/outputs/gates) for a document by UID."""
    try:
        with _db(args.db) as conn:
            result = get_contract(conn, args.uid)
    except QueryError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"doc:     {result.get('scope_uid')}")
        print(f"version: {result.get('version')}")
        for key in ("inputs", "outputs", "gates", "impact"):
            val = result.get(key, [])
            if val:
                print(f"{key}:")
                if isinstance(val, list):
                    for item in val:
                        print(f"  - {item}")
                else:
                    print(f"  {val}")
    return 0


def cmd_validate(args) -> int:
    """Validate a template .md file against required schema (frontmatter + sections)."""
    path = Path(args.path)
    try:
        tmpl = load_template(path)
        errors = validate_template(tmpl)
    except TemplateError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    if errors:
        for err in errors:
            print(f"FAIL  {err}")
        return 1
    else:
        print(f"OK    {path.name}")
        return 0


def cmd_db_check(args) -> int:
    """Check database schema integrity — verify required tables and columns exist."""
    with _db(args.db) as conn:
        errors = validate_schema(conn)

    if errors:
        for err in errors:
            print(f"FAIL  {err}")
        return 1
    print("OK    schema valid")
    return 0


def cmd_rhythm(args) -> int:
    """Show information flow graph (upstream/downstream) for a document by UID."""
    try:
        with _db(args.db) as conn:
            up = rhythm_upstream(conn, args.uid, depth=args.depth)
            down = rhythm_downstream(conn, args.uid, depth=args.depth)
    except QueryError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    if not up and not down:
        print(f"(brak krawedzi rytmu dla {args.uid!r})")
        return 0

    if up:
        print("upstream (co musi powstac przed):")
        for e in up:
            print(f"  d={e['distance']}  {e['from_uid']} --[{e['edge_type']}]--> {e['to_uid']}")
    if down:
        print("downstream (co powstaje po):")
        for e in down:
            print(f"  d={e['distance']}  {e['from_uid']} --[{e['edge_type']}]--> {e['to_uid']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build and return the argument parser for the itdoc CLI."""
    p = argparse.ArgumentParser(
        prog="itdoc",
        description="IT Dokumentacja CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Wiecej: python -m itdoc <polecenie> --help",
    )
    p.add_argument(
        "--db", metavar="PATH", help="Sciezka do pliku .db (domyslnie: reports/it_doc_matrix.db)"
    )
    sub = p.add_subparsers(dest="command", metavar="polecenie")

    pf = sub.add_parser("find", help="Znajdz szablony po standardzie lub regulacji")
    grp = pf.add_mutually_exclusive_group(required=True)
    grp.add_argument("--standard", metavar="KOD", help="Kod standardu (np. 'ISO/IEC 27001')")
    grp.add_argument("--regulation", metavar="KOD", help="Kod regulacji (np. 'UODO-PL')")
    pf.add_argument(
        "--limit", type=int, default=20, metavar="N", help="Maks. wynikow (domyslnie: 20)"
    )

    pc = sub.add_parser("contract", help="Pokaz kontrakt dokumentu")
    pc.add_argument("uid", help="ULID dokumentu")
    pc.add_argument("--json", action="store_true", help="Wyjscie w formacie JSON")

    pv = sub.add_parser("validate", help="Waliduj plik szablonu .md")
    pv.add_argument("path", help="Sciezka do pliku .md")

    sub.add_parser("db-check", help="Sprawdz integralnosc schematu DB")

    pr = sub.add_parser("rhythm", help="Pokaz przeplyw informacji (upstream/downstream)")
    pr.add_argument("uid", help="ULID dokumentu")
    pr.add_argument(
        "--depth", type=int, default=2, metavar="N", help="Glebokosc przeszukiwania (domyslnie: 2)"
    )

    return p


def main(argv=None) -> int:
    """Entry point for the itdoc CLI. Returns exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_usage()
        return 0

    dispatch = {
        "find": cmd_find,
        "contract": cmd_contract,
        "validate": cmd_validate,
        "db-check": cmd_db_check,
        "rhythm": cmd_rhythm,
    }
    try:
        return dispatch[args.command](args)
    except ItDocError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
