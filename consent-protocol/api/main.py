from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.middlewares.security_headers import (
    SecurityHeadersMiddleware,
)


def test_security_headers_present():
    app = FastAPI()

    app.add_middleware(SecurityHeadersMiddleware)

    @app.get("/health")
    async def health():
        return {"ok": True}

    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200

    assert (
        response.headers["X-Content-Type-Options"]
        == "nosniff"
    )

    assert (
        response.headers["X-Frame-Options"]
        == "DENY"
    )

    assert (
        response.headers["Referrer-Policy"]
        == "no-referrer"
    )