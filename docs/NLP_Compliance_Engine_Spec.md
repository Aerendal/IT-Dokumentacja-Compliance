---
title: "NLP Compliance Engine — Specyfikacja Implementacyjna"
document_class: ARCH
gold_standard: "ISO/IEC 42010:2022"
version: "0.1"
status: "PRE_IMPLEMENTATION"
source: "Adaptacja z 'NLP i Algorytmy języka Polskiego' (133 pliki)"
tags:
  - nlp
  - compliance
  - audit-engine
  - semantic-analysis
  - polish-nlp
related_docs:
  - "docs/test_scope_matrix.md"
  - "docs/workshop/"
  - "Jak pisać testy.md"
audit_rules:
  - ARCH-01
  - SEC-01
---

# NLP Compliance Engine — Specyfikacja Implementacyjna

## Cel dokumentu

Niniejszy dokument jest **syntetyczną specyfikacją implementacyjną** powstałą przez:

1. Przegląd 133 plików dokumentacji z `NLP i Algorytmy języka Polskiego/`
2. Odrzucenie elementów czysto lingwistycznych (idiomy, przysłowia, pragmatyka ogólna)
3. Zmapowanie wartościowych komponentów do istniejącego projektu IT Dokumentacja Compliance
4. Dodanie brakujących schematów danych i definicji interfejsów

**Zasada adaptacji:** Budujemy nie ogólny silnik NLP — budujemy **deterministyczny audytor dokumentacji IT** zdolny rozróżnić intencję od dowodu, obowiązek od faktu, i wykryć luki compliance bez halucynacji.

---

## Architektura systemu

### Pipeline (jednokierunkowy przepływ danych)

```
Dokument (.md/.txt/.docx)
    ↓
[ContextClassifier]   — czym jest ten dokument?
    ↓
[NLPCore]             — morfologia + składnia + semantyka
    ↓  StateMatrix (graf)
[TestPlugins]         — plugin per domena compliance
    ↓
[CrossReferenceEngine] — spójność, kaskady, konflikty
    ↓
[AuditReportGenerator] — macierz pokrycia + raport luk
```

### Zasady projektowe

- **Deterministyczność:** identyczne wejście → identyczny wynik, zawsze
- **Offline-first:** bez zewnętrznych API, bez LLM, bez chmury
- **Testowalność:** każdy komponent ma własną warstwę testów jednostkowych
- **Rozszerzalność:** nowy standard (np. PCI DSS) = nowy plugin, zero zmian w core

---

## Komponenty — definicje

### 1. ContextClassifier

**Cel:** Ustalenie typu dokumentu zanim system zacznie go oceniać.

**Wejście:** ścieżka pliku + opcjonalne metadane YAML frontmatter

**Wyjście:** `DocumentContext` (patrz: schemat Pydantic poniżej)

**Logika klasyfikacji:**
- `SRS` → szuka: "wymagania", "requirements", "shall", "musi"
- `TEST_PLAN` → szuka: "plan testów", "test cases", "scenariusz"
- `AUDIT_REPORT` → szuka: "przetestowano", "zweryfikowano", "wyniki"
- `SECURITY_POLICY` → szuka: "polityka", "dostęp", "szyfrowanie", "RBAC"
- `ARCHITECTURE_DOC` → szuka: "komponent", "interfejs", "warstwa", "deployment"

**Tryby walidacji:**
- `PRE_PRODUCTION` → weryfikuje intencje i plany (czas przyszły jest OK)
- `POST_EXECUTION` → weryfikuje dowody (czas przyszły = błąd "Missing Evidence")

```python
from pydantic import BaseModel
from enum import Enum
from typing import Optional

class DocumentClass(str, Enum):
    SRS = "SRS"
    TEST_PLAN = "TEST_PLAN"
    AUDIT_REPORT = "AUDIT_REPORT"
    SECURITY_POLICY = "SECURITY_POLICY"
    ARCHITECTURE_DOC = "ARCHITECTURE_DOC"
    UNKNOWN = "UNKNOWN"

class ValidationMode(str, Enum):
    PRE_PRODUCTION = "PRE_PRODUCTION"
    POST_EXECUTION = "POST_EXECUTION"

class DocumentContext(BaseModel):
    doc_path: str
    doc_class: DocumentClass
    validation_mode: ValidationMode
    standard_hints: list[str]   # np. ["ISO/IEC 27001", "GDPR"]
    confidence: float           # pewność klasyfikacji 0.0–1.0
    classifier_notes: Optional[str] = None
```

