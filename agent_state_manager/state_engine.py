from session_tracker import track_session
from lifecycle_manager import update_lifecycle


def manage_agent_state(agent):

    session = track_session(agent)

    lifecycle = update_lifecycle(agent)

    return {
        "current_state": "processing",
        "session": session,
        "lifecycle": lifecycle
    }