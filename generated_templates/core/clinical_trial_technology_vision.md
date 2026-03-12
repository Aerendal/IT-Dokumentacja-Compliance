---
title: Clinical Trial Technology Vision
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Clinical Trial Technology Vision


## Metadane

- Właściciel: Clinical Lead
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zdefiniować wizję technologii dla badań klinicznych: zintegrowany ekosystem eSource, EDC, ePRO/eCOA, randomizacja, zarządzanie wizytami, dane omiczne i obrazowe, bezpieczeństwo i zgodność (GxP, 21 CFR Part 11, GDPR). Ukierunkować inwestycje, architekturę i roadmapę.


## Zakres i granice

- Obejmuje: architekturę danych i integracji (CDISC/ODM/SEND), eSource/EDC, ePRO/eCOA, IRT (randomizacja/supply), eConsent, remote monitoring/risk-based monitoring, data lake/warehouse, anonimiza­cję/pseudonimizację, audyt/ślad zgodności, bezpieczeństwo, interoperacyjność z site i lab.  
- Poza zakresem: szczegółowy plan wdrożeń poszczególnych systemów (oddzielne plany), negocjacje z CRO i vendorami.


## Użytkownicy i interesariusze
- **Clinical Lead / Chief Medical Officer** — definiuje wymagania kliniczne i waliduje
- **Integration Architect** — projektuje integracje z systemami szpitalnymi
- **Security / Privacy Officer** — zapewnia zgodność z HIPAA, RODO, ustawa o ochronie zdrowia
- **Development Team** — implementuje funkcjonalności kliniczne

## Wejścia i wyjścia

- Wejścia: portfolio badań (faz, wskazań), wymagania regulacyjne (FDA/EMA, ICH E6/E8), standardy CDISC, obecny krajobraz systemów, pain‑pointy site/sponsor, SLA danych, wymagania bezpieczeństwa, koszty.  
- Wyjścia: docelowa architektura i zasady integracji, priorytety inwestycji, roadmapa 12–36 m-cy, guiding principles (dane, bezpieczeństwo, UX site/pacjent), wskaźniki sukcesu, DoR/DoD dla inicjatyw.


## Założenia

- Budżet i wsparcie zarządu są dostępne.  
- Site i partnerzy zaakceptują standardy integracji.  
- Zespół ma kompetencje GxP i data governance.


## Otwarte pytania

- Jakie kraje/regiony wymagają dodatkowych regulacji lokalnych?  
- Czy potrzeba wielojęzycznego eConsent?  
- Jak mierzyć sukces adopcji ePRO/eSource?  
- Jakie są plany interoperacyjności z sieciami badawczymi/registries?

## Powiązania (meta)

- Key Documents: data_governance_requirements, security_controls_reference, risk_based_monitoring_strategy, data_retention_policy, interoperability_guidelines, patient_privacy_guidelines.  
- Key Document Structures: architektura, dane/standardy, bezpieczeństwo, UX pacjenta/site, monitoring, roadmapa.  
- Document Dependencies: master data (site/patient/study), IAM/SSO, audit trail, integration hub (ETL/ESB), ePRO/IRT/EDC/CTMS/LIMS, cloud governance.


## Zależności dokumentu

Wymaga: katalogu badań i systemów, standardów danych (CDISC), wymagań regulatorów, polityk bezpieczeństwa i prywatności, modelu danych master, zdolności integracyjnych, planu budżetu/ROI. Brak = brak DoR.


## Fazy cyklu życia

- Ocena stanu obecnego i regulacji.  
- Definicja wizji/architektury docelowej.  
- Roadmapa i priorytety inicjatyw.  
- Wdrożenia etapowe i kontrola GxP.  
- Ewaluacja i ciągłe usprawnianie.



## Struktura sekcji (szkielet)
- Streszczenie i wizja
- Diagnoza stanu i kontekst
- Cele i KPI
- Filar/priorytety i inicjatywy
- Horyzonty/roadmapa i zależności
- Ryzyka i założenia
- Governance, finansowanie i raportowanie
## Szybkie powiązania

- linkage_index.jsonl (clinical/trial/technology/vision)  
- risk_based_monitoring_strategy, patient_privacy_guidelines, data_governance_requirements


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **HL7 FHIR** — Standard Wymiany Danych w Ochronie Zdrowia
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum

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

