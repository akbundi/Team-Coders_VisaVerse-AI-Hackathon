def calculate_confidence_score(request) -> float:
    """
    AI Confidence Score based on input strength (0.0 – 1.0)
    """

    profile_completeness = 1.0 if request.nationality and request.purpose else 0.5
    print("profile completeness",profile_completeness)

    purpose_clarity = {
        "Job": 1.0,
        "Study": 0.9,
        "Dependent": 0.8,
        "Freelance": 0.6
    }.get(request.purpose, 0.5)

    document_readiness = 1.0 if request.job_role and request.salary_range else 0.5

    print("document readiness",document_readiness)

    timeline_feasibility = {
        "Flexible": 1.0,
        "Urgent": 1.0
    }.get(request.timeline, 0.6)

    input_consistency = 1.0
    if request.purpose == "Job" and request.employer_sponsorship == "No":
        input_consistency = 0.7

    weights = {
        "profile": 0.25,
        "purpose": 0.20,
        "documents": 0.20,
        "timeline": 0.20,
        "consistency": 0.15
    }

    score = (
        weights["profile"] * profile_completeness +
        weights["purpose"] * purpose_clarity +
        weights["documents"] * document_readiness +
        weights["timeline"] * timeline_feasibility +
        weights["consistency"] * input_consistency
    )

    print("score",score)
    return round(min(max(score, 0), 1), 2)
