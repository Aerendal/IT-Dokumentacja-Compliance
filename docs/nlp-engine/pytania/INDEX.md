---
type: index
title: "INDEX — Mapa warstw silnika NLP"
docs_version: 1.0.0
tags: [index, architektura, zależności, warstwy, NLP-engine]
---

# INDEX — Mapa warstw silnika analizy języka polskiego

## Cel dokumentu

Plik ten jest punktem wejścia do kompletnej dokumentacji pytań implementacyjnych
dla każdej warstwy technicznej silnika NLP.
Zawiera mapę zależności, diagram end-to-end, matrycę "co można budować równolegle"
i definicje kryteriów ukończenia per warstwa.

---

## Diagram end-to-end (ASCII)

```
Wejście: tekst w języku polskim (plik .md, .txt, .xml NKJP)
       |
       v
+------+----------------------------------------------+
|  W0  |  Doc Audit Module (JUŻ ZAIMPLEMENTOWANY)     |
|      |  gap_detector, duplicate_detector,           |
|      |  relation_mapper, doc_auditor → SQLite       |
+------+----------------------------------------------+
       |  (W0 działa niezależnie; W1-W8 wzbogacą go)
       v
+------+----------------------------------------------+
|  W1  |  Fundamenty NLP                              |
|      |  Morfeusz → tokenizacja, lematyzacja, MSD    |
|      |  UDPipe → CoNLL-U, drzewo zależności         |
|      |  NKJP parser (lxml/BeautifulSoup, TEI P5)    |
+------+----------------------------------------------+
       |  DependencyTree + Token stream
       v
+------+----------------------------------------------+
|  W2  |  Role Semantyczne (SRL)                      |
|      |  SemanticMapper: nsubj→AGENT, obj→PATIENT    |
|      |  + INSTRUMENT (narzędnik), LOCATION, TIME    |
|      |  SlowosiecAdapter (WSD dla ról)               |
+------+----------------------------------------------+
       |  EventRoleDict                               |
    +--+--+
    |     |
    v     v
+---+--+ +------+--------------------------------------+
|  W3  | |  W4  |  Baza Grafowa                        |
|  Lex | |      |  Neo4j / ArangoDB                    |
|  zasoby|      |  GraphDatabaseAdapter, generate_cypher|
|  Słowo-| |      |  EventNode, Concept, IS_A, AGENT... |
|  sieć| +------+--------------------------------------+
|  Walenty|       |  Graf wiedzy
|  WSD |       v
|  MWE |  +---+--+--------------------------------------+
+------+  |  W5  |  Silnik Wnioskowania                  |
          |      |  InferenceEngine (Python/Drools)      |
          |      |  StateMatrix, IntentClassifier        |
          |      |  _rule_location, _rule_possession...  |
          +------+--------------------------------------+
                 |  InferenceResult
                 v
          +------+--------------------------------------+
          |  W6  |  Koreferencja                        |
          |      |  CoreferenceResolver                  |
          |      |  Recency Heuristic, ellipsis_recovery |
          |      |  merge_coreferences → W4             |
          +------+--------------------------------------+
                 |  CoreferenceChain
                 v
          +------+--------------------------------------+
          |  W7  |  API i Integracja                    |
          |      |  FastAPI: POST /analyze, /audit      |
          |      |  Apache Thrift RPC                   |
          |      |  CI/CD pipeline                      |
          +------+--------------------------------------+
                 |
                 v
          +------+--------------------------------------+
          |  W8  |  Compliance Audit                    |
          |      |  NKJPBridge (tagi MSD → role)        |
          |      |  EventFrame (6 wymiarów)             |
          |      |  AuditEngine (RISK-01, CONS-02)      |
          |      |  GapAnalysisReport                   |
          +------+--------------------------------------+
```

---

## Matryca zależności

| Warstwa | Wymaga gotowości | Można budować równolegle z |
|---------|-----------------|---------------------------|
| **W0** | — (niezależna) | W1, W2, W3, W4, W5, W6, W7, W8 |
| **W1** | — (fundament) | W0 |
| **W2** | W1 (DependencyTree) | W3 (niezależne ładowanie zasobów) |
| **W3** | — (ładowanie Słowosieci niezależne) | W1, W2 |
| **W4** | W2 (EventRoleDict), W3 (synsety) | W5 (schemat Neo4j osobno) |
| **W5** | W4 (graf), W3 (ontologia) | W6 (koreferencja niezależna) |
| **W6** | W1 (tokeny + morfeusz) | W4, W5 |
| **W7** | W1-W6 (cały pipeline) | — |
| **W8** | W5 (InferenceEngine), W4 (Neo4j) | W7 (API osobno) |

### Kolejność budowania (minimalne prerequisity)

```
Tur 1 (równolegle): W0 + W1 + W3
Tur 2 (po Tur 1):   W2 (wymaga W1) + W4 (wymaga W3)
Tur 3 (po Tur 2):   W5 (wymaga W4) + W6 (wymaga W1)
Tur 4 (po Tur 3):   W8 (wymaga W5) + W7 (wymaga W1-W6)
```

---

## Pliki dokumentacji pytań

