---
title: Phased Market Launch
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Phased Market Launch


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Opisać plan stopniowego wejścia na rynek (phased/rollout): etapy, kryteria, ryzyka, komunikacja i pomiary sukcesu.


## Zakres i granice

- Obejmuje: etapy launch (beta/limited/GA), segmenty/kraje, kryteria wejścia/wyjścia, capacity/operational readiness, ryzyka/regulacje, marketing/PR/CS, metryki sukcesu, monitoring i plan rollback.
- Poza zakresem: szczegółowe kampanie marketingowe (w osobnych planach) i implementacja produktu (osobne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: opis funkcji, ryzyka, metryki SLO/KPI, lista zależności (backend, klienty, dane), plan testów i wyniki, plan komunikacji, feature flags, profile ruchu.  
- Wyjścia: harmonogram i fazy rollout, kryteria i progi przejścia, checklisty pre/post fazy, plan monitoringu i alertów, plan backout, raport końcowy.
## Założenia
- Istnieje stabilny monitoring i obserwowalność.  
- Feature flags lub mechanizmy przełączania są dostępne.  
- Zespoły on‑call gotowe do reakcji.
## Otwarte pytania
- Czy wymagane są osobne fazy dla różnych platform/OS?  
- Jak obsłużyć dane w przypadku rollbacku (idempotencja, duplikaty)?  
- Jakie są limity czasowe na poszczególne fazy wg biznesu?
## Powiązania (meta)
- Key Documents: release_plan, change_management_request, incident_response_runbook, observability_plan, feature_flag_strategy, rollback_plan.  
- Key Document Structures: fazy, kryteria, monitoring/alerty, backout, komunikacja, odpowiedzialności.  
- Document Dependencies: CI/CD, feature flags, monitoring/logi, ticketing, CMDB zależności, system komunikacji.
## Zależności dokumentu
Wymaga: wyników testów (funkcjonalnych/NFR), skonfigurowanych feature flags, metryk/kanałów monitoringu, listy zależności i zgodności wersji (klienci/API), planu komunikacji. Braki = DoR otwarte.
## Fazy cyklu życia
- Przygotowanie: plan faz, testy, checklisty, komunikacja.  
- Wykonanie: faza 0 (dark launch/canary), fazy 1..n (regiony/segmenty), decyzje go/no‑go.  
- Stabilizacja: obserwacja, naprawy, ewentualny roll‑forward, raport.  
- Zamknięcie: retrospektywa, aktualizacja runbooków/metryk.
## Struktura sekcji (szkielet)

- Etapy launch i segmenty/kraje
- Kryteria wejścia/wyjścia (produkt, ops, support, risk/reg)
- Capacity i readiness (infrastruktura, support, billing)
- Komunikacja (marketing/PR/CS) i kanały
- Metryki sukcesu i monitoring
- Plan rollback/mitigacja ryzyk


## Szybkie powiązania
- telemedicine-launch
- phased-activation
- market-analysis
- launch-timeline
- launch-retrospective

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum

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

- Zdefiniuj etapy i kryteria, przygotuj komunikację/monitoring; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.
- Po każdym etapie raportuj metryki i decyzje go/hold/rollback.


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
- Canary: mały procent ruchu służący do weryfikacji przed eskalacją.  
- Backout: powrót do poprzedniej konfiguracji/wersji przy spełnionym triggerze.  
- Observation window: czas monitorowania przed przejściem do kolejnej fazy.
## Przykłady użycia
- Wdrożenie nowej wersji API region‑by‑region.  
- Rollout funkcji z feature flagą na segment użytkowników.  
- Migracja bazy z przełączeniem ruchu w krokach 1%/5%/25%/100%.
## Ryzyka i ograniczenia
- Niekompatybilność wersji klient‑serwer lub schematów.  
- Zbyt krótkie okno obserwacji ukrywa wolne regresje.  
- Brak jasnych progów stop/rollback → opóźnione reakcje.
## Decyzje i uzasadnienia
- Wielkość i liczba faz vs ryzyko i koszt czasu.  
- Progi metryk (error rate, latency, biznes) i warunki stop.  
- Stosowanie roll‑forward vs rollback w zależności od typu regresji.
## Powiązania z innymi dokumentami
- rollback_plan — szczegóły cofnięcia.  
- observability_plan — monitoring i alerty.  
- change_management_request — formalne okno i akceptacje.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Wewnętrzne standardy release/change, polityki bezpieczeństwa, RTO/RPO.  
- Wymogi compliance jeśli dotyczy (np. PCI/HIPAA).
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

## Wejścia

- Strategia produktu/rynku, analizy ryzyka/regulacji, prognozy popytu.
- Stany readiness (produkt, ops, support, billing), SLO/SLA.
- Plan marketing/PR/CS i kanały komunikacji.


## Wyjścia

- Harmonogram etapów i kryteria wejścia/wyjścia.
- Plan komunikacji, monitoring i rollback.
- Raporty metryk sukcesu.



## Szybkie powiązania (uzupełnij)

- risk_management_framework.md
- communication_plan_for_incidents.md
- performance_metrics.md
- system_monitoring_strategy.md
- release_plan.md
- compliance_requirements.md


## Wymagane rozwinięcia / streszczenia

- Tabela etapów: etap → zakres → kryteria wejścia/wyjścia → metryki → owner → data.
- Streszczenie ryzyk i planów mitigacji.


## Wymagane powiązania

- Roadmapa produktu, ryzyka/regulacje, monitoring i capacity, marketing/PR/CS plany.


## Kryteria DoR

- [ ] Etapy i segmenty zdefiniowane; ryzyka/regulacje zebrane.
- [ ] Readiness (produkt/ops/support/billing) ocenione; kanały komunikacji gotowe.
- [ ] Metryki sukcesu/SLO uzgodnione.


## Kryteria DoD

- [ ] Etapy i kryteria opisane; komunikacja/monitoring przygotowane.
- [ ] Plan rollback/mitigacji dodany; quick-links/checklisty zaktualizowane.
- [ ] Metadane bieżące.


## Artefakty do załączenia

- Harmonogram etapów, checklisty readiness.
- Plany komunikacji/monitoringu, plan rollback.
- Raporty metryk po etapach.


## Walidacja / testy

- Dry-run kryteriów wejścia/wyjścia i komunikacji.
- Weryfikacja capacity i SLA przed startem etapu.


## Metryki monitorowane

- Kluczowe KPI produktu per etap (adoption, conversion, churn, NPS).
- Incydenty/alerty i SLA; koszty/kapacity.
- Spełnienie kryteriów wejścia/wyjścia.


## Utrzymanie i aktualizacje

- Przegląd po każdym etapie; aktualizuj plan wg wyników/ryzyk.
- Synchronizuj z roadmapą i planami marketing/PR/CS.


## Zakończenie

Po spełnieniu DoD opublikuj plan/stany etapów, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i przekaż decyzje interesariuszom.
