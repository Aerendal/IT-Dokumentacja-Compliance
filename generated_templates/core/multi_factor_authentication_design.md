---
title: Multi-Factor Authentication Design
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Multi-Factor Authentication Design


## Metadane

- Właściciel: Document Owner
- Wersja: v0.3
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved

> Powiązania: linkage_index.jsonl


## Cel dokumentu

Projektuje MFA dla systemów/klientów: metody, polityki wymuszania i recovery, UX, integrację z IdP/SSO, bezpieczeństwo i zgodność, aby podnieść ochronę kont bez nadmiernego tarcia użytkowników.


## Zakres i granice

- Obejmuje: metody MFA (TOTP/push/WebAuthn/FIDO2/SMS fallback), rejestrację i recovery, polityki wymuszania (risk/role/step-up), device binding, session management, step-up dla operacji wrażliwych, integrację z IdP/SSO, logowanie/audyt, odporność na phishing/SIM swap, dostępność (offline/roaming), komunikację użytkownika.
- Poza zakresem: pełny projekt IAM (osobny dokument), polityka haseł (w access_control_policy).


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: wymagania bezpieczeństwa/regulacyjne, profile użytkowników, kanały/urządzenia, istniejący IdP/SSO, ryzyka (phishing, SIM swap), UX wytyczne, logi/audyt, polityki danych.
- Wyjścia: wybór metod MFA, polityki wymuszania/recovery/step-up, architektura integracji z IdP/SSO, scenariusze UX, plan testów (security/UX), checklisty DoR/DoD, decyzje ADR, ryzyka i mitigacje.


## Założenia

- [Założenie 1 — co przyjmujemy za prawdziwe bez weryfikacji]
- [Założenie 2 — warunki brzegowe, które muszą być spełnione]

## Otwarte pytania

- [Pytanie 1 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]
- [Pytanie 2 — kwestia do rozstrzygnięcia, właściciel decyzji, termin]

## Powiązania (meta)

- Key Documents: access_control_policy, security_controls_reference, passwordless_authentication_testing, api_security_testing, logging_and_audit_trail, rollback_runbook, incident_response_playbook.
- Dependencies: IdP/SSO, providerzy push/TOTP/WebAuthn, device management, SIEM/logi, policy-as-code, UX guidelines.


## Zależności dokumentu

- Upstream: strategia bezpieczeństwa/IAM, wymagania regulatora (PCI/PSD2/RODO), kanały/urządzenia, IdP/SSO, UX guidelines.
- Downstream: implementacja MFA w aplikacjach, polityki enforcement, helpdesk/support runbooki, monitoring i audyt.
- Zewnętrzne: dostawcy MFA/IdP, regulatorzy (wymogi MFA/PSD2), MDM/OS policies.


## Fazy cyklu życia

- Analiza ryzyk i wymagań.
- Wybór metod i projekt UX.
- Integracja z IdP/SSO i device binding.
- Testy (security/UX), rollout i komunikacja.
- Monitoring, audyt i ulepszenia.



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

- access_control_policy, security_controls_reference, api_security_testing, logging_and_audit_trail, passwordless_authentication_testing, rollback_runbook, incident_response_playbook


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

- [ ] Metody MFA spełniają wymagania regulacyjne i ryzyka; fallbacki nie obniżają bezpieczeństwa.
- [ ] Step-up i recovery są spójne z politykami; device/session binding zgodne we wszystkich kanałach.
- [ ] Logi/alerty działają; monitoring/UEBA skonfigurowany; rollout ma plan rollback.


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

- Metody ↔ Polityki wymuszania ↔ UX/recovery.
- Device binding ↔ Session management ↔ Step-up.
- Logi/audyt ↔ Monitoring ↔ Incydenty/rollback.


## Struktura sekcji

1) Wymagania i ryzyka (regulacje, phishing/SIM swap, UX/tarcze)  
2) Wybór metod MFA i fallbacki (TOTP/push/WebAuthn/SMS, kryteria wyboru)  
3) Polityki wymuszania (risk-based, role-based, step-up dla operacji wrażliwych)  
4) UX: rejestracja, użycie, recovery (backup codes, delegated reset), komunikacja  
5) Integracja z IdP/SSO, session/device binding (tokeny, cookies, risk signals)  
6) Logging/audyt, monitoring, alerty (SIEM, anomalie, UEBA)  
7) Testy i rollout (security/UX, phishing-resistance, SIM swap, latency), DoR/DoD  
8) Ryzyka, decyzje (ADR), pytania otwarte  


## Wymagane rozwinięcia

- Macierz metod vs scenariusze (web/mobile/admin/edge cases).
- Polityki recovery (backup codes, strong verification, delegated reset).
- Step-up matrix dla operacji wrażliwych; device binding schemat.
- Schemat integracji (OpenID/FIDO2), token TTL, session management.
- Plan testów: phishing-resistance, SIM swap, UX flows, latency; rollback plan.


## Wymagane streszczenia

- Executive summary: wybrane metody, polityki, ryzyka i środki, plan rollout.
- One-pager: które metody, dla kogo, kiedy wymagane, jak odzyskać dostęp, kontakty wsparcia.


## Guidance (skrót)

- DoR: znane ryzyka i wymagania regulacyjne; profile użytkowników i kanały; IdP/SSO dostępny; UX wytyczne; ownerzy supportu/recovery.
- DoD: metody i polityki opisane; integracja z IdP/SSO gotowa; testy security/UX wykonane; monitoring/audyt skonfigurowany; plan rollout/rollback; metadane aktualne; dokument w linkage_index.
- Spójność: każda metoda ma scenariusze użycia i recovery; step-up zdefiniowany; tokeny/TTL i binding spójne; logi/alerty działają.


## Checklisty Definition of Ready (DoR)

- [ ] Ryzyka i wymagania regulacyjne zebrane; profile użytkowników/kanałów znane; IdP/SSO i providerzy MFA dostępni.
- [ ] UX wytyczne i recovery requirements zdefiniowane; ownerzy supportu/recovery ustaleni.


## Checklisty Definition of Done (DoD)

- [ ] Metody/polityki/step-up/recovery opisane; integracja z IdP/SSO przetestowana; logi/alerty i monitoring skonfigurowane.
- [ ] Plan rollout/rollback i komunikacji gotowy; testy phishing/SIM swap/UX/latency wykonane; dokument w linkage_index.

