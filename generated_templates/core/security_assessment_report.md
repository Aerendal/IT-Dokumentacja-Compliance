---
title: Security Assessment Report
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Assessment Report


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Raport z oceny bezpieczeństwa: kontekst, metodologia, znaleziska, ryzyka, rekomendacje i plan działań.


## Zakres i granice

- Obejmuje: zakres ocenianego systemu, metodologię (testy/skany/przeglądy), wyniki i klasyfikację ryzyk, rekomendacje i action plan.
- Poza zakresem: implementacja poprawek, szczegółowe konfiguracje narzędzi (w załącznikach).


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Wejścia i wyjścia
- Wejścia: wyniki skanów/pentestów/bounty/SCA, zakres i metodologię, CMDB/asset, CVSS/kontekst, SLA, status ticketów.
- Wyjścia: raport exec/tech, lista podatności z właścicielami/ETA, rekomendacje, status retestu, metryki SLA/MTTR, log ograniczeń/false positives.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Key Documents: vulnerability_management_procedure, vulnerability_management_policy, patch_release_procedure, incident_response_plan, change_management, asset_inventory_cmdb, security_baseline.
- Dependencies: skanery/SCA, CMDB, ticketing, CVE/CVSS, SLA, change management.
## Zależności dokumentu
- Upstream: zakres i metodologia, dane asset/CMDB, wyniki skan/pentest/SCA/bounty, polityki SLA.
- Downstream: ticketing/remediacja, waivery, retest, raporty exec/audit, risk register.
- Zewnętrzne: CVE feeds, regulator/audytor (jeśli wymagane).
## Fazy cyklu życia
- Zakres/metodologia → wykonanie → analiza → raport → retest → zamknięcie/raport KPI.
## Struktura sekcji (szkielet)

- Streszczenie i zakres oceny
- Metodologia i narzędzia
- Znaleziska i klasyfikacja ryzyk
- Rekomendacje i plan działań
- Ryzyka resztkowe i akceptacje
- Podsumowanie zgodności (kontrolki/baseline)
- Załączniki (artefakty testów)


## Szybkie powiązania
- security-assessment
- vulnerability-assessment-report
- stream-security-assessment
- security-testing-report
- security-status-report

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

### Polskie normy i regulacje
- **CERT-PL-WYTYCZNE** — Wytyczne CERT Polska (CSIRT NASK) dot. cyberbezpieczeństwa
- **KSC-PL** — Ustawa o Krajowym Systemie Cyberbezpieczeństwa

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

- Wstaw zakres i metodologię, dodaj tabelę znalezisk i action plan; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.
- Podlinkuj artefakty testów i zaktualizuj status w rejestrach ryzyk/compliance.


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

- [Ryzyko 1 — prawdopodobieństwo, wpływ, sposób ograniczenia]
- [Ryzyko 2 — prawdopodobieństwo, wpływ, sposób ograniczenia]

## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami

- [Dokument A] — [typ relacji: wymaga/uzupełnia/zastępuje/jest-częścią] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- [Standard 1, np. ISO 27001 §A.5] — [sekcja lub wymaganie, którego dotyczy to odwołanie]
- [Standard 2] — [sekcja lub wymaganie]

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
- Raporty skan/pentest/SCA/bounty, tabela znalezisk, ticket log, waiver log, retest evidence, KPI dashboard, ADR log.
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

- Plan/zakres oceny, wymagania/kontrolki.
- Wyniki testów/skanów/pentestów, przeglądy konfiguracji i kodu.
- Rejestr ryzyk, wcześniejsze raporty, architektura/DFD.


## Wyjścia

- Executive summary i rekomendacja go/no‑go (jeśli releasowa).
- Lista znalezisk z priorytetem i właścicielem.
- Plan działań i terminy; status zgodności z kontrolkami.



## Szybkie powiązania (uzupełnij)

- security_assessment_for_solution.md
- security_assessment_results.md
- security_audit.md
- security_compliance_matrix.md
- security_status_report.md
- risk_management_framework.md


## Wymagane rozwinięcia / streszczenia

- Tabela znalezisk (ID, opis, impact/likelihood/CVSS, właściciel, termin, status).
- Streszczenie executive: top 3 ryzyka, główne rekomendacje, wymagane decyzje.


## Wymagane powiązania

- Rejestr ryzyk, compliance matrix, backlog defektów.
- Artefakty testów/skanów i ich konfiguracje.


## Kryteria DoR

- [ ] Zakres i metodologię potwierdzono.
- [ ] Dane z testów/skanów kompletne.
- [ ] Właściciele oceny i odbiorcy ustaleni.


## Kryteria DoD

- [ ] Znaleziska sklasyfikowane i opisane.
- [ ] Plan działań z właścicielami/terminami wpisany.
- [ ] Status zgodności i ryzyka resztkowe podane.
- [ ] Quick-links/checklisty zaktualizowane, metadane bieżące.


## Artefakty do załączenia

- Raporty narzędzi (scan/pentest/review), logi, zrzuty.
- Tabela znalezisk i action log.
- Diagramy/DFD jeśli użyte.


## Walidacja / testy

- Peer review raportu; sanity danych/FP.
- Potwierdzenie reproducji kluczowych znalezisk.


## Metryki monitorowane

- Liczba/luka Critical/High/Med/Low; % zamkniętych w SLA.
- Czas od raportu do akceptacji/naprawy.
- Pokrycie kontrolkami/baseline.


## Utrzymanie i aktualizacje

- Aktualizuj po każdej iteracji testów lub releasie.
- Zsynchronizuj zmiany z rejestrem ryzyk i matrycą zgodności.


## Zakończenie

Po spełnieniu DoD opublikuj raport, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i przekaż właścicielom plan działań.
