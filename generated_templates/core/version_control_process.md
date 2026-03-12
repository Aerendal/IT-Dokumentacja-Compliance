---
title: Version Control Process
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Version Control Process


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Ustalić spójny proces kontroli wersji (git) dla kodu, konfiguracji i dokumentacji: branch model, review, release tagging, polityki bezpieczeństwa i audytu, aby zapewnić jakość, traceability i szybkie delivery.


## Zakres i granice

- Obejmuje: model gałęzi (trunk/feature/release/hotfix), pull/merge request, code review, commit/PR standardy, konwencje tagów/release, polityki CI/CD, zasady ochrony branchy, podpisy/verified commits, workflow dokumentacji/infra-as-code, governance repo, backupy.  
- Poza zakresem: szczegółowe wytyczne coding style (osobne), proces zarządzania wymaganiami.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania release, polityki bezpieczeństwa, zasady CI/CD, wymogi audytu, role zespołów, repo istniejące.  
- Wyjścia: opis branch modelu, checklisty DoR/DoD PR, konwencje commit/PR/tag, zasady protekcji branchy, matryca ról, instrukcje release, audyt log, linkage_index update.


## Założenia

- Zespół używa git hosta z branch protection i CI.  
- Jest tooling do secret scanning i signed commits.  
- Dostęp do repo jest kontrolowany (MFA).


## Otwarte pytania

- Jak często rotować klucze/SSH tokens?  
- Czy wymagamy signed commits dla wszystkich repo?  
- Jakie raporty audytowe są potrzebne (SOX/ISO)?

## Powiązania (meta)

- Key Documents: change_management, rollback_runbook, release_readiness_statement, documentation_roadmap, security_controls_reference, api_versioning_maintenance.  
- Key Document Structures: branch model, PR/review, tag/release, bezpieczeństwo, audyt.  
- Document Dependencies: git hosting, CI/CD, secret scanning, code owners, backup.


## Zależności dokumentu

Wymaga: wyboru hosta git, polityk bezpieczeństwa (MFA, signed commits), zasad CI/CD, ról i code owners, wymogów audytowych/branch protection. Brak = brak DoR.


## Fazy cyklu życia

- Ustalenie modelu i polityk.  
- Wdrożenie w repo (branch protection, templates, CI).  
- Codzienne operacje PR/release.  
- Przeglądy okresowe i ulepszenia.



## Struktura sekcji (szkielet)
- Cel i zakres
- Definicje i role/RACI
- Standardy/zasady i narzędzia
- Kroki procesu / checklisty
- Kryteria jakości/DoD i wyjątki
- Komunikacja i eskalacje
- Rejestr zmian i utrzymanie
## Szybkie powiązania

- linkage_index.jsonl (version/control/process)  
- release_readiness_statement, rollback_runbook, security_controls_reference


## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **PMBOK 7** — Przewodnik po Zarządzaniu Projektami (PMI)
- **ITIL 4** — Biblioteka Infrastruktury IT (Zarządzanie Usługami)

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

1. Skonfiguruj repo zgodnie z modelami branch/protection.  
2. Twórz PR z checklistą DoR; wykonuj review i CI.  
3. Taguj release, aktualizuj changelog; wdrażaj przez CI/CD.  
4. Monitoruj przestrzeganie zasad; koryguj i aktualizuj dokument.


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

- Branch protection: reguły blokujące nieautoryzowane zmiany.  
- SemVer: MAJOR.MINOR.PATCH.  
- Code owners: osoby/grupy odpowiedzialne za review.


## Przykłady użycia

- Szybki hotfix z protekcją i rollback planem.  
- Release tygodniowy z tagiem i changelogiem.  
- Audyt dostępu do repo i reguł protekcji.


## Ryzyka i ograniczenia

- Brak protekcji → przypadkowe push/force.  
- Słabe review → regresje.  
- Brak changelog → chaos w release.  
- Brak signed commits/scan → ryzyko supply chain.


## Decyzje i uzasadnienia

- Model branch (trunk vs gitflow light).  
- Liczba wymaganych reviewerów i checków.  
- Semver i konwencje commit.  
- Polityka tagów i retencji repo.


