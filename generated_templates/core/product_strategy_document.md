---
title: Product Strategy Document
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Product Strategy Document

## Metadane
- Właściciel: Product Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Definiuje kierunek rozwoju produktu: segmenty/rynki, propozycję wartości, cele/KPI, filary i inicjatywy, horyzonty oraz zasady portfolio/governance. Łączy potrzeby użytkowników i cele biznesowe z wykonalnością techniczną i operacyjną.


## Zakres i granice
- Obejmuje: analiza rynku/segmentów, propozycja wartości, persony/use cases/jobs-to-be-done, cele/KPI/KR, filary i inicjatywy produktowe, model cenowy/monetyzacja, kanały, horyzonty roadmapy, zależności i ryzyka, governance i mierzenie postępu.
- Poza zakresem: szczegółowa implementacja funkcji (to w PRD/epikach), low-level design, backlog sprintów.



## Wejścia i wyjścia
- Wejścia: wizja firmy/produktu, analizy rynku/konkurencji, dane użytkowników (badania, telemetry, support), regulacje/ograniczenia techniczne, dane finansowe (CAC/LTV), sygnały ryzyka i szanse, możliwości technologiczne/partnerstwa.
- Wyjścia: propozycja wartości, cele/KPI/KR, segmenty i priorytety, filary i inicjatywy, roadmapa (T1/T2/T3), model monetyzacji/cen, zasady portfolio/governance, kryteria go/stop i sukcesu.



## Powiązania (meta)
- Key Documents: solution_vision_document, business_value_proposition, market_analysis, competitor_analysis, pricing_strategy, go_to_market_strategy, technology_strategy, ux_strategy, data_strategy, risk_register, roadmap.
- Key Document Structures: segment → problem → wartość → cel/KPI → inicjatywa → roadmapa → mierzenie.
- Document Dependencies: regulacje (np. PCI/ADA/GDPR), ograniczenia techniczne, zdolności operacyjne/support, kontrakty/partnerstwa.
- RACI: CPO/PO, Product Ops, UX/Research, Marketing/GTM, Sales, Finance, Architecture/Tech, Legal/Compliance, Support/Success.
- Standardy/compliance: prywatność/dane, dostępność (WCAG/ADA), płatności, treści/platform policies.

## Zależności dokumentu
- Upstream: strategia firmy, insighty z badań rynku/użytkowników, analizy finansowe, ograniczenia prawne/tech, strategia technologiczna.
- Downstream: PRD/epiki/user stories, UX/UI kierunki, plany GTM/marketing/sales enablement, plany danych/analityki, plany operacyjne/support.
- Zewnętrzne: partnerstwa, marketplace policies, regulacje sektorowe, zależności od platform (OS/store/API), dostawcy płatności/danych.



## Powiązania sekcja↔sekcja
- Segmenty/problem → Propozycja wartości → Cele/KPI → Filary/inicjatywy → Roadmapa/horyzonty → GTM/monetyzacja → Monitoring i rewizje.



## Fazy cyklu życia
- Diagnoza rynku/segmentów i problemów (JTBD, pain points).
- Definicja propozycji wartości i celów/KPI.
- Projekt filarów/inicjatyw, pricing/monetyzacja, horyzonty roadmapy.
- Plan GTM/enablement i finansowanie.
- Monitorowanie KPI, rewizje portfela, sunset/stop rules.




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
## Struktura sekcji (szkielet)
1) Streszczenie i wizja produktu (misja, ambicja)
2) Segmenty/rynki i insighty (JTBD, persony, konkurencja, trendy)
3) Propozycja wartości i kluczowe use case’y
4) Cele/KPI/KR (biznes, produkt, użytkownik, jakość, koszt)
5) Filary i inicjatywy (wartość, koszt/benefit, zależności, alternatywy)
6) Roadmapa i horyzonty (T1/T2/T3, kamienie milowe, kryteria go/stop)
7) Pricing/monetyzacja i kanały (model, testy cenowe, CAC/LTV)
8) Ryzyka, założenia i zależności (regulacyjne, tech, operacyjne, rynkowe)
9) Governance i mierzenie postępu (cadence przeglądów, dashboardy, ownerzy)
10) Decyzje i otwarte pytania



## Wymagane rozwinięcia
- Roadmapa z horyzontami i kryteriami przesuwania inicjatyw.
- Macierz priorytetów (wpływ/łatwość/ryzyko/CAC/LTV) dla inicjatyw.
- Hipotezy i plan eksperymentów (MVP/MVT), metryki sukcesu.
- Model monetyzacji/pricing z wariantami i testem wstępnym.
- Plan GTM/enablement (komunikacja, materiały, szkolenia, kanały).



## Wymagane streszczenia
- Executive summary: propozycja wartości, segmenty, KPI, top filary, koszty/benefit, ryzyka.
- One-pager: co dostarczamy, dla kogo, kiedy (horyzonty), jak zarabiamy, jak mierzymy sukces.



