---
title: Camera System Setup
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Camera System Setup


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje konfigurację systemu kamer (CCTV/IPC) wraz z siecią, zasilaniem, przechowywaniem, bezpieczeństwem i zgodnością prywatności. Ma zapewnić powtarzalne wdrożenia, zgodność regulacyjną i możliwość audytu.


## Zakres i granice

- Obejmuje: dobór lokalizacji kamer, okablowanie/PoE, sieć/VLAN, NVR/VMS, retencję i storage, jakość obrazu (FPS/bitrate/rozdzielczość), zabezpieczenia (hasła, certy, segmentacja), dostęp użytkowników, integracje (alarmy, access control), procedury testów/odbioru, dokumentację i oznaczenia prywatności.
- Poza zakresem: fizyczny montaż wykonywany przez wykonawcę (może być w załączniku), analiza incydentów (oddzielne playbooki), zaawansowana analityka wideo (oddzielne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: plan obiektu, strefy ryzyka, wymagania prawne (RODO, lokalne), polityka retencji, profile jakości (dzień/noc), wymagania sieci (PoE/UPS), lista urządzeń i firmware, konta/użytkownicy, integracje (ACS, alarmy), test plan.
- Wyjścia: plan rozmieszczenia kamer, konfiguracja sieci/VLAN/PoE, konfiguracja kamer i VMS/NVR, retencja i storage, konta/role, checklisty odbioru i testów, etykiety/oznaczenia prywatności.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: physical_security_policy, privacy_camera_policy, network_segmentation, backup_and_retention, incident_response_video.
- Key Document Structures: lokalizacje, sieć, konfiguracja, bezpieczeństwo, testy, dokumentacja.
- Document Dependencies: CMDB asset, IAM, storage/backup, UPS/Power, change management.


## Zależności dokumentu

Wymaga planu obiektu i stref (publiczne/prywatne), polityki retencji/prywatności, listy urządzeń/firmware, dostępów do sieci/PoE/UPS, kont VMS, oraz zasad audytu dostępu. Bez tego DoR otwarte.


## Fazy cyklu życia

- Planowanie: strefy, wymagania prawne, budżet, wybór sprzętu.
- Implementacja: okablowanie/PoE/VLAN, montaż, konfiguracja kamer/VMS.
- Testy/odbiór: checklisty, nagrania testowe, weryfikacja retencji/alertów.
- Operacje: monitoring stanu, rotacja haseł/certów, patching firmware, audyt dostępu.
- Decommission: usunięcie/wyczyszczenie danych, aktualizacja dokumentacji/CMDB.



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
- support-system-setup
- backup-system-setup
- help-desk-system-setup
- energy-management-system-setup
- system-sustainment

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.
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

- Lokalizacje → Konfiguracja jakości → Storage/retencja.
- Sieć/VLAN/PoE → Bezpieczeństwo → Dostępy użytkowników.
- Testy/odbiór → Akceptacja → Operacje/monitoring.


## Struktura sekcji

1) Lokalizacje kamer i cele (plan obiektu, strefy, kąty, oświetlenie)  
2) Sieć/zasilanie (VLAN, PoE, UPS, QoS, przepustowość)  
3) Konfiguracja kamer (rozdzielczość, FPS, bitrate, kodek, WDR/IR, profiles)  
4) VMS/NVR (retencja, storage, backup, replica, health checks)  
5) Bezpieczeństwo (hasła/certy, MFA do VMS, segmentacja, hardening, aktualizacje FW)  
6) Dostępy i role (operator, auditor, export), logi/audyt, proces nadawania/odbierania  
7) Integracje (ACS/alarmy, webhooki, API, time sync)  
8) Prywatność i oznaczenia (tablice informacyjne, maski prywatności, polityka retention)  
9) Testy i odbiór (checklisty: obraz, noc, failover, export, alerty)  
10) Dokumentacja i CMDB (ID urządzeń, firmware, lokalizacja, schematy, zdjęcia)  
