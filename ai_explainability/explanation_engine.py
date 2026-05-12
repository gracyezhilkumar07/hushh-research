from confidence_analyzer import calculate_confidence
from reasoning_tracker import generate_reasons


def explain_decision(data):

    confidence = calculate_confidence(data)

    reasons = generate_reasons(data)

    decision = "approved"

    if confidence < 50:
        decision = "rejected"

    return {
        "decision": decision,
        "confidence": confidence,
        "reasons": reasons
    }