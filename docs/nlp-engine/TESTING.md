---
title: "NLP Engine — Strategia Testowania"
document_class: ARCH
gold_standard: "ISO/IEC 42010:2022"
validation_mode: PRE_PRODUCTION
version: "0.1"
tags:
  - nlp-engine
  - testing
  - tdd
  - oracle
  - coverage
audit_rules:
  - ARCH-01
related_docs:
  - "IMPLEMENTATION_PLAN.md"
  - "../Jak pisać testy.md"
---

# NLP Engine — Strategia Testowania

## Hierarchia testów

Zgodna z `docs/Jak pisać testy.md` — proporcja 60:30:10.

```
Unit (60%)          →  test_nlp_core.py, test_nlp_classifier.py,
                        test_nlp_tense.py, test_nlp_negation.py,
                        test_nlp_srl.py

Integration (30%)   →  test_nlp_plugins.py, test_nlp_pipeline.py,
                        test_nlp_crossref.py, test_nlp_report.py

Contract/Smoke (10%)→  test_nlp_contracts.py, test_nlp_integration.py
```

## Złoty Standard (Oracle)

Zamiast NKJP (ogólny korpus języka polskiego) — własny oracle z zdaniami **z dokumentacji IT compliance**. Plik: `tests/fixtures/nlp_oracle.jsonl`

### Format

```jsonl
{
  "text": "API musi wymagać MFA",
  "doc_class": "SRS",
  "validation_mode": "PRE_PRODUCTION",
  "expected": {
    "tense": "FUTURE",
    "mood": "IMP",
    "negated": false,
    "intent_flags": ["OBLIGATION"],
    "agent": "API",
    "action": "wymagać",
    "patient": "MFA",
    "plugin": "AccessControlPlugin",
    "severity": "OK"
  }
}
```

### Minimalna zawartość oracle (50 zdań)

| Kategoria | Liczba | Przykłady |
|---|---|---|
| Obowiązki (PRE_PROD) | 10 | "musi", "powinien", "należy", "wymaga" |
| Dowody (POST_EXEC) | 10 | "przetestowano", "zweryfikowano", "zostało wdrożone" |
| Negacje | 10 | "nie wymaga", "brak szyfrowania", "nie jest zaszyfrowane" |
| Polisemia | 5 | "klucz" (crypto vs DB), "sesja" (auth vs DB) |
| Missing Evidence | 5 | POST_EXEC + czas przyszły → ERROR |
| Kontrole pozytywne | 10 | Dokumenty prawidłowe → 0 errors |

---

## Testy jednostkowe (60%)

### `tests/test_nlp_classifier.py`

```python
class TestDocumentClassifier:
    def test_srs_detection_by_frontmatter(self): ...
    def test_security_policy_detection_by_keywords(self): ...
    def test_audit_report_detection(self): ...
    def test_unknown_defaults_to_unknown_class(self): ...
    def test_pre_production_mode_from_yaml(self): ...
    def test_post_execution_mode_from_yaml(self): ...
```

### `tests/test_nlp_tense.py`

```python
class TestTenseModeAnalysis:
    # Parametrize po oracle:
    @pytest.mark.parametrize("text,expected_tense,expected_mood", [
        ("musi implementować", "FUTURE", "IMP"),
        ("zostało zaimplementowane", "PAST", "IND"),
        ("jest zaimplementowane", "PRESENT", "IND"),
        ("należy zaimplementować", "FUTURE", "IMP"),
    ])
    def test_tense_detection(self, text, expected_tense, expected_mood): ...

    def test_future_tense_flagged_in_post_execution(self): ...
    def test_past_tense_accepted_in_post_execution(self): ...
```

### `tests/test_nlp_negation.py`

```python
class TestNegationDetection:
    def test_direct_negation_nie_przed_czasownikiem(self): ...
    def test_brak_jako_negacja(self): ...  # "brak szyfrowania"
    def test_bez_jako_negacja(self): ...   # "bez autoryzacji"
    def test_double_negation_resolves_to_positive(self): ...
    def test_negation_in_subordinate_clause(self): ...
```

