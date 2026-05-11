def validate_consent_data(data):

    required_fields = [
        "user_id",
        "expires_at",
        "revoked"
    ]

    for field in required_fields:

        if field not in data:
            return False

    return True