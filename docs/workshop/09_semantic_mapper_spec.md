# 09 — Semantic Mapper Spec

**Status:** Draft v1.0  
**Powiązane dokumenty:** 07_llm_adapter_spec, 08_brief_parser_spec, 05_module_interface_contracts, 12_itdoc_integration_spec

---

## 1. Cel i zakres

Semantic Mapper to rdzeń Side 2. Przekształca `ParsedBrief` w `MappingResult` — ustrukturyzowaną listę szablonów dokumentów z ocenami trafności (confidence). Jest to najważniejszy komponent Warsztatu: jakość jego wyników determinuje jakość kosztorysu i planu pracy.

**Pipeline mapowania:**
```
ParsedBrief
    │
    ▼ (1) LLM Entity Extraction
ExtractedEntities {domains, standards, regulations, phases, keywords}
    │
    ▼ (2) itdoc Multi-Query
RawCandidates (do 500 wyników z DB)
    │
    ▼ (3) Jaccard Scoring
ScoredCandidates (0.0–1.0)
    │
    ▼ (4) [Opcjonalnie] LLM Reranking
RankedCandidates
    │
    ▼ (5) Threshold Filter + Deduplication
MappingResult (N pozycji, confidence ≥ threshold)
```

---

## 2. Etap 1: Ekstrakcja encji przez LLM

```python
# Wywołanie przez LLMAdapter (patrz dok. 07)
entities = await llm_adapter.extract_entities(
    text=parsed_brief.text,
    max_tokens=2000
)

# Jeśli brief ma wiele chunków (word_count > 3000):
# Przetwarzaj każdy chunk osobno, scalaj wyniki (union)
if len(parsed_brief.chunks) > 1:
    all_entities = ExtractedEntities(domains=[], standards=[], ...)
    for chunk in parsed_brief.chunks:
        chunk_entities = await llm_adapter.extract_entities(chunk)
        all_entities = merge_entities(all_entities, chunk_entities)
    entities = deduplicate_entities(all_entities)
```

**Definicja `merge_entities()`:**

```python
def merge_entities(a: ExtractedEntities, b: ExtractedEntities) -> ExtractedEntities:
    """Union dwóch ExtractedEntities. Deduplication po wartości (case-insensitive dla str)."""
    def merge_lists(x: list, y: list) -> list:
        seen = {str(v).lower() for v in x}
        return x + [v for v in y if str(v).lower() not in seen]

    return ExtractedEntities(
        domains=merge_lists(a.domains, b.domains),
        standards=merge_lists(a.standards, b.standards),
        regulations=merge_lists(a.regulations, b.regulations),
        phases=sorted(set(a.phases) | set(b.phases)),  # int — set dedup, posortowane
        keywords=merge_lists(a.keywords, b.keywords),
        project_type=a.project_type or b.project_type,
    )
```

**Wzbogacanie encji (normalizacja):**

Po ekstrakcji przez LLM, encje są normalizowane do kodów znanych bibliotece itdoc:

```python
STANDARD_ALIASES = {
    "ISO 27001":       "ISO/IEC 27001",
    "ISO27001":        "ISO/IEC 27001",
    "GDPR":            "RODO",
    "PCI-DSS":         "PCI DSS",
    "NIST CSF":        "NIST CSF 2.0",
    "owasp top 10":    "OWASP Top 10",
    # ... (pełna lista: ~150 aliasów)
}

def normalize_standards(standards: list[str]) -> list[str]:
    return [STANDARD_ALIASES.get(s.lower(), s) for s in standards]
```

---

## 3. Etap 2: Multi-Query do itdoc (z fallbackiem)

Na podstawie `ExtractedEntities` wykonuje się serię zapytań przez `ItdocConnector` (read-only).
**Uwaga:** Aktualna baza może nie mieć tabel standardów/regulacji — pipeline jest odporny na te braki.

