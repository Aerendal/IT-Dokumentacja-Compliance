# IT Dokumentacja Compliance API

REST API dla biblioteki 9 023 szablonów IT z mapowaniami compliance.

## Uruchomienie

### Lokalnie (development)
```bash
# Z katalogu projektu (dokumentacja/)
./scripts/api/start_server.sh --reload

# Lub bezpośrednio:
IT_DOC_API_TOKEN=my-secret uvicorn scripts.api.main:app --reload
```

### Produkcja (systemd)
```bash
# Skopiuj unit file
sudo cp systemd/it-doc-api.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable it-doc-api
sudo systemctl start it-doc-api
```

## Endpointy

| Metoda | Ścieżka | Opis | Auth |
|--------|---------|------|------|
| GET | `/health` | Status serwera + stats DB | Nie |
| GET | `/templates` | Lista szablonów z filtrem | Nie |
| GET | `/coverage/{standard_code}` | Metryki pokrycia standardu | Nie |
| GET | `/mappings/{doc_path}` | Mapowania dla szablonu | Nie |
| GET | `/violations` | Naruszenia schematu | Nie |
| POST | `/review` | Zatwierdź/odrzuć mapowanie | Tak |

Pełna dokumentacja OpenAPI: `http://localhost:8000/docs`

## Zmienne środowiskowe

| Zmienna | Domyślnie | Opis |
|---------|-----------|------|
| `IT_DOC_DB` | `../reports/it_doc_matrix.db` | Ścieżka do bazy SQLite |
| `IT_DOC_API_TOKEN` | `change-me-before-production` | Token autoryzacji dla POST |
| `IT_DOC_HOST` | `127.0.0.1` | Adres nasłuchu |
| `IT_DOC_PORT` | `8000` | Port |

## Przykłady

```bash
# Health check
curl http://localhost:8000/health

# Szablony z ISO 27001, confidence >= 0.5
curl "http://localhost:8000/templates?standard=ISO%2FIEC%2027001&min_confidence=0.5&limit=10"

# Pokrycie NIST CSF
curl "http://localhost:8000/coverage/NIST%20CSF"

# Zatwierdzenie mapowania (wymaga tokena)
curl -X POST http://localhost:8000/review \
  -H "Authorization: Bearer my-secret" \
  -H "Content-Type: application/json" \
  -d '{"mapping_id": 123, "approved": true, "notes": "verified by expert"}'
```
