#!/usr/bin/env python3
"""
scripts/derive_document_dependencies.py

Faza 9E: Derywacja document_dependencies z content_links_resolved.

Używa content_links_resolved (where to_kind='document') jako podstawy.
Mapuje link_type → dep_type:
  required=1 → 'requires'
  else        → 'relates_to'

Grupuje po (from_uid, to_uid) żeby uniknąć duplikatów.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"


def main():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # Check document_dependencies columns
    cur.execute("PRAGMA table_info(document_dependencies)")
    dep_cols = {r[1] for r in cur.fetchall()}
    if not dep_cols:
        print("Tabela document_dependencies nie istnieje — pomijam.")
        conn.close()
        return

    # Check content_links_resolved columns
    cur.execute("PRAGMA table_info(content_links_resolved)")
    {r[1] for r in cur.fetchall()}

    # Build the SELECT from content_links (uses to_type, from_ref, to_ref)
    # from_ref / to_ref format: "document::Title"
    cur.execute("""
        SELECT from_ref, to_ref, link_type, required, context_doc_uid
        FROM content_links
        WHERE to_type = 'document'
          AND from_ref LIKE 'document::%'
          AND to_ref   LIKE 'document::%'
    """)
    raw_links = cur.fetchall()
    print(f"  Znaleziono {len(raw_links)} linków doc-doc w content_links")

    # Build title → doc_uid lookup (lower-stripped)
    cur.execute("SELECT doc_uid, title FROM docs")
    title_map = {}
    for uid, title in cur.fetchall():
        if title:
            title_map[title.lower().strip()] = uid

    def ref_to_uid(ref: str) -> str | None:
        # "document::Title" → match title
        if "::" in ref:
            title = ref.split("::", 1)[1].strip()
            return title_map.get(title.lower().strip())
        return None

    # Deduplicate (from_uid, to_uid) → strongest dep_type
    seen: dict[tuple, str] = {}
    for from_ref, to_ref, _link_type, required, ctx_uid in raw_links:
        from_uid = ref_to_uid(from_ref) or ctx_uid
        to_uid = ref_to_uid(to_ref)
        if not from_uid or not to_uid or from_uid == to_uid:
            continue
        dep_type = "requires" if required else "relates_to"
        key = (from_uid, to_uid)
        # requires > relates_to
        if key not in seen or dep_type == "requires":
            seen[key] = dep_type

    rows = [(f, t, dt) for (f, t), dt in seen.items()]
    print(f"  Po deduplikacji: {len(rows)} unikalnych par")

    inserted = 0
    skipped = 0

    for from_uid, to_uid, dep_type in rows:
        try:
            # Try to match actual column names
            if "source_doc_id" in dep_cols and "target_doc_id" in dep_cols:
                cur.execute(
                    """
                    INSERT OR IGNORE INTO document_dependencies
                      (source_doc_id, target_doc_id, dep_type)
                    VALUES (?, ?, ?)
                """,
                    (from_uid, to_uid, dep_type),
                )
            elif "doc_id" in dep_cols and "depends_on_doc_id" in dep_cols:
                cur.execute(
                    """
                    INSERT OR IGNORE INTO document_dependencies
                      (doc_id, depends_on_doc_id, dep_type)
                    VALUES (?, ?, ?)
                """,
                    (from_uid, to_uid, dep_type),
                )
            elif "doc_id" in dep_cols and "related_doc_id" in dep_cols:
                cur.execute(
                    """
                    INSERT OR IGNORE INTO document_dependencies
                      (doc_id, related_doc_id, relationship_type)
                    VALUES (?, ?, ?)
                """,
                    (from_uid, to_uid, dep_type),
                )
            else:
                # Fallback: use positional insert with first 3 text columns
                print(f"  Nieznany schemat document_dependencies: {dep_cols}")
                break

            if cur.rowcount:
                inserted += 1
        except Exception as e:
            skipped += 1
            if skipped <= 3:
                print(f"  Błąd: {e}")
            continue

        if inserted % 5000 == 0 and inserted > 0:
            conn.commit()
            print(f"  ...{inserted} wierszy wstawionych...")

    conn.commit()
    conn.close()

    print(f"Faza 9E — document_dependencies: wstawiono {inserted} wierszy")
    if skipped:
        print(f"  Pominięto z błędem: {skipped}")


if __name__ == "__main__":
    main()
