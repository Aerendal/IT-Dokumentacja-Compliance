---
title: Raport compliance IAM
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Raport compliance IAM


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Raportować zgodność systemu IAM z politykami/regulacjami: MFA, polityki haseł, JML, SoD, recertyfikacje, logi/audyt, niezgodności i plan naprawczy.


## Zakres i granice

- Obejmuje: systemy IAM/IdP/SSO, konta/role/uprawnienia, dane objęte regulacjami, kontrole IAM (MFA, password policy, lifecycle JML, SoD, recertyfikacje), logi/audyt, niezgodności/waivery, metryki i plan działań.  
- Poza zakresem: projekt nowej architektury IAM (oddzielny dokument).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: polityki IAM/SoD, wymagania regulatora/klienta, raporty skanów/konfiguracji, logi IAM/IdP, recertyfikacje, wyniki audytów/testów, risk register.  
- Wyjścia: status RAG kontrolek IAM, lista niezgodności/waiverów z sunset, plan naprawczy (owner/ETA), metryki (MFA coverage, JML SLA, recerty coverage), decyzje go/conditional/no‑go.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: access_control_goals, access_control_matrix_design/reference, role_based_access_control_rbac_design, multi_factor_authentication_design, access_control_testing, compliance_with_regulations, compliance_verification, risk_register, change_management_plan, logging_and_audit_trail.
- Key Document Structures: zakres IAM, kontrole, logi/audyt, niezgodności, metryki, plan działań.
- Document Dependencies: IdP/SSO/IAM logi, recertyfikacje, SoD rules, ticketing/GRC, SIEM, CMDB/HRIS (JML).



## Zależności dokumentu
- Upstream: systemy źródłowe, dane referencyjne, decyzje architektoniczne nadrzędne.
- Downstream: konsumpcja rezultatów (zespoły, usługi, dokumenty pokrewne).
- Zewnętrzne: dostawcy, standardy branżowe, umowy/regulacje wpływające na zakres.
## Fazy cyklu życia
- Zbieranie danych i walidacja.
- Analiza i interpretacja.
- Rekomendacje i plan działań.
- Follow-up i przegląd wyników.
## Struktura sekcji (szkielet)
- Zakres raportu i okres
- Definicje metryk/KPI i źródła danych
- Wyniki z trendami i wizualizacjami
- Insighty i obserwacje
- Ryzyka/odchylenia i ich wpływ
- Rekomendacje i plan działań z właścicielami
- Załączniki/metodologia
## Szybkie powiązania

- linkage_index.jsonl (compliance/iam_report)
- access_control_goals, access_control_matrix_design/reference, rbac_design, mfa_design, access_control_testing, compliance_with_regulations, compliance_verification, risk_register, change_management_plan, logging_and_audit_trail


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


Macierz RACI (Responsible / Accountable / Consulted / Informed) dla działań związanych z tym dokumentem.

| Działanie | Responsible | Accountable | Consulted | Informed |
|-----------|-------------|-------------|-----------|----------|
| Tworzenie | [rola]      | [rola]      | [rola]    | [rola]   |
| Przegląd  | [rola]      | [rola]      | [rola]    | [rola]   |
| Aktualizacja | [rola]   | [rola]      | [rola]    | [rola]   |
| Archiwizacja | [rola]   | [rola]      | [rola]    | [rola]   |

## Jak używać dokumentu

1. Uzupełnij zakres i kontrole IAM; wstaw wyniki/metryki.  
2. Zapisz niezgodności/waivery i plan działań; ustaw retesty.  
3. Przygotuj raport dla kierownictwa/audytu; zaktualizuj linkage_index/checklisty.


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

- [ ] Każda kontrola ma dowód, status, ownera; metryki aktualne.  
- [ ] Niezgodności mają plan/ETA; waivery mają sunset; dokument w linkage_index.


## Lista kontrolna spójności relacji

- [ ] Czy każda sekcja z relacją ma wskazaną sekcję źródłową?
- [ ] Czy relacje nie tworzą sprzecznych wymagań?
- [ ] Czy wszystkie wymagane standardy mają odwołania?
- [ ] Czy RACI jest kompletne dla kluczowych działań?

## Artefakty powiązane

- Raporty skanów/konfig, logi IAM/IdP/SIEM, recert report, SoD rules, waiver log, action plan, ADR log.


## Ścieżka decyzji

- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje dla dokumentu i systemu]
- [Decyzja] -> [Uzasadnienie] -> [Konsekwencje]

## Ścieżka akceptacji

- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status: oczekuje/zatwierdzone/odrzucone]
- [Rola zatwierdząca] -> [kryteria akceptacji] -> [status]

## Metryki jakości

- MFA coverage, JML timeliness, recert coverage, liczba SoD violations, czas zamknięcia niezgodności, liczba waiverów i czas sunset, kompletność logów.

## Kryteria ukończenia

- [ ] Raport aktualny, plan działań ustawiony, metryki wypełnione; wersja/data/właściciel aktualne.


## Struktura sekcji

1) Zakres (systemy, konta/role, dane objęte regulacjami)  
2) Kontrole IAM (MFA, password policy, JML, SoD, recertyfikacje, least privilege)  
3) Logi i audyt (co, gdzie, retencja, dostęp, integracja SIEM)  
4) Niezgodności i waivery (sunset, kompensacje)  
5) Metryki i status (MFA %, JML SLA, recert coverage, SoD exceptions)  
6) Plan działań (owner, ETA, priorytet, decyzje go/conditional/no‑go)  
7) Załączniki (raporty skanów/konfig, logi, SoD rules, waiver log)


## Wymagane rozwinięcia

- Tabela kontrolek z wynikami, dowodami i właścicielami; kryteria RAG.  
- Lista niezgodności/waiverów z sunset; plan remediacji i retesty.  
- Metryki: MFA coverage, JML timeliness, recert coverage, SoD violations, audyt log completeness.


## Wymagane streszczenia

- Executive: status RAG, top niezgodności/waivery, plan działań i ETA, metryki IAM.


## Guidance (skrót)

- Brak dowodu = niezgodność; status na podstawie logów/skanów/audytu.  
- SoD i recertyfikacje muszą mieć dowody; JML SLA mierz w dniach/godzinach.  
- Waivery z sunset; aktualizuj risk register; retesty po remediacji.


## Checklisty Definition of Ready (DoR)

- [ ] Polityki IAM/SoD i wymagania regulatora dostępne; logi/skany dostępne.  
- [ ] Właściciele kontrolek i dane metryk (MFA/JML/recerts) zebrane.


## Checklisty Definition of Done (DoD)

- [ ] Kontrole ocenione; metryki wpisane; niezgodności/waivery z sunset; plan działań i retesty ustawione; dokument w linkage_index; metadane aktualne.

