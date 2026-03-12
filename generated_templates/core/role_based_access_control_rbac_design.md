---
title: Role-Based Access Control (RBAC) Design
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Role-Based Access Control (RBAC) Design


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Projektuje RBAC dla systemów/aplikacji/API: role, uprawnienia, zasady nadawania i recertyfikacji, SoD, audyt i testy, by zapewnić least privilege, zgodność i dobre UX.


## Zakres i granice

- Obejmuje: model ról (biznes/tech/system), mapowanie ról do uprawnień i zasobów, SoD, zasady nadawania (JML), wyjątki/waivery, recertyfikacje, audyt/logi, testy i rollout.  
- Poza zakresem: ABAC/JIT (w osobnych dokumentach), polityka haseł/MFA (osobno).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: access_control_goals, data classification, lista zasobów/obiektów, SoD requirements, IdP/IAM, HR/JML procesy, audyty/odchylenia, risk register.
- Wyjścia: model ról i macierz ról→uprawnienia→zasoby, SoD rules, workflow nadawania/recertyfikacji, wyjątki/waivery (sunset), plan testów i rollout, ADR, ryzyka.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: access_control_matrix_design, access_control_matrix_reference, access_control_patterns, access_control_review, access_control_testing, multi_factor_authentication_design, data_classification, security_controls_reference.
- Dependencies: IdP/IAM, CMDB/asset, HR/JML, ticketing/workflow, SIEM/logi.


## Zależności dokumentu

- Upstream: AC goals, SoD, asset/CMDB, data classification, IdP/IAM, JML procesy.
- Downstream: macierze aplikacyjne, provisioning/deprovisioning, recertyfikacje, audyt/logi, testy AC.
- Zewnętrzne: audytorzy/regulatorzy, dostawcy IdP/IAM.


## Fazy cyklu życia

- Analiza ról/zasobów/SoD.
- Projekt i walidacja z ownerami.
- Wdrożenie i testy (SoD/least privilege).
- Rollout i recertyfikacje okresowe.



## Struktura sekcji (szkielet)

- Kontekst i wymagania
- Decyzje architektoniczne (ADR)
- Komponenty i integracje
- Diagramy (C4/UML/flowchart)
- Bezpieczeństwo i compliance
- Skalowalność i ograniczenia

## Szybkie powiązania

- attribute-based-access-control-abac-design
- access-control-design
- access-control-matrix-design
- design-rbac
- access-control

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.

## Standardy i compliance


Lista standardów i wymagań regulacyjnych mających zastosowanie do tego dokumentu.
Uzupełnij na podstawie sekcji "Mające zastosowanie standardy i normy" oraz tabeli `doc_standard_mapping`.

- Standard / norma: [kod i nazwa]
- Wymaganie regulacyjne: [kod i treść]
- Polityka wewnętrzna: [nazwa polityki]


## RACI i role


Macierz RACI (Responsible / Accountable / Consulted / Informed) dla działań związanych z tym dokumentem.

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie | [rola]      | [rola]      | [rola]    | [rola]   |
| Przegląd  | [rola]      | [rola]      | [rola]    | [rola]   |
| Aktualizacja | [rola]   | [rola]      | [rola]    | [rola]   |
| Archiwizacja | [rola]   | [rola]      | [rola]    | [rola]   |

## Jak używać dokumentu
1. Zbierz wymagania i klasyfikacje zasobów; zbuduj słownik atrybutów i źródła.  
2. Zaprojektuj polityki i PDP/PEP z cache i logowaniem; zdecyduj default deny/fail‑closed.  
3. Uruchom testy/regresje, wdroż governance i rollout; zaktualizuj linkage_index.
## Checklisty jakości

### Kompletność
- **Kryterium:** Wszystkie wymagane sekcje i pola są wypełnione
- **Metryka:** Odsetek wypełnionych sekcji do wymaganych
- **Próg OK:** 90%
- **Narzędzie:** template_auditor.py, checklist_atomic.jsonl

### Dokładność
- **Kryterium:** Informacje są poprawne merytorycznie i aktualne
- **Metryka:** Przegląd ekspercki; data ostatniej aktualizacji
- **Próg OK:** Przegląd co 3 mies.
- **Narzędzie:** regulation_updater.py

