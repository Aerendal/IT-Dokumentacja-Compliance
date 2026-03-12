---
title: Enterprise Architecture Maturity Assessment
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Enterprise Architecture Maturity Assessment


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Ocena dojrzałości architektury korporacyjnej (EA) w kluczowych obszarach: strategia, governance, standardy, portfolio aplikacji, dane, integracje, bezpieczeństwo, chmura/on‑prem, procesy i metryki. Ma wskazać luki i priorytety działań usprawniających.


## Zakres i granice

- Obejmuje: model dojrzałości (poziomy), domeny oceny (biznes/IT/data/security/integration/cloud/ops), kryteria i wskaźniki, metodę zbierania dowodów, scoring, wnioski i roadmapę inicjatyw.
- Poza zakresem: szczegółowe projekty transformacyjne (wynik oceny), audyty zgodności pojedynczych systemów (linkowane).


## Użytkownicy i interesariusze

- Enterprise Architecture, IT Strategy, Security, Data, Business/Exec, Audit.


## Wejścia i wyjścia

- Wejścia: strategia IT/biznes, katalog aplikacji i integracji, standardy/zasady EA, procesy governance, metryki (koszt, zwinność, niezawodność), wyniki audytów, raporty bezpieczeństwa/compliance, dane finansowe/FinOps.
- Wyjścia: raport oceny z poziomami dojrzałości per domena, luki i ryzyka, rekomendacje i roadmapa, KPI/KRI monitorujące postęp, lista dowodów.


## Założenia

- Dostępność ownerów; aktualne artefakty EA; wsparcie kierownictwa.


## Otwarte pytania

- Jakie częstotliwości przeglądów (roczna/kwartalna)? 
- Czy uwzględniamy oceny zewnętrzne/certyfikacje?


## Powiązania (meta)

- Key Documents: ea_principles, target_architecture, technology_standards, security_baseline, data_strategy, integration_strategy, cloud_strategy, portfolio_rationalization, finops_policy.
- Key Document Structures: model dojrzałości, kryteria, scoring, rekomendacje, roadmapa.
- Document Dependencies: katalog aplikacji/integracji, CMDB, metryki finansowe/operacyjne, audyty, procesy governance.


## Zależności dokumentu

Wymaga: przyjętego modelu dojrzałości i kryteriów, aktualnych katalogów systemów/integracji, standardów EA, metryk finansowych/operacyjnych, wyników audytów. Bez tego DoR otwarte.


## Fazy cyklu życia

- Przygotowanie: model, kryteria, źródła danych, plan warsztatów/interview.
- Ocena: zbieranie dowodów, scoring per domena, walidacja z właścicielami.
- Raport: luki, rekomendacje, roadmapa, KPI/KRI.
- Monitorowanie: cykliczny przegląd postępu, update roadmapy.


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
## Szybkie powiązania

- linkage_index.jsonl (ea/maturity)
- ea_principles, target_architecture, technology_standards, security_baseline, data_strategy, integration_strategy, cloud_strategy, portfolio_rationalization, finops_policy


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

## Standardy i compliance
### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

## RACI i role

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie dokumentu | DEV / BA | PM | BA / ARCH | OPS / SM |
| Przegląd i zatwierdzenie | PM / BA | PM | Tech Lead | OPS |
| Aktualizacja | DEV / BA | PM | BA | OPS |
| Archiwizacja | OPS | PM | BA | SM |

## Jak używać dokumentu

1. Wybierz model i kryteria, zbierz dowody; wykonaj scoring.
2. Zidentyfikuj luki/ryzyka; przygotuj rekomendacje i roadmapę.
3. Zdefiniuj KPI/KRI postępu; ustal cykl przeglądów.
4. Zamknij DoR/DoD; wprowadź do linkage_index.


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

- EA Maturity, Scoring, Radar chart, KPI/KRI, Evidence.


## Przykłady użycia

- Ocena roczna EA: radar domen, luki w integracjach/security, roadmapa 3/6/12 m.
- Ocena przed migracją chmurową: dojrzałość cloud/security/data, rekomendacje i KPI.


## Ryzyka i ograniczenia

- Subiektywność scoringu; brak dowodów; brak buy‑in ownerów; zbyt duży zakres.


## Decyzje i uzasadnienia

