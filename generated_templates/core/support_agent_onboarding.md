---
title: Support Agent Onboarding
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Support Agent Onboarding


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved
- Repo / moduł: [link]


## Cel dokumentu

Przygotować agenta wsparcia do pracy: narzędzia, procesy, SLA, ton komunikacji, bezpieczeństwo/prywatność i mierniki jakości.


## Zakres i granice

- Obejmuje: dostęp do narzędzi (ticket/chat/CRM), kanały i SLA, playbooki i makra, tone of voice, procedury weryfikacji tożsamości, PII/PCI/RODO, eskalacje, QA/ocena ticketów, raportowanie, szkolenia produktowe.
- Poza zakresem: szczegółowe runbooki techniczne (linkowane), polityki HR.


## Użytkownicy i interesariusze
- Support/Contact Center, Training, Security/Privacy, HR/IT, QA Program, Product.
## Wejścia i wyjścia
- Wejścia: profil uczestników, poziom wejściowy, narzędzia/laby, materiały referencyjne, mentorzy.
- Wyjścia: sylabus, materiały, harmonogram, plan ewaluacji (quiz/lab/egzamin), feedback i plan utrzymania.
## Założenia
- Systemy i materiały dostępne; mentorzy mają czas; polityki PII/security obowiązują.
## Otwarte pytania
- Jak długo monitorujemy KPI po starcie? 
- Czy wymagany re‑cert co rok?
## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Analiza potrzeb i profilu grupy.
- Projekt sylabusa i materiałów.
- Realizacja i wsparcie mentorskie.
- Ocena i follow-up (certyfikacja/mentoring).
## Struktura sekcji (szkielet)

- Narzędzia i dostęp
- SLA/kanały i procedury
- Tone of voice i makra/playbooki
- Bezpieczeństwo/prywatność (PII/PCI)
- Eskalacje i komunikacja
- QA i metryki jakości
- Zadania praktyczne i kryteria ukończenia


## Szybkie powiązania

- Support Strategy Vision, Knowledge Base, Security/Privacy, Incident/Escalation, Training/Product docs.


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

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
1. Zdefiniuj role/KPI; przygotuj dostępy i materiały.
2. Zaplanuj harmonogram szkoleń/shadowing; przypisz mentorów.
3. Certyfikuj; monitoruj KPI i feedback; raportuj postęp.
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
- AHT, CSAT, FCR, Adherence, PII, PCI.
## Przykłady użycia
- Onboarding nowej fali agentów: 2 tyg. szkolenia, shadowing 5 dni, certyfikacja, KPI monitorowane 30 dni.
## Ryzyka i ograniczenia
- Brak dostępu/sprzętu opóźnia start; brak PII szkolenia → ryzyko compliance; brak KPI/feedback → niska jakość.
## Decyzje i uzasadnienia

- [Decyzja 1 — uzasadnienie, alternatywy odrzucone, data]
- [Decyzja 2 — uzasadnienie, alternatywy odrzucone, data]

## Powiązania z innymi dokumentami
- Support Playbook, KB Guidelines, Security/PII Policy, QA Program, Training Materials, Access Mgmt.
## Powiązania z sekcjami innych dokumentów
- Access Mgmt → dostępy; QA Program → KPI; PII Policy → szkolenia.
## Słownik pojęć w dokumencie
- AHT, CSAT, FCR, Adherence, PII, PCI.
## Wymagane odwołania do standardów
- PII/PCI wytyczne, polityki bezpieczeństwa, regulacje branżowe jeśli dot.
## Mapa relacji sekcja→sekcja
- Dostępy/Szkolenia → Shadowing → Certyfikacja → KPI/Coaching.
## Mapa relacji dokument→dokument
- Onboarding Plan → Support Playbook/KB/PII/QA → KPI/Raporty.
## Ścieżki informacji
- Preboarding → Szkolenia → Shadowing → Certyfikacja → KPI/Feedback → Raport.
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
- Checklisty dostępu, materiały szkoleniowe, harmonogram, certyfikacja, raport KPI, feedback log.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji
- Support/Training → Security/Privacy → Product/QA → Owner sign‑off.
## Metryki jakości
- Czas do produktywności, zdawalność certyfikacji, AHT/CSAT/FCR po starcie, błędy PII, retencja po okresie próbnym.
## Kryteria ukończenia
- [ ] Onboarding przeprowadzony, KPI/feedback raportowane; dokument w linkage_index; wersja/data/właściciel aktualne.
## Wejścia

- Narzędzia support, SLA, baza wiedzy, polityki bezpieczeństwa/prywatności, lista eskalacji, materiały produktowe.


## Wyjścia

- Plan onboarding, checklisty dostępu i zadań, zadania praktyczne (ticket, chat), ton of voice guide.



## Jak używać (checklista)

- Zapewnij dostępy; przejdź szkolenie z narzędzi/SLA/ton of voice.
- Wykonaj zadania praktyczne; poznaj makra/playbooki i eskalacje.
- Zdaj QA/ticket review; potwierdź znajomość zasad PII/PCI.


## Wymagane rozwinięcia / powiązania

- Checklisty dostępu, makra/playbooki, tone guide, lista eskalacji, QA rubric.


## Kryteria DoR

- Dostępy i narzędzia gotowe; mentor przydzielony; SLA/playbooki dostępne.


## Kryteria DoD

- Zadania praktyczne zaliczone; QA review pozytywne; polityki PII/PCI potwierdzone.


## Artefakty

- Plan onboarding, checklisty, makra, QA rubric, log zadań.


## Walidacja

- QA ticketów; quiz z PII/PCI; feedback mentora.


## Metryki

- Czas do produktywności, QA score, błędy PII/PCI, satysfakcja nowych agentów.


## Utrzymanie

- Aktualizacja przy zmianie narzędzi/SLA/polityk; kwartalny przegląd makr/playbooków.


## Zakończenie

Onboarding agentów zapewnia spójne i bezpieczne wsparcie; utrzymuj go z QA i aktualnymi politykami.