1. Zbierz wymagania badań i regulacji; zinwentaryzuj systemy.  
2. Określ zasady i architekturę docelową; uzgodnij w governance.  
3. Zbuduj roadmapę z priorytetami i właścicielami; odhacz DoR.  
4. Monitoruj realizację, mierz metryki, aktualizuj wizję.


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

- eSource: bezpośredni zapis danych w formie elektronicznej u źródła.  
- IRT: system randomizacji i zarządzania dostawami w badaniu.  
- Risk-Based Monitoring: monitorowanie oparte na ryzyku wg ICH E6(R2).


## Przykłady użycia

- Wyznaczenie kierunku dla modernizacji EDC/ePRO i integracji z LIMS.  
- Przygotowanie programu cyfryzacji badań fazy III w kilku krajach.  
- Ocena zgodności architektury z 21 CFR Part 11 przed audytem.


## Ryzyka i ograniczenia

- Brak standardów danych → wysokie koszty integracji i analizy.  
- Vendor lock‑in → ograniczona elastyczność i zgodność.  
- Niespełnienie wymogów Part 11/GDPR → ryzyko regulacyjne.  
- Słaba adopcja site/pacjentów → niska jakość danych.


## Decyzje i uzasadnienia

- Wybór platform (EDC/ePRO/IRT) i modeli integracji.  
- Standardy danych i mechanizmy pseudonimizacji.  
- Priorytety inwestycji i harmonogram.  
- Poziom automatyzacji walidacji i RBM.


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

- [Artefakt 1, np. diagram architektury] — [opis i relacja do tego dokumentu]
- [Artefakt 2, np. schemat bazy danych] — [opis i relacja do tego dokumentu]

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

- Standardy danych ↔ Integracje ↔ Monitoring ryzyka.  
- UX pacjenta/site ↔ Adopcja ePRO/eConsent ↔ Jakość danych.  
- Bezpieczeństwo/prywatność ↔ Audit trail ↔ Retencja/anonymizacja.


## Struktura sekcji

1) Kontekst badań i regulacji  
2) Guiding principles (dane, UX, bezpieczeństwo, zgodność)  
3) Architektura docelowa (dane, integracje, narzędzia)  
4) Standardy i interoperacyjność (CDISC, API, semantyka)  
5) Bezpieczeństwo i prywatność (GxP, 21 CFR Part 11, GDPR)  
6) Roadmapa i priorytety (12–36 m-cy)  
7) Metryki sukcesu i governance  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Diagram architektury docelowej z głównymi systemami i przepływami.  
- Lista standardów (CDISC SDTM/ADaM/ODM/SEND) i wymagań Part 11.  
- Priorytety inicjatyw (krótkoterminowe vs strategiczne) z ROI.  
- Model bezpieczeństwa/prywatności (pseudonimizacja, role, audyt).  
- Plan interoperacyjności z site/lab (API/ETL, harmonogram).  
- Metryki: time-to-lock, query rate, ePRO adherence, downtime.


## Wymagane streszczenia

- Executive summary: wizja, 3–5 głównych inicjatyw, kluczowe ryzyka.  
- Skrót standardów i zasad integracji (one‑pager).


## Guidance (skrót)

- Ustandaryzuj dane wg CDISC i trzymaj single source of truth.  
- Projektuj „patient/site first”: niskie tarcie ePRO/eConsent, offline.  
- Wymagaj pełnego audit trail i kontroli GxP w każdym komponencie.  
- Buduj integracje modułowo (API-first), unikaj vendor lock‑in.  
- Zapewnij monitoring jakości danych i RBM; automatyzuj walidacje.  
- Roadmapę mapuj na wartość kliniczną i ryzyko regulacyjne.


## Checklisty Definition of Ready (DoR)

- [ ] Katalog badań i systemów zaktualizowany.  
- [ ] Standardy danych i wymagania regulatorów zebrane.  
- [ ] Właściciele danych i bezpieczeństwa wyznaczeni.  
- [ ] Założenia budżetu/ROI dostępne.  
- [ ] Governance (komitet) gotowe do decyzji.


## Checklisty Definition of Done (DoD)

- [ ] Wizja/architektura zatwierdzone; dokumentacja opublikowana.  
- [ ] Roadmapa z priorytetami i metrykami przyjęta.  
- [ ] Kluczowe ryzyka i decyzje zapisane; linkage_index zaktualizowany.  
- [ ] Plan zgodności (Part 11/GDPR) i audytowy ustalony.  
- [ ] Przegląd okresowy zaplanowany.

