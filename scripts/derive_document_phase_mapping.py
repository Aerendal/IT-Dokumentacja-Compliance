#!/usr/bin/env python3
"""
scripts/derive_document_phase_mapping.py

Faza 9C: Derywacja document_phase_mapping + document_lifecycle.

document_phase_mapping: które dokumenty są tworzone/używane w których fazach.
Źródło: tabela sections — anchor 'phase-NN' wskazuje że doc ma sekcję fazy N.

document_lifecycle: stany cyklu życia per dokument.
Generuje domyślny lifecycle: create (phase 1-2) → review (phase 3-4) → approve → active → archive.
"""

import logging
import sqlite3
from pathlib import Path

_log = logging.getLogger(__name__)

DB_PATH = Path(__file__).parent.parent / "reports" / "it_doc_matrix.db"


def main():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # ── document_phase_mapping ────────────────────────────────────────────────
    # Find all docs that have phase-NN sections
    cur.execute("""
        SELECT DISTINCT s.doc_uid, s.anchor,
               CAST(substr(s.anchor, 7) AS INTEGER) as phase_num
        FROM sections s
        WHERE s.anchor LIKE 'phase-%'
          AND length(s.anchor) <= 9
    """)
    phase_rows = cur.fetchall()

    # Get doc_uid → doc_id mapping (use docs.doc_uid as doc_id)
    cur.execute("SELECT doc_uid FROM docs")
    all_doc_uids = {r[0] for r in cur.fetchall()}

    # Check document_phase_mapping columns
    cur.execute("PRAGMA table_info(document_phase_mapping)")
    dpm_cols = {r[1] for r in cur.fetchall()}

    # Get phases table to map phase_number → phase_id
    cur.execute("SELECT phase_number, id FROM phases WHERE id IS NOT NULL LIMIT 1")
    sample = cur.fetchone()
    has_phase_id = sample is not None

    cur.execute("SELECT phase_number, rowid FROM phases")
    phase_num_to_rowid = {r[0]: r[1] for r in cur.fetchall()}

    inserted_dpm = 0
    for doc_uid, anchor, phase_num in phase_rows:
        if doc_uid not in all_doc_uids:
            continue
        phase_rowid = phase_num_to_rowid.get(phase_num)
        if not phase_rowid:
            continue

        try:
            if "doc_id" in dpm_cols and "phase_id" in dpm_cols:
                cur.execute("""
                    INSERT OR IGNORE INTO document_phase_mapping (doc_id, phase_id, action)
                    VALUES (?, ?, ?)
                """, (doc_uid, phase_rowid, "used"))
                if cur.rowcount:
                    inserted_dpm += 1
        except Exception as exc:
            _log.debug("document_phase_mapping insert skipped for %s: %s", doc_uid, exc)────────────────────────────────────────────────
    cur.execute("PRAGMA table_info(document_lifecycle)")
    dlc_cols = {r[1] for r in cur.fetchall()}

    # Lifecycle states for each doc: create → review → approve → active → archive
    lifecycle_states = [
        ("draft",    "Tworzenie",   "Dokument jest tworzony po raz pierwszy"),
        ("review",   "Przegląd",    "Dokument jest przeglądany przez interesariuszy"),
        ("approved", "Zatwierdzone","Dokument zatwierdzony do użycia"),
        ("active",   "Aktywne",     "Dokument jest aktywnie używany"),
        ("archived", "Archiwum",    "Dokument wycofany, przechowywany jako referencja"),
    ]

    inserted_dlc = 0
    if "doc_id" in dlc_cols and "lifecycle_state" in dlc_cols:
        # Only insert for a sample of docs to avoid 7941×5 = 39k rows — insert per unique doc
        cur.execute("SELECT doc_uid FROM docs LIMIT 500")
        sample_docs = [r[0] for r in cur.fetchall()]

        for doc_uid in sample_docs:
            for state, label, desc in lifecycle_states:
                try:
                    cur.execute("""
                        INSERT OR IGNORE INTO document_lifecycle (doc_id, lifecycle_state, description)
                        VALUES (?, ?, ?)
                    """, (doc_uid, state, desc))
                    if cur.rowcount:
                        inserted_dlc += 1
                except Exception as exc:
                    _log.debug("document_lifecycle insert skipped for %s/%s: %s", doc_uid, state, exc)
                    break  # if schema doesn't match, skip all

    conn.commit()
    conn.close()

    print(f"Faza 9C — document_phase_mapping: wstawiono {inserted_dpm} wierszy")
    print(f"Faza 9C — document_lifecycle:     wstawiono {inserted_dlc} wierszy (próbka 500 dok.)")


if __name__ == "__main__":
    main()
