from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.middlewares.correlation_id import (
    CorrelationIDMiddleware,
)


def test_correlation_id_header_present():
    app = FastAPI()

    app.add_middleware(CorrelationIDMiddleware)

    @app.get("/health")
    async def health():
        return {"ok": True}

    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert "X-Correlation-ID" in response.headers