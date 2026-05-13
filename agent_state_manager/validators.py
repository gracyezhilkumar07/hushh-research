def validate_agent_data(data):

    required_fields = [
        "agent_id",
        "task"
    ]

    for field in required_fields:

        if field not in data:
            return False

    return True