## Powiązania z innymi dokumentami
- Incident Response Playbook, Incident Notifications, DRP/BCP, Monitoring Strategy, Change Management Plan, Risk Register, SLO.
## Powiązania z sekcjami innych dokumentów
- Monitoring → alerty/timeline; DR/BCP → reakcja; Change → przyczyny; Risk Register → wpisy; Lessons Learned → baza wiedzy.
## Słownik pojęć w dokumencie
- MTTR, SLA/SLO, Root Cause, Contributing Factors, CAPA, Waiver, Sunset, Blameless.
## Wymagane odwołania do standardów
- Polityki IR/BCP/DR; ewentualne wymogi regulatora jeśli incydent dotyczył danych/usług krytycznych.
## Mapa relacji sekcja→sekcja
- Timeline → Wpływ → Root cause → CAPA → Usprawnienia → Follow‑up.
## Mapa relacji dokument→dokument
- Postmortem → Incident Response/DR/BCP/Monitoring/Change/Risk → Lessons Learned.
## Ścieżki informacji
- Alert/logi → Timeline → Analiza → CAPA → Retest → Aktualizacja dokumentacji.
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
- Logi/metryki/trace, change log, komunikacja (status/update), runbooki, ticket CAPA, wykresy, lesson learned register.
## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości
- Czas dostarczenia postmortem, % CAPA zamkniętych w terminie, recydywa podobnych incydentów, jakość danych (logi/metryki) w raporcie, liczba waiverów i czas ich zamknięcia.
## Kryteria ukończenia
- [ ] Raport ukończony, CAPA/waivery z planem i dowodami; dokument w linkage_index.  
- [ ] Wersja/data/właściciel aktualne.
## Powiązania sekcja↔sekcja

- Branch model ↔ PR/review ↔ CI/CD ↔ Tag/release.  
- Bezpieczeństwo ↔ Signed commits/scan secrets ↔ Audyt.  
- Governance ↔ Backup/retencja ↔ Compliance.


## Struktura sekcji

1) Model gałęzi i standardy commit/PR/tag  
2) Code review (role, kryteria, SLAs)  
3) CI/CD wymagane checki i gating  
4) Bezpieczeństwo (MFA, signed commits, secret scanning, access)  
5) Release/tagging i changelog  
6) Governance i audyt (logi, retencja, backup)  
7) DoR/DoD PR i release, ryzyka, pytania


## Wymagane rozwinięcia

- Konwencje commit (np. Conventional Commits) i szablony PR.  
- Branch protection rules (required reviews/checks, status checks).  
- Tagging/semver i changelog proces.  
- Matryca ról (maintainer/reviewer/contributor).  
- Procedura hotfix i rollback.  
- Audyt: logi dostępu, retencja, backup repo.


## Wymagane streszczenia

- Executive summary: model branch i wymagane checki.  
- Skrót zasad bezpieczeństwa (MFA, signed commits).


## Guidance (skrót)

- Preferuj trunk-based lub krótkie feature branches; małe PR.  
- Wymuszaj review i automatyczne testy/linty.  
- Używaj semver i changelog; taguj release.  
- Włącz secret scanning i signed commits; ogranicz force push.  
- Dokumentuj i archiwizuj decyzje w linkage_index.  
- Regularnie przeglądaj reguły protekcji i dostępów.


## Checklisty Definition of Ready (DoR)

- [ ] PR ma opis, link do zadania, testy, checklistę.  
- [ ] Gałąź aktualna z main/trunk; brak konfliktów.  
- [ ] Secret scanning i lint/test uruchamiane.  
- [ ] Właściwi reviewerzy przypisani (code owners).  
- [ ] Kryteria bezpieczeństwa (signed commit?) spełnione.


## Checklisty Definition of Done (DoD)

- [ ] PR zmergowany po review i zielonych checkach.  
- [ ] Release otagowany; changelog zaktualizowany.  
- [ ] Brak otwartych krytycznych uwag; follow-up zapisany.  
- [ ] linkages_index i audyt (logi, protekcje) zaktualizowane.  
- [ ] W razie rollback: wykonany i udokumentowany.

