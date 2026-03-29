# CONTRIBUTING.md

## Cel dokumentu

Ten dokument opisuje zasady wprowadzania zmian do repo.

Celem jest:
- utrzymanie spójności technicznej,
- ochrona kontraktu runtime,
- ograniczenie przypadkowych regresji,
- utrzymanie czytelnej historii zmian.

---

# 1. Zasady ogólne

Przyjmowane zmiany powinny:
- mieć jasny zakres,
- nie mieszać niepowiązanych tematów w jednym commicie,
- nie psuć kontraktu runtime,
- nie ukrywać problemów przez miękkie obejścia,
- pozostawiać repo w stanie weryfikowalnym.

Nie są mile widziane:
- commity typu `misc`, `fix all`, `cleanup`,
- zmiany bez dowodu wykonania,
- zmiany oparte o lokalne ścieżki lub lokalne założenia autora,
- niejawne placeholdery w pipeline lub testach.

---

# 2. Workflow pracy

## Zalecana kolejność
1. utwórz branch roboczy,
2. przygotuj środowisko,
3. uruchom bootstrap i doctor,
4. wykonaj zmianę,
5. uruchom odpowiedni poziom testów,
6. sprawdź hooki / toolchain,
7. dopiero wtedy przygotuj commit.

---

# 3. Minimalne wymagania przed commitem

Przed commitem należy uruchomić co najmniej:

```bash
python3 scripts/doctor.py
python3 -m pytest -q -m "not integration and not slow"
```

> **Uwaga:** `doctor.py` bez flagi `--strict` jest trybem informacyjnym (exit 0). Jeżeli zmiana dotyczy pełnego runtime z legacy DB, uruchom `doctor.py --strict` dla weryfikacji całego kontraktu.

Jeżeli zmiana dotyczy runtime, pipeline, compliance lub integration, to dodatkowo:

```bash
python3 -m pytest -q -m "integration and not slow"
python3 scripts/pipeline_run.py
```

---

# 4. Zmiany w runtime i assets

Zmiany dotyczące:

* `reports/it_doc_matrix.db`
* `reports/it_doc_matrix_clean.db`
* `generated_templates/`
* `reports/alignment_log.csv`

muszą być traktowane jako zmiany kontraktowe.

Każda taka zmiana powinna:

* mieć uzasadnienie,
* być opisana w commit message,
* zachować spójność z `bootstrap_runtime.py`,
* zachować spójność z `doctor.py`,
* zachować spójność z dokumentacją.

---

# 5. Zmiany w dokumentacji

Zmiany w:

* `README.md`
* `docs/RUNTIME_BOOTSTRAP.md`
* `docs/DEV_WORKFLOW.md`
* `docs/TROUBLESHOOTING.md`

muszą odpowiadać realnym zachowaniom repo.

Nie aktualizuj dokumentacji „na oko".
Każdą komendę z docs należy uruchomić naprawdę.

---

# 6. Styl commitów

Zalecany format commit message:

* `fix(runtime): ...`
* `fix(pipeline): ...`
* `fix(compliance): ...`
* `test(repo): ...`
* `docs(process): ...`
* `feat(repo): ...`

Każdy commit powinien być:

* logicznie spójny,
* wąski tematycznie,
* czytelny dla osoby z zewnątrz.

---

# 7. Czego nie commitować

Nie commituj:

* lokalnych backupów,
* paczek `.tar.gz`, `.zip`,
* sesyjnych logów naprawczych,
* prywatnych danych,
* cache i artefaktów środowiskowych,
* tymczasowych wyników testów.

Kieruj się `.gitignore`, ale nie traktuj go jako wymówki dla złego porządku repo.

---

# 8. Zgłaszanie większych zmian

Dla zmian naruszających:

* runtime contract,
* profile DB,
* pipeline,
* onboarding,
* model toolchain,

należy opisać:

* problem,
* zakres zmiany,
* wpływ na minimal/full mode,
* sposób weryfikacji,
* warunek ukończenia.

---

# 9. Otwarte decyzje

Jeżeli podczas pracy wychodzi temat, którego nie zamykasz od razu, dodaj go do:

* `docs/OPEN_DECISIONS.md`

Nie zostawiaj krytycznych decyzji „na pamięć".

---

# 10. Odpowiedzialność za jakość

Minimalny standard zmiany to:

* repo nadal się uruchamia,
* kontrakt runtime nie jest rozbity,
* poziom testów adekwatny do zakresu zmiany przechodzi,
* dokumentacja nie kłamie,
* nie pojawiają się ukryte zależności lokalne.


---

## Korzystanie z narzędzi wspomagających AI

Dopuszczalne jest korzystanie z narzędzi wspomagających programowanie i redakcję dokumentacji (np. GitHub Copilot), pod warunkiem że każda zmiana:

- została przeczytana i zrozumiana przez autora commitu,
- jest zgodna z kontraktem repozytorium i aktualną dokumentacją,
- przechodzi wymagane testy i walidację,
- nie wprowadza sekretów, danych poufnych ani treści o niejasnym statusie licencyjnym,
- nie omija odpowiedzialności inżynierskiej za wynik końcowy.

Narzędzia AI traktujemy jako źródło sugestii roboczych.  
Nie zastępują one odpowiedzialności za architekturę, dobór rozwiązań, weryfikację zmian ani utrzymanie repozytorium.

Jeżeli commit lub pull request powstał z użyciem narzędzi wspomagających, autor zmiany powinien w szczególności upewnić się, że:
- rozumie cały wprowadzany kod,
- potrafi uzasadnić zmianę,
- potrafi wskazać sposób jej lokalnej weryfikacji,
- potrafi ocenić jej wpływ na kontrakt runtime, testy i dokumentację.
