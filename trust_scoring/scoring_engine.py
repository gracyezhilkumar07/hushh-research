def calculate_trust_score(data):

    score = 0

    if data.get("anonymized"):
        score += 30

    if data.get("consent_valid"):
        score += 30

    if not data.get("pii_detected"):
        score += 20

    if data.get("audit_verified"):
        score += 20

    return {
        "trust_score": score
    }