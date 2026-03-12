---
title: Sensor Deployment Plan
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Sensor Deployment Plan


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zaplanować i przeprowadzić wdrożenie czujników (IoT/OT) w terenie, zapewniając poprawność danych, bezpieczeństwo, łączność i utrzymanie w cyklu życia.


## Zakres i granice

- Obejmuje: wybór czujników i specyfikacje, lokalizację/instalację, zasilanie (PoE/bateria), łączność (LPWAN/Wi‑Fi/Cellular/LoRa/BLE), onboarding i provisioning, bezpieczeństwo (identyfikacja, klucze, firmware), kalibrację, monitoring zdrowia, retencję danych, serwis i wymiany.  
- Poza zakresem: analityka danych (osobne dokumenty), projekt sieci core (oddzielny dokument).


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: wymagania pomiarowe, mapy/plan terenu, lista zatwierdzonych czujników, polityki bezpieczeństwa, wymagania zasilania/łączności, prognoza środowiskowa, SLA.  
- Wyjścia: plan rozmieszczenia i instalacji, konfiguracja sieci/protocol, procedury onboarding/kalibracja, checklisty DoR/DoD, runbook serwisowy, KPI (uptime, data completeness).


## Założenia

- Dostęp do miejsc instalacji jest możliwy.  
- IoT platforma wspiera wybrane protokoły.  
- Zespół serwisowy dostępny.


## Otwarte pytania

- Jak często przeglądać mapę zasięgu i wymieniać baterie?  
- Jak archiwizować dane historyczne?  
- Czy potrzebne są czujniki rezerwowe na wypadek awarii?

## Powiązania (meta)

- Key Documents: smart_building_sensors_deployment, iot_security_reference, iiot_sensor_deployment, maintenance_windows_schedule, access_control_policy.  
- Key Document Structures: lokalizacja, łączność, bezpieczeństwo, kalibracja, monitoring, serwis.  
- Document Dependencies: IoT platform/MQTT broker, device registry, PKI/keys, OTA/firmware system, CMDB/inventory, field service tools.


## Zależności dokumentu

Wymaga: map lokalizacji i zasięgu, zatwierdzonych modeli czujników, polityk kluczy/PKI, dostępnych kanałów łączności, narzędzi do kalibracji, IoT platformy, planu serwisu. Brak = brak DoR.


## Fazy cyklu życia

- Planowanie lokalizacji i łączności.  
- Instalacja i onboarding.  
- Kalibracja i testy odbiorowe.  
- Monitoring i utrzymanie.  
- Serwis, wymiany, dekomisja.



## Struktura sekcji (szkielet)
- Inwentarz i lokalizacje sensorów.
- Łączność i zasilanie (wired/wireless, QoS, RF survey jeśli).
- Provisioning i bezpieczeństwo (identity, klucze, certy, fizyczne zabezp.).
- Montaż i kalibracja (procedury, narzędzia, wartości referencyjne).
- Integracja i testy komunikacji (gateway/edge/cloud/SCADA/MES).
- Testy funkcjonalne i odbiory (kryteria, wzorce, podpisy).
- Dokumentacja i rejestr urządzeń/wersji/FW.
- Szkolenie obsługi i wsparcie.
- Ryzyka i mitigacje.
## Szybkie powiązania

- linkage_index.jsonl (sensor/deployment/plan)  
- iot_security_reference, maintenance_windows_schedule, iiot_sensor_deployment


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Ustal wymagania, wybierz czujniki i łączność.  
2. Zaplanuj lokalizacje/zasilanie; przygotuj onboarding i bezpieczeństwo.  
3. Zainstaluj, skalibruj, przetestuj; uruchom monitoring.  
4. Prowadź serwis i OTA; aktualizuj dokument i linkage_index.


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

- Onboarding: rejestracja i nadanie tożsamości/kluczy czujnikowi.  
- OTA: Over-the-air update firmware.  
- Data completeness: procent spodziewanych próbek, które dotarły.


## Przykłady użycia

- Wdrożenie czujników jakości powietrza w kampusie.  
- Instalacja czujników drgań w fabryce (LTE/PoE).  
- Sieć LoRa dla monitoringu rolniczego.


## Ryzyka i ograniczenia

- Słabe pokrycie łączności → brak danych.  
- Utrata kluczy → ryzyko bezpieczeństwa.  
- Brak kalibracji → dane niewiarygodne.  
- Brak serwisu/OTA → awarie i drift.


## Decyzje i uzasadnienia

- Wybór łączności i zasilania.  
- Polityka kluczy/PKI i rotacji.  
- Kadencja kalibracji i serwisu.  
- Zakres KPI i progów.


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

- Lokalizacja ↔ Łączność ↔ Zasilanie.  
- Onboarding ↔ Bezpieczeństwo ↔ Monitoring zdrowia.  
- Kalibracja ↔ Dane ↔ SLA/KPI.


## Struktura sekcji

1) Wymagania pomiarowe i SLA  
2) Plan lokalizacji i zasilania/łączności  
3) Onboarding (ID, certyfikaty, tematy, payloady)  
4) Bezpieczeństwo i firmware/OTA  
5) Kalibracja i testy odbiorowe  
6) Monitoring zdrowia/danych i alerty  
7) Serwis/wymiany/wycofanie  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Macierz lokalizacja → typ czujnika → łączność → zasilanie.  
- Procedura onboarding (device ID, cert, keys, claim).  
- Checklista kalibracji i testów odbiorowych.  
- Plan OTA/firmware i okna maintenance.  
- KPI: uptime, data completeness, battery health.  
- Runbook serwisowy (wizyta terenowa, RMA).


## Wymagane streszczenia

- Executive summary: zakres wdrożenia, liczba czujników, kluczowe ryzyka.  
- Skrót łączności/zasilania na mapie pokrycia.


## Guidance (skrót)

- Wybieraj łączność adekwatną do zasięgu/energii; testuj site-survey.  
- Używaj certów/kluczy per urządzenie; rotuj i blokuj utracone.  
- Kalibruj przy wdrożeniu i cyklicznie; loguj wyniki.  
- Monitoruj baterie i data completeness; ustaw alerty.  
- Plan OTA z rollbackiem; testuj na małej puli.  
- Dokumentuj w CMDB/inventory; aktualizuj linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Mapy i zasięg łączności ocenione.  
- [ ] Modele czujników zatwierdzone; polityka kluczy/PKI.  
- [ ] IoT platforma i device registry gotowe.  
- [ ] Narzędzia kalibracji i serwisu dostępne.  
- [ ] Plan serwisu/OTA określony.


## Checklisty Definition of Done (DoD)

- [ ] Czujniki zainstalowane i onboardowane; dane spływają.  
- [ ] Kalibracja i testy odbiorowe zaliczone.  
- [ ] Monitoring/alerty działają; KPI w normie.  
- [ ] Dokumentacja/CMDB/linkage_index zaktualizowane.  
- [ ] Plan serwisu i OTA aktywny; brak krytycznych ryzyk.

