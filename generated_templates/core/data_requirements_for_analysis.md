---
title: Data Requirements for Analysis
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Data Requirements for Analysis


## Metadane

- Właściciel: Product Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje wymagania dotyczące danych potrzebnych do konkretnej analizy/analityki (badawczej lub produkcyjnej): źródła, dostępność, jakość, zakres, bezpieczeństwo/PII oraz kryteria akceptacji. Ma ograniczyć ryzyko błędów, biasów i opóźnień.


## Zakres i granice

- Obejmuje: opis celu analizy, pytania badawcze/KPI, zakres danych (zakres czasowy, populacja, segmenty), źródła i schemy, wymagania jakości (świeżość, kompletność, dokładność), dostęp/PII, metadane, ograniczenia i założenia, oczekiwane artefakty (datasety, raporty, modele), plan walidacji.
- Poza zakresem: implementacja pipeline’ów ETL/ELT (osobny dokument), szczegóły modeli (jeśli oddzielny model card), dashboardy produkcyjne (osobne specyfikacje).


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: cel biznesowy, pytania/analityka, definicje KPI, istniejące źródła danych i schemy, katalog danych, polityki PII/RODO, wymagania compliance, budżet czasowy i SLA, ograniczenia narzędzi.
- Wyjścia: specyfikacja danych (źródła, pola, filtracje, okna czasu, segmenty), definicje i transformacje, kryteria jakości/świeżości, lista braków i ryzyk, plan pozyskania danych, zgody/akceptacje (privacy/legal), checklisty DoR/DoD, odniesienia do kontraktów danych.


## Założenia

- Dostępne narzędzia DQ i katalog danych.  
- Dostęp do systemów źródłowych/wyciągów.  
- Wspólne definicje KPI/metryk obowiązują.


## Otwarte pytania

- Czy potrzebne są dodatkowe źródła zewnętrzne?  
- Czy istnieją ograniczenia prawne (jurysdykcje) dla wybranych danych?  
- Jakie są limity kosztów pozyskania/przetwarzania?


## Powiązania (meta)

- Key Documents: data_contract_standard, data_catalog_entry, privacy_and_pii_handling, data_quality_playbook, metric_definitions, access_request_procedure.
- Key Document Structures: cel/KPI, źródła, pola, filtracje, jakość, bezpieczeństwo/PII, walidacja, artefakty.
- Document Dependencies: katalog danych, IAM/PII, DQ narzędzia, lineage, narzędzia analityczne/notebooki/BI.


## Zależności dokumentu

Wymaga: zatwierdzonego celu/KPI, dostępu do katalogu danych, polityk PII, wstępnych schem, dostępów do źródeł, listy ograniczeń prawnych/regulacyjnych. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja wymagań (pre‑analysis).  
- Pozyskanie/udostępnienie danych i walidacja.  
- Wykonanie analizy / modelowania.  
- Przegląd i zamknięcie (lessons, aktualizacja katalogu/kontraktów).



## Struktura sekcji (szkielet)
- Cel i kontekst biznesowy
- Interesariusze, persony i scenariusze
- Wymagania funkcjonalne (priorytety, reguły, wyjątki)
- Wymagania niefunkcjonalne (wydajność, dostępność, bezpieczeństwo, zgodność)
- Dane i integracje
- Kryteria akceptacji i miary sukcesu
- Zależności, ryzyka i założenia
- Śledzenie (traceability) do epik/testów
## Szybkie powiązania

- linkage_index.jsonl (data/requirements/analysis)  
- data_contract_standard, data_catalog_entry, data_quality_playbook, privacy_and_pii_handling, metric_definitions


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.

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

1. Opisz cel/KPI i zakres danych; zidentyfikuj źródła/pola.  
2. Ustal kryteria jakości i PII; wykonaj walidacje/zgody.  
3. Zanotuj braki/ryzyka i plan ich domknięcia; zaktualizuj DoR/DoD i katalog danych.


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

- Świeżość: maks. opóźnienie dostarczenia danych vs SLA.  
- Kompletność: odsetek brakujących wierszy/pól.  
- Dokładność: zgodność z systemem źródłowym lub ground truth.


## Przykłady użycia

- Specyfikacja danych do analizy churn.  
- Wymagania danych do budowy modelu rekomendacji.  
- Dane do audytu kosztów i marży per segment.


## Ryzyka i ograniczenia

- Bias w danych (niedoreprezentowane segmenty).  
- Braki PII/zgód mogą zablokować użycie danych.  
- Niska jakość danych wydłuża czas analizy lub fałszuje wyniki.


## Decyzje i uzasadnienia

- Zakres czasowy/segmenty vs koszt i czas pozyskania.  
- Poziom agregacji vs granularność wymagana przez KPI.  
- Tolerancje DQ vs harmonogram analizy.


