---
title: Knowledge Article Publishing
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Knowledge Article Publishing


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Proces publikacji artykułów wiedzy (KB): tworzenie, review, publikacja, wersjonowanie, A11y i utrzymanie. Ma zapewnić spójność, aktualność i użyteczność treści dla użytkowników/internal/ external.


## Zakres i granice

- Obejmuje: szablony artykułów, kryteria publikacji, role (autor/reviewer/publisher), workflow (draft→review→publish→retire), tagging i wyszukiwalność, wersjonowanie/changelog, A11y i języki, grafika/media, linki i powiązania, feedback/oceny, metryki (views, deflection, CSAT), bezpieczeństwo/PII, archiwizacja i przeglądy okresowe.  
- Poza zakresem: pełny design portalu (oddzielne), polityka PR/marketing.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: źródła wiedzy (tickets/incydenty/FAQ), standardy style/terminologia, polityki bezpieczeństwa/PII, szablony, listy tagów/taxonomy, narzędzia CMS/KB.  
- Wyjścia: opublikowane artykuły, changelog, metryki i raporty, plan przeglądów, checklisty DoR/DoD, aktualizacje linkage_index.


## Założenia

- CMS/KB dostępny z wersjonowaniem.  
- Zespół ma reviewerów (tech, language, A11y).  
- Dane analityczne dostępne.


## Otwarte pytania

- Jak mierzyć search gaps?  
- Czy potrzebne są guideline’y dla wideo/podcastów?  
- Które artykuły wymagają zatwierdzenia prawnego/PR?


## Powiązania (meta)

- Key Documents: content_style_guide, incident_response_runbook, service_catalog, access_control_policy, localization_guidelines, accessibility_compliance.  
- Key Document Structures: szablony, workflow, wersjonowanie, tagging, metryki, przeglądy.  
- Document Dependencies: CMS/KB platform, search/index, analytics, review calendar, localization, A11y tools.


## Zależności dokumentu

Wymaga: szablonów i stylu, narzędzia CMS/KB, taksonomii/tagów, polityk PII/security, harmonogramu przeglądów, ról i uprawnień. Braki = DoR otwarte.


## Fazy cyklu życia

- Tworzenie i review.  
- Publikacja i lokalizacja.  
- Monitorowanie/feedback.  
- Przeglądy okresowe i archiwizacja.



## Struktura sekcji (szkielet)
- Cel, zakres i definicje sukcesu
- Trigger/scenariusze i preconditions
- Role, uprawnienia i narzędzia
- Kroki operacyjne (checklista) z walidacją
- Monitoring i dowody wykonania
- Rollback/contingency oraz komunikacja/escalacja
- Rejestr zmian runbooka
## Szybkie powiązania

- linkage_index.jsonl (knowledge/article/publishing)  
- content_style_guide, localization_guidelines, accessibility_compliance, incident_response_runbook


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)
- **ISO 20000-1** — System Zarządzania Usługami IT (SMS)
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

1. Twórz artykuł wg szablonu; oznacz tagi/lingo.  
2. Przeprowadź review (techniczne/język/A11y/PII); opublikuj w CMS.  
3. Monitoruj metryki/feedback; aktualizuj lub archiwizuj; DoR/DoD i linkage_index na bieżąco.


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

- Deflection: zmniejszenie ticketów dzięki artykułom.  
- Taxonomy: kontrolowany słownik tagów/kategorii.  
- WCAG: standard dostępności.


## Przykłady użycia

- Artykuł troubleshooting dla produktu SaaS.  
- FAQ dla nowej funkcji.  
- Release notes z linkami do API docs.


## Ryzyka i ograniczenia

- Nieaktualne artykuły → złe odpowiedzi, wzrost ticketów.  
- Brak A11y/lokalizacji → wykluczenie użytkowników.  
- PII w treści → ryzyko compliance.


## Decyzje i uzasadnienia

- Jakie typy artykułów są public vs internal.  
- Kadencja przeglądów (np. 90 dni).  
- Kto publikuje i kto odpowiada za metryki.


## Powiązania z innymi dokumentami

- content_style_guide — styl.  
- accessibility_compliance — A11y.  
- incident_response_runbook — wiedza krytyczna.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- WCAG, wewnętrzne wytyczne brand/styl, polityki PII/security.  
- Wytyczne lokalizacyjne dla języków/regionów.

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

## Powiązania sekcja↔sekcja

- Workflow → Role → Publikacja → Przeglądy.  
- Tagging → Wyszukiwalność → Deflection.  
- Feedback → Aktualizacje → Metryki.


## Struktura sekcji

1) Zakres i typy artykułów (how‑to, FAQ, troubleshooting, release notes)  
2) Role i workflow (autor/reviewer/publisher, SLA, checklisty)  
3) Szablony i styl (strukturę, tytuły, kroki, media, A11y)  
4) Tagging/taxonomy i linkowanie (powiązania, breadcrumbs)  
5) Wersjonowanie i changelog (draft→publish→retire, diff)  
6) Lokalizacja i A11y (języki, WCAG, alt text, captions)  
7) Publikacja i dostęp (uprawnienia, public/internal)  
8) Metryki i feedback (views, deflection, ratings, search gaps)  
9) Przeglądy okresowe i archiwizacja (kalendarz, właściciele)  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Szablon artykułu i checklisty publikacji.  
- Macierz ról/SLA dla review/publish.  
- Plan lokalizacji i A11y (alt text, captions).  
- Dashboard metryk i proces obsługi feedbacku.


## Wymagane streszczenia

- One‑pager: workflow publikacji + SLA + role.  
- Snapshot metryk: top artykuły, deflection, stare do przeglądu.


## Guidance (skrót)

- Używaj jednego szablonu i stylu; unikaj duplikatów.  
- Dodawaj alt text, transkrypcje, multi‑lang jeśli potrzebne.  
- Publikuj tylko po review i checkach PII/security.  
- Monitoruj search gaps i feedback; aktualizuj artykuły regularnie.  
- Planuj przeglądy (np. kwartalnie) i oznaczaj artykuły do archiwizacji.


## Checklisty Definition of Ready (DoR)

- [ ] Artykuł zgodny z szablonem; tagi/taxonomy dodane.  
- [ ] Źródła wiedzy i dowody poprawności zebrane.  
- [ ] Review ownerzy przypisani; terminy SLA ustalone.  
- [ ] Sprawdzenie PII/security/A11y/lokalizacja zaplanowane.  
- [ ] CMS dostępny; uprawnienia nadane.


## Checklisty Definition of Done (DoD)

- [ ] Artykuł opublikowany; wersja/data/status uzupełnione.  
- [ ] Review security/PII/A11y/lokalizacja zaliczone lub wyjątki opisane.  
- [ ] Linkage_index uzupełniony; metryki/feedback monitorowane.  
- [ ] Plan przeglądu okresowego ustawiony; stare wersje zarchiwizowane.  
- [ ] Ryzyka i decyzje udokumentowane.

