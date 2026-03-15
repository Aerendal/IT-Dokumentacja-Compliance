---
title: "NLP Engine — Definicje Modułów"
document_class: ARCH
gold_standard: "ISO/IEC 42010:2022"
validation_mode: PRE_PRODUCTION
version: "0.1"
tags:
  - nlp-engine
  - modules
  - compliance-plugins
  - layers
audit_rules:
  - ARCH-01
  - ARCH-06
related_docs:
  - "ARCHITECTURE.md"
  - "INTEGRATION.md"
  - "DOC_AUDIT_MODULE.md"
---

# NLP Engine — Definicje Modułów

> **Uwaga o stanie bieżącym:** Katalog `scripts/nlp/` już istnieje i zawiera działający
> **Moduł Audytu Dokumentacji**. Szczegóły → `DOC_AUDIT_MODULE.md`.
> Ten dokument opisuje docelową strukturę pełnego silnika semantycznego (Fazy 1–5).
> Nowe pliki będą **dodawane** do istniejącego katalogu — nie zastępować istniejących.

## Struktura katalogów (stan bieżący + docelowy)

```
scripts/nlp/                         ← KATALOG ISTNIEJE
│
│  ── Istniejący Moduł Audytu Dokumentacji (✅ ZAIMPLEMENTOWANY) ──
├── __init__.py                      ✅ istnieje
├── text_utils.py                    ✅ preprocessing polskiego tekstu
├── similarity_engine.py             ✅ TF-IDF + cosine (stdlib)
├── gap_detector.py                  ✅ wykrywanie luk kompletności
├── duplicate_detector.py            ✅ klasyfikacja duplikatów
├── relation_mapper.py               ✅ mapowanie relacji między docs
├── doc_auditor.py                   ✅ orkiestrator + SQLite + CLI
├── ddl_audit.sql                    ✅ schemat bazy danych
│
│  ── Planowany Silnik Semantyczny (⬜ Fazy 1–5) ──
├── nlp_engine.py                    ⬜ główny punkt wejścia (Faza 5)
├── context_classifier.py            ⬜ klasyfikacja doc + tryb (Faza 1)
├── nlp_core.py                      ⬜ tokenize→morph→syntax (Faza 1)
├── state_matrix.py                  ⬜ modele Pydantic (Faza 1)
├── cross_reference.py               ⬜ kaskady, dedukcja, freezing (Faza 4)
├── audit_report.py                  ⬜ TraceabilityMatrix + GAP list (Faza 4)
└── plugins/                         ⬜ CompliancePlugins (Faza 3)
    ├── __init__.py
    ├── base.py
    ├── access_control.py
    ├── encryption.py
    ├── logging_audit.py
    ├── data_privacy.py
    └── backup.py
```

**Zasada koegzystencji:** `text_utils.py` i `similarity_engine.py` z istniejącego modułu audytu
będą importowane przez planowany silnik semantyczny — nie ma duplikowania kodu.

## Struktura katalogów (tylko docelowa — pełny obraz po Fazie 5)

```
dokumentacja/
└── scripts/
    └── nlp/                         ← Docelowy stan
        ├── __init__.py
        ├── nlp_engine.py            ← główny punkt wejścia
        ├── context_classifier.py
        ├── nlp_core.py
        ├── state_matrix.py          ← modele Pydantic
        ├── cross_reference.py
        ├── audit_report.py
        ├── plugins/
        │   ├── __init__.py
        │   ├── base.py              ← klasa bazowa CompliancePlugin
        │   ├── access_control.py    ← ISO/IEC 27001 A.9
        │   ├── encryption.py        ← ISO/IEC 27001 A.10
        │   ├── logging_audit.py     ← ISO/IEC 27001 A.12.4
        │   ├── data_privacy.py      ← GDPR / ISO/IEC 29101
        │   └── backup.py            ← ISO/IEC 27001 A.12.3
        └── models/
            ├── udpipe/              ← model UDPipe dla polskiego
            └── spacy/               ← pl_core_news_sm
```

---

## Warstwa 1 — Infrastruktura