| Plik | Warstwa | Status | Liczba pytań |
|------|---------|--------|-------------|
| [W0_doc_audit.md](W0_doc_audit.md) | W0 — Doc Audit | ✅ Zaimplementowana | 42 |
| [W1_fundamenty_nlp.md](W1_fundamenty_nlp.md) | W1 — Fundamenty NLP | ⬜ Planowana | 206 |
| [W2_role_semantyczne.md](W2_role_semantyczne.md) | W2 — Role Semantyczne | ⬜ Planowana | 62 |
| [W3_leksykalne_zasoby.md](W3_leksykalne_zasoby.md) | W3 — Leksykalne Zasoby | ⬜ Planowana | 69 |
| [W4_baza_grafowa.md](W4_baza_grafowa.md) | W4 — Baza Grafowa | ⬜ Planowana | 79 |
| [W5_silnik_wnioskowania.md](W5_silnik_wnioskowania.md) | W5 — Silnik Wnioskowania | ⬜ Planowana | 94 |
| [W6_koreferencja.md](W6_koreferencja.md) | W6 — Koreferencja | ⬜ Planowana | 36 |
| [W7_api_integracja.md](W7_api_integracja.md) | W7 — API Integracja | ⬜ Planowana | 24 |
| [W8_compliance_audit.md](W8_compliance_audit.md) | W8 — Compliance Audit | ⬜ Planowana | 67 |

**Łącznie: 679 unikalnych pytań** (z 714 źródłowych, po deduplikacji)

## Dokumenty dodatkowe

| Plik | Opis |
|------|------|
| [TRACEABILITY_PATHS.md](TRACEABILITY_PATHS.md) | **Ścieżki prześledzenia end-to-end** — 3 kompletne przykłady z łańcuchem przyczynowym W0→W8; mapa "co produkuje co dla kogo i dlaczego" |
| [COVERAGE_MATRIX.md](COVERAGE_MATRIX.md) | Matryca pokrycia 9×9 sekcji, liczby pytań, luki, statusy ADR |
| [RULES_CATALOGUE.md](RULES_CATALOGUE.md) | Formalne definicje reguł ARCH-01a/b, ARCH-06, API-01, SEC-01, DEP-01, RISK-01, CONS-02 |

---

## Kryteria ukończenia per warstwa

| Warstwa | Kryterium "done" |
|---------|-----------------|
| W0 | completeness_score ≥ 0.7, Mutation Score ≥ 60%, 89 testów green |
| W1 | lematyzacja ≥ 95%, LAS ≥ 88%, UAS ≥ 92%, JSONL dataset z NKJP |
| W2 | Precision SRL ≥ 90%, Recall ≥ 85%, oracle dataset 100 zdań |
| W3 | WSD Accuracy ≥ 75%, MWE F1 ≥ 80%, Walenty coverage ≥ 90% |
| W4 | import 1000 węzłów < 5s, brak duplikatów po 3x MERGE, test integracyjny |
| W5 | wnioskowanie < 100ms/zdanie, Precision prawna ≥ 95%, pełny activation trace |
| W6 | Precision koreferencji ≥ 75%, Recall elipsy ≥ 80% |
| W7 | P95 latency < 5s, throughput ≥ 5 req/s, testy kontraktowe OpenAPI |
| W8 | BRIDGE_ERROR rate < 5%, Precision RISK-01 ≥ 95%, pełny audit trail |

---

## Pytania cross-warstwowe (kontrakty interfejsów)

Poniższe pytania dotyczą granic między warstwami i muszą być odpowiedziane
ZANIM warstwa zostanie uznana za gotową do integracji:

### W1 → W2
- Jaki dokładnie jest schemat `DependencyNode` przekazywanego z W1 do W2?
- Czy W2 oczekuje pełnego `DependencyTree` czy tylko listy `(head, dep, deprel)` par?
- Jak W2 obsługuje tokeny, których Morfeusz nie rozpoznał (OOV)?

### W2 → W4
- Jaki jest schemat `EventRoleDict` — które pola są wymagane przez W4?
- Czy W4 akceptuje `EventRoleDict` z brakującymi rolami (np. brak LOCATION)?
- Jak W3 (Słowosieć) wzbogaca `EventRoleDict` przed przekazaniem do W4?

### W4 → W5
- Jak W5 odpytuje Neo4j — czy przez ten sam `GraphDatabaseAdapter` co W4?
- Jak W5 dostaje aktualne fakty z Neo4j dla reguł dedukcji?
- Jak transakcje Neo4j są zarządzane gdy W5 modyfikuje graf?

### W6 → W2 (lub W5)
- Czy W6 modyfikuje `EventRoleDict` z W2 (zastępuje "on" → "Jan") czy tworzy nowy?
- Na którym etapie pipeline W6 działa — przed W2 (lepiej) czy po (prościej)?
- Jak `CoreferenceChain` jest przekazywany do `GraphDatabaseAdapter` (W4)?

### W8 → W7
- Jak `GapAnalysisReport` jest serializowany do JSON dla API W7?
- Czy W8 jest wywoływany synchronicznie przez W7 czy jako background task?
- Jak W7 obsługuje długie audyty W8 (timeout > 30s)?