```python
async def _query_itdoc(
    self,
    entities: ExtractedEntities,
    connector: ItdocConnector
) -> list[RawCandidate]:
    
    candidates: dict[str, RawCandidate] = {}  # doc_uid → candidate
    
    # ŚCIEŻKA A: Zapytania semantyczne (gdy tabele mapowań istnieją i mają dane)
    
    # Zapytania o standardy
    for standard in entities.standards:
        docs = await connector.find_by_standard(standard)
        for doc in docs:
            _add_candidate(candidates, doc, source=f"standard:{standard}")
    
    # Zapytania o regulacje
    for regulation in entities.regulations:
        docs = await connector.find_by_regulation(regulation)
        for doc in docs:
            _add_candidate(candidates, doc, source=f"regulation:{regulation}")
    
    # Rozszerzenie przez rhythm_downstream
    # Dla każdego znalezionego doc_uid: dodaj jego downstream (głębokość 1)
    top_candidates = sorted(candidates.values(), key=lambda c: c.match_count, reverse=True)[:20]
    for candidate in top_candidates:
        downstream = await connector.rhythm_downstream(candidate.doc_uid, depth=1)
        for doc in downstream:
            _add_candidate(candidates, doc, source=f"rhythm_downstream:{candidate.doc_uid}")
    
    # ŚCIEŻKA B: Keyword fallback (gdy ścieżka A zwróciła < MIN_CANDIDATES wyników)
    # Używane gdy baza nie ma tabel mapowań lub są puste.
    MIN_CANDIDATES = 10
    if len(candidates) < MIN_CANDIDATES:
        # Szukaj po słowach kluczowych z briefu w tytułach dokumentów
        fallback_docs = await connector.find_by_keyword(
            keywords=entities.keywords[:30],
            limit=150,
        )
        for doc in fallback_docs:
            if doc.doc_uid not in candidates:
                _add_candidate(candidates, doc, source="keyword_fallback")
    
    # ŚCIEŻKA C: Phase fallback (gdy ścieżka A+B nadal < MIN_CANDIDATES)
    # Zwraca dokumenty przypisane do faz wyekstrahowanych z briefu.
    # entities.phases zawiera numery 1-based (LLM output); konwertujemy na 0-based dla DB.
    if len(candidates) < MIN_CANDIDATES and entities.phases:
        for phase_id in entities.phases[:5]:  # max 5 faz
            db_phase_id = phase_id - 1  # konwersja 1-based → 0-based (phases.phase_id w DB)
            phase_docs = await connector.get_documents_by_phase(db_phase_id, limit=30)
            for doc in phase_docs:
                if doc.doc_uid not in candidates:
                    _add_candidate(candidates, doc, source=f"phase_fallback:{phase_id}")
    
    return list(candidates.values())
```

**Hierarchia źródeł (wpływa na scoring):**

| Źródło | Prefix | Source score | Jakość dopasowania |
|--------|--------|-------------|--------------------|
| Standard (tabela mapowań) | `standard:` | 0.4 | Wysoka — explicite wymaganie |
| Regulacja (tabela mapowań) | `regulation:` | 0.35 | Wysoka — obowiązkowe |
| Rhythm downstream | `rhythm_downstream:` | 0.25 | Średnia — powiązane |
| Keyword search (title LIKE) | `keyword_fallback` | 0.15 | Niska — przybliżone |
| Phase assignment | `phase_fallback:` | 0.10 | Niska — tylko kontekst |

**Struktura `RawCandidate`:**
```python
@dataclass
class RawCandidate:
    doc_uid:     str
    doc_title:   str
    doc_path:    str | None      # Może być None gdy brak kolumny path w DB
    phase_id:    int
    phase_name:  str
    match_count: int             # ile razy pojawił się w różnych zapytaniach
    sources:     list[str]       # ["standard:PCI_DSS", "keyword_fallback", ...]
    is_required: bool = False    # True jeśli pochodzi z mandatory mapping
```

---

## 4. Etap 3: Jaccard Scoring

> **Uwaga MVP:** Przy domyślnym fallbacku (keyword + phase), sumaryczny confidence
> wynosi 0.2–0.52. Domyślny próg 0.4 oznacza że część kandydatów przejdzie filtr.
> W docelowym stanie bazy (tabele standards/regulations wypełnione) podnieść do 0.6.

