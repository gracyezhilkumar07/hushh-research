from provenance_engine import verify_provenance
from trace_manager import create_trace_record


def track_lineage(dataset):

    provenance_verified = verify_provenance(
        dataset["source"]
    )

    trace_record = create_trace_record(
        dataset["dataset_id"],
        dataset["processed_by"]
    )

    return {
        "lineage_verified": provenance_verified,
        "trace_record": trace_record
    }