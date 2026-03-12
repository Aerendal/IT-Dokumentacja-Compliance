---
title: Stream Quality Monitoring
status: needs_content
aligned: true
aligned_rev: 2
aligned_at: 2026-02-09
aligned_by: codex
---

# Stream Quality Monitoring

## Metadane
- Właściciel: DevOps Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Stream Quality Monitoring definiuje co i jak monitorować, aby wcześnie wykrywać odchylenia i reagować runbookami.


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
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

### Polskie normy i regulacje
- **PN-EN-ISO-9001** — PN-EN ISO 9001:2015-10 — Systemy Zarządzania Jakością
- **PN-EN-ISO-IEC-20000-1** — PN-EN ISO/IEC 20000-1:2019 — Zarządzanie Usługami IT
- **PN-ISO/IEC-27001** — PN-ISO/IEC 27001:2023-09 — Systemy Zarządzania Bezpieczeństwem Informacji

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
- Drift (PSI/KS/JS), Delay etykiet, SLO modelu, Threshold, Rollback.
## Przykłady użycia
- Model scoringu: alert na spadek AUC >5% i PSI cech >0.2; decyzja retrain/rollback.
- Model rekomendacji: monitor CTR, coverage i drift cech; tuning threshold.
## Ryzyka i ograniczenia
- Brak etykiet → brak walidacji; koszt logowania; fałszywe alerty driftu.
## Decyzje i uzasadnienia
- [Decyzja 1 — uzasadnienie]
- [Decyzja 2 — uzasadnienie]

## Założenia
- Dostępny model registry, logging, dane referencyjne; polityki privacy obowiązują.
## Otwarte pytania
- Jaki maks. delay etykiet jest akceptowalny? 
- Jak łączymy alerty jakości z alertami kosztu/latency?
## Powiązania z innymi dokumentami
- Model Card, Model Governance, Observability ML, Data Quality Policy, Retraining Plan, Incident Response ML.
## Powiązania z sekcjami innych dokumentów
- Model Card → metryki; Data Quality → dane referencyjne; IR ML → runbook alertów.
## Słownik pojęć w dokumencie
- Drift, PSI, KS, JS, SLO modelu, Threshold, Rollback.
## Wymagane odwołania do standardów
- Polityki privacy/PII, standardy monitoringu ML, wewn. SLO/SLA.
## Mapa relacji sekcja→sekcja
- Metryki/SLO → Alerty → Działania → Raporty → Korekta progów.
## Mapa relacji dokument→dokument
- Prediction Monitoring → Model Governance/Observability/Retraining → Incident Response ML.
## Ścieżki informacji
- Logi/metryki → Alert → Działanie → Raport → Update progów/planów.
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
- Dashboardy, alert config, logi/metryki, model registry wpisy, runbooki, raporty.
## Ścieżka decyzji
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]

## Użytkownicy i interesariusze
- Data/ML/Ops, Product, Security/Privacy, Compliance, Business Owners.
## Ścieżka akceptacji
- Data/ML → Ops/SRE → Privacy/Compliance → Product/Owner sign‑off.
## Kryteria ukończenia
- [ ] Monitoring metryk/drift/bias działa; runbooki i audyt opisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.
## Metryki jakości
- MTTA/MTTR dla degradacji, odsetek alertów uzasadnionych, czas do retrain/rollback, koszt logowania/sampling, zgodność privacy.
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