### DocumentLoader `[Component: DocumentLoader]`
- **Plik:** `scripts/nlp/nlp_engine.py` (funkcja `load_document`)
- **Obsługa:** `.md`, `.txt`, `.docx` (via python-docx)
- **Open-source:** python-docx, pathlib
- **Uwaga:** PDF i skany (OCR) — poza zakresem MVP, można dodać Apache Tika / Tesseract w Fazie 2+

### TextNormalizer `[Component: TextNormalizer]`
- **Plik:** `scripts/nlp/nlp_engine.py` (funkcja `normalize_text`)
- **Operacje:** usuwanie YAML frontmatter, standaryzacja znaków Unicode, usuwanie Markdown syntax (`##`, `**`, `-`)
- **Implementacja:** własna (proste reguły regex)

---

## Warstwa 2 — Segmentacja

### SentenceSplitter `[Component: SentenceSplitter]`
- **Plik:** `scripts/nlp/nlp_core.py`
- **Open-source:** spaCy (pl pipeline) lub Stanza
- **Problemy polskie:** skróty (`itd.`, `np.`, `ww.`), wyliczenia wielozdaniowe

### Tokenizer `[Component: Tokenizer]`
- **Plik:** `scripts/nlp/nlp_core.py`
- **Open-source:** spaCy `pl_core_news_sm`
- **Problemy polskie:** skróty, liczby, daty, nazwy własne z myślnikami

---

## Warstwa 3 — Morfologia

### MorphologicalAnalyzer `[Component: MorphologicalAnalyzer]`
- **Plik:** `scripts/nlp/nlp_core.py`
- **Open-source:** Morfeusz2
- **Instalacja:** `pip install morfeusz2`
- **Co zwraca:** lemma, POS, cechy fleksyjne (przypadek, liczba, rodzaj, osoba, aspekt)

### Lemmatizer `[Component: Lemmatizer]`
- **Plik:** `scripts/nlp/nlp_core.py` (opakowanie Morfeusz)
- **Priorytet:** Morfeusz → fallback: spaCy lemmatizer

### POSTagger `[Component: POSTagger]`
- **Plik:** `scripts/nlp/nlp_core.py`
- **Open-source:** UDPipe (model `polish-pdb`)
- **Instalacja:** `pip install ufal.udpipe`
- **Model:** pobierz z https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3131

---

## Warstwa 4 — Składnia

### DependencyParser `[Component: DependencyParser]`
- **Plik:** `scripts/nlp/nlp_core.py`
- **Open-source:** UDPipe
- **Wyjście:** drzewo zależności (relacje: nsubj, obj, amod, nmod, aux, neg, ...)
- **Kluczowe dla polskiego:** niezależność od szyku wyrazów

### TenseModeAnalyzer `[Component: TenseModeAnalyzer]`
- **Plik:** `scripts/nlp/nlp_core.py`
- **Implementacja:** własna (reguły oparte o tagi morfologiczne Morfeusz)
- **Mapowanie tagów → tryb:**
  ```
  fut + verb           → FUTURE (plan)
  praet + verb         → PAST   (dowód)
  imp + verb           → IMP    (polecenie)
  "musi/powinien/należy" + verb → OBLIGATION
  ```

### NegationDetector `[Component: NegationDetector]`
- **Plik:** `scripts/nlp/nlp_core.py`
- **Implementacja:** własna (szuka relacji `neg` w drzewie zależności UDPipe)
- **Zakres:** binduje partykułę "nie" / "bez" / "brak" do właściwego węzła czasownikowego

---

## Warstwa 5 — Semantyka

### SemanticRoleLabeler `[Component: SemanticRoleLabeler]`
- **Plik:** `scripts/nlp/nlp_core.py`
- **Implementacja:** własna (reguły oparte o dep_rel + pos z UDPipe)
- **Mapowanie relacji → rola:**
  ```
  nsubj → agent
  obj   → patient
  iobj  → recipient
  obl   → instrument (jeśli narzędnik) / location (jeśli miejscownik)
  advmod czasu → time
  ```

