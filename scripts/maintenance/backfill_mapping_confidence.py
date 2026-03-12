#!/usr/bin/env python3
"""
Backfill confidence scores for doc_standard_mapping rows where
match_reason='keyword_match' AND confidence IS NULL.
"""

import argparse
import csv
import logging
import re
import shutil
import sqlite3
import sys
import unicodedata
from pathlib import Path

from itdoc._batch import batch_continue

_log = logging.getLogger(__name__)

DB_PATH = Path(__file__).parent.parent.parent / "reports" / "it_doc_matrix.db"
GENERATED_TEMPLATES = Path(__file__).parent.parent.parent / "generated_templates"

STOP = {
    "i",
    "w",
    "z",
    "do",
    "na",
    "nie",
    "sie",
    "to",
    "jest",
    "dla",
    "oraz",
    "lub",
    "przy",
    "po",
    "jak",
    "co",
    "by",
    "ale",
    "ze",
    "the",
    "a",
    "an",
    "and",
    "or",
    "of",
    "in",
    "for",
    "is",
    "with",
    "on",
    "at",
    "be",
    "as",
    "from",
    "that",
    "this",
    "it",
    "are",
    "was",
    "will",
    "can",
    "has",
    "have",
    "system",
    "zarzadzanie",
    "zarzadzania",
    "document",
    "dokumentu",
    "management",
    # keep originals for backward compat (lookup happens post-normalize)
    "zarządzanie",
    "zarządzania",
}

