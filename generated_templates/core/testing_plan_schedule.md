---
title: Testing Plan & Schedule
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Testing Plan & Schedule


## Metadane

- Właściciel: Project Manager
- Wersja: v0.3
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan i harmonogram testów (funkcjonalne, niefunkcjonalne, bezpieczeństwo, wydajność, a11y) dla release/projektu. Ma zapewnić pokrycie ryzyk, dostępność zasobów, zgodność z kryteriami go/conditional/no‑go i minimalizować defect leakage.


## Zakres i granice

- Obejmuje: typy testów (unit/int/e2e/UAT/security/perf/a11y), zakres i priorytety, środowiska, dane testowe, zasoby/role, harmonogram runów, wejścia/wyjścia, kryteria go/conditional/no‑go, raportowanie i metryki, zależności (build/feature flags), ryzyka i plan mitigacji.
- Poza zakresem: szczegółowe przypadki testowe (w repo), pełne plany perf/security (osobne dokumenty).


## Użytkownicy i interesariusze

- QA, PM/Release, Dev, Security/Perf, Product/Business.


## Wejścia i wyjścia

- Wejścia: wymagania, ryzyka, user stories/epiki, architektura, dane testowe, środowiska, SLA/SLO, plan release, dostępność zespołu, polityki bezpieczeństwa/zgodności.
- Wyjścia: kalendarz runów, przypisania ról, matryca pokrycia, plan danych, kryteria go/conditional/no‑go, raporty cyklu, lista ryzyk i blokad.


## Założenia

- Dostępne są środowiska, dane i narzędzia testowe; zespoły mają czas na runy.


## Otwarte pytania

- Jakie dodatkowe testy wymagane przez regulatorów/klientów?  
- Czy potrzebne testy prod-shadow / canary?


## Powiązania (meta)

- Key Documents: qa_strategy, test_data_preparation, release_plan, risk_management_plan, change_management, security_testing_plan, performance_testing_plan.
- Key Document Structures: zakres, zasoby, harmonogram, kryteria, raporty.
- Document Dependencies: CI/CD, środowiska, dane testowe, feature flags, monitoring/observability.


## Zależności dokumentu

Wymaga listy wymagań/historii, ryzyk, dostępnych środowisk, danych testowych, kalendarza release, zasobów QA/dev/sec/perf oraz kryteriów jakości. Bez tego DoR pozostaje otwarte.


## Fazy cyklu życia

- Planowanie: zakres, ryzyka, zasoby, harmonogram, dane, środowiska.
- Przygotowanie: test suites, dane, środowiska, narzędzia, kryteria go/conditional/no‑go.
- Wykonanie: runy (CI/CD, manual), raporty, defekty, retesty/regresja.
- Ocena: spełnienie kryteriów go/conditional/no‑go, decyzja release.
- Zamknięcie: retrospektywa, metryki, lekcje.


## Struktura sekcji (szkielet)
- Kontekst i cele
- Częstotliwość i scope
- Okna/środowiska
- Koordynacja z release
- Retest i SLA
- Ryzyka
## Szybkie powiązania

- linkage_index.jsonl (qa/testing_plan)
- qa_strategy, test_data_preparation, release_plan, risk_management_plan, change_management, security_testing_plan, performance_testing_plan


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

## Standardy i compliance
### Standardy międzynarodowe
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

## RACI i role

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie dokumentu | DEV / BA | PM | BA / ARCH | OPS / SM |
| Przegląd i zatwierdzenie | PM / BA | PM | Tech Lead | OPS |
| Aktualizacja | DEV / BA | PM | BA | OPS |
| Archiwizacja | OPS | PM | BA | SM |

## Jak używać dokumentu

1. Wypełnij zakres/ryzyka i typy testów.  
2. Przygotuj dane/środowiska i kalendarz runów; ustaw kryteria go/conditional/no‑go.  
3. W cyklu aktualizuj raporty i metryki; decyzje go/conditional/no‑go dokumentuj.  
4. Po cyklu dodaj retrospektywę i lekcje; zamknij DoR/DoD i linkage_index.


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

- Go/Conditional/No‑go, Defect leakage, Flakiness, Entry/Exit criteria.


## Przykłady użycia

- Release: smoke → regression → perf → security smoke → UAT; decyzja go/conditional/no‑go na podstawie kryteriów.  
- Hotfix: skrócony plan (smoke + targeted regression) z klarownym go/conditional/no‑go.


## Ryzyka i ograniczenia

- Brak gotowości środowisk/danych → poślizgi; niejasne kryteria go/conditional/no‑go → spory; flakiness maskuje defekty.


## Decyzje i uzasadnienia

- [Decyzja] Kolejność i zakres runów — uzasadnienie ryzyk i czasu.  
- [Decyzja] Kryteria go/conditional/no‑go — uzasadnienie SLA/ryzyk.


## Powiązania z innymi dokumentami

