def validate_analytics_data(data):

    required_fields = [
        "approved_requests",
        "rejected_requests",
        "high_risk_alerts"
    ]

    for field in required_fields:

        if field not in data:
            return False

    return True