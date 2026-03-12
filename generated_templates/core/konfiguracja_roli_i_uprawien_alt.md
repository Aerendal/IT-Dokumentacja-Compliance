---
title: Konfiguracja ról i uprawnień
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Konfiguracja ról i uprawnień


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Alias głównego szablonu konfiguracji ról/uprawnień. Opisuje model RBAC/ABAC, mapowanie ról na uprawnienia/zasoby/polityki, wyjątki/waivery, proces nadawania/odbierania i recertyfikacji, integrację z katalogiem/SSO, audyt/logowanie, zgodne z zasadą najmniejszych uprawnień.


## Zakres i granice

- Obejmuje: model ról (RBAC/ABAC), słownik ról, separację obowiązków (SoD), mapowanie ról→uprawnienia→zasoby, wyjątki/waivery (sunset), procesy JML/JIT, recertyfikacje, integracje z IdP/SSO/IAM/CMDB, logowanie/audyt, monitoring i testy AC.
- Poza zakresem: szczegółowe implementacje per aplikacja (linki do planów/testów AC).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: AC goals, data classification, SoD zasady, istniejące macierze ról, IdP/SSO/CMDB, wymagania regulatora, listy systemów/zasobów, raporty audytu.
- Wyjścia: model ról/atrybutów, macierz ról→uprawnienia, wyjątki/waivery z sunset, procesy JML/JIT/recertyfikacji, integracje IdP/SSO, wymagania audytu/logów, testy AC, RACI i harmonogram przeglądów.


## Założenia

- IdP/IAM/CMDB/HRIS dostępne; zespoły Security/IAM mają zasoby; polityki AC/SoD obowiązują.


## Otwarte pytania

- Jakie systemy wymagają bardziej granularnych ról/atrybutów?  
- Jakie raporty audytu są wymagane przez regulatora/klientów?


## Powiązania (meta)

- Key Documents: access_control_goals, access_control_matrix_design, access_control_matrix_reference, role_based_access_control_rbac_design, attribute_based_access_control_abac_design, access_control_patterns, access_control_testing, multi_factor_authentication_design, data_classification, security_controls_reference, risk_register.
- Key Document Structures: model ról/atrybutów, macierz, SoD, procesy JML/JIT/recerts, audyt/testy.
- Document Dependencies: IdP/SSO/IAM, CMDB, HRIS (JML), ticketing, logging/audit, test data (maskowane).


## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia

- Definicja modelu i macierzy.
- Implementacja w IdP/SSO/IAM i systemach.
- Operacje (JML/JIT), recertyfikacje, audyt/testy.
- Przeglądy i doskonalenie.


## Struktura sekcji (szkielet)
- Cel i zakres wdrożenia
- Środowiska i okna wdrożeniowe
- Architektura docelowa i przepływy danych
- Kroki/migracja (pilot → produkcja)
- Plan testów i kryteria go/no-go
- Monitoring/observability i runbooki
- Rollback/contingency i komunikacja
- Ryzyka, zależności, RACI
## Szybkie powiązania

- linkage_index.jsonl (access/roles_alt)
- access_control_goals, access_control_matrix_design/reference, role_based_access_control_rbac_design, attribute_based_access_control_abac_design, access_control_patterns, access_control_testing, multi_factor_authentication_design, data_classification, security_controls_reference, risk_register


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

1. Ustal model i SoD; zbuduj macierz w repo (CSV/JSON) i podlinkuj.  
2. Opisz procesy JML/JIT, recertyfikacje, wyjątki/waivery; skonfiguruj integracje IdP/SSO.  
3. Dodaj audyt/logowanie i testy AC; zamknij DoR/DoD i linkage_index.


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

- [Termin 1] — [definicja robocza i źródło]
- [Termin 2] — [definicja robocza i źródło]

## Przykłady użycia

- [Przykład 1 — krótki opis sytuacji i zastosowania tego dokumentu]
- [Przykład 2 — krótki opis sytuacji i zastosowania tego dokumentu]

## Ryzyka i ograniczenia

- Nadmiarowe uprawnienia, brak SoD, brak recerts/logów → ryzyko audytowe; brak waiver sunset → dług bezpieczeństwa.


## Decyzje i uzasadnienia

- [Decyzja] Model (RBAC/ABAC/hybryda) i repo macierzy; [Decyzja] Cadence recertyfikacji; [Decyzja] Waivery/sunset; [Decyzja] Integracje IdP/IAM/CMDB.


## Powiązania z innymi dokumentami

- access_control_goals, access_control_matrix_design/reference, role_based_access_control_rbac_design, attribute_based_access_control_abac_design, access_control_patterns, access_control_testing, multi_factor_authentication_design, data_classification, security_controls_reference, risk_register.


