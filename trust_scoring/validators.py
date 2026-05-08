def validate_dataset(data):

    required_fields = [
        "anonymized",
        "consent_valid",
        "pii_detected",
        "audit_verified"
    ]

    for field in required_fields:

        if field not in data:
            return False

    return True