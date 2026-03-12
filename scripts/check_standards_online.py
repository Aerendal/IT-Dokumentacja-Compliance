"""scripts/check_standards_online.py — weryfikacja kodow standardow IT.

Dwie warstwy sprawdzenia:
  1. Format + HTTP: czy kazdy z 44 kodow standardow z DB ma znany format
     i czy Wikipedia/oficjalna strona odpowiada HTTP 200.
  2. Mapping quality: probka 50 keyword_match — czy slowa kluczowe w pliku
     .md uzasadniaja przypisany standard (dopasowanie kluczowych slow).

Uruchamiaj z katalogu dokumentacja/:
    python3 scripts/check_standards_online.py [--offline] [--sample N]

Wymagania: requests (pip install requests)
"""

import argparse
import logging
import re
import sqlite3
import sys
import time
from pathlib import Path

_log = logging.getLogger(__name__)

try:
    import requests
    _HAS_REQUESTS = True
except ImportError:
    _HAS_REQUESTS = False

DB_PATH = Path("reports/it_doc_matrix.db")
CORE_DIR = Path("generated_templates/core")

# Znane, wiarygodne URL-e per kod standardu
STANDARD_URLS = {
    "ISO/IEC 27001":   "https://en.wikipedia.org/wiki/ISO/IEC_27001",
    "ISO/IEC 27002":   "https://en.wikipedia.org/wiki/ISO/IEC_27002",
    "ISO/IEC 27005":   "https://en.wikipedia.org/wiki/ISO/IEC_27005",
    "ISO/IEC 27017":   "https://en.wikipedia.org/wiki/ISO/IEC_27017",
    "ISO/IEC 27018":   "https://en.wikipedia.org/wiki/ISO/IEC_27018",
    "ISO/IEC 27035":   "https://www.iso.org/standard/78973.html",
    "ISO/IEC 27701":   "https://en.wikipedia.org/wiki/ISO/IEC_27701",
    "ISO/IEC 25010":   "https://en.wikipedia.org/wiki/ISO/IEC_25010",
    "ISO/IEC 25040":   "https://iso25000.com/index.php/en/iso-25000-standards/iso-25040",
    "ISO/IEC 12207":   "https://en.wikipedia.org/wiki/ISO/IEC_12207",
    "ISO/IEC 15288":   "https://en.wikipedia.org/wiki/ISO/IEC_15288",
    "ISO/IEC 20546":   "https://www.iso.org/standard/68305.html",
    "ISO/IEC 23053":   "https://www.iso.org/standard/74438.html",
    "ISO/IEC 29110":   "https://www.iso.org/standard/74611.html",
    "ISO/IEC 38500":   "https://en.wikipedia.org/wiki/ISO/IEC_38500",
    "ISO/IEC 42001":   "https://www.iso.org/standard/81230.html",
    "ISO 9001":        "https://en.wikipedia.org/wiki/ISO_9001",
    "ISO 20000-1":     "https://en.wikipedia.org/wiki/ISO/IEC_20000",
    "ISO 22301":       "https://en.wikipedia.org/wiki/ISO_22301",
    "IEEE 1012":       "https://en.wikipedia.org/wiki/IEEE_1012",
    "IEEE 1016":       "https://en.wikipedia.org/wiki/Software_design_description",
    "IEEE 42010":      "https://en.wikipedia.org/wiki/ISO/IEC_42010",
    "IEEE 829":        "https://en.wikipedia.org/wiki/IEEE_829",
    "IEEE 830":        "https://en.wikipedia.org/wiki/Software_requirements_specification",
    "NIST CSF":        "https://en.wikipedia.org/wiki/NIST_Cybersecurity_Framework",
    "NIST SP 800-53":  "https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final",
    "OWASP ASVS":      "https://owasp.org/www-project-application-security-verification-standard/",
    "OWASP MASVS":     "https://owasp.org/www-project-mobile-app-security/",
    "CIS Controls v8": "https://en.wikipedia.org/wiki/Center_for_Internet_Security",
    "PCI DSS":         "https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard",
    "SOC 2":           "https://en.wikipedia.org/wiki/System_and_Organization_Controls",
    "GDPR / RODO":     "https://en.wikipedia.org/wiki/General_Data_Protection_Regulation",
    "NIS2":            "https://digital-strategy.ec.europa.eu/en/policies/nis2-directive",
    "DORA":            "https://en.wikipedia.org/wiki/Digital_Operational_Resilience_Act",
    "ITIL 4":          "https://en.wikipedia.org/wiki/ITIL",
    "COBIT 2019":      "https://en.wikipedia.org/wiki/COBIT",
    "TOGAF ADM":       "https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework",
    "PMBOK 7":         "https://en.wikipedia.org/wiki/Project_Management_Body_of_Knowledge",
    "PRINCE2 7":       "https://en.wikipedia.org/wiki/PRINCE2",
    "SAFe 6.0":        "https://en.wikipedia.org/wiki/Scaled_agile_framework",
    "SCRUM Guide":     "https://en.wikipedia.org/wiki/Scrum_(software_development)",
    "HL7 FHIR":        "https://en.wikipedia.org/wiki/Fast_Healthcare_Interoperability_Resources",
    "OpenAPI 3.x":     "https://en.wikipedia.org/wiki/OpenAPI_Specification",
    "AsyncAPI 3.x":    "https://www.asyncapi.com/docs",
}

