---
title: 3D Modeling Training
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# 3D Modeling Training


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Opisać program szkoleniowy dla modelerów 3D (junior→mid→senior), obejmujący styl/art bible, workflow high/low/retopo, UV/texel density, mapy PBR, LOD, kolizje, eksport, QA, performance oraz narzędzia, tak aby zapewnić spójność jakości i efektywność produkcji.


## Zakres i granice

- Obejmuje: sylabus, cele kompetencyjne per poziom, ćwiczenia praktyczne, checklisty jakości, standardy pipeline’u (naming, skala, eksport), oceny (rubryki), mentoring i cadence przeglądów, onboarding do projektów.
- Poza zakresem: rig/animacja (oddzielne szkolenia), VFX, programowanie grafiki (oddzielne). 


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: Art Bible, 3D Asset/Model Design Spec, Graphics Vision/Architecture, materiał/shader guide, performance budgets, narzędzia (DCC, pluginy), przykładowe assety referencyjne.
- Wyjścia: sylabus, materiały szkoleniowe, zestaw ćwiczeń z oceną, checklisty DoR/DoD dla zadań szkoleniowych, raporty postępu, plan mentoringu.


## Założenia
- Narzędzia i logi dostępne.  
- Zespół akceptuje zasady wellbeing.  
- SLO/SLA są zdefiniowane.
## Otwarte pytania
- Jak obsłużyć różne strefy czasowe?  
- Jak mierzyć sukces (MTTR, customer impact)?  
- Czy potrzebny pageduty/inna platforma?
## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Jeżeli brak danych w bazie: wypisz znane zależności (Asset Spec, Model Creation, Graphics Vision/Architecture, QA checklists), wskaż właścicieli i wpływ na kolejność prac; gdy brak zależności – zapisz to wprost.


## Fazy cyklu życia

- Koncepcja i Wizja: zdefiniowanie celu programu, poziomów i metryk.
- Analiza Wymagań: mapowanie na potrzeby projektów/platform.
- Projekt/Design: budowa sylabusa, ćwiczeń, rubryk ocen.
- Planowanie: harmonogram cohort, mentorzy, cadence review.
- Implementacja: prowadzenie zajęć/ćwiczeń, feedback.
- Testowanie/QA: ocena ćwiczeń wg rubryk, checklista jakości.
- Bezpieczeństwo/Compliance: licencje narzędzi, polityki danych (jeśli sample z produkcji), dostęp.
- Wdrożenie: rollout do nowych zespołów/projektów.
- Operacje/Maintenance: aktualizacja programu, nowe techniki.
- Incident Management: korekty po regresjach jakości assetów.
- Monitoring/Observability: metryki progresu (czas, jakość, defekty), ankiety.
- Dokumentacja referencyjna: biblioteka przykładów i rozwiązań.
- Szkolenie/Onboarding: główny cel – onboarding i upskilling.
- Komunikacja stakeholders: raporty postępu do leadów/PM.
- Knowledge Management: repo materiałów, wersjonowanie.
- Postmortem: retro po każdej kohorcie.
- Budżetowanie/Cost: czas mentorów, licencje, laby.
- Vendor Management: jeśli używane kursy zewnętrzne.
- Governance/Compliance: zgodność z procesem jakości assetów.
- Decommission/Sunset: archiwizacja starego sylabusa.
- DR/BCP: backup materiałów szkoleniowych.
- Change Management: proces zatwierdzania zmian sylabusa.
- Capacity Planning: planowanie miejsc w kohorcie vs zapotrzebowanie projektów.



## Struktura sekcji (szkielet)

- Profil kompetencyjny per poziom: oczekiwane umiejętności, KPI jakości/czasu.
- Sylabus: moduły (styl, high/low, retopo, UV/TD, mapy, LOD, kolizje, eksport, QA).
- Ćwiczenia praktyczne: zestawy z kryteriami oceny, referencje jakości.
- Narzędzia i pipeline: DCC, pluginy, eksportery, naming, skala, repo assetów.
- Checklisty jakości: DoR/DoD dla zadań; QA check dla assetów.
- Mentoring i review: cadence, format feedbacku, rubryki.
- Ocena i certyfikacja: sposób zaliczenia, progi, re-try.
- Onboarding do projektów: mapowanie umiejętności na zadania produkcyjne.
- Plan utrzymania: aktualizacja programu, włączanie nowych technik.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

