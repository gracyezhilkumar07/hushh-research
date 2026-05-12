def validate_workflow_data(data):

    required_fields = [
        "dataset_id"
    ]

    for field in required_fields:

        if field not in data:
            return False

    return True