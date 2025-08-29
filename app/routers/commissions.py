# # app/routers/commissions.py
# from fastapi import APIRouter
# from app.services.jagriti_service import get_commissions

# router = APIRouter(prefix="/commissions", tags=["Commissions"])

# @router.get("/{state_id}")
# def commissions(state_id: str):
#     return get_commissions(state_id)

from fastapi import APIRouter
from typing import List
from app.models import Commission
from app.services.jagriti_service import get_commissions

router = APIRouter(prefix="/commissions", tags=["Commissions"])

@router.get("/{state_id}", response_model=List[Commission])
async def commissions(state_id: str):
    return get_commissions(state_id)