---

## Słownik pojęć kluczowych

| Pojęcie | Opis | Warstwa |
|---------|------|---------|
| `DependencyTree` | Drzewo składniowe CoNLL-U z W1 | W1 |
| `EventRoleDict` | Słownik ról semantycznych {AGENT, PATIENT...} | W2 |
| `EnrichedToken` | Token z przypisanym synset_id i sensem | W3 |
| `CoreferenceChain` | Lista par (zaimek → antecedens) | W6 |
| `InferenceResult` | Wyniki wnioskowania: fakty, intencja, stan | W5 |
| `EventFrame` | 6-wymiarowy model zdarzenia (compliance) | W8 |
| `BRIDGE_ERROR` | Błąd mapowania tagu NKJP na rolę semantyczną | W8 |
| `StateMatrix` | Deduplikacja i zamrażanie wniosków compliance | W8 |
| `completeness_score` | Ocena kompletności dokumentu [0,1] | W0 |
| `MFS` | Most Frequent Sense — baseline WSD | W3 |
| `LAS` | Labeled Attachment Score — metryka parsera | W1 |
| `UAS` | Unlabeled Attachment Score — metryka parsera | W1 |

---

## Strategia stopniowego rozszerzania systemu

Poniżej zestawienie kluczowych osi ekspansji i gdzie szukać pytań:

| Oś rozszerzania | Gdzie pytania | Kluczowe pytania |
|----------------|---------------|-----------------|
| **Nowe słowa / leksemy** | W3 §Rozszerzalność | `add_lemma()`, OOV detection, hot-add synset |
| **Nowe zbitki wyrazowe (MWE/kolokacje)** | W3 §Rozszerzalność | `learn_mwe(corpus)`, MI score, bigrams → trigrams |
| **Stopniowa kompleksja zdań** | W1 §Rozszerzalność | proste → złożone → prawne, `sentence_complexity_score` |
| **Nowe role semantyczne** | W2 §Rozszerzalność | `register_role()`, BENEFICIARY, MANNER, CAUSE |
| **Nowe domeny (prawna → medyczna → wojskowa)** | W5, W8 §Rozszerzalność | `load_domain()`, konflikty reguł domenowych |
| **Skalowanie grafu (10k → 10M węzłów)** | W4 §Rozszerzalność | progi Neo4j, indeksy, APOC bulk import |
| **Skalowanie API (10 → 1000 req/s)** | W7 §Rozszerzalność | horizontal scaling, circuit breaker, canary deploy |
| **Inkrementalne reguły wnioskowania** | W5 §Rozszerzalność | hot-reload DRL, rule salience, eksplozja reguł |
| **Przyrostowy audyt compliance** | W8 §Rozszerzalność | `incremental_audit()`, diff raportów, historia audytów |

### Zasada: nie burzyć, tylko rozszerzać

> Każda operacja dodania nowego słowa, reguły, domeny lub endpointu MUSI:
> 1. Nie łamać istniejących testów (non-breaking)
> 2. Być pokryta testem regresyjnym przed wdrożeniem
> 3. Być wersjonowana z opisem zmiany (changelog)
> 4. Nie zmieniać istniejących kontraktów danych (backwards-compatible schema)

---

## Niepodjęte decyzje architektoniczne (ADR — do rozstrzygnięcia przed implementacją)

Poniższe pytania muszą mieć **jednoznaczną odpowiedź zanim dana warstwa zostanie uznana za gotową do implementacji**.
Odpowiedź powinna być zapisana w `docs/nlp-engine/ADR/` jako Architecture Decision Record.

| ADR | Pytanie | Dotyczy warstw | Konsekwencja dla pipeline |
|-----|---------|---------------|--------------------------|
| ADR-01 | Czy W3 (WSD) działa **przed** W2 (SRL) czy **wewnątrz** W2? | W2, W3 | Kolejność pipeline: `W1→W3→W2` vs `W1→W2(+W3)` |
| ADR-02 | Czy W6 (koreferencja) działa **przed** W2 czy **po** W2? | W2, W6 | Czy `SemanticMapper` dostaje rozwiązane zaimki czy surowe |
| ADR-03 | Jak W5 (InferenceEngine) dostaje aktualizacje ontologii z W3 — callback, event, hot-reload? | W3, W5 | Czy W5 wymaga restartu po każdej zmianie Słowosieci |
| ADR-04 | Jak W0 (doc audit) podpina się pod lematyzację W1 — interfejs `ILemmatizer` czy konfiguracja? | W0, W1 | Czy W0 może działać bez W1 (degraded mode) |
| ADR-05 | Jaka jest strategia fallback parsera W1 (UDPipe → Concraft → rule-based) — synchroniczna czy async? | W1 | Czy błędy parsowania blokują pipeline czy są obsługiwane gracefully |

> **Ważne:** Każda z tych decyzji wpływa na więcej niż jedną warstwę.
> Podjęcie decyzji w jednym pliku W_x bez aktualizacji sąsiednich warstw **jest błędem implementacyjnym**.