- [Decyzja] Model i wagi domen — uzasadnienie celów strategii.
- [Decyzja] Priorytety rekomendacji — uzasadnienie ryzyk i wartości.


## Powiązania z innymi dokumentami

- EA Principles, Target Architecture, Technology Standards, Security/Data/Integration/Cloud Strategies, Portfolio Rationalization, FinOps Policy.


## Powiązania z sekcjami innych dokumentów

- Security Baseline → domena security; Data Strategy → domena danych; FinOps → koszty.


## Słownik pojęć w dokumencie

- EA Maturity, Scoring, Radar chart, KPI/KRI, Evidence.


## Wymagane odwołania do standardów

- Ramy EA (TOGAF/FEA/ArchiMate) jeśli stosowane; normy bezpieczeństwa/zgodności.


## Mapa relacji sekcja→sekcja

- Model/kryteria → Scoring → Luki → Rekomendacje → Roadmapa → KPI/KRI.


## Mapa relacji dokument→dokument

- EA Maturity → EA Principles/Strategies → Roadmap → Change/Portfolio Mgmt.


## Ścieżki informacji

- Dane/dowody → Scoring → Luki → Rekomendacje → Roadmapa → Monitoring postępu.


## Weryfikacja spójności

- [ ] Scoring poparty dowodami; luki/roadmapa spójne z wynikami.
- [ ] KPI/KRI mierzalne; relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każda domena ma kryteria, scoring, luki, rekomendacje, KPI.
- [ ] Każda rekomendacja ma priorytet, owner, termin.
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Karty oceny, radar chart, dowody (standardy, raporty), roadmapa, KPI/KRI dashboard.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- EA/IT Strategy → Security/Data → Exec/Audit → Owner sign‑off.


## Metryki jakości

- Pokrycie dowodów, czas oceny, liczba rekomendacji wdrożonych, postęp KPI/KRI w czasie.

## Kryteria ukończenia

- [ ] Ocena zakończona; roadmapa i KPI ustalone; dokument w linkage_index.
- [ ] Wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Model/kryteria → Scoring → Luki → Rekomendacje/Roadmapa → KPI postępu.
- Dowody → Scoring → Audit trail → Raport.


## Struktura sekcji

1) Model dojrzałości i poziomy (definicje)  
2) Domeny i kryteria oceny (biznes, aplikacje, dane, integracje, bezpieczeństwo, chmura/infra, operacje)  
3) Metoda zbierania dowodów (warsztaty, ankiety, artefakty)  
4) Scoring i wyniki (per domena, radar/karty)  
5) Luki i ryzyka (opis, wpływ)  
6) Rekomendacje i roadmapa (krótki/średni/długi termin, priorytet, owner)  
7) KPI/KRI postępu i mechanizm przeglądów  
8) Załączniki (dowody, ankiety, karty oceny)


## Wymagane rozwinięcia

- Opis poziomów dojrzałości i kryteriów scoringu; szablon karty oceny.
- Lista wymaganych dowodów per domena; metodologia warsztatów/ankiet.
- Rekomendacje/mapowanie na cele strategiczne i wartości (koszt/zwinność/ryzyko).


## Wymagane streszczenia

- Wyniki per domena, top 5 luk, top 5 rekomendacji i roadmapa z priorytetami.


## Guidance (skrót)

- Używaj prostego modelu (np. 1–5) i jasnych kryteriów; unikaj subiektywności.
- Zbieraj dowody z wielu źródeł (artefakty, metryki, interv); waliduj z ownerami.
- Rekomendacje wiąż z celami biznes/IT i KPI; planuj iteracyjnie.
- Prowadź audit trail: karty, dowody, daty, uczestnicy.


## Checklisty Definition of Ready (DoR)

- [ ] Model/kryteria uzgodnione; źródła danych/dowodów dostępne.
- [ ] Lista domen i ownerów zmapowana; plan warsztatów/ankiet gotowy.
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Scoring per domena, luki/ryzyka opisane; rekomendacje/roadmapa przygotowane.
- [ ] KPI/KRI postępu zdefiniowane; plan przeglądów ustalony.
- [ ] Evidence/audit trail dołączone; dokument w linkage_index.
- [ ] Wersja/data/właściciel zaktualizowane.

