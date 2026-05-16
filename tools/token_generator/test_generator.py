import time
from tools.token_generator.generator import generate_mock_consent_token

def test_generate_mock_consent_token_structure():
    """Verifies that the generated token contains all necessary fields and types."""
    agent_id = "test-agent"
    client_id = "test-client"
    action = "read"
    
    token = generate_mock_consent_token(agent_id, client_id, action)
    
    # Assert structural keys exist
    assert "token_id" in token
    assert token["agent_id"] == agent_id
    assert token["delegator_id"] == client_id
    assert token["status"] == "ACTIVE"
    
    # Assert timing parameters make sense
    assert token["expires_at"] > int(time.time())
    
    # Assert inner scopes array is formatted correctly
    assert isinstance(token["scopes"], list)
    assert token["scopes"][0]["action"] == action