---
title: Cost Tracking Integration
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Cost Tracking Integration


## Metadane

- Właściciel: Backend Developer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje integrację śledzenia kosztów w systemach/aplikacjach: źródła danych, tagowanie, modele alokacji, raporty i alerty. Celem jest transparentność kosztów, chargeback/showback i wczesne wykrywanie anomalii.


## Zakres i granice

- Obejmuje: źródła kosztów (chmura, CDN, SaaS, licencje), standard tagów/labeli, przypisywanie kosztów (projekty/usługi/zespoły/klienci), metryki (unit cost, COGS), modele alokacji (direct/pośrednie), integracje z billing API/CSV, pipeline danych (ETL/warehouse), raporty/dashboards, alerty anomalii, zgodność (PII/contract), FinOps procesy (budżety, rezerwy).  
- Poza zakresem: negocjacje kontraktów (sourcing) i pełny budżet korporacyjny.


## Użytkownicy i interesariusze
- **Backend Developer / API Owner** — projektuje i implementuje interfejs API
- **Frontend Developer / Consumer** — integruje się z API i zgłasza wymagania
- **Integration Architect** — definiuje standardy integracji i kontrakt API
- **QA Engineer** — weryfikuje kontrakty i scenariusze błędów

## Wejścia i wyjścia

- Wejścia: faktury/billing exports, API dostawców, tagi/labelki, CMDB/usługi, dane użycia (usage), kursy walut, polityki FinOps, budżety, SLA.  
- Wyjścia: ujednolicone dane kosztowe, raporty (showback/chargeback), alerty anomalii, dashboardy unit economics, feed do BI/ERP, checklisty DoR/DoD.


## Założenia

- Dostępne API/eksporty billing i DWH/BI.  
- CMDB usługi aktualne.  
- FinOps proces istnieje (budżety, rezerwy).


## Otwarte pytania

- Jaka częstotliwość odświeżania kosztów jest potrzebna (daily/near‑real‑time)?  
- Jak obsłużyć shared resources bez tagów?  
- Jakie są wymagania księgowe/raportowe (audyt)?


## Powiązania (meta)

- Key Documents: finops_policy, tagging_standard, cost_allocation_model, budget_governance, anomaly_detection_playbook, cmdb_service_catalog.  
- Key Document Structures: źródła kosztów, tagowanie, alokacja, pipeline, raporty, alerty.  
- Document Dependencies: billing APIs/exports, data warehouse, CMDB/usługi, IAM, monitoring/alerts.


## Zależności dokumentu

Wymaga: standardu tagów/labeli, dostępu do billing API/exports, katalogu usług (CMDB), kursów walut, polityk FinOps/budżetów, narzędzi ETL/BI. Braki = DoR otwarte.


## Fazy cyklu życia

- Analiza źródeł i standard tagów.  
- Budowa pipeline i alokacji.  
- Publikacja raportów/alertów.  
- Optymalizacja i przeglądy FinOps.



## Struktura sekcji (szkielet)
- Zakres raportu i okres
- Definicje metryk/KPI i źródła danych
- Wyniki z trendami i wizualizacjami
- Insighty i obserwacje
- Ryzyka/odchylenia i ich wpływ
- Rekomendacje i plan działań z właścicielami
- Załączniki/metodologia
## Szybkie powiązania

- linkage_index.jsonl (cost/tracking/integration)  
- finops_policy, tagging_standard, cost_allocation_model, anomaly_detection_playbook, cmdb_service_catalog


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **DORA** — Ustawa o Cyfrowej Odporności Operacyjnej (UE)

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

1. Ustal tagi/labelki i źródła; skonfiguruj pipeline.  
2. Zaimplementuj alokację i raporty; ustaw alerty anomalii.  
3. Prowadź cykliczne przeglądy FinOps; aktualizuj DoR/DoD i linkage_index.


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

- Chargeback/Showback: obciążanie kosztami lub ich informacyjne przypisanie.  
- Unit cost: koszt na jednostkę (request, GB, user).  
- Tag compliance: % zasobów z wymaganymi tagami.


## Przykłady użycia

- Integracja kosztów chmury i CDN do raportów produktu.  
- Alert na skok kosztu Kinesis/Kafka; RCA i action.  
- Raport unit cost per klient dla rozliczeń.


## Ryzyka i ograniczenia

- Brak tagów → brak alokacji.  
- Opóźnione dane billing → alerty fałszywe/brak sygnału.  
- PII/kontrakty w danych billing wymagają kontroli dostępu.


## Decyzje i uzasadnienia

- Model alokacji (CPU/GB/seat) i progi anomalii.  
- Źródła prawdy dla kursów walut.  
- Retencja danych billing i dostępność w BI.


## Powiązania z innymi dokumentami

- finops_policy — polityki.  
- tagging_standard — tagi/labelki.  
- cost_allocation_model — wzory alokacji.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Wewnętrzne standardy FinOps/tagging; polityki dostępu/PII.  
- Umowy z dostawcami (SLA, billing, retencja).

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

- Tagowanie → Alokacja → Raporty → Budżety/alerty.  
- Źródła kosztów → Pipeline ETL → Dashboardy/BI.  
- Anomalie → Playbook → Decyzje budżetowe.


## Struktura sekcji

1) Zakres i cele (chargeback/showback, unit cost)  
2) Źródła kosztów i dane użycia (cloud/CDN/SaaS/licencje)  
3) Tagowanie/labeling i jakość danych (coverage, conformance)  
4) Modele alokacji (direct/pośrednie, wzorce, wyjątki)  
5) Pipeline i architektura danych (ETL/warehouse, walidacja)  
6) Raporty i dashboardy (unit economics, COGS, budżet vs real)  
7) Alerty/anomalie i playbook reakcji  
8) Zgodność i bezpieczeństwo (PII/kontrakty, dostęp do billing)  
9) Operacje i przeglądy FinOps (cadence, role, RACI)  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Standard tagów/labeli i wymagane pola; coverage KPI.  
- Model alokacji (tabele, formuły) i przykłady.  
- Architektura pipeline (źródła → transformacje → DWH → BI) z walidacją.  
- Playbook anomalii (progi, eskalacje, działania).


## Wymagane streszczenia

- Executive snapshot: koszt per usługa/klient, unit cost, anomalie.  
- Krótki raport tag compliance i coverage.


## Guidance (skrót)

- Taguj u źródła; enforce w CI/IaC.  
- Waliduj dane billing vs usage; koreluj z CMDB.  
- Automatyzuj alerty anomalii, ale dodaj ręczną weryfikację.  
- Raportuj unit cost i kontekst (użycie, SLA) — nie tylko suma.  
- Regularne przeglądy FinOps z właścicielami usług.


## Checklisty Definition of Ready (DoR)

- [ ] Standard tagów/labeli i katalog usług gotowe.  
- [ ] Dostępy do billing API/exports zapewnione.  
- [ ] Model alokacji wstępny uzgodniony.  
- [ ] Narzędzia ETL/BI dostępne; polityki FinOps znane.  
- [ ] Polityki dostępu i PII dla danych billing ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Pipeline kosztów działa; dane zweryfikowane z billing.  
- [ ] Raporty/dashboardy i alerty anomalii opublikowane; status/wersja/data uzupełnione.  
- [ ] Alokacja wdrożona (chargeback/showback); wyjątki udokumentowane.  
- [ ] Tag compliance/coverage raportowane; linkage_index zaktualizowany.  
- [ ] Ryzyka i decyzje FinOps zapisane; backlog optymalizacji utworzony.

