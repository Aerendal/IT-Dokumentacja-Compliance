---
title: Service Usage Monitoring
status: needs_content
aligned: true
aligned_rev: 3
aligned_at: 2026-02-09
aligned_by: codex
---

# Service Usage Monitoring

## Metadane
- Właściciel: DevOps Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Service Usage Monitoring definiuje co i jak monitorować, aby wcześnie wykrywać odchylenia i reagować runbookami.


## Zakres i granice
- Obejmuje: KPI/SLO, metryki/logi/traces, źródła i agregację, alerty/reguły, dashboardy, runbooki i testy syntetyczne.
- Poza zakresem: implementacja funkcjonalna usług.



## Wejścia i wyjścia
- Wejścia: SLO/SLI, architektura usług, krytyczne ścieżki, limity budżetu zdarzeń, progi biznesowe.
- Wyjścia: katalog metryk/logów/traces, konfiguracja alertów, dashboardy, runbooki/eskalacje, plan przeglądów.



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
- Krytyczne ścieżki → Metryki/SLI → Alerty → Runbooki/eskalacje.



## Fazy cyklu życia
- Definicja SLO/SLI i krytycznych ścieżek.
- Projekt metryk/logów/traces i alertów.
- Ustawienie dashboardów i testów syntetycznych.
- Przeglądy i tuning progów.




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
- Cel monitoringu i zakres (usługi/ścieżki)
- SLO/SLI i priorytety alertowania
- Metryki/logi/traces i źródła danych
- Alerty/reguły, progi i runbooki
- Dashboardy i testy syntetyczne
- Operacje: on-call, eskalacje, przeglądy
- Utrzymanie, budżety zdarzeń i ciągłe doskonalenie



## Wymagane rozwinięcia
- Diagramy procesów/architektury wspierające zrozumienie kluczowych przepływów.
- Tabele RACI/odpowiedzialności dla zadań krytycznych.
- Lista decyzji wraz z uzasadnieniem i alternatywami.



## Wymagane streszczenia
- Executive summary: cel, aktualny status, kluczowe decyzje, ryzyka, następne kroki.
- One-pager dla sponsorów: zakres, KPI, plan i data go-live.



## Guidance
DoR: SLO/SLI zdefiniowane, krytyczne ścieżki znane, narzędzia/źródła dostępne.
DoD: metryki/logi/traces opisane, alerty i runbooki gotowe, dashboardy dostępne, przeglądy zaplanowane, metadane aktualne.



## Szybkie powiązania
- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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
- SLI: mierzalny wskaźnik jakości usługi (np. availability 99.9%, latency p95).  
- SLO: cel dla SLI w okresie (np. 99.9% / 28 dni).  
- Error budget: 1 − SLO; budżet na zmiany/awarie.
## Przykłady użycia
- Zmiana architektury logowania — ocena kosztów i tagów.  
- Nowa usługa Tier1 — nadanie SLI/SLO i alertów.  
- Post‑mortem fałszywych alarmów — tuning progów i reguł.
## Ryzyka i ograniczenia
- Alert fatigue z nadmiarem reguł lub złymi progami.  
- Brak standardu tagów uniemożliwia pivotowanie danych.  
- Niekontrolowane koszty retencji/indeksów.
## Decyzje i uzasadnienia
- Zakres SLO (global vs per region) — zależnie od architektury.  
- Retencja logów/traces — kompromis koszt vs potrzeba audytu/IR.  
- Sampling/aggregation — kompromis dokładność vs koszt.
## Założenia
- Stabilne źródła metryk/logów/traces i kontrola PII.  
- On‑call rota dostępna i aktualna.  
- Narzędzia wspierają etykiety/tagi i multi‑region.
## Otwarte pytania
- Czy wszystkie SLO muszą być customer‑facing czy tylko wewnętrzne?  
- Jakie synthetic tests są wymagane per krytyczna ścieżka?  
- Jakie limity kosztów są akceptowalne per usługa?
## Powiązania z innymi dokumentami
- incident_response_runbook — reakcja na alerty.  
- logging_standards — formaty i PII.  
- cost_management_observability — budżet i optymalizacje.
## Powiązania z sekcjami innych dokumentów
- SLO Policy → progi; IR → eskalacje; Privacy → logi/trace redakcja.
## Słownik pojęć w dokumencie
- Golden signals, Burn-rate, Error budget, Sampling, Retention, RUM, APM.
## Wymagane odwołania do standardów
- ISO 27001 / SOC2 (logowanie, audyt).  
- Wewnętrzne standardy PII/RODO i retencji.
## Mapa relacji sekcja→sekcja
- Ścieżki/SLO → Sygnały → Progi/alerty → Runbooki → Raporty → Tuning.
## Mapa relacji dokument→dokument
- Monitoring Strategy → Observability/SLO → Incident/Performance → Cost/Privacy.
## Ścieżki informacji
- SLO → Metryki → Alerty → Incydent → Raport → Korekta progów.
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
- Dashboardy, alert config, runbooki, testy alertów, raporty, koszt/retencja ustawienia.
## Ścieżka decyzji
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]

## Użytkownicy i interesariusze
- SRE/Observability, Engineering, Product, Security/Privacy, FinOps.
## Ścieżka akceptacji
- SRE/Observability → Engineering/Product → Privacy/FinOps → Owner sign‑off.
## Kryteria ukończenia
- [ ] Strategia opisana; alerty/dashboards/runbooki/testy zdefiniowane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.
## Metryki jakości
- MTTR, liczba fałszywych alertów, pokrycie ścieżek krytycznych, koszt observability, zgodność z SLO, częstotliwość testów alertów.
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