# ---------------------------------------------------------------------------
# Polish → English translation map
# ---------------------------------------------------------------------------
PL_EN_MAP = {
    "bezpieczenstwo": "security",
    "bezpieczenstwie": "security",
    "bezpieczenstwem": "security",
    "bezpieczenstwa": "security",
    "ryzyko": "risk",
    "ryzyka": "risk",
    "ryzykiem": "risk",
    "zarzadzanie": "management",
    "zarzadzania": "management",
    "dostep": "access",
    "dostepu": "access",
    "dostepem": "access",
    "audyt": "audit",
    "audytu": "audit",
    "audytem": "audit",
    "incydent": "incident",
    "incydentu": "incident",
    "polityka": "policy",
    "polityki": "policy",
    "procedura": "procedure",
    "procedury": "procedure",
    "zgodnosc": "compliance",
    "zgodnosci": "compliance",
    "kontrola": "control",
    "kontroly": "control",
    "kontroli": "control",
    "dokumentacja": "documentation",
    "dokument": "document",
    "szkolenie": "training",
    "szkolenia": "training",
    "wdrozenie": "implementation",
    "wdrozenia": "implementation",
    "monitorowanie": "monitoring",
    "systemu": "system",
    "systemy": "systems",
    "siec": "network",
    "sieci": "network",
    "konfiguracja": "configuration",
    "konfiguracji": "configuration",
    "kopie": "backup",
    "kopia": "backup",
    "zapasowa": "backup",
    "ciaglosc": "continuity",
    "ciagloci": "continuity",
    "zmiany": "change",
    "zmiana": "change",
    "zmianie": "change",
    "wymagania": "requirements",
    "wymaganie": "requirement",
    "testy": "testing",
    "testow": "testing",
    "oprogramowanie": "software",
    "aplikacja": "application",
    "serwer": "server",
    "infrastruktura": "infrastructure",
    "uzytkownicy": "users",
    "uzytkownik": "user",
    "uprawnienia": "permissions",
    "uprawnienie": "permission",
    "haslo": "password",
    "hasla": "passwords",
    "uwierzytelnianie": "authentication",
    "szyfrowanie": "encryption",
    "szyfrowania": "encryption",
    "podatnosc": "vulnerability",
    "podatnosci": "vulnerabilities",
    "narusznie": "breach",
    "naruszenie": "breach",
    "dostawca": "supplier",
    "dostawcy": "suppliers",
    "zewnetrzny": "external",
    "prywatnosc": "privacy",
    "prywatnosci": "privacy",
    "dane": "data",
    "danych": "data",
    "danymi": "data",
    "ochrona": "protection",
    "ochrony": "protection",
    "zasob": "asset",
    "zasoby": "assets",
    "zasobow": "assets",
    "wlasciwy": "appropriate",
    "odpowiedzialnosc": "responsibility",
    "cel": "objective",
    "cele": "objectives",
    "celach": "objectives",
    "proces": "process",
    "procesy": "processes",
    "procesow": "processes",
    "wejscie": "input",
    "wyjscie": "output",
    "granice": "scope",
    "projekt": "project",
    "projektow": "projects",
    "analiza": "analysis",
    "analize": "analysis",
    "raport": "report",
    "raportu": "report",
    "raportowanie": "reporting",
    "komunikacja": "communication",
    "komunikacji": "communication",
    "przywodztwo": "leadership",
    "kierownictwo": "management",
    "strategia": "strategy",
    "strategii": "strategy",
    "architektura": "architecture",
    "architektury": "architecture",
    # ISO 9001 – quality management
    "jakosc": "quality",
    "jakosci": "quality",
    "jakoscia": "quality",
    "wyrob": "product",
    "wyrobu": "product",
    "wyroby": "products",
    "usluga": "service",
    "uslugi": "services",
    "uslug": "services",
    "klient": "customer",
    "klienta": "customer",
    "klientow": "customers",
    "satysfakcja": "satisfaction",
    "doskonalenie": "improvement",
    "doskonalenia": "improvement",
    "certyfikacja": "certification",
    "certyfikat": "certificate",
    "norma": "standard",
    "normy": "standard",
    "niezgodnosc": "nonconformity",
    "niezgodnosci": "nonconformities",
    "korygowanie": "corrective",
    "korygujace": "corrective",
    "zapobiegawcze": "preventive",
    "zapobieganie": "prevention",
    "przeglad": "review",
    "przegladem": "review",
    "planowanie": "planning",
    "planowania": "planning",
    "produkt": "product",
    "produktu": "product",
    "specyfikacja": "specification",
    "specyfikacji": "specification",
    # TOGAF ADM – enterprise architecture
    "przedsiebiorstwo": "enterprise",
    "przedsiebiorstwa": "enterprise",
    "korporacyjna": "enterprise",
    "korporacyjnej": "enterprise",
    "warstwa": "layer",
    "warstwy": "layers",
    "faza": "phase",
    "fazy": "phase",
    "fazami": "phase",
    "transformacja": "transformation",
    "transformacji": "transformation",
    "zdolnosc": "capability",
    "zdolnosci": "capabilities",
    "migracja": "migration",
    "migracji": "migration",
    "integracja": "integration",
    "integracji": "integration",
    "platforma": "platform",
    "platformy": "platform",
    "interfejs": "interface",
    "interfejsy": "interfaces",
    "komponent": "component",
    "komponentow": "components",
    "metodologia": "methodology",
    "metodologii": "methodology",
    "wizja": "vision",
    "wizji": "vision",
    "repozytorium": "repository",
    # COBIT 2019 – IT governance
    "lad": "governance",
    "ladu": "governance",
    "wartosc": "value",
    "wartosci": "value",
    "interesariusze": "stakeholders",
    "interesariusz": "stakeholder",
    "inwestycja": "investment",
    "inwestycji": "investment",
    "wydajnosc": "performance",
    "wydajnosci": "performance",
    "dojrzalosc": "maturity",
    "dojrzalosci": "maturity",
    "wskaznik": "indicator",
    "wskazniki": "indicators",
    "biznesowy": "business",
    "biznesowych": "business",
}

_PL_NORM = str.maketrans("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ", "acelnoszzACELNOSZZ")


def _normalize_pl(text: str) -> str:
    """Transliterate Polish diacritics to ASCII equivalents."""
    return text.translate(_PL_NORM)


def tokenize(text: str) -> set:
    """Tokenize text: normalize Polish chars, translate via PL_EN_MAP, remove stops."""
    normalized = _normalize_pl(text.lower())
    words = re.findall(r"[a-zA-Z]+", normalized)
    result = set()
    for w in words:
        if len(w) < 3 or w in STOP:
            continue
        result.add(w)
        en = PL_EN_MAP.get(w)
        if en:
            result.add(en)
    return result


def jaccard(set_a: set, set_b: set) -> float:
    """Return Jaccard similarity between two sets."""
    union = set_a | set_b
    if not union:
        return 0.0
    return len(set_a & set_b) / len(union)


def doc_title_from_path(doc_path: str) -> str:
    stem = Path(doc_path).stem  # e.g. "wizja_platformy_zarz_dzania..."
    return stem.replace("_", " ")


