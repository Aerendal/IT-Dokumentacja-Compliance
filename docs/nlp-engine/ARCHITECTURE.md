---
title: "NLP Engine — Architektura"
document_class: ARCH
gold_standard: "ISO/IEC 42010:2022"
validation_mode: PRE_PRODUCTION
version: "0.1"
tags:
  - nlp-engine
  - architecture
  - pipeline
  - deterministic
audit_rules:
  - ARCH-01
  - ARCH-06
  - API-01
  - SEC-01
related_docs:
  - "README.md"
  - "MODULES.md"
---

# NLP Engine — Architektura

## [ARCH-01] Pipeline (przepływ jednokierunkowy)

```
Dokument (.md / .txt / .docx)
         │
         ▼
┌─────────────────────────────┐
│  [ContextClassifier]        │  Krok 0: czym jest ten dokument?
│  doc_class, validation_mode │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  [NLPCore]                  │  Krok 1: analiza lingwistyczna
│  tokenize → morph → syntax  │
│  → StateMatrix (graf)       │
└──────────────┬──────────────┘
               │  StateMatrix
               ▼
┌─────────────────────────────┐
│  [CompliancePlugins]        │  Krok 2: ewaluacja reguł per standard
│  AccessControl / Encryption │
│  Logging / DataPrivacy /    │
│  Backup / ...               │
└──────────────┬──────────────┘
               │  AuditFindings[]
               ▼
┌─────────────────────────────┐
│  [CrossReferenceEngine]     │  Krok 3: spójność, kaskady, konflikty
│  CascadeDetection           │
│  ContextualDeduction        │
│  ConclusionFreezing         │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  [AuditReportGenerator]     │  Krok 4: raport + macierz pokrycia
│  TraceabilityMatrix         │
│  GapAnalysis                │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│  SQLite: nlp_findings       │  Persystencja wyników
│          nlp_traceability   │
└─────────────────────────────┘
```

## [ARCH-06] Model danych centralnych

### StateMatrix

Centralny obiekt przepływający przez cały pipeline. Przechowuje semantyczny graf przeszukanego dokumentu.

```python
class TokenNode(BaseModel):
    token_id:  int
    text:      str
    lemma:     str               # forma podstawowa (Morfeusz)
    pos:       str               # NOUN/VERB/ADJ/...
    dep_rel:   str               # nsubj/obj/amod/nmod/...
    head_id:   int               # indeks głowy składniowej
    tense:     Optional[str]     # PAST / PRESENT / FUTURE
    mood:      Optional[str]     # IND / IMP / COND
    negated:   bool = False
    sem_role:  Optional[str]     # agent / patient / instrument / location / time

class SentenceGraph(BaseModel):
    sent_id:      int
    raw_text:     str
    tokens:       list[TokenNode]
    intent_flags: list[str]      # OBLIGATION / EVIDENCE / STATE / NEGATION

class StateMatrix(BaseModel):
    doc_path:    str
    doc_class:   DocumentClass
    sentences:   list[SentenceGraph]
    metadata:    dict
```

### AuditFinding

Wynik ewaluacji pluginu compliance.

```python
class AuditFinding(BaseModel):
    finding_id:    str            # np. "ACC-001"
    plugin:        str            # "AccessControlPlugin"
    standard_code: str            # "ISO/IEC 27001"
    control_id:    str            # "A.9.2.1"
    severity:      FindingSeverity  # OK / INFO / WARNING / ERROR
    doc_path:      str
    sentence_id:   int
    raw_text:      str            # zdanie które wyzwoliło finding
    message:       str            # opis problemu
    evidence:      Optional[str]  # jeśli OK — co było dowodem
    remediation:   Optional[str]  # jak naprawić
```

## [ARCH-01] Komponenty — opisy

### ContextClassifier

**Cel:** Ustalenie typu dokumentu i trybu walidacji **zanim** system zacznie go oceniać. Słowo „przetestowano" jest błędem w specyfikacji, ale wymogiem w raporcie powykonawczym.

**Dwa tryby walidacji:**

| Tryb | Co szuka | Czas przyszły |
|---|---|---|
| `PRE_PRODUCTION` | Intencje i plany | ✅ Akceptowalny |
| `POST_EXECUTION` | Twarde dowody wykonania | ❌ `MISSING_EVIDENCE` |

**Klasyfikacja typów dokumentów:**

| Typ | Sygnały |
|---|---|
| `SRS` | "wymagania", "requirements", "shall", "musi", "powinien" |
| `TEST_PLAN` | "plan testów", "test cases", "scenariusz testowy", "przypadki testowe" |
| `AUDIT_REPORT` | "przetestowano", "zweryfikowano", "wyniki testów", "data wykonania" |
| `SECURITY_POLICY` | "polityka bezpieczeństwa", "dostęp", "szyfrowanie", "RBAC", "uprawnienia" |
| `ARCHITECTURE_DOC` | "komponent", "interfejs", "warstwa", "deployment", "diagram" |

---

### NLPCore

**Cel:** Zarządzanie cyklem życia analizy opartej o semantykę i gramatykę, **nie** proste dopasowywanie stringów (RegEx).

**Biblioteki narzędziowe:**

| Biblioteka | Rola | Licencja |
|---|---|---|
| `Morfeusz2` | Lematyzacja + analiza morfologiczna (polska fleksja, 7 przypadków) | GPL |
| `UDPipe` | Parser zależności składniowych + POS tagging | Apache 2.0 |
| `spaCy pl_core_news_sm` | Tokenizacja + NER (osoby, instytucje, daty) | MIT |

**Cztery algorytmy rdzenia:**

