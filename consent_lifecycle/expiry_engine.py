from datetime import datetime


def is_consent_expired(expiry_date):

    expiry = datetime.strptime(
        expiry_date,
        "%Y-%m-%d"
    )

    return datetime.now() > expiry