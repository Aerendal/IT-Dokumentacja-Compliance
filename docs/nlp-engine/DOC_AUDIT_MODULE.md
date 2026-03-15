---
title: "NLP Engine — Moduł Audytu Dokumentacji (Zaimplementowany)"
document_class: ARCH
gold_standard: "ISO/IEC 42010:2022"
validation_mode: PRE_PRODUCTION
version: "1.0"
status: "IMPLEMENTED"
tags:
  - nlp-engine
  - doc-audit
  - implemented
  - gap-detection
  - duplicate-detection
  - relation-mapping
audit_rules:
  - ARCH-01
  - ARCH-06
related_docs:
  - "README.md"
  - "MODULES.md"
  - "ARCHITECTURE.md"
  - "IMPLEMENTATION_PLAN.md"
  - "INTEGRATION.md"
---

# NLP Engine — Moduł Audytu Dokumentacji

> **Status: ✅ ZAIMPLEMENTOWANY** — ten dokument opisuje działający kod w `scripts/nlp/`.
> Nie należy go mylić z planowanym silnikiem semantycznym (Fazy 1–5 w `IMPLEMENTATION_PLAN.md`).

---

## Czym jest ten moduł i dlaczego powstał jako pierwszy

Zanim możliwe było zbudowanie silnika semantycznego (który wymaga Morfeusz2, UDPipe, spaCy), potrzebny był sposób na odpowiedź na pytanie: **czy sama dokumentacja projektowa jest wystarczająco dobra, żeby w ogóle mieć co analizować?**

Moduł audytu dokumentacji to **meta-warstwa**: analizuje dokumenty projektowe pod kątem:

| Problem | Co wykrywa | Dlaczego ważne |
|---|---|---|
| **Luki** | Brakujące sekcje, puste nagłówki, brak metadanych | Niekompletna dokumentacja = nieweryfikowalny compliance |
| **Duplikaty** | Ta sama informacja w różnych plikach (exact/extending/thematic/partial) | Duplikaty → rozbieżne wersje → błędne decyzje |
| **Relacje** | Powiązania, zależności, sprzeczności między dokumentami | Brak mapowania relacji = niemożliwa analiza kaskadowa |

Moduł nie wymaga żadnych bibliotek zewnętrznych — działa na czystym Python stdlib. Był budowany równocześnie z projektowaniem silnika semantycznego, bo jego wyniki (jakie dokumenty istnieją, co w nich brakuje, jak są ze sobą powiązane) są **wejściem** dla przyszłego silnika semantycznego.

---

## Miejsce w architekturze

```
scripts/nlp/                          ← Ten moduł żyje tutaj
│
├── text_utils.py         [Warstwa 0] Preprocessing tekstu (fundament)
├── similarity_engine.py  [Warstwa 1] TF-IDF + cosine + Jaccard (math)
├── gap_detector.py       [Warstwa 2] Reguły braków per typ dokumentu
├── duplicate_detector.py [Warstwa 2] Klasyfikacja duplikatów
├── relation_mapper.py    [Warstwa 2] Graf powiązań
├── doc_auditor.py        [Warstwa 3] Orkiestrator + SQLite + CLI
└── ddl_audit.sql         [Warstwa 3] Schemat bazy danych

Planowany silnik semantyczny (Fazy 1–5) będzie DODANY do tego samego katalogu:
├── nlp_engine.py         [Przyszłość - Faza 5]
├── context_classifier.py [Przyszłość - Faza 1]
├── nlp_core.py           [Przyszłość - Faza 1]
├── state_matrix.py       [Przyszłość - Faza 1]
├── cross_reference.py    [Przyszłość - Faza 4]
├── audit_report.py       [Przyszłość - Faza 4]
└── plugins/              [Przyszłość - Faza 3]
```

**Oba podsystemy współdzielą:**
- Ten sam katalog `scripts/nlp/`
- `text_utils.py` — planowany silnik semantyczny też będzie go używał
- `similarity_engine.py` — używany zarówno przez `DuplicateDetector` jak i przyszły `CrossReferenceEngine`

