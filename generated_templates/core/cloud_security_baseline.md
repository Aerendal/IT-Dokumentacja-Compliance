---
title: Cloud Security Baseline
status: draft
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Cloud Security Baseline


## Metadane

- Właściciel: Security Officer
- Wersja: v0.1
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Minimalny, wspólny zestaw wymagań bezpieczeństwa dla środowisk chmurowych (IAM, sieć, dane, obserwowalność, CI/CD, DR) spójny z normami (ISO/SOC2/PCI/NIS2) i zasadą "secure by default".


## Zakres i granice

- Obejmuje: wszystkie konta/projekty/tenanty chmurowe (prod/non-prod), zasady IAM, sieć, szyfrowanie, logowanie/monitoring, CI/CD, backup/DR, 3rd party.
- Nie obejmuje: szczegółowych runbooków usług i specyficznych wyjątków per system (definiowane lokalnie).


## Użytkownicy i interesariusze
- **CISO / Security Officer** — odpowiada za strategię bezpieczeństwa i akceptuje dokument
- **Security Engineer** — implementuje mechanizmy ochronne i przeprowadza testy
- **Compliance Officer** — weryfikuje zgodność z regulacjami (ISO 27001, RODO, NIS2)
- **DevOps / Platform Team** — wdraża zmiany infrastrukturalne wynikające z zaleceń

## Wejścia i wyjścia
- Wejścia: cele biznesowe, backlog/epiki, wymagania niefunkcjonalne, ograniczenia prawne/techniczne, istniejące systemy/dane.
- Wyjścia: zaakceptowana wersja dokumentu, decyzje architektoniczne/procesowe, action items z właścicielami i terminami.
## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)
- Wymaga odniesienia do: Key Documents
- Wymaga odniesienia do: Key Document Structures
- Wymaga odniesienia do: Document Dependencies
- Wymaga odniesienia do: RACI i role
- Wymaga odniesienia do: Standardy i compliance
## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Discovery/Analiza: doprecyzowanie problemu, interesariusze, ograniczenia.
- Projektowanie/Planowanie: decyzje, warianty, kryteria akceptacji, plan wdrożenia.
- Implementacja/Testy: realizacja, walidacja, kryteria go/no-go.
- Wdrożenie/Operacje: rollout, monitoring, eskalacje, ciągłe doskonalenie.
## Struktura sekcji (szkielet)
- Streszczenie i cele szkolenia
- Grupa docelowa i wymagania wstępne
- Moduły/agenda (IAM, sieć, KMS/sekrety, workloady, monitoring, IaC)
- Środowisko/laby i bezpieczeństwo danych
- Ćwiczenia/prace domowe i kryteria zaliczenia
- Ewaluacja (quiz/lab/egzamin), feedback i iteracje
- Plan komunikacji/mentoringu i utrzymania materiałów
## Szybkie powiązania
- cloud-security-training
- cloud-security-architecture
- security-architecture-for-cloud
- vm-security-hardening
- security-training

## Mające zastosowanie standardy i normy

### Standardy międzynarodowe
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **ISO/IEC 27017** — Bezpieczeństwo w Chmurze Obliczeniowej
- **ISO/IEC 27018** — Ochrona Danych Osobowych w Chmurze (PII)
- **SOC 2** — Kontrole Organizacji Usług (Typ I i II)

## Standardy i compliance
### Standardy międzynarodowe
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST
- **ISO/IEC 27017** — Bezpieczeństwo w Chmurze Obliczeniowej
- **ISO/IEC 27018** — Ochrona Danych Osobowych w Chmurze (PII)
- **SOC 2** — Kontrole Organizacji Usług (Typ I i II)

## RACI i role

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie dokumentu | DEV / BA | PM | BA / ARCH | OPS / SM |
| Przegląd i zatwierdzenie | PM / BA | PM | Tech Lead | OPS |
| Aktualizacja | DEV / BA | PM | BA | OPS |
| Archiwizacja | OPS | PM | BA | SM |

## Jak używać dokumentu
- Uzupełnij sylabus i wymagania, przygotuj laby/konta; sekcje N/A uzasadnij.
- Dodaj quick-links i checklisty DoR/DoD w `reports/checklist_atomic.jsonl`.
- Po pilotażu uzupełnij feedback, zaktualizuj materiały i status.
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

## Baseline (wymagania)

1. **IAM**: SSO/MFA dla ludzi, tożsamość maszynowa, RBAC/ABAC, least privilege, zakaz stałych kluczy root, rotacja sekretów/kluczy, recertyfikacje dostępu.
2. **Sieć**: segmentacja VPC/VNet, SG/NSG, WAF, egress control, prywatne ścieżki do danych/serwisów, DNS zarządzane, TLS everywhere.
3. **Dane i szyfrowanie**: klasyfikacja, szyfrowanie at-rest/in-transit, KMS/HSM, rotacja kluczy, DLP, backup/retencja, ochrona przed skasowaniem/immutable, PITR dla krytycznych DB.
4. **Obserwowalność**: centralne logi/audit, metryki/trace, SIEM/SOAR integracje, alerty SLO/SLA, wersjonowane dashboardy, retention zgodna z compliance.
5. **Compute/Containers/Serverless**: hardened images, skanowanie CVE/SBOM, patching, minimalne uprawnienia runtime, policy-as-code (OPA/Kyverno), izolacja sieci/namespace.
6. **CI/CD i IaC**: SAST/DAST/dep scan, SBOM i signing, approvals/4-eyes, policy-as-code na terraform/helm/k8s, secrets management w pipeline.
7. **DR/BCP i ciągłość**: RTO/RPO określone, multi-AZ/region wg krytyczności, testy DR, backup/restore testowane, runbooki DR.
8. **3rd party i SaaS**: due diligence, AOC/raporty, least privilege integracji, rotacja tokenów, monitoring użycia.


## Automatyzacja i egzekwowanie

- IaC/policy-as-code (guardrails), detect/deny drift, skanowanie obrazów i IaC w CI, enforcement na wejściu (pre-commit/CI/CD) i w runtime.
- Evidence: centralne zbieranie dowodów (logi, raporty skanów, recertyfikacje), cykl odświeżania.


## Wyjątki

- Proces wnioskowania o wyjątek (risk accept/waiver), czas obowiązywania, kompensacyjne kontrolki, właściciel, data przeglądu.


## Checklisty (DoR/DoD skrót)

- DoR:
  - [ ] Zakres kont/projektów i standardy odniesienia (ISO/SOC2/PCI/NIS2/CIS) potwierdzone.
  - [ ] Role ownerów domen (IAM/sieć/dane/CI-CD/DR) przydzielone; narzędzia guardrails dostępne.
  - [ ] Plan evidence/recertyfikacji i proces wyjątków zdefiniowany.
- DoD:
  - [ ] Baseline opisany w domenach IAM/sieć/dane/obs/compute/CI-CD/DR/3rd party.
  - [ ] Guardrails/automatyzacja i evidence zdefiniowane; wyjątki mają proces i wzór akceptacji.
  - [ ] Dokument wersjonowany i udostępniony; harmonogram przeglądów baselinu ustalony.


## Wymagane rozwinięcia

- Rozwija: Cloud Infrastructure Requirements, Cloud Compliance Roadmap, Logging/Monitoring standards, Secure SDLC/CI-CD, Vendor Management.


## Streszczenie

- Krótkie podsumowanie kluczowych wymagań i sposobu egzekwowania (policy-as-code + evidence + wyjątki).
