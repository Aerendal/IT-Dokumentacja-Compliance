---
title: Intent and Entity Design
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Intent and Entity Design


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Projektuje intenty i encje dla systemu NLU/chatbot/voice: słowniki, przykłady, reguły ekstrakcji, rozróżnienia kontekstowe, wersjonowanie i jakość. Ma zapewnić wysoką precyzję/recall i spójne doświadczenie użytkownika.


## Zakres i granice

- Obejmuje: katalog intentów, definicje encji (typy/wartości/sinonimy), przykłady treningowe, negatywne/konfuzje, kontekst/slot filling, polityki eskalacji, wersjonowanie datasetów/modeli, metryki jakości (precision/recall/F1, FAR/FRR), testy regresji, A/B, bezpieczeństwo/PII.  
- Poza zakresem: implementacja silnika dialogowego (osobny dokument), integracje backend (oddzielne API specs).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania produktowe, domena i słownictwo, logi konwersacji, dane anotacyjne, polityki PII/RODO, definicje KPI, zasady eskalacji, narzędzia anotacji i treningu.  
- Wyjścia: katalog intentów/encji, zestaw treningowy/valid/test, zasady anotacji, lista konfuzji, metryki jakości i cele, scenariusze testowe, plan rollout modeli i wersji.


## Założenia

- Dostępne narzędzia anotacji i model registry.  
- Logi konwersacji mogą być anonimizowane.  
- Zespół ma zasoby do cyklicznych testów regresji.


## Otwarte pytania

- Jakie języki/rynkowe warianty należy obsłużyć najpierw?  
- Jakie są ograniczenia prawne dla nagrań audio/tekstowych?  
- Jakie progi pewności użyć do auto vs eskalacja?


## Powiązania (meta)

- Key Documents: nlu_annotation_guidelines, model_training_plan, safety_and_abuse_policy, privacy_and_pii_handling, escalation_playbook, release_plan.  
- Key Document Structures: intenty, encje, przykłady, metryki, testy, wersje, bezpieczeństwo.  
- Document Dependencies: narzędzia anotacji, repo datasetów, model registry, CI/CD modeli, monitoring runtime.


## Zależności dokumentu

Wymaga: uzgodnionej listy intentów/encji, zasad anotacji, dostępu do logów/anotacji, polityk PII/safety, narzędzi treningowych i model registry. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja słownika i zasad anotacji.  
- Zbieranie/anotacja danych i trening.  
- Testy regresji/A-B, walidacja bezpieczeństwa/PII.  
- Rollout modeli i monitoring; aktualizacje iteracyjne.



## Struktura sekcji (szkielet)
- Streszczenie i cele biznesowe
- Zakres, założenia, ograniczenia
- Kontekst domenowy i interesariusze
- Wymagania funkcjonalne i niefunkcjonalne
- Architektura/komponenty i integracje
- Model danych i przepływy informacji
- Bezpieczeństwo, prywatność i compliance
- Plan wdrożenia/migracji i kryteria go/no-go
- Monitoring/operacje oraz ryzyka i mitigacje
- Decyzje i uzasadnienia, pytania otwarte
## Szybkie powiązania

- linkage_index.jsonl (intent/and/entity/design)  
- nlu_annotation_guidelines, model_training_plan, safety_and_abuse_policy, privacy_and_pii_handling, escalation_playbook


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

1. Zdefiniuj intenty/encje i zasady anotacji; przygotuj przykłady.  
2. Wytrenuj i przetestuj model; wypełnij metryki i konfuzje.  
3. Zrób rollout z promotion gates; monitoruj drift i feedback; aktualizuj DoR/DoD.


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

- FAR/FRR: False Accept/Reject Rate.  
- Confusion set: para intentów/encji najczęściej mylona.  
- Slot filling: uzupełnianie wymaganych pól kontekstu w dialogu.


## Przykłady użycia

