"""scripts.nlp.text_utils — Preprocessing tekstu polskiego (stdlib only).

Funkcje:
    normalize(text) -> str          # lowercase + PL diacritics → ASCII
    tokenize(text) -> list[str]     # tokeny >=3 znaki bez stopwords
    stem(word) -> str               # uproszczone suffixowe stemowanie
    shingles(text, n=3) -> set[str] # znakowe n-gramy dla Jaccard similarity
    extract_headings(text) -> list[tuple[int,str]]  # poziom nagłówka, tekst
    extract_links(text) -> list[str]                # markdown + wiki linki
    section_text(text, heading) -> str              # tekst pod danym nagłówkiem
"""

from __future__ import annotations

import re
import unicodedata
from typing import Iterator

# ---------------------------------------------------------------------------
# Polskie stopwords — funkcyjne słowa bez wartości semantycznej
# ---------------------------------------------------------------------------
_STOPWORDS: frozenset[str] = frozenset({
    # Spójniki
    "i", "oraz", "a", "ale", "lecz", "jednak", "natomiast", "zaś",
    "lub", "albo", "bądź", "czy", "ani", "ani",
    "bo", "gdyż", "ponieważ", "dlatego", "więc", "zatem",
    "że", "żeby", "aby", "ażeby", "żeby", "iż",
    "chociaż", "choć", "mimo", "pomimo", "chociażby",
    "gdy", "kiedy", "skoro", "jak", "jako",
    # Przyimki
    "w", "we", "z", "ze", "do", "od", "na", "po", "przy", "przez",
    "za", "pod", "nad", "przed", "między", "pomiędzy", "wśród",
    "ku", "u", "o", "ob", "dla", "bez", "poza", "wokół", "około",
    "spod", "spośród", "zza", "znad",
    # Zaimki
    "to", "się", "sobie", "siebie", "jego", "jej", "ich",
    "ich", "im", "je", "go", "mu", "nam", "nas", "was", "wam",
    "ten", "ta", "te", "tego", "tej", "temu", "tym",
    "który", "która", "które", "którego", "której",
    "który", "co", "kto", "gdzie", "kiedy", "jak",
    # Czasowniki posiłkowe
    "jest", "są", "być", "był", "była", "było", "byli", "były",
    "będzie", "będą", "będę", "będziesz", "będziemy", "będziecie",
    "może", "można", "należy", "trzeba", "powinien", "powinna",
    # Partykuły i przysłówki ogólne
    "nie", "też", "już", "jeszcze", "tylko", "jednak", "nawet",
    "bardzo", "bardziej", "najbardziej", "tak", "tak",
    "więcej", "mniej", "zawsze", "nigdy", "często", "rzadko",
    "tutaj", "tam", "tu", "właśnie", "wtedy", "teraz",
    # Liczebniki
    "jeden", "jedna", "jedno", "dwa", "dwie", "trzy", "cztery",
    "pierwsza", "pierwszy", "pierwsze", "drugi", "druga", "drugie",
    # Spójniki zdaniowe
    "np", "tj", "tzn", "itp", "itd", "etc", "czyli",
})

# Przedrostki do usunięcia przy normalizacji diacritics
_PL_TRANS: dict[int, str] = str.maketrans(
    "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ",
    "acelnoszzACELNOSZZ",
)

# Wzorzec tokenizacji — słowa (litery + myślnik)
_WORD_RE = re.compile(r"\b[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ][a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ\-]{2,}\b")

# Wzorzec nagłówków Markdown
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)", re.MULTILINE)

# Wzorzec linków Markdown: [text](url) lub [[wikilink]]
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_WIKI_LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")

# Wzorzec bloków kodu (do wykluczenia z tokenizacji)
_CODE_BLOCK_RE = re.compile(r"```.*?```|`[^`]+`", re.DOTALL)


# ---------------------------------------------------------------------------
# Normalizacja
# ---------------------------------------------------------------------------

