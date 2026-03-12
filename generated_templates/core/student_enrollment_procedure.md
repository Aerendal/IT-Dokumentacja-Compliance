---
title: Student Enrollment Procedure
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Student Enrollment Procedure


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Procedura zapisu studenta: kroki, dane, weryfikacje, płatności i komunikacja. Ma zapewnić zgodność z regulacjami, kompletność danych i dobre doświadczenie kandydata.


## Zakres i granice

- Obejmuje: kanały aplikacji, formularze i dane wymagane, weryfikacje (tożsamość, dokumenty, kwalifikacje), decyzje i komunikację, płatności/depozty, rejestrację na kursy, konta IT/ID, zgody i privacy, SLA czasowe, dostępność/A11y, wyjątki i odwołania.  
- Poza zakresem: proces rekrutacji akademickiej (ocena meritum) – tu koncentrujemy się na formalnym zapisie.


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia

- Wejścia: wniosek kandydata, dokumenty (ID, świadectwa), dane kontaktowe, kwalifikacje, status wizowy, zgody, płatności/depozyt, polityki regulacyjne.  
- Wyjścia: status decyzji, komunikaty do kandydata, opłaty zaksięgowane, konto studenckie i dostęp IT, zapis na kursy, raporty do regulatora/finansów.


## Założenia

- Systemy IT dostępne i zintegrowane.  
- Zespół Admissions i IT współpracują.  
- Obowiązują lokalne przepisy edukacyjne.


## Otwarte pytania

- Jak obsłużyć brakujące dokumenty po starcie semestru?  
- Jakie kanały wsparcia dla kandydatów?  
- Jak raportować do regulatorów?


## Powiązania (meta)

- Key Documents: admissions_policy, identity_verification_policy, payment_reliability_runbook, privacy_policy, accessibility_compliance, course_registration_flow.  
- Key Document Structures: aplikacja, weryfikacje, decyzja, płatność, rejestracja, zgody, komunikacja.  
- Document Dependencies: SIS/CRM, payment gateway, ID verification, document management, IAM/SSO, LMS.


## Zależności dokumentu

Wymaga: polityk przyjęć i weryfikacji, integracji z SIS/CRM/płatności, szablonów komunikacji, wymogów regulatora (dane/raporty), procedur A11y/privacy. Braki = DoR otwarte.


## Fazy cyklu życia

- Przyjęcie wniosku i kompletacja dokumentów.  
- Weryfikacje i decyzja.  
- Płatności/depozyt i rejestracja na kursy.  
- Provisioning kont IT/ID i onboarding.  
- Raporty/regulator i retro.



## Struktura sekcji (szkielet)
- Cel, zakres i definicje sukcesu
- Trigger/scenariusze i preconditions
- Role, uprawnienia i narzędzia
- Kroki operacyjne (checklista) z walidacją
- Monitoring i dowody wykonania
- Rollback/contingency oraz komunikacja/escalacja
- Rejestr zmian runbooka
## Szybkie powiązania

- linkage_index.jsonl (student/enrollment/procedure)  
- admissions_policy, privacy_policy, payment_reliability_runbook, course_registration_flow


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

1. Zmapuj etapy, dane i weryfikacje; przygotuj checklisty/SLA.  
2. Skonfiguruj integracje SIS/CRM/płatności/ID; uruchom komunikację.  
3. Monitoruj metryki; aktualizuj DoR/DoD i linkage_index; wprowadzaj poprawki.


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

- SIS: Student Information System.  
- Time-to-decision: czas od kompletnego wniosku do decyzji.  
- Deposit: opłata rezerwacyjna.


## Przykłady użycia

- Zapis studentów krajowych vs zagranicznych.  
- Ścieżka express dla programów online.  
- Ręczne odwołania/wyjątki.


## Ryzyka i ograniczenia

- Niekompletne dane → opóźnienia.  
- Płatności/zwroty niezgodne → ryzyka prawne.  
- Brak A11y/privacy → skargi/regulator.


## Decyzje i uzasadnienia

- Jakie dane są obowiązkowe.  
- Kryteria automatycznej decyzji vs manualnej.  
- Polityka depozytu/zwrotów.


## Powiązania z innymi dokumentami

- course_registration_flow — rejestracja.  
- payment_reliability_runbook — płatności.  
- privacy_policy — dane.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- RODO i lokalne prawo edukacyjne; polityki uczelni.

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

- Aplikacja → Weryfikacje → Decyzja → Płatność → Rejestracja → Dostępy.  
- Privacy/A11y → Formularze/komunikacja → Zgody.  
- SLA → Komunikacja → Doświadczenie kandydata.


## Struktura sekcji

1) Kanały i formularze aplikacji (web/paper)  
2) Dane wymagane i weryfikacje (ID, kwalifikacje, wizowe)  
3) Decyzja i komunikacja (statusy, SLA, odwołania)  
4) Płatności/depozyt i polityki zwrotów  
5) Rejestracja na kursy i limity (SIS)  
6) Provisioning kont/ID (SSO, e-mail, karty)  
7) Privacy/A11y i zgody (RODO, dostępność formularzy)  
8) Raporty i compliance (regulator, finanse)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Checklista danych/dokumentów i weryfikacji.  
- Szablony komunikacji (ack, decision, payment, onboarding).  
- Flow płatności/depozytu i zwrotów.  
- SLA per etap i wskaźniki (time-to-decision).


## Wymagane streszczenia

- One‑pager procesu (etapy, SLA, dane).  
- Snapshot metryk (czas decyzji, kompletność danych, dropout).


## Guidance (skrót)

- Upraszczaj formularze; waliduj dane wcześnie.  
- Automatyzuj weryfikację (ID/doc) gdzie to możliwe; miej ścieżkę manualną.  
- Jasne SLA i komunikaty statusów; zapewnij A11y.  
- Płatności zgodnie z polityką; loguj i audytuj.  
- Zapewnij zgodność RODO i lokalnych wymogów edukacyjnych.


## Checklisty Definition of Ready (DoR)

- [ ] Polityki przyjęć i weryfikacji dostępne.  
- [ ] Integracje SIS/CRM/płatności/ID przygotowane.  
- [ ] Formularze i komunikaty zgodne z A11y/Privacy.  
- [ ] SLA i wskaźniki ustalone.  
- [ ] Zespół i role przypisane.


## Checklisty Definition of Done (DoD)

- [ ] Proces działa w SIS/CRM; status/wersja/data uzupełnione.  
- [ ] Komunikaty/szablony aktywne; SLA monitorowane.  
- [ ] Płatności/depozyty i zwroty obsługiwane; audyt/PII zabezpieczone.  
- [ ] Raporty regulator/finanse gotowe; linkage_index uzupełniony.  
- [ ] Lessons learned/ryzyka zebrane.

