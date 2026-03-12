---
title: EHR Implementation Retrospective
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# EHR Implementation Retrospective


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Podsumowuje wdrożenie systemu EHR: co się udało, co nie, wpływ kliniczny/operacyjny, ryzyka i rekomendacje. Służy do nauki przed kolejnymi rolloutami i audytami zgodności.


## Zakres i granice

- Obejmuje: cele wdrożenia, przebieg i timeline, szkolenia i adopcję użytkowników, migrację danych, integracje (FHIR/HL7/DICOM), wydajność i dostępność, bezpieczeństwo/zgodność (HIPAA/RODO), wsparcie/incidenty, wyniki kliniczne/operacyjne, FinOps/koszt, rekomendacje i plan działań.  
- Poza zakresem: szczegółowa dokumentacja techniczna komponentów EHR (osobne dokumenty).


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: plan wdrożenia, checklisty cutover, logi incidentów, metryki adopcji i wydajności, ankiety użytkowników, raporty szkoleniowe, dane migracji, audyty bezpieczeństwa, koszty i budżet.  
- Wyjścia: retrospektywa (co działa/nie), lista problemów i root cause, rekomendacje i plan działań, priorytety następnych faz, aktualizacje risk register, status DoR/DoD.


## Założenia

- Dane kliniczne mogą być analizowane w sposób zgodny z privacy.  
- Zespoły kliniczne/IT współpracują w retro.  
- Systemy monitoring/ticketing są dostępne.


## Otwarte pytania

- Czy potrzebne są dodatkowe szkolenia/zimny start dla nowych użytkowników?  
- Jakie są wymagania regulatora na raportowanie wdrożenia?  
- Jak poprawić adoption dla kluczowych modułów (np. e-prescription)?


## Powiązania (meta)

- Key Documents: implementation_plan_ehr, migration_runbook_ehr, training_plan_ehr, interoperability_plan, privacy_and_consent_policy, dr_plan_clinical_it, risk_register.  
- Key Document Structures: cele, timeline, adopcja, migracja, integracje, wydajność, bezpieczeństwo/zgodność, incidenty, rekomendacje.  
- Document Dependencies: CMDB/CMMS EHR, systemy integracyjne, logi, monitoring, ticketing, budżet/FinOps.


## Zależności dokumentu

Wymaga: danych z rolloutów (logi, KPI, ankiety), listy integracji i statusów, raportów bezpieczeństwa/zgodności, kosztów i budżetu, planu szkoleń. Braki = DoR otwarte.


## Fazy cyklu życia

- Zbieranie danych po rolloutach.  
- Analiza i warsztaty retro z zespołami klinicznymi/IT.  
- Publikacja raportu i planu działań.  
- Follow‑up i weryfikacja wdrożonych usprawnień.



## Struktura sekcji (szkielet)
- Cel i kontekst biznesowy
- Interesariusze, persony i scenariusze
- Wymagania funkcjonalne (priorytety, reguły, wyjątki)
- Wymagania niefunkcjonalne (wydajność, dostępność, bezpieczeństwo, zgodność)
- Dane i integracje
- Kryteria akceptacji i miary sukcesu
- Zależności, ryzyka i założenia
- Śledzenie (traceability) do epik/testów
## Szybkie powiązania

- linkage_index.jsonl (ehr/implementation/retrospective)  
- implementation_plan_ehr, migration_runbook_ehr, training_plan_ehr, interoperability_plan, dr_plan_clinical_it


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **HL7 FHIR** — Standard Wymiany Danych w Ochronie Zdrowia
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
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

1. Zbierz dane po rolloutach (KPI, incydenty, feedback).  
2. Przeprowadź warsztat retro, wypełnij sekcje i plan działań.  
3. Opublikuj raport, aktualizuj risk register i monitoruj follow‑up; uzupełnij DoR/DoD i linkage_index.


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

- PHI: Protected Health Information.  
- RCM: Root Cause and Mitigation.  
- Adoption: aktywne użycie funkcji vs uprawnieni użytkownicy.


