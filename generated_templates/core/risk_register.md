---
title: Risk Register
status: needs_content
aligned: true
aligned_rev: 1
aligned_at: 2026-02-09
aligned_by: codex
---

# Risk Register

## Metadane
- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Centralnie rejestrować ryzyka projektu/produktu z oceną wpływu i prawdopodobieństwa, właścicielem, planem mitygacji i statusem. Ułatwia monitorowanie i decyzje „accept / mitigate / transfer / avoid”.

## Zakres i granice
Obejmuje: identyfikację, kategoryzację, scoring (np. 5x5), plany reakcji, status mitygacji, linki do incydentów/zgłoszeń, przeglądy cykliczne. Nie obejmuje: szczegółowych postmortemów (są osobno).

## Risk appetite i tolerancje (skrót)
- Bezpieczeństwo: brak akceptacji ryzyk P1 dla danych wrażliwych; akceptacja czasowa możliwa tylko z datą wygaśnięcia i planem mitygacji.
- Dostępność: tolerancja przestoju zgodnie z RTO, utrata danych zgodnie z RPO; czerwone ryzyka dostępności wymagają planu DR/BCP.
- Budżet: akceptacja odchyleń kosztowych ≤10% (projekt) lub ≤5% (run) po zatwierdzeniu sponsora.
- Regulacje: zero‑tolerance dla niezgodności obowiązkowych (SOX/ISO 27001/PCI DSS/HIPAA); wyjątki dokumentowane w Risk Acceptance Log.

## Wejścia i wyjścia
- Wejścia: warsztaty ryzyk, Lessons Learned, wyniki testów, analizy bezpieczeństwa/compliance, zależności zewnętrzne, roadmapa.
- Wyjścia: zaktualizowana lista ryzyk z priorytetem, plan mitygacji, terminy przeglądów, sygnały do planu testów i harmonogramu.

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance

## Zależności dokumentu
- Konsumuje: Risk Assessment, Project Charter, Test/Deployment/Change plans, Security assessments.
- Dostarcza do: Planów mitygacji, harmonogramu (bufory), komunikacji statusowej, Incident/Problem management.

- Ryzyka wysokie → plany mitygacji i właściciele.
- Ryzyka harmonogramowe → bufory w Timeline.
- Ryzyka bezpieczeństwa → Playbooki i kontrole w Test Strategy/Deployment.

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
- Metodyka i skala oceny: P (1–5) × I (1–5) = score; progi RAG (zielony ≤5, żółty 6–12, czerwony ≥15); opcjonalnie D (wykrywalność) dla FMEA.
- Tabela ryzyk (proponowane kolumny):
  - ID, Tytuł, Opis, Data dodania, Źródło (warsztat/test/incydent/zmiana).
  - Kategoria (biznes/techniczne/operacyjne/bezpieczeństwo/vendor/regulacyjne/dane/AI/dostępność).
  - P, I, Score, RAG; Sygnały wczesne/leading indicators; Trend (↑ ↔ ↓).
  - Właściciel (risk owner), Backup owner; Interesariusze.
  - Reakcja (accept/mitigate/transfer/avoid) + szczegóły mitygacji.
  - Terminy: due date mitygacji, następny przegląd, data wygaśnięcia akceptacji.
  - Status (open/in progress/mitigated/accepted/closed), dowody wdrożenia (ticket/commit/runbook/test report).
  - Powiązania: ADR, Change Request, Release, Test Case/Plan, Incident/Postmortem, Vendor SLA, kontrola bezpieczeństwa.
- Plan reakcji: opis działań, właściciel, koszty, wpływ na RTO/RPO/KPI, kryteria sukcesu.
- Raportowanie i przeglądy: cadence (czerwone tygodniowo, żółte dwutygodniowo, zielone miesięcznie), format dashboard/heatmapa.
- Historia zmian / audyt: kto, kiedy, co zmienił (P/I/score/reakcja/status), link do zatwierdzenia.

## Wymagane rozwinięcia
- Metodyka scoringu → zgodnie z „Risk Management Plan”.
- Tolerancje ryzyka → skrót z „Risk Management Plan / Risk Appetite Statement”.
- Reakcje i eskalacje → „Incident Response Plan” oraz „Change/Release Plan”.
- Kontrole bezpieczeństwa → „Security/Compliance Requirements” i „Cloud Security Baseline”.

## Wymagane streszczenia
- Streszczenie „Top 10 ryzyk” (tytuł, RAG, właściciel, ETA mitygacji) do komunikacji zarządczej.
- Streszczenie „Ryzyka zaakceptowane” z datą wygaśnięcia i warunkami cofnięcia.

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

w/audytów.

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
- [ ] P/I (i D jeśli stosowana) mają zdefiniowaną skalę i progi RAG.
- [ ] Tabela ryzyk zawiera właściciela, status, terminy mitygacji i przeglądów.
- [ ] Każde ryzyko ma przypisaną reakcję (accept/mitigate/transfer/avoid) i dowody postępu.
- [ ] Top ryzyka i ryzyka zaakceptowane mają streszczenie i daty wygaśnięcia.
- [ ] Powiązania do Incident/Postmortem/Change/Release/Test są uzupełnione lub N/A z uzasadnieniem.
- [ ] Link do Risk Management Plan oraz Risk Acceptance Log istnieje.
- [ ] Audyt zmian (kto/kiedy/co) jest prowadzony.
- [ ] Kryteria DoR/DoD poniżej spełnione.

