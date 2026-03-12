---
title: Deployment Schedule
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Deployment Schedule


## Metadane

- Właściciel: Project Manager
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Harmonogram wdrożeń/releasów z oknami, zależnościami, blackoutami i komunikacją, aby zsynchronizować zespoły, zminimalizować ryzyko konfliktów i zapewnić zgodę change management.


## Zakres i granice

- Obejmuje: lista wydań (wersja, zakres, okno), zespoły/ownerzy, zależności między systemami, blackout/maintenance windows, kryteria go/conditional/no‑go, komunikację (kto/kiedy/kanał), ryzyka i plan mitigacji, punkty decyzyjne CAB.
- Poza zakresem: szczegółowe instrukcje wdrożeniowe (w planach deploy/runbookach), techniczne checklisty release (osobne dokumenty).


## Użytkownicy i interesariusze
- **Project Manager** — prowadzi projekt, raportuje status i zarządza ryzykami
- **Project Sponsor** — akceptuje kluczowe decyzje i zapewnia zasoby
- **Development Team** — realizuje zadania zgodnie z planem
- **Stakeholders / Interesariusze** — odbierają raportowanie i zgłaszają zmiany zakresu

## Wejścia i wyjścia

- Wejścia: release plan, backlog/zakres, zależności systemowe, kalendarz blackoutów, CAB/Change zasady, dostępność zespołów, ryzyka.
- Wyjścia: kalendarz wdrożeń, lista zależności/konfliktów, plan komunikacji, decyzje go/conditional/no‑go, action items i eskalacje.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: release_plan, change_management_plan, runbook_deployment, rollback_procedure, incident_response_plan, communication_plan, risk_register.
- Key Document Structures: release lista, okna, zależności, komunikacja, ryzyka/mitigacja.
- Document Dependencies: CI/CD pipeline, środowiska, CAB, monitoring/alerting, ticketing.



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Przygotowanie: cele, zakres, założenia.
- Planowanie: sekwencja prac, zasoby, daty.
- Realizacja: monitoring postępu, decyzje go/stop.
- Zamknięcie: retrospektywa, aktualizacja planów.
## Struktura sekcji (szkielet)
- Cel i definicja sukcesu (KPI)
- Zakres, założenia i ograniczenia
- Interesariusze i role/RACI
- Kamienie milowe i daty
- Plan fal/sprintów z deliverables
- Zależności i ryzyka oraz plan mitigacji
- Budżet/zasoby i obłożenie
- Plan komunikacji i raportowania
- Kryteria akceptacji/go-live i plan rewizji
## Szybkie powiązania

- linkage_index.jsonl (release/deployment_schedule)
- release_plan, change_management_plan, runbook_deployment, rollback_procedure, incident_response_plan, communication_plan, risk_register


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Wpisz wydania, okna i zależności/blackouty; przypisz ownerów/on-call.  
2. Ustal kryteria go/conditional/no‑go i komunikację; dodaj linki do runbooków/rollbacków.  
3. Aktualizuj po zmianach; synchronizuj z CAB/Change i linkage_index.


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

- [ ] Okna i zależności spójne; brak konfliktów z blackoutami.  
- [ ] Kryteria go/conditional/no‑go i on-call jasno opisane; komunikacja zaplanowana.  
- [ ] Relacje cross‑doc opisane; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Kalendarz wydań (iCal/CSV), matryca zależności, szablony komunikacji, tickety CAB/Change, runbook deploy/rollback, log decyzji, waiver log (jeśli wyjątki).


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Terminowość komunikacji, liczba konfliktów/kolizji unikniętych, % wydań z pełnym planem/rollbackiem, czas reakcji na eskalacje, liczba waiverów i czas ich sunset.

## Kryteria ukończenia

- [ ] Harmonogram aktualny, konflikty rozwiązane, komunikacja wysłana; dokument w linkage_index; metadane aktualne.


## Struktura sekcji

1) Lista wydań (wersja, zakres, data/okno, środowiska)  
2) Zespoły i właściciele (release lead, approvers, on-call)  
3) Zależności i blackouty (systemy, integracje, okna serwisowe)  
4) Kryteria go/conditional/no‑go i punkty decyzyjne (CAB)  
5) Plan komunikacji (kogo, kiedy, kanał, szablony)  
6) Ryzyka i plan mitigacji (owner, ETA)  
7) Action items i eskalacje  
8) Załączniki (linki do runbooków, rollbacków, ticketów, kalendarzy)


## Wymagane rozwinięcia

- Kalendarz (iCal/CSV) wydań; blackout/maintenance windows.  
- Matryca zależności (system→system); lista integracji wrażliwych.  
- Szablony komunikatów (przed/po deployu, incydent).  
- Punkty go/conditional/no‑go, wymogi CAB, kryteria wejścia/wyjścia.


## Wymagane streszczenia

- Executive: zbliżające się wydania, kluczowe zależności/blackouty, ryzyka i decyzje go/conditional/no‑go.


## Guidance (skrót)

- Planować z wyprzedzeniem; blokować blackouty w kalendarzu wspólnym.  
- Dla krytycznych zależności ustaw punkty synchronizacji i rollback plan.  
- Komunikuj z wyprzedzeniem do interesariuszy; używaj szablonów.  
- Każde wydanie powinno mieć jasne kryteria go/conditional/no‑go i on-call.


## Checklisty Definition of Ready (DoR)

- [ ] Release plan i zakres gotowe; kalendarz blackoutów znany.  
- [ ] Zależności i zespoły potwierdzone; on-call wyznaczony.  
- [ ] Kryteria go/conditional/no‑go wstępnie określone.


## Checklisty Definition of Done (DoD)

- [ ] Harmonogram opublikowany; zależności/blackouty uwzględnione; komunikacja wysłana.  
- [ ] Decyzje go/conditional/no‑go zapisane; action items/ryzyka z owner/ETA; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.

