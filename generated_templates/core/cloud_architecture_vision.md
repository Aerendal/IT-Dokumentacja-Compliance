---
title: Cloud Architecture Vision
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Cloud Architecture Vision

## Metadane
- Właściciel: Solution Architect
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Opisuje wizję architektury chmurowej: model wdrożenia (single/multi-cloud, regiony), landing zone, sieć/IAM, bezpieczeństwo/compliance, obserwowalność, spójność kosztów (FinOps/GreenOps), standardy IaC/policy-as-code oraz roadmapę migracji/modernizacji. Definiuje kryteria akceptacji i trade‑offy.


## Zakres i granice
- Obejmuje: kontekst biznesowy, model chmury (IaaS/PaaS/SaaS, regiony/AZ), landing zone (network, IAM, logi, klucze, tagowanie), architekturę referencyjną (warstwy: edge/app/data/ops), integracje (hybrid/multi-cloud/VPN/DirectConnect/ExpressRoute), bezpieczeństwo/compliance (segregacja, szyfrowanie, klucze, audit), NFR (wydajność, dostępność, skalowalność, RTO/RPO), obserwowalność, DR/BCP, FinOps/GreenOps, standardy IaC/policy-as-code, governance i wyjątki.
- Poza zakresem: low-level konfiguracje usług, szczegółowe runbooki (opisane w runbookach operacyjnych).



## Wejścia i wyjścia
- Wejścia: strategia IT/produktowa, wymagania biznesowe i NFR, inwentaryzacja workloadów (krytyczność/klasyfikacja danych), ocena gotowości do chmury, ograniczenia regulacyjne/lokalizacyjne, istniejące umowy/dostawcy, koszty/TCO, standardy organizacyjne, ADR/guardrails.
- Wyjścia: target/interim cloud architecture (regiony, landing zone, VPC/VNet, IAM, logowanie, klucze), standardy IaC/policy-as-code, wzorce referencyjne (app/data/ML/edge), plan migracji/modernizacji i go/no-go, model FinOps/GreenOps, ryzyka i mitigacje.



## Powiązania (meta)
- Key Documents: enterprise_architecture_vision, cloud_strategy, security_architecture_vision, data_architecture_vision, network_architecture, identity_and_access_architecture, dr_plan, finops_guidelines, greenops_guidelines, integration_strategy.
- Key Document Structures: workload → architektura (VPC/VNet, IAM, storage, compute, data, observability) → bezpieczeństwo → koszt → operacje/DR.
- Document Dependencies: polityki bezpieczeństwa/compliance, standardy IaC/policy-as-code, katalog usług wspólnych, kontrakty z CSP, strategie lokalizacji danych.
- RACI: Cloud Platform (owner), Security, Network, Identity, Data, App/DevOps, FinOps, Compliance.
- Standardy/compliance: CIS Benchmarks, ISO/IEC, SOC2, PCI, HIPAA, lokalizacja danych, tagging/CMDB, backup/DR normy.

## Zależności dokumentu
- Upstream: decyzje strategiczne (single/multi/hybrid), regulacje, umowy CSP, polityki bezpieczeństwa/danych, limity kosztów.
- Downstream: projekty migracyjne, wzorce referencyjne, backlog epik, runbooki, testy DR, monitoring/observability, FinOps reporting.
- Zewnętrzne: CSP, partnerzy sieciowi, regulatorzy (lokalizacja, retencja, audyt), łańcuch dostaw (SaaS/marketplace).



## Powiązania sekcja↔sekcja
- Workload/NFR → Wybór regionów/architektury → Sieć/IAM/storage/compute → Bezpieczeństwo/compliance → Observability/DR → FinOps.
- Tagging/CMDB → FinOps/GreenOps → Alerty kosztowe → Decyzje skalowania.



