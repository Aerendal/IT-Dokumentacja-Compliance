---
title: Procedury reagowania na nieautoryzowany dostęp
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Procedury reagowania na nieautoryzowany dostęp


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zapewnić szybkie wykrycie, izolację i remediację incydentów nieautoryzowanego dostępu, z minimalizacją wpływu i spełnieniem wymogów prawnych.


## Zakres i granice

- Obejmuje: detekcję (SIEM/IAM/WAF/VPN), klasyfikację severity, izolację (konto/sesja/klucze/sieć), analizę (timeline, IOC, zasięg), remediację (rotacja sekretów, hardening, cleanup tokenów), komunikację i zgłoszenia (IR, właściciele systemów, użytkownicy, regulator), post-incident (postmortem, reguły/alerty, szkolenia, testy).  
- Poza zakresem: pełny playbook IR (incident_response_playbook) i specyficzne runbooki systemowe.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: alerty z SIEM/IAM/WAF/VPN, logi/trace, dane kont/kluczy, polityka klasyfikacji i zgłoszeń prawnych, CMDB systemów.  
- Wyjścia: decyzje izolacji, rotacje sekretów, lista IOC/zasięg, komunikaty (status page/klient/regulator), CAPA i aktualizacje reguł/alertów, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: incident_response_playbook, audit_logging, logging_strategy, design_bezpieczenstwa_api, obsluga_incydentow_rate_limit.  
- Key Document Structures: detekcja, izolacja, analiza, remediacja, komunikacja, post-incident.  
- Document Dependencies: SIEM, IAM/IdP, WAF/VPN, secret manager, ticketing, status page.


## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
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
- Cel, zakres i definicje sukcesu
- Trigger/scenariusze i preconditions
- Role, uprawnienia i narzędzia
- Kroki operacyjne (checklista) z walidacją
- Monitoring i dowody wykonania
- Rollback/contingency oraz komunikacja/escalacja
- Rejestr zmian runbooka
## Szybkie powiązania

- linkage_index.jsonl (security/unauthorized_access_response)  
- incident_response_playbook, audit_logging, logging_strategy


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

1. Po alercie wykonaj klasyfikację i izolację wg checklist.  
2. Zbierz logi/IOC, określ zasięg, wykonaj remediację i komunikację.  
3. Zakończ postmortem/CAPA, zaktualizuj reguły/alerty i linkage_index.


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

- [ ] SEV i klasyfikacja poprawne; izolacja adekwatna; dowody zachowane.  
- [ ] Remediacja/rotacje wykonane; komunikacja zgodna z polityką; zgłoszenia regulatora jeśli wymagane.  
- [ ] Reguły/alerty poprawione; linkage_index uzupełniony.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Logi/trace, decyzje izolacji, rotacje sekretów, IOC lista, komunikaty, raport postmortem, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- MTTR dla incydentów nieautoryzowanego dostępu, czas izolacji, % incydentów z poprawnym zgłoszeniem regulatora (gdy wymagane), % CAPA on-time, liczba powtórek tego samego wektora.

## Kryteria ukończenia

- [ ] Incydent nieautoryzowanego dostępu obsłużony zgodnie ze standardem; CAPA uruchomione; dokument powiązany w linkage_index.


## Struktura sekcji

1) Detekcja i klasyfikacja (źródła, sygnały, SEV, kogo powiadomić)  
2) Izolacja (konto/klucze/sesje/sieć, MFA reset, scope ograniczenie)  
3) Analiza (timeline, IOC, zasięg danych/systemów, korelacja zdarzeń)  
4) Remediacja (rotacja sekretów, patch/hardening, cleanup tokenów/session store)  
5) Komunikacja i zgłoszenia (IR team, właściciele systemów, użytkownicy, regulator/RODO jeśli dotyczy)  
6) Post-incident (postmortem, poprawki reguł/alertów, szkolenia, retest)  
7) Załączniki (checklisty, szablony komunikatów, ADR/waiver log)


## Wymagane rozwinięcia

- Matryca SEV i kanały powiadomień; warunki zgłoszenia regulatorowi.  
- Checklisty izolacji (konto/klucze/sieć) i rotacji sekretów; kto zatwierdza.  
- Lista minimalnych logów/artefaktów do zebrania; procedura dowodowa.  
- Szablony komunikacji (wewnętrzna, użytkownicy, regulator).  
- Plan testów reguł/alertów po incydencie.


## Wymagane streszczenia

- Executive: wpływ, root cause, wykonane izolacje/remediacje, zgłoszenia/regulator, główne CAPA i terminy.


## Guidance (skrót)

- Najpierw izoluj i zachowaj dowody; potem pełna analiza.  
- Rotuj sekrety szeroko jeśli zasięg niepewny; loguj wszystkie decyzje.  
- Sprawdzaj scope danych (PII) i wymogi prawne; używaj status page/PR gdy wymagane.  
- Po incydencie testuj reguły/alerty i szkol zespół; aktualizuj linkage_index.


## Checklisty Definition of Ready (DoR)

- [ ] Źródła alertów/logów dostępne; matryca SEV i kanały powiadomień znane.  
- [ ] Polityka zgłoszeń prawnych/RODO dostępna; kontakty IR/ownerów systemów aktualne.


## Checklisty Definition of Done (DoD)

- [ ] Izolacja/remediacja wykonane; zasięg/IOC opisane; komunikacja i zgłoszenia wykonane wg polityki; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] CAPA i test reguł/alertów zaplanowane/wykonane; checklisty DoR/DoD odhaczone.