---

## Przepływ danych

```
Katalog docs/
      │
      ▼
  DocAuditor.scan(dir)
      │
      ├──► GapDetector.analyse(doc_path, text)
      │         │
      │         ├── _detect_doc_type() → typ: architecture/testing/integration/...
      │         ├── _check_required_sections() → brakujące sekcje
      │         ├── _check_metadata() → brakujące pola YAML frontmatter
      │         ├── _check_empty_sections() → sekcje bez treści
      │         └── completeness_score() → float 0.0–1.0
      │
      ├──► DuplicateDetector.analyse(corpus)
      │         │
      │         ├── DocumentCorpus.build() → wektory TF-IDF
      │         ├── cosine_pair(i, j) → podobieństwo 0.0–1.0
      │         ├── jaccard_pair(i, j) → podobieństwo 0.0–1.0
      │         └── _classify(cos, jac, heading_overlap) → typ duplikatu
      │
      ├──► RelationMapper.analyse(docs)
      │         │
      │         ├── _find_explicit_links() → markdown [text](path) + [[wiki]]
      │         ├── _find_name_mentions() → nazwy plików w treści
      │         ├── _find_thematic_overlap() → wspólne słowa kluczowe
      │         ├── _find_implications() → wymagania ↔ implementacje
      │         └── _find_extends() → doc A uszczegółowia doc B
      │
      └──► _save_to_db(run_id, findings, duplicates, relations)
                │
                └──► SQLite: it_doc_audit.db
```

---

## Warstwa 0 — `text_utils.py`

**Cel:** Fundament dla wszystkich pozostałych modułów. Normalizuje polski tekst, tokenizuje bez zewnętrznych bibliotek.

### Dlaczego własna implementacja, nie spaCy/NLTK?
Silnik semantyczny (Fazy 1–5) wymaga Morfeusz2 + UDPipe — ale *ten* moduł audytu musiał działać w środowisku bez żadnych zależności. `text_utils.py` to świadomy wybór: prostota kosztem dokładności lingwistycznej.

### Kluczowe funkcje

```python
normalize(text: str) -> str
```
Zamienia polskie znaki diakrytyczne na ASCII, lowercase. Używane przed każdym porównaniem.
```
"Bezpieczeństwo Danych" → "bezpieczenstwo danych"
```
⚠️ **Ważne:** `str.maketrans()` wymaga równiej długości obu ciągów. Tablica mapowania:
`"ąćęłńóśźżĄĆĘŁŃÓŚŹŻ"` → `"acelnoszzACELNOSZZ"` (18 znaków = 18 znaków).

---

```python
tokenize(text: str) -> list[str]
```
Tokenizacja: usuwa Markdown syntax, YAML frontmatter, bloki kodu. Filtruje stopwords (185 polskich słów funkcyjnych). Zwraca tokeny ≥ 3 znaki.
```
"## Sekcja bezpieczeństwa\ndane są szyfrowane" → ["sekcja", "bezpieczenstwo", "dane", "szyfrowane"]
```

---

```python
stem(word: str) -> str
```
Uproszczone stemowanie przez odcięcie polskich sufiksów (`-owanie`, `-ości`, `-ność`, `-ania`, itp.). Nie jest to lematyzacja Morfeusz — to heurystyczne przybliżenie wystarczające dla TF-IDF.
```
"szyfrowanie" → "szyfrow"
"bezpieczeństwo" → "bezpieczenst"
```

---

```python
shingles(text: str, n: int = 4) -> set[str]
```
Zbiór n-gramów znakowych (domyślnie 4-znakowe) z tekstu po normalizacji. Używane przez `DuplicateDetector` do Jaccard similarity — odporne na zmianę szyku słów.
```
"dane" → {"dane", "ane ", ...}  (ze spacjami jako separatorami)
```

---