def normalize(text: str) -> str:
    """Zamień wielkie litery i polskie znaki na ASCII lowercase.

    Przykład: 'Żądanie MFA' → 'zadanie mfa'
    """
    text = text.lower().translate(_PL_TRANS)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    return text


# ---------------------------------------------------------------------------
# Stemowanie — uproszczone reguły sufiksów polskich
# ---------------------------------------------------------------------------

_SUFFIXES: tuple[str, ...] = (
    # Rzeczowniki/przymiotniki (od najdłuższych)
    "owania", "owanie", "ywania", "ywanie", "iwania", "iwanie",
    "ności", "ności", "ościom", "ościach", "ością", "ości",
    "owania", "owaniu", "owaniu",
    "owego", "owej", "owym", "owe", "owi", "ową",
    "nych", "nych", "nemu", "nych", "nym",
    "acji", "acji", "acją", "acje", "acji",
    "nych", "nych",
    # Czasowniki
    "ować", "owały", "owała", "owało", "owali",
    "ywać", "ywały", "ywała", "ywało",
    "iwać", "iwały", "iwała",
    "ując", "ując", "uje", "uję", "ujemy", "ujecie",
    # Przymiotniki
    "owego", "owej", "owym", "owe",
    # Krótkie końcówki
    "iem", "iem", "ami", "ach", "owi", "iem",
    "ać", "eć", "yć", "ić",
    "ów", "om", "ie",
    "ę", "ą",
)

_MIN_STEM_LEN = 4  # minimalna długość rdzenia po odcięciu sufiksu


def stem(word: str) -> str:
    """Uproszczone stemowanie — odcinanie polskich sufiksów.

    Nie jest to pełny morphologizer; służy do grupowania form tego
    samego leksemu dla TF-IDF i detekcji duplikatów.
    """
    w = normalize(word)
    for suffix in _SUFFIXES:
        if w.endswith(suffix) and len(w) - len(suffix) >= _MIN_STEM_LEN:
            return w[: len(w) - len(suffix)]
    return w


# ---------------------------------------------------------------------------
# Tokenizacja
# ---------------------------------------------------------------------------

def tokenize(
    text: str,
    *,
    remove_stopwords: bool = True,
    stem_tokens: bool = True,
    min_len: int = 3,
) -> list[str]:
    """Zwróć listę tokenów z tekstu (bez bloków kodu, bez stopwords).

    Args:
        text: Surowy tekst (markdown OK — nagłówki, linki ignorowane).
        remove_stopwords: Czy usuwać polskie stopwords.
        stem_tokens: Czy stemować tokeny.
        min_len: Minimalna długość tokenu po normalizacji.

    Returns:
        Lista tokenów.
    """
    # Usuń bloki kodu
    clean = _CODE_BLOCK_RE.sub(" ", text)
    # Usuń składnię markdown (nagłówki # → tekst, linki → tekst)
    clean = re.sub(r"#{1,6}\s*", "", clean)
    clean = _MD_LINK_RE.sub(lambda m: m.group(1), clean)
    clean = _WIKI_LINK_RE.sub(lambda m: m.group(1), clean)
    # Usuń URL
    clean = re.sub(r"https?://\S+", " ", clean)

    tokens: list[str] = []
    for m in _WORD_RE.finditer(clean):
        word = m.group(0)
        norm = normalize(word)
        if len(norm) < min_len:
            continue
        if remove_stopwords and norm in _STOPWORDS:
            continue
        tokens.append(stem(norm) if stem_tokens else norm)
    return tokens


# ---------------------------------------------------------------------------
# Shingling — n-gramy znakowe dla Jaccard
# ---------------------------------------------------------------------------

