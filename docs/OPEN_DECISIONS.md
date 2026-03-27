# OPEN_DECISIONS.md

## Cel dokumentu

Ten dokument zawiera wyłącznie te tematy, które nie zostały jeszcze formalnie domknięte,
są świadomie pozostawione na później i mają wpływ na dalszy rozwój repo.

## Zasady użycia

- Wpisuj tu tylko decyzje architektoniczne, świadomie otwarte ryzyka, zależności zewnętrzne.
- Każdy wpis musi mieć: ID, status, właściciela, zakres wpływu, warunek zamknięcia.
- Gdy decyzja zostanie zamknięta — przenieś ją do sekcji ZAMKNIĘTE DECYZJE.

Statusy: `OPEN` | `IN_PROGRESS` | `BLOCKED` | `DEFERRED` | `CLOSED`

---

# OTWARTE DECYZJE

## OD-001 — Oficjalny model hooków developerskich

**Status:** `OPEN`  
**Priorytet:** Wysoki  
**Właściciel:** `________________________________`  
**Obszar:** Toolchain / Developer workflow / Onboarding

### Opis
Repo korzysta z własnego modelu hooków (`scripts/install_hooks.sh`, custom `.git/hooks/pre-commit`).
Nie jest używany standardowy framework `pre-commit` oparty o `.pre-commit-config.yaml`.

### Opcje
- **A:** Pozostawić custom hook jako rozwiązanie docelowe.
- **B:** Przenieść repo na standardowy `pre-commit`.

### Rekomendacja
- Wąski, kontrolowany zespół → custom hook akceptowalny.
- Szerokie udostępnienie / contribuorzy z zewnątrz → standardowy `pre-commit` czytelniejszy.

### Warunek zamknięcia
Jeden wybrany model, dokumentacja spójna, onboarding zgodny z wyborem.

**Data przeglądu:** `________________________________`  
**Decyzja końcowa:** `________________________________`

---

## OD-002 — Status i źródło `legacy-runtime` DB

**Status:** `CLOSED`  
**Priorytet:** Wysoki  
**Właściciel:** autor repo  
**Obszar:** Runtime / Reproducibility / Integration testing

### Decyzja: Opcja C — hybrid (external artifact + graceful degradation)

`reports/it_doc_matrix.db` (1.7 GB) jest **zewnętrznym artefaktem organizacyjnym**.  
Repo **nie obiecuje jej pełnej odbudowy z kodu źródłowego**.

#### Co to oznacza w praktyce