- QA Strategy, Test Data Preparation, Release Plan, Risk Mgmt Plan, Change Mgmt, Security/Perf Testing Plans.


## Powiązania z sekcjami innych dokumentów

- Test Data → dane/środowiska; Release Plan → harmonogram/go-no-go; Risk → priorytety.


## Słownik pojęć w dokumencie

- Go/Conditional/No‑go, Defect leakage, Flakiness, Entry/Exit criteria, Regression, Smoke.


## Wymagane odwołania do standardów

- Polityki QA, bezpieczeństwa i wydajności; wymagania klienta/regulatora jeśli dotyczy.


## Mapa relacji sekcja→sekcja

- Zakres/Ryzyka → Typy testów → Harmonogram → Runy → Raporty → Decyzje → Retro.


## Mapa relacji dokument→dokument

- Testing Plan → QA/Release/Risk → Change/Incident → Lessons Learned.


## Ścieżki informacji

- Wymagania/ryzyka → Plan → Runy → Raporty → Decyzje → Retro → Aktualizacja planu.


## Weryfikacja spójności

- [ ] Zakres/ryzyka spójne z typami testów i harmonogramem.  
- [ ] Kryteria go/conditional/no‑go jasne; raporty/metyki dostępne.  
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Każdy run ma cel, dane, środowisko, właściciela, kryteria i raport.  
- [ ] Każda decyzja go/conditional/no‑go ma uzasadnienie i wpis w change/release.  
- [ ] Relacje cross‑doc opisane z uzasadnieniem.


## Artefakty powiązane

- Harmonogram runów, raporty runów, metryki, defekt log, decyzje go/conditional/no‑go, retrospektywa.


## Ścieżka decyzji

- [Decyzja] → [Uzasadnienie] → [Konsekwencje] → [Właściciel] → [Data].


## Ścieżka akceptacji

- QA/PM → Security/Perf (jeśli dotyczy) → Product/Business → Release/CAB.


## Metryki jakości

- Pass rate, Defect leakage, Flake rate, Czas cyklu testów, MTTR defektów w cyklu, dotrzymanie harmonogramu.

## Kryteria ukończenia

- [ ] Plan wykonany; decyzje i raporty zapisane; retrospektywa z lekcjami.  
- [ ] Dokument w linkage_index/checklistach; wersja/data/właściciel aktualne.


## Powiązania sekcja↔sekcja

- Zakres/ryzyka → Typy testów → Harmonogram → Kryteria go/conditional/no‑go.
- Dane/środowiska → Wykonanie → Raporty.
- Ryzyka → Plan mitigacji → Retesty/regresja.


## Struktura sekcji

1) Zakres i ryzyka (co testujemy/nie, priorytety)  
2) Typy testów i pokrycie (unit/int/e2e/UAT/security/perf/a11y)  
3) Środowiska i dane testowe (konfiguracje, refresh, privacy)  
4) Zasoby i role (QA/dev/sec/perf/UAT, dyżury)  
5) Harmonogram runów (kalendarz, zależności build/flags)  
6) Kryteria go/conditional/no‑go oraz entry/exit dla faz  
7) Raportowanie i metryki (pass rate, defect leakage, flake, perf/security gates)  
8) Ryzyka i plan mitigacji  
9) Linki do repo/test suites/runbooków


## Wymagane rozwinięcia

- Matryca pokrycia vs ryzyka/ścieżki krytyczne.
- Kalendarz runów (daty/godziny, właściciele, środowiska) i okna na retesty.
- Kryteria go/conditional/no‑go oraz entry/exit dla faz.


## Wymagane streszczenia

- Zakres/ryzyka, główne runy + daty, kryteria go/conditional/no‑go, zasoby/środowiska.


## Guidance (skrót)

- Zacznij od ryzyk i ścieżek krytycznych; dopasuj typy testów i kolejność runów.  
- Zapewnij gotowość danych/środowisk przed startem; bez tego blokuj go/conditional/no‑go.  
- Ustal jasne kryteria go/conditional/no‑go i właścicieli decyzji; loguj decyzje.  
- Mierz metryki (pass rate, defect leakage, flake, perf/security) i raportuj regularnie.  
- Aktualizuj harmonogram po zmianach release/ryzyk; prowadź retrospektywy.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania/ryzyka zebrane; środowiska/dane gotowe lub plan na ich gotowość.
- [ ] Role/zasoby przypisane; harmonogram wstępny zbudowany.
- [ ] Kryteria go/conditional/no‑go wstępnie zdefiniowane; struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Runy wykonane; raporty i metryki dostępne; defekty/retesty obsłużone.
- [ ] Kryteria go/conditional/no‑go ocenione; decyzja i uzasadnienie zapisane.
- [ ] Retrospektywa i lekcje zapisane; dokument w linkage_index.
- [ ] Wersja/data/właściciel zaktualizowane.

