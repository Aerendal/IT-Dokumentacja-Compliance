---
title: Pharmacovigilance Training
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Pharmacovigilance Training


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Przygotować program szkoleń z farmakowigilancji (PV) dla zespołów medycznych, jakości i operacji, aby zapewnić zgodność regulacyjną, właściwe raportowanie zdarzeń niepożądanych i bezpieczeństwo pacjentów.


## Zakres i granice

- Obejmuje: definicje i obowiązki PV, proces zgłaszania AE/SAE, zarządzanie sygnałami, bazy bezpieczeństwa, formularze i kanały raportowania, timelines regulatorów (EMA/FDA), zarządzanie dokumentacją (PSUR/DSUR), rola QPPV, audyty i inspekcje, szkolenia roczne/refresher.  
- Poza zakresem: tworzenie planów ryzyka dla konkretnych produktów (RMP) – osobne dokumenty.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania regulacyjne, SOP PV, system bezpieczeństwa (DB), role i odpowiedzialności, przykłady AE/SAE, harmonogram raportów okresowych, plan audytów.  
- Wyjścia: program szkolenia (agenda, materiały), checklisty DoR/DoD, test wiedzy, rejestr uczestników, harmonogram refresher, raport z realizacji i zgodności.


## Założenia

- System bezpieczeństwa i LMS dostępne.  
- SOP i wymagania regulatorów są znane.  
- Uczestnicy mają czas na szkolenia.


## Otwarte pytania

- Jak długo przechowywać rejestry i testy?  
- Czy wymagane są lokalne różnice (kraje)?  
- Jak obsłużyć kontraktorów/partnerów w zakresie PV?

## Powiązania (meta)

- Key Documents: data_protection_compliance, hipaa_compliance_training, quality_assurance_plan, regulatory_document_management, audit_trail_monitoring.  
- Key Document Structures: definicje, proces zgłoszeń, role, dokumentacja/raporty, audyt/szkolenia.  
- Document Dependencies: safety DB, reporting portals (E2B/R3), IAM/SSO, LMS, regulator timelines.


## Zależności dokumentu

Wymaga: aktualnych SOP PV, listy ról (QPPV, safety officers), dostępu do systemu bezpieczeństwa i portali raportowych, harmonogramów raportów, polityk ochrony danych (PII/PHI). Brak = brak DoR.


## Fazy cyklu życia

- Planowanie programu i materiałów.  
- Szkolenia podstawowe i role‑based.  
- Test wiedzy i rejestracja.  
- Refresher roczne/po zmianach SOP.  
- Audyt i ciągłe doskonalenie.



## Struktura sekcji (szkielet)
- Cele szkolenia i oczekiwane rezultaty
- Grupa docelowa/persony i wymagania wstępne
- Moduły/agenda z czasem i formą (teoria/lab)
- Materiały i środowisko (lab/demo)
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ocena postępów (quiz/lab/egzamin) i feedback
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania

- linkage_index.jsonl (pharmacovigilance/training)  
- hipaa_compliance_training, regulatory_document_management


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

1. Przygotuj materiały i harmonogram; zmapuj role i dostępy.  
2. Przeprowadź szkolenia i testy; zapisuj w rejestrze.  
3. Weryfikuj zgodność z timelines; aktualizuj przy zmianach SOP.  
4. Przy audycie/inspekcji użyj rejestrów i testów jako dowodów.


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

- AE/SAE: adverse event/serious adverse event.  
- QPPV: Qualified Person Responsible for Pharmacovigilance.  
- PSUR/DSUR: raporty okresowe bezpieczeństwa.


## Przykłady użycia

- Onboarding nowego zespołu klinicznego.  
- Refresher po zmianie SOP lub systemu bezpieczeństwa.  
- Przygotowanie do inspekcji regulatora.


## Ryzyka i ograniczenia

- Przekroczenie timelines → sankcje regulacyjne.  
- Brak zgodności PII/PHI → naruszenia danych.  
- Niekompletne rejestry → niepowodzenie audytu.  
- Niedostosowanie szkoleń do ról → luki w procesie.


## Decyzje i uzasadnienia

- Zakres szkoleń role-based.  
- Progi testów i częstotliwość refresher.  
- Narzędzia do e-learningu/LMS.  
- Zakres danych w materiałach (anonimizacja).


## Powiązania z innymi dokumentami
- escalation_procedure_design — ścieżki eskalacji.  
- communication_plan — komunikaty.  
- observability_plan — alerty.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Wewnętrzne polityki bezpieczeństwa i dostępu, PII.  
- Standardy SRE/ITIL jeśli przyjęte.
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

- Zgłoszenia AE/SAE ↔ Timelines ↔ Dokumentacja (PSUR/DSUR).  
- Role ↔ Dostępy (IAM) ↔ Audyt.  
- Szkolenia ↔ Test wiedzy ↔ Rejestr i inspekcje.


## Struktura sekcji

1) Definicje AE/SAE i obowiązki PV  
2) Proces zgłoszeń (kanały, formularze, czasy)  
3) Zarządzanie sygnałami i eskalacje  
4) Dokumentacja: PSUR/DSUR, rejestry, audyt trail  
5) Role, uprawnienia i QPPV  
6) Szkolenia, testy, rejestry i refresher  
7) DoR/DoD, ryzyka, pytania


## Wymagane rozwinięcia

- Agenda szkolenia (core + role-based).  
- Checklista zgłoszenia AE/SAE i timelines.  
- Instrukcje korzystania z systemu bezpieczeństwa i portali E2B/R3.  
- Szablon testu wiedzy i progi zaliczenia.  
- Rejestr uczestników i ścieżka audytu.  
- Plan refresher i komunikacja zmian SOP.


## Wymagane streszczenia

- Executive summary: zakres PV, role, timelines.  
- Skrót obowiązków QPPV i kluczowych raportów.


## Guidance (skrót)

- Upewnij się, że każdy zna definicje AE/SAE i czasy raportowania.  
- Chronić PII/PHI; dane tylko w systemie bezpieczeństwa.  
- Dokumentuj każde zgłoszenie; trzymaj spójny audyt trail.  
- Szkolenia role-based; refresher przy każdej zmianie SOP.  
- Przygotuj do inspekcji: rejestry, testy, materiały.  
- Aktualizuj linkage_index po cyklu szkoleń.


## Checklisty Definition of Ready (DoR)

- [ ] SOP PV aktualne; role i obowiązki zdefiniowane.  
- [ ] Dostęp do systemu bezpieczeństwa i portali raportowych.  
- [ ] Materiały i testy przygotowane; LMS gotowy.  
- [ ] Harmonogram raportów/inspekcji znany.  
- [ ] Polityka ochrony danych potwierdzona.


## Checklisty Definition of Done (DoD)

- [ ] Szkolenia przeprowadzone; testy zaliczone.  
- [ ] Rejestry uczestników i wyniki zarchiwizowane.  
- [ ] Brak otwartych niezgodności z timelines.  
- [ ] Dokumentacja i linkage_index zaktualizowane.  
- [ ] Plan refresher ustawiony; materiały zaktualizowane po feedbacku.