```python
extract_headings(text: str) -> list[tuple[int, str]]
```
Wyodrębnia nagłówki Markdown z poziomem.
```
"## Bezpieczeństwo\n### TLS" → [(2, "Bezpieczeństwo"), (3, "TLS")]
```

---

```python
extract_links(text: str) -> list[str]
```
Wyodrębnia linki Markdown `[text](path)` i WikiLinki `[[nazwa]]`. Używane przez `RelationMapper` do wykrywania jawnych powiązań.

---

```python
section_text(text: str, heading: str) -> str
```
Zwraca treść sekcji pod danym nagłówkiem (do następnego nagłówka tego samego lub wyższego poziomu).

---

## Warstwa 1 — `similarity_engine.py`

**Cel:** Matematyczna baza dla DuplicateDetector. TF-IDF + cosine implementowane z `collections.Counter` i `math` — bez sklearn, bez numpy.

### `DocumentCorpus`

Centralny obiekt zarządzający wektorami TF-IDF dla kolekcji dokumentów.

```python
corpus = DocumentCorpus()
corpus.add("plik_a.md", "treść dokumentu A")
corpus.add("plik_b.md", "treść dokumentu B")
corpus.build()  # oblicz IDF dla całego korpusu

similarity = corpus.cosine_pair("plik_a.md", "plik_b.md")  # float 0.0–1.0
jaccard_sim = corpus.jaccard_pair("plik_a.md", "plik_b.md")  # float 0.0–1.0
```

### Formuła TF-IDF

```
TF(t, d)  = count(t in d) / len(d)
IDF(t)    = log((1 + N) / (1 + df(t))) + 1   # smooth IDF (jak sklearn)
TF-IDF    = TF × IDF
```

### Cosine similarity (sparse)

Wektory TF-IDF są rzadkie (sparse dicts) — iloczyn skalarny liczony tylko dla wspólnych kluczy. O(|v1 ∩ v2|) zamiast O(dim).

### Dlaczego Jaccard + cosine razem?

- **Cosine** — dobry dla tematycznego podobieństwa (proporcje słów)
- **Jaccard shingle** — dobry dla dosłownych kopii (identyczne fragmenty tekstu)
- Kombinacja obu pozwala odróżnić "to samo napisane inaczej" od "skopiowany fragment"

---

## Warstwa 2a — `gap_detector.py`

**Cel:** Odpowiedź na pytanie: *czy ten dokument zawiera to, co powinien?*

### Wykrywanie typu dokumentu

`_detect_doc_type()` sprawdza dwie rzeczy (w tej kolejności):
1. Nazwę pliku (stem lowercase) — `"architecture"` w nazwie → typ `architecture`
2. Słowa kluczowe w pierwszych 500 znakach tekstu

| Typ | Sygnały w nazwie pliku | Sygnały w treści |
|---|---|---|
| `architecture` | `arch`, `archit` | `architektura`, `komponent`, `diagram` |
| `testing` | `test`, `testy`, `qa` | `plan testów`, `test cases`, `scenariusz` |
| `integration` | `integr`, `api`, `int` | `endpoint`, `interfejs`, `integracja` |
| `modules` | `modul`, `module` | `warstwa`, `klasa`, `funkcja` |
| `readme` | `readme`, `quickstart` | `instalacja`, `uruchomienie`, `how to` |
| `implementation` | `impl`, `implement` | `implementacja`, `kod`, `algorytm` |
| `audit` | `audit`, `compliance` | `compliance`, `audyt`, `standard` |
| `security` | `security`, `sec`, `bezp` | `bezpieczeństwo`, `szyfrowanie`, `autoryzacja` |
| `_default` | (fallback) | — |

### Szablony sekcji

Każdy typ dokumentu ma listę `(wymagana_sekcja, waga)`. Waga 3 = ERROR (krytyczne), waga 2 = WARNING (ważne), waga 1 = INFO (sugerowane).

