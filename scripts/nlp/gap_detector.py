"""scripts.nlp.gap_detector — Detekcja braków w dokumentacji projektowej.

Wykrywa:
  - Brakujące wymagane sekcje (wg. szablonów typów dokumentów)
  - Sekcje istniejące ale puste lub za krótkie
  - Brakujące metadane (tytuł, data, autor, standard)
  - Niespójność struktury (nagłówki niespójnego poziomu)

Klasa:
    GapDetector.analyse(doc_path, text) -> list[GapFinding]
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

from scripts.nlp.text_utils import extract_headings, normalize, tokenize

# ---------------------------------------------------------------------------
# Szablony wymaganych sekcji per typ dokumentu
# Klucz: wzorzec nazwy pliku (lowercase) lub wykryte słowo kluczowe w tytule
# Wartość: lista (wymagana_nazwa_sekcji, waga)
# ---------------------------------------------------------------------------

_SECTION_TEMPLATES: dict[str, list[tuple[str, int]]] = {
    # Specyfikacja wymagań / architektura
    "architecture": [
        ("overview", 3),
        ("context", 2),
        ("components", 3),
        ("interfaces", 2),
        ("data", 2),
        ("security", 3),
        ("deployment", 1),
    ],
    # Plan testów
    "testing": [
        ("scope", 3),
        ("approach", 3),
        ("test cases", 2),
        ("fixtures", 2),
        ("coverage", 2),
        ("metrics", 1),
        ("oracle", 2),
    ],
    # Integracja
    "integration": [
        ("api", 2),
        ("schema", 2),
        ("endpoints", 2),
        ("authentication", 3),
        ("migration", 1),
    ],
    # Implementacja / moduły
    "modules": [
        ("overview", 2),
        ("dependencies", 2),
        ("interface", 3),
        ("configuration", 2),
        ("error handling", 2),
    ],
    # Readme / overview
    "readme": [
        ("overview", 2),
        ("installation", 2),
        ("usage", 2),
        ("configuration", 1),
        ("contributing", 1),
    ],
    # Plan implementacji
    "implementation": [
        ("goals", 2),
        ("phases", 3),
        ("tasks", 3),
        ("acceptance criteria", 3),
        ("risks", 2),
        ("dependencies", 2),
    ],
    # Raport zgodności / audyt
    "audit": [
        ("scope", 3),
        ("findings", 3),
        ("recommendations", 3),
        ("risk", 2),
        ("timeline", 1),
    ],
    # Polityka bezpieczeństwa
    "security": [
        ("scope", 2),
        ("requirements", 3),
        ("authentication", 3),
        ("authorization", 3),
        ("encryption", 3),
        ("logging", 2),
        ("incident response", 2),
    ],
    # Domyślny szablon (każdy dokument)
    "_default": [
        ("overview", 2),
        ("scope", 2),
    ],
}

# Minimalna liczba tokenów dla sekcji — poniżej tej wartości sekcja uznana za pustą
_MIN_SECTION_TOKENS = 5

# Minimalna liczba nagłówków w dokumencie IT
_MIN_HEADING_COUNT = 2

# Wzorce wykrywania metadanych w tekście dokumentu (YAML frontmatter lub pierwszy nagłówek)
_METADATA_PATTERNS: dict[str, re.Pattern] = {
    "title": re.compile(r"^(#\s+.+|title\s*:\s*.+)", re.MULTILINE | re.IGNORECASE),
    "author": re.compile(r"(author|autor|właściciel|owner)\s*[:=]\s*\S+", re.IGNORECASE),
    "date": re.compile(r"(date|data|version|wersja)\s*[:=]\s*\d", re.IGNORECASE),
    "standard": re.compile(r"(ISO|IEEE|OWASP|GDPR|RODO|NIST|SOC)\s*[\d/:]", re.IGNORECASE),
}


# ---------------------------------------------------------------------------
# Struktury danych
# ---------------------------------------------------------------------------

@dataclass
class GapFinding:
    """Pojedynczy brak wykryty w dokumencie."""
    doc_path: str
    gap_type: str        # "missing_section" | "empty_section" | "missing_metadata" |
                         # "shallow_structure" | "heading_depth_inconsistency"
    severity: str        # "ERROR" | "WARNING" | "INFO"
    description: str
    section: str = ""    # nazwa brakującej/problematycznej sekcji
    weight: int = 1      # waga braku z szablonu

    def to_dict(self) -> dict:
        return {
            "doc_path": self.doc_path,
            "gap_type": self.gap_type,
            "severity": self.severity,
            "description": self.description,
            "section": self.section,
            "weight": self.weight,
        }


# ---------------------------------------------------------------------------
# Detekcja szablonu dokumentu
# ---------------------------------------------------------------------------

def _detect_doc_type(doc_path: str, text: str) -> str:
    """Wykryj typ dokumentu na podstawie nazwy pliku i treści."""
    path_lower = Path(doc_path).stem.lower()

    # Najpierw po nazwie pliku
    for key in _SECTION_TEMPLATES:
        if key != "_default" and key in path_lower:
            return key

    # Potem po słowach kluczowych w treści (pierwsze 500 znaków)
    text_sample = normalize(text[:500])
    for key in _SECTION_TEMPLATES:
        if key != "_default" and key in text_sample:
            return key

    return "_default"


# ---------------------------------------------------------------------------
# Normalizacja nagłówka do klucza szablonu
# ---------------------------------------------------------------------------

def _heading_matches_required(
    heading_norm: str,
    required_norm: str,
) -> bool:
    """Sprawdź czy nagłówek pasuje do wymaganej sekcji.

    Używa częściowego dopasowania (required może być podstringiem heading).
    """
    # Dokładne dopasowanie
    if required_norm == heading_norm:
        return True
    # Wymagana sekcja zawiera się w nagłówku
    if required_norm in heading_norm:
        return True
    # Nagłówek zawiera się w wymaganej sekcji (krótki nagłówek)
    if heading_norm in required_norm and len(heading_norm) >= 3:
        return True
    # Pierwsze słowo wymaganej sekcji pasuje do pierwszego słowa nagłówka
    req_first = required_norm.split()[0] if required_norm.split() else ""
    head_first = heading_norm.split()[0] if heading_norm.split() else ""
    if req_first and head_first and req_first == head_first and len(req_first) >= 4:
        return True
    return False


# ---------------------------------------------------------------------------
# GapDetector
# ---------------------------------------------------------------------------

class GapDetector:
    """Analizuje dokumenty pod kątem braków strukturalnych i merytorycznych.

    Przykład:
        detector = GapDetector()
        findings = detector.analyse("docs/architecture.md", text)
        for f in findings:
            print(f.severity, f.description)
    """

    def __init__(
        self,
        min_section_tokens: int = _MIN_SECTION_TOKENS,
        min_heading_count: int = _MIN_HEADING_COUNT,
    ) -> None:
        self._min_section_tokens = min_section_tokens
        self._min_heading_count = min_heading_count

    def analyse(self, doc_path: str, text: str) -> list[GapFinding]:
        """Przeanalizuj dokument i zwróć listę wykrytych braków.

        Args:
            doc_path: Ścieżka do dokumentu (używana w findings jako identyfikator).
            text: Treść dokumentu (Markdown).

        Returns:
            Lista GapFinding, posortowana wg severity (ERROR > WARNING > INFO).
        """
        findings: list[GapFinding] = []

        findings.extend(self._check_metadata(doc_path, text))
        findings.extend(self._check_min_structure(doc_path, text))
        findings.extend(self._check_required_sections(doc_path, text))
        findings.extend(self._check_empty_sections(doc_path, text))
        findings.extend(self._check_heading_consistency(doc_path, text))

        # Sortuj: ERROR najpierw
        _order = {"ERROR": 0, "WARNING": 1, "INFO": 2}
        findings.sort(key=lambda f: (_order.get(f.severity, 3), f.section))
        return findings

    # -------------------------------------------------------------------
    # Metody prywatne — poszczególne sprawdzenia
    # -------------------------------------------------------------------

    def _check_metadata(self, doc_path: str, text: str) -> list[GapFinding]:
        """Sprawdź obecność podstawowych metadanych."""
        findings: list[GapFinding] = []

        for meta_name, pattern in _METADATA_PATTERNS.items():
            if not pattern.search(text):
                severity = "ERROR" if meta_name == "title" else "INFO"
                findings.append(GapFinding(
                    doc_path=doc_path,
                    gap_type="missing_metadata",
                    severity=severity,
                    description=f"Brak metadanych: '{meta_name}'",
                    section=meta_name,
                    weight=2 if meta_name == "title" else 1,
                ))

        return findings

    def _check_min_structure(self, doc_path: str, text: str) -> list[GapFinding]:
        """Sprawdź czy dokument ma minimalną strukturę nagłówków."""
        findings: list[GapFinding] = []
        headings = extract_headings(text)

        if len(headings) < self._min_heading_count:
            findings.append(GapFinding(
                doc_path=doc_path,
                gap_type="shallow_structure",
                severity="WARNING",
                description=(
                    f"Dokument ma tylko {len(headings)} nagłówek/nagłówki; "
                    f"minimum to {self._min_heading_count}"
                ),
                section="_structure",
                weight=2,
            ))

        # Sprawdź czy dokument nie jest za krótki
        token_count = len(tokenize(text, remove_stopwords=False))
        if token_count < 20:
            findings.append(GapFinding(
                doc_path=doc_path,
                gap_type="shallow_structure",
                severity="WARNING",
                description=f"Dokument bardzo krótki: {token_count} tokenów",
                section="_content",
                weight=1,
            ))

        return findings

    def _check_required_sections(self, doc_path: str, text: str) -> list[GapFinding]:
        """Sprawdź czy wszystkie wymagane sekcje są obecne."""
        findings: list[GapFinding] = []
        doc_type = _detect_doc_type(doc_path, text)
        required = _SECTION_TEMPLATES.get(doc_type, _SECTION_TEMPLATES["_default"])

        headings = extract_headings(text)
        heading_norms = [normalize(h) for _, h in headings]

        for section_name, weight in required:
            section_norm = normalize(section_name)
            found = any(
                _heading_matches_required(h_norm, section_norm)
                for h_norm in heading_norms
            )
            if not found:
                severity = "ERROR" if weight >= 3 else "WARNING"
                findings.append(GapFinding(
                    doc_path=doc_path,
                    gap_type="missing_section",
                    severity=severity,
                    description=(
                        f"[{doc_type.upper()}] Brakuje sekcji: '{section_name}'"
                    ),
                    section=section_name,
                    weight=weight,
                ))

        return findings

    def _check_empty_sections(self, doc_path: str, text: str) -> list[GapFinding]:
        """Sprawdź czy sekcje nie są puste lub prawie puste."""
        findings: list[GapFinding] = []
        lines = text.split("\n")
        current_heading: str | None = None
        current_content: list[str] = []

        for line in lines:
            m = re.match(r"^(#{1,6})\s+(.*)", line)
            if m:
                # Oceń poprzednią sekcję
                if current_heading is not None:
                    content = " ".join(current_content)
                    tokens = tokenize(content, remove_stopwords=False)
                    if len(tokens) < self._min_section_tokens:
                        findings.append(GapFinding(
                            doc_path=doc_path,
                            gap_type="empty_section",
                            severity="WARNING",
                            description=(
                                f"Sekcja '{current_heading}' prawie pusta "
                                f"({len(tokens)} tokenów)"
                            ),
                            section=current_heading,
                            weight=1,
                        ))
                current_heading = m.group(2).strip()
                current_content = []
            else:
                current_content.append(line)

        # Ostatnia sekcja
        if current_heading is not None:
            content = " ".join(current_content)
            tokens = tokenize(content, remove_stopwords=False)
            if len(tokens) < self._min_section_tokens:
                findings.append(GapFinding(
                    doc_path=doc_path,
                    gap_type="empty_section",
                    severity="WARNING",
                    description=(
                        f"Sekcja '{current_heading}' prawie pusta "
                        f"({len(tokens)} tokenów)"
                    ),
                    section=current_heading,
                    weight=1,
                ))

        return findings

    def _check_heading_consistency(self, doc_path: str, text: str) -> list[GapFinding]:
        """Sprawdź spójność poziomów nagłówków (nie pomijaj poziomów)."""
        findings: list[GapFinding] = []
        headings = extract_headings(text)
        if len(headings) < 2:
            return findings

        prev_level = headings[0][0]
        for level, heading_text in headings[1:]:
            if level > prev_level + 1:
                findings.append(GapFinding(
                    doc_path=doc_path,
                    gap_type="heading_depth_inconsistency",
                    severity="INFO",
                    description=(
                        f"Nagłówek '{heading_text}' przeskakuje poziom "
                        f"(z H{prev_level} do H{level})"
                    ),
                    section=heading_text,
                    weight=1,
                ))
            prev_level = level

        return findings

    def completeness_score(self, findings: list[GapFinding]) -> float:
        """Oblicz wskaźnik kompletności [0.0–1.0] na podstawie znalezionych braków.

        Formuła logarytmiczna — odporna na "inflację" ostrzeżeń:
          - Każdy ERROR odejmuje 0.10 (max cap 0.50 za ERRORy)
          - Każdy WARNING odejmuje 0.02 (max cap 0.30 za WARNINGi)
          - INFO: bez wpływu

        Wynik 1.0 = brak braków, 0.0 = bardzo niekompletny dokument.
        """
        if not findings:
            return 1.0
        error_count = sum(1 for f in findings if f.severity == "ERROR")
        warning_count = sum(1 for f in findings if f.severity == "WARNING")
        error_penalty = min(error_count * 0.10, 0.50)
        warning_penalty = min(warning_count * 0.02, 0.30)
        return max(0.0, round(1.0 - error_penalty - warning_penalty, 3))