---

### 2. NLPCore

**Cel:** Przekształcenie tekstu w StateMatrix — graf semantyczny z etykietami gramatycznymi.

**Biblioteki:**
| Biblioteka | Rola | Licencja |
|---|---|---|
| `Morfeusz2` | Lematyzacja, analiza morfologiczna (polska fleksja) | GPL |
| `UDPipe` | Parser zależności składniowych, POS tagging | Apache 2.0 |
| `spaCy` (pl_core_news_sm) | Tokenizacja, NER | MIT |

**Instalacja:**
```bash
pip install morfeusz2 ufal.udpipe spacy
python -m spacy download pl_core_news_sm
# Pobrać model UDPipe dla polskiego:
# https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3131
```

**Algorytmy rdzenia:**

#### 2a. DependencyParsing
Konwertuje zdanie do drzewa skierowanego (DAG).
- Każdy węzeł = token (słowo)
- Każda krawędź = relacja składniowa (nsubj, obj, amod, nmod...)
- Niezależne od szyku wyrazów (SVO/OVS/VSO) — kluczowe dla polskiego

Przykład:
```
"Moduł autoryzacji musi implementować MFA"
→ nsubj(implementować, Moduł)
→ obj(implementować, MFA)
→ aux(implementować, musi)      ← modalność: obowiązek
→ nmod(Moduł, autoryzacji)
```

#### 2b. TenseModeAnalysis
Wykrywa gramatyczny czas i tryb każdego zdania — kluczowe dla compliance:

| Wzorzec | Znaczenie compliance | Przykład |
|---|---|---|
| Czas przyszły + modalny | Obowiązek (plan) | "musi być zaszyfrowane" |
| Czas przeszły dokonany | Dowód (wykonanie) | "zostało zaszyfrowane" |
| Czas teraźniejszy | Stan obecny | "jest zaszyfrowane" |
| Tryb rozkazujący | Zalecenie | "zaszyfruj dane" |

W trybie `POST_EXECUTION`: zdania z czasem przyszłym oznaczone jako `MISSING_EVIDENCE`.

#### 2c. NegationDetection
Wiąże partykułę "nie" z odpowiednim czasownikiem.
- "nie wymaga testu" ≠ "wymaga testu"
- "nie szyfruje danych" ≠ "szyfruje danych"
Wynik: `negated: bool` per węzeł czasownikowy.

#### 2d. SemanticRoleLabeling (SRL)
Mapuje węzły drzewa zależności na role semantyczne:
```
agent     = kto wykonuje (podmiot)
action    = co robi (orzeczenie)
patient   = na czym/kogo (dopełnienie bliższe)
instrument = czym/jak (narzędnik)
location  = gdzie (miejscownik)
time      = kiedy (okolicznik czasu)
```

**Schemat StateMatrix:**
```python
class TokenNode(BaseModel):
    token_id: int
    text: str
    lemma: str
    pos: str              # NOUN, VERB, ADJ...
    dep_rel: str          # nsubj, obj, amod...
    head_id: int
    tense: Optional[str]  # PAST, PRESENT, FUTURE
    mood: Optional[str]   # IND, IMP, COND
    negated: bool = False
    sem_role: Optional[str]  # agent, patient, instrument...

class SentenceGraph(BaseModel):
    sent_id: int
    raw_text: str
    tokens: list[TokenNode]
    intent_flags: list[str]   # OBLIGATION, EVIDENCE, STATE, NEGATION

class StateMatrix(BaseModel):
    doc_path: str
    doc_class: DocumentClass
    sentences: list[SentenceGraph]
    metadata: dict
```

---

### 3. TestPlugins (Compliance Plugins)

**Cel:** Każdy standard/domena = osobny plugin aktywowany przez słownik intencji.

