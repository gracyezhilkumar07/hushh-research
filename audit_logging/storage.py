import json


def save_log(log):

    with open(
        "logs/audit_logs.json",
        "a"
    ) as file:

        file.write(
            json.dumps(log) + "\\n"
        )
