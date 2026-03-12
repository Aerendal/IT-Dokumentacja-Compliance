---
title: Maritime Emergency Response
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Maritime Emergency Response


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan reagowania na sytuacje awaryjne na morzu/akwenach: ratownictwo, kolizje, pożary, wycieki, ewakuacje, łączność i koordynacja służb. Ma zminimalizować straty życia/środowiska i czas reakcji.


## Zakres i granice

- Obejmuje: typy zdarzeń (SAR, pożar, kolizja, wyciek, grounding), role i łączność (VHF, AIS, sat), procedury alarmowania, koordynację z MRCC, podział stref odpowiedzialności, środki (statki, RIB, helikoptery, boje, sorbenty), bezpieczeństwo załóg, ewakuacje, medyczne MRO, scenariusze pogodowe/noc, raportowanie do regulatorów, ćwiczenia i przeglądy.  
- Poza zakresem: szczegółowe SOP jednostek (oddzielne), prawo morskie w pełnym zakresie (linki).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: mapy/strefy SAR, lista środków i kontaktów (MRCC, straż, policja, medyczne), procedury VHF/AIS/GMDSS, plany tankowania/ładunków, listy pasażerów/crew, dane pogodowe, oceny ryzyka, wymagania regulatorów.  
- Wyjścia: plan reagowania (checklisty, schemat łączności, RACI), karty zdarzeń, wzory raportów do MRCC/regulatorów, harmonogram ćwiczeń, aktualizacje risk register.


## Założenia

- AIS/VHF/GMDSS działają.  
- Zasoby ratunkowe są utrzymywane i dostępne.  
- Zespoły przeszkolone i PPE dostępne.


## Otwarte pytania

- Jak integrować dane AIS/pogoda do wczesnego ostrzegania?  
- Jakie są lokalne wymagania raportowe (czasy, format)?  
- Jak często aktualizować scenariusze ćwiczeń?


## Powiązania (meta)

- Key Documents: port_operations_plan, safety_compliance, oil_spill_response_plan, mass_rescue_operations, communication_plan_emergency, incident_response_runbook.  
- Key Document Structures: zdarzenia, łączność, zasoby, procedury, raporty, ćwiczenia.  
- Document Dependencies: AIS/VHF/GMDSS systemy, listy kontaktów, sprzęt SAR/pożarowy, pogoda, CMMS/maintenance.


## Zależności dokumentu

Wymaga: aktualnych kontaktów i list zasobów, map stref, procedur łączności, list pasażerów/crew i planów ładunków, polityk bezpieczeństwa, wymogów regulatorów. Braki = DoR otwarte.


## Fazy cyklu życia

- Przygotowanie (listy kontaktów, zasoby, training).  
- Reakcja (alarmowanie, łączność, akcja, raporty).  
- Po zdarzeniu (debrief, raporty, aktualizacje).  
- Ćwiczenia okresowe.



## Struktura sekcji (szkielet)
- Scenariusze i role.
- Kanały i eskalacje (progi, redundancja, kolejność).
- Integracje (HR/IDP/CMDB/location services).
- Szablony komunikatów i wielojęzyczność.
- Bezpieczeństwo/prywatność (PII, logging, retention).
- Dostępność/DR (redundancja, fallback, testy failover).
- Runbooki i testy/ćwiczenia.
- Monitoring SLA i raporty po incydencie.
- Ryzyka i mitigacje.
## Szybkie powiązania

- linkage_index.jsonl (maritime/emergency/response)  
- oil_spill_response_plan, mass_rescue_operations, port_operations_plan, communication_plan_emergency


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

1. Przygotuj kontakty/zasoby i łączność; rozdystrybuuj checklisty.  
2. W zdarzeniu stosuj procedury per typ; loguj działania i raporty.  
3. Po zdarzeniu debrief, wnioski i aktualizacja DoR/DoD i linkage_index.


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

- SAR: Search and Rescue.  
- MRCC: Maritime Rescue Coordination Centre.  
- MRO: Mass Rescue Operations.


## Przykłady użycia

