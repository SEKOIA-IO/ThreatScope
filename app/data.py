from typing import List, Dict


INDUSTRIES: List[str] = [
    "Finance",
    "Healthcare",
    "Manufacturing",
    "Energy",
    "Government",
    "Retail",
    "Technology"
]

COUNTRIES: List[Dict[str, str]] = [
    {"code": "FR", "name": "France"},
    {"code": "DE", "name": "Germany"},
    {"code": "ES", "name": "Spain"},
    {"code": "IT", "name": "Italy"},
    {"code": "GB", "name": "United Kingdom"},
    {"code": "US", "name": "United States"},
    {"code": "CA", "name": "Canada"},
    {"code": "BR", "name": "Brazil"},
    {"code": "JP", "name": "Japan"},
]

MOCK_THREATS = [
    {
        "id": "apt29",
        "name": "APT29",
        "type": "Threat Actor",
        "risk": "High",
        "industries": ["Government", "Healthcare", "Energy"],
        "countries": ["FR", "DE", "GB", "US"],
        "description": "Suspected nation-state espionage group targeting public sector and critical infrastructure."
    },
    {
        "id": "lockbit",
        "name": "LockBit",
        "type": "Ransomware",
        "risk": "High",
        "industries": ["Manufacturing", "Retail", "Healthcare", "Technology"],
        "countries": ["FR", "DE", "IT", "ES", "US", "CA"],
        "description": "Ransomware-as-a-Service with affiliate double-extortion frameworks"
    },
]

RISK_RANK = {"High": 3, "Medium": 2, "Low": 1}

def score_threat(threat, industry: str, countries: List[str]) -> int:
    score = 0
    if industry and industry in threat["industries"]:
        score += 2 
    overlap = len([c for c in countries if c in threat["countries"]])
    score += overlap
    return score




def query_threats(industry: str, countries: List[str], type_filter: str = "All", risk_filter: str = "All"):
    scored = []
    for t in MOCK_THREATS:
        s = score_threat(t, industry, countries)
        if s <= 0:
            continue
        if type_filter != "All" and t["type"] != type_filter:
            continue
        if risk_filter != "All" and t["risk"] != risk_filter:
            continue
        scored.append({**t, "score": s})


    scored.sort(key=lambda x: (x["score"], RISK_RANK[x["risk"]]), reverse=True)
    return scored[:8]