# 16 — Data Strategy (Strategia Danych)

**Status:** Draft v1.0  
**Powiązane dokumenty:** 02_system_state_description, 09_semantic_mapper_spec, 12_itdoc_integration_spec, 15_implementation_roadmap

---

## 1. Problem: stan bazy it_doc_matrix.db

Empiryczna weryfikacja bazy przed implementacją ujawniła krytyczną rozbieżność między założeniami specyfikacji a rzeczywistym stanem danych:

### 1.1 Tabele puste lub nieistniejące

| Tabela | Stan | Kluczowe metody zależne |
|--------|------|------------------------|
| `doc_standard_mapping` | **NIE ISTNIEJE** | `find_by_standard()` |
| `contracts` | **NIE ISTNIEJE** | `get_contract()` |
| `rhythm_edges` | **0 wierszy** | `rhythm_upstream()`, `rhythm_downstream()` |
| `standards` | **0 wierszy** | normalizacja aliasów |
| `document_standards` | **0 wierszy** | — |
| `compliance_regulations` | **0 wierszy** | `find_by_regulation()` |
| `document_phases` | **0 wierszy** | `get_phases()` |
| `document_raci` | **0 wierszy** | role assignee |

### 1.2 Tabele wypełnione (dostępne dla fallback)

| Tabela | Wiersze | Kolumny dostępne | Przydatność |
|--------|---------|-----------------|-------------|
| `documents` | 7 205 | `doc_id, branch_id, phase_id, flag, title` | Keyword search po `title` |
| `document_phase_mapping` | 7 205 | `doc_id, phase_id, priority` | Filtr po fazie |
| `phases` | 24 | `rowid, name, ordinal` | Lista faz (zamiast `document_phases`) |
| `branches` | 12 | `rowid, name, ordinal` | Filtr po branży (Backend/QA/itp.) |
| `industries` | 90 | — | Rozpoznanie domeny projektu |

> **Uwaga:** `documents` nie ma kolumny `path` — tylko `title`. Scoring Jaccard może operować wyłącznie po tytułach szablonów.

### 1.3 Konsekwencja dla pipeline

```
Przy pustej bazie:
  find_by_standard("ISO 27001")  → []   (tabela nie istnieje)
  find_by_regulation("RODO")     → []   (j.w.)
  rhythm_upstream("doc123")      → []   (rhythm_edges = 0)
  get_contract("doc123")         → None (tabela nie istnieje)

  Etap 2 (Multi-Query):          → 0 kandydatów
  Etap 3 (Jaccard scoring):      → puste wyniki
  MappingResult:                 → {items: [], total_items: 0}
  EstimationReport:              → InsufficientMappingError
```

---

## 2. Trzy strategie — możliwość łączenia

Strategie nie wykluczają się — można je wdrożyć incremenalnie.

```
STRATEGIA 1          STRATEGIA 2          STRATEGIA 3
─────────────        ─────────────────    ─────────────────────────
Populate itdoc DB    Keyword Fallback     Embeddings Layer
(raz, offline)       (już zaimplementow.) (opcjonalny, konfigurowalny)
      │                     │                        │
      ▼                     ▼                        ▼
Pełna semantyka      MVP działa teraz     Najlepsza jakość bez danych
standardów/rhythm    z ograniczoną        ze złożonych briefów
                     jakością
```

---

## 3. Strategia 1: Populate itdoc DB

### 3.1 Co wypełnić

Skrypt `scripts/maintenance/populate_itdoc_db.py` powinien wypełnić:

| Tabela | Źródło danych | Metoda wypełnienia |
|--------|--------------|-------------------|
| `standards` | NIST SP 800-53, ISO katalog, oficjalne listy | Ręczny import CSV |
| `document_standards` | Analiza treści szablonów + LLM | LLM-assisted annotation |
| `compliance_regulations` | Regulacje UE (RODO, KSC, NIS2), HIPAA | Ręczny import |
| `rhythm_edges` | Zależności między dokumentami SDLC | Graph analysis szablonów |
| `contracts` | Kontrakty SDLC per dokument | LLM extraction z treści szablonów |
| `document_phases` | Alias do `phases` (już wypełniona) | VIEW lub migration |

### 3.2 Kontrakt skryptu populate

> **Zgodność z ADR-01:** Zapis do `it_doc_matrix.db` jest dozwolony WYŁĄCZNIE dla
> skryptu maintenance `populate_itdoc_db.py`. Runtime aplikacji Warsztat nigdy
> nie pisze do tej bazy (ADR-01, dok.03).