**1. DependencyParsing** — konwertuje zdanie do drzewa skierowanego (DAG):
```
"Moduł autoryzacji musi implementować MFA"
→ nsubj(implementować, Moduł)
→ obj(implementować, MFA)
→ aux(implementować, musi)    ← modalność: obowiązek
→ nmod(Moduł, autoryzacji)
```
Niezależne od szyku wyrazów — kluczowe dla języka polskiego (SVO/OVS/VSO dają ten sam wynik).

**2. TenseModeAnalysis** — wykrywa czas gramatyczny i tryb:
```
"musi być zaszyfrowane"       → FUTURE + IMP  → OBLIGATION
"zostało zaszyfrowane"        → PAST           → EVIDENCE
"jest zaszyfrowane"           → PRESENT        → STATE
"nie jest zaszyfrowane"       → PRESENT + NEG  → VIOLATION
```

**3. NegationDetection** — wiąże partykułę „nie" z właściwym czasownikiem:
```
"nie wymaga autoryzacji"  → negated(wymaga) = True  → wynik odwrócony
"wymaga braku autoryzacji"→ negated = False          → normalny
```

**4. SemanticRoleLabeling (SRL)** — mapuje węzły drzewa na role semantyczne:
```
"Jan szyfruje dane klientów kluczem AES-256 w module auth"
→ agent:      Jan
→ action:     szyfruje
→ patient:    dane klientów
→ instrument: klucz AES-256
→ location:   moduł auth
```

---

### CompliancePlugins

**Cel:** Odseparowanie logiki per standard. Każdy plugin = dedykowany słownik intencji + reguły zaspokojenia.

**Struktura pluginu:**
```python
class CompliancePlugin(ABC):
    trigger_vocabulary: list[str]  # słowa aktywujące plugin
    standard_code: str             # "ISO/IEC 27001"
    control_id:    str             # "A.9.2.1"

    def should_activate(self, sentence: SentenceGraph) -> bool: ...
    def evaluate(self, sentence: SentenceGraph,
                 matrix: StateMatrix) -> list[AuditFinding]: ...
```

**Zasada:** moduł analizuje graf zdania. Jeśli intencja się odpali (np. „zapisuje do bazy"), sprawdza czy w powiązanym węźle istnieje gramatycznie poprawne potwierdzenie. System **nigdy** nie akceptuje czasu przyszłego jako dowodu wykonania w trybie `POST_EXECUTION`.

Szczegółowe definicje pluginów → `MODULES.md`.

---

### CrossReferenceEngine

**Cel:** Analiza wielowarstwowa. Testy nie żyją w próżni — system musi widzieć pełen obraz i eliminować fałszywe alarmy.

**Trzy algorytmy:**

**CascadeDetection** — jeśli plugin Security raportuje brak opisu autoryzacji w API, silnik sprawdza czy plugin Data też widzi problem z tymi danymi, i czy Architecture Doc nie definiuje auth gdzie indziej.

**ContextualDeduction** — polisemia techniczna:
```
"klucz" + kontekst "bazy danych"    → PRIMARY KEY → plugin: DataTests
"klucz" + kontekst "szyfrowania"    → klucz kryptograficzny → plugin: EncryptionPlugin
```
Wynik dedukcji jest **zawsze idempotentny** — wielokrotne wywołanie dla tego samego wejścia zwraca identyczny wynik.

**ConclusionFreezing** — po podjęciu decyzji przez silnik reguł, wniosek jest zamrażany w SQLite (`locked=1`) aby zapobiec konfliktom z kolejnymi przebiegami.

---

### AuditReportGenerator

**Wyjście 1 — TraceabilityMatrix:**
```
│ Sekcja │ Wymaganie              │ Role semantyczne               │ Standard/Kontrola   │ Tryb      │ Status           │
│ 3.2    │ "API musi wymagać MFA" │ agent=API, action=wymagać,     │ ISO/IEC 27001 A.9.2 │ POST_EXEC │ ❌ Missing Evid. │
│        │                        │ obj=MFA, mood=IMP              │                     │           │                  │
```

**Wyjście 2 — GapAnalysis:**
```
GAP-001 [ERROR] ISO/IEC 27001 A.9.2.1
  Sekcja 3.2, zdanie #14: "API musi wymagać MFA" (tryb: POSTęEXECUTION)
  Problem: czas przyszły użyty jako dowód wykonania
  Wymagane: zdanie w czasie przeszłym dokonanym + data weryfikacji
  Remediacja: Dodaj sekcję "Wyniki testów autoryzacji" z datą ≥ 2024-01-01
```

## [API-01] Interfejsy zewnętrzne

```
POST /nlp/audit
  Body: {path: str, mode: "PRE_PRODUCTION"|"POST_EXECUTION"}
  Response: {findings: AuditFinding[], summary: dict}

GET  /nlp/findings/{doc_path}
  Response: list[AuditFinding]

GET  /nlp/traceability/{doc_path}
  Response: TraceabilityMatrix (JSON)
```

Integracja z istniejącym `scripts/api/main.py` → dodanie routera `nlp_router` do obecnej aplikacji FastAPI.

## [SEC-01] Model zagrożeń

1. **Wstrzyknięcie przez YAML frontmatter** — mitigacja: walidacja schematu Pydantic przed parsowaniem
2. **Eskalacja przez manipulację `doc_class`** — mitigacja: allowlista `DocumentClass` (enum)
3. **Path traversal w `doc_path`** — mitigacja: normalizacja i sprawdzenie że ścieżka jest wewnątrz projektu
4. **Brak persystencji treści** — dokument analizowany w pamięci, do SQLite trafiają tylko `findings` (nie treść dokumentu)
