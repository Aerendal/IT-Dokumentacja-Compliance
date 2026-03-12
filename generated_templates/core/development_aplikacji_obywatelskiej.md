---
title: Development aplikacji obywatelskiej
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Development aplikacji obywatelskiej


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Opisać proces wytwarzania aplikacji dla obywateli: wymagania prawne (RODO), dostępność (WCAG), eID/podpis, bezpieczeństwo PII, release (store checklisty), observability i wsparcie.


## Zakres i granice

- Obejmuje: wymagania WCAG, RODO/priv, eID/podpis elektroniczny, język prosty, architekturę mobile/web, bezpieczeństwo PII (szyfrowanie, IAM, logging), development i testy (a11y/security/perf/UAT), release do store (Apple/Google) z privacy forms, staged rollout, observability, helpdesk/feedback, SLA.  
- Poza zakresem: polityka prywatności publiczna (osobny dokument), szczegółowe DPIA (oddzielne).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania prawne (RODO/eIDAS), WCAG, wytyczne UX języka prostego, architektura i stack, dane PII, checklisty store, narzędzia testowe a11y/security/perf, plan release/rollout.  
- Wyjścia: plan i artefakty dev/test/release, wyniki testów a11y/security/perf/UAT, privacy forms store, staged rollout plan, monitoring/alerty, plan wsparcia i feedbacku, log zgodności.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: privacy_policy, records_of_processing, data_privacy_assessment, security_requirements, wcag_level_requirements, accessibility_compliance, app_store_compliance_review, incident_response_runbook, monitoring_strategy_document, support_runbook.
- Key Document Structures: wymagania, architektura, testy, release/store, observability/support.
- Document Dependencies: IdP/eID, payment/signature APIs, logging/monitoring, test labs/device farm, helpdesk/ticketing, analytics/feedback.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (public_app/development)
- privacy_policy, records_of_processing, data_privacy_assessment, security_requirements, wcag_level_requirements, accessibility_compliance, app_store_compliance_review, incident_response_runbook, monitoring_strategy_document, support_runbook


## Mające zastosowanie standardy i normy


### Polskie normy i regulacje
- **CYBERSEC-STRATEGIA-PL** — Strategia Cyberbezpieczeństwa RP 2019-2024 (aktualizacja 2025+)
- **MC-INTEROP-PL** — Wytyczne Ministerstwa Cyfryzacji dot. interoperacyjności systemów publicznych
- **PZP-PL** — Prawo Zamówień Publicznych

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

1. Zbierz wymagania (RODO, WCAG, eID/podpis), architekturę i PII; zaplanuj testy.  
2. Opisz testy i release/store, monitoring i support; dodaj ryzyka/waivery.  
3. Po testach/release zaktualizuj wyniki, plan rollout, linkage_index i checklisty.


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

- [ ] Wymagania WCAG/RODO/eID spełnione z dowodami; testy mają wyniki i kryteria.  
- [ ] Store checklisty/polityki privacy uzupełnione; monitoring/support działa.  
- [ ] Dokument w linkage_index; relacje cross‑doc opisane.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Checklisty WCAG/store, wyniki testów, DPIA, privacy forms, release notes, plan rollout/rollback, monitoring/alerty, helpdesk runbook, waiver log, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Wyniki WCAG (A/AA), SLA testów security/perf, % pokrycia testów urządzeń, czas rollout/rollback, liczba incydentów PII, liczba waiverów i czas sunset, feedback/CSAT wsparcia.

## Kryteria ukończenia

- [ ] Aplikacja spełnia WCAG/RODO/eID, testy i release zrealizowane, monitoring/support aktywne; dokument w linkage_index; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Wymagania prawne i dostępności (RODO, eID/podpis, WCAG, język prosty)  
2) Architektura i stack (mobile/web, bezpieczeństwo PII, szyfrowanie, IAM/logging)  
3) Development i testy (a11y, security, perf, UAT, device farm)  
4) Release i stores (Apple/Google checklist, privacy forms, staged/canary rollout)  
5) Observability i wsparcie (monitoring, alerty, helpdesk/feedback, SLA)  
6) Ryzyka i plan mitigacji; waivery (sunset)  
7) Załączniki (checklisty store, wyniki testów, DPIA linki, runbooki supportu/incident)


## Wymagane rozwinięcia

- Checklisty WCAG/eID/podpis/RODO; tabela danych PII i zabezpieczeń.  
- Wyniki testów a11y/security/perf/UAT i kryteria go/conditional/no‑go.  
- Privacy forms i store metadata; plan staged rollout i rollback.  
- Monitoring/alerty/SLA i proces feedbacku/helpdesku.


## Wymagane streszczenia

- Executive: status WCAG/RODO/eID, wyniki testów, plan release/rollout, ryzyka.


## Guidance (skrót)

- Priorytet: dostępność i prywatność; testuj WCAG i security przed release.  
- Wymagaj eID/podpis tam, gdzie prawo; minimalizuj PII i loguj zgodnie z privacy.  
- Używaj staged/canary; zapewnij rollback i monitoring.  
- Jasny kanał feedbacku; SLA wsparcia i incident response powiązane.


## Checklisty Definition of Ready (DoR)

- [ ] Wymagania prawne/RODO, WCAG i eID/podpis zebrane; PII zidentyfikowana.  
- [ ] Checklisty store i narzędzia testowe dostępne; ownerzy sekcji wskazani.


## Checklisty Definition of Done (DoD)

- [ ] Testy a11y/security/perf/UAT wykonane; privacy forms/store metadata gotowe; staged rollout/rollback opisane.  
- [ ] Monitoring/alerty/support uruchomione; ryzyka/waivery z sunset; dokument w linkage_index; metadane aktualne.

