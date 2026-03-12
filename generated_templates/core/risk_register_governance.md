---
title: Risk Register (Governance)
status: needs_content
aligned: true
aligned_rev: 3
aligned_at: 2026-02-09
aligned_by: codex
---
# Risk Register (Governance)


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved



## Cel dokumentu

Zdefiniować zasady ładu (governance) dla prowadzenia Risk Register: role i odpowiedzialności, częstotliwość przeglądów, kryteria akceptacji ryzyk, wymagane dowody, audyt zmian i integracja z decyzjami zarządczymi (Steering/Exec/Board).


## Zakres i granice

- Obejmuje: procesy utrzymania rejestru (tworzenie/aktualizacja/przeglądy), RACI, polityki akceptacji/eskalacji, wymagania dowodowe, integrację z planem testów/release/TPRM, raportowanie (zarząd/audyt/regulator).
- Poza zakresem: szczegółowe wpisy ryzyk (są w Risk Register), wybór konkretnych mitygacji (Risk Mitigation Plan/Status), definicja scoringu (Risk Management Plan).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia
- Wejścia: warsztaty ryzyk, Lessons Learned, wyniki testów, analizy bezpieczeństwa/compliance, zależności zewnętrzne, roadmapa.
- Wyjścia: zaktualizowana lista ryzyk z priorytetem, plan mitygacji, terminy przeglądów, sygnały do planu testów i harmonogramu.
## Założenia
- Jeden rejestr dla projektu/produktu (unikaj duplikatów w wielu arkuszach).
- Każda mitygacja ma przypisanego właściciela i mierzalny dowód wdrożenia (test, ticket, raport).
## Otwarte pytania
- Czy wymagany jest osobny rejestr dla ryzyk vendorów (TPRM), czy wystarczy tag „vendor”?
- Czy ryzyka czerwone muszą mieć zatwierdzenie Steering Committee przy akceptacji?
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
## Struktura sekcji (szkielet)

1. Zasady utrzymania rejestru: źródło prawdy (DB/arkusz), format, kontrola dostępu (RBAC).
2. Cykl przeglądów: cadence wg RAG (czerwone tyg., żółte co 2 tyg., zielone mies.), agenda, uczestnicy.
3. Akceptacje ryzyk: kto zatwierdza, progi (czerwone/żółte), data wygaśnięcia, warunki cofnięcia, Risk Acceptance Log.
4. Wymagania dowodowe: testy/scan/runbook/DR drill jako evidence dla statusu „mitigated/done”, linki do repo logów/ticketów.
5. Eskalacje i raportowanie: ścieżka eskalacji, format executive summary (Top 10, blockers), heatmapy, raporty dla audytu/regulatora.
6. Integracje: Change/Release gating, Test Strategy/Security Testing (priorytety), Incident/Postmortem (aktualizacje), TPRM (vendor SLA/exit plan).
7. KPI/metryki: % ryzyk bez ownera, % ryzyk z przeterminowaną akceptacją, średni czas zamknięcia mitygacji, pokrycie dowodami.
8. Ścieżka audytu: kto/kiedy/co zmienił (P/I/RAG/reakcja/status), zatwierdzenia, wersjonowanie.


## Szybkie powiązania

- Dodaj ręcznie 2–3 kluczowe powiązania doc↔doc lub sekcja↔sekcja, korzystając z linkage_index.jsonl / content_links*.json (decyzje, ryzyka, zależności).

Przykład:
- Risk Management Plan ↔ ta polityka governance (metodyka i tolerancje).
- Risk Register ↔ Change/Release Plan (warunki „go/no-go”).
- Risk Register ↔ Incident/Postmortem (źródło nowych ryzyk i rewizji P/I).


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **COBIT 2019** — Kontrola nad Informacją i Technologiami (ISACA)
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **ISO/IEC 38500** — Ład Informatyczny Organizacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.

## Standardy i compliance


Lista standardów i wymagań regulacyjnych mających zastosowanie do tego dokumentu.
Uzupełnij na podstawie sekcji "Mające zastosowanie standardy i normy" oraz tabeli `doc_standard_mapping`.

- Standard / norma: [kod i nazwa]
- Wymaganie regulacyjne: [kod i treść]
- Polityka wewnętrzna: [nazwa polityki]

## RACI i role

- Risk Owner — odpowiada za treść wpisu, mitygacje, dowody.
- Risk Manager/PM — utrzymuje rejestr, pilnuje cadence przeglądów, konsoliduje raporty.
- Security/Compliance — weryfikuje ryzyka bezpieczeństwa/regulacyjne, akceptacje wyjątków.
- Steering Committee / Sponsor — zatwierdza akceptacje ryzyk czerwonych, decyduje o „go/no-go”.
- Audit/QA — weryfikuje kompletność, dowody i ścieżkę audytu.
- Backup owners — wyznaczeni dla ciągłości w razie nieobecności.



## Jak używać dokumentu

- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty jakości

- [ ] Źródło prawdy rejestru i kontrola dostępu (RBAC) opisane.
- [ ] Cadence przeglądów zdefiniowane per RAG; uczestnicy i agenda wskazane.
- [ ] Zasady akceptacji ryzyk (progi, kto zatwierdza, data wygaśnięcia) opisane; link do Risk Acceptance Log.
- [ ] Wymagania dowodowe dla statusu „mitigated/done” podane.
- [ ] Eskalacje i format raportów (Top 10, blockers, heatmapy) określone.
- [ ] KPI/metryki jakości rejestru zdefiniowane i mierzalne.
- [ ] Ścieżka audytu (kto/kiedy/co) opisana; wersjonowanie zapewnione.
- [ ] Powiązania z Change/Release/Test/Incident/TPRM opisane lub N/A z uzasadnieniem.


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

## Kryteria ukończenia (DoD)

- Sekcje źródło prawdy/RBAC, cadence, akceptacje, dowody, eskalacje, KPI, audyt – uzupełnione lub N/A z uzasadnieniem.
- Linki do Risk Management Plan, Risk Register, Risk Mitigation Plan/Status, Risk Acceptance Log działają.
- Metadane (status, data, wersja, właściciel) aktualne.


## Kryteria wejścia (DoR)

- Risk Management Plan i Risk Register dostępne.
- Ustalony właściciel procesu (Risk Manager/PM) i sponsor akceptacji (Steering/Exec).
- Określone narzędzia/DB jako źródło prawdy i dostęp dla interesariuszy.
