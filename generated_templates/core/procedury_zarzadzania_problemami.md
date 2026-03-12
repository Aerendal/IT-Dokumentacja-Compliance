---
title: Procedury zarządzania problemami
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Procedury zarządzania problemami


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Minimalizować wpływ powtarzalnych incydentów poprzez formalne zarządzanie problemami (Problem Management): identyfikacja, RCA, działania trwałe i KEDB.


## Zakres i granice

- Obejmuje: identyfikację trendów incydentów, rejestr problemów, diagnostykę/RCA, działania trwałe i Change Management, KEDB/workaroundy, przegląd i zamknięcie.  
- Poza zakresem: obsługa pojedynczych incydentów (incident_response_playbook), pełne CAB (oddzielne procedury).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: dane z incydentów (ticketing, alerty), raporty SRE/Support, metryki trendów, logi/trace, polityka change.  
- Wyjścia: rejestr problemów z priorytetami, RCA i hipotezami, plan działań trwałych/zmian, workaroundy w KEDB, metryki skuteczności, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: incident_response_playbook, logging_strategy, audit_logging, change_management_policy, service_incident_postmortem.  
- Key Document Structures: identyfikacja, rejestracja, diagnostyka/RCA, działania trwałe, KEDB, przegląd/zamknięcie.  
- Document Dependencies: ticketing, monitoring, CMDB, CAB/Change process, KEDB repo.



## Zależności dokumentu

- Konsumuje: [dokumenty wejściowe — co musi istnieć zanim ten dokument powstanie]
- Dostarcza do: [dokumenty wyjściowe — co korzysta z tego dokumentu]

## Fazy cyklu życia

- Faza 1: Koncepcja i Wizja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 2: Analiza Wymagań: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 3: Projekt / Design: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 4: Planowanie: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 5: Implementacja: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 6: Testowanie / QA: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 7: Bezpieczeństwo / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 8: Wdrożenie / Deployment: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 9: Operacje / Maintenance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
## Struktura sekcji (szkielet)
1. Polityka haseł: długość, złożoność, reuse, expiry (jeśli wymagane), MFA preferowane.
2. Przechowywanie: menedżery haseł, tajemnice w HSM/Secrets Manager, zakaz plaintext.
3. Zmiana/reset: self-service z weryfikacją, proces administracyjny, logowanie audytowe.
4. Kontrole uprzywilejowane: częstsza rotacja, konta serwisowe, klucze do systemów krytycznych.
5. Monitoring naruszeń: haveibeenpwned, detekcja reuse, alerty na nietypowe logowania.
6. Edukacja i zgodność: szkolenia, przypomnienia, testy phishingowe.
## Szybkie powiązania

- linkage_index.jsonl (operations/problem_management)  
- service_incident_postmortem, change_management_policy, logging_strategy


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Otwórz problem wg kryteriów; wypełnij rejestr.  
2. Wykonaj RCA i zaplanuj działania trwałe + workaroundy w KEDB.  
3. Śledź postęp, mierząc trend incydentów; zamknij po spełnieniu kryteriów.


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

- [ ] Problem ma ownera, RCA i działania trwałe; workaround w KEDB.  
- [ ] Powiązania z incydentami i change/CAB; metryki poprawy monitorowane.  
- [ ] Linkage_index i dokumentacja zaktualizowane.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Rejestr problemów, RCA dokumenty, KEDB wpisy, backlog zmian/CAB decyzje, raport trendów, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- Liczba otwartych problemów, czas do RCA, czas do działania trwałego, spadek incydentów powtarzalnych, liczba workaroundów w KEDB, % problemów zaktualizowanych on-time.

## Kryteria ukończenia

- [ ] Problem zamknięty: RCA znane, działania trwałe wdrożone/planowane, trend incydentów spada, dokument powiązany w linkage_index.


## Struktura sekcji

1) Identyfikacja i priorytety (trendowanie incydentów, SRE/Support sygnały, impact/urgency)  
2) Rejestracja problemu (opis, scope, właściciel, daty, priorytet)  
3) Diagnostyka i RCA (logi, 5xWhy, Ishikawa, hipotezy, potwierdzenie przyczyny)  
4) Działania trwałe i zmiany (kod/infra/proces, backlog, CAB)  
5) KEDB i workaroundy (powiązanie z incydentami, status, instrukcje)  
6) Przegląd i zamknięcie (walidacja efektów, metryki, aktualizacja dokumentacji, komunikacja)  
7) Załączniki (szablon wpisu problemu, KEDB entry, ADR/waiver log)


## Wymagane rozwinięcia

- Kryteria otwarcia problemu (np. 3 incydenty/30 dni, wysoki impact).  
- Szablon RCA i definicja root vs contributory.  
- Polityka działań trwałych: timebox, owner, status, kryteria sukcesu.  
- Format KEDB i linkowanie do incydentów; kto zatwierdza workaround.  
- Cadence przeglądów (np. tygodniowe/ miesięczne) i raport metryk.


## Wymagane streszczenia

- Executive: top problemy, status RCA/CAPA, trend incydentów, blokery i wymagane zmiany.


## Guidance (skrót)

- Wybieraj problemy na podstawie trendów i impactu; ogranicz liczbę otwartych.  
- Oddziel fact timeline od hipotez; RCA musi mieć dowody.  
- Workaround do KEDB szybko; fix trwały przez CAB/backlog z właścicielem.  
- Mierz efekt (spadek incydentów); aktualizuj linkage_index i dokumentację.


## Checklisty Definition of Ready (DoR)

- [ ] Trend/incydenty potwierdzone; owner problemu wyznaczony; dane (logi/metryki) dostępne.  
- [ ] Kryteria sukcesu i wstępny zakres działań trwałych ustalone.


## Checklisty Definition of Done (DoD)

- [ ] RCA udokumentowane; działania trwałe zaplanowane/wykonane; KEDB/workaroundy dodane; linkage_index uzupełniony; status/metadane aktualne.  
- [ ] Metryki pokazują poprawę lub są planowane kolejne działania; checklisty DoR/DoD odhaczone.

