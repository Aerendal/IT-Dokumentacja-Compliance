---
title: Procedury kontroli nawadniania
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Procedury kontroli nawadniania


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Standardowe procedury sterowania i monitorowania systemów nawadniania (IoT/field), aby zapewnić poprawne podlewanie, oszczędność wody i bezpieczeństwo urządzeń.


## Zakres i granice

- Obejmuje: harmonogramy i reguły nawadniania, czujniki wilgotności/meteodata, sterowniki/valves, komunikację IoT, bezpieczeństwo (dostęp/aktualizacje), observability (metryki, alerty, DLQ), procedury ręczne/fallback.  
- Poza zakresem: projekt instalacji hydraulicznej (osobny dokument).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: mapy pól/stref, progi wilgotności, prognozy pogody, konfiguracje sterowników, polityka OTA, limity wody/energetyczne, SLA nawadniania.  
- Wyjścia: harmonogram/algorytm nawadniania, konfiguracje sterowników/OTA, alerty/monitoring, procedury ręczne, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: iot_architecture_design, security_edge_ai, observability_edge, ota_update_policy, wymagania_automatyzacji_nawadniania.  
- Key Document Structures: harmonogram/reguły, czujniki, sterowniki/komunikacja, bezpieczeństwo, observability, procedury ręczne.  
- Document Dependencies: IoT sensors, gateway, connectivity (LPWAN/5G/Wi‑Fi), OTA system, CMDB stref.



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
1. Zakres: produkt/partia/proces, normy/standardy, punkty kontrolne.
2. Metody: testy/inspekcje, próbki, narzędzia pomiarowe, kalibracje.
3. Kryteria akceptacji: tolerancje, kategorie defektów, decyzje (accept/rework/reject).
4. Rejestry i śledzenie: karty kontroli, traceability, SPC, raporty defektów.
5. Reakcja na niezgodności: izolacja, CAPA, segregacja, powiadomienia.
6. Utrzymanie jakości: audyty, przeglądy trendów, aktualizacja planów QC.
## Szybkie powiązania

- linkage_index.jsonl (agri/irrigation_control)  
- iot_architecture_design, ota_update_policy, observability_edge


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

1. Zdefiniuj reguły/harmonogramy i progi wilgotności; skonfiguruj czujniki i sterowniki.  
2. Włącz bezpieczeństwo/OTA i monitoring; ustaw alerty.  
3. Przyjmij procedury manual override; zaktualizuj linkage_index i checklisty.


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

- [ ] Dane z czujników wiarygodne; reguły sterowania stosowane; OTA/bezpieczeństwo aktywne.  
- [ ] Alerty/monitoring pokrywają suchość/offline/DLQ; manual override dostępne.  
- [ ] Linkage_index uzupełniony.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Mapy stref, progi wilgotności, konfiguracje sterowników/OTA, kalibracje czujników, alert rules, manual override instrukcje, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Zużycie wody vs cel, % czasu wilgotność w przedziale, uptime sterowników, liczba alertów offline/DLQ, czas reakcji na manual override.

## Kryteria ukończenia

- [ ] System nawadniania ma ustawione reguły, bezpieczeństwo, monitoring i procedury ręczne; dokument powiązany w linkage_index.


## Struktura sekcji

1) Harmonogramy i reguły (wilgotność, ET, prognoza, limity, priorytety stref)  
2) Czujniki i dane (wilgotność, deszcz, temp, kalibracja, walidacja danych, failover)  
3) Sterowniki i komunikacja (valves/pompy, protokoły, retry/store-and-forward, bezpieczeństwo)  
4) Bezpieczeństwo (auth/keys, OTA podpisy, sieć, fizyczny dostęp)  
5) Observability (metryki: wilgotność, zużycie wody, uptime sterowników; alerty; DLQ)  
6) Procedury ręczne/fallback (ręczne otwarcie/zamknięcie, lokalny override, komunikacja)  
7) Załączniki (checklisty, mapy stref, ADR/waiver log)


## Wymagane rozwinięcia

- Algorytm sterowania (wilgotność progowa + ET + prognoza) i parametry; histereza.  
- Lista czujników i ich kalibracja/testy; procedura wymiany/błędnych danych.  
- Retencja/aktualizacja konfiguracji sterowników; OTA plan i rollback.  
- Polityka alertów (suchość/stawka, offline sterownik, DLQ) i thresholdy.  
- Instrukcje manual override dla operatorów.


## Wymagane streszczenia

- Executive: stan systemu nawadniania, kluczowe alerty/risky strefy, zużycie wody vs cel.


## Guidance (skrót)

- Najpierw dane: kalibracja czujników i sanity checks; bez wiarygodnych danych nie steruj.  
- Wykorzystuj prognozę pogody i ET, aby oszczędzać wodę; stosuj histerezę.  
- Zapewnij OTA z rollbackiem; klucze unikalne per sterownik.  
- Monitoruj offline/packet loss; miej manual override.  
- Aktualizuj linkage_index i checklisty po zmianach algorytmu/reguł.


## Checklisty Definition of Ready (DoR)

- [ ] Mapy stref i progi wilgotności dostępne; czujniki zainstalowane/skalibrowane.  
- [ ] Sterowniki połączone, polityka OTA i klucze przygotowane; kanały alertów gotowe.


## Checklisty Definition of Done (DoD)

- [ ] Reguły/harmonogramy wdrożone; monitoring/alerty działają; OTA/bezpieczeństwo aktywne; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] Procedury manual override opisane; checklisty DoR/DoD odhaczone.

