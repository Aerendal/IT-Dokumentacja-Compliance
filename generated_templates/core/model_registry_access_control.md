---
title: Model Registry Access Control
status: needs_content
aligned: true
aligned_rev: 4
aligned_at: 2026-02-09
aligned_by: codex
---
# Model Registry Access Control


## Metadane

- Właściciel: ML Engineer
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Definiuje zasady dostępu do rejestru modeli (Model Registry): role, uprawnienia, procesy publikacji/wersjonowania, audyt, zgodność i bezpieczeństwo artefaktów modeli. Ma chronić przed nieautoryzowanymi zmianami, wyciekami i utratą kontroli wersji.


## Zakres i granice

- Obejmuje: model lifecycle (eksperyment → staging → production), role (viewer/editor/approver/admin/robot), polityki RBAC/ABAC, repo artefaktów (weights, metadata), podpisy/attestacje, skanowanie bezpieczeństwa, zatwierdzanie i promotion, audyt/logi, integracje z CI/CD i serving, zarządzanie sekretami/kluczami, retencję i archiwizację.  
- Poza zakresem: szczegóły trenowania modeli (osobne dokumenty), specyficzne runtime’y serving (linki do runbooków).


## Użytkownicy i interesariusze
- **ML Engineer / Data Scientist** — buduje, trenuje i ewaluuje modele
- **Data Engineer** — przygotowuje dane i zarządza pipeline'ami
- **Product Owner** — definiuje metryki sukcesu i priorytety eksperymentów
- **MLOps Engineer** — zarządza wdrożeniem i monitoringiem modeli na produkcji

## Wejścia i wyjścia

- Wejścia: polityki bezpieczeństwa danych/modeli, klasyfikacja modeli (PII/regulowane), wymagania compliance (SOX/PCI/medical), struktura zespołów, narzędzia MLOps/CI/CD, wymagania audytu.  
- Wyjścia: macierz ról/uprawnień, zasady promotion i podpisów, proces zatwierdzania i publikacji, procedury skanowania, konfiguracja logowania/audytu, checklista DoR/DoD dla publikacji, powiązania z katalogiem/CMDB.


## Założenia

- Dostępne IAM/SSO, KMS/HSM, narzędzie registry zgodne z politykami.  
- CI/CD wspiera skanowanie i podpisy.  
- Zespół Security i MLOps ma proces przeglądów.


## Otwarte pytania

- Czy wymagane są certyfikacje/regulacje branżowe (med/fin)?  
- Jak obsłużyć dostęp partnerów zewnętrznych?  
- Jakie są limity retencji dla modeli/regresji?


## Powiązania (meta)

- Key Documents: ml_governance_policy, model_promotion_process, security_requirements, data_classification, supply_chain_security, change_management_request.  
- Key Document Structures: role, promotion, security/scanning, audyt/logi, integracje CI/CD, retencja.  
- Document Dependencies: registry tool (e.g., MLflow/SageMaker/Vertex), IAM/SSO, KMS/HSM, CI/CD, artifact store, monitoring, CMDB.


## Zależności dokumentu

Wymaga: klasyfikacji modeli/danych, polityk RBAC/ABAC i narzędzia IAM, decyzji o podpisach/attestacjach, integracji z CI/CD i serving, wymagań audytu/regulacji. Braki = DoR otwarte.


## Fazy cyklu życia

- Definicja polityk i ról.  
- Wdrożenie w narzędziu registry i CI/CD.  
- Operacje: publikacje/promotion, audyt, rotacje kluczy.  
- Przeglądy okresowe i aktualizacje polityk.



## Struktura sekcji (szkielet)
- Streszczenie celu i KPI
- Kontekst, założenia i ograniczenia
- Zakres oraz role/RACI
- Główne decyzje i warianty
- Proces/architektura/etapy
- Ryzyka, zależności i mitigacje
- Plan wdrożenia i kryteria akceptacji
- Monitoring i raportowanie
- Załączniki i źródła
## Szybkie powiązania

- linkage_index.jsonl (model/registry/access_control)  
- ml_governance_policy, model_promotion_process, supply_chain_security, security_requirements


## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **ISO/IEC 23053** — Framework dla Systemów AI z Uczeniem Maszynowym
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
- **ISO/IEC 42001** — System Zarządzania Sztuczną Inteligencją (AIMS)
- **NIST CSF** — Framework Cyberbezpieczeństwa NIST

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

1. Zdefiniuj role/uprawnienia i promotion gates; skonfiguruj w narzędziu registry.  
2. Włącz skanowanie/podpisy w CI/CD; ustaw logi/audyt i retencję.  
3. Dokumentuj publikacje i decyzje; aktualizuj DoR/DoD, macierz ról i linkage_index.


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

