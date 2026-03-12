---
title: Enterprise Architecture Vision
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Enterprise Architecture Vision

## Metadane
- Właściciel: Solution Architect
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Opisuje wizję architektury przedsiębiorstwa: domeny, capability, zasadnicze decyzje i standardy, docelowe i przejściowe stany (to-be / interim / as-is), kryteria akceptacji i roadmapę transformacji. Ma zapewnić spójność strategiczną między biznesem, produktami, danymi, technologią i operacjami.


## Zakres i granice
- Obejmuje: kontekst biznesowy i mapę capability, domeny i ich interfejsy, zasady segmentacji (biznes/data/app/tech), architekturę targetową i warianty interim, standardy/guardrails, integracje (API/event), dane i ich linie, bezpieczeństwo/compliance, NFR (wydajność, dostępność, odporność, skalowalność), model operacyjny i governance, roadmapę transformacji.
- Poza zakresem: low-level design poszczególnych systemów, szczegółowe runbooki; te pojawią się w dokumentach domenowych/produkowych.



## Wejścia i wyjścia
- Wejścia: strategia biznesowa i produktowa, mapy procesów i capability, as-is architektura i CMDB, backlog inicjatyw, ograniczenia regulacyjne/techniczne/finansowe, istniejące ADR/standardy, dane referencyjne i integracje, plany sourcingu/partnerstw.
- Wyjścia: target i interim architektura przedsiębiorstwa (diagramy kontekst/warstwy/domeny/linie danych), zasady/guardrails, decyzje architektoniczne z uzasadnieniem, roadmapa transformacji z kamieniami i zależnościami, plan migracji danych i integracji, kryteria go/no-go, lista ryzyk/założeń.



## Powiązania (meta)
- Key Documents: business_strategy, product_strategy_document, technology_strategy, data_strategy, security_architecture_vision, integration_strategy, operating_model, sourcing_strategy, cost_model/FinOps, risk_register.
- Key Document Structures: domena/capability → usługi/aplikacje → dane → interfejsy → bezpieczeństwo/compliance → operacje.
- Document Dependencies: polityki/regulacje (np. GDPR/PCI/ISO), standardy architektoniczne organizacji, katalog usług wspólnych, umowy z dostawcami/partnerami.
- RACI: Enterprise Architect (owner), Domain/Capability Architects, Security, Data, Infra/Cloud, Product, Ops, Finance/Procurement.
- Standardy/compliance: architektura referencyjna, standardy API/event/IaC, klasyfikacja danych, IAM/segregacja, DR/BCP, FinOps/GreenOps.

## Zależności dokumentu
- Upstream: strategia i portfel inicjatyw, decyzje korporacyjne (cloud, buy vs build, vendor lock-in), dane o bieżących systemach/umowach, regulacje.
- Downstream: architektury domenowe, projekty produktów, backlog epik/roadmap, plany danych/integracji, standardy implementacyjne, budżety i kontrakty.
- Zewnętrzne: dostawcy chmurowi/SaaS, integracje partnerskie, wymogi regulatorów (lokalizacja danych, audyt), zależności łańcucha dostaw.



## Powiązania sekcja↔sekcja
- Capability/domena → Usługi/aplikacje → Dane/linia danych → Integracje → Bezpieczeństwo/compliance → Operacje/monitoring → Ciągłe doskonalenie.
- NFR/guardrails → Decyzje/ADR → Roadmapa transformacji → Kryteria go/no-go.



## Fazy cyklu życia
- Discovery: inwentaryzacja as-is, mapy capability/domen, problemy i ryzyka.
- Target/Interim Design: warianty, ADR, model danych i integracji, standardy/guardrails.
- Review: board (arch/security/compliance/finanse), koszty/TCO/FinOps, performance i dostępność, ryzyka/regulacje.
- Implementation & Test: zgodność implementacji z target/interim, testy NFR, walidacja integracji i danych.
- Rollout & Ops: migracje etapowe, monitoring/SLO, DR/BCP, governance zmian, postmortems i iteracje.




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
1) Streszczenie i cele biznesowe (KPI, mierniki wartości)
2) Zakres, założenia i ograniczenia (techniczne/prawne/finansowe, preferowane/zakazane tech)
3) Mapa capability/domen i interesariuszy (właściciele, RACI)
4) Target & interim architektura (warstwy: biznes/data/app/tech, diagramy kontekstu/domen/warstw)
5) Dane i linie danych (klasyfikacja, retencja, lineage, katalog, MDM/reference)
6) Integracje i interfejsy (API/event, standardy, SLA, wersjonowanie, kontrakty)
7) Bezpieczeństwo, prywatność, compliance (IAM, sieć, szyfrowanie, audyt, segregacja, regulacje)
8) NFR i SLO (wydajność, dostępność, odporność, skalowalność, DR/BCP, obserwowalność)
9) Plan transformacji i migracji (fazy, kamienie, zależności, cutover, rollback, dane)
10) Governance i operacje (guardrails, arch board, FinOps/GreenOps, zmiany, monitoring, postmortem)
11) Ryzyka i mitigacje; założenia i zależności
12) Decyzje (ADR) i alternatywy; otwarte pytania



