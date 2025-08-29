# app/main.py
from fastapi import FastAPI
from app.routers import states, commissions, cases

app = FastAPI(title="DCDRC Case Tracker")

app.include_router(states.router)
app.include_router(commissions.router)
app.include_router(cases.router)