### `tests/test_nlp_srl.py`

```python
class TestSemanticRoleLabeling:
    def test_simple_svo_extracts_agent_action_patient(self): ...
    def test_instrument_detected_from_narzednik(self): ...
    def test_location_detected_from_miejscownik(self): ...
    def test_passive_voice_swaps_agent_patient(self): ...
    def test_free_word_order_ovo_same_result(self): ...

    # Testy z oracle
    @pytest.mark.parametrize("text,expected_roles", load_oracle("srl"))
    def test_oracle_srl_accuracy(self, text, expected_roles): ...
```

---

## Testy integracyjne (30%)

### `tests/test_nlp_plugins.py`

Każdy plugin testowany na 3 typach dokumentów:

```python
class TestAccessControlPlugin:
    def test_doc_with_full_auth_doc_returns_ok(self, auth_doc_fixture):
        findings = run_plugin(AccessControlPlugin(), auth_doc_fixture)
        assert all(f.severity in ("OK", "INFO") for f in findings)

    def test_doc_missing_mfa_returns_error(self, missing_mfa_fixture):
        findings = run_plugin(AccessControlPlugin(), missing_mfa_fixture)
        errors = [f for f in findings if f.finding_id == "ACC-002"]
        assert len(errors) >= 1

    def test_future_tense_in_post_exec_is_missing_evidence(self, post_exec_fixture):
        findings = run_plugin(AccessControlPlugin(), post_exec_fixture)
        assert any(f.finding_id == "ACC-003" for f in findings)
```

### `tests/test_nlp_pipeline.py`

```python
class TestFullPipeline:
    def test_full_pipeline_security_policy(self, security_policy_fixture):
        findings = run_nlp_audit(security_policy_fixture, mode="PRE_PRODUCTION")
        assert isinstance(findings, list)
        assert all("severity" in f for f in findings)

    def test_pipeline_time_under_30s(self, ten_page_doc_fixture):
        import time
        start = time.time()
        run_nlp_audit(ten_page_doc_fixture)
        assert time.time() - start < 30

    def test_empty_doc_returns_no_findings(self, empty_doc_fixture):
        findings = run_nlp_audit(empty_doc_fixture)
        assert findings == []
```

---

## Testy kontraktowe i smoke (10%)

### `tests/test_nlp_contracts.py`

```python
class TestSchemas:
    def test_state_matrix_serializes_to_json(self): ...
    def test_audit_finding_all_required_fields_present(self): ...
    def test_finding_severity_only_valid_values(self): ...
    def test_token_node_sem_role_from_allowed_set(self): ...

class TestAPIContracts:
    def test_nlp_audit_endpoint_returns_findings_list(self, client): ...
    def test_nlp_audit_requires_auth_token(self, client): ...
    def test_nlp_findings_endpoint_returns_list(self, client): ...
```

### `tests/test_nlp_smoke.py`

```python
def test_morfeusz_available():
    """Smoke: czy Morfeusz jest zainstalowany i działa."""
    import morfeusz2
    m = morfeusz2.Morfeusz()
    results = m.analyse("szyfrowanie")
    assert len(results) > 0

def test_udpipe_model_loadable():
    """Smoke: czy model UDPipe dla polskiego się ładuje."""
    from ufal.udpipe import Model
    model = Model.load("scripts/nlp/models/polish-pdb-ud-2.10-220711.udpipe")
    assert model is not None

def test_spacy_pl_pipeline_available():
    """Smoke: czy spaCy pl_core_news_sm jest zainstalowany."""
    import spacy
    nlp = spacy.load("pl_core_news_sm")
    doc = nlp("Testowe zdanie")
    assert len(doc) > 0
```

---

## Metryki jakości

| Metryka | Cel | Jak mierzyć |
|---|---|---|
| Coverage (moduły NLP) | ≥ 85% | `pytest --cov=scripts/nlp` |
| Mutation Score | ≥ 60% | `mutmut run` |
| Precision (brak FP) | ≥ 90% | Oracle: poprawne docs → 0 errors |
| Recall (wykrycie luk) | ≥ 80% | Oracle: docs z lukami → ≥ 80% luk wykrytych |
| Czas audytu 10 str. | < 30s | `test_pipeline_time_under_30s` |