## Guidance (skrót)
- DoR: segmenty i problemy zbadane; persony/JTBD opisane; ambicja KPI i horyzonty; ograniczenia/regulacje/guardrails spisane; właściciele filarów wyznaczeni.
- DoD: propozycja wartości, cele/KPI, filary/inicjatywy z koszt/benefit i priorytetem; roadmapa horyzontów; pricing/monetyzacja; ryzyka/założenia; governance i cadence przeglądów; metadane aktualne.
- Spójność: każda inicjatywa ma wskaźnik sukcesu, koszt/benefit, zależności, ryzyka i kanał walidacji (eksperyment/test rynkowy).



## Szybkie powiązania
- solution_vision_document, business_value_proposition, market_analysis, competitor_analysis, pricing_strategy, go_to_market_strategy, technology_strategy, ux_strategy, data_strategy, analytics_strategy
- roadmap, portfolio_management, cost_model, finops_guidelines, risk_register, accessibility_requirements, privacy_impact_assessment

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **SCRUM Guide** — Przewodnik Scrum

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty Definition of Ready (DoR)
- [ ] Segmenty/rynki, persony/JTBD i problemy opisane; dane/insighty zebrane.
- [ ] Ambicja KPI i horyzonty uzgodnione; ograniczenia/regulacje znane.
- [ ] Wstępne filary i warianty inicjatyw zidentyfikowane; metoda priorytetyzacji ustalona.

## Checklisty Definition of Done (DoD)
- [ ] Propozycja wartości, cele/KPI, filary i inicjatywy opisane z priorytetem i metrykami sukcesu.
- [ ] Roadmapa horyzontów, pricing/monetyzacja, GTM/enablement, ryzyka/założenia gotowe.
- [ ] Governance/cadence i dashboard KPI ustalone; metadane aktualne; dokument w linkage_index.

## Definicje robocze
- JTBD — Jobs To Be Done, opis pracy/użycia, jaką użytkownik próbuje wykonać.
- CAC/LTV — koszt pozyskania klienta / wartość życiowa klienta.
- Go/stop rule — warunek kontynuacji lub zatrzymania inicjatywy (kryteria metryk/czasu).

## Przykłady użycia
- Nowy produkt SaaS: segment SMB, propozycja wartości „redukcja czasu onboardingu”, KPI: aktywacje, time-to-value, NRR; filary: automatyzacja, self-service, integracje; pricing seat+usage.
- Rozszerzenie enterprise: moduł compliance, KPI: adoption modułu, upsell, churn reduction; filary: funkcje wymagane przez regulatora, raporty audytowe, SSO/SCIM; kanał: sprzedaż bezpośrednia + partnerzy.

## Artefakty powiązane
- Market/competitor analysis, persona/JTBD karty, value proposition canvas, pricing deck, roadmap, backlog epik, eksperymenty/hypothesis log, KPI dashboard.

## Weryfikacja spójności
- [ ] Każdy filar ma przypisane inicjatywy, metryki sukcesu, kanał walidacji i właściciela.
- [ ] Roadmapa spójna z zasobami, kanałami i ograniczeniami/regulacjami.
- [ ] Pricing/monetyzacja zgodne z segmentami i propozycją wartości; wsparcie GTM/enablement zaplanowane.

## Ryzyka i ograniczenia
- [Ryzyko 1 — wpływ i sposób ograniczenia]
- [Ryzyko 2 — wpływ i sposób ograniczenia]

## Decyzje i uzasadnienia
- [Decyzja 1 — uzasadnienie]
- [Decyzja 2 — uzasadnienie]

## Założenia
- [Założenie 1]
- [Założenie 2]

## Otwarte pytania
- [Pytanie 1]
- [Pytanie 2]

## Powiązania z innymi dokumentami
- [Dokument A] — [typ relacji] — [uzasadnienie]
- [Dokument B] — [typ relacji] — [uzasadnienie]

## Powiązania z sekcjami innych dokumentów
- [Dokument X → Sekcja Y] — [powód powiązania]
- [Dokument Z → Sekcja W] — [powód powiązania]

## Słownik pojęć w dokumencie
- [Pojęcie 1] — [definicja i źródło]
- [Pojęcie 2] — [definicja i źródło]
- [Pojęcie 3] — [definicja i źródło]

## Wymagane odwołania do standardów
- [Standard 1] — [sekcja/fragment, którego dotyczy]
- [Standard 2] — [sekcja/fragment, którego dotyczy]

## Mapa relacji sekcja→sekcja
- [Sekcja A] -> [Sekcja B] : [typ relacji]
- [Sekcja C] -> [Sekcja D] : [typ relacji]

## Mapa relacji dokument→dokument
- [Dokument A] -> [Dokument B] : [typ relacji]
- [Dokument C] -> [Dokument D] : [typ relacji]

## Ścieżki informacji
- [Wejście] → [Sekcja źródłowa] → [Sekcja rozwinięcia] → [Wyjście]
- [Wejście] → [Sekcja źródłowa] → [Sekcja streszczenia] → [Wyjście]

