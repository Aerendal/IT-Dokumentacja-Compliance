---
title: Data Architecture Vision
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Data Architecture Vision

## Metadane
- Właściciel: Solution Architect
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Opisuje wizję architektury danych: domeny i linie danych, klasyfikację i jakość, platformy (ingest/processing/storage/analytics/ML), integracje (API/event/batch), bezpieczeństwo i prywatność, standardy oraz roadmapę transformacji. Ustala kryteria akceptacji i trade‑offy.


## Zakres i granice
- Obejmuje: kontekst biznesowy i mapę domen danych, typy obciążeń (OLTP/OLAP/stream/ML), platformy i usługi danych, modele danych (canonical/semantic), linie danych i lineage, jakość i katalogowanie, standardy API/event/schema, bezpieczeństwo/prywatność/compliance (PII/PCI/PHI), NFR (skala, wydajność, dostępność, opóźnienia), model operacyjny i governance, plan migracji/modernizacji.
- Poza zakresem: low-level DDL/ETL jobów, szczegółowe pipeline’y operacyjne – będą w dokumentach implementacyjnych/runbookach.



## Wejścia i wyjścia
- Wejścia: strategia biznesowa/produktowa, katalog systemów źródłowych, typy use case (BI/real‑time/ML), ograniczenia regulacyjne (GDPR/PCI/HIPAA), standardy korporacyjne, istniejące platformy danych, koszty/TCO, wymagania NFR (SLO, RPO/RTO, latency), dane referencyjne/master.
- Wyjścia: target i interim architektura danych (diagramy: strefy/layering, przepływy, lineage), standardy schema/API/event, zasady klasyfikacji/retencji/anonimizacji, plan migracji i modernizacji, katalog komponentów/platform, decyzje/ADR z trade‑offami, ryzyka i mitigacje.



## Powiązania (meta)
- Key Documents: enterprise_architecture_vision, data_strategy, integration_strategy, security_architecture_vision, privacy_impact_assessment, mlops_architecture, analytics_strategy, cloud_architecture_vision, data_governance_model.
- Key Document Structures: domena danych → źródła → przetwarzanie → przechowywanie → udostępnianie → bezpieczeństwo → obserwowalność → operacje.
- Document Dependencies: polityki danych (klasyfikacja/retencja/DLP), kontrakty danych i SLAs, katalog danych/MDM, umowy z dostawcami chmurowymi/SaaS, wytyczne FinOps/GreenOps.
- RACI: Chief Data Officer / Data Architect (owner), Security/Privacy, Platform/Data Engineering, Analytics/BI, ML, Domain Owners, Ops/FinOps.
- Standardy i compliance: GDPR/PCI/HIPAA/GLBA, ISO/IEC 27001, SOC2, lokalizacja danych, standardy API/event/schema/versioning, szyfrowanie i klucze.

## Zależności dokumentu
- Upstream: strategia/EA, regulacje, polityki danych/security, aktualne systemy i kontrakty, dostępność danych źródłowych.
- Downstream: projekty BI/AI/produktowe, integracje API/event, katalog danych/MDM, ML pipeline’y, observability i FinOps/GreenOps raportowanie, runbooki.
- Zewnętrzne: dostawcy chmurowi/SaaS, integracje partnerskie, wymogi regulatorów co do lokalizacji/retencji/audytu.



## Powiązania sekcja↔sekcja
- Use case/NFR → Model danych i linie → Platformy/komponenty → Bezpieczeństwo/priv → Operacje/observability → SLA/SLO.
- Klasyfikacja/retencja → Architektura storage → Anonimizacja/DLP → Dostęp/udostępnianie → Audyt/compliance.



## Fazy cyklu życia
- Discovery: inwentaryzacja źródeł i obciążeń, gap vs wymagania, decyzja buy/build/reuse.
- Target/Interim design: strefy/layers, formaty, governance, NFR, security/privacy, ADR.
- Review: arch/security/privacy/FinOps, koszty, performance/latency, lokalizacja danych.
- Implementation & Test: budowa stref/pipeline, walidacja danych/jakości, testy NFR, dry-run migracji.
- Rollout & Ops: migracje etapowe, monitorowanie SLA/SLO, audyty, optymalizacja kosztów, postmortem.




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
1) Streszczenie i cele biznesowe (KPI danych, decyzje oparte na danych)
2) Zakres, założenia, ograniczenia (regulacje, lokalizacja danych, limit kosztów/latency)
3) Domeny danych i interesariusze (ownerzy, RACI, źródła krytyczne)
4) Architektura target/interim (strefy: raw/cleansed/curated/serving, batch/stream, lake/warehouse/mart, API/event)
5) Model danych i linie (canonical/semantic, standardy schematów, wersjonowanie, lineage)
6) Jakość danych i katalogowanie (DQ rules, scoring, data contracts, katalog/MDM/reference)
7) Bezpieczeństwo/prywatność/compliance (klasyfikacja, retencja, maskowanie/anonimizacja, DLP, IAM, klucze, audyt)
8) Platformy i komponenty (ingest/ETL/ELT, stream, storage, processing, ML/feature store, BI/semantics)
9) NFR i SLO (skala, latency, dostępność, RPO/RTO, koszt/FinOps, GreenOps, obserwowalność)
10) Plan migracji/modernizacji (fazy, kamienie, walidacje jakości, cutover/rollback)
11) Governance i operacje (fora, cadence, role, proces zmian, audyty, postmortem)
12) Ryzyka i mitigacje; założenia i zależności
13) Decyzje (ADR) i otwarte pytania



