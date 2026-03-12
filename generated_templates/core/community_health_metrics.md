---
title: Community Health Metrics
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Community Health Metrics


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje metryki oceniające zdrowie społeczności (fora, OSS, gry, produkty) – aktywność, jakość, bezpieczeństwo i satysfakcję. Ma pomóc w wczesnym wykrywaniu spadków jakości, toksyczności i ryzyk reputacyjnych.


## Zakres i granice

- Obejmuje: metryki aktywności (MAU/DAU, posty, komentarze), retencję i kohorty, jakość treści (signal/noise, odpowiedzi rozwiązane), moderację/toxicity/abuse, SLA odpowiedzi, sentiment/NPS, wkład kontrybutorów (PR/issue velocity w OSS), eskalacje, raportowanie i alerty, segmenty (nowi/stali, role).
- Poza zakresem: strategia wzrostu społeczności (oddzielny dokument), szczegółowe polityki moderacji (referencja).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: dane z platformy (posty, reakcje, raporty nadużyć), logi moderacji, dane produktowe (aktywizacje), ankiety (NPS/CSAT), dane sentiment, SLA supportu, metadane ról, polityki moderacji.
- Wyjścia: zestaw metryk/KPI/KRI, definicje i źródła, dashboardy, alerty i progi, raporty cykliczne, lista działań korygujących i właścicieli.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: moderation_policy, support_sla, product_analytics, trust_and_safety, community_growth_strategy.
- Key Document Structures: metryki, progi, alerty, raporty, działania.
- Document Dependencies: data warehouse/BI, abuse detection, sentiment pipeline, support tooling, identity/roles.


## Zależności dokumentu

Wymaga spójnych źródeł danych (posty, raporty, moderacja), polityk moderacji/SLA, narzędzi BI/alertingu, definicji ról/segmentów. Bez tego DoR otwarte.


## Fazy cyklu życia

- Planowanie: wybór metryk/KPI/KRI, źródeł danych i progów.
- Implementacja: instrumentacja, dashboardy, alerty.
- Operacje: monitoring, raporty cykliczne, działania korygujące.
- Retrospektywa: trend, wpływ działań, zmiana progów/metryk.



## Struktura sekcji (szkielet)
- Zakres raportu i okres
- Definicje metryk/KPI i źródła danych
- Wyniki z trendami i wizualizacjami
- Insighty i obserwacje
- Ryzyka/odchylenia i ich wpływ
- Rekomendacje i plan działań z właścicielami
- Załączniki/metodologia
## Szybkie powiązania

- linkage_index.jsonl (community/health)
- moderation_policy, support_sla, trust_and_safety, product_analytics, community_growth_strategy


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **GDPR / RODO** — Ogólne Rozporządzenie o Ochronie Danych Osobowych (UE)
- **HL7 FHIR** — Standard Wymiany Danych w Ochronie Zdrowia
- **IEEE 829** — Dokumentacja Testowania Oprogramowania i Systemów
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 25010** — Model Jakości Systemu i Oprogramowania (SQuaRE)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)

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
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.
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

- Metryki → Progi/alerty → Raporty → Działania korygujące.
- Moderacja/toxicity → Trust & Safety → Komunikacja/eskalacje.
- Wkład kontrybutorów → Velocity → Backlog/roadmap.


## Struktura sekcji

1) Cele i segmenty społeczności (role, nowi/stali)  
2) Metryki aktywności i wzrostu (MAU/DAU, posty, retention, kohorty)  
3) Metryki jakości i rozwiązywania (accepted/solution rate, time to first response, SLA)  
4) Trust & Safety (toxicity/abuse reports, mod actions, false pos/neg)  
5) Satysfakcja/sentiment (NPS/CSAT, sentiment, feedback)  
6) Kontrybucje (PR/issues velocity, reviewers, bus factor w OSS)  
7) Alerty/progi i eskalacje (kto reaguje, w jakim czasie)  
8) Raporty i dashboardy (widoki exec/ops/community)  
9) Działania korygujące, właściciele, harmonogram  


## Wymagane rozwinięcia

- Definicje metryk i wzory (np. time to first response, accepted rate, toxicity score), okna czasowe.
- Progi/alerty i właściciele reakcji; kanały eskalacji.
- Segmentacja ról/regionów; źródła sentiment/NPS/CSAT.


## Wymagane streszczenia

- Top KPI/KRI i ich progi; obecny stan (zielony/pomarańczowy/czerwony).
- Najważniejsze ryzyka (toxicity, spadek odpowiedzi, odpływ kontrybutorów).


## Guidance (skrót)

- Zacznij od kilku KPI: time to first response, solution rate, toxicity, DAU/MAU, NPS/CSAT.
- Mierz jakościowo: ratio odpowiedzi wysokiej jakości vs. spam/noise.
- Automatyzuj alerty dla toxicity/abuse i SLA odpowiedzi; przypisz właścicieli.
- Oddziel widoki exec (trend, ryzyka) od ops (alerty, backlog moderacji).
- Zbieraj feedback i iteruj progi; dokumentuj działania i ich wpływ.

