"""scripts.nlp.similarity_engine — TF-IDF i metryki podobieństwa (stdlib only).

Funkcje:
    tf_idf_vectors(docs) -> list[dict[str,float]]   # oblicz wektory TF-IDF
    cosine_similarity(v1, v2) -> float              # podobieństwo kosinusowe
    jaccard(set1, set2) -> float                    # podobieństwo Jaccard
    top_similar(query_vec, corpus_vecs, n) -> list  # top-N podobnych
    DocumentCorpus                                   # cache wektorów dla wielu doc
"""

from __future__ import annotations

import math
from collections import Counter
from typing import NamedTuple, Sequence

from scripts.nlp.text_utils import tokenize, shingles


# ---------------------------------------------------------------------------
# Typy
# ---------------------------------------------------------------------------

Vector = dict[str, float]  # sparse TF-IDF vector: {term: weight}


class SimilarityResult(NamedTuple):
    doc_id: str
    score: float
    method: str  # "cosine_tfidf" | "jaccard_shingle"


# ---------------------------------------------------------------------------
# Jaccard similarity (zbiory n-gramów)
# ---------------------------------------------------------------------------

def jaccard(set_a: set, set_b: set) -> float:
    """Współczynnik Jaccarda — szybki, nie wymaga wektoryzacji.

    Używany do wykrywania niemal identycznych dokumentów (plagiat/duplikat).

    Args:
        set_a, set_b: Zbiory elementów (np. shingle sets).

    Returns:
        Wartość z [0.0, 1.0] — 1.0 = identyczne, 0.0 = brak wspólnych elementów.
    """
    if not set_a and not set_b:
        return 1.0
    if not set_a or not set_b:
        return 0.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union


# ---------------------------------------------------------------------------
# TF-IDF
# ---------------------------------------------------------------------------

def _compute_tf(tokens: list[str]) -> dict[str, float]:
    """Term Frequency — znormalizowana częstość termu w dokumencie."""
    if not tokens:
        return {}
    counts = Counter(tokens)
    total = len(tokens)
    return {term: count / total for term, count in counts.items()}


def _compute_idf(docs_tokens: list[list[str]]) -> dict[str, float]:
    """Inverse Document Frequency — log((N+1) / (df+1)) + 1 (smooth).

    Implementacja zgodna z sklearn TfidfVectorizer(smooth_idf=True).
    """
    n = len(docs_tokens)
    df: dict[str, int] = Counter()
    for tokens in docs_tokens:
        for term in set(tokens):
            df[term] += 1
    return {
        term: math.log((n + 1) / (count + 1)) + 1.0
        for term, count in df.items()
    }


def tf_idf_vectors(
    docs: list[list[str]],
    idf: dict[str, float] | None = None,
) -> tuple[list[Vector], dict[str, float]]:
    """Oblicz wektory TF-IDF dla listy tokenizowanych dokumentów.

    Args:
        docs: Lista tokenizowanych dokumentów (lista list tokenów).
        idf: Gotowy słownik IDF; jeśli None, oblicza z `docs`.

    Returns:
        (vectors, idf_dict) — lista wektorów TF-IDF i użyty słownik IDF.
    """
    if idf is None:
        idf = _compute_idf(docs)
    vectors: list[Vector] = []
    for tokens in docs:
        tf = _compute_tf(tokens)
        vec: Vector = {}
        for term, tf_val in tf.items():
            if term in idf:
                vec[term] = tf_val * idf[term]
        # L2 normalizacja wektora
        norm = math.sqrt(sum(v * v for v in vec.values()))
        if norm > 0:
            vec = {t: v / norm for t, v in vec.items()}
        vectors.append(vec)
    return vectors, idf


# ---------------------------------------------------------------------------
# Cosine similarity
# ---------------------------------------------------------------------------

def cosine_similarity(v1: Vector, v2: Vector) -> float:
    """Podobieństwo kosinusowe dwóch rzadkich wektorów TF-IDF.

    Wektory muszą być L2-znormalizowane (co robi tf_idf_vectors).

    Returns:
        float w [0.0, 1.0].
    """
    if not v1 or not v2:
        return 0.0
    # Iloczyn skalarny (suma po wspólnych terminach)
    dot = sum(v1.get(term, 0.0) * val for term, val in v2.items())
    return max(0.0, min(1.0, dot))  # clip do [0,1] ze względu na błędy float


# ---------------------------------------------------------------------------
# Top-N podobnych dokumentów
# ---------------------------------------------------------------------------

