from fastapi import APIRouter
from pydantic import BaseModel

from services.azure_openai import ask_mobility_ai

router = APIRouter()

# ---------- Request Schema ----------
class ChatRequest(BaseModel):
    message: str
    country: str | None = None
    nationality: str | None = None
    job: str | None = None


# ---------- Chat Endpoint ----------
@router.post("/")
def mobility_chat(request: ChatRequest):
    """
    AI chatbot endpoint for country-specific mobility questions.
    """

    context = f"""
    Destination country: {request.country}
    Nationality: {request.nationality}
    Job role: {request.job}
    """

    prompt = f"""
    You are a global mobility expert.

    Context:
    {context}

    User question:
    {request.message}

    Answer clearly and in simple language.
    """

    response = ask_mobility_ai(prompt)
    return {"reply": response}
