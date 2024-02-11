"""Main api module."""
from fastapi import FastAPI

from src.models import UserInput
from src.openai_client import get_plan as openai_get_plan
from src.openai_client.openai_client import get_user_message

app = FastAPI()


@app.get("/")
async def get():
    """GET /"""
    return {"service": "ai-trainer-bff", "status": "ok"}


@app.post("/get-plan")
async def get_plan(user_input: UserInput):
    """POST /get-plan"""
    return {"msg": openai_get_plan(user_input)}
