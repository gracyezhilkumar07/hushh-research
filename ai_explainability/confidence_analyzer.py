def calculate_confidence(data):

    confidence = 0

    if data.get("trust_score", 0) > 80:
        confidence += 40

    if data.get("policy_compliant"):
        confidence += 30

    if data.get("consent_active"):
        confidence += 30

    return confidence