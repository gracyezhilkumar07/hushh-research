from alert_engine import generate_alert
from escalation_manager import determine_risk_level


def monitor_risk(data):

    risk_level = determine_risk_level(data)

    alert = generate_alert(
        risk_level,
        data
    )

    return {
        "risk_level": risk_level,
        "alert": alert
    }