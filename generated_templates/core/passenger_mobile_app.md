---
title: Passenger Mobile App
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Passenger Mobile App


## Metadane

- Właściciel: Mobile Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zdefiniować wymagania i standardy aplikacji mobilnej dla pasażerów (transport/linie lotnicze/kolej/metro), zapewniając spójne doświadczenie, niezawodność i bezpieczeństwo.


## Zakres i granice

- Obejmuje: rejestracja/logowanie (SSO/MFA), planowanie podróży i wyszukiwanie połączeń, bilety/boarding passes, płatności, notyfikacje (opóźnienia/gate), status lotu/pociągu, mapa terminalu/stacji, offline/low-connectivity, dostępność (WCAG mobile), bezpieczeństwo danych/PII, telemetria i crash reporting.  
- Poza zakresem: systemy operacyjne back-office (DCS/OMS), hardware kiosków.


## Użytkownicy i interesariusze
- **Mobile Developer (iOS/Android)** — projektuje i implementuje funkcje aplikacji mobilnej
- **UX/UI Designer** — dostarcza projekty interfejsu dopasowane do platform
- **QA Engineer** — testuje na urządzeniach docelowych
- **Product Owner** — definiuje wymagania funkcjonalne aplikacji

## Wejścia i wyjścia

- Wejścia: wymagania biznesowe (SLA, NPS), regulacje (PCI/RODO), integracje z backendami (booking, schedule, payments, loyalty), design system UI, wytyczne a11y, profile użytkowników.  
- Wyjścia: specyfikacja funkcjonalna, API kontrakty, wymagania offline/cache, flow notyfikacji, checklisty DoR/DoD, testy (functional/a11y/perf/security), plan release i monitoring.


## Założenia

- Backend booking/schedule dostępny.  
- Payment provider zgodny z PCI.  
- Zespół ma proces release mobilnych.


## Otwarte pytania

- Jak obsłużyć zwroty i zmiany rezerwacji w offline?  
- Jak długo przechowywać dane biletów i telemetry?  
- Jak wspierać multi-tenant/regionalne różnice treści?

## Powiązania (meta)

- Key Documents: api_reference_for_mobile_developers, ui_test_strategy, payment_processing_standards, accessibility_improvement_plan, security_controls_reference, offline_mode_guidelines (jeśli istnieje).  
- Key Document Structures: auth, search/travel plan, tickets/payments, notifications, offline, a11y, telemetry.  
- Document Dependencies: backend booking/schedule, payment gateway, push provider, analytics, feature flags, crashlytics.


## Zależności dokumentu

Wymaga: kontraktów API backendów, wymagań płatności/PCI, design systemu, polityk RODO, planu offline, infrastruktury push, danych rozkładów, polityk notyfikacji. Brak = brak DoR.


## Fazy cyklu życia

- Definicja wymagań i kontraktów API.  
- Projekt UX/UI i architektury mobilnej.  
- Implementacja i testy (functional/a11y/perf/sec).  
- Rollout (feature flags), monitoring, release plan.  
- Utrzymanie, feedback i iteracje.



## Struktura sekcji (szkielet)
- Streszczenie i cele biznesowe
- Zakres, założenia, ograniczenia
- Kontekst domenowy i interesariusze
- Wymagania funkcjonalne i niefunkcjonalne
- Architektura/komponenty i integracje
- Model danych i przepływy informacji
- Bezpieczeństwo, prywatność i compliance
- Plan wdrożenia/migracji i kryteria go/no-go
- Monitoring/operacje oraz ryzyka i mitigacje
- Decyzje i uzasadnienia, pytania otwarte
## Szybkie powiązania

- linkage_index.jsonl (passenger/mobile/app)  
- api_reference_for_mobile_developers, ui_test_strategy


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **OWASP MASVS** — Standard Weryfikacji Bezpieczeństwa Aplikacji Mobilnych (OWASP)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów

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

