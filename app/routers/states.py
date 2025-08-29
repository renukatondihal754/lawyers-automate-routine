# from fastapi import APIRouter
# from app.services.jagriti_service import get_states

# router = APIRouter()

# @router.get("/states")
# def list_states():
#     return get_states()


# # app/routers/states.py
# from fastapi import APIRouter
# from app.services.jagriti_service import get_states

# router = APIRouter(prefix="/states", tags=["states"])

# @router.get("/")
# async def fetch_states():
#     states = await get_states()   # ✅ await the coroutine
#     return states


# from fastapi import APIRouter
# from app.services.jagriti_service import get_states, search_cases

# router = APIRouter()

# @router.get("/states")
# async def states():
#     return await get_states()

# @router.post("/cases")
# async def cases(payload: dict):
#     return await search_cases(payload)


# app/routers/states.py
from fastapi import APIRouter
from app.services.jagriti_service import get_states

router = APIRouter(prefix="/states", tags=["States"])

@router.get("/")
def states():
    return get_states()