### ContextualDeductor `[Component: ContextualDeductor]`
- **Plik:** `scripts/nlp/cross_reference.py`
- **Cel:** rozwiązywanie polisemii technicznej
- **Algorytm:** analiza sąsiedztwa tokenu (±3 tokeny) w grafie; sprawdzenie czy sąsiedzi należą do słownika domeny A lub B
- **Przykład:** "klucz" obok "szyfrowania/AES/RSA" → EncryptionPlugin; obok "PRIMARY/tabeli/indeksu" → DataPlugin

---

## Warstwa 6 — Compliance Plugins (szczegóły)

### AccessControlPlugin `[Plugin: AccessControl]`
```yaml
standard: "ISO/IEC 27001"
controls: ["A.9.1.1", "A.9.2.1", "A.9.4.2"]
trigger_vocabulary:
  - autoryzacja, uwierzytelnienie, autentykacja
  - hasło, hasła, password
  - RBAC, ACL, uprawnienia, rola, role
  - MFA, 2FA, wieloskładnikowe
  - login, sesja, token, JWT, OAuth, SSO
  - dostęp, kontrola dostępu, zezwolenie

reguły:
  ACC-001: API + brak (auth/token/autoryzacja) → WARNING A.9.4.2
  ACC-002: "dane użytkownika" + brak "uwierzytelnienie" → ERROR A.9.2.1
  ACC-003: POST_EXECUTION + czas_przyszły(MFA) → ERROR "Missing Evidence"
  ACC-004: "hasło" + brak "polityka haseł/złożoność" → WARNING A.9.4.3
  ACC-005: "sesja" + brak "timeout/wygaśnięcie" → WARNING A.9.4.2
```

### EncryptionPlugin `[Plugin: Encryption]`
```yaml
standard: "ISO/IEC 27001"
controls: ["A.10.1.1", "A.10.1.2"]
trigger_vocabulary:
  - szyfrowanie, szyfruje, zaszyfrowane
  - AES, RSA, ECC, ChaCha20
  - TLS, SSL, HTTPS, mTLS
  - certyfikat, klucz kryptograficzny, klucz prywatny
  - at rest, in transit, end-to-end

reguły:
  ENC-001: "dane osobowe/wrażliwe" + brak "szyfrowanie" → ERROR A.10.1.1
  ENC-002: "TLS" bez wersji (≥1.2) → WARNING "Nieokreślona wersja TLS"
  ENC-003: "klucz" + brak "rotacja/wymiana" → WARNING A.10.1.2
  ENC-004: "HTTP" (bez S) + "dane" → ERROR "Nieszyfrowany transport"
```

### LoggingPlugin `[Plugin: Logging]`
```yaml
standard: "ISO/IEC 27001"
controls: ["A.12.4.1", "A.12.4.2", "A.16.1.5"]
trigger_vocabulary:
  - log, logi, logowanie, dziennik, audit trail
  - monitoring, alerting, SIEM
  - zdarzenie, event, incydent
  - retencja, przechowywanie logów, archiwizacja

reguły:
  LOG-001: "log/audit trail" + brak "retencja/okres" → WARNING A.12.4.1
  LOG-002: "incydent" + brak "czas reakcji/RTO/SLA" → WARNING A.16.1.5
  LOG-003: "monitoring" + brak "alerty/powiadomienia" → INFO A.12.4.2
  LOG-004: POST_EXECUTION + "będą logowane" (czas przyszły) → ERROR "Missing Evidence"
```

### DataPrivacyPlugin `[Plugin: DataPrivacy]`
```yaml
standard: "GDPR / ISO/IEC 29101"
controls: ["Art.5", "Art.6", "Art.13", "Art.35"]
trigger_vocabulary:
  - dane osobowe, PII, dane wrażliwe
  - RODO, GDPR, ochrona danych
  - przetwarzanie danych, podmiot danych
  - zgoda, podstawa prawna, legitymacja
  - DPIA, ocena ryzyka, DPO, IOD
  - retencja danych, prawo do usunięcia

reguły:
  PRIV-001: "dane osobowe" + brak "DPIA/ocena wpływu" → ERROR GDPR Art.35
  PRIV-002: "przetwarzanie" + brak "podstawa prawna" → ERROR GDPR Art.6
  PRIV-003: "dane osobowe" + brak "retencja/okres przechowywania" → WARNING GDPR Art.5
  PRIV-004: "transfer danych" + brak "kraj/UE/SCC" → ERROR GDPR Art.46
```

