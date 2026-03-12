---
title: Smart Building Sensors Deployment
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Smart Building Sensors Deployment


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Planować i realizować wdrożenie czujników smart building (HVAC, energia, occupancy, bezpieczeństwo), zapewniając poprawność danych, bezpieczeństwo, ciągłość i integrację z BMS/IoT/analytics.


## Zakres i granice

- Obejmuje: dobór czujników (typy, klasy dokładności), lokalizację i instalację, zasilanie/PoE/baterie, sieć (BACnet/IP, Modbus, Zigbee, BLE, Wi‑Fi), bezpieczeństwo OT/IT, onboarding do platformy IoT/BMS, kalibrację, monitoring zdrowia urządzeń, retencję danych, testy odbiorowe i dokumentację.  
- Poza zakresem: projekt architektury BMS (osobny dokument), systemy bezpieczeństwa fizycznego wysokiego ryzyka (osobne runbooki).


## Użytkownicy i interesariusze
- **DevOps / Platform Engineer** — zarządza infrastrukturą i pipeline'ami wdrożeniowymi
- **SRE (Site Reliability Engineer)** — definiuje SLO/SLI i zarządza niezawodnością
- **Development Team** — dostarcza artefakty do wdrożenia
- **Security Officer** — weryfikuje zgodność wdrożeń z polityką bezpieczeństwa

## Wejścia i wyjścia

- Wejścia: wymagania funkcjonalne (co mierzymy), plany budynku, standardy HSE, wytyczne sieci/OT, lista modeli czujników, budżet/energetyka, polityki bezpieczeństwa, wymagania danych/retencji.  
- Wyjścia: plan rozmieszczenia, konfiguracje sieci/protokołów, procedura kalibracji, lista urządzeń i identyfikatorów, testy odbiorowe, plan monitoringu i utrzymania, checklisty DoR/DoD.


## Założenia

- Budynek ma infrastrukturę sieciową/elektryczną zgodną z wymaganiami.  
- Zespół ma dostęp do stref instalacji.  
- IoT/BMS platforma obsługuje wymagane protokoły.


## Otwarte pytania

- Czy wymagane są certyfikaty bezpieczeństwa urządzeń?  
- Jak długo przechowywać surowe dane czujników?  
- Czy potrzebne są fallbacki offline dla krytycznych pomiarów?  
- Jak zarządzać dostępem serwisowym w terenie?

## Powiązania (meta)

- Key Documents: iot_security_reference, building_performance_metrics, data_quality_playbook, maintenance_windows_schedule, access_control_policy, network_segmentation.  
- Key Document Structures: inwentarz czujników, sieć/protokoły, instalacja, kalibracja, monitoring, utrzymanie.  
- Document Dependencies: BMS/IoT platforma, sieć OT/IT, CMDB/inventory, PKI/klucze, NMS/monitoring.


## Zależności dokumentu

Wymaga: planów budynku i stref, standardów sieci/protokołów, listy zatwierdzonych czujników, polityk bezpieczeństwa i dostępu, narzędzi do kalibracji, platformy IoT/BMS oraz identyfikatorów/naming. Braki = brak DoR.


## Fazy cyklu życia

- Planowanie (zakres, lokalizacje, sieć).  
- Instalacja i onboarding do platformy.  
- Kalibracja i testy odbiorowe.  
- Monitoring zdrowia i danych.  
- Utrzymanie/kalibracje okresowe i wycofanie.



## Struktura sekcji (szkielet)
- Cel i zakres wdrożenia
- Środowiska i okna wdrożeniowe
- Architektura docelowa i przepływy danych
- Kroki/migracja (pilot → produkcja)
- Plan testów i kryteria go/no-go
- Monitoring/observability i runbooki
- Rollback/contingency i komunikacja
- Ryzyka, zależności, RACI
## Szybkie powiązania

- linkage_index.jsonl (smart_building/sensors/deployment)  
- iot_security_reference, building_performance_metrics, maintenance_windows_schedule


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SAFe 6.0** — Scaled Agile Framework

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

