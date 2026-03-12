---
title: Risk Mitigation Status
status: needs_content
aligned: true
aligned_rev: 2
aligned_at: 2026-02-09
aligned_by: codex
---

# Risk Mitigation Status

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Zapewnić bieżący, audytowalny podgląd stanu mitygacji ryzyk: co jest wdrożone, co opóźnione, jakie są blokery, dowody skuteczności i wpływ na ryzyka (RAG, trend). Służy do decyzji „go/no-go”, eskalacji i raportowania (zarząd, audyt, regulator).

## Zakres i granice
Obejmuje: wszystkie mitygacje dla ryzyk czerwonych i żółtych (oraz zaakceptowane z datą wygaśnięcia), status wdrożenia, dowody testów, wpływ na SLA/SLO/RTO/RPO, koszty/zasoby. Poza zakresem: definiowanie metodyki scoringu (jest w Risk Management Plan) i pierwotne planowanie mitygacji (Risk Mitigation Plan).

## Wejścia i wyjścia
- Wejścia: Risk Register (RAG, trend), Risk Mitigation Plan (działania, terminy, kryteria sukcesu), wyniki testów/scanów, CR/Release/Deployment status, SLA/SLO, TPRM/SLA vendorów, postmortem/incident actions.
- Wyjścia: zaktualizowany status mitygacji (tabela), sygnały do harmonogramu i release (go/no-go), decyzje eskalacyjne, raporty dla zarządu/audytu, aktualizacje heatmapy i Risk Acceptance Log.

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
Jeżeli brak danych w bazie: wypisz znane zależności (dokumenty, kontrakty, usługi), wskaż właścicieli i wpływ na kolejność prac; gdy brak zależności – zapisz to wprost.

## Powiązania sekcja↔sekcja
Określ, które sekcje wymagają rozwinięcia lub streszczenia (np. gdy są kluczowe dla decyzji, ryzyka lub zgodności) i podaj uzasadnienie.

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
- Faza 10: Incident Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 11: Monitoring / Observability: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 12: Dokumentacja referencyjna: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 13: Szkolenie / Onboarding: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 14: Komunikacja stakeholders: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 15: Knowledge Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 16: Postmortem / Retrospektywa: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 17: Budżetowanie / Cost Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 18: Vendor Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 19: Governance / Compliance: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 20: Decommission / Sunset: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 21: DR / BCP: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 22: Change Management: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.
- Faza 23: Capacity Planning: Określ czy w tej fazie dokument powstaje, jest aktualizowany, przeglądany lub archiwizowany; podaj uzasadnienie i odpowiedzialnych.


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
- Podsumowanie statusu (executive): % mitygacji czerwonych/żółtych zakończonych, opóźnione, blokery, decyzje.
- Tabela mitygacji (propozycja kolumn):
  - Risk ID/tytuł, Kategoria, RAG, Trend.
  - Właściciel mitygacji, Backup owner.
  - Status mitygacji (not started / in progress / blocked / done / accepted), Data ostatniej aktualizacji.
  - Działania kluczowe, % ukończenia, zależności/blokery, wymagane zasoby.
  - Dowody skuteczności: test/scan/runbook/DR drill/pen‑test, data, wynik.
  - Wpływ na SLA/SLO/RTO/RPO/KPI (przed/po), residual risk.
  - Termin mitygacji, termin kolejnego przeglądu, data wygaśnięcia akceptacji.
  - Linki: CR/Release/Ticket, Test Case, Playbook/Runbook, Vendor SLA, Evidence.
- Eskalacje i decyzje: lista elementów wymagających decyzji Steering/Exec, proponowane warianty (continue/pivot/stop), konsekwencje.
- Raportowanie i cadence: częstotliwość aktualizacji (czerwone tyg., żółte co 2 tyg.), format (dashboard/CSV/DB), odbiorcy.
- Wpływ na harmonogram i budżet: bufory, zmiany zakresu, koszty CapEx/OpEx.

## Wymagane rozwinięcia
- Metodyka statusów i progów RAG → Risk Management Plan.
- Lista mitygacji i kryteria sukcesu → Risk Mitigation Plan.
- Dowody bezpieczeństwa/testów → Security Testing Plan / Test Strategy.
- Vendor/TPRM → Vendor Management / SLA.