**Struktura pluginu:**
```python
class CompliancePlugin(ABC):
    trigger_vocabulary: list[str]   # słowa które aktywują plugin
    standard_code: str              # np. "ISO/IEC 27001"
    control_id: str                 # np. "A.9.2.1"

    def should_activate(self, sentence: SentenceGraph) -> bool:
        """Sprawdza czy którykolwiek token pasuje do trigger_vocabulary."""

    def evaluate(self, sentence: SentenceGraph, matrix: StateMatrix) -> list[AuditFinding]:
        """Ewaluuje regułę i zwraca listę findings (OK/WARNING/ERROR)."""
```

**Zdefiniowane pluginy (MVP):**

#### Plugin: AccessControlPlugin
```
standard: ISO/IEC 27001 A.9
trigger: ["autoryzacja", "uwierzytelnienie", "hasło", "RBAC", "uprawnienia",
          "MFA", "2FA", "login", "dostęp", "sesja", "token", "JWT", "OAuth"]
reguły:
  - jeśli "API" + brak "autoryzacja/token" → WARNING: "Brak opisu mechanizmu auth"
  - jeśli "dane użytkownika" + brak "uwierzytelnienie" → ERROR: "A.9.2.1 violated"
  - jeśli PRE_PRODUCTION + "musi wymagać MFA" → OK: plan udokumentowany
  - jeśli POST_EXECUTION + "musi wymagać MFA" (czas przyszły) → ERROR: Missing Evidence
```

#### Plugin: EncryptionPlugin
```
standard: ISO/IEC 27001 A.10
trigger: ["szyfrowanie", "AES", "TLS", "SSL", "certyfikat", "klucz kryptograficzny",
          "at rest", "in transit", "HTTPS", "RSA", "SHA"]
reguły:
  - jeśli "dane osobowe" + brak "szyfrowanie" → ERROR: "A.10.1.1 violated"
  - jeśli "TLS" bez wersji → WARNING: "Nie określono wersji TLS (wymagane ≥1.2)"
  - jeśli "klucz" + brak "rotacja" → WARNING: "Brak polityki rotacji kluczy"
```

#### Plugin: LoggingPlugin
```
standard: ISO/IEC 27001 A.12.4
trigger: ["log", "audit trail", "dziennik", "zdarzenie", "monitoring",
          "SIEM", "alert", "incydent", "retencja"]
reguły:
  - jeśli "log" + brak "retencja/okres" → WARNING: "A.12.4.1: brak okresu retencji"
  - jeśli "incydent" + brak "czas reakcji" → WARNING: "A.16.1.5: brak RTO"
```

#### Plugin: DataPrivacyPlugin
```
standard: GDPR / ISO/IEC 29101
trigger: ["dane osobowe", "RODO", "GDPR", "PII", "przetwarzanie danych",
          "zgoda", "podmiot danych", "DPIA", "DPO"]
reguły:
  - jeśli "dane osobowe" + brak "DPIA/ocena" → ERROR: "GDPR Art.35: brak DPIA"
  - jeśli "przetwarzanie" + brak "podstawa prawna" → ERROR: "GDPR Art.6"
```

#### Plugin: BackupPlugin
```
standard: ISO/IEC 27001 A.12.3
trigger: ["backup", "kopia zapasowa", "odtworzenie", "RPO", "RTO",
          "disaster recovery", "BCP", "DRP"]
reguły:
  - jeśli "backup" + brak "częstotliwość" → WARNING: "A.12.3.1: brak harmonogramu"
  - jeśli "backup" + brak "test odtworzenia" → WARNING: "Brak procedury testowania"
```

**Schemat AuditFinding:**
```python
class FindingSeverity(str, Enum):
    OK = "OK"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

class AuditFinding(BaseModel):
    finding_id: str           # unikalny ID np. "ACC-001"
    plugin: str               # "AccessControlPlugin"
    standard_code: str        # "ISO/IEC 27001"
    control_id: str           # "A.9.2.1"
    severity: FindingSeverity
    doc_path: str
    sentence_id: int
    raw_text: str             # zdanie które wyzwoliło finding
    message: str              # opis problemu
    evidence: Optional[str]   # jeśli OK — co było dowodem
    remediation: Optional[str] # jak naprawić
```