```python
# scripts/maintenance/populate_itdoc_db.py
# ZASADA: populate może TYLKO INSERT do pustych tabel.
# NIE może UPDATE/DELETE/DROP istniejących danych.
# Bezpieczny w re-run: INSERT OR IGNORE.

class ItdocPopulator:
    """
    Wypełnia puste tabele it_doc_matrix.db danymi referencyjnymi.
    Bezpieczny: INSERT OR IGNORE + transakcje atomowe.
    """

    def populate_standards(self, standards_csv_path: Path) -> int:
        """Importuje standardy z CSV. Zwraca liczbę dodanych wierszy."""
        ...

    def create_document_phases_view(self) -> None:
        """
        Tworzy widok document_phases jako alias do tabeli phases.
        Rozwiązuje niezgodność nazw tabel.
        """
        # CREATE VIEW IF NOT EXISTS document_phases AS
        #     SELECT rowid as phase_id, name as phase_name, ordinal FROM phases
        ...

    def populate_rhythm_edges_from_template_analysis(
        self,
        templates_dir: Path,
        dry_run: bool = True
    ) -> list[dict]:
        """
        Analizuje szablony Markdown i próbuje wnioskować zależności
        z sekcji 'Wejścia', 'Wyjścia', 'Poprzedza'.
        dry_run=True: tylko wypisuje, nie zapisuje.
        """
        ...

    def annotate_standards_via_llm(
        self,
        llm_adapter,
        batch_size: int = 50
    ) -> None:
        """
        Dla każdego szablonu (documents) wywołuje LLM aby
        powiązać dokument z listą standardów.
        Zapisuje do document_standards.
        """
        ...
```

### 3.3 Tworzenie widoku `document_phases`

Najprostsze rozwiązanie dla niezgodności `document_phases` vs `phases`:

```sql
-- Uruchom jednorazowo na it_doc_matrix.db (nie modyfikuje tabel!)
CREATE VIEW IF NOT EXISTS document_phases AS
    SELECT
        rowid   AS phase_id,
        name    AS phase_name,
        ordinal AS ordinal
    FROM phases;
```

> To jedyne "zapisy" do it_doc_matrix.db które są dozwolone:
> CREATE VIEW (nie dotyka tabel danych) + INSERT do pustych tabel.
> UPDATE/DELETE/DROP są zawsze zakazane (ADR-01).

---

## 4. Strategia 2: Keyword Fallback (już zaimplementowana)

Opisana szczegółowo w dok.12 §3.6 i dok.09 §3.

**Efektywna jakość mapowania przy keyword fallback:**

| Typ briefu | Jakość mapowania | Wyjaśnienie |
|------------|-----------------|-------------|
| Brief z explicite wymienionymi tytułami dokumentów | ~70% | Jaccard na tytułach |
| Brief techniczny z terminologią branżową | ~50-60% | Częściowe dopasowanie tytułów |
| Brief ogólny ("system CRM dla firmy") | ~30-40% | Mało dopasowań do tytułów |
| Brief ze standardami (ISO, PCI DSS) bez danych w DB | ~40-50%+ (fallback faz) | Phase fallback |

> Keyword fallback to MVP-viable, ale nie production-quality dla złożonych briefów.

---

## 5. Strategia 3: Embeddings Layer

### 5.1 Uzasadnienie

Embeddings rozwiązują fundamentalny problem keyword fallback:
- "Polityka bezpieczeństwa danych" ≈ "Data Security Policy" (semantycznie identyczne, Jaccard = 0)
- "Analiza wymagań biznesowych" ≈ "Business Requirements Document" (Jaccard = 0)

### 5.2 Architektura EmbeddingScorer

```python
# workshop/api/services/embedding_scorer.py

class EmbeddingScorer:
    """
    Semantyczne scorowanie kandydatów przez embeddingi.
    Używane jako UZUPEŁNIENIE Jaccard, nie jako zamiennik.
    Konfigurowane przez EMBEDDING_ENABLED=true.
    """

    def __init__(self, settings: Settings):
        self._model_name = settings.embedding_model
        # Modele obsługiwane:
        # - "paraphrase-multilingual-MiniLM-L12-v2" (lokalny, 420MB, dobry PL+EN)
        # - "text-embedding-3-small" (OpenAI API, płatny, najlepsza jakość)
        # - "nomic-embed-text" (Ollama, lokalny)
        self._model = None  # lazy load
        self._cache: dict[str, np.ndarray] = {}  # doc_uid → vector

    async def compute_similarity(
        self,
        query_text: str,
        candidates: list[ScoredCandidate],
    ) -> list[tuple[ScoredCandidate, float]]:
        """
        Zwraca listę (candidate, cosine_similarity).
        Cosine similarity ∈ [-1.0, 1.0], normaliz. do [0.0, 1.0].
        """
        ...

    async def _get_embedding(self, text: str) -> np.ndarray:
        """Embedding z cache lub obliczony na żądanie."""
        if text in self._cache:
            return self._cache[text]
        # Oblicz embedding (sync → run_in_executor jeśli lokalny model)
        ...

    async def precompute_document_embeddings(
        self,
        connector: ItdocConnector,
        batch_size: int = 100,
    ) -> None:
        """
        Pre-oblicza embeddingi dla wszystkich 7205 dokumentów.
        Uruchamiane jednorazowo przy starcie lub na żądanie.
        Wektory cachowane w PostgreSQL (tabela document_embeddings).
        """
        ...
```

