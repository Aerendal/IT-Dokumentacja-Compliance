---
title: Go-to-Market Vision
status: needs_content
aligned: true
aligned_rev: 2
aligned_at: 2026-02-09
aligned_by: codex
---

# Go-to-Market Vision

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Opisuje wizję wejścia lub rozszerzenia na rynek: dla kogo, jaką wartość, jakimi kanałami i w jakich etapach, z mierzalnymi celami i kryteriami sukcesu. Ustala kierunek, zanim powstaną szczegółowe plany GTM.


## Zakres i granice
- Obejmuje: segmenty/ICP, propozycję wartości, pozycjonowanie, kanały wysokiego poziomu, wstępny pricing/monetyzację (hipotezy), etapy launchu (beta/MVP/GA), kluczowe KPI/KR, ryzyka i zgodność (treści, płatności, dane), wstępny plan komunikacji i enablement.
- Poza zakresem: szczegółowe plany kampanii i playbooki sprzedażowe; są w strategii/planach GTM.



## Wejścia i wyjścia
- Wejścia: wizja/strategia produktu, badania rynku/użytkowników, analizy konkurencji, ograniczenia regulacyjne/treści/płatności, dane CAC/LTV, możliwości partnerstw, budżet ramowy.
- Wyjścia: segmenty/ICP i propozycja wartości, pozycjonowanie, wstępny mix kanałów, hipotezy pricing/packaging, etapy launchu i kryteria sukcesu, KPI/KR (aktywacja/konwersja/retencja/NRR), lista ryzyk i założeń, wstępny plan komunikacji/enablement.



## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.



## Powiązania sekcja↔sekcja
- Segmenty/problem → Propozycja wartości → Kanały/pricing (hipotezy) → Etapy launchu → KPI/KR.



## Fazy cyklu życia
- Discovery: segmenty/ICP, potrzeby, konkurencja, hipotezy wartości i pricingu.
- Vision design: pozycjonowanie, kanały wysokiego poziomu, etapy launchu, KPI.
- Alignment: interesariusze, budżet ramowy, kryteria go/no-go.
- Refresh: rewizje po wynikach beta/MVP.




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
1) Streszczenie i wizja (dla kogo, jaka wartość, dlaczego teraz)
2) Segmenty/ICP i potrzeby (insighty, konkurencja)
3) Propozycja wartości i pozycjonowanie
4) Kanały (wysoki poziom) i wstępne hipotezy pricing/monetyzacji
5) Etapy launchu (beta/MVP/GA) i kryteria sukcesu/go-no-go
6) KPI/KR (aktywacja, konwersja, retencja, NRR, CAC/LTV)
7) Ryzyka, założenia, zgodność (treści/płatności/dane)
8) Wstępny plan komunikacji i enablement (materiały, szkolenia, wsparcie)
9) Governance i rewizje (cadence, fora, wersjonowanie wizji)
10) Decyzje i otwarte pytania



## Wymagane rozwinięcia
- Segmentacja i ICP, propozycja wartości per segment.
- Hipotezy pricing/packaging i plan testów (MVT/A/B).
- Etapy launchu z kryteriami sukcesu i go/no-go.
- Lista ryzyk/regulacji i wstępne mitigacje; plan alignamentu interesariuszy.
- Wstępny plan materiałów enablement (sales/CS/support) i komunikacji.



## Wymagane streszczenia
- Executive summary: segmenty, wartość, kanały, pricing hipotezy, etapy launchu, KPI, ryzyka.
- One-pager: kto/za ile/jak/dokiedy; kryteria go/no-go.



## Guidance (skrót)
- DoR: segmenty/ICP i potrzeby opisane; konkurencja i regulacje znane; hipotezy wartości/pricingu; wstępny budżet i kanały; ownerzy kanałów.
- DoD: wizja opisuje segmenty, wartość, kanały, pricing hipotezy, etapy launchu i KPI; ryzyka/założenia i zgodność; plan komunikacji/enablement; metadane aktualne; dokument w linkage_index.
- Spójność: każdy segment ma wartość, kanał, KPI; etapy launchu mają kryteria; pricing ma hipotezy/testy.



## Szybkie powiązania
- product_strategy_document, go_to_market_strategy, pricing_strategy, marketing_plan, sales_playbook, partner_program, customer_success_plan, analytics_strategy

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
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
- Vision: opis „dlaczego i co”, zanim „jak”.  
- Scope: co robimy i czego nie robimy w tej iteracji.
## Przykłady użycia
- Nowa platforma danych.  
- Replatforming legacy.  
- Wprowadzenie nowej linii produktu.
## Ryzyka i ograniczenia
- Niejasny scope → creep.  
- Cele bez metryk → brak oceny sukcesu.  
- Brak alignment → sprzeczne decyzje.
## Decyzje i uzasadnienia
- Priorytety faz.  
- Architektura docelowa high-level.  
- Kryteria sukcesu.
## Założenia
- Dane i interesariusze dostępni.  
- Budżet/własność zatwierdzone.  
- Strategia firmy stabilna.
## Otwarte pytania
- Jakie są zależności z innymi programami?  
- Jakie ryzyka prawne/regulacyjne?  
- Jakie są limity budżetu/czasu?
## Powiązania z innymi dokumentami
- product_strategy — kierunek biznesu.  
- architecture_vision — kierunek tech.  
- risk_register — ryzyka.
## Powiązania z sekcjami innych dokumentów
- [Dokument X → Sekcja Y] — [powód powiązania]
- [Dokument Z → Sekcja W] — [powód powiązania]

## Słownik pojęć w dokumencie
- [Pojęcie 1] — [definicja i źródło]
- [Pojęcie 2] — [definicja i źródło]
- [Pojęcie 3] — [definicja i źródło]

## Wymagane odwołania do standardów
- Wewnętrzne standardy architektoniczne i procesowe.  
- Polityki prawne/compliance jeśli wpływają.
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
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

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
