"""itdoc.anchor — kanoniczne generowanie anchor-slug z nagłówka sekcji.

Logika odzwierciedla oryginalne generowanie anchorów w DB (scripts/reindex_sections.py,
scripts/resolve_content_links_extended.py).  Utrzymywana w jednym miejscu aby uniknąć
rozbieżności między skryptami.

Zasady:
  1. Lowercase + strip białych znaków.
  2. Nagłówki faz: "Faza N: ..." → "phase-0N" (zachowanie z reindex_sections).
  3. Strip znaków non-ASCII (polskie diakrytyki usuwane, nie transliterowane).
  4. Usunięcie znaków innych niż [a-z0-9 -].
  5. Spacje → myślnik.
  6. Kolaps wielokrotnych myślników.
"""

import re


def to_anchor(text: str) -> str:
    """Normalizuje nagłówek sekcji do anchor-slug.

    Przykłady:
      "Cel dokumentu"           → "cel-dokumentu"
      "Zakres i granice"        → "zakres-i-granice"
      "Standardy i compliance"  → "standardy-i-compliance"
      "Zależności"              → "zalenoci"  (strip non-ASCII)
      "Faza 3: Design"          → "phase-03"
    """
    if not text:
        return ""

    s = text.lower().strip()

    # Nagłówki faz — specjalny format zachowany z reindex_sections.py
    m = re.match(r'^faza\s+(\d+)\s*:', s)
    if m:
        n = int(m.group(1))
        return f"phase-{n:02d}"

    # Strip polskich diakrytyków (usunięcie, nie transliteracja — zgodne z DB)
    s = s.encode('ascii', 'ignore').decode('ascii')

    # Tylko alfanumeryczne, spacje i myślniki
    s = re.sub(r'[^a-z0-9\s\-]', '', s)

    # Spacje → myślnik, kolaps wielokrotnych
    s = re.sub(r'\s+', '-', s.strip())
    s = re.sub(r'-+', '-', s)

    return s
