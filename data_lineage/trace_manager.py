from datetime import datetime


def create_trace_record(dataset_id, processed_by):

    return {
        "dataset_id": dataset_id,
        "processed_by": processed_by,
        "timestamp": str(datetime.now())
    }