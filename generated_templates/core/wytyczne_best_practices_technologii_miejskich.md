---
title: Wytyczne best practices technologii miejskich
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Wytyczne best practices technologii miejskich


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zbiór praktyk dla systemów smart city (IoT, dane miejskie, bezpieczeństwo, prywatność, SLA, etyka) umożliwiający spójną architekturę i operacje usług miejskich.


## Zakres i granice

- Obejmuje: sieci i sensory IoT (LPWAN/5G/Wi‑Fi/mesh), edge/gateway, model danych miejskich, integracje (open data, API miejskie, ITS, transport, energia, środowisko), bezpieczeństwo i prywatność (PII/RTLS), observability i SLO, ciągłość działania/BCP/DR, etyka/transparentność i zgodność regulacyjna.  
- Poza zakresem: polityki urbanistyczne i prawo lokalne (referencje tylko), zarządzanie danymi zdrowotnymi (oddzielne regulacje), budżet/finansowanie.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: inwentarz sensorów i sieci, mapy integracji systemów miejskich, klasy danych i PII, wymagania SLA/SLO, profile ruchu (dobowe/sezonowe), polityki privacy/ethics, plany kryzysowe miasta.  
- Wyjścia: wzorce architektury IoT/edge, wymagania bezpieczeństwa i prywatności, plan observability, procedury BCP/DR, guidance etyczny, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: architektura_platformy_smart_city, urban_data_platform_design, api_gateway_architecture, security_privacy_policy, incident_response_retail (adaptacja L1/L2), backup_and_disaster_recovery, monitoring_strategy, risk_register.  
- Key Document Structures: IoT/edge, model danych, integracje, bezpieczeństwo/prywatność, observability/SLO, BCP/DR, etyka/transparentność.  
- Document Dependencies: sieć miejska i zasilanie, rejestr sensorów/CMDB, PKI/klucze urządzeń, open data portal, SOC/CSIRT miejski, przepisy (RODO, drony, ITS).



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (smart_city/best_practices)  
- architektura_platformy_smart_city, urban_data_platform_design, security_privacy_policy, monitoring_strategy, backup_and_disaster_recovery


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

1. Zweryfikuj listę urządzeń/sieci i klasy danych; zidentyfikuj wymagania prawne.  
2. Wypełnij sekcje architektury, bezpieczeństwa, observability i BCP/DR dla Twojego miasta/projektu.  
3. Dodaj powiązania w linkage_index i odhacz checklisty DoR/DoD.


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

- [ ] Dane PII mają kontrole prywatności; edge buffering i podpisy aktywne.  
- [ ] SLO/alerty pokrywają kluczowe usługi; BCP/DR obejmuje brak zasilania/łączności.  
- [ ] Rollout/pilotaż i rollback są udokumentowane; powiązania w linkage_index działają.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Diagramy sieci/edge, katalog danych, polityki PKI, DPIA, playbooki awaryjne, SLO/SLA, open data publishing rules, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Dostępność usług miejskich vs SLO, % urządzeń z aktualnym certyfikatem, opóźnienie danych, liczba incydentów prywatności, MTTR dla awarii sieci/energii.

## Kryteria ukończenia

- [ ] Dokument umożliwia bezpieczne i odporne wdrożenia smart city (IoT, dane, SLO, BCP/DR, etyka) i jest osadzony w linkage_index.


## Struktura sekcji

1) Architektura IoT/edge i łączność (LPWAN/5G/mesh, zarządzanie urządzeniami, OTA)  
2) Model danych i integracje (API, open data, normalizacja, wersjonowanie, katalog danych)  
3) Bezpieczeństwo i prywatność (PII, RTLS, szyfrowanie, PKI, segmentacja, klucze urządzeń)  
4) Observability i SLO (metryki sensora, zdrowie sieci, trace API, syntetyki usług)  
5) BCP/DR i odporność (zasilanie, redundancja łącz, buffering edge, recovery playbook)  
6) Etyka i transparentność (minimalizacja danych, DPIA, dostęp obywateli, audyty)  
7) Operacje i rollout (prowizjonowanie urządzeń, certyfikaty, inspekcje terenowe, pilotaże)  
8) Załączniki i decyzje (ADR, waiver log, mapy ryzyka)


## Wymagane rozwinięcia

- Klasyfikacja danych (PII/nie‑PII/geo) i zasady retencji/anonimizacji.  
- Proces provisioningu urządzeń (klucze, certyfikaty, rotacja, zgubione urządzenia).  
- SLO/SLA dla usług miejskich (dostępność, opóźnienie, kompletność danych) i alarmy.  
- Scenariusze awaryjne (blackout, brak łączności, klęski żywiołowe) i ścieżki degradacji.  
- Rejestr wyjątków etycznych/prawnych, publikacja danych do open data z filtrami prywatności.


## Wymagane streszczenia

- Executive: pokrycie bezpieczeństwa/prywatności, stan sieci IoT, główne ryzyka i plan BCP/DR.


## Guidance (skrót)

- Domyślnie edge bufferuje i podpisuje dane; backpressure i anti‑replay obowiązkowe.  
- PKI per urządzenie, rotacja kluczy, zero‑touch provisioning, segmentacja ruchu IoT.  
- SLO per usługa (np. czujnik jakości powietrza, ITS) i mapowanie alertów do dyżurów L1/L2.  
- DPIA dla strumieni z PII/RTLS; minimalizacja i maskowanie przed publikacją open data.  
- Pilotaż w małym obszarze → progresywny rollout; każde urządzenie musi mieć owner i lokalizację w CMDB.


## Checklisty Definition of Ready (DoR)

- [ ] CMDB sensorów/sieci i klasy danych dostępne; wymagania prawne znane.  
- [ ] Uzgodnione SLO usług miejskich oraz polityki bezpieczeństwa/prywatności.  
- [ ] Zdefiniowany proces pilotażu i rollback.


## Checklisty Definition of Done (DoD)

- [ ] Sekcje wypełnione, SLO/alerty opisane, ADR/waivery zapisane, linkage_index zaktualizowany.  
- [ ] Plan BCP/DR i playbook recovery gotowe; proces provisioningu i rotacji kluczy opisany.  
- [ ] Status/metadane aktualne; checklisty DoR/DoD odhaczone.

