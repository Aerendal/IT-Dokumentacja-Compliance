---
title: "CapabilityStatement serwera FHIR (HL7 FHIR)"
status: aktywny
aligned: HL7 FHIR
---

## Cel dokumentu
Opisać i udokumentować CapabilityStatement (Conformance Resource) serwera HL7 FHIR — formalne metadane opisujące możliwości techniczne implementacji FHIR. CapabilityStatement jest wymaganym zasobem FHIR (endpoint `/metadata`) każdego serwera FHIR R4/R5: informuje klientów o obsługiwanych typach zasobów, operacjach (read/write/search), profilach, wersjach FHIR, mechanizmach bezpieczeństwa i rozszerzeniach — umożliwiając automatyczną negocjację możliwości między systemami zdrowotnymi (interoperacyjność semantyczna).

## Zakres i granice
Dokument odnosi się do konkretnej implementacji serwera FHIR — każdy serwer FHIR w organizacji ma własny CapabilityStatement. Wersja FHIR: **[R4 / R4B / R5]**

## Wejścia i wyjścia
**Wejścia:**
- Wymagania integracyjne (które zasoby FHIR muszą być obsługiwane)
- Profile FHIR stosowane przez organizację (np. PL Core, US Core, Da Vinci)
- Wymagania bezpieczeństwa (SMART on FHIR, OAuth2, mTLS)
- Wymagania regulatora (np. ONC 21st Century Cures Act interoperability)

**Wyjścia:**
- CapabilityStatement JSON/XML publikowany na `/metadata` endpoint
- Dokumentacja możliwości serwera dla developerów aplikacji klienckich
- Podstawa do testów zgodności (FHIR Validator, HL7 TestScript)

## Informacje ogólne serwera FHIR

| Pole | Wartość |
|------|---------|
| **name** | [NazwaSerwera]CapabilityStatement |
| **title** | Możliwości serwera [Nazwa systemu] FHIR |
| **status** | active |
| **date** | [Data ostatniej aktualizacji] |
| **publisher** | [Organizacja] |
| **kind** | instance |
| **fhirVersion** | 4.0.1 / 5.0.0 |
| **format** | application/fhir+json, application/fhir+xml |

## Bezpieczeństwo

```json
"security": {
  "cors": true,
  "service": [{
    "coding": [{ "system": "http://hl7.org/fhir/restful-security-service", "code": "SMART-on-FHIR" }]
  }],
  "description": "OAuth2 SMART on FHIR authorization. Scopes: patient/*.read, user/*.* "
}
```

**Mechanizm uwierzytelnienia:** [OAuth2 / SMART on FHIR / mTLS / API Key]  
**Transport:** HTTPS (TLS 1.2+), zakaz HTTP

## Obsługiwane zasoby FHIR

| Zasób FHIR | Read | VRead | Search | Create | Update | Delete | Profile |
|-----------|------|-------|--------|--------|--------|--------|---------|
| Patient | TAK | TAK | TAK | TAK | TAK | NIE | [PL Core Patient] |
| Observation | TAK | TAK | TAK | TAK | NIE | NIE | [PL Core Observation] |
| Condition | TAK | NIE | TAK | TAK | TAK | NIE | [Standard FHIR] |
| MedicationRequest | TAK | NIE | TAK | TAK | NIE | NIE | [ePrescription PL] |
| DiagnosticReport | TAK | NIE | TAK | TAK | NIE | NIE | [Standard FHIR] |
| Bundle | TAK | NIE | NIE | TAK | NIE | NIE | transaction, batch |
| ... | | | | | | | |

## Obsługiwane operacje (Operations)

| Operacja | Poziom | Opis |
|---------|--------|------|
| $validate | Resource | Walidacja zasobu FHIR względem profilu |
| $everything | Patient | Pobieranie wszystkich danych pacjenta |
| $summary | Patient | Podsumowanie danych pacjenta (IPS) |
| $convert | System | Konwersja FHIR ↔ CDA/HL7v2 |

## Parametry wyszukiwania (Search Parameters)

**Patient:**
- `_id`, `identifier`, `family`, `given`, `birthdate`, `gender`, `address-city`

**Observation:**
- `_id`, `patient`, `code`, `date`, `category`, `status`

**MedicationRequest:**
- `_id`, `patient`, `medication`, `status`, `authoredon`

## Profile i rozszerzenia (Extensions)

| Profil / Rozszerzenie | URL | Zasób |
|----------------------|-----|-------|
| PL Core Patient | `http://hl7.pl/fhir/pl-core/StructureDefinition/Patient` | Patient |
| [Profil organizacyjny X] | [URL] | [Zasób] |

## Testowanie zgodności
- **FHIR Validator:** `java -jar validator.jar -version 4.0.1 [plik.json]`
- **Touchstone / Inferno:** automatyczne testy zgodności HL7
- **CapabilityStatement URL:** `GET [base_url]/metadata`

## Powiązania (meta)
- standardy-i-compliance: HL7 FHIR R4/R5, SMART on FHIR, ONC 21st Century Cures Act, IHE profiles
- raci-i-role: FHIR Architect (Owner), Integracja IT (Author), Audytor HL7 (Reviewer), developerzy aplikacji klienckich (Informed)
