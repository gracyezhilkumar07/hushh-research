def calculate_metrics(data):

    approved = data.get("approved_requests", 0)
    rejected = data.get("rejected_requests", 0)
    alerts = data.get("high_risk_alerts", 0)

    total = approved + rejected

    approval_rate = 0

    if total > 0:
        approval_rate = (approved / total) * 100

    risk_alert_ratio = 0

    if total > 0:
        risk_alert_ratio = (alerts / total) * 100

    return {
        "approval_rate": round(approval_rate, 2),
        "risk_alert_ratio": round(risk_alert_ratio, 2)
    }