### 5.3 Tabela `document_embeddings` (PostgreSQL)

```sql
-- Alembic migration 0007_embeddings (opcjonalna, gdy EMBEDDING_ENABLED=true)
CREATE TABLE document_embeddings (
    doc_uid         TEXT PRIMARY KEY,        -- doc_id z it_doc_matrix.db (as TEXT)
    doc_title       TEXT NOT NULL,
    model_name      TEXT NOT NULL,           -- nazwa modelu embeddingów
    embedding       FLOAT4[] NOT NULL,       -- wektor (384 dim dla MiniLM, 1536 dla OpenAI)
    computed_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Indeks wektorowy (opcjonalnie pgvector dla ANN search):
-- CREATE INDEX ON document_embeddings USING ivfflat (embedding vector_cosine_ops);
-- (wymaga postgresql-pgvector extension)
```

> Alternatywnie bez pgvector: przechowuj wektory jako FLOAT4[] i używaj numpy cosine_similarity
> na załadowanym zbiorze w pamięci (7205 × 384 dim = ~11 MB — mieści się w RAM).

### 5.4 Integracja z SemanticMapper

```python
# Blending: Jaccard + Embedding (gdy EMBEDDING_ENABLED=true)

async def _score_with_embeddings(
    self,
    brief_text: str,
    scored_candidates: list[ScoredCandidate],
) -> list[ScoredCandidate]:
    """
    Wzbogaca confidence o embedding similarity.
    Blending: final = α * jaccard_conf + (1-α) * embedding_sim
    Domyślnie α = 0.5 (konfigurowalny: EMBEDDING_BLEND_ALPHA)
    """
    if not self._embedding_scorer:
        return scored_candidates  # pass-through gdy wyłączone

    alpha = self._settings.embedding_blend_alpha  # default 0.5

    similarities = await self._embedding_scorer.compute_similarity(
        query_text=brief_text,
        candidates=scored_candidates,
    )

    for candidate, sim in similarities:
        candidate.confidence = round(
            alpha * candidate.confidence + (1 - alpha) * sim,
            3
        )

    return sorted(scored_candidates, key=lambda c: c.confidence, reverse=True)
```

### 5.5 Konfiguracja embeddings

```ini
# .env
EMBEDDING_ENABLED=false                                        # domyślnie wyłączone
EMBEDDING_MODEL=paraphrase-multilingual-MiniLM-L12-v2         # lokalny (rekomendowany)
# EMBEDDING_MODEL=text-embedding-3-small                      # OpenAI (najlepsza jakość)
# EMBEDDING_MODEL=nomic-embed-text                             # Ollama
EMBEDDING_BLEND_ALPHA=0.5                                     # 0.5 = równe wagi Jaccard+Embedding
EMBEDDING_PRECOMPUTE_ON_STARTUP=false                         # oblicz wektory przy starcie?
```

---

## 6. Rekomendowana ścieżka wdrożenia

```
TERAZ (MVP):
  1. Fix error handling (D12 — już gotowe w dok.12 v1.1)
  2. Keyword + Phase fallback (D02 — już gotowe w dok.09 v1.1)
  3. Uruchom CREATE VIEW document_phases (jednorazowo)
  → System działa z ograniczoną jakością mapowania (~50-60%)

KRÓTKI TERMIN (2-4 tygodnie po MVP):
  4. populate_standards.py — import standardów z CSV
  5. Annotate document_standards via LLM (batch job)
  → find_by_standard() zaczyna działać, jakość ~75%

ŚREDNI TERMIN (po stabilizacji):
  6. EMBEDDING_ENABLED=true
  7. Precompute document_embeddings (batch job, ~30 min)
  → Jakość mapowania ~85-90% dla złożonych briefów

DŁUGI TERMIN:
  8. populate_rhythm_edges (wymaga analizy szablonów)
  9. populate_contracts (LLM extraction z treści szablonów)
  → Pełna funkcjonalność WorkPlanner z zależnościami
```

---

## 7. Metryki jakości mapowania

Dla każdego etapu wdrożenia należy mierzyć:

| Metryka | Definicja | Cel MVP | Cel docelowy |
|---------|-----------|---------|-------------|
| `precision@10` | Ile z top-10 wyników jest trafnych | > 50% | > 80% |
| `recall` | Jaki % oczekiwanych dokumentów jest w wynikach | > 40% | > 70% |
| `avg_confidence` | Średnia confidence w MappingResult | > 0.5 | > 0.7 |
| `empty_rate` | % briefów kończących się `total_items=0` | < 20% | < 5% |

**Zestaw testowy:** Przynajmniej 10 reprezentatywnych briefów z oczekiwanymi dokumentami (ground truth) — przygotować przed implementacją jako `tests/fixtures/evaluation_briefs/`.
