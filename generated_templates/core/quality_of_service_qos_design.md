---
title: Quality of Service (QoS) Design
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Quality of Service (QoS) Design


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Zaprojektować QoS dla usług/ruchu sieciowego/aplikacyjnego: klasy, priorytety, polityki i monitorowanie.


## Zakres i granice

- Obejmuje: klasy usług (voice/video/data/ctrl), oznaczenia (DSCP/CoS), kolejkowanie/shaping, rate limiting, polityki retry/timeout, SLA/SLO, monitoring (latencja/jitter/loss), testy QoS, bezpieczeństwo i izolacja ruchu.
- Poza zakresem: fizyczny design sieci (topologia) – osobne dokumenty.


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

- Klasy i oznaczenia ruchu
- Polityki kolejkowania/shaping/rate limit
- SLA/SLO i progi
- Monitoring i alerty
- Testy QoS i walidacja
- Bezpieczeństwo/izolacja
- Utrzymanie i przeglądy


## Szybkie powiązania

- QoS Requirements, Network design, Observability, Incident Management, Change Management.


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

### Polskie normy i regulacje
- **PN-EN-ISO-9001** — PN-EN ISO 9001:2015-10 — Systemy Zarządzania Jakością
- **PN-EN-ISO-IEC-20000-1** — PN-EN ISO/IEC 20000-1:2019 — Zarządzanie Usługami IT
- **PN-ISO/IEC-27001** — PN-ISO/IEC 27001:2023-09 — Systemy Zarządzania Bezpieczeństwem Informacji

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

Wypełniaj każdą sekcję zgodnie z rzeczywistym stanem dokumentowanego systemu lub projektu.
- Sekcje obowiązkowe: Cel dokumentu, Zakres i granice, Wejścia i wyjścia.
- Sekcje oznaczone [opcjonalnie] wypełnij gdy masz dane; wpisz 'Nie dotyczy' jeśli sekcja nie ma zastosowania.
- Po wypełnieniu przekaż do przeglądu zgodnie z macierzą RACI; zaktualizuj metadata (wersja, data, autor).
- Śledź zmiany przez system kontroli wersji; podlinkuj powiązane dokumenty w sekcji 'Szybkie powiązania'.

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

## Wejścia

- Wymagania biznesowe/SLA, profil ruchu, architektura sieci, ograniczenia regulatorów, narzędzia monitoringu.


## Wyjścia

- Polityka QoS z klasami i parametrami, konfiguracje referencyjne, plan monitoringu/testów, kryteria akceptacji.



## Jak używać (checklista)

- Zdefiniuj klasy ruchu i DSCP/CoS; ustaw kolejki i limity.
- Ustal SLO i alerty; skonfiguruj monitoring.
- Przeprowadź testy QoS; zatwierdź konfigurację; dokumentuj.


## Wymagane rozwinięcia / powiązania

- Tabela klas i parametrów, przykładowe konfiguracje (router/switch/k8s), plan testów, dashboardy.


## Kryteria DoR

- Profil ruchu i SLA znane; dostęp do sprzętu/labu; narzędzia monitoringu dostępne.


## Kryteria DoD

- Polityka QoS opisana, konfiguracje przetestowane, monitoring działa, testy zatwierdzone.


## Artefakty

- Polityka QoS, konfiguracje, plan/testy, dashboardy, raport zatwierdzenia.


## Walidacja

- Testy lab/field, pomiar latencja/jitter/loss, weryfikacja oznaczeń, audyt bezpieczeństwa/izolacji.


## Metryki

- QoS SLO compliance, jitter/latency/loss, % ruchu w klasach, liczba incydentów QoS.


## Utrzymanie

- Przegląd kwartalny klas/progów; testy po zmianach sieci; aktualizacja konfiguracji i dashboardów.


## Zakończenie

Projekt QoS zapewnia przewidywalność ruchu; utrzymuj go z monitoringiem i testami.

