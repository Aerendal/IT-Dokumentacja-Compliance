---
title: Procedury provisioning VM
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Procedury provisioning VM


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Standaryzować proces provisioning maszyn wirtualnych, aby zapewnić spójność, bezpieczeństwo, koszt i zgodność.


## Zakres i granice

- Obejmuje: szablony/obrazy bazowe, sieć/VPC/subnet, security groups/firewall, klucze/sekrety, tagging/CMDB, IaC/CI/CD, kontrole kosztowe, backup/DR, monitoring/logi, compliance (hardening/benchmarks).  
- Poza zakresem: provisioning bare-metal i kontenerów (oddzielne dokumenty).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: katalog flavorów/szablonów, polityki sieci/bezpieczeństwa, tagowanie/CMDB, wymagania aplikacji, limity kosztowe, IaC repo.  
- Wyjścia: checklisty provisioning, skrypty/IaC, zarejestrowane VM w CMDB, monitoring/backup włączone, linki w linkage_index.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: security_hardening_vm, logging_strategy, audit_logging, backup_and_disaster_recovery, cmdb_policy, change_management_policy.  
- Key Document Structures: obrazy/szablony, sieć/bezpieczeństwo, IaC/proces, koszt/backup/monitoring, compliance.  
- Document Dependencies: cloud/virtualization platform, secret manager, CMDB, monitoring/backup tools, IaC pipeline.



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

- linkage_index.jsonl (infra/provisioning_vm)  
- security_hardening_vm, logging_strategy, cmdb_policy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum

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

1. Wybierz szablon/obraz, zaplanuj sieć/SG/IAM; przygotuj IaC.  
2. Uruchom pipeline z tagami/CMDB, monitoring/backup; zweryfikuj compliance.  
3. Udokumentuj w linkage_index, odhacz checklisty DoR/DoD.


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

- [ ] Obraz/hardening zgodne; SG/IAM poprawne; tagi/CMDB i monitoring/backup aktywne.  
- [ ] IaC i policy-as-code enforce; drift detection działa; linkage_index uzupełniony.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- IaC skrypty, lista approved images, SG templates, tag policy, CMDB wpisy, backup/monitoring config, audit trail, ADR/waiver log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- % VM utworzonych przez IaC, % VM z monitoring/backup/tagami/CMDB, liczba driftów, czas provisioning vs cel, compliance pass rate.

## Kryteria ukończenia

- [ ] Standaryzacja provisioning VM wdrożona; każda nowa VM przechodzi checklisty; dokument powiązany w linkage_index.


## Struktura sekcji

1) Szablony/obrazy i konfiguracja bazowa (OS, agent, hardening baseline)  
2) Sieć i bezpieczeństwo (VPC/subnet, SG/firewall, mTLS, klucze/sekrety, IAM role)  
3) IaC/CI/CD i proces (repo, review, drift detection, approvals)  
4) Tagging/CMDB i koszt (tagi: owner/env/app/cost-center, limity, lifecycle)  
5) Backup/DR i monitoring (snapshots, restore tests, logi/metryki/trace, alerty)  
6) Compliance i testy (benchmarki CIS, skany, hardening, audit trail)  
7) Załączniki (checklisty, skrypty/IaC, ADR/waiver log)


## Wymagane rozwinięcia

- Lista approved images i hardening baseline; kto utrzymuje.  
- Standard security groups i zasady ruchu; rotacja kluczy/sekretów.  
- IaC pipeline: review/approvals, drift detection, policy-as-code.  
- Tagging/CMDB: wymagane pola, walidacja w CI.  
- Backup/DR: RPO/RTO, harmonogram snapshotów, test restore; monitoring/alerty obligatoryjne.


## Wymagane streszczenia

- Executive: stan standaryzacji VM (obrazy, SG, IaC), ryzyka (drift, brak backup/monitoringu), plan domknięcia luk.


## Guidance (skrót)

- Provisioning tylko przez IaC; żadnych ad‑hoc klików w prod.  
- Używaj approved images + hardening; taguj i rejestruj w CMDB.  
- Włącz monitoring/logi/backup w momencie tworzenia; enforce policy-as-code.  
- Aktualizuj linkage_index i checklisty po zmianach.


## Checklisty Definition of Ready (DoR)

- [ ] Approved images i polityki sieci/SG dostępne; tagi/CMDB wymagania znane.  
- [ ] IaC repo i pipeline działają; secret manager dostępny.


## Checklisty Definition of Done (DoD)

- [ ] VM utworzona IaC, z SG/IAM/kluczami, monitoring/backup/tagi/CMDB skonfigurowane; linkage_index zaktualizowany; status/metadane aktualne.  
- [ ] Compliance/hardening i test restore/monitoring potwierdzone; checklisty DoR/DoD odhaczone.

