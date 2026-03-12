---
title: Executive Risk Dashboard
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Executive Risk Dashboard


## Metadane

- Właściciel: Document Owner
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Zapewnić zwięzły widok zarządczy (C‑level/Steering) kluczowych ryzyk i issues: RAG, trend, top 10, wygasające akceptacje, status mitygacji i decyzje go/conditional/no‑go. Łączy dane z Risk Register, Mitigation, Acceptance, Incident/Postmortem i Compliance dashboards.


## Zakres i granice

- Obejmuje: KPI/KRI ryzyka (liczba czerwonych, trend), top 10 ryzyk, top issues P1/P2, wygasające akceptacje (sunset ≤30/60 dni), status mitygacji, decyzje/eskalacje, warunki go/conditional/no‑go na releasy/kamienie milowe.
- Poza zakresem: szczegółowe runbooki i pełne tabele rejestru (są w systemach operacyjnych).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: Risk Register, Risk Mitigation Plan/Status, Risk Acceptance Log, Risk & Issue Report, Incident/Postmortem, Compliance/Observability dashboards, Change/Release status.
- Wyjścia: deck/dashboard exec, lista decyzji/eskalacji (owner, due), sygnały do Release/Change gating, snapshot do audytu/regulatora.


## Założenia
- Zespoły używają jednego narzędzia do rejestru ryzyk (np. tracker w DB lub arkusz powiązany).
- Wszystkie mitygacje mają testy regresji bezpieczeństwa lub scenariusze UAT odzwierciedlające ryzyko.
## Otwarte pytania
- Czy dla tego projektu potrzebna jest ocena TPRM (Third‑Party Risk Management) dla nowych vendorów?
- Czy heatmapa ma być publikowana w raportach dla regulatora (jeśli tak, w jakim formacie)?
## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
- Konsumuje: Project Charter, Risk Assessment, Postmortem learnings, Security/Compliance wymagania.
- Dostarcza do: Risk Register, Harmonogram (bufory), Test Strategy/Plans, Change/Release plans, Communication plan.
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
- Cel, zakres, risk appetite/tolerancje.
- Metodyka oceny: skala P (1–5) × I (1–5) = wynik; progi RAG (zielony ≤5, żółty 6–12, czerwony ≥15); opcjonalnie wykrywalność (D) dla FMEA.
- Kategorie ryzyk: biznes (przychody, KPI), techniczne (architektura, wydajność, skalowalność), bezpieczeństwo (CIA, IAM, kryptografia), operacyjne (procesy, zmiany), vendor/supply chain, regulacyjne/compliance, dane/AI, dostępność (RTO/RPO), reputacyjne.
- Role i RACI: Sponsor (A), Risk Owner (R), Risk Manager (R), Architekt/Tech Lead (C), Security/Compliance (C), PM (A/R), QA (C), Legal/Privacy (C), Ops/SRE (R/C), Steering Committee (I).
- Proces: identyfikacja → ocena (P/I/D, RAG) → wybór reakcji (avoid/mitigate/transfer/accept) → plan mitygacji z właścicielami i terminami → monitorowanie metryk → eskalacja.
- Powiązanie z harmonogramem: bufory na ryzyka czerwone, warunki „go/no‑go”, punkty kontroli na kamieniach milowych.
- Raportowanie i cykl przeglądów: tygodniowo dla czerwonych, dwutygodniowo dla żółtych, miesięcznie dla zielonych; format: dashboard + notatka ryzyka; eskalacja P1 do Steering Committee ≤24h.
- Integracja z testami/QA: ryzyka wpływają na priorytety testów, testy bezpieczeństwa/regresji dla mitygacji, kryteria wyjścia release zaktualizowane o ryzyka czerwone.
- Integracja z Change/Release/Incident/Problem: każde change request ma ocenę ryzyka; incydenty wysokie tworzą nowe ryzyka; postmortem aktualizuje rejestr.
- Narzędzia/artefakty: Risk Register (ID, opis, P/I/RAG, właściciel, akcje, daty), Risk Acceptance Log, Risk Heatmap, dashboard (BI/Observability), checklisty DoR/DoD, linkage_index.jsonl.
- Audyt i dowody: log decyzji, daty przeglądów, potwierdzenia wdrożeń mitygacji (ticket, commit, runbook), wyniki testów regresji bezpieczeństwa.
## Szybkie powiązania
- risk-tracking
- risk-report
- risk-register
- risk-assessment
- production-dashboard

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