def top_similar(
    query_vec: Vector,
    corpus_vecs: list[tuple[str, Vector]],
    n: int = 5,
    threshold: float = 0.0,
) -> list[SimilarityResult]:
    """Znajdź top-N dokumentów podobnych do query_vec.

    Args:
        query_vec: Wektor zapytania (TF-IDF).
        corpus_vecs: Lista (doc_id, wektor) z korpusu.
        n: Maksymalna liczba wyników.
        threshold: Minimalne podobieństwo (domyślnie 0.0).

    Returns:
        Lista SimilarityResult posortowana malejąco.
    """
    results: list[SimilarityResult] = []
    for doc_id, vec in corpus_vecs:
        score = cosine_similarity(query_vec, vec)
        if score >= threshold:
            results.append(SimilarityResult(doc_id, score, "cosine_tfidf"))
    results.sort(key=lambda r: r.score, reverse=True)
    return results[:n]


# ---------------------------------------------------------------------------
# DocumentCorpus — cache wektorów dla wielu dokumentów
# ---------------------------------------------------------------------------

class DocumentCorpus:
    """Cache TF-IDF i shingle wektorów dla zbioru dokumentów.

    Umożliwia inkrementalne dodawanie dokumentów i efektywne
    wyszukiwanie podobieństwa bez ponownego przeliczania IDF.

    Użycie:
        corpus = DocumentCorpus()
        corpus.add("doc1.md", text1)
        corpus.add("doc2.md", text2)
        corpus.build()
        results = corpus.find_similar("doc1.md", threshold=0.4)
    """

    def __init__(self) -> None:
        self._docs: dict[str, str] = {}          # doc_id → raw text
        self._tokens: dict[str, list[str]] = {}  # doc_id → tokens
        self._shingles: dict[str, set[str]] = {} # doc_id → shingle set
        self._vectors: dict[str, Vector] = {}    # doc_id → TF-IDF vector
        self._idf: dict[str, float] = {}
        self._built: bool = False

    def add(self, doc_id: str, text: str) -> None:
        """Dodaj dokument do korpusu. Wymaga ponownego build()."""
        self._docs[doc_id] = text
        self._tokens[doc_id] = tokenize(text)
        self._shingles[doc_id] = shingles(text, n=4)
        self._built = False

    def build(self) -> None:
        """Przelicz wektory TF-IDF dla całego korpusu."""
        doc_ids = list(self._tokens.keys())
        token_lists = [self._tokens[d] for d in doc_ids]
        vectors, self._idf = tf_idf_vectors(token_lists)
        self._vectors = dict(zip(doc_ids, vectors))
        self._built = True

    def find_similar(
        self,
        doc_id: str,
        n: int = 10,
        threshold: float = 0.15,
        method: str = "cosine",
    ) -> list[SimilarityResult]:
        """Znajdź dokumenty podobne do doc_id.

        Args:
            doc_id: Identyfikator dokumentu zapytania.
            n: Maksymalna liczba wyników.
            threshold: Minimalne podobieństwo.
            method: "cosine" (TF-IDF) | "jaccard" (shingle) | "both" (max)

        Returns:
            Lista SimilarityResult bez self-match.
        """
        if not self._built:
            self.build()
        if doc_id not in self._vectors:
            return []

        results: list[SimilarityResult] = []
        query_vec = self._vectors[doc_id]
        query_sh = self._shingles[doc_id]

        for other_id in self._docs:
            if other_id == doc_id:
                continue

            if method in ("cosine", "both"):
                cos = cosine_similarity(query_vec, self._vectors[other_id])
            else:
                cos = 0.0

            if method in ("jaccard", "both"):
                jac = jaccard(query_sh, self._shingles[other_id])
            else:
                jac = 0.0

            if method == "both":
                score = max(cos, jac)
                used_method = "cosine_tfidf" if cos >= jac else "jaccard_shingle"
            elif method == "jaccard":
                score = jac
                used_method = "jaccard_shingle"
            else:
                score = cos
                used_method = "cosine_tfidf"

            if score >= threshold:
                results.append(SimilarityResult(other_id, score, used_method))

        results.sort(key=lambda r: r.score, reverse=True)
        return results[:n]

    def jaccard_pair(self, id_a: str, id_b: str) -> float:
        """Jaccard similarity między parą dokumentów."""
        return jaccard(
            self._shingles.get(id_a, set()),
            self._shingles.get(id_b, set()),
        )

    def cosine_pair(self, id_a: str, id_b: str) -> float:
        """Cosine TF-IDF similarity między parą dokumentów."""
        if not self._built:
            self.build()
        return cosine_similarity(
            self._vectors.get(id_a, {}),
            self._vectors.get(id_b, {}),
        )

    @property
    def doc_ids(self) -> list[str]:
        return list(self._docs.keys())

    def __len__(self) -> int:
        return len(self._docs)
