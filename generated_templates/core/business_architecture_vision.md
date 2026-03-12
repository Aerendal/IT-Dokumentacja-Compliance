---
title: Business Architecture Vision
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Business Architecture Vision

## Metadane
- Właściciel: Solution Architect
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Opisuje wizję architektury biznesowej: model domen/capability, procesy end‑to‑end, mapę wartości i strumienie wartości, role/interesariuszy, mierniki i governance oraz powiązanie z architekturą danych/IT. Określa trade‑offy i kryteria akceptacji zmian.


## Zakres i granice
- Obejmuje: mapę capability i domen, procesy end‑to‑end i strumienie wartości, role i RACI, KPI/KRI biznesowe, zależności między domenami, interfejsy do IT/ danych, zasady zmian (governance), varianty target/interim, ryzyka/regulacje.
- Poza zakresem: szczegółowe procesy operacyjne L4/L5, low-level design IT.



## Wejścia i wyjścia
- Wejścia: strategia firmy/produktów, analizy rynku/klientów, KPI finansowe/operacyjne, mapa procesów as-is, katalog capability, regulacje, ograniczenia operacyjne, insighty z danych, portfel inicjatyw.
- Wyjścia: target/interim mapa capability/domen, mapy procesów/strumieni wartości (E2E), RACI, KPI/KRI, powiązania z architekturą danych/IT, plan zmian i kolejność transformacji, ADR/trade‑offy, ryzyka i mitigacje.



## Powiązania (meta)
- Key Documents: enterprise_architecture_vision, product_strategy_document, operating_model, data_architecture_vision, integration_strategy, security_strategy, process_architecture, value_stream_mapping, risk_register.
- Key Document Structures: capability → proces/strumień wartości → systemy/dane → KPI/KRI → governance.
- Document Dependencies: CMDB/system inventory, katalog danych/capability, regulacje branżowe, polityki compliance, plany transformacji/portfel.
- RACI: Business Architecture (owner), Domain Owners, Process Owners, Product/Strategy, Data, IT/Architecture, Compliance, Finance.
- Standardy/compliance: branżowe regulacje procesowe, dane (PII/PCI/PHI), zasady segregacji obowiązków.

## Zależności dokumentu
- Upstream: strategia, regulacje, portfel inicjatyw, dane finansowe/operacyjne, polityki danych/compliance.
- Downstream: architektura IT/danych, roadmapy produktowe, zmiany procesów, szkolenia i komunikacja, finanse/controlling.
- Zewnętrzne: regulatorzy, partnerzy ekosystemu (B2B/B2C), outsourcerzy procesów.



## Powiązania sekcja↔sekcja
- Capability/domena → Proces/strumień wartości → Systemy/dane → KPI/KRI → Governance i zmiany.
- Regulacje/ryzyka → Kontrole procesowe → Zmiany w systemach/danych → Audyt/monitoring.



## Fazy cyklu życia
- Discovery: inwentaryzacja capability/procesów, mapowanie E2E i problemów, definicja KPI/KRI.
- Design: target/interim mapa capability/procesów/strumieni, RACI, zależności z IT/danymi, ADR/trade‑offy.
- Review: business/architecture/compliance/finance; koszty/benefity, ryzyka/regulacje.
- Implementation & Change: wdrożenie zmian procesowych/systems, komunikacja i szkolenia, testy UAT/procesowe.
- Rollout & Ops: monitorowanie KPI/KRI, audyty, doskonalenie ciągłe.




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
## Struktura sekcji (szkielet)
1) Streszczenie i cele biznesowe (KPI/KRI)
2) Zakres, założenia, ograniczenia (regulacje, SOX/segregacja, budżet/czas)
3) Mapa capability i domen (as-is vs target/interim, właściciele)
4) Strumienie wartości i procesy E2E (pain points, metryki)
5) Powiązanie z systemami i danymi (system map, dane krytyczne, integracje)
6) RACI i governance (fora decyzyjne, cadence, zasady zmian)
7) KPI/KRI i mierzenie (dashboards, cadence, odpowiedzialność)
8) Plan transformacji (fazy, priorytety, zależności, quick wins)
9) Ryzyka/regulacje i kontrolki (procesowe/techniczne), założenia/dependencies
10) Decyzje (ADR) i otwarte pytania



## Wymagane rozwinięcia
- Mapa capability/domen (as-is/target/interim), value stream mapy, procesy E2E (L2/L3), system map.
- RACI i governance (fora, właściciele, cadence), ADR dla zmian strukturalnych.
- Plan transformacji: fazy, mierniki sukcesu, zależności z IT/danymi, koszty/benefity.
- Kontrolki procesowe/zgodność (segregacja obowiązków, audyt, privacy).



