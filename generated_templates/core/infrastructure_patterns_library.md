---
title: Infrastructure Patterns Library
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Infrastructure Patterns Library


## Metadane

- Właściciel: DevOps Engineer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Zbudować bibliotekę wzorców infrastrukturalnych (network/IaC/compute/storage/security/observability) ułatwiającą szybkie, spójne i bezpieczne wdrożenia.


## Zakres i granice

- Obejmuje: katalog patternów (VPC/VNet, subnety, security groups, ingress/egress, load balancer, bastion, storage, DB, cache, queue, CDN), warianty per chmura/on-prem, IaC moduły, guardrails, koszt i limity, checklisty NFR/security/compliance, wersjonowanie i deprecacje.
- Poza zakresem: szczegółowe wdrożenia aplikacji (osobne), nietypowe eksperymentalne architektury bez wsparcia.


## Użytkownicy i interesariusze

- [Rola] — [potrzeby/odpowiedzialności]
- [Rola] — [potrzeby/odpowiedzialności]


## Wejścia i wyjścia

- Wejścia: standardy bezpieczeństwa, katalog usług chmurowych, ADR, lessons learned, FinOps, compliance (CIS/FedRAMP/ISO), SLO.
- Wyjścia: karty patternów, moduły IaC, diagramy, checklisty wdrożeniowe, guardrails, znane ograniczenia, instrukcje użycia i wyjątków.


## Założenia
- Istnieje design system z komponentami.  
- Zespół ma dostęp do SR i narzędzi.  
- Polityki A11y obowiązują.
## Otwarte pytania
- Jakie lokalizacje/języki wymagają dodatkowych ARIA-label?  
- Jak często audytować DS pod kątem A11y?  
- Czy trzeba wspierać high-contrast mode?
## Powiązania (meta)

- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance


## Zależności dokumentu

Wskaż: standardy bezpieczeństwa/compliance, katalog usług, repo IaC, ADR, proces wyjątków/waiverów; brak – odnotuj.


## Fazy cyklu życia

Curacja → Opracowanie → Publikacja → Utrzymanie/przeglądy → Deprecacje.



## Struktura sekcji (szkielet)

- Cel/kontekst patternu.
- Diagram i warianty (cloud/on-prem).
- Komponenty i zależności.
- IaC moduły i instrukcje użycia.
- NFR/SLO i bezpieczeństwo (IAM, sieć, szyfrowanie, logi, backup, DR).
- FinOps/koszt (limity, skalowanie).
- Checklista wdrożeniowa i guardrails.
- Ograniczenia i wyjątki.
- Wersjonowanie i deprecacje.


## Szybkie powiązania

- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
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

- Wybierz pattern, użyj karty 1-stronicowej i modułów IaC; przejdź checklistę/guardrails; w razie odstępstw uruchom proces waiver.


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
- ARIA: Accessible Rich Internet Applications.  
- APG: Authoring Practices Guide.  
- Live region: obszar informujący SR o zmianach.
## Przykłady użycia
- Dodanie nowego komponentu modal w DS.  
- Audyt istniejących tabów/accordionów.  
- Naprawa błędów keyboard/focus zgłoszonych w audycie.
## Ryzyka i ograniczenia
- Nadmierne ARIA może pogorszyć UX SR.  
- Brak focus mgmt → pułapki klawiatury.  
- Brak testów SR → regresje niewidoczne.
## Decyzje i uzasadnienia
- Docelowe SR/przeglądarki do wsparcia.  
- Standard keybindings per komponent.  
- Poziom automatyzacji testów A11y.
## Powiązania z innymi dokumentami
- accessibility_compliance — standardy.  
- design_system_guidelines — komponenty.  
- testing_plan_accessibility — testy.
## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód]
- [Dokument Z → Sekcja W] — [powód]


## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów
- WCAG 2.1 AA, WAI-ARIA APG.  
- Wewnętrzne wytyczne A11y/DS.
## Mapa relacji sekcja→sekcja

- [Sekcja A] -> [Sekcja B] : [typ]
- [Sekcja C] -> [Sekcja D] : [typ]


## Mapa relacji dokument→dokument

- [Dokument A] -> [Dokument B] : [typ]
- [Dokument C] -> [Dokument D] : [typ]


## Ścieżki informacji

- [Wejście] → [Źródło] → [Rozwinięcie] → [Wyjście]
- [Wejście] → [Źródło] → [Streszczenie] → [Wyjście]


## Weryfikacja spójności

- [ ] Ścieżki informacji zamknięte
- [ ] Brak sprzecznych relacji
- [ ] Sekcje krytyczne mają źródła


## Lista kontrolna spójności relacji

- [ ] Relacje mają sekcje źródłowe
- [ ] Relacje nie są sprzeczne
- [ ] Cross-doc uzasadnione
- [ ] Rozwinięcia/streszczenia odnotowane


## Artefakty powiązane

- [Artefakt 1]
- [Artefakt 2]


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

Pattern → IaC → guardrails/checklisty; compliance → kontrolki; koszt → warianty.


## Wymagane rozwinięcia

- Checklista compliance → mapowanie do standardów (CIS, ISO, lokalne).
- IaC → repo i wersje modułów.


## Wymagane streszczenia

- Karta patternu 1 strona: kiedy użyć, diagram, guardrails, koszt.


## Guidance

Cel: bezpieczny reuse infrastruktury. DoR: standardy, katalog usług, repo IaC gotowe. DoD: karty/diagramy/IaC/checklisty/ograniczenia; sekcje N/A uzasadnione; metadane aktualne.


## Checklisty jakości (DoR/DoD skrót)

- DoR: [ ] Standardy bezpieczeństwa/compliance i katalog usług zebrane; [ ] Repo IaC dostępne; [ ] Właściciel patternu wskazany.
- DoD: [ ] Karty/diagramy/IaC/checklisty gotowe; [ ] Ograniczenia/waivery opisane; [ ] Sekcje N/A uzasadnione; metadane aktualne.