def shingles(text: str, n: int = 4) -> set[str]:
    """Wygeneruj zbiór n-gramów znakowych z znormalizowanego tekstu.

    Używane do szybkiego wykrywania duplikatów (Jaccard similarity).

    Args:
        text: Wejściowy tekst.
        n: Rozmiar n-gramu (domyślnie 4 — dobry balans precision/recall).

    Returns:
        Zbiór n-gramów.
    """
    norm = normalize(text)
    # Usuń spacje wielokrotne
    norm = re.sub(r"\s+", " ", norm).strip()
    if len(norm) < n:
        return set()
    return {norm[i : i + n] for i in range(len(norm) - n + 1)}


# ---------------------------------------------------------------------------
# Ekstrakcja nagłówków
# ---------------------------------------------------------------------------

def extract_headings(text: str) -> list[tuple[int, str]]:
    """Zwróć listę (poziom, tekst_nagłówka) z dokumentu Markdown.

    Poziom 1 = `#`, poziom 2 = `##`, itd.
    """
    results: list[tuple[int, str]] = []
    for m in _HEADING_RE.finditer(text):
        level = len(m.group(1))
        heading_text = m.group(2).strip()
        # Usuń emoji i nadmiarowe znaki
        heading_text = re.sub(r"[^\w\s\-:/()\[\].,]", "", heading_text).strip()
        if heading_text:
            results.append((level, heading_text))
    return results


# ---------------------------------------------------------------------------
# Ekstrakcja linków
# ---------------------------------------------------------------------------

def extract_links(text: str) -> list[str]:
    """Zwróć listę celów linków (URL, ścieżki, nazwy wiki) z dokumentu.

    Wynikiem jest lista referencji — później RelationMapper decyduje
    czy to link wewnętrzny czy zewnętrzny.
    """
    refs: list[str] = []
    for m in _MD_LINK_RE.finditer(text):
        target = m.group(2).strip()
        refs.append(target)
    for m in _WIKI_LINK_RE.finditer(text):
        target = m.group(1).strip()
        refs.append(target)
    return refs


# ---------------------------------------------------------------------------
# Ekstrakcja tekstu pod nagłówkiem
# ---------------------------------------------------------------------------

def section_text(text: str, heading: str) -> str:
    """Zwróć tekst sekcji zaczynającej się od podanego nagłówka.

    Sekcja kończy się przy następnym nagłówku tego samego lub wyższego poziomu.

    Args:
        text: Cały tekst dokumentu.
        heading: Tekst nagłówka (bez #, case-insensitive).

    Returns:
        Tekst sekcji lub pusty string jeśli nagłówek nie znaleziony.
    """
    heading_norm = normalize(heading)
    lines = text.split("\n")
    start_idx: int | None = None
    start_level: int = 0

    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m and normalize(m.group(2).strip()) == heading_norm:
            start_idx = i + 1
            start_level = len(m.group(1))
            break

    if start_idx is None:
        return ""

    result_lines: list[str] = []
    for line in lines[start_idx:]:
        m = re.match(r"^(#{1,6})\s+", line)
        if m and len(m.group(1)) <= start_level:
            break
        result_lines.append(line)

    return "\n".join(result_lines).strip()


# ---------------------------------------------------------------------------
# Wykrywanie języka sekcji (heurystyka)
# ---------------------------------------------------------------------------

_PL_MARKERS: frozenset[str] = frozenset({
    "system", "dokument", "opis", "wymagania", "architektura",
    "implementacja", "testy", "bezpieczeństwo", "dane",
    "konfiguracja", "proces", "zakres",
})


def is_polish(text: str, threshold: float = 0.05) -> bool:
    """Prosta heurystyka: czy tekst jest po polsku.

    Sprawdza proporcję polskich znaków diakrytycznych.
    """
    if not text:
        return False
    pl_chars = sum(1 for c in text if c in "ąćęłńóśźżĄĆĘŁŃÓŚŹŻ")
    return (pl_chars / max(len(text), 1)) > threshold or any(
        m in normalize(text).split() for m in _PL_MARKERS
    )
