from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.data import COUNTRIES, INDUSTRIES, THREATS, THREATS_BY_ID, query_threats
from app.models import ListCountriesResponse, ListIndustriesResponse, ListThreatsResponse, QueryRequest, ThreatItem, User, UserInDB
from app.security import USER_DB, oauth2_scheme


api_router = APIRouter()

@api_router.get("/countries")
async def get_countries() -> ListCountriesResponse:
    """
    Get a list of countries.
    """
    return {"countries": COUNTRIES}

@api_router.get("/industries")
async def get_industries() -> ListIndustriesResponse:
    """
    Get a list of industries.
    """
    return {"industries": INDUSTRIES}

@api_router.get("/threats")
async def get_threats() -> ListThreatsResponse:
    """
    Get a list of threats.
    """
    return {"threats": THREATS}

@api_router.get("/threats/{threat_id}")
async def get_threat(threat_id: str) -> ThreatItem:
    """
    Get a specific threat by ID.
    """

    if threat_id not in THREATS_BY_ID:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return THREATS_BY_ID.get(threat_id)


@api_router.post("/threats/query")
async def query_threats_lite(
    payload: QueryRequest,
    token: str = Depends(oauth2_scheme)
):
    """
    This endpoint queries threats based on various filters.
    Requires authentification.
    """

    industry = payload.industry
    countries: list[str] = payload.countries
    type_filter: str | None = payload.type_filter
    risk_filter: str | None = payload.risk_filter

    items = query_threats(industry, countries, type_filter, risk_filter)
    return {"items": items}


