---
title: Access Control Matrix Design
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Access Control Matrix Design


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Projektuje i standaryzuje macierz kontroli dostępu (role → zasoby → uprawnienia) wraz z zasadami nadawania, przeglądów i audytu. Zapewnia spójność, minimalny dostęp i zgodność (SoD/least privilege).


## Zakres i granice

- Obejmuje: role/atrybuty, zasoby/systemy/obiekty, uprawnienia (CRUD/RBAC/ABAC), zasady nadawania (joiner/mover/leaver), SoD, wyjątki/waivery, przeglądy okresowe, audyt/logi, integracje z IdP/SSO/IAM/CMDB, wzorce dla aplikacji/API/data.
- Poza zakresem: szczegółowe polityki haseł/MFA (osobne dokumenty), implementacja kodu aplikacji (low-level).


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

- access_control_policy, identity_and_access_architecture, multi_factor_authentication_design, logging_and_audit_trail, security_controls_reference, data_classification, security_requirements, risk_register


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

- [ ] Każde uprawnienie ma rolę/atrybut, zasób, uzasadnienie i właściciela; SoD ma wyjątki z sunset.
- [ ] Workflow nadawania/recertyfikacji działa; audyt/logi i testy least privilege/SoD są zaplanowane.


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

## Powiązania sekcja↔sekcja

- Role/atrybuty → zasoby → uprawnienia → workflow nadawania → przeglądy → audyt/logi.
- SoD → wyjątki/waivery → przeglądy → sunset.


## Struktura sekcji

1) Streszczenie i cele (least privilege, SoD, compliance)  
2) Zakres ról/zasobów/obiektów (aplikacje/API/data, klasyfikacja)  
3) Model ról/atrybutów i uprawnień (CRUD, RBAC/ABAC, SoD)  
4) Macierz kontroli dostępu (role/atributy → zasoby → uprawnienia)  
5) Workflow nadawania/zmian (JML, self-service, approval, waivery)  
6) Przeglądy okresowe i SoD (cadence, właściciele, raporty)  
7) Audyt i logi (kto/co/kiedy, SIEM, dowody)  
8) Integracje (IdP/IAM, HR, CMDB, ticketing, aplikacje/API/bazy)  
9) Testy i walidacja (SoD tests, least privilege, regressje), kryteria akceptacji  
10) Ryzyka i wyjątki; decyzje (ADR) i otwarte pytania  


## Wymagane rozwinięcia

- Macierz ról/atrybutów→zasoby→uprawnienia; SoD rules; lista wyjątków/waivers z sunset.
- Workflow JML i approval; audyt/logi zakres; raport SoD i recertyfikacji.
- Plan testów (SoD, least privilege, regressje) i harmonogram przeglądów.


## Wymagane streszczenia

- Executive summary: scope, główne zasady, top ryzyka i wyjątki, harmonogram przeglądów.
- One-pager: macierz ról/zasobów high-level, SoD zasady, cykl przeglądów.


## Guidance (skrót)

- DoR: role/zasoby/klasyfikacja i wymagania SoD zebrane; IdP/IAM/CMDB dostępne; właściciele ról/zasobów wskazani.
- DoD: macierz i workflow opisane; SoD i wyjątki z sunset; audyt/logi/testy zdefiniowane; harmonogram przeglądów; metadane aktualne; dokument w linkage_index.
- Spójność: każda rola ma zakres i właściciela; każde uprawnienie ma zasób i uzasadnienie; SoD ma wyjątki z sunset; przeglądy mają cadence i dowody.


## Checklisty Definition of Ready (DoR)

- [ ] Role/zasoby/klasyfikacja i wymagania SoD zebrane; IdP/IAM/CMDB dostępne; właściciele ról/zasobów wskazani.


## Checklisty Definition of Done (DoD)

- [ ] Macierz ról/zasobów/uprawnień zdefiniowana; workflow JML/approvals; SoD i wyjątki z sunset; testy/audyt/przeglądy zdefiniowane; dokument w linkage_index.

