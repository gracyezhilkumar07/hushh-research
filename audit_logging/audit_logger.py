from datetime import datetime
from storage import save_log


def log_consent_event(
    user_id,
    dataset_id,
    access_type,
    approved
):

    log = {
        "user_id": user_id,
        "dataset_id": dataset_id,
        "access_type": access_type,
        "approved": approved,
        "timestamp": str(datetime.utcnow())
    }

    save_log(log)

    return log