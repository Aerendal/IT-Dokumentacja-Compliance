---
title: Storage Utilization Report
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Storage Utilization Report


## Metadane

- Właściciel: Document Owner
- Wersja: v0.3
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Raport wykorzystania storage (blok/plik/obiekt) z trendami, kosztami, ryzykami i rekomendacjami optymalizacji. Ma pozwolić kontrolować pojemność, koszty i zgodność (retencja, bezpieczeństwo), oraz zapewnić plan działań z właścicielami.


## Zakres i granice

- Obejmuje: metryki wykorzystania (GB/TB, wzrost, tiering), koszty (per tier/region/projekt), hot/warm/cold dane, duplikaty i dane nieużywane, retencję/archiwizację, bezpieczeństwo (szyfrowanie, dostęp/public exposure), alerty progów, rekomendacje (cleanup, tiering, lifecycle), wyjątki biznesowe.
- Poza zakresem: projekt architektury storage (osobny dokument), pełne polityki backup/DR (link).


## Użytkownicy i interesariusze

- SRE/Infra, FinOps, Security/Compliance, Product/Teams właściciele danych, Leadership.


## Wejścia i wyjścia

- Wejścia: metryki z systemów storage/obiektów, billing/FinOps, tagowanie (owner, cost center, data class), polityki retencji/bezpieczeństwa, listy właścicieli danych, prognozy wzrostu, wyjątki biznesowe.
- Wyjścia: raport (MD/PDF/BI), KPI i alerty, lista rekomendacji z priorytetem/KPI, plan działań (owner, ETA), wyjątki z uzasadnieniem i datą przeglądu.


## Założenia

- Dostępne metryki i billing; tagowanie działa; polityki retencji/bezpieczeństwa obowiązują.


## Otwarte pytania

- Jaka częstotliwość raportu i kto jest ownerem?  
- Czy wymagane są raporty per klient/tenant?


## Powiązania (meta)

- Key Documents: finops_policy, data_lifecycle_policy, backup_and_retention, security_baseline_storage, tagging_standards, capacity_planning.
- Key Document Structures: metryki, koszty, ryzyka, rekomendacje, plan działań.
- Document Dependencies: monitoring/storage metrics, billing data, tagging/owners, security/retention policies.


## Zależności dokumentu

Wymaga metryk storage i billing, tagowania danych/właścicieli, polityk retencji/bezpieczeństwa oraz progów/alertów. Bez tego DoR pozostaje otwarte.


## Fazy cyklu życia

- Zbieranie danych: metryki, koszty, tagi, właściciele.
- Analiza: trendy, hot/warm/cold, duplikaty, ryzyka.
- Rekomendacje: cleanup, tiering, lifecycle, wyjątki.
- Raport i plan działań: właściciele, ETA, alerty.
- Follow‑up: realizacja, ponowny pomiar, aktualizacja.



## Struktura sekcji (szkielet)
- Zakres okresu i stref.
- KPI: occupancy/utilization, przychód per m2/godz., no-show/cancel, throughput wejść.
- Analiza przychodów i kosztów (media, personel, sprzątanie).
- Anomalie i insighty (szczyty/dole, overbooking, puste okna).
- Rekomendacje (zmiana cenników, grafiku, layoutu, staffing).
- Action items (owner, termin, status).
## Szybkie powiązania

- linkage_index.jsonl (storage/utilization)
- finops_policy, data_lifecycle_policy, backup_and_retention, security_baseline_storage, tagging_standards, capacity_planning


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

1. Zbierz metryki i koszty; wypełnij KPI/trendy.  
2. Dodaj ryzyka i rekomendacje z owner/ETA; zapisz wyjątki z przeglądem.  
3. Publikuj raport, śledź wykonanie i aktualizuj cyklicznie.


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

- Hot/Warm/Cold, Tiering, Lifecycle, Cost/GB, Capacity %, Public exposure.


## Przykłady użycia

- Raport m-c: growth 8%, hot 40% → rekomendacja tiering + cleanup orphaned buckets.  
- Anomalia kosztów: spike w regionie X → analiza tagów → restrykcja public access.


## Ryzyka i ograniczenia

- Brak tagów/właścicieli → brak odpowiedzialności; brak retencji → ryzyko compliance; brak alertów → overflow/koszty.


## Decyzje i uzasadnienia