def rough_slug(s: str) -> str:
    """Transliterate Polish chars and slugify — mirrors how doc filenames are built."""
    pl = str.maketrans("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ", "acelnoszzACELNOSZZ")
    s = s.translate(pl).lower()
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_")[:80]


def get_real_title(doc_path: str, slug_to_title: dict) -> str:
    """Return the full Polish title for doc_path, falling back to underscore→space."""
    basename = doc_path.split("/")[-1].replace(".md", "")
    return slug_to_title.get(basename, basename.replace("_", " "))


def add_evidence_column(conn: sqlite3.Connection) -> None:
    try:
        conn.execute("ALTER TABLE doc_standard_mapping ADD COLUMN evidence TEXT")
        conn.commit()
    except sqlite3.OperationalError as exc:
        _log.debug(
            "evidence column already exists or ALTER failed: %s", exc
        )  # column already exists


# ---------------------------------------------------------------------------
# Content cache
# ---------------------------------------------------------------------------


def build_content_cache(base_dir: Path) -> dict:
    """Returns {doc_path: set_of_tokens} built from .md file headings + body."""
    cache: dict[str, set] = {}
    if not base_dir.exists():
        return cache
    for md_file in base_dir.rglob("*.md"):
        doc_path = str(md_file.relative_to(base_dir))
        with batch_continue(f"tokenize {doc_path}", logger=_log):
            raw = md_file.read_text(encoding="utf-8", errors="ignore")

            tokens: set = set()

            # Extract ## headings
            for line in raw.splitlines():
                stripped = line.strip()
                if stripped.startswith("#"):
                    tokens |= tokenize(stripped.lstrip("#").strip())

            # Strip frontmatter, then take first 300 words of body
            body = raw
            if raw.startswith("---"):
                parts = raw.split("---", 2)
                if len(parts) >= 3:
                    body = parts[2]
            body_words = re.findall(r"[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]+", body)[:300]
            tokens |= tokenize(" ".join(body_words))

            # Path components (skip 'generated_templates')
            for part in md_file.relative_to(base_dir).parts:
                clean = re.sub(r"\.md$", "", part).replace("_", " ").replace("-", " ")
                tokens |= tokenize(clean)

            cache[doc_path] = tokens
    return cache


# ---------------------------------------------------------------------------
# Domain bonus
# ---------------------------------------------------------------------------

# (code_keyword_in_standard, path_keywords, token_keywords)
_DOMAIN_KEYWORDS: list[tuple[str, list[str], list[str]]] = [
    (
        "27001",
        ["security", "bezpiecze", "isms", "audit", "incydent", "dostep"],
        ["security", "audit", "controls", "information"],
    ),
    ("27002", ["security", "bezpiecze", "control", "audit"], ["security", "controls", "audit"]),
    ("27005", ["risk", "ryzyko", "analiza"], ["risk", "vulnerability", "analysis"]),
    (
        "NIST CSF",
        ["cybersecurity", "security", "bezpiecze", "framework"],
        ["security", "controls", "protection"],
    ),
    (
        "CIS Controls",
        ["control", "cis", "benchmark", "security", "bezpiecze"],
        ["controls", "security", "audit"],
    ),
    (
        "RODO",
        ["prywatnosc", "privacy", "dane", "data", "gdpr", "osobow"],
        ["privacy", "data", "protection"],
    ),
    ("GDPR", ["privacy", "dane", "data", "personal", "osobow"], ["privacy", "data", "protection"]),
    ("PCI DSS", ["payment", "card", "pci", "platnosc"], ["security", "data"]),
    ("ISO 22301", ["continuity", "ciaglosc", "bcp", "bcm", "awaryjn"], ["continuity", "backup"]),
    (
        "COBIT",
        ["governance", "audit", "control", "zarzadzanie", "lad"],
        ["governance", "audit", "controls", "management", "maturity", "value"],
    ),
    (
        "ISO 9001",
        ["jakosc", "quality", "wyrob", "usluga", "klient", "doskonalen"],
        ["quality", "product", "service", "customer", "improvement"],
    ),
    (
        "TOGAF ADM",
        ["architektur", "enterprise", "faz", "transformacj", "migracj"],
        ["architecture", "enterprise", "phase", "framework", "layer"],
    ),
]


