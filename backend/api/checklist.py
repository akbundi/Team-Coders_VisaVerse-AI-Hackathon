from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ChecklistRequest(BaseModel):
    country: str
    visa_type: str

@router.post("/generate")
def generate_checklist(request: ChecklistRequest):
    """
    Generate a realistic relocation checklist.
    """
    checklist = [
        {"task": "Apply for visa"},
        {"task": "Book accommodation"},
        {"task": "Open bank account"},
        {"task": "Register healthcare"},
    ]

    return {
        "country": request.country,
        "visa_type": request.visa_type,
        "checklist": checklist
    }
