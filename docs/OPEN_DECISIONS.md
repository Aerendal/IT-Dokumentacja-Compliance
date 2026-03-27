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

**Status:** `OPEN`  
**Priorytet:** Wysoki  
**Właściciel:** `________________________________`  
**Obszar:** Runtime / Reproducibility / Integration testing

### Opis
Repo używa `reports/it_doc_matrix.db` (1.7 GB) jako bazy `legacy-runtime`.
Nie jest formalnie zapisane: skąd pochodzi, kto ją utrzymuje, jak odtworzyć.

### Opcje
- **A:** DB jest artefaktem dostarczanym zewnętrznie — opisać źródło i opiekuna.
- **B:** DB ma procedurę pełnego odtworzenia — dostarczyć builder + pipeline.

### Ryzyko braku decyzji
Integration suite działa tylko „tam, gdzie działała wcześniej". Nowa osoba nie odtworzy runtime.

### Warunek zamknięcia
Status DB opisany w docs, `doctor.py` komunikuje to poprawnie, integration zgodne z modelem.

**Data przeglądu:** `________________________________`  
**Decyzja końcowa:** `________________________________`

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

# ZASADY PRZEGLĄDU

Ten dokument należy przeglądać:
- przy formalnym zamykaniu fazy,
- przed otwarciem PR,
- przed pokazaniem repo na zewnątrz,
- po każdej większej zmianie runtime lub CI.

---

# ZAMKNIĘTE DECYZJE

*(Przenoszone tutaj po formalnym rozstrzygnięciu i wdrożeniu.)*
