---
title: "NLP Engine — Plan Implementacji"
document_class: PLAN
gold_standard: "ISO/IEC 42010:2022"
validation_mode: PRE_PRODUCTION
version: "0.1"
tags:
  - nlp-engine
  - implementation-plan
  - phases
  - tdd
audit_rules:
  - ARCH-01
related_docs:
  - "ARCHITECTURE.md"
  - "MODULES.md"
  - "TESTING.md"
  - "DOC_AUDIT_MODULE.md"
  - "../Jak pisać testy.md"
---

# NLP Engine — Plan Implementacji

## Stan bieżący (przed Fazą 1)

> **✅ Zaimplementowany: Moduł Audytu Dokumentacji** (`scripts/nlp/`)
>
> Przed uruchomieniem Faz 1–5 powstał działający moduł audytujący dokumentację projektową.
> Jest to oddzielny podsystem, który **nie blokuje** i **nie zastępuje** planowanego silnika
> semantycznego. Szczegóły → `DOC_AUDIT_MODULE.md`.
>
> **Co już istnieje w `scripts/nlp/`:**
> - `text_utils.py` — preprocessing polskiego tekstu (używany też przez przyszły silnik)
> - `similarity_engine.py` — TF-IDF + cosine (używany też przez przyszły silnik)
> - `gap_detector.py`, `duplicate_detector.py`, `relation_mapper.py` — analiza struktury docs
> - `doc_auditor.py` — orkiestrator + CLI + SQLite (`reports/it_doc_audit.db`)
> - 89 testów w `tests/test_nlp_doc_auditor.py` — wszystkie green
>
> **Wyniki live audit:** 10 dokumentów, 179 luk, 8 duplikatów, 83 relacje.

## Zasada budowy

Budujemy **od dołu do góry**: najpierw pipeline lingwistyczny (który można samodzielnie przetestować), potem pluginy compliance (które opierają się na pipeline), na końcu raportowanie i integracja z istniejącym projektem.

Każda faza kończy się działającym, przetestowanym komponentem. Nie przechodzimy do kolejnej fazy bez spełnienia kryterium akceptacji.

---

## Faza 1 — Fundament NLP (Tygodnie 1–3)

**Cel:** Pipeline `tekst → StateMatrix` działający dla pojedynczego zdania.

### Środowisko

```bash
# Nowe zależności do pyproject.toml
pip install morfeusz2 ufal.udpipe spacy
python -m spacy download pl_core_news_sm

# Model UDPipe dla polskiego (~19MB):
# https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-3131
# Zapisać do: scripts/nlp/models/polish-pdb-ud-2.10-220711.udpipe
```

### Zadania

- [x] ~~Stworzyć `scripts/nlp/` z `__init__.py`~~ ✅ Istnieje (doc audit module)
- [x] ~~`text_utils.py` — tokenize, normalize~~ ✅ Istnieje (rozbudowana wersja)
- [ ] Zaimplementować `state_matrix.py` — modele Pydantic: `TokenNode`, `SentenceGraph`, `StateMatrix`
- [ ] Zaimplementować `context_classifier.py` — `DocumentClass` + `ValidationMode` + klasyfikacja przez frontmatter/sygnały
- [ ] Zaimplementować `nlp_core.py` — `morph_analyze()` (Morfeusz), `dep_parse()` (UDPipe)
  - *Uwaga:* `tokenize()` już istnieje w `text_utils.py` — `nlp_core.py` będzie go importować
- [ ] Zaimplementować `TenseModeAnalyzer` — mapowanie tagów morfologicznych → `tense`, `mood`
- [ ] Zaimplementować `NegationDetector` — szukanie relacji `neg` w drzewie UDPipe
- [ ] Napisać `tests/fixtures/nlp_oracle.jsonl` — min. 30 zdań z oczekiwanymi wynikami
- [ ] Napisać `tests/test_nlp_core.py` — min. 30 testów jednostkowych

### Kryterium akceptacji Fazy 1

```python
matrix = get_state_matrix("Moduł autoryzacji musi implementować MFA")
assert matrix.sentences[0].tokens[2].mood == "IMP"
assert matrix.sentences[0].tokens[2].tense == "FUTURE"
assert matrix.sentences[0].tokens[2].negated == False
assert "OBLIGATION" in matrix.sentences[0].intent_flags

matrix2 = get_state_matrix("dane nie są szyfrowane")
assert matrix2.sentences[0].tokens[1].negated == True  # "nie szyfruje"
```

---

## Faza 2 — Semantyka (Tygodnie 4–6)

**Cel:** `StateMatrix` wzbogacona o role semantyczne (agent/action/patient/instrument).

### Zadania

- [ ] Zaimplementować `SemanticRoleLabeler` — mapowanie `dep_rel + pos → sem_role`
- [ ] Zaimplementować `ContextualDeductor` — rozwiązywanie polisemii przez sąsiedztwo
- [ ] Stworzyć `config/nlp_ontology.yaml` — słowniki per domena (security, data, ops)
- [ ] Rozszerzyć `nlp_oracle.jsonl` o oczekiwane role semantyczne
- [ ] Napisać `tests/test_nlp_srl.py` — min. 20 testów dla SRL

### Kryterium akceptacji Fazy 2

```python
result = get_semantic_roles("Jan szyfruje dane klientów kluczem AES-256")
assert result.agent == "Jan"
assert result.action == "szyfruje"
assert result.patient == "dane klientów"
assert result.instrument == "klucz AES-256"

result2 = get_semantic_roles("klucz szyfrowania AES")
assert get_domain_context(result2) == "encryption"  # nie "database"
```

---

## Faza 3 — Compliance Plugins (Tygodnie 7–10)

