---
title: Dokumentacja definicji ról
status: needs_content
aligned: true
aligned_rev: 7
aligned_at: 2026-02-09
aligned_by: codex
---
# Dokumentacja definicji ról


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Udokumentować role w systemie/projekcie: zakres i odpowiedzialności, uprawnienia, ograniczenia SoD, proces nadawania/odbierania/recertyfikacji, integracje z IAM/IdP/SSO oraz audyt/logowanie zmian.


## Zakres i granice

- Obejmuje: lista ról i opisy, uprawnienia per rola (zasoby/akcje/poziomy), SoD, wyjątki/waivery, procesy JML/JIT/recertyfikacji, integracje z IdP/SSO/IAM, audyt/logi, raportowanie.
- Poza zakresem: szczegółowe testy AC (oddzielny dokument), polityki organizacyjne (linki).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: AC goals, data classification, SoD zasady, istniejące macierze ról, IdP/SSO/IAM, wymagania regulatora, logi audytu, systemy/zasoby w scope.
- Wyjścia: definicje ról, macierz ról→uprawnienia, lista SoD/wyjątków z sunset, procesy JML/JIT/recerts, wymagania audytu/logów, raporty ról.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: access_control_goals, access_control_matrix_design, access_control_matrix_reference, role_based_access_control_rbac_design, attribute_based_access_control_abac_design, access_control_patterns, access_control_testing, multi_factor_authentication_design, data_classification, security_controls_reference, risk_register.
- Key Document Structures: role, uprawnienia, SoD, procesy, audyt/testy.
- Document Dependencies: IdP/SSO/IAM, CMDB, HRIS (JML), ticketing, logging/audit.



## Zależności dokumentu
- Security/Access Policy.
- RACI w kluczowych dokumentach (plan projektu, operacje, bezpieczeństwo).
- Org chart / struktura zespołu.
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
1. Lista ról i cel każdej roli.
2. Zakres odpowiedzialności (co robi, czego nie robi).
3. Uprawnienia i dostęp (systemy, poziomy).
4. RACI (Responsible/Accountable/Consulted/Informed).
5. Luki i konflikty (co trzeba doprecyzować/zmienić).
## Szybkie powiązania

- linkage_index.jsonl (access/roles_definition)
- access_control_goals, access_control_matrix_design/reference, rbac_design, abac_design, access_control_patterns, access_control_testing, mfa_design, data_classification, security_controls_reference, risk_register


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

1. Zbuduj słownik ról i macierz ról→uprawnienia; podlinkuj repo CSV/JSON.  
2. Dodaj SoD/wyjątki, procesy JML/JIT/recerts, integracje, audyt/testy.  
3. Utrzymuj wersje i logi; zamknij DoR/DoD i linkage_index.


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
- **RACI** — macierz odpowiedzialności: kto wykonuje, kto zatwierdza, kogo konsultować, kogo informować.
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

- [ ] Role/uprawnienia/zasoby i SoD spójne; wyjątki mają sunset.  
- [ ] JML/JIT/recerts mają SLA i dowody; audyt/logi działają.  
- [ ] Testy AC pokrywają model; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Macierz ról (CSV/JSON), SoD rules, waiver log, workflow JML/JIT/recerts, raporty audytu/logów, testy AC, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % ról po recertyfikacji w terminie, liczba waiverów i czas sunset, liczba nadmiarowych uprawnień wykrytych, czas provision/deprovision, pokrycie testów AC.

## Kryteria ukończenia

- [ ] Role opisane, macierz i procesy AC udokumentowane; dokument w linkage_index; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Słownik ról (opis, odpowiedzialności, właściciel)  
2) Uprawnienia per rola (zasoby/akcje/poziomy), referencja macierzy (CSV/JSON)  
3) SoD i wyjątki/waivery (sunset/kompensacje)  
4) Procesy JML/JIT/recertyfikacji (SLA, approvals, dowody)  
5) Integracje z IdP/SSO/IAM/CMDB/HRIS  
6) Audyt/logowanie i raporty (zmiany ról, wyjątki, recertyfikacje)  
7) Testy AC i monitoring (API/UI/data; dane testowe)  
8) Załączniki (macierz, waiver log, raporty audytu, ADR)


## Wymagane rozwinięcia

- Pola minimalne roli (nazwa, opis, owner, zasoby, poziom, SoD tag).  
- Macierz ról→uprawnienia (repo CSV/JSON) i zasady wersjonowania/review.  
- SoD rules i procedura wyjątku/waiver z sunset; logowanie zmian ról.  
- Procesy JML/JIT/recerts z SLA i dowodami; raporty audytu i recerts.


## Wymagane streszczenia

- Executive: liczba ról, status recertyfikacji, SoD/wyjątki, top ryzyka.  
- One-pager: jak znaleźć rolę, macierz repo, proces JML/JIT, cadence recerts.


## Guidance (skrót)

- Każda rola ma ownera i opis; trzymaj macierz w repo z wersjonowaniem.  
- Oznaczaj SoD i wyjątki; każdy waiver ma sunset/kompensację.  
- Automatyzuj JML/JIT/recerts i loguj zmiany; testuj AC w CI/CD.


## Checklisty Definition of Ready (DoR)

- [ ] AC goals, SoD i klasyfikacja dostępne; istniejące role/macierze zebrane.  
- [ ] Ownerzy ról/systemów wskazani; narzędzia IdP/IAM/CMDB/HRIS gotowe.  
- [ ] Struktura sekcji wypełniona/N/A.


## Checklisty Definition of Done (DoD)

- [ ] Słownik ról i macierz ról→uprawnienia opublikowane; SoD/wyjątki opisane.  
- [ ] Procesy JML/JIT/recerts i audyt/logi zdefiniowane; testy AC opisane.  
- [ ] Waivery z sunset/kompensacją; dokument w linkage_index; metadane aktualne.