## Wymagane rozwinięcia
- Diagramy stref/warstw, przepływów, lineage, kontraktów API/event, deployment (jeśli potrzebne).
- RACI dla domen danych, katalogu/MDM, bezpieczeństwa/prywatności, operacji i kosztów.
- ADR: wybór storage/formatów, polityki retencji, standardy event/schema, integracje krytyczne.
- Plan migracji danych: walidacje jakości, dual‑run, reconciliacje, rollback.
- Macierz NFR/SLO (skala, latency, koszt, RPO/RTO) z metodą pomiaru/testów.



## Wymagane streszczenia
- Executive summary: cele danych, architektura target/interim, top decyzje, ryzyka, koszty/TCO, plan migracji.
- One-pager: strefy/warstwy, główne źródła i interfejsy, SLO/NFR, plan i kamienie.



## Guidance (skrót)
- DoR: zinwentaryzowane źródła i obciążenia (BI/stream/ML), regulacje i klasyfikacja danych znane, NFR/SLO i ograniczenia kosztów zebrane, ownerzy domen i dane referencyjne wskazani.
- DoD: target/interim opisane; dane/linia/jakość/katalog/security/privacy/NFR pokryte; plan migracji z walidacjami i rollbackiem; ryzyka/założenia; metadane aktualne; dokument w linkage_index.
- Spójność: każde źródło ma klasę danych i właściciela; każdy interfejs ma kontrakt i wersjonowanie; NFR mają metryki i testy.



## Szybkie powiązania
- enterprise_architecture_vision, data_strategy, integration_strategy, security_architecture_vision, privacy_impact_assessment, analytics_strategy, mlops_architecture, cloud_architecture_vision, data_governance_model
- risk_register, change_management_process, dr_plan, finops_guidelines, greenops_guidelines

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty Definition of Ready (DoR)
- [ ] Inwentaryzacja źródeł i obciążeń (BI/stream/ML) zakończona; klasyfikacja/regulacje znane.
- [ ] NFR/SLO i limity kosztów/latency zebrane; ownerzy domen i danych referencyjnych wskazani.
- [ ] Warianty target/interim i standardy (schema/API/event) wstępnie zidentyfikowane.

## Checklisty Definition of Done (DoD)
- [ ] Target/interim architektura danych opisana diagramami; standardy schema/API/event określone.
- [ ] Jakość/katalog/MDM, bezpieczeństwo/prywatność, NFR/SLO pokryte testami i metrykami.
- [ ] Plan migracji/modernizacji z walidacjami, reconciliacją i rollbackiem; ryzyka/założenia opisane; metadane aktualne; dokument w linkage_index.

## Definicje robocze
- Data lineage — śledzenie pochodzenia danych i transformacji na kolejnych etapach.
- Data contract — uzgodniony schemat/kontrakt API/event dla producenta/konsumenta danych.
- NFR/SLO danych — wymagania dotyczące skali, opóźnień, dostępności, jakości, kosztu.

## Przykłady użycia
- Modernizacja hurtowni: migracja do lakehouse, standaryzacja schematów, event ingestion, DQ/lineage, FinOps.
- Real-time analytics: Kappa/stream-first, event contracts, low-latency storage, SLO na opóźnienia, privacy/masking, obserwowalność pipeline’ów.

## Artefakty powiązane
- Mapy źródeł i lineage, katalog danych/MDM, kontrakty API/event, DQ rules, ADR log, plan migracji, macierz NFR/SLO, RACI, dashboard SLO/FinOps/GreenOps.

## Weryfikacja spójności
- [ ] Każde źródło i strumień ma właściciela, klasę danych i kontrakt.
- [ ] Lineage i DQ są zdefiniowane dla kluczowych zestawów; NFR/SLO mają metryki i testy.
- [ ] Plan migracji ma walidacje, reconciliacje i rollback; decyzje zgodne z regulacjami i kosztami.

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