## Wymagane streszczenia
- Executive summary: mapa capability/strumieni, cele/KPI, top decyzje, ryzyka, plan faz.
- One-pager: target/interim capability map, value streams, główne zależności z IT/danymi, timeline.



## Guidance (skrót)
- DoR: capability/procesy zinwentaryzowane; KPI/KRI określone; regulacje/ograniczenia spisane; właściciele domen/procesów wskazani; zależności IT/dane znane.
- DoD: mapa capability/domen target/interim, value streams E2E, RACI i governance, KPI/KRI i plan pomiaru, plan transformacji z zależnościami, ryzyka/założenia; metadane aktualne; dokument w linkage_index.
- Spójność: każda capability ma właściciela i KPI; value stream ma mierniki i systemy/dane; zmiany mają governance i kontrolki zgodności.



## Szybkie powiązania
- enterprise_architecture_vision, product_strategy_document, operating_model, data_architecture_vision, integration_strategy, security_strategy, process_architecture, value_stream_mapping, risk_register

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty Definition of Ready (DoR)
- [ ] Capability/procesy zinwentaryzowane; KPI/KRI zdefiniowane; regulacje/ograniczenia znane.
- [ ] Właściciele domen/procesów wskazani; zależności z IT/danymi spisane.

## Checklisty Definition of Done (DoD)
- [ ] Target/interim capability map, value streams E2E, RACI/governance, KPI/KRI opisane.
- [ ] Plan transformacji z zależnościami IT/dane, koszt/benefit, ryzyka/założenia; dokument w linkage_index.

## Definicje robocze
- Capability — zdolność biznesowa wspierająca cele (ludzie+proces+technologia).
- Value stream — end‑to‑end przepływ wartości dla klienta/rynku; mierzalny czas/przepustowość/jakość.
- Governance — zasady decyzyjne i odpowiedzialności dla zmian w capability/procesach/systemach.

## Przykłady użycia
- Transformacja operacji sprzedaży: target capability map (Lead→Order→Billing), value stream z KPI (cycle time, conversion), zależności z CRM/ERP/DWH, plan fazowy.
- Optymalizacja obsługi klienta: value stream Case→Resolution, capability Support/Knowledge/Analytics, integracja kanałów, KPI (AHT, CSAT, FCR), governance zmian.

## Artefakty powiązane
- Capability map, value stream mapy, RACI/governance, system map, KPI/KRI dashboard, ADR log, plan transformacji.

## Weryfikacja spójności
- [ ] Każda capability ma właściciela, KPI/KRI i powiązanie z systemami/danymi.
- [ ] Value streams mają mierniki i kontrolki; zależności z IT/danymi są opisane.
- [ ] Plan transformacji ma fazy, zależności, koszty/benefity i kontrolki zgodności.

## Ryzyka i ograniczenia
- [Ryzyko 1 — wpływ i sposób ograniczenia]
- [Ryzyko 2 — wpływ i sposób ograniczenia]

## Decyzje i uzasadnienia
- [Decyzja 1 — uzasadnienie]
- [Decyzja 2 — uzasadnienie]

## Założenia
- [Założenie 1]
- [Założenie 2]

## Otwarte pytania
- [Pytanie 1]
- [Pytanie 2]

## Powiązania z innymi dokumentami
- [Dokument A] — [typ relacji] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów
- [Dokument X → Sekcja Y] — [powód powiązania]
- [Dokument Z → Sekcja W] — [powód powiązania]

## Słownik pojęć w dokumencie
- [Pojęcie 1] — [definicja i źródło]
- [Pojęcie 2] — [definicja i źródło]
- [Pojęcie 3] — [definicja i źródło]

## Wymagane odwołania do standardów
- [Standard 1] — [sekcja/fragment, którego dotyczy]
- [Standard 2] — [sekcja/fragment, którego dotyczy]

## Mapa relacji sekcja→sekcja
- [Sekcja A] -> [Sekcja B] : [typ relacji]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument
- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji
- [Wejście] → [Sekcja źródłowa] → [Sekcja rozwinięcia] → [Wyjście]
- [Wejście] → [Sekcja źródłowa] → [Sekcja streszczenia] → [Wyjście]

## Weryfikacja spójności
- [ ] Czy wszystkie ścieżki informacji są zamknięte?
- [ ] Czy istnieją pętle lub sprzeczne relacje?
- [ ] Czy sekcje krytyczne mają wskazane źródła i rozwinięcia?

## Lista kontrolna spójności relacji
- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań (np. wzajemne wykluczanie)?
- [ ] Czy relacje cross‑doc mają uzasadnienie i są zgodne z fazą?
- [ ] Czy relacje wymagają rozwinięć lub streszczeń są odnotowane?