## Definicje robocze
- Risk Owner — osoba odpowiedzialna za mitygację i raportowanie statusu ryzyka.
- Risk Acceptance Log — rejestr akceptacji ryzyk z datą wygaśnięcia i warunkami.
- Heatmapa — wizualizacja ryzyk wg P/I (i D), służy do priorytetyzacji.

## Przykłady użycia
- Migracja do chmury: ryzyka lokalizacji danych, szyfrowania, cutover/rollback, przydział kluczy KMS.
- Wdrożenie nowego vendor SaaS: ryzyka TPRM (SLA, dostępność, BCP dostawcy), privacy, lock‑in, zgodność (SOC2/ISO 27001).

## Ryzyka i ograniczenia
- Brak terminów przeglądu → ustal cadence wg RAG, automatyczne przypomnienia.
- Nieaktualne P/I po zmianach architektury → wymuś aktualizację przy każdym major change lub postmortem.
- Rozproszone akceptacje → centralizuj w Risk Acceptance Log z datą wygaśnięcia.

## Decyzje i uzasadnienia
- Utrzymanie skali 5×5 (P×I) dla spójności z raportowaniem zarządczym.
- Dodanie trendu ryzyka (↑ ↔ ↓) ułatwia decyzje o eskalacji.

## Założenia
- Jeden rejestr dla projektu/produktu (unikaj duplikatów w wielu arkuszach).
- Każda mitygacja ma przypisanego właściciela i mierzalny dowód wdrożenia (test, ticket, raport).

## Otwarte pytania
- Czy wymagany jest osobny rejestr dla ryzyk vendorów (TPRM), czy wystarczy tag „vendor”?
- Czy ryzyka czerwone muszą mieć zatwierdzenie Steering Committee przy akceptacji?

## Powiązania z innymi dokumentami
- Risk Management Plan — dostarcza metodykę, progi RAG i tolerancje.
- Risk Acceptance Log — przechowuje decyzje o akceptacji wraz z datą wygaśnięcia.
- Test Strategy / Security Testing Plan — priorytetyzuje testy wg ryzyk czerwonych/żółtych.
- Change/Release Plan — wymaga oceny ryzyka dla każdego CR/release.
- Incident/Postmortem — źródło nowych ryzyk lub aktualizacji P/I.

## Powiązania z sekcjami innych dokumentów
- Incident Response Plan → Lessons Learned → nowe ryzyka lub zmiana trendu.
- Architecture Decision Records → decyzje kryptografia/IAM → wpływ na P/I bezpieczeństwa.
- SLA/SLO → sekcja dostępności → wpływ na kategorie dostępności i operacyjne.

## Słownik pojęć w dokumencie
- RAG — Red/Amber/Green, kodowanie progów ryzyka.
- Early Warning Indicator — metryka/sygnał wczesnego ostrzegania dla ryzyka.
- Residual Risk — ryzyko po mitygacji; może wymagać akceptacji.

## Wymagane odwołania do standardów
- ISO 31000 / ISO 27005 — metodyka oceny i raportowania.
- NIST SP 800‑30 — analiza ryzyk; wspiera kolumny P/I i heatmapę.
- SOC 2 / ISO 27001 A.8 / PCI DSS — dowód istnienia procesu rejestru ryzyk i akceptacji.

## Mapa relacji sekcja→sekcja
- Metodyka → Tabela ryzyk: skale i progi stosowane w kolumnach P/I/Score.
- Tabela ryzyk → Plan reakcji: dla ryzyk czerwonych wymagany plan i właściciel.
- Plan reakcji → Status/Przeglądy: terminy mitygacji determinują cadence raportów.
- Status → Raportowanie: RAG i trend zasilają dashboard/heatmapę.

## Mapa relacji dokument→dokument
- Risk Register -> Risk Management Plan: używa jego metodyki.
- Risk Register -> Test Strategy / Security Testing Plan: priorytety testów.
- Risk Register -> Change/Release Plan: gating release’ów przy ryzykach czerwonych.
- Risk Register -> Incident/Postmortem: aktualizacja po incydentach.

## Ścieżki informacji
- „Nowy vendor” → Identyfikacja → Kategoria vendor → Plan mitygacji + TPRM → SLA/exit plan → Status/Przegląd.
- „Zmiana architektury” → Analiza → Kategoria techniczne/operacyjne → P/I/Score → Plan mitygacji → Bufory w harmonogramie.
- „Incydent P1” → Postmortem → Nowe ryzyko lub zmiana P/I → Plan reakcji → Testy regresji i warunki release.

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
- Skale P/I (i D jeśli używana) zdefiniowane; progi RAG wpisane.
- Tabela ryzyk uzupełniona: kategorie, właściciele, reakcje, terminy, powiązania.
- Top 10 ryzyk i lista akceptacji mają streszczenia i daty przeglądu.
- Linki do Risk Management Plan i Risk Acceptance Log działają.
- Raportowanie/heatmapa ma ustalony format i odbiorców.
- Audyt zmian prowadzony; status/właściciel/data w metadanych aktualne.

## Kryteria wejścia (DoR)
- Zakres projektu i cele znane; wstępna lista ryzyk (z warsztatów/incydentów) dostępna.
- Ustalony właściciel rejestru i kanał przechowywania (DB/arkusz).
- Metodyka scoringu i progi RAG zatwierdzone (spójne z Risk Management Plan).

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
