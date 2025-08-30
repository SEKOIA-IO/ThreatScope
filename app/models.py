

from pydantic import BaseModel

class Country(BaseModel):
    name: str
    code: str


class Industry(BaseModel):
    name: str

class ThreatItem(BaseModel):
    id: str
    name: str
    type: str
    risk: str
    industries: list[str]
    countries: list[str]
    description: str

class QueryRequest(BaseModel):
    industry: str
    countries: list[str]
    type_filter: str | None = "All"
    risk_filter: str | None = "All"


class ListCountriesResponse(BaseModel):
    countries: list[Country]


class ListIndustriesResponse(BaseModel):
    industries: list[Industry]


class ListThreatsResponse(BaseModel):
    threats: list[ThreatItem]

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
    