## Artefakty powiązane
- [Artefakt 1] — [opis i relacja do dokumentu]
- [Artefakt 2] — [opis i relacja do dokumentu]

## Ścieżka decyzji
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]

## Użytkownicy i interesariusze
- **Solution / Enterprise Architect** — projektuje i zatwierdza architekturę
- **Tech Lead** — odpowiada za spójność techniczną implementacji
- **Product Owner** — definiuje wymagania biznesowe wchodzące na wejście
- **Development Team** — implementuje na podstawie projektu

## Ścieżka akceptacji
- [Kto zatwierdza] → [kryteria akceptacji] → [status]
- [Kto zatwierdza] → [kryteria akceptacji] → [status]

## Kryteria ukończenia
- [ ] Kryterium 1 — [opis]
- [ ] Kryterium 2 — [opis]

## Metryki jakości
- [Metryka 1] — [cel / próg]
- [Metryka 2] — [cel / próg]

## Monitoring i utrzymanie
- [Co monitorujemy] — [narzędzie / częstotliwość]
- [Kto utrzymuje] — [rola]

## Kontrola zmian
- [Zmiana] — [powód] — [data] — [akceptacja]

## Wymogi prawne i regulacyjne
- [Wymóg 1] — [źródło / akt prawny / standard]
- [Wymóg 2] — [źródło / akt prawny / standard]

## Zasady bezpieczeństwa informacji
- [Zasada 1] — [opis i wpływ na dokument]
- [Zasada 2] — [opis i wpływ na dokument]

## Ochrona danych i prywatność
- [Wymaganie 1] — [opis i sekcja docelowa]
- [Wymaganie 2] — [opis i sekcja docelowa]

## Wersjonowanie treści
- [Wersja] — [zmiana] — [autor] — [data]
- [Wersja] — [zmiana] — [autor] — [data]

## Historia zmian sekcji
- [Sekcja] — [zmiana] — [data]
- [Sekcja] — [zmiana] — [data]

## Wymagane aktualizacje
- [Sekcja] — [powód aktualizacji] — [termin]
- [Sekcja] — [powód aktualizacji] — [termin]

## Integracje i interfejsy
- [System / API] — [zakres integracji] — [wymagania]
- [System / API] — [zakres integracji] — [wymagania]

## Wymagania danych
- [Dane wejściowe] — [format] — [walidacja]
- [Dane wyjściowe] — [format] — [walidacja]

## Logowanie i audyt
- [Zdarzenie] — [poziom] — [retencja]
- [Zdarzenie] — [poziom] — [retencja]

## Utrzymanie i operacje
- [Procedura] — [cel] — [częstotliwość]
- [Procedura] — [cel] — [częstotliwość]

## KPI i SLA
- [KPI] — [cel] — [pomiar]
- [SLA] — [cel] — [pomiar]

## Scenariusze awaryjne
- [Scenariusz] — [objawy] — [reakcja]
- [Scenariusz] — [objawy] — [reakcja]

## Wpływ na inne systemy
- [System] — [rodzaj wpływu] — [ryzyko]
- [System] — [rodzaj wpływu] — [ryzyko]

## Zależności danych między systemami
- [Źródło danych] → [Odbiorca] — [opis]
- [Źródło danych] → [Odbiorca] — [opis]

## Harmonogram przeglądów
- [Obszar] — [częstotliwość] — [właściciel]
- [Obszar] — [częstotliwość] — [właściciel]

## Wymagania wydajnościowe
- [Wymaganie] — [metryka] — [próg]
- [Wymaganie] — [metryka] — [próg]

## Wymagania dostępnościowe
- [Wymaganie] — [SLA] — [metoda pomiaru]
- [Wymaganie] — [SLA] — [metoda pomiaru]

## Wymagania skalowalności
- [Wymaganie] — [cel] — [warunki]
- [Wymaganie] — [cel] — [warunki]

## Wymagania dostępności danych
- [Dane] — [częstotliwość dostępu] — [SLA]
- [Dane] — [częstotliwość dostępu] — [SLA]

## Retencja i archiwizacja
- [Dane] — [retencja] — [archiwizacja]
- [Dane] — [retencja] — [archiwizacja]

## Dostępność w sytuacjach awaryjnych
- [Scenariusz] — [zachowanie] — [priorytet]
- [Scenariusz] — [zachowanie] — [priorytet]

## Testy i weryfikacja
- [Test] — [cel] — [wynik oczekiwany]
- [Test] — [cel] — [wynik oczekiwany]

## Walidacja zgodności
- [Wymóg] — [metoda weryfikacji]
- [Wymóg] — [metoda weryfikacji]

## Audyty i przeglądy
- [Audyty] — [częstotliwość] — [odpowiedzialny]
- [Audyty] — [częstotliwość] — [odpowiedzialny]
