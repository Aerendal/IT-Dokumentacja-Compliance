---
title: Port Operations Testing
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Port Operations Testing


## Metadane

- Właściciel: QA Lead
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zdefiniować strategię testów dla systemów operacji portowych (TOS/Berth/yard/gate): funkcjonalność, integracje, wydajność, bezpieczeństwo i zgodność.


## Zakres i granice

- Obejmuje: scenariusze terminalowe (przyjęcie/wyjście kontenerów, yard/gate/berth planning), integracje (VGM, celne, EDI, IoT/RTG/ASC), wydajność (volume/peak), dostępność, bezpieczeństwo (role/SoD, audyt), a11y/UX, DR/BCP, testy terenowe z urządzeniami.
- Poza zakresem: szczegółowe SOP operacyjne (osobne dokumenty), hardware urządzeń przeładunkowych.


## Użytkownicy i interesariusze
- **QA Lead / Test Manager** — planuje strategię testowania i zarządza procesem QA
- **QA Engineer** — projektuje i wykonuje przypadki testowe
- **Development Team** — naprawia defekty i dostarcza testowalny kod
- **Product Owner** — definiuje kryteria akceptacji i priorytetyzuje defekty

## Wejścia i wyjścia
- Wejścia: rozkład zawinięć, manifesty ładunkowe, plany stowarzyszeń linii (VSA), dostępność sprzętu i załóg, SLA z klientami, wymagania celne, dane pogodowe/pływy.  
- Wyjścia: plan operacyjny na dobę/tydzień, przydział zasobów (suwnice, bramy, składy), procedury bezpieczeństwa i komunikacji, plan kolejkowania ciężarówek/kolei, alerty i runbooki incydentów, raport KPI.
## Założenia
- Dostępność TOS, łączności radiowej/IT i danych AIS.  
- Współpraca służb portowych i celnych.  
- Stała dostępność sprzętu i załóg wg planu.
## Otwarte pytania
- Czy wymagane są dodatkowe kontrole celne dla określonych ładunków?  
- Jakie SLA z liniami priorytetują przydział okien?  
- Jak często testować runbooki awaryjne?  
- Czy kolejkowanie gate będzie dynamiczne (ETA‑driven) czy slotowe?
## Powiązania (meta)
- Key Documents: safety_management_plan, crisis_management_playbook, network_ot_security, customs_clearance_procedure, tos_configuration_reference, asset_maintenance_plan.  
- Key Document Structures: okno nabrzeżne, przydział zasobów, bezpieczeństwo, kolejka gate/rail, monitoring KPI, scenariusze awaryjne.  
- Document Dependencies: TOS/WMS/rail system, CCTV/VMS, IoT/RFID, meteo/tide feed, workforce planning.  
- Standardy/Compliance: ISPS Code, IMO/IAPH zalecenia, lokalne przepisy portowe, HSE.
## Zależności dokumentu
Wymaga: dostępności TOS i jego API, integracji z systemem kolejki gate, danych AIS/ETA, planów sprzętu i utrzymania, polityk HSE/ISPS, kontaktów do służb (port, cło, straż). Braki = blokery DoR.
## Fazy cyklu życia
- Inicjacja okna nabrzeżnego.  
- Planowanie szczegółowe (resource planning).  
- Operacje i monitoring w czasie rzeczywistym.  
- Rozliczenie/raport KPI i wnioski.  
- Retrospektywa i zmiany procedur.
## Struktura sekcji (szkielet)

- Zakres funkcjonalny (gate/yard/berth/EDI)
- Integracje i dane testowe
- Wydajność/obciążenie i SLA
- Bezpieczeństwo/SoD/audyt
- Testy terenowe (urządzenia, connectivity)
- DR/BCP i failover
- Kryteria akceptacji i regresja
- Raportowanie


## Szybkie powiązania

- TOS Requirements, EDI/Customs, Security/SoD, DR/BCP, Observability.


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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
1. Wypełnij kartę statku i plan zasobów.  
2. Potwierdź bezpieczeństwo (ISPS/HSE) i komunikację.  
3. Uruchom operacje, monitoruj KPI/alerty, aktualizuj plan.  
4. Po zakończeniu zamknij raport dzienny i odhacz DoD.
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
- TOS: Terminal Operating System do planowania i realizacji ruchu.  
- Berth window: zarezerwowane okno czasowe przy nabrzeżu.  
- Moves per hour (MPH): kluczowy KPI wydajności suwnic.
## Przykłady użycia
- Planowanie serwisu kontenerowego z trzema statkami jednocześnie.  
- Przeładunek ro‑ro z priorytetem pojazdów ciężkich.  
- Zarządzanie kolejką gate w szczycie i przekierowanie na rail.
## Ryzyka i ograniczenia
- Sztorm/opóźnienia pogodowe → przesunięcia okien i koszty.  
- Awaria TOS/komunikacji → przestoje.  
- Incydent HSE/ISPS → zatrzymanie operacji.  
- Niedoszacowanie zasobów → kongestia yard/gate.
## Decyzje i uzasadnienia
- Priorytetyzacja serwisów wg SLA i demurrage.  
- Model kolejki (sloty vs FCFS) i kanały komunikacji.  
- Progi KPI dla alertów i eskalacji.
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

## Wejścia

- Wymagania TOS, integracje EDI/API, profile wolumenów, polityki bezpieczeństwa, środowiska test, urządzenia terenowe.


## Wyjścia

- Plan testów (funkcjonalne, integracyjne, wydajnościowe, DR), zestaw przypadków, kryteria akceptacji, raporty, plan regresji i testów terenowych.



## Jak używać (checklista)

- Zbierz scenariusze operacyjne i integracje; przygotuj dane.
- Zaplanuj testy funkcjonalne i EDI; uruchom wydajnościowe z peak load.
- Zweryfikuj role/SoD i audyt; wykonaj testy terenowe z urządzeniami.
- Przeprowadź testy DR/BCP; podsumuj raportem i kryteriami akceptacji.


## Wymagane rozwinięcia / powiązania

- Zestaw przypadków testowych, dane EDI/API, skrypty load, matryca ról/SoD, plan testów terenowych, runbook DR.


## Kryteria DoR

- Wymagania TOS i integracji znane; środowisko i dane testowe dostępne; urządzenia terenowe gotowe.


## Kryteria DoD

- Testy wykonane, wyniki spełniają SLA; raport i decyzja akceptacji; regresja zaplanowana.


## Artefakty

- Plan testów, przypadki, raporty, logi load, checklisty terenowe, runbook DR.


## Walidacja

- Przegląd wyników; audyt bezpieczeństwa/SoD; weryfikacja EDI; testy failover w środowisku test.


## Metryki

- Pass rate, wydajność vs SLA, błędy EDI, czas odprawy gate, incydenty bezpieczeństwa, czas odtworzenia DR.


## Utrzymanie

- Aktualizacja po zmianach TOS/integracji; przegląd regresji; testy terenowe cyklicznie.


## Zakończenie

Strategia testów portowych zapewnia niezawodność operacji; utrzymuj ją z regresją, EDI i testami terenowymi.

