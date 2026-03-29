# Szybki start — przewodnik operacyjny IT_Dokumentacja

> **8 002 szablonów core** gotowych do wypełnienia. Ten przewodnik wskazuje, od czego zacząć w zależności od
> typu projektu, roli i kontekstu. Każda ścieżka zawiera minimalny zestaw (3–5 dokumentów) wymagany do
> uruchomienia pracy oraz rozszerzony zestaw dla pełnego pokrycia.

---

## Jak korzystać z biblioteki

1. **Wybierz ścieżkę** odpowiadającą typowi projektu (poniżej).
2. **Skopiuj** wskazane pliki `.md` z `generated_templates/core/` do swojego repozytorium.
3. **Wypełnij** każdą sekcję — pola `[Założenie 1]`, `[Ryzyko 1]` itp. to miejsca do uzupełnienia.
4. **Podlinkuj** dokument w `## Szybkie powiązania` powiązanych szablonów.
5. **Zatwierdź** zgodnie z macierzą RACI zawartą w sekcji `## RACI i role`.

> Szablon = szkielet + guidance (wskazówki co wpisać). **Nie zawiera** treści projektowych — te wpisujesz Ty.

---

## Ścieżki startowe

### Nowa aplikacja webowa / SaaS

**Minimalny zestaw (start projektu):**
1. `wizja_produktu.md` — cel, użytkownicy, zakres
2. `wymagania_funkcjonalne.md` — user stories, przypadki użycia
3. `architektura_systemu.md` — decyzje techniczne (ADR)
4. `plan_projektu.md` lub `roadmap_produktu.md` — harmonogram
5. `polityka_bezpieczenstwa.md` — podstawy security

**Rozszerzony zestaw (pre-launch):**
- `specyfikacja_api.md` — kontrakt API
- `test_plan.md` + `plan_testow_akceptacyjnych.md`
- `deployment_plan.md` + `runbook_wdrozenia.md`
- `dokumentacja_techniczna.md` (dla dev teamu)
- `polityka_prywatnosci.md` (RODO)

---

### Migracja / modernizacja systemu

**Minimalny zestaw:**
1. `analiza_luki.md` (as-is vs to-be)
2. `plan_migracji.md`
3. `architektura_docelowa.md`
4. `plan_testow_migracji.md`
5. `plan_wycofania_systemu.md` (rollback)

**Rozszerzony:**
- `inwentaryzacja_systemow.md`
- `mapowanie_danych.md`
- `plan_komunikacji.md` (stakeholders)
- `runbook_migracji.md` (krok po kroku)

---

### Wdrożenie chmury (Cloud / DevOps)

**Minimalny zestaw:**
1. `strategia_chmurowa.md`
2. `architektura_chmury.md`
3. `cloud_security_architecture.md`
4. `pipeline_cicd.md`
5. `runbook_monitorowania.md`

**Rozszerzony:**
- `polityka_kosztow_chmury.md`
- `disaster_recovery_plan.md`
- `plan_pojemnosci.md` (capacity planning)
- `konfiguracja_srodowisk.md`
- `inwentaryzacja_vm.md` / `inwentaryzacja_komponentow.md`

---

### Projekt bezpieczeństwa (Security / Compliance)

**Minimalny zestaw:**
1. `polityka_bezpieczenstwa_informacji.md`
2. `analiza_ryzyka_bezpieczenstwa.md`
3. `plan_reagowania_na_incydenty.md`
4. `polityka_kontroli_dostepu.md`
5. `rejestr_ryzyk.md`

**Rozszerzony (ISO 27001 / KSC):**
- `deklaracja_stosowania.md` (SoA)
- `plan_audytu.md`
- `polityka_klasyfikacji_danych.md`
- `plan_ciaglosci_dzialania.md` (BCP)
- `polityka_retencji_danych.md`

---

### Projekt AI / ML

**Minimalny zestaw:**
1. `wizja_ai.md` lub `ai_strategy.md`
2. `specyfikacja_modelu.md`
3. `data_governance_policy.md`
4. `ai_ethics_guidelines.md`
5. `model_evaluation_plan.md`

**Rozszerzony:**
- `mlops_strategy.md`
- `data_quality_framework.md`
- `ai_risk_assessment.md`
- `model_retraining_procedure.md`
- `ai_governance_framework.md`

---

### Projekt integracyjny (API / Middleware)

**Minimalny zestaw:**
1. `specyfikacja_api.md`
2. `architektura_integracji.md`
3. `umowa_poziomu_uslug_sla.md`
4. `plan_testow_integracyjnych.md`
5. `instrukcja_obslugi_api.md`

**Rozszerzony:**
- `event_driven_architecture_vision.md`
- `api_security_policy.md`
- `api_versioning_strategy.md`
- `api_gateway_deployment_plan.md`

