---
title: Security Controls Documentation
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Security Controls Documentation


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Udokumentować kontrolki bezpieczeństwa (techniczne i procesowe) z właścicielami, dowodami, przeglądami i statusem zgodności.


## Zakres i granice

- Obejmuje: listę kontrolek/klas, wymagania, właścicieli, dowody/testy, status, częstotliwość przeglądów i wyjątki.
- Poza zakresem: implementacja szczegółowa w kodzie/usługach (opisana w runbookach/IaC).


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Wejścia i wyjścia
- Wejścia: feedback użytkowników/support, analytics (search gaps, deflection), roadmapa produktu, wymagania compliance, zasoby docs, style guide, lokalizacja.  
- Wyjścia: lista celów i KPI, priorytety treści, plan publikacji/aktualizacji, mierniki i dashboard, DoR/DoD dla contentu.
## Założenia
- Analytics/feedback dostępne.  
- Zespół ma czas i zasoby.  
- Style guide istnieje.
## Otwarte pytania
- Jak mierzyć quality poza deflection (np. survey)?  
- Jak integrować feedback z produkt roadmap?  
- Jakie kanały publikacji priorytetowe (portal/PDF/SDK inline)?
## Powiązania (meta)
- Key Documents: content_style_guide, knowledge_article_publishing, api_design_standards, release_plan, accessibility_compliance.  
- Key Document Structures: audience, content types, goals/KPI, governance, tooling.  
- Document Dependencies: docs portal/CMS, analytics, review workflow, localization tooling.
## Zależności dokumentu
Wymaga: danych o potrzebach użytkowników i support, roadmapy produktu, zasobów zespołu, style guide, wymagań compliance/A11y. Braki = DoR otwarte.
## Fazy cyklu życia
- Ustalenie celów/KPI i priorytetów.  
- Publikacja/aktualizacje i pomiar.  
- Przeglądy okresowe i iteracje.
## Struktura sekcji (szkielet)

- Kontekst i zakres kontrolek
- Tabela kontrolek/klas → wymagania → dowody → właściciele → częstotliwość
- Status, luki i wyjątki
- Plan przeglądów/testów
- Raportowanie i utrzymanie dowodów


## Szybkie powiązania
- security-controls-reference
- security-controls-implementation
- security-controls-evaluation
- security-controls-rollout-plan
- vm-security-hardening

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

- Wpisz kontrolki i wymagania, dodaj dowody/właścicieli; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj status i wyjątki po przeglądach/testach.


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
- Deflection: redukcja ticketów dzięki docs.  
- Freshness: aktualność treści względem wersji produktu.  
- Time-to-first-success: czas do wykonania zadania z pomocą docs.
## Przykłady użycia
- Roadmapa docs dla nowego API.  
- Ustalenie priorytetów i KPI dla portal support.  
- Ocena jakości i deflection po wydaniu.
## Ryzyka i ograniczenia
- Brak ownerów → stara dokumentacja.  
- Brak metryk → nie wiadomo, czy docs pomagają.  
- Brak A11y/l10n → wykluczenie użytkowników.
## Decyzje i uzasadnienia
- Jakie KPI mierzyć i progi.  
- Kadencja review.  
- Zakres języków/A11y.
## Powiązania z innymi dokumentami
- knowledge_article_publishing — workflow.  
- content_style_guide — styl.  
- release_plan — harmonogram.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- Standardy A11y/l10n, polityki brand, wymagania compliance.
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

- Polityki/standardy/regulacje, compliance matrix.
- Mapa kontrolek/konfiguracji i architektura.
- Wymagania audytowe, incydenty/lessons learned.


## Wyjścia

- Katalog kontrolek z właścicielami/dowodami/statusami.
- Lista wyjątków i plan przeglądów/testów.
- Raport zgodności dla audytów/interesariuszy.



## Szybkie powiązania (uzupełnij)

- security_controls_implementation.md
- security_controls_evaluation.md
- security_compliance_matrix.md
- logging_and_audit_trail.md
- security_status_report.md
- risk_management_framework.md


## Wymagane rozwinięcia / streszczenia

- Tabela kontrolek (MD/CSV) i streszczenie luk/wyjątków.
- Streszczenie: krytyczne braki i plan działań.


## Wymagane powiązania

- Polityki, compliance matrix, audyty/testy, rejestr ryzyk, plan działań.


## Kryteria DoR

- [ ] Lista kontrolek/klas i wymagania zebrane.
- [ ] Właściciele i źródła dowodów znane.
- [ ] Częstotliwość przeglądów/testów uzgodniona.


## Kryteria DoD

- [ ] Katalog uzupełniony; dowody i statusy wpisane.
- [ ] Wyjątki/luki i plan działań dodane.
- [ ] Quick-links/checklisty zaktualizowane, metadane bieżące.


## Artefakty do załączenia

- Katalog kontrolek (MD/CSV/JSON).
- Dowody (logi, konfiguracje, raporty testów).
- Plan przeglądów/testów i lista wyjątków.


## Walidacja / testy

- Peer review przypisań kontrolka→wymaganie→dowód.
- Sanity świeżości dowodów i statusów.


## Metryki monitorowane

- % kontrolek green/amber/red.
- Liczba luk/wyjątków i ich wiek.
- Świeżość dowodów vs częstotliwość przeglądów.


## Utrzymanie i aktualizacje

- Przegląd cykliczny (np. kwartalny) lub po audytach/incydentach.
- Aktualizuj katalog po zmianach architektury/standardów.


## Zakończenie

Po spełnieniu DoD opublikuj katalog, podlinkuj artefakty, odhacz checklisty w `reports/checklist_atomic.jsonl` i przekaż status interesariuszom.