---

### 4. CrossReferenceEngine

**Cel:** Wykrywanie niespójności MIĘDZY sekcjami/dokumentami.

**Algorytmy:**

#### CascadeDetection
Jeśli plugin SecurityTests raportuje brak opisu autoryzacji w API, silnik sprawdza:
- Czy plugin DataTests też widzi problem z tymi danymi?
- Czy inny dokument (Architecture Doc) definiuje auth?
→ Eliminacja false-positives: "SecurityTests WARNING ale Architecture Doc zawiera odpowiedź → DOWNGRADE do INFO"

#### ContextualDeduction
Polisemia techniczna ("klucz"):
- W kontekście "bazy danych" → klucz główny (PRIMARY KEY) → plugin: DataTests
- W kontekście "szyfrowania" → klucz kryptograficzny → plugin: EncryptionPlugin
Silnik sprawdza sąsiedztwo w grafie (±3 tokeny) i przypisuje do właściwego pluginu.

#### ConclusionFreezing
Po podjęciu decyzji przez silnik reguł — zapis do SQLite:
```sql
INSERT INTO audit_conclusions (doc_path, sent_id, finding_id, locked, decided_at)
VALUES (?, ?, ?, TRUE, CURRENT_TIMESTAMP);
```
Kolejne przebiegi nie nadpisują zamrożonych wniosków.

---

### 5. AuditReportGenerator

**Wyjście 1: TraceabilityMatrix**

Tabela audytowalna:
```
| Sekcja | Wymaganie (tekst) | Rola semantyczna | Standard/Kontrola | Tryb | Status |
|--------|-------------------|------------------|-------------------|------|--------|
| 3.2    | "API musi wymagać MFA" | agent=API, action=wymagać, obj=MFA | ISO 27001 A.9.2.1 | PRE_PROD | ✅ PLAN |
| 3.2    | "API musi wymagać MFA" | ... | ISO 27001 A.9.2.1 | POST_EXEC | ❌ Missing Evidence |
```

**Wyjście 2: GapAnalysis Report**
```
GAP-001 [ERROR] ISO/IEC 27001 A.9.2.1
Sekcja 3.2 zawiera wymaganie "API musi wymagać MFA" (zdanie #14, czas przyszły).
Tryb POST_EXECUTION wymaga dowodu wykonania (czas przeszły dokonany + data).
Brak zdania potwierdzającego wdrożenie lub logu testowego.
Remediacja: Dodaj sekcję "Wyniki testów autoryzacji" z datą weryfikacji.
```

**Schemat SQLite (tabele):**
```sql
CREATE TABLE nlp_findings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_path TEXT NOT NULL,
    sentence_id INTEGER,
    finding_id TEXT NOT NULL,
    plugin TEXT NOT NULL,
    standard_code TEXT,
    control_id TEXT,
    severity TEXT NOT NULL,   -- OK/INFO/WARNING/ERROR
    raw_text TEXT,
    message TEXT,
    evidence TEXT,
    remediation TEXT,
    locked INTEGER DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE nlp_traceability (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_path TEXT,
    section TEXT,
    requirement_text TEXT,
    semantic_role TEXT,       -- JSON: {agent, action, patient, instrument}
    standard_code TEXT,
    control_id TEXT,
    validation_mode TEXT,
    status TEXT,              -- PLAN_OK / MISSING_EVIDENCE / EVIDENCE_OK
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
```

---

## Fazy implementacji (dostosowane do istniejącego projektu)

### Faza 1 — Fundament (Tygodnie 1–3)
**Cel:** Działający pipeline `tekst → StateMatrix` dla jednego zdania.

Zadania:
- [ ] Zainstalować Morfeusz2 + UDPipe + spaCy pl
- [ ] Zaimplementować `ContextClassifier` (regex + frontmatter YAML)
- [ ] Zaimplementować `Tokenizer` + `MorphologicalAnalyzer` (opakowanie Morfeusz)
- [ ] Zaimplementować `DependencyParser` (opakowanie UDPipe)
- [ ] Zaimplementować `TenseModeAnalysis` (reguły oparte o tagi morfologiczne)
- [ ] Zaimplementować `NegationDetection`
- [ ] Napisać 30+ testów jednostkowych dla każdego modułu
- [ ] **Kryterium akceptacji:** `get_state_matrix("API musi wymagać MFA")` zwraca poprawne TokenNode z `mood=IMP, tense=FUTURE`

