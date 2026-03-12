---
title: Risk Management Architecture
status: needs_content
aligned: true
aligned_rev: 2
aligned_at: 2026-02-09
aligned_by: codex
---

# Risk Management Architecture

## Metadane
- Właściciel: Solution Architect
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


> Powiązania: linkage_index.jsonl

## Cel dokumentu
Opisać architekturę procesów, danych i narzędzi do zarządzania ryzykiem: źródła prawdy (DB/CSV/BI), przepływy danych, integracje z systemami Change/Release/CI/CD/Monitoring/SIEM/ITSM, kontrola dostępu i audyt. Zapewnić, że scoring, rejestr, mitygacje, akceptacje i raportowanie są spójne i automatyzowalne.

## Zakres i granice
- Obejmuje: komponenty architektury (źródła danych, ETL, repo rejestru, dashboardy/heatmapy, automaty), modele uprawnień (RBAC/ABAC), integracje (Change/Release, Issue tracker, CI/CD, SIEM, CMDB, TPRM), ścieżkę audytu.
- Poza zakresem: szczegółowe wpisy ryzyk (Risk Register), plan działań (Risk Mitigation), bieżący status (Risk Mitigation Status) — tu skupiamy się na strukturze i przepływach.

## Wejścia i wyjścia
- Wejścia: wymagania compliance (ISO 27001/PCI/SOC2), polityka risk appetite, katalog ryzyk, źródła danych (Issue/Incident tracker, CI/CD, SIEM, monitoring, CMDB, TPRM), potrzeby raportowe C-level/regulatora.
- Wyjścia: projekt architektury danych i procesów, mapy integracji, model uprawnień, wymagania niefunkcjonalne (RPO/RTO dla rejestru), plan audytu/logowania, wymagania dla dashboardów/heatmap.

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
- Kontekst i cele architektury (compliance, automatyzacja, single source of truth).
- Komponenty i przepływy:
  - Źródło prawdy dla rejestru (DB/CSV/git) + wersjonowanie.
  - Integracje: Change/Release (gating), Issue/Incident tracker, CI/CD (quality gates), SIEM/monitoring (sygnały wczesne), CMDB (asset->risk), TPRM (vendor SLA).
  - ETL/ELT: import/normalizacja z wielu źródeł, deduplikacja, mapping ID.
  - Dashboard/heatmap: BI/Observability; aktualność danych, SLA na odświeżanie.
  - Evidence store: repo testów/scanów/runbooków/DR drills, powiązania z ryzykiem.
  - Notification/alerting: przypomnienia o przeglądach, sunset akceptacji, brak dowodów.
- Model uprawnień i bezpieczeństwo:
  - RBAC/ABAC dla edycji/odczytu; separacja duties (owner vs approver vs auditor).
  - Szyfrowanie danych, backupy, RPO/RTO dla rejestru; logowanie dostępu/zmian.
  - Tagowanie wrażliwych wpisów (security/privacy/regulatory) + maskowanie.
- Jakość danych i audyt:
  - Walidacje: wymagane pola (owner, RAG, sunset), spójność ID/linków, aktualność.
  - Audyt zmian: kto/kiedy/co; ślad do Change/Release/Test Evidence.
  - Metryki jakości: % brakujących ownerów, % wpisów po SLA aktualności, drift między źródłami.
- Niefunkcjonalne:
  - Skalowalność (wolumen wpisów/połączeń), dostępność (SLO dla dashboardu), opóźnienie danych.
  - Backup/restore, DR/BCP dla rejestru i evidence store.
- Operacje i utrzymanie:
  - Proces deploy/upgrade narzędzi risk (DB/BI/ETL), monitorowanie health, runbooki awaryjne.
  - Onboarding użytkowników, szkolenia, uprawnienia czasowe.

## Wymagane rozwinięcia
- Wymagania compliance → ISO 27001, SOC 2, PCI DSS, ISO 31000/27005.
- Gating w CI/CD/Release → DevSecOps/Change Management Plan.
- Dane z SIEM/monitoringu → Observability / Incident Response.
- Evidence store → Test Strategy / Security Testing / DR drills.

## Wymagane streszczenia
- Streszczenie architektury (diagram + opis przepływów) dla C-level/audytu.
- Streszczenie modelu uprawnień i kontroli dostępu.

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
- **IEEE 1016** — Standard dla Opisów Projektowania Oprogramowania (SDD)
- **IEEE 42010** — Opis Architektoniczny Systemów i Oprogramowania
- **ISO/IEC 15288** — Procesy Cyklu Życia Systemów
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **TOGAF ADM** — Framework Architektury Korporacyjnej (The Open Group)