| Aspekt | Wartość |
|---|---|
| Źródło | `it_doc_matrix_before_auto_approve.db` — wynik wcześniejszego pipeline'u domenowego |
| Opiekun | autor repo — nie jest dostarczana przez zewnętrzną usługę |
| Odtwarzalność | NIE (wymaga pełnego ponownego przebiegu wcześniejszego pipeline'u domenowego) |
| Wymagana do | integration suite, compliance E2E (`TestComplianceE2E`) |
| Wymagana do fast suite | NIE — fast suite przechodzi bez niej |
| Wymagana do pipeline smoke | NIE — pipeline smoke uruchamia `build_current.py` na `it_doc_matrix_clean.db` |
| Bez niej `doctor --strict` | FAIL (missing: reports/it_doc_matrix.db) |

#### Tryby pracy

- **minimal / clean-room**: bez legacy DB → fast suite ✅, doctor ⚠️ (FAIL legacy_db, ale nie blokuje fast suite)
- **full-integration**: z legacy DB → wszystkie testy ✅

#### Jak dostarczyć legacy DB

```bash
# Jeśli plik istnieje jako kopia:
ln -sf it_doc_matrix_before_auto_approve.db reports/it_doc_matrix.db

# Jeśli plik nie istnieje — integration suite nie może być wykonany.
# Patrz: docs/TROUBLESHOOTING.md → sekcja "Missing legacy DB"
```

#### Implikacje dla `doctor.py`

`doctor.py --strict` zgłosi FAIL na `legacy_db` jeśli plik nie istnieje.  
To jest **oczekiwane zachowanie** w trybie minimal.  
`--strict` powinien być uruchamiany z pełnymi assets lub pomijany w CI smoke.

### Zamknięte przez

Phase 7 (2026-03-27) — hybrid model zatwierdzony, docs operacyjne zaktualizowane.

**Data przeglądu:** 2026-03-27  
**Decyzja końcowa:** Opcja C — external artifact z graceful degradation, opisana w RUNTIME_BOOTSTRAP.md i TROUBLESHOOTING.md

---

## OD-003 — Status pustego `generated_templates/satellite/`

**Status:** `OPEN`  
**Priorytet:** Średni  
**Właściciel:** `________________________________`  
**Obszar:** Runtime assets / Bootstrap / Doctor

### Opis
Katalog `generated_templates/satellite/` istnieje i jest częścią kontraktu runtime,
ale pozostaje pusty. Nie jest zapisane: czy to stan poprawny czy niepełny.

### Opcje
- **A:** Pusty `satellite/` jest poprawny (tylko strukturalnie wymagany).
- **B:** Pusty `satellite/` oznacza niepełny runtime — bootstrap powinien go zasilać.

### Warunek zamknięcia
Bootstrap, doctor i docs mają to samo stanowisko; testy nie zakładają sprzecznych interpretacji.

**Data przeglądu:** `________________________________`  
**Decyzja końcowa:** `________________________________`

---

## OD-004 — Poziom docelowy CI: smoke vs full-runtime

**Status:** `OPEN`  
**Priorytet:** Średni  
**Właściciel:** `________________________________`  
**Obszar:** CI / Release discipline / Automation

### Opis
Repo posiada smoke workflow (defensywny, skip gdy brak assets). Nie rozstrzygnięto,
czy ma powstać pełny CI z runtime assets na runnerze.

### Opcje
- **A:** Tylko smoke workflow.
- **B:** Pełny CI z pełnymi assets.
- **C:** Workflow ręczny / nightly z pełnymi assets (rekomendowane).

### Warunek zamknięcia
Poziomy CI jawnie nazwane; wiadomo, co jest twardą bramką, co jest smoke.

**Data przeglądu:** `________________________________`  
**Decyzja końcowa:** `________________________________`

---

## OD-005 — Poziom hermetyzacji danych runtime

**Status:** `OPEN`  
**Priorytet:** Średni  
**Właściciel:** `________________________________`  
**Obszar:** Reproducibility / Data contract / Repo maturity

### Opis
Repo jest technicznie stabilne, ale nie jest data-hermetic. Nie jest zamknięte:
czy repo ma być samowystarczalne bez zewnętrznych assets, czy tylko opisywać ich użycie.

### Opcje
- **A:** Repo jest code-first, assets są zewnętrzne.
- **B:** Repo ma procedurę pełnego odtworzenia.
- **C:** Dwa tryby: minimalny lokalny + pełny z assetami organizacyjnymi (rekomendowane).

### Warunek zamknięcia
Docs i tooling opisują wybrany model; bootstrap i doctor są zgodne; CI uwzględnia poziom hermetyzacji.

**Data przeglądu:** `________________________________`  
**Decyzja końcowa:** `________________________________`

---

## OD-006 — Status imported templates zawierających zewnętrzne referencje

**Status:** `OPEN`  
**Priorytet:** Niski (estetyczny, nie blokujący)  
**Właściciel:** maintainer repo  
**Zakres wpływu:** publiczny odbiór repo, recenzja techniczna

### Opis
`generated_templates/imported/` zawiera surowe dane wejściowe z zewnętrznego procesu importu.
Te pliki mogą zawierać:
- ścieżki `/home/...` z oryginalnego środowiska budującego (np. `/home/claude/doc-matrix/`),
- historyczne placeholdery dokumentacyjne,
- referencje kontekstowe z procesu importu.

Nie są to sekrety ani dane prywatne — są to artefakty procesu importu treści.

Zewnętrzny recenzent odpalający `git grep -n '/home/'` zobaczy wyniki w tym katalogu.

### Opcje
- **A (aktualna):** Zostawić i jasno opisać, że `generated_templates/imported/` jest surowym input data, nie code contractem.
- **B:** Usunąć `generated_templates/imported/` z repo, przenieść do zewnętrznych assets.
- **C:** Przenieść do dedykowanego katalogu `data/imported/` lub `samples/` z jawnym opisem.

### Aktualna decyzja
Opcja A: status opisany w `README.md` i `docs/EXTERNAL_REVIEW.md`. Imported templates są jawnie
oznaczone jako surowy input — nie są częścią kontraktu runtime.

### Warunek zamknięcia
Formally wybrana opcja; katalog ma jasny opis w dokumentacji lub został przeniesiony/usunięty.

**Data przeglądu:** `________________________________`  
**Decyzja końcowa:** `________________________________`

---

# ZASADY PRZEGLĄDU

Ten dokument należy przeglądać:
- przy formalnym zamykaniu fazy,
- przed otwarciem PR,
- przed pokazaniem repo na zewnątrz,
- po każdej większej zmianie runtime lub CI.

---

# ZAMKNIĘTE DECYZJE

*(Przenoszone tutaj po formalnym rozstrzygnięciu i wdrożeniu.)*