## Wymagane streszczenia
- Streszczenie „Top blockers” (ryzyka czerwone, opóźnienia, wpływ) dla Steering.
- Streszczenie „Mitigations done” z dowodami i redukcją ryzyka (score/RAG przed vs po).

## Guidance
Cel: skrócone wskazówki do wypełniania szablonów dokumentów (core/satellite).

- Cel dokumentu: 2–3 zdania o decyzjach, ryzykach i wartości dokumentu.
- Zakres i granice: co obejmuje (systemy/procesy/zespoły) i czego nie obejmuje; zaznacz granice odpowiedzialności.
- Wejścia: dane, wymagania, standardy, zależności potrzebne przed startem.
- Wyjścia: artefakty/rezultaty, kto je konsumuje, format (link/plik).
- Zależności dokumentu: wymagane dokumenty lub decyzje; właściciel; wpływ na kolejność prac.
- Powiązania sekcja↔sekcja: które sekcje się rozwijają/streszczają; podaj uzasadnienie.
- Struktura sekcji: utrzymuj układ logiczny; sekcje bez treści oznacz jako N/A z krótkim uzasadnieniem.
- Fazy cyklu życia: zaznacz, w których fazach dokument powstaje/aktualizuje się/archiwizuje; kto odpowiada.
- DoR (Definition of Ready): zakres, wejścia, role, zależności, kryteria akceptacji gotowe.
- DoD (Definition of Done): sekcje uzupełnione lub N/A, powiązania wpisane, checklisty jakości sprawdzone, wersja/data/właściciel, linki/artefakty działają.
- Język: polski; nazwy własne pozostają bez zmian; liczby w nazwach plików usunięte już w szablonach.
- Filozofia: optymalizuj przez rozwój, nie ucinanie — dodawaj, nie kasuj; elementy „satelitarne” zostają.

odwołania.

## Szybkie powiązania
- Meta: Key Documents
- Meta: Key Document Structures
- Meta: Document Dependencies

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty jakości
- [ ] Statusy mitygacji są aktualne (data, właściciel, % ukończenia).
- [ ] Każdy status ma dowód (test/scan/runbook/DR drill) albo plan pozyskania dowodu.
- [ ] Opóźnienia mają zidentyfikowane blokery, właścicieli i daty usunięcia.
- [ ] Wpływ na SLA/SLO/RTO/RPO/KPI jest zaktualizowany po mitygacji.
- [ ] Eskalacje i decyzje są opisane z konsekwencjami (czas/koszt/bezpieczeństwo).
- [ ] Raportowanie ma ustaloną cadence i odbiorców; format danych spójny z dashboardem/DB.
- [ ] Linki do Risk Register, Risk Mitigation Plan, Change/Release, Test, Vendor SLA są uzupełnione.
- [ ] Kryteria DoR/DoD poniżej spełnione; metadane aktualne.

## Definicje robocze
- Status „blocked” — mitygacja nie postępuje z powodu zależności (vendor, zasób, okno wdrożenia, decyzja).
- Residual Risk — ryzyko po mitygacji; może pozostać żółte, wymaga akceptacji.
- Evidence — zweryfikowany dowód (raport testu, log z DR drill, ticket z wdrożenia).

## Przykłady użycia
- Czerwone ryzyko „data exposure”: mitygacja (KMS/rotation/DLP/log review) → status „in progress”, dowód: pen‑test i log review; blocker: dostęp do kluczy → eskalacja do Security Lead.
- Żółte ryzyko „downtime”: mitygacja (HA/auto‑scale/failover drills) → status „done”, dowód: DR drill, metryki SLO poprawione 99.5→99.9.

## Ryzyka i ograniczenia
- Fałszywe „done” bez dowodów → wymagaj evidence i daty testów; audyt okresowy.
- Brak aktualizacji statusów → automatyczne przypomnienia; właściciel statusu i zastępstwo.
- Rozjazd danych między dashboardem a dokumentem → źródło prawdy ustalone (DB/CSV) + export.

## Decyzje i uzasadnienia
- Cadence: czerwone tygodniowo, żółte co 2 tyg., zielone miesięcznie — fokus na krytyczne luki.
- Wymóg dowodu dla statusu „done” — zgodność z audytem/regulatorem i ograniczenie ryzyka pozornego domknięcia.

