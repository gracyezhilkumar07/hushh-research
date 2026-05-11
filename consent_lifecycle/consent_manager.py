from expiry_engine import is_consent_expired
from revocation_engine import is_consent_revoked


def check_consent_status(consent_data):

    expired = is_consent_expired(
        consent_data["expires_at"]
    )

    revoked = is_consent_revoked(
        consent_data["revoked"]
    )

    return {
        "consent_active": not expired and not revoked
    }