def validate_log_data(data):

    required_fields = [
        "user_id",
        "dataset_id",
        "access_type",
        "approved"
    ]

    for field in required_fields:

        if field not in data:
            return False

    return True