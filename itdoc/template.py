"""itdoc.template — ładowanie i walidacja szablonów IT Dokumentacja.

Szablony są plikami Markdown z YAML frontmatter (między ---).
Format:
    ---
    title: Tytuł szablonu
    status: needs_content
    aligned: true
    aligned_rev: 1
    aligned_at: RRRR-MM-DD
    aligned_by: codex
    ---

    # Tytuł szablonu

    ## Cel dokumentu
    ...

Funkcje:
  load_template(path) → dict z kluczami: frontmatter, body, sections, path
  validate_template(tmpl, validators=[]) → list[str] — lista błędów
  get_required_sections(section_set=None) → list[str] — kanoniczne wymagane nagłówki
"""

import re
from pathlib import Path
from typing import Callable, List, Optional

from itdoc.exceptions import TemplateError

# Wymagane nagłówki sekcji (jako wzorce regex, case-insensitive)
_REQUIRED_SECTION_PATTERNS = [
    r"## Cel dokumentu",
    r"## Zakres i granice",
    r"## Wejścia i wyjścia",
]

# Placeholdery które NIE powinny pozostać w szablonach
_FORBIDDEN_PLACEHOLDERS = [
    r"\[Rola / interesariusz\]",
    r"\[osoba/rola\]",
]

# Wzorzec emoji (zakres Unicode)
_EMOJI_RE = re.compile(
    "["
    "\U0001f600-\U0001f64f"
    "\U0001f300-\U0001f5ff"
    "\U0001f680-\U0001f6ff"
    "\U0001f700-\U0001f77f"
    "\U0001f780-\U0001f7ff"
    "\U0001f800-\U0001f8ff"
    "\U0001f900-\U0001f9ff"
    "\U0001fa00-\U0001fa6f"
    "\U0001fa70-\U0001faff"
    "\U00002702-\U000027b0"
    "\U000024c2-\U0001f251"
    "]+",
    flags=re.UNICODE,
)


_ALL_REQUIRED_SECTIONS = [
    "## Cel dokumentu",
    "## Zakres i granice",
    "## Wejścia i wyjścia",
]

_SECTION_SETS = {
    "core": ["## Cel dokumentu", "## Zakres i granice", "## Wejścia i wyjścia"],
    "minimal": ["## Cel dokumentu"],
    "extended": [
        "## Cel dokumentu",
        "## Zakres i granice",
        "## Wejścia i wyjścia",
        "## Metadane",
    ],
}


def get_required_sections(section_set: Optional[str] = None) -> list:
    """Zwraca listę kanonicznych wymaganych nagłówków sekcji.

    Args:
        section_set: Nazwa predefiniowanego zestawu sekcji lub None (domyślny).
            Dostępne zestawy: "core" (domyślny), "minimal", "extended".
            Można też przekazać własną listę nagłówków poprzez słownik
            _SECTION_SETS przed wywołaniem.

    Returns:
        list[str] — lista nagłówków sekcji (wzorce do sprawdzania).
    """
    if section_set is None:
        return list(_ALL_REQUIRED_SECTIONS)
    if section_set not in _SECTION_SETS:
        raise ValueError(
            f"Nieznany section_set: '{section_set}'. "
            f"Dostępne: {list(_SECTION_SETS.keys())}"
        )
    return list(_SECTION_SETS[section_set])


def load_template(path: Path) -> dict:
    """Ładuje szablon z pliku Markdown.

    Returns:
        dict z kluczami:
          - path: Path
          - frontmatter: dict (parsed YAML fields as strings)
          - body: str (treść po frontmatterze)
          - headings: list[str] (nagłówki ## znalezione w body)

    Raises:
        TemplateError: Gdy plik nie istnieje lub frontmatter jest niepoprawny.
    """
    path = Path(path)
    if not path.exists():
        raise TemplateError(f"Plik nie istnieje: {path}")

    raw = path.read_text(encoding="utf-8")

    frontmatter, body = _parse_frontmatter(raw, path)
    headings = re.findall(r"^##\s+(.+)$", body, re.MULTILINE)

    return {
        "path": path,
        "frontmatter": frontmatter,
        "body": body,
        "headings": headings,
    }


def validate_template(tmpl: dict, validators: Optional[List[Callable]] = None) -> list:
    """Waliduje załadowany szablon.

    Args:
        tmpl: Słownik zwrócony przez load_template().
        validators: Opcjonalna lista callables (tmpl: dict) -> list[str].
            Każdy validator otrzymuje tmpl i zwraca listę komunikatów o błędach.
            Wyniki są dołączane do listy błędów wbudowanych walidatorów.

    Returns:
        Lista stringów z opisem błędów. Pusta lista = szablon OK.
    """
    errors = []
    body = tmpl.get("body", "")
    fm = tmpl.get("frontmatter", {})
    path = tmpl.get("path", "?")

    # Sprawdź wymagane pola frontmattera
    for field in ("title", "status", "aligned"):
        if field not in fm:
            errors.append(f"{path}: brak pola frontmatter: {field}")

    # Sprawdź wymagane sekcje
    for section in _REQUIRED_SECTION_PATTERNS:
        if not re.search(section, body, re.IGNORECASE):
            errors.append(f"{path}: brakująca sekcja: {section}")

    # Sprawdź zakazane placeholdery
    for ph in _FORBIDDEN_PLACEHOLDERS:
        if re.search(ph, body, re.IGNORECASE):
            errors.append(f"{path}: niedozwolony placeholder: {ph}")

    # Sprawdź emoji
    if _EMOJI_RE.search(body):
        errors.append(f"{path}: zawiera emoji (hard gate)")

    # Uruchom dodatkowe pluggable validators
    if validators:
        for validator in validators:
            try:
                extra = validator(tmpl)
                if extra:
                    errors.extend(extra)
            except Exception as exc:
                errors.append(f"{path}: błąd validatora {getattr(validator, '__name__', '?')}: {exc}")

    return errors


def _parse_frontmatter(raw: str, path: Optional[Path] = None) -> tuple:
    """Parsuje YAML frontmatter z treści pliku Markdown.

    Returns:
        Tuple (frontmatter_dict, body_str).

    Raises:
        TemplateError: Gdy frontmatter jest nieobecny lub nie można go sparsować.
    """
    lines = raw.split("\n")
    if not lines or lines[0].strip() != "---":
        raise TemplateError(f"{path}: brak frontmattera (oczekiwano '---' na początku)")

    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        raise TemplateError(f"{path}: frontmatter nie jest zamknięty '---'")

    fm_lines = lines[1:end_idx]
    fm: dict = {}
    for line in fm_lines:
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip()

    body = "\n".join(lines[end_idx + 1:])
    return fm, body