### Faza 2 — Semantyka (Tygodnie 4–6)
**Cel:** `StateMatrix` z rolami semantycznymi (agent/action/patient).

Zadania:
- [ ] Zaimplementować `SemanticRoleLabeler` (reguły oparte o dep_rel + pos)
- [ ] Zaimplementować `ContextualDeduction` (polisemia przez sąsiedztwo)
- [ ] Napisać 20+ testów dla SRL z realnymi zdaniami z dokumentacji IT
- [ ] **Kryterium akceptacji:** "Jan szyfruje dane klientów kluczem AES-256" → `{agent: Jan, action: szyfruje, patient: dane, instrument: klucz AES-256}`

### Faza 3 — Pluginy compliance (Tygodnie 7–10)
**Cel:** 5 pluginów MVP pokrywających ISO 27001 A.9, A.10, A.12, GDPR, Backup.

Zadania:
- [ ] Zaimplementować `CompliancePlugin` (klasa bazowa)
- [ ] Zaimplementować `AccessControlPlugin` (ISO 27001 A.9)
- [ ] Zaimplementować `EncryptionPlugin` (ISO 27001 A.10)
- [ ] Zaimplementować `LoggingPlugin` (ISO 27001 A.12.4)
- [ ] Zaimplementować `DataPrivacyPlugin` (GDPR)
- [ ] Zaimplementować `BackupPlugin` (ISO 27001 A.12.3)
- [ ] Napisać 10+ testów na plugin (50+ łącznie)
- [ ] **Kryterium akceptacji:** 10 dokumentów testowych → 0 false-positives, ≥80% recall

### Faza 4 — CrossReference + Raport (Tygodnie 11–14)
**Cel:** Spójność między dokumentami + generowanie raportu.

Zadania:
- [ ] Zaimplementować `CascadeDetection`
- [ ] Zaimplementować `ConclusionFreezing` (zapis do SQLite)
- [ ] Zaimplementować `TraceabilityMatrix` generator (Markdown + SQLite)
- [ ] Zaimplementować `GapAnalysis` generator
- [ ] Integracja z istniejącym `itdoc/` (zapisywanie do `doc_standard_mapping` + `template_violations`)
- [ ] **Kryterium akceptacji:** Pełny audit 10-stronicowego dokumentu ISO 27001 < 30 sekund

### Faza 5 — Integracja z istniejącym projektem (Tygodnie 15–18)
**Cel:** NLP engine jako dodatkowa warstwa nad istniejącym SQLite pipeline.

Zadania:
- [ ] Nowy endpoint FastAPI: `POST /nlp/audit` — przyjmuje dokument, zwraca findings
- [ ] Nowe CLI command: `itdoc nlp-audit <path>` 
- [ ] Migracja `doc_standard_mapping` — dodanie kolumny `nlp_confidence`
- [ ] Pipeline CI/CD — testy NLP w GitHub Actions
- [ ] **Kryterium akceptacji:** `itdoc nlp-audit docs/security_policy.md` → JSON z findings w < 60s

---

## Integracja z istniejącym projektem

### Gdzie NLP zastępuje/rozszerza obecne mechanizmy

| Obecny mechanizm | Ograniczenie | Zastąpienie NLP |
|---|---|---|
| Keyword matching w `map_standards_to_docs.py` | "TLS" znajdzie też "ATLAS" | SRL + kontekst → tylko prawdziwe użycia |
| `confidence` ustalany heurystycznie | Brak podstawy lingwistycznej | `confidence` z SRL + TenseModeAnalysis |
| Brak detekcji "obowiązku vs dowodu" | Specyfikacja i raport traktowane jednakowo | TenseModeAnalysis → `validation_mode` |
| `template_violations` tylko schema | Nie sprawdza treści | GapAnalysis sprawdza treść zdań |

