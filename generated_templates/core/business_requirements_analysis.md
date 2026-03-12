---
title: Business Requirements Analysis
status: needs_content
aligned: true
aligned_rev: 3
aligned_at: 2026-02-09
aligned_by: codex
---

# Business Requirements Analysis

## Metadane
- Właściciel: Product Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Zbiera i porządkuje wymagania biznesowe (funkcjonalne i niefunkcjonalne) z jasnymi kryteriami akceptacji, priorytetami oraz ścieżką traceability do testów, architektury i planów wdrożeniowych.


## Zakres i granice
- Obejmuje: persony/use cases, funkcje i wyjątki, reguły biznesowe, dane i integracje, wymagania niefunkcjonalne (wydajność, dostępność, bezpieczeństwo, zgodność, użyteczność), kryteria akceptacji, priorytetyzację i traceability.
- Poza zakresem: projekt techniczny, low-level design i implementacja (opisane w dokumentach architektonicznych/technicznych).



## Wejścia i wyjścia
- Wejścia: cele biznesowe/OKR, brief produktowy, regulacje i polityki, istniejące procesy/systemy, dane referencyjne, wyniki discovery/interviews/warsztatów, ograniczenia techniczne/prawne.
- Wyjścia: uporządkowana lista wymagań z priorytetami (MoSCoW/WSJF), kryteriami akceptacji, mapą NFR, traceability do architektury/testów, lista ryzyk/założeń/dependencies.



## Powiązania (meta)
- Key Documents: solution_vision, business_value_proposition, product_strategy, technology_strategy, security_architecture, data_architecture, integration_strategy, ux_strategy, test_strategy.
- Key Document Structures: persona → use case → wymaganie → kryterium akceptacji → test → metryka.
- Document Dependencies: polityki bezpieczeństwa/compliance, standardy UX, backlog epik/user stories, guardrails arch/tech, dane referencyjne.
- RACI: product owner, business analyst, architecture, security, data, QA/test, legal/compliance, UX.
- Standardy/compliance: regulacje branżowe (np. PCI/HIPAA/GxP/ADA/WCAG), standardy danych/API.

## Zależności dokumentu
- Upstream: strategia/vision, analizy rynku, regulacje, arch guardrails, istniejące procesy i systemy.
- Downstream: architektura high-level, backlog epik/user stories, plany testów (UAT/NFR), plany migracji, szkolenia, komunikacja zmian.
- Zewnętrzne: dostawcy systemów źródłowych, integracje partnerskie, wymagania regulatorów/audytów.



## Powiązania sekcja↔sekcja
- Use case/persona → Wymagania → Kryteria akceptacji → Testy → Raportowanie postępu.
- Reguły biznesowe → Scenariusze testowe → Weryfikacja z danymi i integracjami.



## Fazy cyklu życia
- Elicytacja (wywiady/warsztaty, shadowing, analiza dokumentów).
- Konsolidacja i priorytetyzacja (MoSCoW/WSJF, grupowanie, konflikt priorytetów).
- Walidacja i sign-off (biznes/arch/security/legal/UX/QA).
- Traceability i aktualizacja (mapowanie do epik/user stories, testów, architektury, release planów).




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
1) Cel i kontekst biznesowy (OKR/KPI)
2) Interesariusze, persony i scenariusze (journey, pain points)
3) Wymagania funkcjonalne (priorytety, reguły, wyjątki, business rules)
4) Wymagania niefunkcjonalne (wydajność, dostępność, bezpieczeństwo, zgodność, użyteczność, obserwowalność)
5) Dane i integracje (źródła, słowniki, klasyfikacja, retencja, API/eventy, SLA)
6) Kryteria akceptacji i miary sukcesu (DoD, KPI, testy)
7) Zależności, ryzyka i założenia (techniczne/organizacyjne/regulacyjne)
8) Traceability (mapowanie do epik/user stories, testów, architektury, release/migracji)



## Wymagane rozwinięcia
- Macierz traceability: wymaganie → epik/user story → testy → komponent/architektura → decyzje/ADR.
- Macierz NFR (SLO/SLA, RPO/RTO, bezpieczeństwo, dostępność, UX, dane wrażliwe) z właścicielami i metodą pomiaru.
- Tabela reguł biznesowych i wyjątków, powiązana z testami i danymi.



