from services.azure_openai import ask_mobility_ai
from difflib import SequenceMatcher


def text_similarity(a: str, b: str) -> float:
    """
    Simple semantic proxy using string similarity.
    Output: 0.0 – 1.0
    """
    return SequenceMatcher(None, a, b).ratio()


def temperature_sensitivity_confidence(prompt: str) -> float:
    """
    Estimates AI confidence by comparing responses
    generated at different temperatures.

    Output range: 0.0 – 1.0
    """

    # Low temperature → deterministic
    response_low = ask_mobility_ai(
        prompt=prompt,
        temperature=0.2
    )

    # Higher temperature → more creative / uncertain
    response_high = ask_mobility_ai(
        prompt=prompt,
        temperature=0.7
    )

    similarity = text_similarity(response_low, response_high)

    # Similar responses → high confidence
    return round(similarity, 2)
