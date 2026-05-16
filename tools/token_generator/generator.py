import json
import time

def generate_mock_consent_token(agent_id: str, client_id: str, scope_action: str) -> dict:
    """Generates a structurally valid mock MCP consent token for localized isolation testing."""
    return {
        "token_id": f"mock_tkn_{int(time.time())}",
        "agent_id": agent_id,
        "delegator_id": client_id,
        "expires_at": int(time.time()) + 3600, # Valid for 1 hour
        "scopes": [
            {
                "action": scope_action,
                "resource": "context_environment"
            }
        ],
        "status": "ACTIVE"
    }

if __name__ == "__main__":
    mock_token = generate_mock_consent_token("agent-alpha", "user-123", "read")
    print(json.dumps(mock_token, indent=4))