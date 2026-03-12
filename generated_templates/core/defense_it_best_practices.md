---
title: Defense IT Best Practices
status: needs_content
aligned: true
aligned_rev: 5
aligned_at: 2026-02-09
aligned_by: codex
---
# Defense IT Best Practices


## Metadane

- Właściciel: Document Owner
- Wersja: v0.2
- Data aktualizacji: RRRR-MM-DD
- Status: draft | in review | approved


## Cel dokumentu

Skonsolidować najlepsze praktyki IT w środowiskach obronnych (wojskowych/bezpieczeństwa publicznego): bezpieczeństwo, ciągłość działania, łączność o podwyższonym zaufaniu, ochrona danych niejawnych/jawnych, zgodność z normami obronnymi. Dokument prowadzi decyzje architektoniczne i operacyjne.


## Zakres i granice

- Obejmuje: segmentację sieci (air‑gap/guard), klasyfikację danych, kryptografię i zarządzanie kluczami, hardening systemów, kontrolę dostępu (RBAC/ABAC, MFA), rejestrowanie i korelację zdarzeń, łączność taktyczną i satelitarną, aktualizacje w środowiskach ograniczonych, ciągłość działania (DR/COOP), supply‑chain security, testy bezpieczeństwa.  
- Poza zakresem: taktyki operacyjne i procedury wojskowe (oddzielne SOP), polityka kadrowa i szkoleniowa.


## Użytkownicy i interesariusze
- **Product Owner / Manager** — definiuje priorytety i akceptuje wyniki
- **Technical Lead** — odpowiada za jakość techniczną i decyzje architektoniczne
- **Development Team** — implementuje i dostarcza wyniki pracy
- **QA / Reviewer** — weryfikuje jakość i poprawność dokumentu

## Wejścia i wyjścia

- Wejścia: klasyfikacja informacji (jawne/zastrzeżone/niejawne), wymagania regulacyjne (np. STANAG, NIST 800‑53/171, ISO/IEC 27001), architektura sieci, lista systemów/łączności, profile zagrożeń (APT), wyniki audytów i testów penetracyjnych.  
- Wyjścia: katalog praktyk i kontrolnych, profile bezpieczeństwa dla segmentów, wytyczne konfiguracji (baseline/hardening), wzorce łączności i szyfrowania, listy kontrolne DoR/DoD, mapa ryzyk i plan działań.


## Założenia

- Dostępne HSM/KMS i podpisy cyfrowe.  
- Zespół ma procedury dla środowisk odseparowanych.  
- Audyty bezpieczeństwa są cykliczne.


## Otwarte pytania

- Jakie są krajowe/sojusznicze ograniczenia eksportowe na kryptografię?  
- Jak weryfikować integralność aktualizacji w polu taktycznym?  
- Jak często testować łączność alternatywną (sat/tactical mesh)?  
- Jak zarządzać wyjątkami od polityk w misjach krytycznych?

## Powiązania (meta)

- Key Documents: security_controls_reference, zero_trust_vision, network_segmentation, logging_and_audit_trail, incident_response_playbook, supply_chain_security_policy.  
- Key Document Structures: segmentacja, kryptografia/klucze, tożsamość, monitoring/audyt, aktualizacje, ciągłość, dostawcy.  
- Document Dependencies: KMS/HSM, SIEM/SOAR, TACLANE/crypto devices, CMDB, patch management, SCAP/hardening skrypty, DR sites.  
- Standardy: STANAG, NIST 800‑53/171, CIS Benchmarks, ISO 27001/27019, NATO/UE relewantne polityki.


## Zależności dokumentu

Wymaga: aktualnej klasyfikacji danych, inwentarza systemów i kanałów łączności, polityki kryptograficznej, katalogu dostawców i łańcucha dostaw, wyników ostatnich testów bezpieczeństwa. Braki = brak DoR.


## Fazy cyklu życia

- Ocena zagrożeń i regulacji.  
- Projekt architektury i segmentacji.  
- Implementacja kontroli i hardeningu.  
- Operacje/monitoring i reagowanie.  
- Testy okresowe, audyty, ulepszenia.



## Struktura sekcji (szkielet)
1. Cel/zakres i Definition of Done.
2. Jakość: code review, testy, standardy codingu.
3. Bezpieczeństwo: minimalne wymagania (secrets, least privilege, dependency scanning).
4. Dokumentacja i wersjonowanie.
5. Observability: logi/metryki/trace, alerty.
6. Zmiany i release: change mgmt, rollback.
7. Komunikacja i decyzje (decision log).
## Szybkie powiązania