### Nowe kolumny w istniejących tabelach
```sql
ALTER TABLE doc_standard_mapping ADD COLUMN nlp_confidence REAL;
ALTER TABLE doc_standard_mapping ADD COLUMN nlp_evidence TEXT;   -- wyekstrahowane zdanie-dowód
ALTER TABLE doc_standard_mapping ADD COLUMN validation_mode TEXT;

ALTER TABLE template_violations ADD COLUMN nlp_finding_id TEXT;  -- powiązanie z nlp_findings
ALTER TABLE template_violations ADD COLUMN sentence_id INTEGER;
ALTER TABLE template_violations ADD COLUMN raw_text TEXT;
```

---

## Wymagania zewnętrzne

### Zależności Python
```toml
# Dodać do pyproject.toml [project.dependencies]
morfeusz2 = ">=2.0.0"
"ufal.udpipe" = ">=1.3.0"
spacy = ">=3.7.0"

# Model spaCy:
# python -m spacy download pl_core_news_sm
```

### Modele do pobrania (offline)
```
UDPipe model (Polish):
  URL: https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3131
  Plik: polish-pdb-ud-2.10-220711.udpipe (~19MB)
  Miejsce: models/udpipe/

Morfeusz2 słownik:
  Instalowany razem z pip install morfeusz2
  (wbudowany w pakiet)
```

---

## Strategia testowania

Zgodna z `Jak pisać testy.md` — hierarchia Unit→Integration→Contract→Smoke, proporcja 60:30:10.

### Złoty Standard (Oracle)
Zestaw 50 zdań z dokumentacji IT z ręcznie opisanymi rolami semantycznymi — plik `tests/fixtures/nlp_oracle.jsonl`:
```jsonl
{"text": "API musi wymagać MFA", "expected": {"mood": "IMP", "tense": "FUTURE", "agent": "API", "action": "wymagać", "patient": "MFA"}}
{"text": "Dane zostały zaszyfrowane kluczem AES-256", "expected": {"tense": "PAST", "action": "zaszyfrowane", "patient": "Dane", "instrument": "klucz AES-256"}}
```

### Testy jednostkowe (60%)
- `test_nlp_classifier.py` — DocumentClass detection per wzorzec
- `test_nlp_tense.py` — TenseModeAnalysis na 30+ zdaniach
- `test_nlp_negation.py` — NegationDetection (20 par zdań)
- `test_nlp_srl.py` — SemanticRoleLabeling vs oracle

### Testy integracyjne (30%)
- `test_nlp_plugins.py` — każdy plugin na 10 dokumentach testowych
- `test_nlp_pipeline.py` — pełny pipeline text→StateMatrix→findings
- `test_nlp_crossref.py` — CascadeDetection na parach dokumentów

### Testy kontraktowe (10%)
- `test_nlp_contracts.py` — StateMatrix schema validation, AuditFinding schema, API contracts

---

## Co z dokumentacji NLP zostało pominięte i dlaczego

| Komponent | Powód pominięcia |
|---|---|
| IdiomDetector, ProverbParser | Dokumentacja IT nie używa idiomów/przysłów |
| Coreference Resolution (pełne) | Docs IT używają nazw jawnych, nie zaimków; prostsze heurystyki wystarczą |
| Pragmatic module (ironia, sarkazm) | Dokumentacja compliance to język formalny |
| General World Knowledge | Potrzebna tylko ontologia domenowa IT/compliance |
| Drools (Java rule engine) | Zastąpiony Python-native reguły w pluginach — prostszy maintenance |
| Neo4j/ArangoDB | Zastąpiony SQLite (StateMatrix w pamięci, wyniki do SQLite) — mniejszy footprint |
| NKJP corpus | Zastąpiony własnym oracle z zdań IT compliance (50–200 przykładów wystarczy) |

---

## Metryki sukcesu (MVP — Faza 3)

| Metryka | Cel |
|---|---|
| Precision (brak false-positives) | ≥ 90% |
| Recall (wykrycie prawdziwych luk) | ≥ 80% |
| Czas audytu 10-stronicowego dokumentu | < 30 sekund |
| Code coverage (testy NLP) | ≥ 85% |
| Mutation Score | ≥ 60% |
