"""scripts.nlp.duplicate_detector — Detekcja duplikatów i pokrewnych treści.

Klasyfikacja par dokumentów:
  exact      — Jaccard > 0.80 (niemal identyczna treść)
  extending  — cosine 0.55–0.80 + różne nagłówki (ta sama info, rozszerzenie)
  thematic   — cosine 0.30–0.55 (ten sam temat, różna głębokość)
  partial    — Jaccard 0.20–0.40 + cosine < 0.30 (fragment kopiowany)

Klasa:
    DuplicateDetector.analyse(corpus) -> list[DuplicateRecord]
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from scripts.nlp.similarity_engine import DocumentCorpus, jaccard, cosine_similarity
from scripts.nlp.text_utils import extract_headings, normalize


# ---------------------------------------------------------------------------
# Progi podobieństwa
# ---------------------------------------------------------------------------

_EXACT_JACCARD_THRESHOLD = 0.75     # >= → exact duplicate
_EXTENDING_COS_THRESHOLD = 0.55     # >= → extending (+ different headings)
_THEMATIC_COS_THRESHOLD = 0.30      # >= → thematic overlap
_PARTIAL_JACCARD_THRESHOLD = 0.20   # >= → partial copy (fragment)

# Maksymalna różnica współczynnika Jaccard między dwoma "extending" doc
# (jeśli są zbyt podobne Jaccard, to "exact", nie "extending")
_EXTENDING_JACCARD_MAX = 0.75

# Minimalna różnica struktury nagłówków (dla extending vs exact)
_HEADING_OVERLAP_THRESHOLD = 0.85   # jeśli nagłówki >=85% overlap → likely exact


# ---------------------------------------------------------------------------
# Struktury danych
# ---------------------------------------------------------------------------

@dataclass
class DuplicateRecord:
    """Para dokumentów ze wskaźnikiem podobieństwa i typem duplikatu."""
    doc_a: str
    doc_b: str
    similarity: float            # najwyższy z cosine/jaccard
    method: str                  # cosine_tfidf | jaccard_shingle
    duplicate_type: str          # exact | extending | thematic | partial
    description: str

    def to_dict(self) -> dict:
        return {
            "doc_a": self.doc_a,
            "doc_b": self.doc_b,
            "similarity": round(self.similarity, 4),
            "method": self.method,
            "duplicate_type": self.duplicate_type,
            "description": self.description,
        }


# ---------------------------------------------------------------------------
# Porównanie struktury nagłówków (wykrywanie "extending")
# ---------------------------------------------------------------------------

def _heading_overlap(headings_a: list[str], headings_b: list[str]) -> float:
    """Zwróć Jaccard similarity zbioru znormalizowanych nagłówków."""
    set_a = {normalize(h) for h in headings_a}
    set_b = {normalize(h) for h in headings_b}
    return jaccard(set_a, set_b)


def _describe_overlap(
    doc_a: str,
    doc_b: str,
    cos: float,
    jac: float,
    dup_type: str,
    heading_sim: float,
) -> str:
    """Zbuduj czytelny opis znalezionego duplikatu."""
    a_name = doc_a.split("/")[-1]
    b_name = doc_b.split("/")[-1]
    if dup_type == "exact":
        return (
            f"'{a_name}' i '{b_name}' są niemal identyczne "
            f"(Jaccard={jac:.2f}, cosine={cos:.2f}). "
            "Rozważ scalenie lub usunięcie jednego."
        )
    elif dup_type == "extending":
        return (
            f"'{a_name}' i '{b_name}' opisują ten sam temat, "
            f"ale z różnych perspektyw lub z innym zakresem "
            f"(cosine={cos:.2f}, różnica struktury nagłówków={1-heading_sim:.2f}). "
            "Rozważ: czy warto trzymać oba? Czy jeden jest nadpisaniem drugiego?"
        )
    elif dup_type == "thematic":
        return (
            f"'{a_name}' i '{b_name}' dotyczą zbliżonego tematu "
            f"(cosine={cos:.2f}). "
            "Sprawdź czy nie opisują tej samej koncepcji w różnych miejscach."
        )
    else:  # partial
        return (
            f"'{a_name}' i '{b_name}' mają wspólne fragmenty "
            f"(Jaccard={jac:.2f}). "
            "Możliwe kopiowanie sekcji — sprawdź manualnie."
        )


# ---------------------------------------------------------------------------
# DuplicateDetector
# ---------------------------------------------------------------------------

class DuplicateDetector:
    """Wykrywa duplikaty i pokrewne treści w zbiorze dokumentów.

    Używa DocumentCorpus (TF-IDF + shingling) i klasyfikuje pary.

    Przykład:
        detector = DuplicateDetector()
        for path, text in docs.items():
            detector.add(path, text)
        records = detector.analyse()
        for r in records:
            print(r.duplicate_type, r.description)
    """

    def __init__(self) -> None:
        self._corpus = DocumentCorpus()
        self._headings: dict[str, list[str]] = {}

    def add(self, doc_id: str, text: str) -> None:
        """Dodaj dokument do analizy."""
        self._corpus.add(doc_id, text)
        self._headings[doc_id] = [h for _, h in extract_headings(text)]

    def analyse(
        self,
        cos_threshold: float = _THEMATIC_COS_THRESHOLD,
        jac_threshold: float = _PARTIAL_JACCARD_THRESHOLD,
    ) -> list[DuplicateRecord]:
        """Przeanalizuj wszystkie pary dokumentów.

        Args:
            cos_threshold: Minimalny cosine similarity do zgłoszenia.
            jac_threshold: Minimalny Jaccard similarity do zgłoszenia.

        Returns:
            Lista DuplicateRecord, posortowana malejąco wg similarity.
        """
        if len(self._corpus) < 2:
            return []

        self._corpus.build()
        doc_ids = self._corpus.doc_ids
        records: list[DuplicateRecord] = []
        seen: set[frozenset] = set()

        for i, id_a in enumerate(doc_ids):
            for id_b in doc_ids[i + 1:]:
                pair = frozenset([id_a, id_b])
                if pair in seen:
                    continue
                seen.add(pair)

                cos = self._corpus.cosine_pair(id_a, id_b)
                jac = self._corpus.jaccard_pair(id_a, id_b)

                # Nic do zgłoszenia
                if cos < cos_threshold and jac < jac_threshold:
                    continue

                dup_type, method = self._classify(id_a, id_b, cos, jac)
                if dup_type is None:
                    continue

                similarity = max(cos, jac)
                heading_sim = _heading_overlap(
                    self._headings.get(id_a, []),
                    self._headings.get(id_b, []),
                )
                description = _describe_overlap(id_a, id_b, cos, jac, dup_type, heading_sim)

                records.append(DuplicateRecord(
                    doc_a=id_a,
                    doc_b=id_b,
                    similarity=similarity,
                    method=method,
                    duplicate_type=dup_type,
                    description=description,
                ))

        records.sort(key=lambda r: r.similarity, reverse=True)
        return records

    def _classify(
        self,
        id_a: str,
        id_b: str,
        cos: float,
        jac: float,
    ) -> tuple[str | None, str]:
        """Klasyfikuj parę (doc_a, doc_b) i zwróć (dup_type, method)."""

        # 1. Exact duplicate — wysoki Jaccard
        if jac >= _EXACT_JACCARD_THRESHOLD:
            return "exact", "jaccard_shingle"

        # 2. Extending — wysoki cosine, różne nagłówki
        if cos >= _EXTENDING_COS_THRESHOLD and jac < _EXTENDING_JACCARD_MAX:
            heading_sim = _heading_overlap(
                self._headings.get(id_a, []),
                self._headings.get(id_b, []),
            )
            if heading_sim < _HEADING_OVERLAP_THRESHOLD:
                return "extending", "cosine_tfidf"
            # Jeśli nagłówki też podobne → exact
            return "exact", "cosine_tfidf"

        # 3. Partial copy — widoczny fragment
        if jac >= _PARTIAL_JACCARD_THRESHOLD and cos < _THEMATIC_COS_THRESHOLD:
            return "partial", "jaccard_shingle"

        # 4. Thematic overlap
        if cos >= _THEMATIC_COS_THRESHOLD:
            return "thematic", "cosine_tfidf"

        return None, ""

    def top_duplicates(self, n: int = 10) -> list[DuplicateRecord]:
        """Zwróć top-N najbardziej podobnych par."""
        return self.analyse()[:n]
