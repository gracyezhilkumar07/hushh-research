def determine_risk_level(data):

    if (
        data.get("trust_score", 100) < 50
        or not data.get("policy_compliant")
    ):
        return "high"

    return "low"