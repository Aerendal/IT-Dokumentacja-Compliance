---
title: Procedury Maintenance Sensorów IIoT
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Procedury Maintenance Sensorów IIoT


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Ujednolicić utrzymanie i serwis sensorów IIoT (kalibracja, czyszczenie, wymiana, firmware) w środowisku przemysłowym.


## Zakres i granice

- Obejmuje: harmonogramy przeglądów, checklisty serwisowe, bezpieczeństwo pracy, firmware/OTA, kalibrację, części zamienne, rejestrowanie zdarzeń, SLA, zależności z produkcją.
- Poza zakresem: projekt sieci/edge (osobne dokumenty), analityka danych (inne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: listy maszyn/assetów, instrukcje OEM, historia awarii, części zamienne, BHP/LOTO, plan produkcji, CMMS konfiguracja.  
- Wyjścia: harmonogram PM/CM, checklisty, zlecenia w CMMS, raporty wykonania, metryki OEE/MTBF/MTTR, linki w linkage_index.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Key Documents: cmms_configuration, safety_lockout_tagout, bhp_policy, oee_optimization_patterns, backup_and_disaster_recovery (jeśli systemy sterowania), incident_response_playbook.  
- Key Document Structures: harmonogramy, checklisty, części, bezpieczeństwo, rejestr/CMMS, metryki/raporty.  
- Document Dependencies: CMMS, magazyn części, BHP procedury, systemy sterowania (SCADA/PLC).
## Zależności dokumentu

- Konsumuje: [dokumenty wejściowe — co musi istnieć zanim ten dokument powstanie]
- Dostarcza do: [dokumenty wyjściowe — co korzysta z tego dokumentu]

## Fazy cyklu życia

- Faza 1: Koncepcja i Wizja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 2: Analiza Wymagań: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 3: Projekt / Design: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 4: Planowanie: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 5: Implementacja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 6: Testowanie / QA: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 7: Bezpieczeństwo / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 8: Wdrożenie / Deployment: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 9: Operacje / Maintenance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
## Struktura sekcji (szkielet)

- Inwentarz i krytyczność sensorów
- Harmonogramy (czasowe/zdarzeniowe) i okna serwisowe
- Checklisty serwisowe per typ sensora
- Kalibracja i walidacja
- Firmware/OTA i kontrola wersji
- Bezpieczeństwo pracy i lockout/tagout
- Rejestrowanie, SLA, eskalacje


## Szybkie powiązania

- IIoT Security, Edge maintenance, Change Management, Incident/Failure response, CMDB.


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
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
1. Zbuduj harmonogram PM/CM i checklisty per maszyna; wprowadź do CMMS.  
2. Zapewnij części, BHP/LOTO, pozwolenia; wykonuj i rejestruj prace.  
3. Raportuj metryki, aktualizuj plan i linkage_index; odhacz DoR/DoD.
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
- Harmonogramy PM/CM, checklisty, karty pracy, stany magazynowe, raporty OEE/MTBF/MTTR, audyty BHP/LOTO, ADR/waiver log.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości
- OEE, MTBF, MTTR, liczba awarii krytycznych, poziom zapasu części krytycznych, % prac PM wykonanych on-time.
## Kryteria ukończenia
- [ ] Procedury maintenance maszyn wdrożone, metryki monitorowane, dokument powiązany w linkage_index.
## Wejścia

- Inwentarz sensorów (typ, lokalizacja, krytyczność), manuale producentów, historia awarii, wymagania BHP.


## Wyjścia

- Plan przeglądów (czas/zdarzenia), checklisty operacyjne, rejestr maintenance i metryki niezawodności.



## Jak używać (checklista)

- Uzupełnij inwentarz i krytyczność; przypisz właścicieli.
- Zdefiniuj harmonogram: co ile dni/zgodnie z cyklami pracy lub alertami.
- Stwórz checklisty per typ sensora (czyszczenie, kalibracja, test sygnału, OTA).
- Ustal rejestr prac (czas, części, osoba, wynik) i metryki niezawodności.
- Zapewnij procedury BHP i lockout/tagout dla stref niebezpiecznych.


## Wymagane rozwinięcia / powiązania

- Wzory checklist, instrukcje producentów, SOP BHP, szablon rejestru maintenance.


## Kryteria DoR

- Pełny inwentarz z lokalizacją i krytycznością.
- Dostęp do manuali i narzędzi (OTA, kalibracja).


## Kryteria DoD

- Harmonogram i checklisty zatwierdzone; rejestr działa.
- Pierwszy cykl maintenance wykonany i odnotowany.


## Artefakty

- Checklisty (MD/CSV), plan przeglądów, rejestr prac, logi OTA, raport kalibracji.


## Walidacja

- Losowe audyty wykonanych prac vs rejestr.
- Test po maintenance: odczyt, dryft, komunikacja.


## Metryki

- MTBF/MTTR sensorów, % wykonanych przeglądów w SLA.
- Liczba incydentów po maintenance, wskaźnik kalibracji poza tolerancją.


## Utrzymanie

- Przegląd planów kwartalnie, aktualizacja po zmianie procesu/środowiska.
- Aktualizacja firmware listy kompatybilności.


## Zakończenie

Procedury zapewniają przewidywalną pracę sensorów IIoT; utrzymuj je z aktualnymi harmonogramami, OTA i rejestrem zdarzeń.