1. Zbierz scenariusze i kontrakty API; zdefiniuj offline i a11y.  
2. Zaprojektuj flow auth, płatności, notyfikacji; przygotuj testy.  
3. Implementuj z feature flags; testuj functional/a11y/perf/sec.  
4. Rollout etapowy; monitoruj telemetry; aktualizuj dokument/linkage_index.


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

- Boarding pass: elektroniczny dokument wejścia na pokład.  
- Staged rollout: stopniowe udostępnianie wersji użytkownikom.  
- Offline-first: kluczowe dane dostępne bez połączenia.


## Przykłady użycia

- Aplikacja linii lotniczej z boarding pass i status flight.  
- Aplikacja kolejowa z biletami i mapą stacji offline.  
- Aplikacja komunikacji miejskiej z opóźnieniami i płatnościami.


## Ryzyka i ograniczenia

- Brak offline → utrata dostępu do biletów.  
- Opóźnione notyfikacje → frustracja użytkowników.  
- Błędy płatności → utrata przychodu.  
- Luka bezpieczeństwa → wycieki PII/płatności.


## Decyzje i uzasadnienia

- Model offline/cache i TTL.  
- Metody płatności i provider.  
- Priorytety notyfikacji i częstotliwość.  
- Strategie rollout i monitoring KPI.


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

- Search/plan ↔ Tickets/payments ↔ Notifications.  
- Offline/cache ↔ Dane rozkładów ↔ UX i SLA.  
- A11y ↔ UI ↔ Testy.  
- Telemetria ↔ Monitoring ↔ Release/rollout.


## Struktura sekcji

1) Użytkownicy i scenariusze (journeys)  
2) Auth i konta (SSO/MFA/loyalty)  
3) Wyszukiwanie i plan podróży; bilety/boarding  
4) Płatności i PCI; portfele/loyalty  
5) Notyfikacje (push/in-app/SMS), status i alerty  
6) Offline/low-connectivity i cache danych  
7) Dostępność i UI (WCAG mobile)  
8) Telemetria, crash, monitoring  
9) Testy i DoR/DoD  
10) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- API kontrakty (search, booking, payments, status).  
- Flow offline i cache (TTL, invalidacja).  
- Notyfikacje: matryca zdarzeń, częstotliwość, treść, opt-in.  
- Wymagania a11y (wielkość czcionek, kontrast, screen readers).  
- Plan testów perf (zimny start, render list, sieć 2G/3G).  
- Plan security (MFA, cert pinning, storage wrażliwych danych).


## Wymagane streszczenia

- Executive summary: scope, integracje krytyczne, SLA UX.  
- Skrót ryzyk: offline, płatności, opóźnienia notyfikacji.


## Guidance (skrót)

- Utrzymuj offline-first dla kluczowych funkcji (bilety, boarding).  
- Pin certyfikaty, szyfruj storage; minimalizuj PII.  
- Testuj na niskiej łączności; optymalizuj payloady.  
- WCAG mobile: focus, kontrast, alternatywy dotyku.  
- Używaj feature flags i staged rollout; monitoruj crash rate i NPS.  
- Aktualizuj linkage_index po releasach.


## Checklisty Definition of Ready (DoR)

- [ ] API kontrakty dostępne; dane rozkładów/biletów gotowe.  
- [ ] Wymagania płatności/PCI i polityki RODO potwierdzone.  
- [ ] Plan offline/cache i notyfikacji zdefiniowany.  
- [ ] Wytyczne a11y i design system dostępne.  
- [ ] Narzędzia telemetry/crash i monitoring skonfigurowane.


## Checklisty Definition of Done (DoD)

- [ ] Funkcje wdrożone; testy functional/a11y/perf/sec zielone.  
- [ ] Offline/cache działa; bilety/boarding dostępne bez sieci.  
- [ ] Notyfikacje działają; opt-in/out obsłużone.  
- [ ] Crash rate i latency w SLA; monitoring/alerty aktywne.  
- [ ] Dokumentacja i linkage_index zaktualizowane; rollout zakończony.