Przykład dla `architecture`:
```python
("overview", 3),       # ERROR jeśli brak
("components", 3),     # ERROR jeśli brak
("security", 3),       # ERROR jeśli brak
("interfaces", 2),     # WARNING jeśli brak
("context", 2),        # WARNING jeśli brak
("data", 2),           # WARNING jeśli brak
("deployment", 1),     # INFO jeśli brak
```

### Sprawdzanie sekcji pustych

Sekcja jest uznana za "pustą" jeśli po tokenizacji jej treści zostaje 0 tokenów. Typowe przypadki fałszywie-dodatnich:
- Sekcja zawiera wyłącznie bloki kodu (````python ... `````) → tokenize usuwa
- Sekcja zawiera wyłącznie tabelę Markdown → tokenize usuwa
- Root H1 (przed pierwszym H2) — zawsze raportowany jako pusty (prawidłowe zachowanie)

### `completeness_score(findings) -> float`

Formuła logarytmiczna (odporna na "inflację" ostrzeżeń):

```
error_penalty   = min(count_errors * 0.10, 0.50)   # max -50%
warning_penalty = min(count_warnings * 0.02, 0.30) # max -30%
score           = max(0.0, 1.0 - error_penalty - warning_penalty)
```

Przykład: 3 ERRORy + 22 WARNINGi → score = 1.0 - 0.3 - 0.30 = 0.40.

---

## Warstwa 2b — `duplicate_detector.py`

**Cel:** Odpowiedź na pytanie: *czy ta sama informacja jest opisana w kilku miejscach?*

### Progi klasyfikacji

| Typ | Warunek | Znaczenie |
|---|---|---|
| `exact` | Jaccard ≥ 0.75 | Prawie identyczna treść — jeden powinien być usunięty |
| `extending` | cosine ≥ 0.55 AND Jaccard < 0.75 AND heading_overlap < 0.85 | Ta sama informacja, ale jeden rozszerza/uszczegółowia drugi — sprawdź czy nie powinny być połączone |
| `thematic` | cosine ≥ 0.30 | Ten sam temat, różna głębokość — prawdopodobnie docelowo celowe, ale warto znać |
| `partial` | Jaccard ≥ 0.20 AND cosine < 0.30 | Skopiowany fragment tekstu — ryzyko rozbieżności |

### `heading_overlap`

Mierzy jaki procent nagłówków jest wspólny dla obu dokumentów. Niska wartość przy wysokim cosine = oba dokumenty mówią o tym samym, ale z innej perspektywy (→ `extending`).

### API

```python
detector = DuplicateDetector()
# Opcja 1: przez DocumentCorpus
corpus = DocumentCorpus()
corpus.add("a.md", text_a)
corpus.add("b.md", text_b)
corpus.build()
records = detector.analyse(corpus)

# Opcja 2: przez DocAuditor (automatycznie)
auditor = DocAuditor()
run_id = auditor.scan(Path("docs/"))
```

---

## Warstwa 2c — `relation_mapper.py`

**Cel:** Odpowiedź na pytanie: *jak dokumenty są ze sobą powiązane?*

### Typy relacji

| Typ | Jak wykrywany | Skąd → Dokąd |
|---|---|---|
| `explicit_link` | Markdown `[text](ścieżka)` lub `[[WikiLink]]` | Source → Target |
| `name_mention` | Nazwa pliku docelowego (bez `.md`) pojawia się w tekście | Source → Target |
| `thematic_overlap` | ≥ N wspólnych słów kluczowych (TF-IDF top-20) | Bidirectional |
| `implication` | Source zawiera `wymaganie/musi/powinien`, Target zawiera `implementacja/zaimplementowano` | Requirement → Implementation |
| `extends` | Source zawiera sekcje/słowa kluczowe z Target + ma `rozszerza/uszczegółowia` lub dodatkowe sekcje | Extension → Base |

### `find_isolated() -> list[str]`

Zwraca listę dokumentów bez żadnych relacji do innych. Izolowane dokumenty to kandydaci do usunięcia lub wbudowania w inne.

### `build_adjacency() -> dict[str, list[str]]`

Buduje słownik sąsiedztwa grafu dokumentów. Przydatne do wizualizacji i analizy spójności.

---

## Warstwa 3 — `doc_auditor.py`

**Cel:** Orkiestrator — łączy wszystkie warstwy w jeden przebieg, persystuje wyniki, udostępnia CLI.

### Programatyczne API

```python
from scripts.nlp.doc_auditor import DocAuditor
from pathlib import Path

auditor = DocAuditor(db_path="reports/it_doc_audit.db")

# Skanowanie katalogu
run_id = auditor.scan(scan_dir=Path("dokumentacja/docs/"))
# → uruchamia GapDetector, DuplicateDetector, RelationMapper
# → zapisuje do SQLite
# → zwraca UUID przebiegu

# Raport tekstowy
print(auditor.report(run_id))
# → sekcje: GAPS, DUPLICATES, RELATIONS, ISOLATED DOCS

# Lista przebiegów
runs = auditor.list_runs()  # list[dict]
```

### CLI

```bash
# Skan dokumentów
python scripts/nlp/doc_auditor.py scan --dir dokumentacja/docs/
python scripts/nlp/doc_auditor.py scan --dir docs/ --db reports/my_audit.db

# Raport z ostatniego przebiegu
python scripts/nlp/doc_auditor.py report --run-id <UUID>

# Lista wszystkich przebiegów
python scripts/nlp/doc_auditor.py list-runs
```

### Integracja z `compliance_check.py`

```bash
# Przez centralny skrypt compliance
python scripts/compliance_check.py doc-audit --dir dokumentacja/docs/
```

### `_ensure_schema()`

Przy pierwszym uruchomieniu `DocAuditor` automatycznie tworzy schemat bazy danych z `ddl_audit.sql`. Schemat jest idempotentny (`CREATE TABLE IF NOT EXISTS`) — bezpieczne przy wielokrotnym wywołaniu.

---

## Schemat bazy danych (`ddl_audit.sql`)

Wyniki trafiają do **osobnej bazy** `reports/it_doc_audit.db` — nie do głównej `it_doc_matrix.db`. Jest to celowe: audyt dokumentacji to oddzielna domena od matrycy zgodności.

```sql
-- Przebiegi audytu
CREATE TABLE doc_audit_runs (
    run_id      TEXT PRIMARY KEY,          -- UUID
    scan_dir    TEXT NOT NULL,             -- skanowany katalog
    doc_count   INTEGER DEFAULT 0,        -- liczba przeskanowanych plików
    started_at  TEXT,
    finished_at TEXT
);

-- Kompletność każdego dokumentu
CREATE TABLE doc_completeness (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id      TEXT NOT NULL,
    doc_path    TEXT NOT NULL,
    doc_type    TEXT,                      -- wykryty typ (architecture/testing/...)
    score       REAL,                      -- 0.0–1.0
    error_count INTEGER DEFAULT 0,
    warning_count INTEGER DEFAULT 0,
    FOREIGN KEY (run_id) REFERENCES doc_audit_runs(run_id)
);

-- Indywidualne znaleziska (luki)
CREATE TABLE doc_audit_findings (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id      TEXT NOT NULL,
    doc_path    TEXT NOT NULL,
    severity    TEXT NOT NULL,             -- ERROR/WARNING/INFO
    rule        TEXT NOT NULL,             -- missing_section/empty_section/missing_metadata/...
    message     TEXT,
    weight      INTEGER DEFAULT 1,
    FOREIGN KEY (run_id) REFERENCES doc_audit_runs(run_id)
);

-- Wykryte duplikaty
CREATE TABLE doc_duplicates (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id      TEXT NOT NULL,
    doc_a       TEXT NOT NULL,
    doc_b       TEXT NOT NULL,
    dup_type    TEXT NOT NULL,             -- exact/extending/thematic/partial
    cosine_sim  REAL,
    jaccard_sim REAL,
    FOREIGN KEY (run_id) REFERENCES doc_audit_runs(run_id)
);

-- Graf relacji między dokumentami
CREATE TABLE doc_relations (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id      TEXT NOT NULL,
    source_doc  TEXT NOT NULL,
    target_doc  TEXT NOT NULL,
    rel_type    TEXT NOT NULL,             -- explicit_link/name_mention/thematic_overlap/implication/extends
    confidence  REAL DEFAULT 1.0,
    FOREIGN KEY (run_id) REFERENCES doc_audit_runs(run_id)
);
```

---

## Testy — 89 testów w `tests/test_nlp_doc_auditor.py`

Pokrycie:

| Klasa testowa | Zakres | Liczba |
|---|---|---|
| `TestTextUtils` | normalize, tokenize, stem, shingles, extract_headings, extract_links, section_text | ~20 |
| `TestSimilarityEngine` | cosine, jaccard, DocumentCorpus.build(), find_similar() | ~15 |
| `TestGapDetector` | każdy typ dokumentu, brakujące sekcje, puste sekcje, brak metadanych, completeness_score | ~25 |
| `TestDuplicateDetector` | wszystkie 4 typy duplikatów, dokładne progi, brak fałszywych alarmów | ~15 |
| `TestRelationMapper` | wszystkie 5 typów relacji, find_isolated(), build_adjacency() | ~10 |
| `TestDocAuditorIntegration` | pełny przebieg scan + report + SQLite, idempotentność | ~4 |

Uruchomienie:
```bash
python -m pytest tests/test_nlp_doc_auditor.py -v
# 89 passed in 0.47s
```

---

## Wyniki live audit na IT_Dokumentacja

Uruchomione na `dokumentacja/docs/` (10 dokumentów):

```
Docs scanned:   10
Gaps found:     179  (ERROR: ~30, WARNING: ~149)
Duplicates:     8    (thematic: 6, extending: 2)
Relations:      83   (extends: ~60, explicit_link: ~15, thematic_overlap: ~8)
```

**Najważniejsze znaleziska:**
- `NLP_Compliance_Engine_Spec.md` ↔ `IMPLEMENTATION_PLAN.md`: thematic duplicate (cosine=0.54) — stara specyfikacja jednorazowa, którą zastąpił folder `nlp-engine/`; kandydat do usunięcia lub archiwizacji
- Wysokie `empty_section` warnings — większość sekcji używa bloków kodu i tabel jako treści (false-positive, prawidłowe dokumenty)
- 83 relacje `extends` między plikami `nlp-engine/` — poprawne (wszystkie dokumenty wzajemnie się uzupełniają)

---

## Różnica między tym modułem a planowanym silnikiem semantycznym

| Cecha | Doc Audit Module (ten) | Semantic NLP Engine (Fazy 1–5) |
|---|---|---|
| **Status** | ✅ Zaimplementowany | ⬜ Planowany |
| **Analizuje** | Strukturę i metadane dokumentów projektowych | Znaczenie zdań w dokumentach compliance |
| **Wykrywa** | Luki, duplikaty, brakujące sekcje | Brak dowodów, naruszenia kontrolek, False-negations |
| **Biblioteki** | Czyste Python stdlib | Morfeusz2 + UDPipe + spaCy |
| **Kontekst** | "Czy dokument zawiera to co powinien?" | "Czy zdanie to dowód wykonania czy tylko plan?" |
| **Wyjście** | Raport tekstowy + SQLite (`it_doc_audit.db`) | AuditFindings + TraceabilityMatrix + SQLite (`nlp_findings`) |
| **Współdzielone** | `text_utils.py`, `similarity_engine.py` (będą też użyte przez silnik semantyczny) | ← |

**Kolejność budowy jest celowa:** doc audit module dostarcza metadane o strukturze dokumentacji → silnik semantyczny będzie wiedział które dokumenty analizować i czego w nich szukać.