**Cel:** 5 pluginów MVP pokrywających najczęstsze kontrole ISO 27001 i GDPR.

### Zadania

- [ ] Zaimplementować `plugins/base.py` — klasa abstrakcyjna `CompliancePlugin`
- [ ] Zaimplementować `plugins/access_control.py` — ISO/IEC 27001 A.9 (reguły ACC-001..005)
- [ ] Zaimplementować `plugins/encryption.py` — ISO/IEC 27001 A.10 (reguły ENC-001..004)
- [ ] Zaimplementować `plugins/logging_audit.py` — ISO/IEC 27001 A.12.4 (reguły LOG-001..004)
- [ ] Zaimplementować `plugins/data_privacy.py` — GDPR (reguły PRIV-001..004)
- [ ] Zaimplementować `plugins/backup.py` — ISO/IEC 27001 A.12.3 (reguły BCK-001..004)
- [ ] Stworzyć `tests/fixtures/compliance_docs/` — 10 dokumentów testowych (5 poprawnych, 5 z lukami)
- [ ] Napisać `tests/test_nlp_plugins.py` — min. 10 testów na plugin (50 łącznie)

### Kryterium akceptacji Fazy 3

```
doc_ok.md    (zawiera pełną dokumentację auth) → 0 ERRORs, 0 WARNINGs
doc_gap.md   (brak opisu MFA, brak retencji logów) → ≥2 ERRORs
doc_future.md (tryb POST_EXEC + czas przyszły) → ERROR "Missing Evidence"

Precision ≥ 90% (brak false-positives)
Recall    ≥ 80% (wykrycie prawdziwych luk)
```

---

## Faza 4 — CrossReference + Raport (Tygodnie 11–14)

**Cel:** Spójność między dokumentami + generowanie raportu audytowego.

### Zadania

- [ ] Zaimplementować `cross_reference.py`:
  - `CascadeDetector`
  - `ContextualDeductor` (przeniesienie z Fazy 2)
  - `ConclusionFreezer` (zapis `locked=1` do SQLite)
- [ ] Zaimplementować `audit_report.py`:
  - `TraceabilityMatrixGenerator` → Markdown + SQLite
  - `GapAnalysisGenerator` → lista GAP-XXX
- [ ] Dodać nowe tabele do schematu SQLite (patrz: `INTEGRATION.md`)
- [ ] Napisać `tests/test_nlp_crossref.py` — min. 10 testów
- [ ] Napisać `tests/test_nlp_report.py` — min. 10 testów

### Kryterium akceptacji Fazy 4

```bash
python scripts/nlp/nlp_engine.py --doc tests/fixtures/compliance_docs/doc_gap.md --mode post

# Wyjście:
# GAP-001 [ERROR] ISO/IEC 27001 A.9.2.1 — sekcja 3.2 — Missing Evidence
# GAP-002 [WARNING] ISO/IEC 27001 A.12.4.1 — sekcja 5.1 — brak retencji logów
# TraceabilityMatrix zapisana do: reports/nlp/doc_gap_trace.md

# Czas wykonania dla 10 stron: < 30 sekund
```

---

## Faza 5 — Integracja z projektem (Tygodnie 15–18)

**Cel:** NLP Engine jako pełnoprawna warstwa projektu — CLI, API, CI/CD.

### Zadania

- [ ] Dodać kolumny do istniejących tabel (migracja SQLite)
- [ ] Dodać `nlp_router` do `scripts/api/main.py` (FastAPI)
- [ ] Dodać komendę `nlp-audit` do `itdoc/cli.py`
- [ ] Zaktualizować `Makefile` o target `make nlp-audit`
- [ ] Zaktualizować GitHub Actions workflow o testy NLP
- [ ] Zaktualizować `QUICK_START.md` o nowe funkcjonalności
- [ ] Napisać `tests/test_nlp_integration.py` — min. 10 testów E2E

### Kryterium akceptacji Fazy 5

```bash
# CLI
itdoc nlp-audit docs/security_policy.md --mode post
# → wyświetla findings + zapisuje do SQLite

# API
curl -X POST /nlp/audit \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"path": "docs/policy.md", "mode": "POST_EXECUTION"}'
# → JSON z findings

# Istniejące testy nadal przechodzą
python -m pytest tests/ -q
# ≥ 1720 passed (baseline) + nowe testy NLP
```

---

## Metryki sukcesu (MVP — Faza 3)

| Metryka | Cel |
|---|---|
| Precision (brak false-positives) | ≥ 90% |
| Recall (wykrycie prawdziwych luk) | ≥ 80% |
| Czas audytu dokumentu 10-stronicowego | < 30 sekund |
| Code coverage (moduły NLP) | ≥ 85% |
| Mutation Score | ≥ 60% |
| Testy — liczba | ≥ 150 nowych |

## Zależności zewnętrzne

```toml
# Dodać do pyproject.toml [project.dependencies]:
morfeusz2 = ">=2.0.0"
"ufal.udpipe" = ">=1.3.0"
spacy = ">=3.7.0"

# [project.optional-dependencies.nlp]:
# python-docx = ">=1.1.0"   # dla .docx support
```

## Największe ryzyka

| Ryzyko | Prawdopodobieństwo | Mitigacja |
|---|---|---|
| Morfeusz2 — problemy z instalacją na różnych OS | Średnie | Dockerfile + CI test na Ubuntu |
| Model UDPipe — niedokładność dla tekstu technicznego | Wysokie | Własny oracle + ręczne korekty reguł SRL |
| Rozrost ontologii (300+ pojęć) | Wysokie | Zacząć od 50 pojęć per domena, rozszerzać inkrementalnie |
| False-positives w NegationDetection | Średnie | Dataset 20 par zdań (pozytywne/negatywne) |