- [Decyzja] Progi capacity/kosztów; [Decyzja] Priorytet rekomendacji (koszt/ryzyko).


## Powiązania z innymi dokumentami

- FinOps Policy, Data Lifecycle, Backup & Retention, Security Baseline (storage), Tagging Standards, Capacity Planning.


## Powiązania z sekcjami innych dokumentów

- Tagging → właściciele; Lifecycle → retencja/tiering; Security → public access/szyfrowanie.


## Słownik pojęć w dokumencie

- Hot/Warm/Cold, Tiering, Lifecycle, Cost/GB, Capacity %, Public exposure.


## Wymagane odwołania do standardów

- Polityki retencji/bezpieczeństwa/FinOps, wymogi regulatorów dot. danych (jeśli dotyczy).


## Mapa relacji sekcja→sekcja

- Metryki/KPI → Ryzyka → Rekomendacje → Plan działań → Follow‑up.


## Mapa relacji dokument→dokument

- Storage Report → FinOps/Lifecycle/Security → Capacity/DR → Audit/Compliance.


## Ścieżki informacji

- Metryki/billing → Analiza → Rekomendacje → Plan → Follow‑up → Kolejny raport.


## Weryfikacja spójności

- [ ] KPI/trendy/koszty kompletne; rekomendacje powiązane z ryzykami i ownerami.  
- [ ] Wyjątki mają datę przeglądu; relacje cross‑doc opisane.


## Lista kontrolna spójności relacji

- [ ] Każde ryzyko ma rekomendację/owner; każda rekomendacja ma KPI/ETA.  
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Dashboardy storage/billing, surowe dane, listy tagów/owners, plan działań, raport PDF/BI.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- SRE/Infra → FinOps → Security/Compliance → Leadership/Owner sign‑off.


## Metryki jakości

- Dokładność danych vs billing, tempo realizacji rekomendacji, zmiana kosztów/pojemności, liczba otwartych wyjątków, public exposure findings.

## Kryteria ukończenia

- [ ] Raport opublikowany; rekomendacje/owner/ETA zapisane; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Metryki → Koszty → Rekomendacje → Plan działań.
- Retencja/bezpieczeństwo → Rekomendacje → Wyjątki.


## Struktura sekcji

1) Podsumowanie i główne KPI (użycie, wzrost, koszt, alerty progowe)  
2) Metryki wykorzystania (tier/region/service), trendy, forecast  
3) Koszty i FinOps (per tier/region/project), anomalie  
4) Retencja/lifecycle i zgodność (polityki, wyjątki)  
5) Bezpieczeństwo (szyfrowanie, uprawnienia, public exposure)  
6) Ryzyka (pojemność, koszt, compliance)  
7) Rekomendacje i plan działań (owner, ETA, KPI)  
8) Załączniki: dane źródłowe, definicje metryk, tagi/owners


## Wymagane rozwinięcia

- Progi alertów (capacity %, growth %, cost/GB) i definicje KPI.
- Lista rekomendacji z priorytetem i uzasadnieniem biznes/ryzyko/koszt.
- Mapowanie właścicieli/tagów do zasobów; wyjątki z datą przeglądu i ownerem.


## Wymagane streszczenia

- Top KPI i ryzyka, kluczowe rekomendacje, szacowany wpływ (koszt/pojemność), wyjątki.


## Guidance (skrót)

- Utrzymuj tagowanie właścicieli; brak ownera → cleanup lub eskalacja.
- Mierz growth i forecast; ustaw alerty na progi capacity/kosztów.
- Stosuj tiering/lifecycle i cleanup duplikatów/stale; dokumentuj wyjątki.
- Sprawdzaj bezpieczeństwo: public buckets, szyfrowanie, nadmierne uprawnienia.
- Raportuj cyklicznie (np. m-c) i śledź wykonanie rekomendacji.


## Checklisty Definition of Ready (DoR)

- [ ] Metryki storage/billing i tagi właścicieli dostępne.
- [ ] Progi capacity/kosztów oraz polityki retencji/bezpieczeństwa znane.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] KPI/trendy/koszty opisane; ryzyka i rekomendacje z owner/ETA.
- [ ] Wyjątki udokumentowane z datą przeglądu; plan działań zapisany.
- [ ] Dokument w linkage_index/checklistach; wersja/data/właściciel aktualne.