- Ustal profil kompetencji i KPI, zmapuj na moduły i ćwiczenia.
- Przygotuj materiały/asset referencyjne, narzędzia i checklisty QA.
- Przeprowadź kohortę, oceniaj wg rubryk, zamykaj DoR/DoD, aktualizuj program.


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
- MTTA/MTTR: Mean Time To Acknowledge/Resolve.  
- Alert fatigue: przeciążenie liczbą alertów.  
- Game day: ćwiczenie symulujące awarie.
## Przykłady użycia
- Szkolenie nowych SRE przed dołączeniem do rotacji.  
- Game day dla usługi krytycznej.  
- Retro po serii nocnych alertów.
## Ryzyka i ograniczenia
- Brak ćwiczeń → słaba reakcja.  
- Za dużo alertów → burnout/fatigue.  
- Nieaktualne runbooki → dłuższy MTTR.
## Decyzje i uzasadnienia
- Częstotliwość game day.  
- Limity alertów/osoba i rotacje.  
- Zakres uprawnień na dyżurach.
## Powiązania z innymi dokumentami
- escalation_procedure_design — ścieżki eskalacji.  
- communication_plan — komunikaty.  
- observability_plan — alerty.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania]
- [Dokument Z → Sekcja W] — [powód powiązania]


## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło]
- [Pojęcie 2] — [definicja i źródło]
- [Pojęcie 3] — [definicja i źródło]


## Wymagane odwołania do standardów
- Wewnętrzne polityki bezpieczeństwa i dostępu, PII.  
- Standardy SRE/ITIL jeśli przyjęte.
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


## Ścieżka akceptacji

1. Autor przygotowuje wersję roboczą i przeprowadza samorecenzję.
2. Recenzent techniczny (Tech Lead / BA) weryfikuje merytorycznie.
3. Właściciel procesu zatwierdza treść i zakres.
4. PM / Scrum Master aktualizuje metadata (wersja, data, status).
5. Dokument trafia do repozytorium i jest linkowany w Szybkie powiązania.

## Metryki jakości

- [Metryka 1, np. pokrycie testami] — [cel / próg minimalny]
- [Metryka 2, np. czas przeglądu] — [cel / próg minimalny]

## Kryteria ukończenia

- [ ] Kryterium 1 — [opis stanu ukończenia tej sekcji lub dokumentu]
- [ ] Kryterium 2 — [opis stanu ukończenia tej sekcji lub dokumentu]

## Powiązania sekcja↔sekcja

Określ, które sekcje rozwijają/streszczają inne (np. cele kompetencyjne → ćwiczenia; pipeline → checklisty QA; performance → LOD/UV/kolizje), podaj uzasadnienie.


## Wymagane rozwinięcia

- Sylabus → szczegóły ćwiczeń i rubryk.
- Checklisty QA → z „3D Model Creation/Design/Loading”.
- Narzędzia → specyfikacje DCC/pluginów.


## Wymagane streszczenia

- Tabela kompetencji per poziom + kryteria zaliczenia na 1 stronie.


## Guidance

Cel: zapewnić spójne, mierzalne szkolenie, które odzwierciedla pipeline produkcyjny.

- Cel dokumentu: 2–3 zdania o celu szkolenia i mierzalnym wyniku (jakość/czas/defekty).
- Zakres: moduły, poziomy, co wchodzi/nie wchodzi (np. brak rig/VFX).
- Wejścia: Art Bible, asset spec, narzędzia, KPI perf, przykłady referencyjne.
- Wyjścia: sylabus, ćwiczenia, checklisty, raporty postępu.
- Zależności: model creation/design/loading, graphics vision/architecture, QA checklists.
- Powiązania: cele → ćwiczenia → oceny; pipeline → checklisty; performance → LOD/UV.
- Struktura: logiczna; sekcje N/A uzasadnij.
- Fazy: gdzie projektujemy/aktualizujemy/oceniamy program.
- DoR: zebrane referencje, asset spec, KPI, mentorzy, narzędzia.
- DoD: sylabus + ćwiczenia + rubryki gotowe; checklisty DoR/DoD dla zadań; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR:
  - [ ] Art Bible i asset spec dostępne; KPI jakości/czasu ustalone.
  - [ ] Narzędzia/pluginy gotowe; mentorzy przydzieleni.
  - [ ] Ćwiczenia i rubryki naszkicowane; repo materiałów przygotowane.
- DoD:
  - [ ] Sylabus, ćwiczenia, rubryki i checklisty QA zatwierdzone; sekcje N/A uzasadnione.
  - [ ] Raport postępu i feedback zebrane; metadane aktualne.
  - [ ] Plan utrzymania/aktualizacji programu wpisany.