- Attestacja: podpis kryptograficzny potwierdzający integralność/pochodzenie artefaktu.  
- SBOM: lista komponentów modelu/pakietów do oceny bezpieczeństwa.  
- Promotion gate: automatyczny warunek wejścia modelu do wyższego środowiska.


## Przykłady użycia

- Rejestr modeli MLflow z promotion do prod po podpisie i skanach.  
- Dostęp tylko read dla analityków, write dla MLOps, approve dla Security.  
- Rollback do poprzedniej wersji modelu po detekcji regresji.


## Ryzyka i ograniczenia

- Nadmierne uprawnienia → ryzyko modyfikacji/wycieku modeli.  
- Brak skanów/podpisów → supply chain atak.  
- Brak audytu → trudne dochodzenie przy incydentach.


## Decyzje i uzasadnienia

- Zakres ról i rozdzielenie obowiązków (SoD).  
- Wymóg podpisów/attestacji i narzędzia skanowania.  
- Retencja logów/artefaktów vs koszt storage.


## Powiązania z innymi dokumentami

- model_promotion_process — zasady promocji.  
- supply_chain_security — skanowanie/podpisy.  
- change_management_request — formalne zatwierdzenia.


## Powiązania z sekcjami innych dokumentów

- [Dokument X → Sekcja Y] — [powód powiązania i kierunek przepływu informacji]
- [Dokument Z → Sekcja W] — [powód powiązania i kierunek przepływu informacji]

## Słownik pojęć w dokumencie

- [Pojęcie 1] — [definicja i źródło normalizacyjne lub wewnętrzne]
- [Pojęcie 2] — [definicja i źródło normalizacyjne lub wewnętrzne]

## Wymagane odwołania do standardów

- ISO 27001/SOC2, regulacje branżowe (np. med/fin), polityki RODO/PII.  
- Wewnętrzne standardy security i change management.

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

- Role/uprawnienia → Promotion → Audyt/logi.  
- Skanowanie bezpieczeństwa → Zatwierdzenie → Publikacja.  
- Integracje CI/CD → Kontrola wersji → Rollback/retencja.


## Struktura sekcji

1) Kontekst i zakres (tool, zakwalifikowanie danych/modeli)  
2) Role i uprawnienia (RBAC/ABAC, roboty techniczne)  
3) Promotion/publikacja (dev→staging→prod, approvals, podpisy/attestacje)  
4) Bezpieczeństwo i zgodność (skanowanie, SBOM, supply chain, PII/regulacje)  
5) Audyt i logowanie (kto/co/kiedy, immutable logs)  
6) Integracje z CI/CD i serving (pipelines, policy-as-code, deployment gates)  
7) Zarządzanie kluczami/secretami (KMS/HSM, rotacja, dostęp)  
8) Retencja, archiwizacja, cleanup, rollback  
9) Ryzyka, decyzje, otwarte pytania


## Wymagane rozwinięcia

- Macierz ról i uprawnień per akcja (create/register/update/publish/delete/promote/roll back).  
- Proces zatwierdzania i listy kontrolne promotion (testy, skany, podpisy).  
- Wymagania audytu i retencji logów/artefaktów.  
- Procedury reakcji na incydenty bezpieczeństwa modeli (compromise/leak).


## Wymagane streszczenia

- Executive snapshot: kto ma prawa do produkcji, kiedy ostatni audyt, status skanów/podpisów.  
- Run sheet publikacji modelu (kroki, odpowiedzialni, kryteria go/no‑go).


## Guidance (skrót)

- Least privilege na poziomie projektów/modeli; osobno ludzie i roboty.  
- Promotion blokowane bez skanów bezpieczeństwa i podpisów artefaktów.  
- Logi i audyt nieusuwalne; koreluj z CI/CD i deploymentami.  
- Ustal retencję/cleanup starych modeli, ale zachowaj rollback.  
- Aktualizuj polityki wraz ze zmianami regulacji/klasyfikacji danych.


## Checklisty Definition of Ready (DoR)

- [ ] Klasyfikacja modeli/danych i polityki RBAC/ABAC dostępne.  
- [ ] Narzędzie registry i IAM zintegrowane; KMS/HSM dostępne.  
- [ ] Proces promotion/podpisów i skanów uzgodniony.  
- [ ] Wymagania audytu/regulacji zidentyfikowane.  
- [ ] Plan retencji i cleanup ustalony.


## Checklisty Definition of Done (DoD)

- [ ] Role i uprawnienia wdrożone; least privilege potwierdzony.  
- [ ] Promotion działa z wymaganymi skanami/podpisami i logami audytu.  
- [ ] Integracje CI/CD/serving aktywne; status/wersja/data zaktualizowane.  
- [ ] Retencja/cleanup i procedury rollback opisane.  
- [ ] Raport audytu i linkage_index uzupełnione; otwarte ryzyka odnotowane.