### Spójność
- **Kryterium:** Terminologia i struktura są spójne w całej bibliotece
- **Metryka:** Liczba niespójności terminologicznych i strukturalnych
- **Próg OK:** 0 niespójności
- **Narzędzie:** bulk_section_patcher.py

### Śledzalność
- **Kryterium:** Każda sekcja ma źródło (standard, regulacja, decyzja)
- **Metryka:** Odsetek sekcji z wypełnionymi standards_refs
- **Próg OK:** 80%
- **Narzędzie:** impact_analyzer.py

### Aktualność
- **Kryterium:** Dokument jest aktualny względem obowiązujących regulacji
- **Metryka:** Czas od ostatniej aktualizacji vs. częstotliwość przeglądów
- **Próg OK:** < 6 mies.
- **Narzędzie:** changelog_tracker.py

### Użyteczność
- **Kryterium:** Użytkownik końcowy może efektywnie wypełnić dokument na podstawie guidance
- **Metryka:** Ocena guidance (score z template_auditor); feedback użytkowników
- **Próg OK:** Score >= 70
- **Narzędzie:** template_auditor.py

## Definicje robocze

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]

## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ relacji: rozszerza/streszcza/wymaga/wyklucza]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji

- [Wejście] -> [Sekcja źródłowa] -> [Sekcja rozwinięcia] -> [Wyjście]
- [Wejście] -> [Sekcja źródłowa] -> [Sekcja streszczenia] -> [Wyjście]

## Weryfikacja spójności

- [ ] Czy wszystkie ścieżki informacji są zamknięte (każde wejście ma wyjście)?
- [ ] Czy istnieją pętle lub sprzeczne relacje między sekcjami?
- [ ] Czy sekcje kluczowe mają wskazane źródła i odbiorców?
- [ ] Czy terminologia jest spójna z sekcją "Słownik pojęć"?

## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane
- Słownik atrybutów, repo polityk (Rego/XACML), diagram PDP/PEP, konfiguracja cache, logi decyzji, metryki, ADR/waiver log.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości
- Latency decyzji, hit/miss cache, deny rate vs oczekiwany, liczba bypass/waiver, czas propagacji zmian atrybutów, liczba incydentów eskalacji uprawnień.
## Kryteria ukończenia
- [ ] ABAC zaprojektowany z pełnym zestawem atrybutów, polityk, PDP/PEP, testów i audytu; powiązany w linkage_index.
## Powiązania sekcja↔sekcja

- Role → uprawnienia → zasoby → SoD → nadawanie → recertyfikacje → audyt/logi → testy.


## Struktura sekcji

1) Streszczenie i cele (least privilege, SoD, compliance)  
2) Zakres ról i zasobów (systemy/API/data, klasyfikacja)  
3) Model ról (biznes/tech/system), dziedziczenie, opis, właściciele  
4) Macierz ról→uprawnienia→zasoby (tabele, CSV/JSON)  
5) SoD i wyjątki/waivery (sunset, kompensacje)  
6) Nadawanie/zmiany (JML, approval, self-service), recertyfikacje (cadence, dowody)  
7) Audyt i logi (kto/co/kiedy, SIEM, raporty)  
8) Testy i rollout (scenariusze SoD/escalation, automaty, regressje)  
9) Ryzyka i decyzje (ADR); otwarte pytania  


## Wymagane rozwinięcia

- Macierz ról→uprawnienia→zasoby (CSV/JSON), SoD rules, waiver log.
- Workflow JML i recertyfikacji; audyt/logi zakres; testy AC (SoD/least privilege).
- Plan rollout i komunikacji; harmonogram recertyfikacji.


## Wymagane streszczenia

- Executive summary: kluczowe role, SoD, zmiany, harmonogram rollout/recerts.
- One-pager: model ról, SoD zasady, cadence recertyfikacji, link do macierzy.


## Guidance (skrót)

- DoR: role/zasoby/SoD zebrane; IdP/IAM/CMDB dostępne; ownerzy ról i systemów; wymagania audyt/regulatora znane.
- DoD: model ról i macierz opublikowane; SoD/waivery z sunset; workflow JML/recerts i audyt/logi opisane; testy i rollout plan; metadane aktualne; dokument w linkage_index.
- Spójność: każda rola ma właściciela/opis; uprawnienia powiązane z zasobami; SoD i wyjątki udokumentowane; recertyfikacje mają cadence i dowody.