> Sekcja generowana automatycznie. Zweryfikuj trafność i uzupełnij o dodatkowe normy/regulacje specyficzne dla kontekstu projektu.
## Jak używać dokumentu
- Przeczytaj sekcje "Cel dokumentu" i "Zakres i granice" i upewnij się, że opisują Twój przypadek.
- Wypełniaj kolejne sekcje zgodnie z guidance i powiązaniami; korzystaj z kryteriów DoR/DoD w `reports/checklist_atomic.jsonl`.
- Aktualizuj statusy w checklistach (structure/clarity/links, DoR/DoD), gdy sekcje są gotowe lub oznaczone jako N/A.


## Checklisty jakości
- [ ] Źródło prawdy i wersjonowanie rejestru opisane; backup/RPO/RTO podane.
- [ ] Integracje (Change/Release/CI-CD/Issue/Incident/SIEM/TPRM/CMDB) zmapowane z ID/linkami.
- [ ] Model uprawnień (RBAC/ABAC), audyt dostępu i zmian opisane.
- [ ] Evidence store i linki do dowodów (testy/scan/runbook/DR drill) wskazane.
- [ ] Walidacje jakości danych i metryki (aktualność, owner, sunset) zdefiniowane.
- [ ] Alerting na wygasające akceptacje/brak dowodów/brak ownera opisane.
- [ ] DR/BCP dla rejestru i dashboardów określone.
- [ ] Kryteria DoR/DoD poniżej spełnione; metadane aktualne.

## Definicje robocze
- Source of Truth — repo/DB uznane za jedyne wiążące dla wpisów ryzyka.
- Evidence Store — miejsce przechowywania dowodów kontroli/mitygacji (raporty testów, logi, ticket).
- Heatmapa — wizualizacja ryzyk wg P/I (i D), aktualizowana automatycznie z rejestru.

## Przykłady użycia
- Program chmurowy: rejestr w DB + automatyczny import z CI/CD (quality gates), SIEM (P1/P2 alerts) i Issue tracker; dashboard w BI aktualizowany co 4h; alerty o sunset akceptacji.
- Platforma SaaS: CMDB → mapowanie usług do ryzyk SLA; Release gating korzysta z RAG i statusu mitygacji; evidence store w repo artefaktów testów.

## Ryzyka i ograniczenia
- Rozjazd danych między narzędziami → wymaga ETL/normalizacji i walidacji ID/linków.
- Brak backupu lub słaby RPO rejestru → ryzyko utraty historii audytu.
- Nadmierne uprawnienia edycji → wprowadzić RBAC i ścieżkę zatwierdzeń.

## Decyzje i uzasadnienia
- Wybór jednego źródła prawdy (DB) + eksporty do BI — minimalizuje rozjazdy i dublowanie.
- Automatyczne przypomnienia/alerty (sunset, brak dowodów) — redukują ryzyko „zapomnianych” akceptacji.

## Założenia
- Istnieje dostęp do systemów źródłowych (Issue/Incident, CI/CD, SIEM, CMDB, TPRM).
- Zespół ma zasoby na utrzymanie ETL/BI i kontroli uprawnień.

## Otwarte pytania
- Jaki SLA na odświeżanie dashboardu (np. co 4h/24h)?
- Czy evidence store ma być w jednym repo (git/DB) czy rozproszone + indeks?

## Powiązania z innymi dokumentami
- Risk Management Plan — metodyka i tolerancje.
- Risk Register — dane podstawowe; to architektura ich przechowywania/przepływu.
- Risk Mitigation Plan/Status — źródło statusów i dowodów mitygacji.
- Risk Acceptance Log — akceptacje z sunset; wymagają alertów/odświeżania.
- Change/Release Plan — gating na podstawie ryzyk.
- Incident/Postmortem — zasila dane źródłowe (issues, CAPA).
- Test Strategy / Security Testing Plan — evidence store.

## Powiązania z sekcjami innych dokumentów
- Incident Response → Lessons Learned → update rejestru i heatmap.
- Observability/Monitoring → sygnały wczesne do risk scoringu (trend).
- CMDB → mapping asset→risk; Change Management → gating releasów.

## Słownik pojęć w dokumencie
- RTO/RPO — Recovery Time / Recovery Point Objective; źródło: BCP/DR standard.
- Residual Risk — ryzyko po wdrożeniu mitygacji; akceptowane formalnie przez sponsora.
- Single Point of Failure (SPOF) — element, którego awaria zatrzymuje usługę; należy zmapować i mitygować.
## Wymagane odwołania do standardów
- ISO 31000 / ISO 27005 — proces i metryki.
- SOC 2 / ISO 27001 — kontrola dostępu, audyt, dowody.
- PCI DSS — logowanie, integralność danych, audyt zmian.

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
- **Solution / Enterprise Architect** — projektuje i zatwierdza architekturę
- **Tech Lead** — odpowiada za spójność techniczną implementacji
- **Product Owner** — definiuje wymagania biznesowe wchodzące na wejście
- **Development Team** — implementuje na podstawie projektu

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
