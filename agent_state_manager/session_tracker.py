def track_session(agent):

    return {
        "agent_id": agent.get("agent_id"),
        "task": agent.get("task"),
        "session_status": "active"
    }