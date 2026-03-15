"""scripts.nlp.relation_mapper — Mapowanie relacji między dokumentami.

Wykrywa:
  explicit_link  — markdown link [text](path) lub [[wikilink]]
  name_mention   — wzmianka nazwy innego dokumentu w tekście
  thematic_overlap — wspólne słowa kluczowe (>= próg)
  implication    — jeden doc zawiera wymaganie, inny je implementuje
  contradiction  — ta sama fraza kluczowa w sprzecznym kontekście
  extends        — doc A rozszerza/uszczegółowia doc B

Klasa:
    RelationMapper.analyse(docs: dict[str,str]) -> list[RelationRecord]
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

from scripts.nlp.text_utils import (
    extract_links,
    extract_headings,
    normalize,
    tokenize,
    shingles,
)
from scripts.nlp.similarity_engine import jaccard


# ---------------------------------------------------------------------------
# Wzorce implikacji i sprzeczności
# ---------------------------------------------------------------------------

# Słowa wyrażające wymagania (mogą implikować inny doc)
_REQUIREMENT_TRIGGERS: frozenset[str] = frozenset({
    "musi", "wymaga", "należy", "powinien", "powinna", "wymagane",
    "obowiązkowe", "konieczne", "must", "shall", "required", "mandatory",
})

# Słowa negujące / potencjalnie sprzeczne
_NEGATION_TRIGGERS: frozenset[str] = frozenset({
    "nie", "brak", "zabrania", "niedozwolone", "nie wolno",
    "not", "never", "prohibited", "forbidden",
})

# Słowa "extends" — dokument rozszerza inny
_EXTENDS_TRIGGERS: frozenset[str] = frozenset({
    "rozszerza", "uszczegółowia", "bazuje na", "opiera się na",
    "patrz", "zgodnie z", "zob.", "extends", "based on", "see also",
    "references", "per", "według", "wg",
})

# Minimalna liczba wspólnych kluczowych tokenów dla thematic_overlap
_THEMATIC_TOKEN_OVERLAP_MIN = 4

# Minimalne Jaccard shingle dla "extends" (umiarkowane podobieństwo)
_EXTENDS_JACCARD_RANGE = (0.15, 0.50)

# Stosunek wspólnych tokenów do ogółu (dla thematic)
_THEMATIC_RATIO_MIN = 0.25


# ---------------------------------------------------------------------------
# Struktury danych
# ---------------------------------------------------------------------------

@dataclass
class RelationRecord:
    """Relacja między dwoma dokumentami."""
    source_doc: str
    target_doc: str
    relation_type: str     # explicit_link | name_mention | thematic_overlap |
                           # implication | contradiction | extends
    link_text: str         # fraza lub tekst linku
    confidence: float      # 0.0–1.0

    def to_dict(self) -> dict:
        return {
            "source_doc": self.source_doc,
            "target_doc": self.target_doc,
            "relation_type": self.relation_type,
            "link_text": self.link_text,
            "confidence": round(self.confidence, 3),
        }


# ---------------------------------------------------------------------------
# Narzędzia pomocnicze
# ---------------------------------------------------------------------------

def _doc_name_variants(doc_path: str) -> set[str]:
    """Wygeneruj warianty nazwy dokumentu do rozpoznawania wzmianek.

    Np. 'docs/nlp-engine/ARCHITECTURE.md' →
        {'architecture', 'architektura', 'ARCHITECTURE', 'nlp-engine/architecture'}
    """
    stem = Path(doc_path).stem
    variants: set[str] = {
        normalize(stem),
        stem.lower(),
        stem.upper(),
        stem,
    }
    # Rozbij myślniki/podkreślenia → osobne warianty
    parts = re.split(r"[-_]", stem)
    if len(parts) > 1:
        variants.add(normalize(" ".join(parts)))
        variants.add(" ".join(p.lower() for p in parts))
    return variants


def _resolve_link_target(
    link_target: str,
    all_doc_ids: list[str],
) -> str | None:
    """Spróbuj rozwiązać cel linku na konkretny doc_id z korpusu."""
    link_norm = normalize(link_target)

    # Dokładne dopasowanie ścieżki
    for doc_id in all_doc_ids:
        if normalize(doc_id) == link_norm:
            return doc_id

    # Dopasowanie po nazwie pliku (bez ścieżki i rozszerzenia)
    link_stem = normalize(Path(link_target).stem)
    for doc_id in all_doc_ids:
        doc_stem = normalize(Path(doc_id).stem)
        if doc_stem == link_stem:
            return doc_id

    # Częściowe dopasowanie
    for doc_id in all_doc_ids:
        if link_stem and link_stem in normalize(doc_id):
            return doc_id

    return None


def _find_trigger_sentences(
    text: str,
    triggers: frozenset[str],
) -> list[str]:
    """Znajdź zdania zawierające triggery (do opisu relacji)."""
    sentences = re.split(r"[.!?\n]", text)
    result: list[str] = []
    for s in sentences:
        s_norm = normalize(s)
        if any(t in s_norm.split() for t in triggers):
            result.append(s.strip()[:100])
    return result[:3]  # maks 3 przykłady


# ---------------------------------------------------------------------------
# RelationMapper
# ---------------------------------------------------------------------------

class RelationMapper:
    """Wykrywa i klasyfikuje relacje między dokumentami.

    Przykład:
        mapper = RelationMapper()
        records = mapper.analyse({"doc1.md": text1, "doc2.md": text2})
        for r in records:
            print(r.relation_type, r.source_doc, "→", r.target_doc)
    """

    def analyse(
        self,
        docs: dict[str, str],
        *,
        similarity_threshold: float = _THEMATIC_RATIO_MIN,
    ) -> list[RelationRecord]:
        """Przeanalizuj słownik {doc_id: text} i zwróć listę relacji.

        Args:
            docs: Słownik dokumentów (identyfikator → treść).
            similarity_threshold: Próg dla thematic_overlap.

        Returns:
            Lista RelationRecord.
        """
        records: list[RelationRecord] = []
        all_ids = list(docs.keys())

        # Precompute tokensets i shingles
        tokens_map: dict[str, set[str]] = {
            doc_id: set(tokenize(text))
            for doc_id, text in docs.items()
        }
        shingles_map: dict[str, set[str]] = {
            doc_id: shingles(text, n=4)
            for doc_id, text in docs.items()
        }

        for source_id, source_text in docs.items():
            records.extend(
                self._find_explicit_links(source_id, source_text, all_ids)
            )
            records.extend(
                self._find_name_mentions(source_id, source_text, all_ids, docs)
            )
            records.extend(
                self._find_thematic_overlaps(
                    source_id, source_text, tokens_map, similarity_threshold
                )
            )
            records.extend(
                self._find_implications(source_id, source_text, all_ids, docs)
            )
            records.extend(
                self._find_extends(
                    source_id, source_text, shingles_map, all_ids, docs
                )
            )

        # Deduplikacja (ten sam source+target+type)
        seen: set[tuple] = set()
        unique: list[RelationRecord] = []
        for r in records:
            key = (r.source_doc, r.target_doc, r.relation_type)
            if key not in seen:
                seen.add(key)
                unique.append(r)

        # Sortuj: najwyższe confidence pierwsze
        unique.sort(key=lambda r: r.confidence, reverse=True)
        return unique

    # -------------------------------------------------------------------
    # Metody prywatne — poszczególne typy relacji
    # -------------------------------------------------------------------

    def _find_explicit_links(
        self,
        source_id: str,
        source_text: str,
        all_ids: list[str],
    ) -> list[RelationRecord]:
        """Znajdź jawne linki markdown i wikilinki."""
        records: list[RelationRecord] = []
        links = extract_links(source_text)
        for link_target in links:
            resolved = _resolve_link_target(link_target, all_ids)
            if resolved and resolved != source_id:
                records.append(RelationRecord(
                    source_doc=source_id,
                    target_doc=resolved,
                    relation_type="explicit_link",
                    link_text=link_target[:80],
                    confidence=1.0,
                ))
        return records

    def _find_name_mentions(
        self,
        source_id: str,
        source_text: str,
        all_ids: list[str],
        docs: dict[str, str],
    ) -> list[RelationRecord]:
        """Znajdź wzmianki nazw innych dokumentów w tekście."""
        records: list[RelationRecord] = []
        source_norm = normalize(source_text)

        for target_id in all_ids:
            if target_id == source_id:
                continue
            variants = _doc_name_variants(target_id)
            for variant in variants:
                if len(variant) >= 4 and variant in source_norm:
                    records.append(RelationRecord(
                        source_doc=source_id,
                        target_doc=target_id,
                        relation_type="name_mention",
                        link_text=variant[:60],
                        confidence=0.8,
                    ))
                    break  # jeden match per dokument wystarczy
        return records

    def _find_thematic_overlaps(
        self,
        source_id: str,
        source_text: str,
        tokens_map: dict[str, set[str]],
        threshold: float,
    ) -> list[RelationRecord]:
        """Znajdź dokumenty z silnym pokryciem słów kluczowych."""
        records: list[RelationRecord] = []
        source_tokens = tokens_map.get(source_id, set())
        if not source_tokens:
            return records

        for target_id, target_tokens in tokens_map.items():
            if target_id == source_id:
                continue
            if not target_tokens:
                continue

            common = source_tokens & target_tokens
            if len(common) < _THEMATIC_TOKEN_OVERLAP_MIN:
                continue

            ratio = len(common) / min(len(source_tokens), len(target_tokens))
            if ratio >= threshold:
                # Wybierz 3 najczęstsze wspólne tokeny jako opis
                sample = sorted(common)[:5]
                records.append(RelationRecord(
                    source_doc=source_id,
                    target_doc=target_id,
                    relation_type="thematic_overlap",
                    link_text=", ".join(sample),
                    confidence=round(min(ratio, 1.0), 3),
                ))

        return records

    def _find_implications(
        self,
        source_id: str,
        source_text: str,
        all_ids: list[str],
        docs: dict[str, str],
    ) -> list[RelationRecord]:
        """Wykryj implikacje: source zawiera wymaganie dla target."""
        records: list[RelationRecord] = []
        trigger_sentences = _find_trigger_sentences(source_text, _REQUIREMENT_TRIGGERS)
        if not trigger_sentences:
            return records

        # Sprawdź czy w treści pojawia się nazwa innego dokumentu
        for target_id in all_ids:
            if target_id == source_id:
                continue
            target_name = normalize(Path(target_id).stem)
            if len(target_name) < 4:
                continue
            for sentence in trigger_sentences:
                if target_name in normalize(sentence):
                    records.append(RelationRecord(
                        source_doc=source_id,
                        target_doc=target_id,
                        relation_type="implication",
                        link_text=sentence[:80],
                        confidence=0.7,
                    ))
                    break

        return records

    def _find_extends(
        self,
        source_id: str,
        source_text: str,
        shingles_map: dict[str, set[str]],
        all_ids: list[str],
        docs: dict[str, str],
    ) -> list[RelationRecord]:
        """Wykryj relacje 'extends' — doc A jest rozszerzeniem doc B."""
        records: list[RelationRecord] = []
        source_sh = shingles_map.get(source_id, set())

        # Sprawdź triggery extends w tekście
        trigger_sentences = _find_trigger_sentences(source_text, _EXTENDS_TRIGGERS)

        # Jeśli znaleziono triggery — sprawdź przez shingle similarity
        if trigger_sentences:
            for target_id in all_ids:
                if target_id == source_id:
                    continue
                target_sh = shingles_map.get(target_id, set())
                jac = jaccard(source_sh, target_sh)
                lo, hi = _EXTENDS_JACCARD_RANGE
                if lo <= jac <= hi:
                    records.append(RelationRecord(
                        source_doc=source_id,
                        target_doc=target_id,
                        relation_type="extends",
                        link_text=trigger_sentences[0][:80] if trigger_sentences else "",
                        confidence=round(0.5 + jac, 3),
                    ))

        return records

    def build_adjacency(
        self, records: list[RelationRecord]
    ) -> dict[str, list[str]]:
        """Zbuduj słownik adjacencji: {source: [targets]} z listy relacji."""
        adj: dict[str, list[str]] = {}
        for r in records:
            adj.setdefault(r.source_doc, []).append(r.target_doc)
        return adj

    def find_isolated(
        self,
        all_ids: list[str],
        records: list[RelationRecord],
    ) -> list[str]:
        """Zwróć dokumenty bez żadnych relacji (izolowane)."""
        connected: set[str] = set()
        for r in records:
            connected.add(r.source_doc)
            connected.add(r.target_doc)
        return [d for d in all_ids if d not in connected]