> **UWAGA: doc_uid to str(integer) z documents.doc_id — scoring semantyczny
> jest niemożliwy na samym uid. Scoring bazuje na doc_title i match_reason.**

Każdy kandydat otrzymuje score `confidence` na podstawie:
1. **Source score** — ile różnych typów źródeł dopasowało ten dokument
2. **Keyword overlap** — Jaccard similarity między słowami kluczowymi briefu a tytułem/ścieżką dokumentu
3. **Phase match** — czy faza dokumentu należy do wyekstrahowanych faz

```python
def _score_candidate(
    self,
    candidate: RawCandidate,
    entities: ExtractedEntities
) -> float:
    
    # 1. Source score (0.0–0.5)
    unique_source_types = len({s.split(':')[0] for s in candidate.sources})
    # max: standard + regulation + rhythm = 3 typów → 0.5
    source_score = min(unique_source_types / 6.0, 0.5)
    
    # 2. Keyword Jaccard overlap (0.0–0.3)
    # doc_path zawsze None w aktualnym stanie it_doc_matrix.db (brak kolumny 'path')
    # Guard (or "") chroni przed: f-string z None, split na None, LIKE query z None
    doc_words = set(candidate.doc_title.lower().split() +
                    (candidate.doc_path or "").replace('/', ' ').split('_'))
    brief_keywords = set(kw.lower() for kw in entities.keywords)
    
    if doc_words and brief_keywords:
        intersection = len(doc_words & brief_keywords)
        union = len(doc_words | brief_keywords)
        keyword_score = (intersection / union) * 0.3
    else:
        keyword_score = 0.0
    
    # 3. Phase match (0.0–0.2)
    phase_score = 0.2 if candidate.phase_id in entities.phases else 0.0
    
    confidence = source_score + keyword_score + phase_score
    return min(round(confidence, 3), 1.0)


def _compute_match_reason(
    self,
    candidate: RawCandidate,
    entities: ExtractedEntities
) -> str:
    """Generuje czytelny opis uzasadnienia (bez LLM)."""
    parts = []
    standard_sources = [s for s in candidate.sources if s.startswith("standard:")]
    regulation_sources = [s for s in candidate.sources if s.startswith("regulation:")]
    
    if standard_sources:
        stds = ", ".join(s.split(':')[1] for s in standard_sources)
        parts.append(f"wymagany przez standard: {stds}")
    if regulation_sources:
        regs = ", ".join(s.split(':')[1] for s in regulation_sources)
        parts.append(f"wymagany przez regulację: {regs}")
    if candidate.phase_id in entities.phases:
        parts.append(f"należy do fazy {candidate.phase_id} ({candidate.phase_name})")
    if any(s.startswith("rhythm_downstream:") for s in candidate.sources):
        parts.append("wynika z zależności dokumentowej (rhythm)")
    
    return "; ".join(parts) if parts else "dopasowanie słów kluczowych"
```

---

## 5. Etap 4: LLM Reranking (opcjonalny)

LLM Reranking jest włączany gdy:
- Liczba kandydatów > 100 (zbyt wiele dla samego Jaccard)
- LLM_RERANKING_ENABLED=true w konfiguracji

```python
if len(scored_candidates) > 100 and settings.llm_reranking_enabled:
    # Przekaż top-100 (wg Jaccard) do reranking
    top_100 = sorted(scored_candidates, key=lambda c: c.confidence, reverse=True)[:100]
    
    # Skrót briefu (maks. 500 słów) dla promptu
    brief_summary = parsed_brief.chunks[0][:2000]
    
    reranked = await llm_adapter.rerank_mapping(
        brief_text=brief_summary,
        candidates=[MappingCandidate(c.doc_uid, c.doc_title, c.phase_id, c.match_reason)
                    for c in top_100],
        max_candidates=50
    )
    
    # Scalaj score: 0.6 × Jaccard + 0.4 × LLM
    # item.score pochodzi z LLMAdapter.LLMScoredCandidate (dok.07, pole "score")
    # original.confidence pochodzi z SemanticMapper.ScoredCandidate (ten plik, pole "confidence")
    # Dwie różne klasy z różnymi nazwami — LLMScoredCandidate (dok.07) vs ScoredCandidate (ten plik).
    for item in reranked:
        original = next(c for c in top_100 if c.doc_uid == item.doc_uid)
        original.confidence = round(0.6 * original.confidence + 0.4 * item.score, 3)
        original.match_reason += f"; LLM rerank: {item.reason}"
```

