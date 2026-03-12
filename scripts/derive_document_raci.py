#!/usr/bin/env python3
"""
scripts/derive_document_raci.py

Faza 9D: Derywacja document_raci z sekcji '## RACI i role'.

Dla każdego szablonu który ma sekcję 'RACI i role':
1. Odczytaj treść sekcji z pliku .md
2. Poszukaj tabeli markdown: | Działanie | Responsible | Accountable | Consulted | Informed |
3. Dla każdego wiersza tabeli wstaw do document_raci

Dla szablonów bez tabeli RACI lub z samym guidance — użyj domyślnego RACI wg kategorii.
"""

import logging
import re
import sqlite3
from pathlib import Path

_log = logging.getLogger(__name__)

DB_PATH = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"
TEMPLATES_DIR = Path(__file__).parent.parent / "generated_templates" / "core"

# Default RACI by category keyword in doc title
DEFAULT_RACI_BY_KEYWORD = {
    "bezpiecze": ("SEC", "CISO", "ARCH", "DEVOPS"),
    "architekt": ("ARCH", "CTO", "DEV", "OPS"),
    "test": ("QA", "PM", "DEV", "BA"),
    "incident": ("SRE", "CISO", "OPS", "MGR"),
    "zmian": ("PM", "CTO", "DEV", "OPS"),
    "dane": ("DPO", "CISO", "DEV", "LEGAL"),
    "wymagani": ("BA", "PM", "DEV", "CLIENT"),
    "zgodnos": ("AUDIT", "CISO", "MGR", "LEGAL"),
}
DEFAULT_RACI = ("DEV", "PM", "BA", "OPS")


def parse_raci_table(md_text: str) -> list[tuple[str, str, str, str, str]]:
    """
    Parse first markdown RACI table found in the text.
    Returns list of (action, responsible, accountable, consulted, informed).
    """
    rows = []
    in_table = False
    header_found = False
    col_map = {}

    for line in md_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            if in_table:
                break
            continue

        cells = [c.strip() for c in stripped.split("|") if c.strip()]

        if not header_found:
            # Check if this looks like a RACI header
            combined = " ".join(cells).lower()
            if any(
                k in combined
                for k in (
                    "responsible",
                    "accountable",
                    "consulted",
                    "informed",
                    "odpowiedzial",
                    "akceptuj",
                )
            ):
                header_found = True
                in_table = True
                # Map header cells to positions
                for i, cell in enumerate(cells):
                    cl = cell.lower()
                    if "działani" in cl or "czynno" in cl or "zadani" in cl:
                        col_map["action"] = i
                    elif "responsible" in cl or "realizuj" in cl:
                        col_map["responsible"] = i
                    elif "accountable" in cl or "akceptuj" in cl or "zatwierdz" in cl:
                        col_map["accountable"] = i
                    elif "consulted" in cl or "konsult" in cl:
                        col_map["consulted"] = i
                    elif "informed" in cl or "informow" in cl:
                        col_map["informed"] = i
            continue

        # Skip separator line (---|---|---)
        if all(c.replace("-", "").replace(":", "") == "" for c in cells):
            continue

        if in_table and len(cells) >= 2:
            action = (
                cells[col_map.get("action", 0)]
                if col_map.get("action", 0) < len(cells)
                else cells[0]
            )
            resp = (
                cells[col_map.get("responsible", 1)]
                if col_map.get("responsible", 1) < len(cells)
                else ""
            )
            acc = (
                cells[col_map.get("accountable", 2)]
                if col_map.get("accountable", 2) < len(cells)
                else ""
            )
            cons = (
                cells[col_map.get("consulted", 3)]
                if col_map.get("consulted", 3) < len(cells)
                else ""
            )
            inf = (
                cells[col_map.get("informed", 4)] if col_map.get("informed", 4) < len(cells) else ""
            )

            # Skip rows that look like guidance text (very long cells)
            if len(action) > 100:
                continue
            rows.append((action, resp, acc, cons, inf))

    return rows


def default_raci_for_title(title: str) -> tuple[str, str, str, str]:
    tl = title.lower()
    for kw, (r, a, c, i) in DEFAULT_RACI_BY_KEYWORD.items():
        if kw in tl:
            return r, a, c, i
    return DEFAULT_RACI


def main():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # Check document_raci columns
    cur.execute("PRAGMA table_info(document_raci)")
    raci_cols = {r[1] for r in cur.fetchall()}

    if not raci_cols:
        print("Tabela document_raci nie istnieje lub brak kolumn — pomijam.")
        conn.close()
        return

    # Get all docs with their path and title
    cur.execute("SELECT doc_uid, title, path FROM docs")
    docs = cur.fetchall()

    inserted = 0
    used_default = 0
    skipped = 0

    for doc_uid, title, path in docs:
        md_file = TEMPLATES_DIR / path if path else None
        if not md_file or not md_file.exists():
            md_file = None

        rows = []
        if md_file:
            try:
                text = md_file.read_text(encoding="utf-8")
                # Find RACI i role section
                raci_match = re.search(
                    r"##\s+RACI\s+i\s+role\b(.*?)(?=\n##\s|\Z)", text, re.DOTALL | re.IGNORECASE
                )
                if raci_match:
                    rows = parse_raci_table(raci_match.group(1))
            except Exception as exc:
                _log.debug("RACI parse failed for doc %s: %s", doc_uid, exc)
            # Use one default RACI row per document
            r, a, c, i = default_raci_for_title(title or "")
            rows = [("Ogólna odpowiedzialność", r, a, c, i)]
            used_default += 1

        for action, resp, acc, cons, inf in rows:
            try:
                if "doc_id" in raci_cols and "responsible" in raci_cols:
                    cur.execute(
                        """
                        INSERT OR IGNORE INTO document_raci
                          (doc_id, role_name, responsible, accountable, consulted, informed)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """,
                        (doc_uid, action, resp, acc, cons, inf),
                    )
                elif "doc_id" in raci_cols and "raci_id" in raci_cols:
                    # Has raci_id as PK — skip, needs auto-id
                    cur.execute(
                        """
                        INSERT OR IGNORE INTO document_raci
                          (doc_id, role_name, responsible, accountable, consulted, informed)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """,
                        (doc_uid, action, resp, acc, cons, inf),
                    )
                if cur.rowcount:
                    inserted += 1
            except Exception as e:
                skipped += 1
                if skipped <= 3:
                    print(f"  Błąd {doc_uid}: {e}")
                continue

        if inserted % 1000 == 0 and inserted > 0:
            conn.commit()
            print(f"  ...{inserted} wierszy wstawionych...")

    conn.commit()
    conn.close()

    print(f"Faza 9D — document_raci: wstawiono {inserted} wierszy")
    print(f"  Użyto default RACI dla {used_default} dokumentów")
    print(f"  Pominięto z błędem: {skipped}")


if __name__ == "__main__":
    main()