## Fazy cyklu życia
- Discovery: inwentaryzacja workloadów, klasyfikacja danych, ocena gotowości, warianty (rehost/replatform/refactor/retire/retain).
- Target/Interim design: regiony, landing zone, sieć/IAM, standardy IaC/policy, wzorce referencyjne (app/data/ML), NFR/DR.
- Review: arch/security/compliance/FinOps, koszty/TCO, lokalizacja i regulacje, performance.
- Implementation & Test: budowa landing zone, wzorców, validacja bezpieczeństwa/DR, testy NFR, pilot migracji.
- Rollout & Ops: migracje etapowe, monitoring/SLO, FinOps/GreenOps, audyty, postmortem, ciągłe doskonalenie.




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
1) Streszczenie i cele (biznes, czas/ryzyko/koszt)
2) Zakres, założenia, ograniczenia (regulacje, dane wrażliwe, RTO/RPO, limity kosztów)
3) Workloady i wymagania (klasyfikacja, NFR, priorytety migracji)
4) Target/interim architektura (regiony/AZ, landing zone: sieć, IAM, logi, klucze, tagi, CMDB)
5) Wzorce referencyjne (app, data, ML, edge, storage/backup, CI/CD, observability)
6) Bezpieczeństwo/compliance (segregacja, szyfrowanie, klucze, IAM, audit, privacy, data residency)
7) Observability i operacje (logi/metryki/tracing, SLO/SLA, incident/DR, capacity, change, IaC/policy-as-code)
8) FinOps/GreenOps (tagging, budżety/alerty, showback/chargeback, optymalizacje, ślad węglowy)
9) Plan migracji/modernizacji (strategie 6R, fale, walidacje, cutover/rollback)
10) Ryzyka i mitigacje; założenia i zależności
11) Decyzje (ADR) i otwarte pytania



## Wymagane rozwinięcia
- Diagramy: landing zone, sieć/VPC/VNet, IAM, wzorce referencyjne, DR/topologie, data flow.
- RACI dla chmury (sieć/IAM/security/data/FinOps/ops), governance i fora.
- ADR: wybór regionów, single vs multi-cloud, standardy IaC/policy, wzorce referencyjne, data residency.
- Plan migracji: 6R per workload, walidacje, testy DR, rollback.
- FinOps/GreenOps: tagowanie, budżety, KPI kosztowe/energetyczne.



## Wymagane streszczenia
- Executive summary: model chmury, regiony, koszty/TCO, top decyzje, ryzyka, plan migracji.
- One-pager: landing zone, wzorce referencyjne, bezpieczeństwo/DR, FinOps/GreenOps, roadmapa.



## Guidance (skrót)
- DoR: inwentaryzacja workloadów i danych (klasyfikacja, NFR), regulacje/lokalizacja znane, warianty regionów/modelu chmury zebrane, limity kosztów ustalone, ownerzy i fora governance wyznaczeni.
- DoD: target/interim architektura z landing zone i wzorcami, bezpieczeństwo/compliance/DR/observability opisane, plan migracji/6R z testami i rollbackiem, FinOps/GreenOps z KPI, ryzyka/założenia; metadane aktualne; dokument w linkage_index.
- Spójność: każdy workload ma NFR, klasy danych, strategię migracji 6R, region/AZ i kontrolki; tagowanie/CMDB i polityki kosztowe są zdefiniowane.



## Szybkie powiązania
- enterprise_architecture_vision, cloud_strategy, security_architecture_vision, data_architecture_vision, integration_strategy, network_architecture, identity_and_access_architecture, dr_plan, finops_guidelines, greenops_guidelines, cloud_compliance_roadmap

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 27017** — Bezpieczeństwo w Chmurze Obliczeniowej
- **ISO/IEC 27018** — Ochrona Danych Osobowych w Chmurze (PII)
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum
- **SOC 2** — Kontrole Organizacji Usług (Typ I i II)
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty Definition of Ready (DoR)
- [ ] Workloady zinwentaryzowane i sklasyfikowane; regulacje/lokalizacja znane; limity kosztów ustalone.
- [ ] Warianty regionów/modelu chmury i standardy IaC/policy zidentyfikowane; fora governance i ownerzy wyznaczeni.