## Powiązania z innymi dokumentami

- data_contract_standard — wymagania kontraktowe.  
- privacy_and_pii_handling — reguły PII.  
- data_quality_playbook — testy i progi DQ.


## Powiązania z sekcjami innych dokumentów
- Access Control/SoD → polityki dostępu; Retention → polityki retencji; DQ → metryki; TPRM → dostawcy danych; Security/Privacy → kontrole.
## Słownik pojęć w dokumencie
- Data Owner/Steward/Custodian, SoD, Lineage, DQ, DLP, SLO, KPI/KRI, Waiver, Sunset.
## Wymagane odwołania do standardów

- RODO/PII i wewnętrzne polityki danych.  
- Standardy jakości danych i katalogowania obowiązujące w organizacji.

## Mapa relacji sekcja→sekcja
- Klasyfikacja/role → Polityki → Metryki/SLO → Procesy → Narzędzia → Audyt → Waivery.
## Mapa relacji dokument→dokument
- Data Governance Requirements ↔ data_strategy/data_classification/privacy/security/retention/tprm/access_control_sod/lineage_standards.
## Ścieżki informacji
- Strategia/klasyfikacja → Polityki → Metryki → Procesy → Narzędzia → Raporty/Audyt → Przeglądy → Aktualizacje.
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
- RACI, matryca klasyfikacji, polityki (access/privacy/retention/sharing), definicje metryk/SLO, procesy i checklisty, katalog/lineage/DQ/DLP wymagania, TPRM rejestr, dashboard KPI/KRI, waiver log, ADR log.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości
- Coverage klasyfikacji, % systemów w katalogu/lineage, SLO jakości spełnione, czas zamykania incydentów danych, liczba waiverów i ich sunset, status audytów.
## Kryteria ukończenia
- [ ] Wymagania governance opisane i powiązane z metrykami/procesami/narzędziami; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

- Cel/KPI → Zakres danych → Źródła/pola → Kryteria jakości → Walidacja/akceptacja.  
- PII/bezpieczeństwo → Dostępy/anonimizacja → Możliwość użycia danych.  
- Braki danych → Plan pozyskania → Ryzyka/terminy.


## Struktura sekcji

1) Cel i pytania analityczne / KPI  
2) Zakres danych (czas, populacja, segmenty)  
3) Źródła i pola (schemy, klucze, wersje, lineage)  
4) Kryteria jakości (świeżość, kompletność, dokładność, spójność)  
5) PII/bezpieczeństwo i dostęp (klasy danych, maskowanie, zgody)  
6) Transformacje i agregacje potrzebne do analizy  
7) Walidacja i akceptacja danych (testy DQ, sampling, sanity checks)  
8) Braki, ryzyka, plan pozyskania/obejść  
9) Artefakty i formaty wyjściowe (datasety, raporty, modele)  
10) Decyzje, otwarte pytania


## Wymagane rozwinięcia

- Tabela pól (nazwa, opis, typ, źródło, jakość, PII).  
- Kryteria DQ z progami i metodą pomiaru; plan monitoringu.  
- Plan pozyskania brakujących danych lub alternatyw.


## Wymagane streszczenia

- Executive summary: cel, kluczowe źródła, ryzyka/braki, gotowość danych.  
- Krótka karta jakości danych (traffic light) dla decydentów.


## Guidance (skrót)

- Zacznij od KPI i pytania; ogranicz zakres danych do niezbędnych.  
- Waliduj jakość i PII przed uruchomieniem analizy/modelu.  
- Dokumentuj definicje pól i transformacje; uaktualnij katalog/kontrakty.  
- Jeśli brakuje danych, zaplanuj pozyskanie z terminem i ownerem.


## Checklisty Definition of Ready (DoR)

- [ ] Cel/KPI i pytania analityczne zatwierdzone.  
- [ ] Źródła danych i dostęp potwierdzone; PII ocenione.  
- [ ] Wstępna tabela pól i kryteria jakości przygotowane.  
- [ ] Zgody/privacy/legal, jeśli wymagane, uzgodnione.  
- [ ] Plan walidacji i narzędzia ustalone.


## Checklisty Definition of Done (DoD)

- [ ] Dane dostarczone zgodnie z zakresem; walidacje DQ zaliczone lub wyjątki udokumentowane.  
- [ ] PII zabezpieczone (maskowanie/anonimizacja); dostępy zarejestrowane.  
- [ ] Artefakty (dataset/raport/model) w uzgodnionym formacie.  
- [ ] Katalog/kontrakty zaktualizowane; status/wersja/data uzupełnione.  
- [ ] Braki/ryzyka zamknięte lub zaakceptowane.