### BackupPlugin `[Plugin: Backup]`
```yaml
standard: "ISO/IEC 27001"
controls: ["A.12.3.1"]
trigger_vocabulary:
  - backup, kopia zapasowa, archiwum
  - odtworzenie, przywracanie, recovery
  - RPO, RTO, disaster recovery
  - BCP, DRP, ciągłość działania

reguły:
  BCK-001: "backup" + brak "częstotliwość/harmonogram" → WARNING A.12.3.1
  BCK-002: "backup" + brak "test odtworzenia/weryfikacja" → WARNING A.12.3.1
  BCK-003: "backup" + brak "szyfrowanie kopii" → INFO A.10.1.1
  BCK-004: "RPO/RTO" + brak wartości liczbowej → WARNING "Nieokreślone cele"
```

---

## Warstwa 7 — Cross-Reference

### CascadeDetector `[Component: CascadeDetector]`
- **Plik:** `scripts/nlp/cross_reference.py`
- **Cel:** sprawdzenie czy finding w jednym pluginie koreluje z findingami w innych
- **Algorytm:**
  1. Zbierz wszystkie findings z tego samego `doc_path`
  2. Jeśli `SECURITY.ERROR` + `DATA.WARNING` → upgrade DATA do ERROR (problem kaskadowy)
  3. Jeśli `SECURITY.WARNING` + Architecture Doc definiuje auth → downgrade do INFO

### ConclusionFreezer `[Component: ConclusionFreezer]`
- **Plik:** `scripts/nlp/cross_reference.py`
- **Cel:** po zamrożeniu decyzji — kolejne przebiegi nie nadpisują
- **Implementacja:** `UPDATE nlp_findings SET locked=1 WHERE finding_id=?`

---

## Warstwa 8 — Raportowanie

### TraceabilityMatrixGenerator `[Component: TraceabilityMatrix]`
- **Plik:** `scripts/nlp/audit_report.py`
- **Format wyjścia:** Markdown tabela + zapis do `nlp_traceability` w SQLite
- **Kolumny:** Sekcja | Wymaganie | Role semantyczne | Standard/Kontrola | Tryb | Status

### GapAnalysisGenerator `[Component: GapAnalysis]`
- **Plik:** `scripts/nlp/audit_report.py`
- **Format wyjścia:** lista `GAP-XXX` z: severity, control_id, sekcja, problem, remediacja
- **Integracja:** wyniki trafiają też do `template_violations` (kolumna `nlp_finding_id`)

---

## Narzędzia pomocnicze

### ComplianceDomainOntology `[Component: DomainOntology]`
- **Plik:** `config/nlp_ontology.yaml`
- **Zawartość:** słowniki per domena (security, data, network, testing, ops)
- **Format:**
  ```yaml
  security:
    synonyms:
      authentication: [uwierzytelnienie, autentykacja, weryfikacja tożsamości]
      encryption: [szyfrowanie, kryptografia, scrambling]
  ```

### NLPOracle `[Component: NLPOracle]`
- **Plik:** `tests/fixtures/nlp_oracle.jsonl`
- **Zawartość:** 50+ zdań z ręcznie opisanymi rolami semantycznymi
- **Format:**
  ```jsonl
  {"text": "API musi wymagać MFA", "mood": "IMP", "tense": "FUTURE", "agent": "API", "action": "wymagać", "patient": "MFA", "expected_plugin": "AccessControl", "expected_severity": "OK"}
  {"text": "dane nie są szyfrowane", "negated": true, "action": "szyfrować", "patient": "dane", "expected_plugin": "Encryption", "expected_severity": "ERROR"}
  ```
