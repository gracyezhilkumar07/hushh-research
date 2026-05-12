def validate_explainability_data(data):

    required_fields = [
        "trust_score",
        "policy_compliant",
        "consent_active"
    ]

    for field in required_fields:

        if field not in data:
            return False

    return True