## Fixtures

```
tests/fixtures/
└── nlp/
    ├── nlp_oracle.jsonl              ← złoty standard (50+ zdań)
    ├── compliance_docs/
    │   ├── ok_security_policy.md     ← poprawny dokument (0 errors)
    │   ├── ok_test_plan.md           ← poprawny plan testów
    │   ├── gap_missing_auth.md       ← brak opisu autoryzacji
    │   ├── gap_missing_encryption.md ← brak szyfrowania
    │   ├── gap_future_tense.md       ← POST_EXEC + czas przyszły
    │   ├── gap_negation.md           ← "dane NIE są szyfrowane"
    │   ├── gap_missing_retention.md  ← brak retencji logów
    │   ├── gap_gdpr_no_dpia.md       ← brak DPIA dla danych osobowych
    │   ├── multi_standard.md         ← jeden doc, wiele standardów
    │   └── ten_page_doc.md           ← duży dokument (test wydajności)
    └── db/
        └── test_nlp.db               ← pre-populated SQLite dla testów API
```

---

## Model matematyczny testowania (IEEE 829 / T = P × O × S × C)

*Sekcja bazuje na `matematyka_testow_fundamenty.md`, `model_matematyczny_testu.md`, `metodologia_myslenia_o_testach.md`.*

### Formuła przestrzeni testu

```
T = P × O × S × C
```

| Wymiar | Symbol | Znaczenie | Przykład dla NLP Engine |
|---|---|---|---|
| Właściwość | **P** | Co system ma gwarantować | Precyzja ekstrakcji ról semantycznych ≥ 90% |
| Wyrocznia | **O** | Jak ocenić pass/fail | Porównanie z `nlp_oracle.jsonl` |
| Zakres | **S** | Ile systemu obejmuje | Jeden predykat vs pełny pipeline |
| Koszt | **C** | Czas pisania + egzekucji | Oracle fixture: 2h; unit: 5 min |

**Właściwości (P) dla NLP Engine:**
- Funkcjonalna: poprawność — `assert finding.action == expected_action`
- Strukturalna: spójność — `assert all(f.severity in VALID_SEVERITIES for f in findings)`
- Własnościowa (invariant): `assert len(run_nlp_audit([])) == 0` (zawsze prawdziwe)
- Wydajnościowa: `assert audit_time < 30s` dla dokumentu 10 stron

---

### Taksonomia wyroczni (Oracle Problem) — 6 typów

| Typ wyroczni | Jak działa | Kiedy użyć w NLP | Ograniczenie |
|---|---|---|---|
| **Specyfikacja** | `assert output == expected_from_docs` | Unit tests dla predykatów modalnych | Wymaga pełnej specyfikacji |
| **Referencja** | `assert new_impl(x) == old_impl(x)` | Refaktor MorphologicalAnalyzer | Stara impl. musi być poprawna |
| **Własnościowy** | `assert invariant(output) == True` | Property-based: puste wejście → puste findings | Nie wykrywa błędów logiki domenowej |
| **Metamorficzny** | `assert f(transform(x)) == relation(f(x))` | NLP: zmiana szyku zdania → te same role semantyczne | Trudny do definiowania |
| **Statystyczny** | `assert abs(output - expected) < ε` | Precision/Recall ≥ 90% na korpusie | Wymaga dużego zbioru danych |
| **Brak wyroczni** | Test zawsze przechodzi | Smoke: `test_morfeusz_available()` | Wykrywa tylko crashe, nie błędy |

> **Kluczowa pułapka:** Testy NLP bez wyroczni (`nlp_oracle.jsonl`) wykryją tylko wyjątki, nie błędy semantyczne. Każdy test IntentClassifier i SRL **musi** mieć wyrocznię specyfikacyjną lub referencyjną.

---

### Metodologia 4-krokowa (P1 → P2 → P3 → P4)

