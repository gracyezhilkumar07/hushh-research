from orchestration_manager import orchestrate_workflow
from execution_pipeline import execute_pipeline


def run_governance_workflow(data):

    workflow = orchestrate_workflow(data)

    pipeline_result = execute_pipeline(workflow)

    return {
        "workflow_executed": True,
        "pipeline_result": pipeline_result
    }