def _domain_bonus(standard_code: str, doc_path: str, doc_tokens: set | None = None) -> float:
    path_lower = doc_path.lower()
    tokens = doc_tokens or set()
    for code_kw, path_kws, token_kws in _DOMAIN_KEYWORDS:
        if code_kw in standard_code:
            if any(kw in path_lower for kw in path_kws) or any(kw in tokens for kw in token_kws):
                return 0.08
    return 0.0


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------


def _coverage_score(std_tokens: set, doc_tokens: set) -> float:
    """Fraction of std_tokens covered by doc_tokens, scaled to [0, 0.35]."""
    if not std_tokens:
        return 0.0
    covered = len(std_tokens & doc_tokens) / len(std_tokens)
    return covered * 0.35


def score_row(
    row,
    standards_cache: dict,
    guidance_cache: dict,
    slug_to_title: dict | None = None,
    content_cache: dict | None = None,
) -> tuple[float, str]:
    doc_path, standard_code = row["doc_path"], row["standard_code"]

    description = standards_cache.get(standard_code, "")
    std_tokens = tokenize(description)

    if slug_to_title is not None:
        title_text = get_real_title(doc_path, slug_to_title)
    else:
        title_text = doc_title_from_path(doc_path)
    title_tokens = tokenize(title_text)

    # Merge with content cache tokens (headings + body + path)
    cached_tokens = (content_cache or {}).get(doc_path, set())
    doc_tokens = title_tokens | cached_tokens

    intersection = std_tokens & doc_tokens
    base = _coverage_score(std_tokens, doc_tokens)

    has_guidance = lookup_guidance(guidance_cache, title_text, standard_code)
    guidance_bonus = 0.3 if has_guidance else 0.0

    bonus = _domain_bonus(standard_code, doc_path, doc_tokens)

    confidence = min(1.0, base + guidance_bonus + bonus)
    matched = sorted(intersection)[:5]
    evidence = f"tokens: {', '.join(matched)} | guidance_refs: {'yes' if has_guidance else 'no'}"
    return confidence, evidence


def build_caches(conn: sqlite3.Connection) -> tuple[dict, dict, dict]:
    standards_cache: dict[str, str] = {}
    for row in conn.execute("SELECT standard_code, description FROM standards"):
        standards_cache[row["standard_code"]] = row["description"] or ""

    guidance_cache: dict[tuple, bool] = {}
    slug_to_title: dict[str, str] = {}
    for row in conn.execute("SELECT doc_title, standards_refs FROM doc_section_guidance"):
        dt = row["doc_title"] or ""
        refs_raw = row["standards_refs"] or "[]"
        codes = re.findall(r'"([^"]+)"', refs_raw)
        for code in codes:
            guidance_cache[(dt.lower(), code)] = True
        # Build slug→full-title mapping
        slug = rough_slug(dt)
        if slug:
            slug_to_title[slug] = dt

    return standards_cache, guidance_cache, slug_to_title


def lookup_guidance(guidance_cache: dict, title_text: str, standard_code: str) -> bool:
    # Try exact match (case-insensitive), then partial slug match
    key = (title_text.lower(), standard_code)
    if key in guidance_cache:
        return True
    # Sometimes doc_title has slightly different spacing; try contains approach
    for (dt, sc), _ in guidance_cache.items():
        if sc == standard_code and title_text.lower() in dt:
            return True
    return False


