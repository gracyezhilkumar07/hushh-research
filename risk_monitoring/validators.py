def validate_risk_data(data):

    required_fields = [
        "trust_score",
        "policy_compliant"
    ]

    for field in required_fields:

        if field not in data:
            return False

    return True