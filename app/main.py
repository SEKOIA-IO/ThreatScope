from app.data import COUNTRIES, INDUSTRIES, query_threats
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="ThreatScope Application",
    description="API for ThreatScope",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "industries": INDUSTRIES,
            "countries": COUNTRIES,
        },
    )

@app.post("/threats", response_class=HTMLResponse)
async def threats(
    request: Request,
    industry: str = Form(...),
    countries: list[str] = Form([]),
    type_filter: str = Form("All"),
    risk_filter: str = Form("All"),
):
    items = query_threats(industry, countries, type_filter, risk_filter)
    return templates.TemplateResponse(
        "components/threat_cards.html",
        {
            "request": request,
            "items": items,
            "industry": industry,
            "countries": countries,
        },
    )