## Standardy i compliance
### Standardy międzynarodowe
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

## RACI i role

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie dokumentu | DEV / BA | PM | BA / ARCH | OPS / SM |
| Przegląd i zatwierdzenie | PM / BA | PM | Tech Lead | OPS |
| Aktualizacja | DEV / BA | PM | BA | OPS |
| Archiwizacja | OPS | PM | BA | SM |

## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.
## Checklisty jakości

- [ ] KPI/KRI zdefiniowane, progi i trend pokazane.
- [ ] Top 10 ryzyk i top issues mają ownerów, ETA i status/dowody.
- [ ] Akceptacje mają sunset/warunki i wyróżnienia na 30/60 dni.
- [ ] Decyzje/eskalacje mają właścicieli i terminy; konsekwencje opisane.
- [ ] Release/Change gating pokazuje blokery i warunki odblokowania.
- [ ] Linki do źródeł (register/mitigation/acceptance/incident/compliance) działają; sekcje N/A uzasadnione.
- [ ] Kryteria DoR/DoD poniżej spełnione; metadane aktualne.


## Definicje robocze
- Prawdopodobieństwo (P) — subiektywny lub historyczny poziom szans wystąpienia; skala 1 (bardzo mało prawdopodobne) do 5 (pewne/≥50% w horyzoncie).
- Wpływ (I) — konsekwencja dla zakresu/czasu/kosztu/jakości/bezpieczeństwa/regulacji; skala 1 (pomijalne) do 5 (katastrofalne).
- Akceptacja ryzyka — formalna zgoda sponsora/Steering Committee na pozostawienie ryzyka z określonym terminem przeglądu i warunkami cofnięcia.
## Przykłady użycia
- Migracja do chmury: mapowanie ryzyk danych wrażliwych (lokalizacja, szyfrowanie, klucze), zależności sieciowych, cutover i rollback.
- Wprowadzenie nowego dostawcy: ocena ryzyk SLA, ciągłości usług, lock‑in, poddostawców, zgodności (SOC 2/ISO 27001), plan wyjścia.
## Ryzyka i ograniczenia
- Brak spójnej skali P/I w zespołach → ujednolicić skale i dodać przykłady progu dla każdej domeny.
- Akceptacje bez daty wygaśnięcia → wymagaj daty przeglądu, warunków cofnięcia, właściciela.
- Ryzyka bezpieczeństwa nieuwzględnione w harmonogramie → dodać bufory i warunki „no‑go” dla brakujących mitygacji krytycznych.
## Decyzje i uzasadnienia
- Wybór metodyki P×I (bez D) dla prostoty — uzasadnienie: spójność z resztą portfela; D dodawane tylko dla FMEA systemów krytycznych.
- Progi RAG: zielony ≤5/żółty 6–12/czerwony ≥15 — uzasadnienie: zgodne z ISO 27005 i stosowane w raportowaniu do zarządu.
## Powiązania z innymi dokumentami
- Risk Register — dostarcza listę ryzyk i statusów → ten plan definiuje metodę i akceptacje.
- Security/Compliance Requirements — źródło obowiązków prawnych/regulacyjnych.
- Test Strategy / Security Testing Plan — używa priorytetów z ryzyk do kolejności testów.
- Change Management Plan — wymaga oceny ryzyka dla każdego change request.
## Powiązania z sekcjami innych dokumentów
- Incident Response Plan → Lessons Learned/Postmortem → aktualizacja ryzyk czerwonych i żółtych.
- Architecture Decision Records → decyzje o kryptografii/IAM → ryzyka projektowe i bezpieczeństwa.
- Service Level Objectives → sekcja dostępności → wpływ na I (impact) i tolerancje.
## Słownik pojęć w dokumencie
- RTO/RPO — Recovery Time / Recovery Point Objective; źródło: BCP/DR standard.
- Residual Risk — ryzyko po wdrożeniu mitygacji; akceptowane formalnie przez sponsora.
- Single Point of Failure (SPOF) — element, którego awaria zatrzymuje usługę; należy zmapować i mitygować.
## Wymagane odwołania do standardów
- ISO 31000 / ISO 27005 — metodyka zarządzania ryzykiem i scoring.
- NIST SP 800‑30 — proces oceny ryzyk; uzupełnia sekcję metodyki.
- SOC 2 / ISO 27001 A.8 / PCI DSS — wymagają dowodów istnienia procesu zarządzania ryzykiem i akceptacji.
## Mapa relacji sekcja→sekcja
- Risk Appetite -> Metodyka oceny : progi RAG zależą od tolerancji.
- Metodyka oceny -> Raportowanie : heatmapa i dashboard bazują na scoringu.
- Proces reakcji -> Harmonogram : mitygacje dodają bufory i warunki „go/no‑go”.
- Raportowanie -> Eskalacja : czerwone ryzyka eskalowane do Steering Committee.
## Mapa relacji dokument→dokument
- Risk Management Plan -> Risk Register : definiuje sposób uzupełniania.
- Risk Management Plan -> Change/Release Plan : nakłada obowiązek oceny ryzyk przed wdrożeniem.
- Risk Management Plan -> Incident/Postmortem : wymusza aktualizację ryzyk po incydencie.
## Ścieżki informacji
- „Nowy vendor chmurowy” → Identyfikacja ryzyk → Kategoria vendor/TPRM → Plan mitygacji + testy dostawcy → Aktualizacja Risk Register i warunki SLA.
- „Zmiana architektury (monolit → mikroserwisy)” → Analiza techniczna → Kategoria techniczne/operacyjne → Bufory wdrożenia + testy regresji → warunki release „go/no‑go”.
- „Regulator żąda raportu” → Ryzyka regulacyjne → Raportowanie → Streszczenie top ryzyk + dowody mitygacji → Komunikacja z C‑level/regulatorem.
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