## Wymagane rozwinięcia
- Diagramy: kontekst, warstwy, domeny, linie danych, integracje, deployment (jeśli potrzebne).
- Tabela RACI dla domen/capability, bezpieczeństwa, danych, operacji, zmian.
- ADR: decyzje, alternatywy, konsekwencje, sunset/rewizje.
- Plan migracji danych i systemów (walidacje, równoległość, ryzyka, rollback).
- Macierz NFR/SLO z właścicielami i metodą pomiaru.



## Wymagane streszczenia
- Executive summary: cele, wartość, target/interim, top decyzje, ryzyka, koszty/TCO.
- One-pager: mapa domen/capability, główne integracje, SLO/NFR, plan transformacji (fazy/kamienie).



## Guidance (skrót)
- DoR: inwentaryzacja as-is (systemy, dane, integracje), mapy capability/domen, cele/KPI, ograniczenia/regulacje, właściciele domen, zebrane NFR/SLO.
- DoD: target/interim opisane diagramami i ADR; dane/integracje/security/compliance/NFR pokryte; plan transformacji/migracji z testami i kryteriami go/no-go; ryzyka/założenia; metadane aktualne; dokument w linkage_index.
- Spójność: każda domena ma ownera, integracje mają kontrakty/SLA, dane mają klasyfikację/retencję, NFR mają metryki i testy.



## Szybkie powiązania
- business_strategy, product_strategy_document, technology_strategy, data_strategy, security_architecture_vision, integration_strategy, operating_model, sourcing_strategy, cost_model, finops_guidelines, greenops_guidelines
- risk_register, change_management_process, dr_plan, architecture_principles, cloud_architecture_vision

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

### Polskie normy i regulacje
- **UoR-PL** — Ustawa o Rachunkowości

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty Definition of Ready (DoR)
- [ ] Inwentaryzacja as-is (systemy, dane, integracje) zakończona; mapy capability/domen gotowe.
- [ ] Cele/KPI i NFR/SLO zebrane; ograniczenia/regulacje/guardrails spisane.
- [ ] Ownerzy domen/capability i kluczowi interesariusze potwierdzeni; warianty target/interim zidentyfikowane.

## Checklisty Definition of Done (DoD)
- [ ] Target/interim architektura opisana diagramami; ADR i alternatywy udokumentowane.
- [ ] Dane/integracje/security/compliance/NFR pokryte; plan transformacji/migracji z testami i kryteriami go/no-go.
- [ ] Ryzyka/założenia/dependencies opisane; metadane aktualne; dokument w linkage_index.

## Definicje robocze
- Capability — zdolność biznesowa realizowana przez procesy, dane i systemy.
- Domain — spójny obszar funkcjonalny z jasno określonym właścicielem i interfejsami.
- Guardrails — zasady ograniczające wybory architektoniczne/technologiczne (np. dozwolone chmury, standardy API/IaC).

## Przykłady użycia
- Transformacja platformy płatniczej: segmentacja domen (Payments, Risk/Fraud, Ledger), event-driven integracje, multi-region, PCI/DR/BCP, plan migracji danych i cutover.
- Konsolidacja aplikacji front-office: target composable architecture, API gateway + event mesh, wspólne capability (identity/catalog), redukcja duplikatów, roadmapa fazowa.

## Artefakty powiązane
- Mapy capability/domen, CMDB/system inventory, diagramy C4/layered, ADR log, macierz NFR/SLO, plan migracji danych, katalog API/event, RACI, FinOps/GreenOps modele kosztów.

## Weryfikacja spójności
- [ ] Dla każdej domeny: owner, interfejsy, dane (klasyfikacja/retencja), NFR/SLO, ryzyka i zależności.
- [ ] Integracje mają kontrakty, SLA i wersjonowanie; dane mają lineage i polityki.
- [ ] Plan transformacji ma kamienie, kryteria go/no-go, testy i rollback.

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