Przed napisaniem każdego testu przejdź przez 4 pytania:

```
P1: Co testuję?
    → Jednostka pracy, granice, zależności zewnętrzne
    → Czy to: funkcja czysta / moduł / kontrakt API / właściwość systemu?

P2: Jaką właściwość weryfikuję?
    → Poprawność / Idempotentność / Deterministyczność / Wydajność / Bezpieczeństwo
    → To pytanie WYBIERA klasę testu i typ wyroczni

P3: Ile testów?
    → V(G) = E - N + 2P  (złożoność cyklomatyczna → liczba ścieżek)
    → BVA: 4n+1  (wartości graniczne)
    → EP: liczba klas równoważności
    → Pairwise: k² × log(n)  (dla kombinatorycznych wejść)

P4: Jaki typ i jak zaprojektować?
    → Wynik P1+P2+P3 deterministycznie wskazuje typ
    → Kolejność: zaprojektuj oracle → dane wejściowe → izolację → asercję
```

**Przykład dla `test_negation_detection`:**
- P1: funkcja `detect_negation(sentence: str) -> bool` — czysta, bez I/O
- P2: poprawność + deterministyczność
- P3: V(G) ≈ 3 (negacja obecna / nieobecna / zagnieżdżona) → minimum 3 testy
- P4: Unit test, wyrocznia specyfikacyjna, dane: frazy z `nlp_oracle.jsonl`

---

### Słownik triggerów — język dokumentacji → typ testu

*Źródło: `Myślenie inżynieryjne o pisaniu testów.md`. To ten sam mechanizm co `trigger_vocabulary` w CompliancePlugins.*

#### R-01: Logika i algorytmy

| Fraza w dokumentacji | Typ testu | Kod |
|---|---|---|
| „Oblicza", „Zwraca wynik dla...", „Transformuje" | Unit test | T-01 |
| „Dla każdego przypadku z...", „W zależności od flag..." | Testy parametryczne / tablice decyzyjne | T-02 |
| „**Zawsze**", „**Nigdy**", „Niezależnie od..." | Testy własnościowe (property-based) | T-03 |

#### R-02: Granice, integracja, architektura

| Fraza | Typ testu | Kod |
|---|---|---|
| „Komunikuje się z...", „Zapisuje do bazy", „Odczytuje z pliku" | Testy integracyjne | T-04 |
| „Format payloadu", „Struktura JSON", „Zgodnie z OpenAPI" | Testy kontraktowe | T-05 |
| „Nie może zależeć od...", „Zabrania się importowania..." | Testy architektury | T-06 |

#### R-03: Czas, stan, środowisko

| Fraza | Typ testu | Kod |
|---|---|---|
| „Nawet jeśli uruchomione wielokrotnie...", „Bezpieczne przy ponowieniu" | Testy idempotentności | T-07 |
| „Równocześnie", „W wielu wątkach", „Przez wielu agentów" | Testy współbieżności | T-08 |
| „Po migracji...", „Stara wersja danych..." | Testy migracji / wstecznej kompatybilności | T-09 |

#### R-04: Awaryjność i bezpieczeństwo

| Fraza | Typ testu | Kod |
|---|---|---|
| „Co jeśli padnie...", „Przy braku sieci...", „Zapewnia fallback" | Testy chaosu / Recovery | T-10 |
| „Tylko dla admina", „Uprawnienia", „Zabezpieczone przed..." | Testy autoryzacji / SAST/DAST | T-11 |
| „Gdy użytkownik wprowadzi błędne...", „Odrzuca niepoprawne..." | Testy negatywne | T-12 |

> **Zastosowanie w NLP Engine:** Uruchom parser triggerów na tekście nowego wymagania systemowego → automatyczne zaproponowanie klasy testu. To jest implementacja `CompliancePlugin.trigger_vocabulary` na wyższym poziomie.

---

*Źródła: `matematyka_testow_fundamenty.md`, `model_matematyczny_testu.md`, `metodologia_myslenia_o_testach.md`, `Myślenie inżynieryjne o pisaniu testów.md`*