# Slowa kluczowe wskazujace na zasadnosc mappingu (per standard)
STANDARD_KEYWORDS = {
    "ISO/IEC 27001": ["bezpiecze", "security", "isms", "27001", "informacji", "ryzyko", "access control"],
    "ISO/IEC 27002": ["bezpiecze", "security", "27002", "kontrola"],
    "ISO/IEC 27701": ["prywatno", "privacy", "gdpr", "rodo", "dane osobowe"],
    "ISO/IEC 25010": ["jakosc", "quality", "uzyteczno", "niezawod", "wydajno"],
    "ISO/IEC 12207": ["cykl zycia", "oprogramow", "software lifecycle"],
    "ISO/IEC 15288": ["system", "architektur", "systems engineering"],
    "ISO/IEC 42001": ["sztuczna intelig", "ai", "machine learning", "ml"],
    "ISO/IEC 20546": ["big data", "danych", "analityka", "analytics"],
    "ISO 9001":      ["jakosc", "quality", "zarzadzan", "management"],
    "ISO 22301":     ["ciagl", "continuity", "disaster", "recovery", "bcp"],
    "IEEE 829":      ["test", "plan testow", "testing"],
    "IEEE 830":      ["wymagani", "requirements", "srs"],
    "IEEE 42010":    ["architektur", "architecture"],
    "NIST CSF":      ["cybersecurity", "bezpiecze", "security", "nist"],
    "NIST SP 800-53":["bezpiecze", "security", "access control", "kontrola dostepu"],
    "OWASP ASVS":    ["aplikacja", "web", "api", "security", "bezpiecze"],
    "OWASP MASVS":   ["mobile", "mobilna", "android", "ios", "aplikacja"],
    "PCI DSS":       ["platno", "payment", "karta", "card", "finans"],
    "SOC 2":         ["soc", "audit", "compliance", "bezpiecze"],
    "GDPR / RODO":   ["gdpr", "rodo", "prywatno", "dane osobowe", "privacy"],
    "NIS2":          ["nis", "cybersecurity", "krytyczna infrastruktura", "bezpiecze"],
    "DORA":          ["dora", "operational resilience", "fintech", "finans", "odporno"],
    "ITIL 4":        ["itsm", "itil", "serwis", "service management", "incident"],
    "COBIT 2019":    ["governance", "it governance", "kontrola", "cobit"],
    "TOGAF ADM":     ["architektur", "enterprise", "togaf", "adm"],
    "PMBOK 7":       ["projekt", "project", "pmbok", "pmi", "zarzadzan"],
    "PRINCE2 7":     ["projekt", "project", "prince", "metodyk"],
    "SAFe 6.0":      ["safe", "agile", "scaled", "pi planning"],
    "SCRUM Guide":   ["scrum", "sprint", "agile", "backlog"],
    "HL7 FHIR":      ["fhir", "hl7", "medical", "health", "zdrowie", "kliniczn"],
    "OpenAPI 3.x":   ["openapi", "rest", "api", "swagger", "endpoint"],
    "AsyncAPI 3.x":  ["asyncapi", "event", "kafka", "message", "async"],
}


def validate_format(code: str) -> tuple[bool, str]:
    """Sprawdza czy kod ma poprawny format dla swojej rodziny."""
    patterns = [
        (r"^ISO/IEC \d{4,6}(-\d+)?$", "ISO/IEC format OK"),
        (r"^ISO \d{4,6}(-\d+)?$", "ISO format OK"),
        (r"^IEEE \d{2,5}$", "IEEE format OK"),
        (r"^NIST (CSF|SP \d{3}-\d{1,3})$", "NIST format OK"),
        (r"^OWASP [A-Z]+$", "OWASP format OK"),
        (r"^(ITIL|COBIT|TOGAF|PMBOK|PRINCE2|SAFe|SCRUM Guide).*$", "Framework format OK"),
        (r"^(PCI DSS|SOC 2|CIS Controls.*|GDPR.*|NIS2|DORA|HL7.*|OpenAPI.*|AsyncAPI.*)$", "Other format OK"),
    ]
    for pattern, msg in patterns:
        if re.match(pattern, code):
            return True, msg
    return False, f"Nieznany format: {repr(code)}"


def check_url(url: str, timeout: int = 8) -> tuple[int, str]:
    """HTTP GET do URL, zwraca (status_code, info)."""
    if not _HAS_REQUESTS:
        return -1, "requests niedostepny"
    try:
        r = requests.get(url, timeout=timeout, allow_redirects=True,
                         headers={"User-Agent": "itdoc-standards-checker/0.1"})
        return r.status_code, f"HTTP {r.status_code}"
    except requests.exceptions.ConnectionError:
        return 0, "ConnectionError (brak sieci?)"
    except requests.exceptions.Timeout:
        return 0, "Timeout"
    except Exception as e:
        return 0, str(e)


