def generate_reasons(data):

    reasons = []

    if data.get("trust_score", 0) > 80:
        reasons.append("high trust score")

    if data.get("policy_compliant"):
        reasons.append("policy compliant")

    if data.get("consent_active"):
        reasons.append("active consent")

    return reasons