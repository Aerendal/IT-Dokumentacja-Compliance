---
title: Harmonogram budowy bazy wiedzy
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Harmonogram budowy bazy wiedzy


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Plan utworzenia lub rozbudowy bazy wiedzy (KB): etapy, zadania, role, terminy, zależności, ryzyka, metryki postępu i kryteria publikacji.


## Zakres i granice

- Obejmuje: IA/projekt, szablony, migrację/kurację treści, review/QA, publikację, szkolenia i komunikację, metryki adopcji/feedback, utrzymanie.
- Poza zakresem: szczegółowa treść artykułów (linkowane), polityki korporacyjne (osobne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: decyzja o KB, narzędzie/portal, lista źródeł treści, właściciele domen, szablony, wytyczne stylu, plan komunikacji/szkoleń.
- Wyjścia: harmonogram etapów i zadań, IA i szablony, zkuracjonowana treść, publikacja/launch, plan utrzymania, metryki i raporty postępu.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: knowledge_base_strategy, content_governance, style_guide, template_library, migration_plan, communication_plan, training_plan, feedback_process.
- Key Document Structures: etapy, zadania, zależności, ryzyka, metryki, DoD.
- Document Dependencies: narzędzie KB, repo treści, autorzy/reviewerzy, analytics/feedback, ticketing.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery: doprecyzowanie problemu, warianty.
- Design: wybór wariantu, decyzje, model danych, integracje.
- Review: security/compliance/architecture board, koszty, performance.
- Implementation & Test: odbiór spełnienia projektu.
- Rollout & Ops: migracja, monitoring, zarządzanie zmianą.
## Struktura sekcji (szkielet)
1. IA: kategorie/sekcje, tagi, słownik pojęć.
2. Szablony artykułów: how-to, FAQ, runbook, decyzje.
3. Workflow: tworzenie, review, publikacja, przeglądy okresowe.
4. Jakość: język prosty, a11y, lokalizacje, multimedia.
5. Wersjonowanie/archiwizacja i deprecjacje.
6. Wyszukiwanie/SEO wewnętrzne, rekomendacje.
7. Observability: użycie, deflection, feedback.
## Szybkie powiązania

- linkage_index.jsonl (knowledge/kb_schedule)
- knowledge_base_strategy, content_governance, style_guide, template_library, migration_plan, communication_plan, training_plan, feedback_process


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **PRINCE2 7** — Projekty w Kontrolowanych Środowiskach
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania

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

1. Zdefiniuj etapy, IA, szablony i listę treści do migracji.  
2. Rozpisz zadania z owner/due/DoD; ustaw komunikację i szkolenia.  
3. Śledź metryki postępu/adopcji; aktualizuj harmonogram i linkage_index.


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

- [ ] Etapy/zadania i zależności spójne; DoD jasno określone.  
- [ ] Metryki adopcji/feedbacku mierzone; ryzyka/waivery odnotowane.  
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- IA mapa, szablony artykułów, lista treści, checklisty QA/A11y, dashboardy adopcji/feedbacku, plan komunikacji/szkoleń, log zmian.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % treści zmigrowanej, liczba wyszukań 0-result, CSAT/feedback, czas publikacji, aktualność artykułów (wiek), liczba przestarzałych/archiwizowanych wpisów.

## Kryteria ukończenia

- [ ] KB zbudowana/rozszerzona wg harmonogramu, QA/A11y spełnione, metryki monitorowane; dokument w linkage_index; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Etapy projektu KB (IA/projekt, szablony, migracja, review/QA, publikacja, szkolenia, utrzymanie)  
2) Zadania per etap (owner, due, priorytet, DoD, status)  
3) Zależności i ryzyka (źródła treści, autorzy, narzędzia, dostępności)  
4) Kryteria gotowości publikacji (DoR/DoD, QA treści, A11y, linki)  
5) Metryki postępu i adopcji (liczba artykułów, pokrycie tematów, wyszukiwania 0-result, CSAT/feedback, czas publikacji)  
6) Plan komunikacji i szkoleń (kto, kiedy, kanał, materiały)  
7) Utrzymanie i przeglądy (cadence, właściciele domen, archiwizacja)  
8) Załączniki (szablony artykułów, IA mapa, checklisty QA, log zmian)


## Wymagane rozwinięcia

- Tabela etapów/zadań z owner/due/DoD; kamienie milowe i zależności.  
- Szablony artykułów i wytyczne stylu; definicja IA/taxonomii/tagów.  
- Kryteria publikacji (QA, A11y, linki, aktualność); plan QA/peer review.  
- Metryki adopcji/feedback (dashboard) i cadence przeglądów/archiwizacji.


## Wymagane streszczenia

- Executive: status etapów, % treści zmigrowanej, top ryzyka/blokery, plan launch/szkoleń.


## Guidance (skrót)

- Ustal IA i szablony zanim zaczniesz migrację; bez tego chaos.  
- Priorytetyzuj treści o najwyższym użyciu i deficycie; zapewnij QA/A11y.  
- Mierz adopcję (wyszukania 0-result, CSAT) i poprawiaj na podstawie feedbacku.  
- Planuj utrzymanie/archiwizację – KB bez pielęgnacji szybko się starzeje.


## Checklisty Definition of Ready (DoR)

- [ ] IA/taxonomia i szablony uzgodnione; narzędzie KB wybrane.  
- [ ] Lista źródeł treści i ownerzy domen zidentyfikowani.  
- [ ] Plan QA/A11y i kryteria publikacji wstępnie spisane.


## Checklisty Definition of Done (DoD)

- [ ] Etapy/zadania zrealizowane; treści z QA/A11y opublikowane; metryki i dashboard działają.  
- [ ] Komunikacja/szkolenia przeprowadzone; utrzymanie/archiwizacja zaplanowane.  
- [ ] Dokument w linkage_index/checklistach; metadane aktualne.

