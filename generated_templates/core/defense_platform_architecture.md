---
title: Defense Platform Architecture
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Defense Platform Architecture


## Metadane

- Właściciel: Solution Architect
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje architekturę platformy obronnej (mission / C2 / ISR / sensor‑to‑shooter) zapewniającą bezpieczeństwo, odporność i interoperacyjność. Określa domeny funkcjonalne, integracje, wymagania bezpieczeństwa, sieci, dane, oprogramowanie i operacje.


## Zakres i granice

- Obejmuje: domeny (C2, komunikacja, sensory, efektory), sieć (tactical/edge/cloud), bezpieczeństwo (zero trust, szyfrowanie, COMSEC), dane (formaty, wymiana, klasyfikacja), integracje z systemami sojuszniczymi/legacy, ciągłość działania, monitoring i testy w warunkach polowych/lab, zgodność regulacyjną i export control.
- Poza zakresem: szczegółowy projekt sprzętu, specyfikacje efektorów, kontrakty zakupowe (oddzielne dokumenty).


## Użytkownicy i interesariusze
- **Solution / Enterprise Architect** — projektuje i zatwierdza architekturę
- **Tech Lead** — odpowiada za spójność techniczną implementacji
- **Product Owner** — definiuje wymagania biznesowe wchodzące na wejście
- **Development Team** — implementuje na podstawie projektu

## Wejścia i wyjścia

- Wejścia: wymagania misji i scenariusze, profile zagrożeń, mapy łączności, katalog interfejsów/danych (Link 16, STANAG, NATO/US DoD), wymagania bezpieczeństwa/klasyfikacji, ograniczenia środowiskowe (EMI/EMC, rugged), polityki bezpieczeństwa narodowego.
- Wyjścia: model architektury (logiczny/fizyczny), wzorce integracji, wymagania bezpieczeństwa i segmentacji, standardy danych/interfejsów, plan testów (lab/field), plan ciągłości i degradacji, decyzje technologiczne, RACI i roadmapa wdrożeń.


## Założenia

- Dostępność kluczy/COMSEC i PKI.  
- Zapewnione zasilanie/zapas energii dla edge.  
- Możliwość testów w cyber range i polu.


## Otwarte pytania

- Jakie są ograniczenia prawne/eksportowe dla partnerów?  
- Czy wymagany jest tryb full offline dla konkretnych scenariuszy?  
- Jak zarządzać aktualizacjami/patchami w środowiskach odciętych?


## Powiązania (meta)

- Key Documents: mission_requirements, threat_model_defense, comms_architecture, zero_trust_architecture, data_exchange_standards, continuity_plan, interoperability_matrix.
- Key Document Structures: domeny funkcjonalne, sieć/łączność, bezpieczeństwo, dane/interfejsy, operacje/testy, ciągłość i degradacja.
- Document Dependencies: klasyfikacja danych, PKI/COMSEC, radio/mesh/sat, edge compute, SIEM/SOAR, CM/IM, supply chain assurance.


## Zależności dokumentu

Wymaga: zaakceptowanych wymagań misji, profili zagrożeń, polityk klasyfikacji i łączności, listy interfejsów/standardów, uzgodnionych założeń zero trust/segregacji. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja i model referencyjny.  
- Warianty misji/teatru i integracje partnerskie.  
- Testy lab/field, cyber range, red/blue/purple team.  
- Operacje, utrzymanie, aktualizacje, audyty, releasy bezpieczeństwa.



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

- linkage_index.jsonl (defense/platform/architecture)  
- comms_architecture, zero_trust_architecture, data_exchange_standards, continuity_plan, interoperability_matrix


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

1. Zbierz wymagania misji i profile zagrożeń; uzupełnij domeny i mapy łączności.  
2. Zdefiniuj architekturę sieci/danych/bezpieczeństwa i katalog interfejsów.  
3. Zaplanuj testy lab/field, tryby degradacji i roadmapę; aktualizuj DoR/DoD.


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

- Interoperacyjność: zdolność do bezpiecznej wymiany danych/komend między systemami sojuszniczymi.  
- Degraded mode: utrzymanie funkcji krytycznych przy ograniczonej łączności/zapasie energii.  
- Zero Trust: weryfikacja tożsamości i stanu każdego elementu/połączenia, ciągła autoryzacja.