## Checklisty Definition of Done (DoD)
- [ ] Target/interim architektura z landing zone, wzorcami, bezpieczeństwem/DR/observability; ADR opisane.
- [ ] Plan migracji 6R z walidacjami/testami/rollbackiem; FinOps/GreenOps KPI zdefiniowane.
- [ ] Ryzyka/założenia opisane; metadane aktualne; dokument w linkage_index.

## Definicje robocze
- Landing zone — minimalny zestaw usług/konfiguracji (sieć/IAM/logi/klucze/tagi/CMDB) pod wszystkie workloady.
- 6R — rehost, replatform, refactor, retire, retain, repurchase (strategia migracji per workload).
- FinOps/GreenOps — zarządzanie kosztem i śladem środowiskowym usług chmurowych.

## Przykłady użycia
- Migracja monolitu do chmury: landing zone, wybór regionu, replatform + strangler, DR multi-AZ, IaC/policy, FinOps tagowanie.
- Platforma danych real-time: multi-AZ, sieć hub-spoke, stream + lakehouse, security (IAM/KMS, tokeny), SLO opóźnień, koszt i GreenOps.

## Artefakty powiązane
- Diagramy landing zone i sieci, katalog usług/wzorców, ADR log, rejestr workloadów i strategii 6R, plan migracji, RACI, FinOps/GreenOps dashboardy, testy DR, policy-as-code repo.

## Weryfikacja spójności
- [ ] Każdy workload ma przypisany model migracji 6R, region/AZ, klasę danych i NFR.
- [ ] Landing zone spełnia bezpieczeństwo/compliance; tagging/CMDB i polityki kosztowe działają.
- [ ] Plan migracji zawiera testy DR, walidacje i rollback; FinOps/GreenOps KPI są mierzalne.

## Ryzyka i ograniczenia
- [Ryzyko 1 — wpływ i sposób ograniczenia]
- [Ryzyko 2 — wpływ i sposób ograniczenia]

## Decyzje i uzasadnienia
- [Decyzja 1 — uzasadnienie]
- [Decyzja 2 — uzasadnienie]

## Założenia
- [Założenie 1]
- [Założenie 2]

## Otwarte pytania
- [Pytanie 1]
- [Pytanie 2]

## Powiązania z innymi dokumentami
- [Dokument A] — [typ relacji] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów
- [Dokument X → Sekcja Y] — [powód powiązania]
- [Dokument Z → Sekcja W] — [powód powiązania]

## Słownik pojęć w dokumencie
- [Pojęcie 1] — [definicja i źródło]
- [Pojęcie 2] — [definicja i źródło]
- [Pojęcie 3] — [definicja i źródło]

## Wymagane odwołania do standardów
- [Standard 1] — [sekcja/fragment, którego dotyczy]
- [Standard 2] — [sekcja/fragment, którego dotyczy]

## Mapa relacji sekcja→sekcja
- [Sekcja A] -> [Sekcja B] : [typ relacji]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument
- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji
- [Wejście] → [Sekcja źródłowa] → [Sekcja rozwinięcia] → [Wyjście]
- [Wejście] → [Sekcja źródłowa] → [Sekcja streszczenia] → [Wyjście]

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
- [Artefakt 1] — [opis i relacja do dokumentu]
- [Artefakt 2] — [opis i relacja do dokumentu]

## Ścieżka decyzji
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]

## Użytkownicy i interesariusze
- **Solution / Enterprise Architect** — projektuje i zatwierdza architekturę
- **Tech Lead** — odpowiada za spójność techniczną implementacji
- **Product Owner** — definiuje wymagania biznesowe wchodzące na wejście
- **Development Team** — implementuje na podstawie projektu

## Ścieżka akceptacji
- [Kto zatwierdza] → [kryteria akceptacji] → [status]
- [Kto zatwierdza] → [kryteria akceptacji] → [status]

## Kryteria ukończenia
- [ ] Kryterium 1 — [opis]
- [ ] Kryterium 2 — [opis]

## Metryki jakości
- [Metryka 1] — [cel / próg]
- [Metryka 2] — [cel / próg]

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
