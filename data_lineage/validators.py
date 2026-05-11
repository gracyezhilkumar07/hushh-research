def validate_lineage_data(data):

    required_fields = [
        "dataset_id",
        "source",
        "processed_by"
    ]

    for field in required_fields:

        if field not in data:
            return False

    return True