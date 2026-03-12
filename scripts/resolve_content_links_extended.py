#!/usr/bin/env python3
"""
resolve_content_links_extended.py

Rozszerzenie istniejacego resolve_content_links.py o obsluge formatu:
    document::TITLE::section::SECTION_NAME

Podejscie:
  1. Buduje indeks: title_norm -> doc_uid z tabeli docs
  2. Dla kazdego linku doc_title_section: normalizuje tytul i nazwe sekcji
     do anchor (slug), szuka section_uid w tabeli sections
  3. Wstawia znalezione pary do content_links_resolved (INSERT OR IGNORE)
  4. Naprawia takze wildcard-owe linki (document::* i subsection::*) przez skip

Nie nadpisuje istniejacych resolved wpisow.
"""
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path(__file__).parent.parent / 'reports' / 'it_doc_matrix.db'
DOC_TITLE_SECTION_RE = re.compile(r'^document::(.+?)::section::(.+)$', re.IGNORECASE)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def to_anchor(s: str) -> str:
    """Normalizuje nazwe sekcji do anchor-slug zgodnie z logika DB.
    Usuwa znaki non-ASCII (polskie znaki diakrytyczne), zamienia spacje na '-'."""
    s = s.lower().strip()
    # Usun wszystkie znaki non-ASCII (tak jak robi to generator anchorow w DB)
    s = s.encode('ascii', 'ignore').decode('ascii')
    # Usun znaki specjalne oprocz alfanumerycznych, spacji i myslnikow
    s = re.sub(r'[^a-z0-9\s\-]', '', s)
    # Spacje -> myslnik, kolaps wielokrotnych myslnikow
    s = re.sub(r'\s+', '-', s.strip())
    s = re.sub(r'-+', '-', s)
    return s


def norm_title(s: str) -> str:
    """Normalizuje tytul dokumentu do porownania (lowercase, strip)."""
    return s.lower().strip() if s else ''


def build_doc_title_index(cur) -> dict[str, str]:
    """Zwraca slownik: title_norm -> doc_uid."""
    cur.execute("SELECT doc_uid, title FROM docs WHERE title IS NOT NULL")
    index = {}
    for doc_uid, title in cur.fetchall():
        key = norm_title(title)
        if key not in index:
            index[key] = doc_uid
    return index


def build_section_anchor_index(cur) -> dict[tuple[str, str], str]:
    """Zwraca slownik: (doc_uid, anchor) -> section_uid."""
    cur.execute("SELECT section_uid, doc_uid, anchor FROM sections WHERE anchor IS NOT NULL")
    return {(du, anchor): su for su, du, anchor in cur.fetchall()}


def strength_from_required(required) -> str:
    return "required" if required == 1 else "navigational"


def main():
    dry_run = '--dry-run' in sys.argv

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    print("Budowanie indeksow...")
    doc_index = build_doc_title_index(cur)
    section_index = build_section_anchor_index(cur)
    print(f"  doc_index: {len(doc_index)} tytulów")
    print(f"  section_index: {len(section_index)} sekcji")

    # Pobierz tylko nierozwiazane linki formatu doc_title_section
    cur.execute("""
        SELECT id, from_type, from_ref, to_type, to_ref,
               link_type, direction, rationale, required, context_doc_uid
        FROM content_links
        WHERE id NOT IN (SELECT content_link_id FROM content_links_resolved)
          AND (
            from_ref LIKE 'document::%::section::%'
            OR to_ref LIKE 'document::%::section::%'
          )
    """)
    rows = cur.fetchall()
    print(f"\nLinków do rozwiązania (doc_title format): {len(rows)}")

    resolved = 0
    missing_doc = 0
    missing_section = 0
    ambiguous = 0

    def resolve_doc_title_ref(ref: str):
        """Zwraca (section_uid, method, confidence) lub None."""
        m = DOC_TITLE_SECTION_RE.match(ref)
        if not m:
            return None

        doc_title_raw = m.group(1).strip()
        section_name_raw = m.group(2).strip()

        doc_uid = doc_index.get(norm_title(doc_title_raw))
        if not doc_uid:
            return None, 'missing_doc', 0.0

        anchor = to_anchor(section_name_raw)
        section_uid = section_index.get((doc_uid, anchor))

        if section_uid:
            return section_uid, 'context_doc', 0.85
        else:
            return None, 'missing_section', 0.0

    inserts = []
    for (cid, from_type, from_ref, to_type, to_ref,
         link_type, direction, rationale, required, context_doc_uid) in rows:

        strength = strength_from_required(required)

        # Resolve from_ref
        if from_type == 'section' and from_ref and '::section::' in from_ref:
            fr_result = resolve_doc_title_ref(from_ref)
        else:
            fr_result = (None, 'skip', 0.0)

        # Resolve to_ref
        if to_type == 'section' and to_ref and '::section::' in to_ref:
            tr_result = resolve_doc_title_ref(to_ref)
        else:
            tr_result = (None, 'skip', 0.0)

        from_uid, from_method, from_conf = (fr_result if fr_result else (None, 'skip', 0.0))
        to_uid, to_method, to_conf = (tr_result if tr_result else (None, 'skip', 0.0))

        if from_uid and to_uid:
            method = from_method if from_method == to_method else 'mixed'
            # Upewnij sie ze method jest na liscie dozwolonych wartosci CHECK
            allowed = {'explicit','global_unique','manual','ambiguous','missing','mixed','context_doc'}
            if method not in allowed:
                method = 'mixed'
            conf = min(from_conf, to_conf)
            inserts.append((
                cid,
                'section', from_uid,
                'section', to_uid,
                link_type, direction, rationale, strength,
                method, conf,
                context_doc_uid
            ))
            resolved += 1
        else:
            if from_method == 'missing_doc' or to_method == 'missing_doc':
                missing_doc += 1
            elif from_method == 'missing_section' or to_method == 'missing_section':
                missing_section += 1

    print(f"\nWyniki:")
    print(f"  Rozwiązano:       {resolved}")
    print(f"  Brak dokumentu:   {missing_doc}")
    print(f"  Brak sekcji:      {missing_section}")
    print(f"  Razem niewynik.:  {missing_doc + missing_section}")

    if not dry_run and inserts:
        print(f"\nWstawianie {len(inserts)} rekordow do content_links_resolved...")
        cur.executemany("""
            INSERT OR IGNORE INTO content_links_resolved
            (content_link_id, from_kind, from_uid, to_kind, to_uid,
             link_type, direction, rationale, strength,
             resolution_method, resolution_confidence, notes)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        """, inserts)
        conn.commit()

        # Stan po resolucji
        cur.execute("SELECT COUNT(DISTINCT content_link_id) FROM content_links_resolved")
        total_resolved = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM content_links")
        total_links = cur.fetchone()[0]
        print(f"  content_links_resolved razem: {total_resolved} / {total_links}")

        # Zapisz do sync_runs
        try:
            from ulid import ulid
            cur.execute(
                "INSERT INTO sync_runs(sync_id,ran_at_utc,kind,status,notes) VALUES(?,?,?,?,?)",
                (ulid(), utc_now(), 'content_links_extended',
                 'OK', f"resolved={resolved}, missing_doc={missing_doc}, missing_section={missing_section}")
            )
            conn.commit()
        except Exception:
            pass
    elif dry_run:
        print("\nDRY-RUN — brak zmian w DB.")

    conn.close()
    print("\nGotowe.")


if __name__ == '__main__':
    main()