## Założenia
- Risk Register i Risk Mitigation Plan są aktualne i spójne (ID, RAG, właściciele).
- Dostępne narzędzia do testów/scanów i repo dowodów (DB/arkusz/git/ELK/SIEM).

## Otwarte pytania
- Czy statusy mają być aktualizowane automatycznie z narzędzi (Jira/CI/CD/SIEM), czy ręcznie?
- Jak długo przechowujemy dowody (wymogi audytu/regulatora)?

## Powiązania z innymi dokumentami
- Risk Register — źródło RAG/trend/owner.
- Risk Mitigation Plan — źródło działań i kryteriów sukcesu.
- Change/Release Plan — warunki „go/no-go” powiązane ze statusem mitygacji.
- Test Strategy / Security Testing Plan — dostarcza dowody skuteczności.
- Incident/Postmortem — dodaje lub zmienia mitygacje i statusy.

## Powiązania z sekcjami innych dokumentów
- Incident Response Plan → Lessons Learned → aktualizacja statusów i nowych mitygacji.
- Architecture Decision Records → wpływ na zależności i priorytety mitygacji.
- SLA/SLO → wpływ na kolumnę „wpływ po mitygacji”.

## Słownik pojęć w dokumencie
- Blocker — przeszkoda uniemożliwiająca postęp mitygacji; musi mieć właściciela i datę usunięcia.
- Evidence — potwierdzenie skuteczności (raport testu, log, ticket).
- Residual Risk — ryzyko po mitygacji, oceniane ponownie w Risk Register.

## Wymagane odwołania do standardów
- ISO 31000 / ISO 27005 — zasady raportowania i przeglądów ryzyk.
- NIST SP 800‑30 — rekomendacje dotyczące dokumentowania skuteczności mitygacji.
- SOC 2 / ISO 27001 A.8 / PCI DSS — wymagają dowodów kontroli i ich regularnej weryfikacji.

## Mapa relacji sekcja→sekcja
- Kryteria włączenia -> Tabela mitygacji: filtruje, które ryzyka trafiają do planu.
- Tabela mitygacji -> Integracja z harmonogramem: działania wprowadzane jako zadania/kamienie milowe.
- Integracja -> Monitoring: metryki i SLO obserwują skuteczność działań.
- Monitoring -> Eskalacja: brak postępu lub niespełnione kryteria sukcesu wyzwalają eskalację.
## Mapa relacji dokument→dokument
- Risk Mitigation Plan -> Risk Register: korzysta z rankingów i parametrów ryzyk.
- Risk Mitigation Plan -> Change/Release Plan: wymaga wdrożenia mitygacji przed releasami.
- Risk Mitigation Plan -> Test Strategy/Security Testing: definiuje testy potwierdzające skuteczność.
- Risk Mitigation Plan -> Incident/Postmortem: aktualizuje działania po incydentach.
## Ścieżki informacji
- „Ryzyko P1 data exposure” → Kryteria włączenia → Tabela mitygacji (szyfrowanie/KMS/DLP/runbook) → Testy/Scan → Status/raport.
- „Ryzyko downtime 4h” → Tabela mitygacji (HA/auto‑scale/failover drills) → Integracja z release i SLO → Monitoring → Eskalacja gdy SLO naruszone.
- „Ryzyko vendor lock‑in” → Tabela mitygacji (exit plan, dual vendor, escrow) → SLA → Przegląd TPRM.
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
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Ścieżka akceptacji
- [Kto zatwierdza] → [kryteria akceptacji] → [status]
- [Kto zatwierdza] → [kryteria akceptacji] → [status]

## Kryteria ukończenia (DoD)
- Statusy mitygacji uzupełnione (właściciel, % ukończenia, blokery, dowody/testy, terminy).
- Top blockers opisane z planem usunięcia i właścicielem.
- Raportowanie: cadence/format/odbiorcy zapisane; eksport do dashboardu działa.
- Linki do Risk Register, Risk Mitigation Plan, Change/Release, Test Evidence działają.
- Sekcje N/A oznaczone z uzasadnieniem; metadane aktualne (status/wersja/data/owner).

## Kryteria wejścia (DoR)
- Risk Mitigation Plan dostępny i aktualny.
- Risk Register zaktualizowany (RAG, trend).
- Źródło prawdy dla statusów/dowodów ustalone (DB/arkusz/narzędzie) i dostępne.

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