---

## 6. Etap 5: Filtracja i deduplikacja

```python
def _filter_and_deduplicate(
    self,
    candidates: list[ScoredCandidate],
    threshold: float,
    max_results: int
) -> list[ScoredCandidate]:
    
    # 1. Filtr confidence
    filtered = [c for c in candidates if c.confidence >= threshold]
    
    # 2. Deduplikacja po doc_uid (zachowaj najwyższe confidence)
    seen = {}
    for c in filtered:
        if c.doc_uid not in seen or c.confidence > seen[c.doc_uid].confidence:
            seen[c.doc_uid] = c
    
    # 3. Sortuj malejąco wg confidence
    deduped = sorted(seen.values(), key=lambda c: c.confidence, reverse=True)
    
    # 4. Ogranicz do max_results
    return deduped[:max_results]
```

---

## 7. Pełny pipeline — klasa SemanticMapper

```python
class SemanticMapper:
    
    def __init__(
        self,
        llm_adapter: BaseLLMAdapter,
        itdoc_connector: ItdocConnector,
        settings: Settings
    ):
        self._llm = llm_adapter
        self._itdoc = itdoc_connector
        self._settings = settings
    
    async def map(
        self,
        brief: ParsedBrief,
        project_id: UUID,   # ← przekazywany z routera (router pobiera z briefs table)
        confidence_threshold: float = 0.4,
        max_results: int = 200,
    ) -> MappingResult:
        
        # 1. Ekstrakcja encji przez LLM
        entities = await self._extract_entities(brief)
        
        # 2. Multi-query do itdoc
        raw_candidates = await self._query_itdoc(entities)
        
        # 3. Scoring Jaccard
        scored = [
            ScoredCandidate(
                doc_uid=c.doc_uid,
                doc_title=c.doc_title,
                phase_id=c.phase_id,
                phase_name=c.phase_name,
                confidence=self._score_candidate(c, entities),
                match_reason=self._compute_match_reason(c, entities),
                match_sources=c.sources,
                is_required=c.is_required,
            )
            for c in raw_candidates
        ]
        
        # 4. Opcjonalny LLM reranking
        if len(scored) > 100 and self._settings.llm_reranking_enabled:
            scored = await self._llm_rerank(brief, scored)
        
        # 5. Filtr + deduplikacja
        final = self._filter_and_deduplicate(scored, confidence_threshold, max_results)
        
        return MappingResult(
            project_id=project_id,   # ← z parametru, nie z brief.project_id
            extracted_entities=entities,
            items=final,
            total_items=len(final),
            avg_confidence=sum(c.confidence for c in final) / len(final) if final else 0.0,
        )
```

---

## 8. Konfiguracja

```ini
# .env
CONFIDENCE_THRESHOLD_DEFAULT=0.4      # min confidence do włączenia w wynikach
# UWAGA: Przy aktualnym stanie bazy (bez tabel mapowań), keyword fallback daje
# confidence max ~0.52. Próg 0.4 jest właściwy dla MVP. Docelowo: 0.6 gdy
# tabele standards/regulations zostaną wypełnione (patrz dok.16).
MAX_MAPPING_RESULTS=200               # max pozycji w MappingResult
LLM_RERANKING_ENABLED=false           # włącz LLM reranking dla dużych zbiorów
RHYTHM_DEPTH=1                        # głębokość ekspansji rhythm_downstream
KEYWORD_FALLBACK_MIN_CANDIDATES=10    # próg poniżej którego włącza się keyword fallback
KEYWORD_FALLBACK_LIMIT=150            # max wyników z find_by_keyword()
```

---

## 9. Przykład wyjścia MappingResult

