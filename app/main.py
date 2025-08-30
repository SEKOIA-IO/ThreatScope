from typing import Annotated

from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.data import COUNTRIES, INDUSTRIES, query_threats
from app.api import api_router
from fastapi import FastAPI, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.models import User, UserInDB
from app.security import USER_DB, get_current_user, oauth2_scheme

app = FastAPI(
    title="ThreatScope Application",
    description="API for ThreatScope",
    version="1.0.0",
    openapi_url="/api/openapi.json",
    docs_url="/api",
)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "industries": INDUSTRIES,
            "countries": COUNTRIES,
        },
    )

@app.post("/threats", response_class=HTMLResponse, include_in_schema=False)
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

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = USER_DB.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)

    hashed_password = "fakehashed" + form_data.password
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_user)],
):
    return current_user

app.include_router(api_router, prefix="/api")