- linkage_index.jsonl (defense/it/best_practices)  
- security_controls_reference, supply_chain_security_policy, network_segmentation


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

1. Określ klasę systemu i dane; wybierz profil kontroli.  
2. Zaprojektuj segmentację i łączność; zdefiniuj politykę kluczy.  
3. Zastosuj hardening i monitoring; zaplanuj aktualizacje/DR.  
4. Waliduj kontrolę (testy, audyt), aktualizuj linkage_index i DoD.


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

- Air‑gap: fizyczna/logiczna izolacja sieci.  
- Guard: kontrolowany transfer danych między domenami o różnej klasyfikacji.  
- COOP: plan ciągłości działania misji.


## Przykłady użycia

- Projekt segmentacji i kontroli dla systemu dowodzenia.  
- Aktualizacje w sieci odseparowanej z podpisanymi pakietami.  
- Detekcja APT w środowisku klasyfikowanym z korelacją w SIEM.


## Ryzyka i ograniczenia

- Błędna klasyfikacja danych → ryzyko naruszenia tajemnicy.  
- Brak rotacji kluczy → kompromitacja kryptografii.  
- Zbyt szerokie uprawnienia → nadużycia/insider.  
- Aktualizacje bez walidacji → supply‑chain compromise.


## Decyzje i uzasadnienia

- Wybrane algorytmy/kryptoperiod.  
- Model segmentacji i użycie guardów.  
- Zakres i retencja logów.  
- Polityka wyjątków i akceptacji ryzyka.


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

## Powiązania sekcja↔sekcja

- Segmentacja ↔ Tożsamość/MFA ↔ Monitoring.  
- Kryptografia ↔ Zarządzanie kluczami ↔ Aktualizacje offline.  
- Dostawcy/supply chain ↔ Hardening ↔ CI/CD/DevSecOps.  
- Ciągłość/DR ↔ Łączność alternatywna ↔ Testy.


## Struktura sekcji

1) Kontekst misji i klasyfikacja danych  
2) Segmentacja i łączność (air‑gap/guard/VPN/sat/tactical)  
3) Kryptografia i zarządzanie kluczami  
4) Tożsamość i dostęp (RBAC/ABAC/MFA/PIV)  
5) Hardening, aktualizacje, supply chain  
6) Logging/monitoring/SIEM, detekcja zagrożeń  
7) Ciągłość działania i DR/COOP  
8) Ryzyka, decyzje, pytania


## Wymagane rozwinięcia

- Wzorce segmentacji (misja, administracja, gość, SCADA/OT).  
- Polityka kluczy (generacja, rotacja, przechowywanie HSM, algorytmy dopuszczone).  
- Baseline hardening (CIS/SCAP) dla OS/aplikacji/sieci.  
- Procedura aktualizacji w sieciach odseparowanych (media offline, whitelisting).  
- Matryca SoD i dostępów uprzywilejowanych.  
- Playbook detekcji APT (TTP, MITRE ATT&CK) i testy w ringu ćwiczebnym.


## Wymagane streszczenia

- Executive summary: stan kontroli, top ryzyka APT, luki krytyczne.  
- Snapshot kryptografii: algorytmy, długości kluczy, cykl rotacji.


## Guidance (skrót)

- Preferuj zero trust: weryfikuj każdy dostęp, micro‑segmentation.  
- Szyfruj wszędzie; trzymaj klucze w HSM, rotuj wg polityki.  
- Aktualizacje w środowiskach odseparowanych tylko po walidacji i podpisie.  
- Logi centralizuj, koreluj z MITRE ATT&CK, utrzymuj niezmienność.  
- Testuj DR i łączność alternatywną regularnie.  
- Weryfikuj dostawców (SBOM, podpisy, łańcuch dostaw).


## Checklisty Definition of Ready (DoR)

- [ ] Klasyfikacja danych i systemu potwierdzona.  
- [ ] Mapa sieci/segmentów i kanałów łączności dostępna.  
- [ ] Polityka kryptograficzna i KMS/HSM dostępne.  
- [ ] Lista dostawców/SBOM i wyniki testów bezpieczeństwa.  
- [ ] Właściciele systemów i SoD zidentyfikowani.


## Checklisty Definition of Done (DoD)

- [ ] Kontrole wdrożone i zweryfikowane; logi/korelacje działają.  
- [ ] Plan DR/COOP przetestowany; RPO/RTO spełnione.  
- [ ] Klucze/algorytmy zgodne z polityką; rotacja ustawiona.  
- [ ] Hardening i aktualizacje udokumentowane; wyjątki zatwierdzone.  
- [ ] linkage_index/CMDB zaktualizowane; wyniki audytu zapisane.