## Przykłady użycia

- Projekt architektury C2 dla ćwiczeń wielonarodowych.  
- Integracja nowych sensorów ISR w istniejącej sieci taktycznej.  
- Planowanie degradacji i DR dla baz forward operating.


## Ryzyka i ograniczenia

- Ograniczona przepustowość/latencja łącz taktycznych.  
- Zależność od dostawców sprzętu/crypto (supply chain).  
- Ryzyka klasyfikacji i eksportu technologii.


## Decyzje i uzasadnienia

- Wybór standardów łączności i formatów (Link 16/STANAG/IP).  
- Poziomy segmentacji i zasady wymiany danych między domenami.  
- Zakres edge vs cloud przy wymaganiach latency/odporności.


## Powiązania z innymi dokumentami

- comms_architecture — szczegół łączności.  
- zero_trust_architecture — kontrola dostępu/segregacja.  
- continuity_plan — DR/BCP i degradacja.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- NATO STANAG / DoD (interfejsy, bezpieczeństwo).  
- Normy kryptograficzne/COMSEC, polityki klasyfikacji i export control.

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

- Wymagania misji → Domeny funkcjonalne → Architektura sieci/danych → Bezpieczeństwo → Testy/ciągłość.  
- Integracje/standardy → Interoperacyjność → Scenariusze testowe.  
- Klasyfikacja danych → Segmentacja/ZTNA → Operacje/monitoring.


## Struktura sekcji

1) Kontekst misji i cele architektury  
2) Domeny funkcjonalne (C2/ISR/efektory/wsparcie) i krytyczne scenariusze  
3) Architektura sieci i łączności (warstwy, segmenty, łącza, QoS, degradacja)  
4) Architektura danych i interfejsów (formaty, standardy, katalog, semantyka)  
5) Bezpieczeństwo/zero trust (identity, crypto, segmentacja, supply chain, hardening)  
6) Edge/Cloud/Hybrid compute (deployment patterns, latency, resiliencja)  
7) Monitorowanie, logging, cyber defense (SIEM/SOAR, detekcja, response)  
8) Ciągłość działania i degradacja (fallback, disconnected ops, DR/BCP)  
9) Testy i walidacja (lab/field, interoperacyjność, cyber, performance)  
10) Roadmapa, decyzje, ryzyka i otwarte punkty


## Wymagane rozwinięcia

- Mapy łączności i segmentacji (mission/secret/unclassified).  
- Katalog interfejsów i standardów (Link 16, STANAG, IP crypto).  
- Scenariusze degradacji/fallback i checklisty DR.  
- Model danych i klasyfikacji z zasadami wymiany/udostępniania.


## Wymagane streszczenia

- Executive view: domeny, top ryzyka, decyzje technologiczne, gotowość interoperacyjna.  
- Jednostronicowa mapa sieci/segmentacji z punktami kontroli bezpieczeństwa.


## Guidance (skrót)

- Projektuj zero trust od edge po cloud; minimalizuj zaufanie w łączności taktycznej.  
- Standaryzuj interfejsy i formaty; utrzymuj katalog i testy interoperacyjności.  
- Zawsze planuj tryb degraded/disconnected; zapewnij lokalne buforowanie i resync.  
- Testuj w warunkach polowych i cyber range, nie tylko w labie.  
- Ścieżka zgodności: export control, klasyfikacja, supply chain assurance.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania misji i profile zagrożeń zatwierdzone.  
- [ ] Katalog interfejsów/standardów i klasyfikacja danych dostępne.  
- [ ] Założenia zero trust/segmentacji uzgodnione.  
- [ ] Plan testów (lab/field/cyber) z ownerami.  
- [ ] Ścieżki zgodności (export control/klasyfikacja) określone.


## Checklisty Definition of Done (DoD)

- [ ] Architektura opisana, mapy łączności/segmentacji dołączone.  
- [ ] Standardy danych/interfejsów i testy interoperacyjności zdefiniowane.  
- [ ] Plany degradacji/DR i runbooki awaryjne dołączone.  
- [ ] Ryzyka/decisions udokumentowane; status/wersja/data zaktualizowane.  
- [ ] Powiązania z innymi dokumentami w linkage_index uzupełnione.