---

### Projekt regulacyjny / Compliance (RODO, KSC, NIS2)

**Minimalny zestaw:**
1. `polityka_ochrony_danych_osobowych.md`
2. `rejestr_czynnosci_przetwarzania.md` (RCP / RoPA)
3. `analiza_ryzyka_danych.md` (DPIA)
4. `procedury_zglaszania_naruszen.md`
5. `umowy_powierzenia_przetwarzania.md`

**Rozszerzony:**
- `polityka_retencji_danych.md`
- `procedury_realizacji_praw_podmiotow.md`
- `ocena_skutkow_ksc.md`
- `plan_audytu_compliance.md`

---

## Szybka mapa po roli

| Rola | Kluczowe szablony do wypełnienia | Typowe sekcje do aktualizacji |
|------|----------------------------------|-------------------------------|
| **PM / Scrum Master** | plan_projektu, roadmap, plan_komunikacji, rejestr_ryzyk | Harmonogram, RACI, Ryzyka |
| **Architekt / Tech Lead** | architektura_systemu, ADR, specyfikacja_techniczna | Decyzje architektoniczne, Komponenty |
| **Developer** | specyfikacja_api, dokumentacja_kodu, przewodnik_wdrozenia | Struktura sekcji, Przykłady użycia |
| **QA / Tester** | test_plan, przypadki_testowe, raport_z_testow | Przypadki testowe, Kryteria akceptacji |
| **DevOps / SRE** | runbook, deployment_plan, plan_monitorowania, disaster_recovery | Kroki wykonania, Rollback |
| **Security** | polityka_bezpieczenstwa, analiza_ryzyka, plan_reagowania | Ryzyka, Standardy, Kontrole |
| **BA / Product Owner** | wymagania_funkcjonalne, user_stories, specyfikacja_ekranow | Użytkownicy, Zakres, Przypadki użycia |
| **Compliance / DPO** | polityka_danych_osobowych, DPIA, RCP, umowy_powierzenia | Podstawy prawne, Retencja, RACI |

---

## Wskazówki operacyjne

### Wypełnianie szablonu
```
[Założenie 1 — ...]  → wpisz swoje założenie, np. "System będzie dostępny 24/7"
[Ryzyko 1 — ...]     → opisz ryzyko, prawdopodobieństwo, mitygację
[Decyzja 1 — ...]    → ADR: co zdecydowano, dlaczego, jakie alternatywy odrzucono
[rola]               → konkretna osoba lub stanowisko, np. "Tech Lead - Jan Kowalski"
```

### Struktura powiązań
Każdy szablon ma sekcję `## Szybkie powiązania` z powiązanymi dokumentami.
Uzupełnij ją linkami do realnych plików w swoim repozytorium:
```markdown
## Szybkie powiązania
- [Architektura systemu](./architektura_systemu.md)
- [Plan testów](./test_plan.md)
- [ADR-001: Wybór bazy danych](./adr_001_baza_danych.md)
```

### Cykl życia dokumentu
```
Roboczy → Przegląd → Zatwierdzony → Aktywny → Zdezaktualizowany → Archiwalny
```
Aktualizuj pole `status:` w sekcji `## Metadane` przy każdej zmianie stanu.

### Wyszukiwanie szablonu
```bash
# Po nazwie (PL)
ls generated_templates/core/ | grep -i "polityka"

# Po tematyce (zawartość)
grep -rl "ISO/IEC 27001" generated_templates/core/ | head -20

# Przez narzędzie wizard
python3 scripts/new_template_wizard.py
```

---

## Narzędzia pomocnicze

| Skrypt | Do czego służy |
|--------|----------------|
| `scripts/new_template_wizard.py` | Tworzenie nowego szablonu przez interaktywny kreator |
| `scripts/maintenance/impact_analyzer.py` | Jakie szablony dotyka zmiana regulacji/standardu |
| `scripts/maintenance/bulk_section_patcher.py` | Masowe aktualizacje sekcji (np. po nowelizacji prawa) |
| `scripts/maintenance/regulation_updater.py` | Dodanie nowej regulacji + auto-propagacja |
| `scripts/maintenance/template_auditor.py` | Ocena jakości szablonów (score 0–100) |
| `scripts/maintenance/changelog_tracker.py` | Historia zmian per szablon |
| `scripts/pipeline_run.py` | Walidacja całej biblioteki (hard gate: zero emoji) |

---

*Publiczna biblioteka core templates: 8 002 szablony. Ostatnia aktualizacja: 2026-03-29.*
*Docs: `TEMPLATE_HOWTO.md` (tworzenie) · `MAINTENANCE_HOWTO.md` (utrzymanie) · `AGENT.md` (historia)*