## Wymagane streszczenia
- Streszczenie: zakres, priorytety, KPI, top ryzyka i zależności, plan walidacji.



## Guidance (skrót)
- DoR: zebrane źródła, interesariusze i cele; zidentyfikowane persony/use cases; wstępne priorytety; ograniczenia/regulacje znane; dostęp do danych/systemów potwierdzony.
- DoD: wymagania opisane i priorytetyzowane, kryteria akceptacji i NFR zdefiniowane, traceability do epik/testów/architektury, ryzyka/założenia opisane, metadane aktualne.
- Sprawdzaj spójność: każde wymaganie powinno mieć właściciela, priorytet, kryterium akceptacji, mapowanie do testu i komponentu.



## Szybkie powiązania
- solution_vision_document, business_value_proposition, product_strategy, technology_strategy, ux_strategy, data_architecture, security_architecture, integration_strategy, test_strategy, accessibility_requirements
- compliance_requirements, privacy_impact_assessment, risk_register, change_management_process

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty Definition of Ready (DoR)
- [ ] Zebrane źródła, interesariusze, persony/use cases; znane regulacje/ograniczenia.
- [ ] Wstępne priorytety i metoda priorytetyzacji (np. WSJF) uzgodnione.
- [ ] Dostęp do danych/systemów potwierdzony; NFR kategorie spisane.

## Checklisty Definition of Done (DoD)
- [ ] Wymagania funkcjonalne/niefunkcjonalne opisane i priorytetyzowane; kryteria akceptacji gotowe.
- [ ] Traceability do epik/user stories, testów i architektury; NFR z metodą pomiaru.
- [ ] Ryzyka/założenia/dependencies udokumentowane; metadane aktualne; dokument w linkage_index.

## Definicje robocze
- Kryterium akceptacji — mierzalny warunek spełnienia wymagania (pass/fail), łączony z testem.
- Traceability — powiązanie wymagania z epik/user story, testem, komponentem, decyzją architektoniczną.
- NFR — wymagania niefunkcjonalne wpływające na SLO/SLA, bezpieczeństwo, zgodność, UX.

## Przykłady użycia
- Nowy kanał sprzedaży: zdefiniowanie wymagań koszyka/płatności, NFR (SLO, bezpieczeństwo PCI, dostępność), traceability do epik i testów UAT.
- System raportowy: wymagania na źródła danych, SLA odświeżania, uprawnienia, dostępność, testy akceptacyjne i integracja z architekturą danych.

## Artefakty powiązane
- Backlog epik/user stories, macierz traceability, tabela reguł biznesowych, macierz NFR, diagramy procesów, prototypy UX, plan testów.

## Weryfikacja spójności
- [ ] Każde wymaganie ma kryterium akceptacji, priorytet, właściciela i powiązanie z testem.
- [ ] NFR mają metody pomiaru i są powiązane z testami/monitoringiem.
- [ ] Traceability pokrywa epik → wymaganie → test → architektura → release.

## Ryzyka i ograniczenia
- Bias w danych (niedoreprezentowane segmenty).  
- Braki PII/zgód mogą zablokować użycie danych.  
- Niska jakość danych wydłuża czas analizy lub fałszuje wyniki.
## Decyzje i uzasadnienia
- Zakres czasowy/segmenty vs koszt i czas pozyskania.  
- Poziom agregacji vs granularność wymagana przez KPI.  
- Tolerancje DQ vs harmonogram analizy.
## Założenia
- Dostępne narzędzia DQ i katalog danych.  
- Dostęp do systemów źródłowych/wyciągów.  
- Wspólne definicje KPI/metryk obowiązują.
## Otwarte pytania
- Czy potrzebne są dodatkowe źródła zewnętrzne?  
- Czy istnieją ograniczenia prawne (jurysdykcje) dla wybranych danych?  
- Jakie są limity kosztów pozyskania/przetwarzania?
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
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Ścieżka akceptacji
- [Kto zatwierdza] → [kryteria akceptacji] → [status]
- [Kto zatwierdza] → [kryteria akceptacji] → [status]

## Kryteria ukończenia
- [ ] Wymagania governance opisane i powiązane z metrykami/procesami/narzędziami; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.
## Metryki jakości
- Coverage klasyfikacji, % systemów w katalogu/lineage, SLO jakości spełnione, czas zamykania incydentów danych, liczba waiverów i ich sunset, status audytów.
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
