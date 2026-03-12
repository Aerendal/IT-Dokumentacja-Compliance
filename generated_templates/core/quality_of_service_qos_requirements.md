---
title: Quality of Service (QoS) Requirements
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Quality of Service (QoS) Requirements


## Metadane

- Właściciel: Product Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Określić wymagania QoS dla usług/systemów: parametry wydajności, niezawodności, priorytety ruchu i zasady egzekwowania.


## Zakres i granice

- Obejmuje: SLO/SLI (latencja, throughput, dostępność, jitter, packet loss), klasy ruchu/prioritization, limity/rate limiting, kolejki, capacity i rezerwy, polityki degradacji, monitoring i alerty, testy QoS.
- Poza zakresem: szczegółowe konfiguracje sieci (oddzielne runbooki), QoE użytkownika (osobne dokumenty jeśli potrzebne).


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia
- Wejścia: cele biznesowe, brief produktowy, regulacje, istniejące procesy/systemy, dane referencyjne.
- Wyjścia: uporządkowana lista wymagań z priorytetami, kryteriami akceptacji i powiązaniem z testami/architekturą.
## Założenia
- Zespoły architektury/ops/security dostępne do review.  
- Narzędzia CI/CD/monitoringu są dostępne.  
- Polityki bezpieczeństwa i PII obowiązują.
## Otwarte pytania
- Czy potrzebne są warianty architektury na różne rynki/regulacje?  
- Jakie limity kosztowe/skalowalności są akceptowalne?  
- Jakie są wymagania klientów na SLO/raportowanie?
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
- Elicytacja i warsztaty.
- Konsolidacja i priorytetyzacja.
- Walidacja z interesariuszami (biznes/arch/security/legal).
- Traceability do backlogu/testów.
## Struktura sekcji (szkielet)

- Klasy usług i priorytety
- SLO/SLI i progi
- Polityki QoS (queueing, shaping, rate limit, retry)
- Degradacja kontrolowana i fallbacki
- Monitoring i alerty
- Testy QoS i walidacja
- Utrzymanie i przeglądy


## Szybkie powiązania

- Capacity Planning, Incident Management, Performance runbooks, Network design, API Rate Limiting.


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)

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

- Wymagania biznesowe/SLA, profil ruchu, architektura usług, zależności, ryzyka, wcześniejsze incydenty.


## Wyjścia

- Zestaw wymagań QoS per klasa usługi, progi SLO/SLI, polityki priorytetyzacji/degradacji, plan monitoringu i testów.



## Jak używać (checklista)

- Zidentyfikuj klasy ruchu/usług; przypisz priorytety i SLO.
- Ustal polityki queue/shaping/limitów; zdefiniuj fallback/degradację.
- Skonfiguruj monitoring i alerty; zaplanuj testy (synthetic/chaos/load).
- Włącz zasady do change/incident mgmt.


## Wymagane rozwinięcia / powiązania

- Tabela SLO/SLI per klasa, matryca priorytetów, przykładowe konfiguracje, plan testów QoS.


## Kryteria DoR

- Profil ruchu i wymagania SLA znane; inwentarz usług; akceptacja biznesu na priorytety.


## Kryteria DoD

- SLO/SLI i polityki QoS zatwierdzone; monitoring i testy uruchomione; fallbacki udokumentowane.


## Artefakty

- Spec QoS, konfiguracje, dashboardy, raporty testów, matryca priorytetów.


## Walidacja

- Testy load/chaos; weryfikacja alertów; analiza incydentów vs progi.


## Metryki

- SLO compliance, latency/jitter/loss, liczba/czas degradacji kontrolowanej, % ruchu w klasach priorytetowych.


## Utrzymanie

- Przegląd kwartalny SLO/priorytetów; aktualizacja po zmianach architektury/ruchu.


## Zakończenie

Wymagania QoS zapewniają przewidywalność usług; utrzymuj je wraz z monitoringiem i testami.