1. Zbierz wymagania i plany; zaplanuj rozmieszczenie.  
2. Przygotuj sieć/protokoły i onboarding; zainstaluj czujniki.  
3. Skalibruj, wykonaj testy odbiorowe; uruchom monitoring.  
4. Prowadź utrzymanie, kalibracje, aktualizuj dokument i linkage_index.


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

- BMS: Building Management System.  
- Dryft czujnika: odchylenie od wartości referencyjnej w czasie.  
- Onboarding czujnika: rejestracja, identyfikacja, konfiguracja sieci i bezpieczeństwa.


## Przykłady użycia

- Instalacja czujników occupancy i CO₂ w biurowcu.  
- Rozbudowa systemu energetycznego o pomiary mocy/temperatury.  
- Migracja starej instalacji na protokół IP/BACnet.


## Ryzyka i ograniczenia

- Słabe pokrycie sieci → braki danych.  
- Brak kalibracji → błędne sterowanie HVAC.  
- Nieaktualne firmware → luki bezpieczeństwa.  
- Brak CMDB → utrudnione utrzymanie i audyt.


## Decyzje i uzasadnienia

- Wybór protokołów (BACnet/Modbus/Zigbee/Wi‑Fi).  
- Polityka kalibracji i wymiany baterii.  
- Zakres szyfrowania i segmentacji.  
- Kryteria wyboru lokalizacji czujników.


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

- Lokalizacja ↔ Sieć/zasilanie ↔ Kalibracja.  
- Bezpieczeństwo ↔ Onboarding ↔ Monitoring urządzeń.  
- Dane/retencja ↔ Analytics ↔ BMS integracje.


## Struktura sekcji

1) Wymagania i zakres pomiarów  
2) Inwentarz i plan rozmieszczenia czujników  
3) Sieć/protokoły i bezpieczeństwo OT/IT  
4) Instalacja, onboarding, identyfikacja  
5) Kalibracja i testy odbiorowe  
6) Monitoring zdrowia i danych, alerty  
7) Utrzymanie, aktualizacje, wycofanie  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Matryca czujnik → lokalizacja → protokół/zasilanie → dokładność.  
- Procedura onboarding (ID, certyfikaty, klucze, temat MQTT/REST).  
- Plan kalibracji (częstotliwość, narzędzia, progi).  
- Testy odbiorowe (funkcja, sieć, dane, alarmy).  
- Plan monitoringu (uptime, bateria, dryft, dane nieprawidłowe).  
- Polityka aktualizacji firmware i wycofania urządzeń.


## Wymagane streszczenia

- Executive summary: zakres wdrożenia, liczba czujników, główne ryzyka.  
- Skrót sieci/protokołów i zasad bezpieczeństwa OT/IT.


## Guidance (skrót)

- Używaj zatwierdzonych czujników i protokołów; trzymaj spójny naming/ID.  
- Segmentuj sieć OT, szyfruj tam gdzie możliwe; certyfikaty/klucze rotuj.  
- Kalibruj przy instalacji i cyklicznie; loguj wyniki.  
- Monitoruj baterie i dryft; alarmuj na brak danych/anomalie.  
- Dokumentuj lokalizację (mapy) i aktualizuj CMDB/linkage_index.  
- Plan maintenance w oknach; rollback firmware w razie problemów.


## Checklisty Definition of Ready (DoR)

- [ ] Plany budynku i stref dostępne; zakres pomiarów zdefiniowany.  
- [ ] Zatwierdzona lista czujników i protokołów; zasady bezpieczeństwa.  
- [ ] Sieć/zasilanie przygotowane; identyfikatory przydzielone.  
- [ ] Narzędzia do instalacji/kalibracji dostępne.  
- [ ] IoT/BMS platforma gotowa do onboardingu.


## Checklisty Definition of Done (DoD)

- [ ] Czujniki zainstalowane, onboardowane, wykaz w CMDB.  
- [ ] Kalibracja i testy odbiorowe zaliczone; dane poprawne.  
- [ ] Monitoring/alerty działają; baterie/firmware zweryfikowane.  
- [ ] Dokumentacja i linkage_index zaktualizowane; ryzyka zamknięte.  
- [ ] Plan utrzymania (kalibracje, aktualizacje) ustawiony.

