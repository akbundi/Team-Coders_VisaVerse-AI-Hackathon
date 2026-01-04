from fastapi import APIRouter
from pydantic import BaseModel

from services.azure_openai import ask_mobility_ai
from services.confidence_score import calculate_confidence_score
from services.temperature_confidence import temperature_sensitivity_confidence

router = APIRouter()


class VisaSummaryRequest(BaseModel):
    country: str
    nationality: str
    purpose: str  # Job / Study / Freelance / Dependent
    job_role: str | None = None
    salary_range: str | None = None
    employer_sponsorship: str | None = None  # Yes / No
    timeline: str | None = None               # Urgent / Flexible


@router.post("/summary")
def visa_summary(request: VisaSummaryRequest):
    """
    AI-powered visa & work permit guidance
    with entropy-inspired confidence scoring.
    """

    input_confidence = calculate_confidence_score(request)

    prompt = f"""
    You are a global mobility assistant.

    Destination country: {request.country}
    Nationality: {request.nationality}
    Purpose: {request.purpose}
    Job role: {request.job_role}
    Salary range: {request.salary_range}
    Employer sponsorship: {request.employer_sponsorship}
    Timeline: {request.timeline}

    Provide visa and work permit guidance in clear language.
    """

    summary = ask_mobility_ai(prompt)

    response_confidence = temperature_sensitivity_confidence(prompt)

    final_confidence = round(
        0.65 * input_confidence + 0.35 * response_confidence,
        2
    )

    return {
        "summary": summary,
        "ai_confidence_score": final_confidence,
        "confidence_breakdown": {
            "input_confidence": input_confidence,
            "response_stability": response_confidence
        },
        "confidence_explanation": (
            "This score reflects input clarity and response stability, "
            "not legal approval or immigration outcomes."
        )
    }
