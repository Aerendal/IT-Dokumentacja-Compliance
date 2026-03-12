---
title: Citizen Digital Literacy
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Citizen Digital Literacy


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl


## Cel dokumentu

Citizen Digital Literacy — szablon dokumentu IT.

Opisuje cel, zakres i zastosowanie tego dokumentu w kontekście procesu lub systemu IT. Zawiera: definicję problemu lub potrzeby biznesowej adresowanej przez ten dokument, kluczowe decyzje które wspiera, ryzyka które ogranicza i wartość dostarczaną interesariuszom.
Ten szablon jest zgodny ze standardem **ISO/IEC 12207**.



## Zakres i granice

- Obejmuje: kontekst biznesowy, zakres funkcjonalny, główne role/aktorów, punkt wejścia/wyjścia procesu.
- Poza zakresem: elementy niezwiązane z zakresem produktu/usługi; tematy strategiczne lub operacyjne spoza odpowiedzialności zespołu.




## Użytkownicy i interesariusze

- Product/Business, Architecture, OT/IT, Security, Data/Analytics, Operations, Finance.

## Wejścia i wyjścia

- **Wejścia** (co musi być dostępne przed wypełnieniem): Cele biznesowe i wymagania projektu, istniejące dokumenty powiązane, wymagania standardów i regulacji, ograniczenia i założenia środowiskowe.
- **Wyjścia** (co dokument wytwarza jako rezultat): Zatwierdzona wersja dokumentu z kompletnymi sekcjami, lista otwartych pytań i decyzji do podjęcia, action items z właścicielami i terminami.




## Założenia

- Dostępne są dane i systemy źródłowe; sponsor biznesowy; budżet pilota.

## Otwarte pytania

- Jakie regulacje/bezpieczeństwo OT dotyczą środowiska? 
- Jaki horyzont zwrotu (ROI) jest akceptowalny?

## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

- **Wpływa na** (downstream — co zależy od tego dokumentu): Dokumenty powiązane (downstream): plany realizacji, specyfikacje techniczne, raporty i rejestry wynikające z decyzji tego dokumentu.
- **Zależy od** (upstream — co musi istnieć przed tym dokumentem): Dokumenty wejściowe (upstream): wymagania, polityki, standardy, wyniki analiz będące podstawą dla treści tego dokumentu.




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

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


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

- [ ] Czy cel dokumentu jest jednoznaczny?
- [ ] Czy zakres i granice są jasno określone?
- [ ] Czy wszystkie zależności są opisane?
- [ ] Czy wskazano wymagane rozwinięcia i streszczenia?
- [ ] Czy powiązania sekcja↔sekcja są spójne?


## Definicje robocze

- Digital Twin, Edge, OT/IT, ModelOps, SCADA, PLM, CMMS.

## Przykłady użycia

- Pilotaż linii produkcyjnej: monitoring + predykcja awarii, architektura edge+cloud, KPI: downtime -X%.
- Miasto smart: twin infrastruktury, symulacja ruchu, KPI: czas przejazdu -Y%.

## Ryzyka i ograniczenia

- Brak danych jakościowych; bezpieczeństwo OT; brak KPI → trudny zwrot z inwestycji; integracje legacy.

## Decyzje i uzasadnienia
- Progi alertów i retry/backoff.  
- Które integracje mają tryb degradacji/łagodzenia.  
- Kryteria rollback vs hotfix.  
- Zakres komunikacji do klientów/partnerów.
## Powiązania z innymi dokumentami

- IoT Strategy, Data Strategy, Security OT Policy, Edge Architecture, Model Governance, Integration Strategy, PLM Strategy.

## Powiązania z sekcjami innych dokumentów

- Security OT → segmentacja; Data Strategy → governance; Model Governance → lifecycle modeli.

## Słownik pojęć w dokumencie

- Digital Twin, Edge, OT, IT, SCADA, PLM, CMMS, ModelOps.

## Wymagane odwołania do standardów

- Standardy OT security, wytyczne branżowe (np. ISA/IEC 62443), privacy danych IoT.

## Mapa relacji sekcja→sekcja

- Use case/KPI → Dane/architektura → Bezpieczeństwo/governance → Pilot → Roadmapa.

## Mapa relacji dokument→dokument

- Digital Twin Vision → IoT/Data/Security/Model Governance → Pilot → Roadmap.

## Ścieżki informacji

- Use case → Dane/architektura → Pilot → Wyniki → Roadmapa.

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

- Mapy assetów/systemów, diagram architektury, plan pilota, KPI, raport pilota, roadmapa.

## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]


## Ścieżka akceptacji

- Product/Architecture → Security/OT → Data/Analytics → Exec/Owner sign‑off.

## Metryki jakości

- Postęp pilotów vs plan, osiągnięcie KPI, czas do decyzji scale/no‑go, zgodność bezpieczeństwa/governance.

## Kryteria ukończenia

- [ ] Wizja/use case/KPI/architektura/pilot/roadmapa opisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.

## Powiązania sekcja↔sekcja

- "Cel i zakres" **constrains** "Wszystkie pozostałe sekcje dokumentu".
- "Wejścia" **must be available** "Przed wypełnieniem sekcji merytorycznych".
- "Decyzje i uzasadnienia" **feeds** "Downstream documents i rejestry zmian".




## Wymagane rozwinięcia

- Diagramy procesów/architektury wspierające zrozumienie kluczowych przepływów.
- Tabele RACI/odpowiedzialności dla zadań krytycznych.
- Lista decyzji wraz z uzasadnieniem i alternatywami.




## Wymagane streszczenia

- Executive summary: cel, aktualny status, kluczowe decyzje, ryzyka, następne kroki.
- One-pager dla sponsorów: zakres, KPI, plan i data go-live.




## Guidance

Cel: opisz jak dokument wspiera decyzje, jakie KPI mierzy sukces i jakie ryzyka ogranicza.
Zakres: jasno oddziel, co jest w obrębie odpowiedzialności, a co poza nią.
Wejścia: wypisz dane/artefakty, bez których praca nie ma sensu (DoR).
Wyjścia: wskaż mierzalne rezultaty i odbiorców (DoD).
Powiązania: wskaż dokumenty, które rozwijasz/streszczasz lub z którymi jesteś spójny.
Fazy: zaznacz, w których etapach cyklu życia dokument powstaje, jest aktualizowany lub przeglądany.




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