## Weryfikacja spójności
- [ ] Czy wszystkie ścieżki informacji są zamknięte?
- [ ] Czy istnieją pętle lub sprzeczne relacje?
- [ ] Czy sekcje krytyczne mają wskazane źródła i rozwinięcia?

## Lista kontrolna spójności relacji
- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań (np. wzajemne wykluczanie)?
- [ ] Czy relacje cross‑doc mają uzasadnienie i są zgodne z fazą?
- [ ] Czy relacje wymagają rozwinięć lub streszczeń są odnotowane?

## Artefakty powiązane
- [Artefakt 1] — [opis i relacja do dokumentu]
- [Artefakt 2] — [opis i relacja do dokumentu]

## Ścieżka decyzji
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]
- [Decyzja] → [Uzasadnienie] → [Konsekwencje]

## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Ścieżka akceptacji
- [Kto zatwierdza] → [kryteria akceptacji] → [status]
- [Kto zatwierdza] → [kryteria akceptacji] → [status]

## Kryteria ukończenia
- [ ] Kryterium 1 — [opis]
- [ ] Kryterium 2 — [opis]

## Metryki jakości
- [Metryka 1] — [cel / próg]
- [Metryka 2] — [cel / próg]

## Monitoring i utrzymanie
- [Co monitorujemy] — [narzędzie / częstotliwość]
- [Kto utrzymuje] — [rola]

## Kontrola zmian
- [Zmiana] — [powód] — [data] — [akceptacja]

## Wymogi prawne i regulacyjne
- [Wymóg 1] — [źródło / akt prawny / standard]
- [Wymóg 2] — [źródło / akt prawny / standard]

## Zasady bezpieczeństwa informacji
- [Zasada 1] — [opis i wpływ na dokument]
- [Zasada 2] — [opis i wpływ na dokument]

## Ochrona danych i prywatność
- [Wymaganie 1] — [opis i sekcja docelowa]
- [Wymaganie 2] — [opis i sekcja docelowa]

## Wersjonowanie treści
- [Wersja] — [zmiana] — [autor] — [data]
- [Wersja] — [zmiana] — [autor] — [data]

## Historia zmian sekcji
- [Sekcja] — [zmiana] — [data]
- [Sekcja] — [zmiana] — [data]

## Wymagane aktualizacje
- [Sekcja] — [powód aktualizacji] — [termin]
- [Sekcja] — [powód aktualizacji] — [termin]

## Integracje i interfejsy
- [System / API] — [zakres integracji] — [wymagania]
- [System / API] — [zakres integracji] — [wymagania]

## Wymagania danych
- [Dane wejściowe] — [format] — [walidacja]
- [Dane wyjściowe] — [format] — [walidacja]

## Logowanie i audyt
- [Zdarzenie] — [poziom] — [retencja]
- [Zdarzenie] — [poziom] — [retencja]

## Utrzymanie i operacje
- [Procedura] — [cel] — [częstotliwość]
- [Procedura] — [cel] — [częstotliwość]

## KPI i SLA
- [KPI] — [cel] — [pomiar]
- [SLA] — [cel] — [pomiar]

## Scenariusze awaryjne
- [Scenariusz] — [objawy] — [reakcja]
- [Scenariusz] — [objawy] — [reakcja]

## Wpływ na inne systemy
- [System] — [rodzaj wpływu] — [ryzyko]
- [System] — [rodzaj wpływu] — [ryzyko]

## Zależności danych między systemami
- [Źródło danych] → [Odbiorca] — [opis]
- [Źródło danych] → [Odbiorca] — [opis]

## Harmonogram przeglądów
- [Obszar] — [częstotliwość] — [właściciel]
- [Obszar] — [częstotliwość] — [właściciel]

## Wymagania wydajnościowe
- [Wymaganie] — [metryka] — [próg]
- [Wymaganie] — [metryka] — [próg]

## Wymagania dostępnościowe
- [Wymaganie] — [SLA] — [metoda pomiaru]
- [Wymaganie] — [SLA] — [metoda pomiaru]

## Wymagania skalowalności
- [Wymaganie] — [cel] — [warunki]
- [Wymaganie] — [cel] — [warunki]

## Wymagania dostępności danych
- [Dane] — [częstotliwość dostępu] — [SLA]
- [Dane] — [częstotliwość dostępu] — [SLA]

## Retencja i archiwizacja
- [Dane] — [retencja] — [archiwizacja]
- [Dane] — [retencja] — [archiwizacja]

## Dostępność w sytuacjach awaryjnych
- [Scenariusz] — [zachowanie] — [priorytet]
- [Scenariusz] — [zachowanie] — [priorytet]

## Testy i weryfikacja
- [Test] — [cel] — [wynik oczekiwany]
- [Test] — [cel] — [wynik oczekiwany]

## Walidacja zgodności
- [Wymóg] — [metoda weryfikacji]
- [Wymóg] — [metoda weryfikacji]

## Audyty i przeglądy
- [Audyty] — [częstotliwość] — [odpowiedzialny]
- [Audyty] — [częstotliwość] — [odpowiedzialny]
