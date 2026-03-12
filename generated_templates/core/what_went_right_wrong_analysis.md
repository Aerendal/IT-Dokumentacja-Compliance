---
title: What Went Right/Wrong Analysis
status: needs_content
aligned: true
aligned_rev: 3
aligned_at: 2026-02-09
aligned_by: codex
---

# What Went Right/Wrong Analysis

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
What Went Right/Wrong Analysis — szablon dokumentu IT.

Zawiera wyniki systematycznej analizy — metodologię, dane źródłowe, znaleziska, wnioski i rekomendacje. Każdy wniosek powinien być poparty danymi i zawierać propozycję działań z priorytetami.
Ten szablon jest zgodny ze standardem **ISO/IEC 12207**.


## Zakres i granice
- Obejmuje: kontekst biznesowy, zakres funkcjonalny, główne role/aktorów, punkt wejścia/wyjścia procesu.
- Poza zakresem: elementy niezwiązane z zakresem produktu/usługi; tematy strategiczne lub operacyjne spoza odpowiedzialności zespołu.



## Wejścia i wyjścia
- **Wejścia** (co musi być dostępne przed wypełnieniem): Zakres analizy i pytania badawcze, dane źródłowe (metryki, logi, wywiady, obserwacje), kryteria oceny, benchmarki branżowe.
- **Wyjścia** (co dokument wytwarza jako rezultat): Raport z analizy z uzasadnionymi wnioskami, macierz priorytetów rekomendacji, plan działań, wizualizacje danych.



## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
- **Wpływa na** (downstream — co zależy od tego dokumentu): Plany naprawcze i improvement initiatives, aktualizacje polityk i procesów, raporty zarządcze, decyzje inwestycyjne.
- **Zależy od** (upstream — co musi istnieć przed tym dokumentem): Dane operacyjne i metryki, poprzednie analizy, wymagania regulacyjne, cel strategiczny analizy.



## Powiązania sekcja↔sekcja
- "Dane źródłowe" **determines** "Jakość i pewność wniosków".
- "Rekomendacje" **drives** "Plan działań z priorytetami".
- "Wnioski analizy" **feeds** "Decyzje strategiczne i aktualizacje rejestrów".



## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.




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
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła



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



## Szybkie powiązania
- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies

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
- Sanity check: proste testy wykrywające oczywiste błędy danych/wyników.  
- Backtest: testowanie modelu na danych historycznych z symulacją.  
- Conditional go: akceptacja z warunkami/mitigacjami.
## Przykłady użycia
- Walidacja analizy wpływu ceny na konwersję.  
- Backtest modelu scoringowego.  
- Re-run analizy po aktualizacji danych źródłowych.
## Ryzyka i ograniczenia
- Brak dowodów → wnioski słabe; brak follow‑up → powtórki; brak ownerów → CAPA niezamknięte; blame → kultura defensywna.
## Decyzje i uzasadnienia
- Progi istotności/efektu.  
- Zakres testów DQ/sanity vs czas.  
- Kiedy wymagany niezależny reviewer.
## Założenia
- Dostępne są dane (logi/metryki), zespoły są dostępne do analizy, kultura blameless obowiązuje.
## Otwarte pytania
- Czy wymagane są powiadomienia regulatora/klientów?  
- Czy potrzebna jest dodatkowa analiza bezpieczeństwa (jeśli dotyczy)?
## Powiązania z innymi dokumentami
- Incident Response Playbook, Incident Notifications, DRP/BCP, Monitoring Strategy, Change Management Plan, Risk Register, SLO.
## Powiązania z sekcjami innych dokumentów
- Monitoring → alerty/timeline; DR/BCP → reakcja; Change → przyczyny; Risk Register → wpisy; Lessons Learned → baza wiedzy.
## Słownik pojęć w dokumencie
- MTTR, SLA/SLO, Root Cause, Contributing Factors, CAPA, Waiver, Sunset, Blameless.
## Wymagane odwołania do standardów
- Polityki IR/BCP/DR; ewentualne wymogi regulatora jeśli incydent dotyczył danych/usług krytycznych.
## Mapa relacji sekcja→sekcja
- Timeline → Wpływ → Root cause → CAPA → Usprawnienia → Follow‑up.
## Mapa relacji dokument→dokument
- Postmortem → Incident Response/DR/BCP/Monitoring/Change/Risk → Lessons Learned.
## Ścieżki informacji
- Alert/logi → Timeline → Analiza → CAPA → Retest → Aktualizacja dokumentacji.
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
- Logi/metryki/trace, change log, komunikacja (status/update), runbooki, ticket CAPA, wykresy, lesson learned register.
## Ścieżka decyzji
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]

## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Ścieżka akceptacji
- [Kto zatwierdza] → [kryteria akceptacji] → [status]
- [Kto zatwierdza] → [kryteria akceptacji] → [status]

## Kryteria ukończenia
- [ ] Raport ukończony, CAPA/waivery z planem i dowodami; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.
## Metryki jakości
- Czas dostarczenia postmortem, % CAPA zamkniętych w terminie, recydywa podobnych incydentów, jakość danych (logi/metryki) w raporcie, liczba waiverów i czas ich zamknięcia.
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