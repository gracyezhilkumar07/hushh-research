def generate_alert(risk_level, data):

    if risk_level == "high":

        return {
            "alert_triggered": True,
            "alert_reason": "policy violation"
        }

    return {
        "alert_triggered": False
    }