def check_mapping_quality(conn, sample: int = 50) -> list[dict]:
    """Sprawdza jakosc keyword_match: czy plik .md zawiera slowa kluczowe standardu."""
    rows = conn.execute("""
        SELECT doc_path, standard_code, match_reason
        FROM doc_standard_mapping
        WHERE match_reason = 'keyword_match'
        ORDER BY RANDOM()
        LIMIT ?
    """, (sample,)).fetchall()

    results = []
    for row in rows:
        doc_path = row["doc_path"]
        code = row["standard_code"]
        keywords = STANDARD_KEYWORDS.get(code, [])

        # Sprawdz czy plik zawiera slowa kluczowe
        fpath = CORE_DIR / Path(doc_path).name
        if not fpath.exists():
            fpath = Path(doc_path)

        found_keywords = []
        if fpath.exists() and keywords:
            try:
                content = fpath.read_text(encoding="utf-8", errors="replace").lower()
                found_keywords = [kw for kw in keywords if kw.lower() in content]
            except Exception as exc:
                _log.debug("Cannot read %s for keyword check: %s", fpath, exc) else ("NO_KEYWORDS" if keywords else "NO_RULES")
        results.append({
            "doc_path": doc_path,
            "standard_code": code,
            "found_keywords": found_keywords,
            "quality": quality,
        })
    return results


def main():
    parser = argparse.ArgumentParser(description="Weryfikacja standardow IT w DB")
    parser.add_argument("--offline", action="store_true", help="Tylko walidacja formatu (bez HTTP)")
    parser.add_argument("--sample", type=int, default=50, help="Probka mapowań do sprawdzenia jakosci (domyslnie: 50)")
    parser.add_argument("--db", default=str(DB_PATH))
    args = parser.parse_args()

    db_path = Path(args.db)
    if not db_path.exists():
        print(f"BLAD: DB nie istnieje: {db_path}")
        return 1

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    codes = [r[0] for r in conn.execute(
        "SELECT DISTINCT standard_code FROM standards ORDER BY standard_code"
    ).fetchall()]

    print(f"=== Warstwa 1: Weryfikacja {len(codes)} kodow standardow ===\n")

    format_ok = []
    format_bad = []
    http_ok = []
    http_bad = []
    http_unknown = []

    for code in codes:
        valid, msg = validate_format(code)
        url = STANDARD_URLS.get(code)

        if not valid:
            format_bad.append((code, msg))
        else:
            format_ok.append(code)

        if not args.offline:
            if url:
                status, info = check_url(url)
                if status == 200:
                    http_ok.append((code, url, info))
                    print(f"  OK    {code:30} {info}")
                elif status == 0:
                    http_unknown.append((code, url, info))
                    print(f"  WARN  {code:30} {info}")
                else:
                    http_bad.append((code, url, info))
                    print(f"  FAIL  {code:30} {info} — {url}")
                time.sleep(0.3)  # grzecznosc wobec serwerow
            else:
                http_unknown.append((code, "", "brak URL w slowniku"))
                print(f"  ???   {code:30} brak URL w slowniku")
        else:
            if valid:
                print(f"  OK    {code:30} {msg}")
            else:
                print(f"  FAIL  {code:30} {msg}")

    print(f"\nFormat: {len(format_ok)} OK / {len(format_bad)} niepoprawnych")
    if not args.offline:
        print(f"HTTP:   {len(http_ok)} OK / {len(http_bad)} FAIL / {len(http_unknown)} brak URL")

    if format_bad:
        print("\nNiepoprawny format:")
        for code, msg in format_bad:
            print(f"  {code}: {msg}")

    if http_bad:
        print("\nHTTP FAIL (kod nie znaleziony?):")
        for code, url, info in http_bad:
            print(f"  {code}: {info} — {url}")

    print(f"\n=== Warstwa 2: Jakosc mapowań (probka {args.sample} keyword_match) ===\n")
    quality_results = check_mapping_quality(conn, sample=args.sample)
    bad = [r for r in quality_results if r["quality"] == "NO_KEYWORDS"]
    ok = [r for r in quality_results if r["quality"] == "OK"]

    print(f"OK (slowa kluczowe znalezione):   {len(ok)}/{len(quality_results)}")
    print(f"Podejrzane (brak slow kluczowych): {len(bad)}/{len(quality_results)}")

    if bad:
        print("\nPodejrzane mapowania (keyword match bez slow kluczowych w pliku):")
        for r in bad[:20]:
            print(f"  {r['standard_code']:25} {r['doc_path']}")

    conn.close()

    # Podsumowanie
    print("\n=== PODSUMOWANIE ===")
    issues = len(format_bad) + len(http_bad) + len(bad)
    if issues == 0:
        print("OK — brak problemow")
    else:
        print(f"Wykryto {issues} potencjalnych problemow (patrz powyzej)")

    return 0 if issues == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
