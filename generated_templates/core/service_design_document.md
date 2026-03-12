---
title: Service Design Document
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Service Design Document


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisuje projekt usługi (service) end‑to‑end: wartość, wymagania, architektura, integracje, SLO/SLA, operacje i bezpieczeństwo. Ma zapewnić spójność między biznesem, architekturą i utrzymaniem.


## Zakres i granice

- Obejmuje: cel/usability, wymagania funkcjonalne i niefunkcjonalne, architekturę logiczną/fizyczną, interfejsy (API/eventy), dane i kontrakty, SLO/SLA, bezpieczeństwo/prywatność, koszt/FinOps, operacje (monitoring, runbooki, incident/change), DR/BCP, roadmapę i ryzyka.  
- Poza zakresem: szczegółowe implementacje komponentów (oddzielne dokumenty), plany marketingowe.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: BRD/FRS, NFR/SLO, architektura referencyjna, katalog zależności, wymagania bezpieczeństwa/privacy, profile ruchu, budżet/koszt, regulacje branżowe.  
- Wyjścia: projekt usługi (diagramy, kontrakty), SLO/SLA, lista zależności i integracji, plan operacyjny (monitoring/runbooki/incident/change), plan DR/BCP, decyzje architektoniczne, ryzyka i roadmapa.


## Założenia

- Zespoły architektury/ops/security dostępne do review.  
- Narzędzia CI/CD/monitoringu są dostępne.  
- Polityki bezpieczeństwa i PII obowiązują.


## Otwarte pytania

- Czy potrzebne są warianty architektury na różne rynki/regulacje?  
- Jakie limity kosztowe/skalowalności są akceptowalne?  
- Jakie są wymagania klientów na SLO/raportowanie?


## Powiązania (meta)

- Key Documents: non_functional_requirements, architecture_decision_records, api_design_standards, observability_plan, security_requirements, dr_plan, cost_management_plan.  
- Key Document Structures: wymagania, architektura, interfejsy, SLO/SLA, bezpieczeństwo, operacje, DR/BCP, koszt, roadmapa.  
- Document Dependencies: CMDB/katalog usług, dependency map, IAM, monitoring/logging, CI/CD, runbooki, ticketing, DR/backup.


## Zależności dokumentu

Wymaga: zdefiniowanych wymagań biznesowych/NFR, mapy zależności, standardów bezpieczeństwa, danych o ruchu i budżecie, dostępnych narzędzi monitoringu/CI/CD/DR. Braki = DoR otwarte.


## Fazy cyklu życia

- Projekt (inicjacja, warianty, decyzje).  
- Wdrożenie i walidacja.  
- Operacje i ciągłe doskonalenie.  
- Modernizacja/decommission.



## Struktura sekcji (szkielet)
- Streszczenie i cele biznesowe
- Zakres, założenia, ograniczenia
- Kontekst domenowy i interesariusze
- Wymagania funkcjonalne i niefunkcjonalne
- Architektura/komponenty i integracje
- Model danych i przepływy informacji
- Bezpieczeństwo, prywatność i compliance
- Plan wdrożenia/migracji i kryteria go/no-go
- Monitoring/operacje oraz ryzyka i mitigacje
- Decyzje i uzasadnienia, pytania otwarte
## Szybkie powiązania

- linkage_index.jsonl (service/design/document)  
- non_functional_requirements, architecture_decision_records, observability_plan, security_requirements, dr_plan


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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

1. Uzupełnij wymagania i SLO/SLA, opisz architekturę i interfejsy.  
2. Dodaj bezpieczeństwo, operacje, DR/BCP i koszt; zmapuj zależności.  
3. Publikuj decyzje i roadmapę; aktualizuj DoR/DoD i linkage_index.


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

- SLO/SLA: cele jakości/usługi i umowy na poziom usług.  
- ADR: zapis decyzji architektonicznych.  
- FinOps: praktyki kontroli kosztów w chmurze/usługach.


## Przykłady użycia

- Nowa usługa API B2B.  
- Modernizacja istniejącej usługi monolitu → mikroserwis.  
- Przygotowanie do audytu/DR testu.


## Ryzyka i ograniczenia

- Brak SLO → brak priorytetyzacji operacji.  
- Nieudokumentowane interfejsy → regresje i integracyjne błędy.  
- Niedoszacowany koszt → przekroczenia budżetu.


## Decyzje i uzasadnienia

- Wybór architektury (mono vs micro) ze względu na SLO/koszt.  
- Wersjonowanie API/eventów.  
- Poziom redundancji i DR vs budżet.


## Powiązania z innymi dokumentami

- architecture_decision_records — decyzje kluczowe.  
- observability_plan — monitoring i SLO.  
- dr_plan — odporność i testy.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- Wewnętrzne standardy architektury, bezpieczeństwa, PII, DR/BCP.  
- Branżowe regulacje, jeśli dotyczy (fin/health/public).

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

- Wymagania → Architektura → Interfejsy → SLO/SLA → Operacje/DR.  
- Bezpieczeństwo → Architektura/Interfejsy → Monitoring/Incident.  
- Koszt/FinOps → Architektura → Roadmapa/priorytety.


## Struktura sekcji

1) Kontekst i cele usługi  
2) Wymagania (funkcjonalne, NFR/SLO/SLA)  
3) Architektura (logiczna/fizyczna, diagramy, decyzje)  
4) Interfejsy i kontrakty (API/eventy, wersjonowanie, kompatybilność)  
5) Dane i zgodność (PII/RODO, retencja, katalog, DQ)  
6) Bezpieczeństwo i kontrolki (IAM, sieć, szyfrowanie, audit)  
7) Operacje i obserwowalność (metryki, logi, tracing, runbooki)  
8) DR/BCP i odporność (RTO/RPO, testy, scenariusze)  
9) Koszt/FinOps (capacity, scaling, limity, budżet)  
10) Roadmapa, ryzyka, decyzje i otwarte pytania


## Wymagane rozwinięcia

- Diagramy architektury i interfejsów; kontrakty API/eventów.  
- SLO/SLA z metodą pomiaru; plan DR/BCP; checklisty operacyjne.  
- Macierz zależności i plan de-risking; plan kosztowy.


## Wymagane streszczenia

- Executive summary: cel, SLO, top ryzyka, koszt i decyzje.  
- Jednostronicowy przegląd architektury i interfejsów.


## Guidance (skrót)

- Ustal SLO/SLA wcześnie i projektuj pod nie; integruj z monitoringiem.  
- Wymagania bezpieczeństwa/PII wpleć w architekturę i kontrakty.  
- Wersjonuj interfejsy i decyzje (ADR); unikaj breaking changes.  
- Planuj koszt i skalowanie (capacity, limity, budżet).  
- Utrzymuj runbooki/DR w sync z projektem.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania biznesowe i NFR/SLO/SLA zebrane.  
- [ ] Zależności i standardy bezpieczeństwa znane.  
- [ ] Wstępna architektura i interfejsy zidentyfikowane.  
- [ ] Dane/PII i wymagania zgodności określone.  
- [ ] Narzędzia monitoringu/CI/CD/DR dostępne.


## Checklisty Definition of Done (DoD)

- [ ] Architektura/interfejsy opisane i wersjonowane; diagramy dołączone.  
- [ ] SLO/SLA, bezpieczeństwo i DR/BCP zdefiniowane; testy/plan.  
- [ ] Operacje/observability/runbooki przygotowane; status/wersja/data uzupełnione.  
- [ ] Koszt/FinOps oszacowany; ryzyka i decyzje udokumentowane.  
- [ ] Linkage_index/CMDB zaktualizowane; luki odnotowane.

