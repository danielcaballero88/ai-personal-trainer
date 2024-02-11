"""Main api module."""
from fastapi import FastAPI

from models import UserInput

app = FastAPI()


@app.get("/")
async def get():
    """GET /"""
    return {"service": "ai-trainer-bff", "status": "ok"}


@app.post("/get-plan")
async def get_plan(user_input: UserInput):
    """POST /get-plan"""
    return user_input
