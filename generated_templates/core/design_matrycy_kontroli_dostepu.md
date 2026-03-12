---
title: Design matrycy kontroli dostępu
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Design matrycy kontroli dostępu


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Stworzyć i utrzymać matrycę kontroli dostępu: role → uprawnienia → zasoby/akcje, z uwzględnieniem SoD, wyjątków/waiverów, procesów zmian i audytu.


## Zakres i granice

- Obejmuje: role, zasoby/systemy/moduły/dane, poziomy uprawnień (view/edit/admin/approve), SoD, wyjątki/waivery, proces aktualizacji (change control, przeglądy), audyt/logowanie zmian, repo macierzy (CSV/JSON).  
- Poza zakresem: projekt RBAC/ABAC na poziomie architektury (oddzielny dokument).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: AC goals, data classification, SoD zasady, listy systemów/zasobów, istniejące role/macierze, wymagania regulatora, logi audytu.  
- Wyjścia: macierz ról→uprawnień (repo), lista SoD/wyjątków z sunset, proces zmian/przeglądów, audyt/logowanie zmian, export dla audytu/klientów.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: access_control_goals, access_control_matrix_design/reference, rbac_design, abac_design, access_control_patterns, access_control_testing, konfiguracja_roli_i_uprawien_alt, dokumentacja_definicji_rol, logging_and_audit_trail, risk_register.
- Key Document Structures: role, zasoby, uprawnienia, SoD, wyjątki, procesy, audyt.
- Document Dependencies: IdP/SSO/IAM, CMDB, HRIS (JML), ticketing/change, logging/audit.



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
1. Model uprawnień (RBAC/ABAC) i zasady (least privilege, SoD).
2. Role/grupy i proces ich tworzenia/zmian.
3. Dostęp uprzywilejowany (PAM), just-in-time, break glass.
4. Audyt i recertyfikacja (przeglądy, logi, alerty).
5. Integracje z IdP/SSO i aplikacjami.
## Szybkie powiązania

- linkage_index.jsonl (access/matrix_design)
- access_control_goals, access_control_matrix_design/reference, rbac_design, abac_design, access_control_patterns, access_control_testing, konfiguracja_roli_i_uprawien_alt, dokumentacja_definicji_rol, logging_and_audit_trail, risk_register


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
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

1. Zbierz role/zasoby i zasady SoD; zbuduj macierz (CSV/JSON) i podlinkuj.  
2. Opisz poziomy, wyjątki/waivery, proces zmian/recerts, audyt/logi.  
3. Aktualizuj po zmianach; zamknij DoR/DoD i linkage_index.


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
- **SoD** — segregation of duties.
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

- [ ] Role/zasoby/uprawnienia kompletne; SoD i wyjątki opisane; repo aktualne.  
- [ ] Procesy change/recerts działają; logi/audyt spełniają wymagania; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Macierz CSV/JSON, SoD rules, waiver log, change/recert schedule, log zmian, audit trail, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % ról po recertyfikacji w terminie, liczba waiverów i czas sunset, czas provision/deprovision, liczba SoD violations, kompletność macierzy.

## Kryteria ukończenia

- [ ] Macierz i procesy AC opisane, audyt/logi działają; dokument w linkage_index; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Role i zasoby (systemy/moduły/dane) – macierz RACI/ACL, repo CSV/JSON  
2) Poziomy uprawnień (view/edit/admin/approve) i ograniczenia  
3) SoD i wyjątki/waivery (sunset/kompensacje, aprobata)  
4) Proces zmian/przeglądów (change control, cadence recerts, approvals)  
5) Audyt i logowanie (kto/co/kiedy/skąd, retencja, dostęp)  
6) Załączniki (macierz, SoD rules, waiver log, log zmian)


## Wymagane rozwinięcia

- Format macierzy i minimalne pola (rola, zasób, akcja, poziom, SoD tag, owner).  
- Zasady SoD i procedura wyjątków/waiverów z sunset; ścieżka aprobacji.  
- Proces change: kto zgłasza/approvuje, SLA, wersjonowanie, recertyfikacje.  
- Wymagania audytu/logów (retencja, dostęp, integracja z SIEM).


## Wymagane streszczenia

- Executive: status macierzy, SoD/wyjątki, nadchodzące recertyfikacje, top ryzyka.


## Guidance (skrót)

- Prowadź macierz w repo z wersjonowaniem; każda rola ma ownera.  
- SoD i wyjątki muszą być jawne; waiver zawsze z sunset/kompensacją.  
- Automatyzuj recertyfikacje i change flow; loguj wszystkie zmiany.


## Checklisty Definition of Ready (DoR)

- [ ] AC goals, SoD, klasyfikacja danych i lista systemów/zasobów dostępne.  
- [ ] Ownerzy ról/systemów wskazani; repo macierzy i format uzgodnione.


## Checklisty Definition of Done (DoD)

- [ ] Macierz opublikowana; SoD/wyjątki opisane; proces change/recerts i audyt/logi zdefiniowane.  
- [ ] Waivery z sunset; dokument w linkage_index; metadane aktualne.