## Powiązania z sekcjami innych dokumentów

- Data classification → SoD i uprawnienia; IAM/MFA → integracje; Risk Register → wpisy ryzyka; AC Testing → walidacja macierzy.


## Słownik pojęć w dokumencie

- RBAC, ABAC, SoD, JML, JIT, Recertyfikacja, Waiver, Sunset, IdP, IAM.


## Wymagane odwołania do standardów

- Polityki AC/IAM/SoD organizacji; wymogi audytowe/regulatora (SOX/ISO/PCI itp., jeśli dotyczy).


## Mapa relacji sekcja→sekcja

- Model/SoD → Macierz → JML/JIT → Recertyfikacje → Audyt/testy → Waivery.


## Mapa relacji dokument→dokument

- Konfiguracja ról i uprawnień ↔ AC goals/matrix/RBAC/ABAC/testing/MFA/risk_register.


## Ścieżki informacji

- SoD/klasyfikacja → Macierz → Provisioning → Recertyfikacje → Audyt/testy → Waivery → Aktualizacje.


## Weryfikacja spójności

- [ ] Role/uprawnienia/zasoby i SoD spójne; wyjątki mają sunset.  
- [ ] JML/JIT/recerts mają SLA i dowody; audyt/logi działają.  
- [ ] Testy AC pokrywają model; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Macierz CSV/JSON, SoD rules, waiver log, workflow JML/JIT/recerts, raporty audytu/logów, testy AC, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % ról po recertyfikacji w terminie, liczba waiverów i czas sunset, pokrycie testów AC, liczba nadmiarowych uprawnień wykrytych, czas provision/deprovision.

## Kryteria ukończenia

- [ ] Macierz i procesy AC opisane; testy/audyt/waivery zdefiniowane; dokument w linkage_index; metadane aktualne.


## Powiązania sekcja↔sekcja

- Model ról/SoD → Macierz → JML/JIT → Recertyfikacje → Audyt/testy → Waivery.


## Struktura sekcji

1) Streszczenie (zakres, systemy, ryzyka, SoD)  
2) Model RBAC/ABAC i słownik ról/atrybutów  
3) Macierz ról→uprawnienia→zasoby (format CSV/JSON, repo)  
4) Separacja obowiązków (SoD) i wyjątki/waivery (sunset/kompensacje)  
5) Procesy JML/JIT (provision/deprovision, approvals, SLA, auditing)  
6) Recertyfikacje (cadence, scope, dowody, narzędzia)  
7) Integracje (IdP/SSO/IAM/CMDB/HRIS, MFA, logging)  
8) Audyt/logowanie i monitoring (śledzenie zmian, alerty)  
9) Testy kontroli dostępu (API/UI/data), dane testowe, automatyzacja  
10) Załączniki (macierz CSV/JSON, waiver log, runbooki, ADR)


## Wymagane rozwinięcia

- Format i repo macierzy; minimalne pola (rola, zasób, uprawnienie, system, SoD tag, owner).  
- Zasady SoD i lista par zakazanych; procedura wyjątku/waiver z sunset.  
- Kroki JML/JIT i SLA; recertyfikacja (kto, kiedy, dowody).  
- Integracje IdP/SSO/IAM i logowanie zmian (kto/co/kiedy/skąd).  
- Zestaw testów AC (API/UI/data) i metryki coverage/KPI.


## Wymagane streszczenia

- Executive: model, top ryzyka/SoD, status macierzy i recertyfikacji, wyjątki/waivery.  
- One-pager: macierz repo, proces JML/JIT, cadence recerts, audyt/logging.


## Guidance (skrót)

- Zacznij od SoD i danych krytycznych; trzymaj macierz w repo z wersjonowaniem.  
- Każda rola ma ownera; każdy wyjątek ma sunset/kompensację.  
- Automatyzuj JML/JIT i recertyfikacje; loguj zmiany i testuj w CI/CD.  
- Regularnie przeglądaj role „zbyt szerokie” i łącz to z risk register.


## Checklisty Definition of Ready (DoR)

- [ ] AC goals, SoD, klasyfikacja danych i istniejące macierze dostępne.  
- [ ] Ownerzy ról/systemów wskazani; narzędzia IdP/IAM/CMDB/HRIS gotowe.  
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Macierz opublikowana (CSV/JSON/repo); SoD/wyjątki opisane; JML/JIT/recerts udokumentowane.  
- [ ] Audyt/logowanie i testy AC zdefiniowane; waivery z sunset/kompensacją.  
- [ ] Dokument w linkage_index/checklistach; wersja/data/właściciel aktualne.

