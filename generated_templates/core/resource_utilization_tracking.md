---
title: Resource Utilization Tracking
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Resource Utilization Tracking


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Śledzenie wykorzystania zasobów.



## Zakres i granice
- Obejmuje: zakres okresu/obiektu raportowania, metryki/KPI, źródła danych, obserwacje, ryzyka, rekomendacje, akcje follow-up.
- Poza zakresem: zmiana procesu/systemu poza rekomendacjami; implementacja poprawek.
## Użytkownicy i interesariusze
- SRE/Infra, FinOps, Security/Compliance, Product/Teams właściciele danych, Leadership.
## Wejścia i wyjścia
- Wejścia: definicje metryk, źródła danych, okres raportowania, limity/targety, wcześniejsze raporty.
- Wyjścia: sekcja wyników z wizualizacjami, wnioski, rekomendacje i przypisane zadania.
## Założenia
- Telemetry i billing dostępne.  
- Zespoły ops/finops współpracują.  
- CMDB aktualna.
## Otwarte pytania
- Jakie SLO na resource utilization?  
- Czy potrzebne alerty per tenant/region?  
- Jak włączyć automatyczne rightsizing?
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
## Fazy cyklu życia
- Zbieranie danych i walidacja.
- Analiza i interpretacja.
- Rekomendacje i plan działań.
- Follow-up i przegląd wyników.
## Struktura sekcji (szkielet)

1. Zakres: zespoły/systemy.
2. Metryki: utilization %, obciążenie, nadgodziny.
3. Źródła danych: timesheet, telemetry.
4. Alerty i progi: over/under-utilization.
5. Raportowanie: dashboard, częstotliwość.
6. Działania korygujące.


## Szybkie powiązania

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

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

- [ ] Metryki i źródła danych zdefiniowane.
- [ ] Progi/alerty ustawione.
- [ ] Raporty działają cyklicznie.
- [ ] Plan korekt istnieje.

## Definicje robocze
- Saturation: poziom zbliżenia do limitu zasobu.  
- Rightsizing: dostosowanie zasobów do potrzeb.  
- Noise reduction: techniki ograniczające fałszywe/nadmierne alerty.
## Przykłady użycia
- Monitoring CPU/RAM/IO dla mikrousług; alerty SLO.  
- Raport FinOps: koszt vs wykorzystanie, rekomendacje rightsizing.  
- Tuning progów po incydencie wydajności.
## Ryzyka i ograniczenia
- Alert fatigue przy złych progach.  
- Brak retencji → zły forecast capacity.  
- Brak tagów kosztów → brak odpowiedzialności za koszty.
## Decyzje i uzasadnienia
- Zakres SLO vs koszt monitoringu.  
- Retencja danych a koszt storage.  
- Polityka alertów (saturation/SLO vs raw).
## Powiązania z innymi dokumentami
- performance_test_plan — dane do progów.  
- incident_response_runbook — reakcja na alerty.  
- scaling_policies — progi autoscaling.
## Powiązania z sekcjami innych dokumentów
- Tagging → właściciele; Lifecycle → retencja/tiering; Security → public access/szyfrowanie.
## Słownik pojęć w dokumencie
- Hot/Warm/Cold, Tiering, Lifecycle, Cost/GB, Capacity %, Public exposure.
## Wymagane odwołania do standardów
- Wewnętrzne standardy observability/FinOps.  
- Ewentualne wymogi regulatorów dot. capacity/availability.
## Mapa relacji sekcja→sekcja
- Metryki/KPI → Ryzyka → Rekomendacje → Plan działań → Follow‑up.
## Mapa relacji dokument→dokument
- Storage Report → FinOps/Lifecycle/Security → Capacity/DR → Audit/Compliance.
## Ścieżki informacji
- Metryki/billing → Analiza → Rekomendacje → Plan → Follow‑up → Kolejny raport.
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
- Dashboardy storage/billing, surowe dane, listy tagów/owners, plan działań, raport PDF/BI.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- SRE/Infra → FinOps → Security/Compliance → Leadership/Owner sign‑off.
## Metryki jakości
- Dokładność danych vs billing, tempo realizacji rekomendacji, zmiana kosztów/pojemności, liczba otwartych wyjątków, public exposure findings.
## Kryteria ukończenia
- [ ] Raport opublikowany; rekomendacje/owner/ETA zapisane; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.
