---
title: Multi-Factor Authentication (MFA) Requirements
status: needs_content
aligned: true
aligned_rev: 6
aligned_at: 2026-02-09
aligned_by: codex
---
# Multi-Factor Authentication (MFA) Requirements


## Metadane

- Właściciel: Product Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Zbiera wymagania funkcjonalne i niefunkcjonalne dla wdrożenia MFA: metody, polityki wymuszania, recovery, integracje, bezpieczeństwo, UX i zgodność, z jasnymi kryteriami akceptacji i ścieżką testów.


## Zakres i granice

- Obejmuje: metody MFA (TOTP/push/WebAuthn/FIDO2/SMS fallback), rejestrację i recovery, polityki (risk/role/step-up), device binding, session management, step-up dla operacji wrażliwych, integrację z IdP/SSO, logowanie/audyt, wymagania bezpieczeństwa (phishing/SIM swap), UX dostępność (offline/roaming), SLA/SLO, zgodność (PCI/PSD2/RODO).
- Poza zakresem: implementacja i architektura (w MFA Design), polityka haseł (osobny dokument).


## Użytkownicy i interesariusze
- **Product Owner** — definiuje priorytety i kryteria akceptacji
- **Business Analyst** — zbiera i analizuje wymagania od interesariuszy
- **Development Team** — szacuje i implementuje wymagania
- **UX Designer** — projektuje doświadczenie użytkownika zgodne z wymaganiami

## Wejścia i wyjścia

- Wejścia: profile użytkowników i kanały, wymagania regulatora, ryzyka (phishing/SIM swap), istniejący IdP/SSO, urządzenia, UX guidelines, logi/audyt, polityki danych.
- Wyjścia: lista wymagań z priorytetami, kryteriami akceptacji i traceability do testów/architektury, NFR/SLO, warunki recovery/step-up, lista integracji i zależności.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: multi_factor_authentication_design, access_control_policy, security_controls_reference, logging_and_audit_trail, api_security_testing, passwordless_authentication_testing.
- Dependencies: IdP/SSO, providerzy MFA (push/TOTP/WebAuthn), device management, SIEM/logi, policy-as-code, UX guidelines.


## Zależności dokumentu

- Upstream: wymagania regulatora, profil użytkowników/kanałów, IdP/SSO, risk register, UX wytyczne.
- Downstream: MFA Design/architektura, testy security/UX, rollout plan, runbooki support/recovery.
- Zewnętrzne: dostawcy IdP/MFA, regulator (PCI/PSD2), MDM/OS policies.


## Fazy cyklu życia

- Elicytacja (scenariusze, persony, regulacje, ryzyka).
- Konsolidacja i priorytetyzacja (metody/polityki/UX).
- Walidacja z bezpieczeństwem/UX/produkt/operacje.
- Traceability do architektury/testów/rolloutu.



## Struktura sekcji (szkielet)

1) Cel i kontekst (regulacje, ryzyka, kanały/urządzenia)  
2) Wymagania funkcjonalne (metody, rejestracja, recovery, step-up, device binding, session)  
3) Wymagania niefunkcjonalne (SLO: latency, dostępność; bezpieczeństwo: phishing/SIM swap; zgodność)  
4) Integracje (IdP/SSO, push/WebAuthn/TOTP provider, SIEM/logi, device mgmt)  
5) UX i dostępność (offline/roaming, komunikaty, języki)  
6) Polityki wymuszania (risk/role-based, exception handling, BYOD)  
7) Logging/audyt i monitoring (eventy, korelacja, alerty)  
8) Kryteria akceptacji i testy (security/UX/perf, step-up, recovery, rollback)  
9) Traceability (wymaganie→test→architektura/komponent)  
10) Ryzyka i założenia; otwarte pytania  


## Szybkie powiązania

- multi-factor-authentication-design
- authentication-requirements
- multi-currency-requirements
- multi-device-support-requirements
- vr-ar-requirements

## Mające zastosowanie standardy i normy


### Standardy międzynarodowe
- **CIS Controls v8** — Krytyczne Mechanizmy Bezpieczeństwa (CIS)
- **IEEE 830** — Zalecana Praktyka dla Specyfikacji Wymagań Oprogramowania (SRS)
- **ISO 9001** — System Zarządzania Jakością (QMS)
- **ISO/IEC 12207** — Procesy Cyklu Życia Oprogramowania
- **ISO/IEC 27001** — System Zarządzania Bezpieczeństwem Informacji (ISMS)
- **ISO/IEC 27002** — Wytyczne Praktyk Bezpieczeństwa Informacji
- **ISO/IEC 27005** — Zarządzanie Ryzykiem Bezpieczeństwa Informacji
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

Wypełniaj każdą sekcję zgodnie z rzeczywistym stanem dokumentowanego systemu lub projektu.
- Sekcje obowiązkowe: Cel dokumentu, Zakres i granice, Wejścia i wyjścia.
- Sekcje oznaczone [opcjonalnie] wypełnij gdy masz dane; wpisz 'Nie dotyczy' jeśli sekcja nie ma zastosowania.
- Po wypełnieniu przekaż do przeglądu zgodnie z macierzą RACI; zaktualizuj metadata (wersja, data, autor).
- Śledź zmiany przez system kontroli wersji; podlinkuj powiązane dokumenty w sekcji 'Szybkie powiązania'.

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
- Macierz metod/scenariuszy, step-up matrix, schemat integracji, polityki recovery, plan testów, wyniki testów, ADR log, rollout/rollback plan.
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

- Wymagania metod → polityki → UX/recovery → integracja → testy/akceptacja.
- Ryzyka → środki → testy bezpieczeństwa → kryteria akceptacji.


## Wymagane rozwinięcia

- Macierz wymagań metod vs scenariusze (web/mobile/admin); step-up matrix.
- Polityki recovery i exception (waivery/sunset).
- SLO/NFR (latency, dostępność, UX) i metryki; plan testów security/UX.
- Traceability do architektury/testów; lista integracji i zależności.


## Wymagane streszczenia

- Executive summary: metody/polityki, top ryzyka, SLO, kryteria akceptacji.
- One-pager: które metody, dla kogo, kiedy wymagane, recovery, kryteria testów.


## Guidance (skrót)

- DoR: ryzyka/regulacje znane; profile użytkowników/kanały; IdP/SSO i providerzy dostępni; UX wytyczne; ownerzy testów/security/UX.
- DoD: wymagania opisane z priorytetem i kryteriami akceptacji; SLO/testy zdefiniowane; traceability do architektury/testów; ryzyka/założenia; metadane aktualne; dokument w linkage_index.
- Spójność: każda metoda ma scenariusze i recovery; step-up/recovery spójne z politykami; SLO/testy pokrywają bezpieczeństwo i UX.