def run(dry_run: bool, limit: int | None, reprocess: bool = False) -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    add_evidence_column(conn)

    if not dry_run:
        backup_path = str(DB_PATH) + ".pre_backfill_backup"
        shutil.copy(str(DB_PATH), backup_path)
        print(f"[INFO] DB backed up to {backup_path}")

    print("[INFO] Building caches...")
    standards_cache, guidance_cache, slug_to_title = build_caches(conn)

    print(f"[INFO] Building content cache from {GENERATED_TEMPLATES} ...")
    content_cache = build_content_cache(GENERATED_TEMPLATES)
    print(f"[INFO] Content cache: {len(content_cache)} files indexed")

    if reprocess:
        where = "match_reason IN ('keyword_match', 'keyword_match_scored')"
    else:
        where = "match_reason = 'keyword_match' AND confidence IS NULL"

    query = f"""
        SELECT id, doc_path, standard_code
        FROM doc_standard_mapping
        WHERE {where}
    """
    if limit:
        query += f" LIMIT {limit}"

    rows = conn.execute(query).fetchall()
    total = len(rows)
    print(f"[INFO] Rows to process: {total}")

    rows_processed = 0
    rows_updated = 0
    confidences: list[float] = []
    pending_updates: list[tuple] = []

    for row in rows:
        title_text = get_real_title(row["doc_path"], slug_to_title)
        std_tokens = tokenize(standards_cache.get(row["standard_code"], ""))
        title_tokens = tokenize(title_text)
        cached_tokens = content_cache.get(row["doc_path"], set())
        doc_tokens = title_tokens | cached_tokens

        intersection = std_tokens & doc_tokens
        base = _coverage_score(std_tokens, doc_tokens)

        has_guidance = lookup_guidance(guidance_cache, title_text, row["standard_code"])
        guidance_bonus = 0.3 if has_guidance else 0.0
        bonus = _domain_bonus(row["standard_code"], row["doc_path"], doc_tokens)
        confidence = min(1.0, base + guidance_bonus + bonus)

        matched = sorted(intersection)[:5]
        evidence = (
            f"tokens: {', '.join(matched)} | guidance_refs: {'yes' if has_guidance else 'no'}"
        )

        rows_processed += 1
        confidences.append(confidence)

        if not dry_run:
            pending_updates.append((confidence, evidence, row["id"]))

        if not dry_run and len(pending_updates) >= 500:
            conn.executemany(
                "UPDATE doc_standard_mapping SET confidence=?, evidence=?, match_reason='keyword_match_scored' WHERE id=?",
                pending_updates,
            )
            conn.commit()
            rows_updated += len(pending_updates)
            pending_updates.clear()

        if rows_processed % 1000 == 0:
            print(f"  ...processed {rows_processed}/{total}")

    # Flush remaining
    if not dry_run and pending_updates:
        conn.executemany(
            "UPDATE doc_standard_mapping SET confidence=?, evidence=?, match_reason='keyword_match_scored' WHERE id=?",
            pending_updates,
        )
        conn.commit()
        rows_updated += len(pending_updates)
        pending_updates.clear()

    conn.close()

    print("\n=== Stats ===")
    print(f"  rows_processed : {rows_processed}")
    print(f"  rows_updated   : {rows_updated if not dry_run else '(dry-run, 0 written)'}")
    if confidences:
        print(f"  avg_confidence : {sum(confidences) / len(confidences):.4f}")
        print(f"  min_confidence : {min(confidences):.4f}")
        print(f"  max_confidence : {max(confidences):.4f}")
    print(f"  mode           : {'DRY RUN' if dry_run else 'APPLY'}")


def export_low_confidence(threshold: float) -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """SELECT doc_path, standard_code, confidence, match_reason, evidence
           FROM doc_standard_mapping
           WHERE confidence < ? AND confidence IS NOT NULL
           ORDER BY confidence ASC""",
        (threshold,),
    ).fetchall()
    conn.close()

    writer = csv.writer(sys.stdout)
    writer.writerow(["doc_path", "standard_code", "confidence", "match_reason", "evidence"])
    for r in rows:
        writer.writerow(
            [r["doc_path"], r["standard_code"], r["confidence"], r["match_reason"], r["evidence"]]
        )
    print(f"Exported {len(rows)} rows with confidence < {threshold}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Backfill confidence scores for keyword_match rows"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--dry-run", action="store_true", default=True, help="Show stats but don't write (default)"
    )
    group.add_argument(
        "--apply", action="store_true", help="Actually write confidence scores to DB"
    )
    parser.add_argument(
        "--limit", type=int, default=None, help="Process only first N rows (for testing)"
    )
    parser.add_argument(
        "--reprocess",
        action="store_true",
        help="Also reprocess rows already scored (match_reason='keyword_match_scored')",
    )
    parser.add_argument(
        "--export-low-confidence",
        type=float,
        metavar="THRESHOLD",
        help="Export rows with confidence < THRESHOLD to CSV (stdout). Example: --export-low-confidence 0.4",
    )
    args = parser.parse_args()

    if args.export_low_confidence is not None:
        export_low_confidence(args.export_low_confidence)
        return

    dry_run = not args.apply
    run(dry_run=dry_run, limit=args.limit, reprocess=args.reprocess)


if __name__ == "__main__":
    main()