- Chatbot obsługi zamówień (intenty: status, zwrot, zmiana adresu).  
- Voice bot call center (encje: numer klienta, data, adres).  
- Asystent wewnętrzny IT (intenty: reset hasła, dostęp, zgłoszenie incydentu).


## Ryzyka i ograniczenia

- Drift językowy lub sezonowy → spadek metryk.  
- PII w logach/anotacjach → ryzyko compliance.  
- Brak negatywnych przykładów → wysoki FAR.


## Decyzje i uzasadnienia

- Poziomy progów metryk dla produkcji vs beta.  
- Strategia fallback/escalation przy niskiej pewności.  
- Częstotliwość re‑train i refreshu słownika.


## Powiązania z innymi dokumentami

- nlu_annotation_guidelines — szczegóły anotacji.  
- model_training_plan — trening i promotion.  
- escalation_playbook — fallback/eskalacja.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- RODO/PII, polityki bezpieczeństwa danych i treści.  
- Wewnętrzne standardy NLU/ML i kontroli jakości.

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

- Intenty/encje → Przykłady/anotacje → Trening/testy → Metryki → Rollout.  
- PII/safety → Anotacja/dane → Monitoring produkcji.  
- Kontekst/sloty → Eskalacja → Doświadczenie użytkownika.


## Struktura sekcji

1) Kontekst i cele (KPI: precision/recall/F1, CSAT)  
2) Katalog intentów i encji (definicje, przykłady pozytywne/negatywne)  
3) Zasady anotacji i jakości danych (guidelines, PII, balans klas)  
4) Wersjonowanie danych/modeli i promotion gates  
5) Metryki i testy (offline/online, FAR/FRR, confusion sety)  
6) Kontekst i slot filling (obowiązkowe/opcjonalne, disambiguation)  
7) Eskalacja i fallback (do agenta/FAQ, safety)  
8) Bezpieczeństwo/PII i nadużycia (filtering, redaction, abuse)  
9) Rollout i monitoring runtime (drift, feedback loop)  
10) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Tabela intentów z opisem, przykładami, negatywnymi przykładami i powiązanymi encjami.  
- Lista encji z typami (enum/free text/regex/ML), sinonimy, wartości przykładowe.  
- Konfuzje i reguły disambiguation; scenariusze testów regresji i safety.  
- Plan rollout i kryteria promotion (metryki progowe).


## Wymagane streszczenia

- Executive snapshot: top intenty, pokrycie, metryki, główne konfuzje.  
- Lista krytycznych scenariuszy safety/abuse i ich obsługa.


## Guidance (skrót)

- Minimalizuj liczbę intentów, ale pokrywaj krytyczne scenariusze; dodawaj negatywne przykłady.  
- Pilnuj PII: redakcja w logach, maskowanie w anotacjach.  
- Utrzymuj balans klas i monitoruj drift; okresowo re‑train.  
- Automatyzuj testy regresji i walidacje safety przed promocją modelu.  
- Dokumentuj zmiany (data/model version) i ich wpływ na metryki.


## Checklisty Definition of Ready (DoR)

- [ ] Lista intentów/encji i zasady anotacji uzgodnione.  
- [ ] Dane/anotacje dostępne i oczyszczone z PII; narzędzia gotowe.  
- [ ] Metryki docelowe i progi ustalone; scenariusze testów opisane.  
- [ ] Plan rollout/promotion i monitoringu określony.  
- [ ] Wymagania safety/abuse i privacy zidentyfikowane.


## Checklisty Definition of Done (DoD)

- [ ] Zbiory train/valid/test i modele wersjonowane; metryki osiągnięte lub wyjątki zaakceptowane.  
- [ ] Testy regresji/safety przeszły; logi/anotacje bez PII.  
- [ ] Rollout wykonany zgodnie z planem; monitoring drift/feedback aktywny.  
- [ ] Dokumentacja/intenty/encje zaktualizowane; status/wersja/data uzupełnione.  
- [ ] Konfuzje i lesson learned dopisane do linkage_index/repo wiedzy.