```json
{
  "id": "9a3f...",
  "brief_id": "7b2c...",
  "llm_model": "gpt-4o",
  "extracted_entities": {
    "domains":    ["fintech", "cloud", "mobile"],
    "standards":  ["PCI DSS", "ISO/IEC 27001"],
    "regulations":["RODO", "KSC"],
    "phases":     [3, 5, 6, 13, 19],
    "keywords":   ["payment gateway", "API", "szyfrowanie", "audyt", "testy penetracyjne"],
    "project_type": "greenfield_saas"
  },
  "items": [
    {
      "doc_uid": "42",
      "doc_title": "Plan audytu bezpieczeństwa",
      "phase_id": 13,
      "phase_name": "Security",
      "confidence": 0.847,
      "match_reason": "wymagany przez standard: PCI DSS, ISO/IEC 27001; należy do fazy 13 (Security)",
      "match_sources": ["standard:PCI_DSS", "standard:ISO/IEC_27001", "keyword:audyt"],
      "is_required": true
    },
    {
      "doc_uid": "118",
      "doc_title": "Rejestr czynności przetwarzania danych",
      "phase_id": 19,
      "phase_name": "Compliance",
      "confidence": 0.762,
      "match_reason": "wymagany przez regulację: RODO, KSC; należy do fazy 19 (Compliance)",
      "match_sources": ["regulation:RODO", "regulation:KSC"],
      "is_required": true
    }
  ],
  "total_items": 87,
  "avg_confidence": 0.694,
  "status": "done"
}
```

---

## 10. Konfigurowalne wagi scoringu per projekt (v2+)

Tabela `project_settings` (dok.04) umożliwia nadpisanie wag per projekt:

```python
# Klucze project_settings:
# "scoring.source_weight"    → float (default 0.5)
# "scoring.keyword_weight"   → float (default 0.3)
# "scoring.phase_weight"     → float (default 0.2)
# "scoring.confidence_threshold" → float (default 0.4)
# "estimation.domain_multiplier.<domain>" → float

async def _get_scoring_config(self, project_id: UUID) -> ScoringConfig:
    """Pobierz konfigurację z project_settings lub użyj defaults."""
    settings = await self.settings_repo.get_project_settings(project_id)
    return ScoringConfig(
        source_weight=settings.get("scoring.source_weight", SOURCE_WEIGHT),
        keyword_weight=settings.get("scoring.keyword_weight", KEYWORD_WEIGHT),
        phase_weight=settings.get("scoring.phase_weight", PHASE_WEIGHT),
    )
```

---

## 11. Query Fallback Strategy — algorytm przejść

Poniższy algorytm definiuje kiedy `_query_itdoc()` przechodzi do następnego poziomu.

### 11.1 Poziomy fallbacku

| Poziom | Metoda | Warunek wejścia | Warunek zatrzymania |
|--------|--------|----------------|---------------------|
| 1 | `find_by_standard(s)` per standard | zawsze | candidates >= MIN_CANDIDATES |
| 2 | `find_by_regulation(r)` per regulacja | zawsze | candidates >= MIN_CANDIDATES |
| 3 | `rhythm_downstream(uid, depth=1)` dla top-20 | po L1+L2 | candidates >= MIN_CANDIDATES |
| 4 | `find_by_keyword(keywords[:30])` | candidates < MIN_CANDIDATES | candidates >= MIN_CANDIDATES |
| 5 | `get_documents_by_phase(db_phase_id)` per faza | candidates < MIN_CANDIDATES | zawsze (max fallback) |

`MIN_CANDIDATES = 10` — poniżej tej wartości pipeline jest nienasycony.

### 11.2 Obsługa pustych tabel (graceful degradation)

```python
async def _query_level(self, method, *args) -> list[DocRef]:
    """Wrapper odporny na OperationalError (brakujące tabele w DB)."""
    try:
        return await method(*args)
    except OperationalError:
        return []  # Tabela nie istnieje → pusty wynik, kontynuuj fallback
```

Wywołanie:
```python
docs = await self._query_level(connector.find_by_standard, standard)
```