## Przykłady użycia

- Retro po rollout pilota EHR w jednej klinice.  
- Podsumowanie migracji danych pacjentów i integracji labów.  
- Ocena wsparcia użytkowników i plan szkoleń uzupełniających.


## Ryzyka i ograniczenia

- Niedokładne dane migracji → utrata zaufania klinicystów.  
- Brak follow‑up → powtarzające się incydenty.  
- Ryzyka zgodności (HIPAA/RODO) przy raportowaniu danych.


## Decyzje i uzasadnienia

- Priorytety działań naprawczych (kliniczne bezpieczeństwo > UX > koszt).  
- Zakres kolejnej fazy rollout vs stabilizacja.  
- Zakres testów integracyjnych i walidacji danych przed kolejną fazą.


## Powiązania z innymi dokumentami

- training_plan_ehr — szkolenia.  
- migration_runbook_ehr — migracja danych.  
- interoperability_plan — integracje.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- HIPAA/RODO, lokalne regulacje medyczne, standardy EHR (FHIR/HL7).  
- Wewnętrzne polityki kliniczne i bezpieczeństwa.

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

- Timeline → Incidenty/Migracja → Wnioski → Plan działań.  
- Adopcja/szkolenia → Wyniki kliniczne/operacyjne → Rekomendacje.  
- Bezpieczeństwo/zgodność → Ryzyka → Aktualizacja register.


## Struktura sekcji

1) Cele i zakres wdrożenia (kliniczne/operacyjne)  
2) Timeline i przebieg (fazy, cutover, kluczowe decyzje)  
3) Adopcja i szkolenia (metryki, feedback, pokrycie)  
4) Migracja danych (jakość, błędy, poprawki, PII/PHI)  
5) Integracje (FHIR/HL7/DICOM/API) i problemy  
6) Wydajność i dostępność (SLO/SLA, incydenty)  
7) Bezpieczeństwo i zgodność (HIPAA/RODO, audyty, inspekcje)  
8) Incidenty i wsparcie (typy, MTTR, contact rate)  
9) Wyniki kliniczne/operacyjne i FinOps (koszt vs budżet)  
10) Rekomendacje i plan działań (owner, termin, priorytet)  
11) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Tabela problemów/RCM i akcji; status i owner.  
- Metryki adopcji (użytkownicy aktywni, task completion, błędy).  
- Podsumowanie incydentów (typy, MTTR, wpływ kliniczny).  
- Plan działań z terminami i zależnościami.


## Wymagane streszczenia

- Executive snapshot: sukcesy, top 5 problemów, wpływ kliniczny, koszt, decyzje.  
- Lista działań krytycznych na kolejną fazę z terminami.


## Guidance (skrót)

- Zbieraj dane z wielu źródeł (logi, ankiety, kliniczne KPI).  
- Ocena jakości danych po migracji jest kluczowa dla zaufania użytkowników.  
- Mapuj problemy do root cause i ownerów; ustal SLA na poprawki.  
- Uwzględnij bezpieczeństwo/zgodność w rekomendacjach (HIPAA/RODO).  
- Weryfikuj plan działań na follow‑up, nie tylko publikuj raport.


## Checklisty Definition of Ready (DoR)

- [ ] Logi/metryki rolloutów i ankiety dostępne.  
- [ ] Lista integracji i statusów zebrana.  
- [ ] Raporty bezpieczeństwa/zgodności dostępne.  
- [ ] Dane budżet/koszt z FinOps.  
- [ ] Zespół retro (kliniczni/IT) umówiony.


## Checklisty Definition of Done (DoD)

- [ ] Sekcje uzupełnione; problemy/RCM i plan działań z ownerami.  
- [ ] Risk register zaktualizowany; status/wersja/data uzupełnione.  
- [ ] Follow‑up zaplanowany; raport udostępniony interesariuszom.  
- [ ] Lessons learned dodane do repo wiedzy; linkage_index zaktualizowany.  
- [ ] Najważniejsze KPI kliniczne/operacyjne z raportu.

