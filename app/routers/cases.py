# from fastapi import APIRouter
# from app.models import CaseSearchRequest, CaseResponse
# from app.services.jagriti_service import search_cases
# from typing import List

# router = APIRouter()

# @router.post("/cases/by-case-number", response_model=List[CaseResponse])
# def cases_by_case_number(payload: CaseSearchRequest):
#     return search_cases(payload.state, payload.commission, "case_number", payload.search_value)

# @router.post("/cases/by-complainant", response_model=List[CaseResponse])
# def cases_by_complainant(payload: CaseSearchRequest):
#     return search_cases(payload.state, payload.commission, "complainant", payload.search_value)

# @router.post("/cases/by-respondent", response_model=List[CaseResponse])
# def cases_by_respondent(payload: CaseSearchRequest):
#     return search_cases(payload.state, payload.commission, "respondent", payload.search_value)

# @router.post("/cases/by-complainant-advocate", response_model=List[CaseResponse])
# def cases_by_complainant_advocate(payload: CaseSearchRequest):
#     return search_cases(payload.state, payload.commission, "complainant_advocate", payload.search_value)

# @router.post("/cases/by-respondent-advocate", response_model=List[CaseResponse])
# def cases_by_respondent_advocate(payload: CaseSearchRequest):
#     return search_cases(payload.state, payload.commission, "respondent_advocate", payload.search_value)

# @router.post("/cases/by-industry-type", response_model=List[CaseResponse])
# def cases_by_industry(payload: CaseSearchRequest):
#     return search_cases(payload.state, payload.commission, "industry", payload.search_value)

# @router.post("/cases/by-judge", response_model=List[CaseResponse])
# def cases_by_judge(payload: CaseSearchRequest):
#     return search_cases(payload.state, payload.commission, "judge", payload.search_value)


# app/routers/cases.py
from fastapi import APIRouter
from typing import List
from app.models import Case, CaseSearchRequest
from app.services.jagriti_service import search_cases

router = APIRouter(prefix="/cases", tags=["Cases"])

def create_case_endpoint(search_field: str):
    async def endpoint(request: CaseSearchRequest) -> List[Case]:
        return search_cases(
            state_name=request.state,
            commission_name=request.commission,
            search_value=request.search_value,
            search_field=search_field
        )
    return endpoint

router.post("/by-case-number")(create_case_endpoint("case_number"))
router.post("/by-complainant")(create_case_endpoint("complainant"))
router.post("/by-respondent")(create_case_endpoint("respondent"))
router.post("/by-complainant-advocate")(create_case_endpoint("complainant_advocate"))
router.post("/by-respondent-advocate")(create_case_endpoint("respondent_advocate"))
router.post("/by-industry-type")(create_case_endpoint("industry_type"))
router.post("/by-judge")(create_case_endpoint("judge"))