### 11.3 Obsługa pustych `ExtractedEntities`

Gdy brief był zbyt krótki lub LLM nie wyekstrahował nic:

```python
if entities.is_empty():
    # Pomiń L1–L3, przejdź od razu do keyword fallback (L4)
    # Jeśli też puste → phase fallback (L5) z entities.phases=[] → pomiń
    # Wynik: candidates mogą być puste → MappingResult.items=[], status="insufficient"
    logger.warning("Empty ExtractedEntities — fallback to keyword+phase only")
```

```python
@dataclass
class ExtractedEntities:
    # ...
    def is_empty(self) -> bool:
        return (not self.standards and not self.regulations
                and not self.keywords and not self.phases)
```

### 11.4 Obsługa `LLMTimeoutError` w ekstrakcji

```python
try:
    entities = await llm_adapter.extract_entities(chunk)
except LLMTimeoutError:
    logger.warning("LLM timeout in extract_entities — using keyword-only fallback")
    # Zbuduj ExtractedEntities tylko ze słów kluczowych (bez LLM)
    entities = _extract_keywords_without_llm(chunk)
    # _extract_keywords_without_llm: simple tokenizer, stopword removal, top-30 terms
```

---

## 12. MappingResult Contract — gwarantowana struktura

Wywołujący (EstimationEngine, WorkPlanner, API) mogą polegać na następujących gwarancjach:

### 12.1 JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "MappingResult",
  "type": "object",
  "required": ["id", "brief_id", "items", "total_items", "status"],
  "properties": {
    "id":           { "type": "string", "format": "uuid" },
    "brief_id":     { "type": "string", "format": "uuid" },
    "llm_model":    { "type": "string" },
    "items": {
      "type": "array",
      "minItems": 0,
      "maxItems": 200,
      "description": "Posortowane malejąco wg confidence. Max 200 (konfig MAX_MAPPING_RESULTS).",
      "items": {
        "type": "object",
        "required": ["doc_uid", "doc_title", "phase_id", "confidence", "match_sources"],
        "properties": {
          "doc_uid":       { "type": "string" },
          "doc_title":     { "type": "string" },
          "phase_id":      { "type": "integer", "minimum": 1, "maximum": 24 },
          "phase_name":    { "type": ["string", "null"] },
          "confidence":    { "type": "number", "minimum": 0, "maximum": 1,
                             "description": "Zaokrąglone do 4 miejsc po przecinku" },
          "match_reason":  { "type": ["string", "null"] },
          "match_sources": { "type": "array", "items": {"type": "string"},
                             "description": "Bez duplikatów (set semantics)" },
          "is_required":   { "type": "boolean", "default": false }
        }
      }
    },
    "total_items":    { "type": "integer", "minimum": 0 },
    "avg_confidence": { "type": ["number", "null"] },
    "status": {
      "type": "string",
      "enum": ["done", "insufficient", "error"],
      "description": "'insufficient' gdy items=[] lub brak danych; 'error' gdy wyjątek LLM"
    }
  }
}
```

### 12.2 Gwarancje implementacyjne

```python
def _build_mapping_result(self, candidates: list[MappingItem], ...) -> MappingResult:
    # 1. Sortowanie malejące po confidence
    candidates.sort(key=lambda x: x.confidence, reverse=True)

    # 2. Zaokrąglenie confidence do 4dp
    for item in candidates:
        item.confidence = round(item.confidence, 4)

    # 3. Deduplikacja match_sources (set semantics, zachowana kolejność)
    for item in candidates:
        seen: set[str] = set()
        deduped = []
        for src in item.match_sources:
            if src not in seen:
                seen.add(src)
                deduped.append(src)
        item.match_sources = deduped

    # 4. Limit do MAX_MAPPING_RESULTS (domyślnie 200)
    items = candidates[:MAX_MAPPING_RESULTS]

    status = "done" if items else "insufficient"
    avg = round(sum(i.confidence for i in items) / len(items), 4) if items else None
    return MappingResult(items=items, total_items=len(items),
                         avg_confidence=avg, status=status)
```