- Pożar na statku w porcie; koordynacja z strażą pożarną i holownikami.  
- Wyciek paliwa; deploy booms/sorbent, zawiadomienie regulatora.  
- Kolizja jednostek; SAR, medyczne, clearing toru wodnego.


## Ryzyka i ograniczenia

- Brak łączności lub przestarzałe kontakty → opóźnienia.  
- Zła pogoda ogranicza zasoby (helikoptery).  
- Brak ćwiczeń → chaos w realnym zdarzeniu.


## Decyzje i uzasadnienia

- Priorytety zasobów przy zdarzeniach równoległych.  
- Kanały alternatywne łączności.  
- Kiedy angażować regulator/wojsko/partnerów.


## Powiązania z innymi dokumentami

- safety_compliance — zgodność i bezpieczeństwo.  
- port_operations_plan — koordynacja operacji.  
- incident_response_runbook — procesy ogólne.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- SOLAS/GMDSS, lokalne przepisy SAR, przepisy środowiskowe (wycieki).  
- Wewnętrzne polityki bezpieczeństwa.

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
- Checklisty scenariuszy, logi/test reports, komunikacja (status/alerty), backup/snapshot dowody, zdjęcia/raporty, action plan, waiver log, ADR log.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości
- Osiągnięcie RTO/RPO, czas ewakuacji/reakcji, liczba luk i czas ich zamknięcia, liczba retestów, bezpieczeństwo podczas ćwiczeń (incydenty=0), terminowość raportu.
## Kryteria ukończenia
- [ ] Testy przeprowadzone, wyniki i luki opisane, plan retestów ustawiony; wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

- Typ zdarzenia → Procedury → Zasoby → Raportowanie.  
- Łączność → Koordynacja → Decyzje i bezpieczeństwo.  
- Ćwiczenia → Wnioski → Aktualizacje planu.


## Struktura sekcji

1) Zakres i definicje zdarzeń  
2) RACI i kontakty (MRCC, służby, operatorzy)  
3) Łączność i procedury alarmowe (VHF/AIS/GMDSS, kanały, kody)  
4) Procedury per typ zdarzenia (SAR, pożar, wyciek, kolizja, grounding)  
5) Zasoby i logistyka (statki, RIB, helikoptery, boje/sorbenty, medyczne)  
6) Bezpieczeństwo załóg i ewakuacje (MRO, PPE, muster)  
7) Raportowanie i dokumentacja (MRCC/regulator, log zdarzeń)  
8) Ćwiczenia i testy (harmonogram, scenariusze, wnioski)  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Checklisty procedur per zdarzenie.  
- Schemat łączności i kanały zapasowe.  
- Szablony raportów (initial/final).  
- Harmonogram ćwiczeń i lessons learned.


## Wymagane streszczenia

- Executive snapshot: gotowość zasobów, ostatnie ćwiczenia, top ryzyka.  
- Krótka karta łączności (kanały, kontakty).


## Guidance (skrót)

- Utrzymuj listy kontaktów i zasobów aktualne; testuj łączność.  
- Ćwicz scenariusze z pogodą noc/niska widoczność.  
- Dokumentuj każde zdarzenie; raportuj w czasie wymaganym przez regulatora.  
- Bezpieczeństwo załóg priorytetem; PPE i muster.  
- Po zdarzeniu wykonaj debrief i zaktualizuj plan.


## Checklisty Definition of Ready (DoR)

- [ ] Kontakty i zasoby zaktualizowane; kanały łączności przetestowane.  
- [ ] Checklisty procedur dostępne na jednostkach/centrach.  
- [ ] Wymogi raportowania znane; szablony przygotowane.  
- [ ] Harmonogram ćwiczeń ustalony.  
- [ ] PPE i sprzęt ratunkowy sprawdzony.


## Checklisty Definition of Done (DoD)

- [ ] Zdarzenie obsłużone; raport initial/final wysłany.  
- [ ] Logi działań i łączności zapisane; status/wersja/data uzupełnione.  
- [ ] Lessons learned i aktualizacje procedur wykonane; linkage_index uzupełniony.  
- [ ] Ćwiczenia/inspekcje zaplanowane po zdarzeniu (jeśli wymagane).  
- [ ] Ryzyka i decyzje odnotowane w risk register.

