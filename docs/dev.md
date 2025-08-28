# Development


## Stack
- **FastAPI** for HTTP & templating glue (Jinja)
- **HTMX** for server-driven updates (partial swap)
- **Tailwind (CDN)** for styling
- **uv** for dependency + venv management


## Data Model (mock)
- `INDUSTRIES: list[str]`
- `COUNTRIES: list[{ code: str, name: str }]`
- `MOCK_THREATS: list[{ id, name, type, risk, industries, countries, description }]`

## Add a New Threat

Edit app/data.py → MOCK_THREATS list.
Optionally expand the scoring logic or filters.