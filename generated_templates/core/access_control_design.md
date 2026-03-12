---
title: Access Control Design
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Access Control Design


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zaplanować projekt kontroli dostępu (role/atrybuty, zasady, wyjątki) dla systemu/API.


## Zakres i granice

- Obejmuje: model RBAC/ABAC, mapa zasobów, zasady, wyjątki/waivery, procesy nadawania/odbierania.
- Poza zakresem: implementacja kodu/konfiguracji.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: wymagania bezpieczeństwa/compliance (SoD/PCI/SOX/GDPR), modele ról/atrybutów, zasoby i klasyfikacja danych, procesy JML, istniejące uprawnienia/odchylenia, IdP/IAM/CMDB, audyt/logi.
- Wyjścia: macierz kontroli dostępu (role/atrybuty → zasoby → uprawnienia), zasady nadawania i przeglądów, SoD rules i wyjątki, integracje (IdP/IAM/app/API/data), plan wdrożenia i przeglądów, testy i audyt.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Key Documents: access_control_policy, identity_and_access_architecture, multi_factor_authentication_design, logging_and_audit_trail, security_controls_reference, data_classification, security_requirements.
- Dependencies: IdP/IAM, CMDB/asset, HR/JML, ticketing/IAM workflow, SIEM/logi, SoD rules, data classification.
## Zależności dokumentu
- Upstream: wymagania regulacyjne/SoD, klasyfikacja danych, katalog zasobów, role/atrybuty, IdP/IAM, HR procesy.
- Downstream: implementacja w aplikacjach/API/bazach, workflow nadawania/przeglądów, audyt/logi, testy bezpieczeństwa.
- Zewnętrzne: dostawcy IdP/IAM, audytorzy/regulatorzy (SOX/PCI/ISO), 3rd party systemy.
## Fazy cyklu życia
- Inwentaryzacja ról/zasobów/uprawnień i SoD.
- Projekt macierzy i workflow.
- Wdrożenie i testy (security/SoD/audyt).
- Przeglądy okresowe i doskonalenie.
## Struktura sekcji (szkielet)

- Kontekst i cele
- Model ról/atrybutów
- Zasady i wyjątki
- Procesy nadawania/odbierania
- Audyt/review
- Ryzyka


## Szybkie powiązania
- access-control-matrix-design
- access-control
- support-access-control
- role-based-access-control-rbac-design
- mission-control-design

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

- Wypełnij sekcje według szkieletu; jeśli sekcja N/A, uzasadnij.
- Dodaj quick-links i uzupełnij checklisty DoR/DoD w reports/checklist_atomic.jsonl.
- Po review zaktualizuj metadane, artefakty i status.


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
- Macierz ról/atrybutów→zasoby→uprawnienia, SoD rules, waiver log, JML/approval workflow, raporty recertyfikacji, logi audytu, ADR log.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Wejścia

- Mapa zasobów i ról
- Polityki bezpieczeństwa
- Wymagania compliance
- Ryzyka/incydenty


## Wyjścia

- Design access control
- Mapa ról→zasoby
- Procesy przydziału/odbioru
- Checklisty DoR/DoD



## Szybkie powiązania (uzupełnij)

- [ ] access_control_security.md
- [ ] access_control_matrix_reference.md
- [ ] logging_and_audit_trail.md
- [ ] security_policy_design.md
- [ ] api_security_design.md
- [ ] security_best_practices.md


## Wymagane rozwinięcia / streszczenia

- Streszczenie kluczowych decyzji/ryzyk; rozwinięcia testów/polityk/macierzy.


## Wymagane powiązania

- Dokumenty security/access control/logging/testy; runbooki incydentów; compliance.


## Kryteria DoR

- [ ] Wymagania/cel zebrane
- [ ] Owner dokumentu przypisany
- [ ] Narzędzia/środowiska dostępne
- [ ] Ryzyka wstępne zidentyfikowane


## Kryteria DoD

- [ ] Sekcje wypełnione lub N/A z uzasadnieniem
- [ ] Quick-links/checklisty dodane
- [ ] Artefakty wskazane
- [ ] Metadane/DoR/DoD zaktualizowane


## Artefakty do załączenia

- Plan/ramy dokumentu
- Checklisty
- Przykłady lub macierze
- Linki do narzędzi


## Walidacja / testy

- Sanity/negative/abuse scenariusze; weryfikacja logów/alertów jeśli dotyczy.


## Metryki monitorowane

- Czas przygotowania dokumentu
- Pokrycie sekcji (%)
- Liczba otwartych TODO
- Incydenty/regresje związane z tematem


## Utrzymanie i aktualizacje

- Przegląd co release lub kwartalnie; aktualizacja quick-links/checklist/macierzy.


## Zakończenie

Po spełnieniu DoD zaktualizuj status, podlinkuj artefakty/quick-links i odhacz checklistę w reports/checklist_atomic.jsonl.
