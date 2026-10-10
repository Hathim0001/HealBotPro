# Backend Tests

Run with:

`ash
cd backend
pip install pytest httpx
pytest tests/ -v
`

## Test Coverage

| Test | Endpoint | Description |
|------|----------|-------------|
| 	est_health_check | GET / | Verifies the server starts and returns ok |
| 	est_debug_pdf_endpoint | GET /debug/pdf | Checks PyPDF2 import |
| 	est_intake_turn_missing_body | POST /intake/turn | Expects 422 on empty body |
| 	est_consult_missing_body | POST /consult | Expects 422 on empty body |