## Struktura sekcji (widoki)

- KPI/KRI: # ryzyk czerwonych/żółtych, trend, % z ownerem, % z dowodem, wygasające akceptacje.
- Top 10 ryzyk: ID, tytuł, RAG, trend, owner, ETA mitygacji, status, link do szczegółu.
- Akceptacje: lista z sunset/warunkami, kompensacje, właściciel; ostrzeżenia na ≤30/60 dni.
- Top issues (P1/P2): opis, severity, owner, ETA CAPA, wpływ na SLA/SLO.
- Decyzje/eskalacje: wymagane decyzje (go/conditional/no‑go), właściciel, termin, konsekwencje.
- Release/Change gating: releasy blokowane przez ryzyka/akceptacje; warunki odblokowania.
- Trendy: heatmapa RAG, wykres zmian liczby ryzyk/akceptacji/issues w czasie.


## Wymagane rozwinięcia

- RAG i metodyka → Risk Management Plan.
- Dane źródłowe → Risk Register/Mitigation/Acceptance, Incident/Postmortem, Compliance dashboard.
- Gating → Release/Change Plan.


## Wymagane streszczenia

- Streszczenie top 10 ryzyk i top 5 issues z decyzjami.
- Streszczenie wygasających akceptacji i warunków go/conditional/no‑go.


## Kryteria ukończenia (DoD)

- Widoki exec uzupełnione (KPI/KRI, top ryzyka/issues, akceptacje, decyzje, gating).
- Alerty/sygnalizacje (sunset, blokery) opisane; linki do źródeł działają.
- Publikacja/odświeżanie (cadence, kanał, format) określone.
- Metadane aktualne; sekcje N/A uzasadnione.


## Kryteria wejścia (DoR)

- Aktualne dane w Risk Register/Mitigation/Acceptance i Incident/Postmortem.
- Uzgodnione KPI/KRI i progi z C‑level/Steering.
- Ustalony source of truth i kanał publikacji dashboardu.
