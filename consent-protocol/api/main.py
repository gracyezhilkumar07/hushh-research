from fastapi import FastAPI

from api.middlewares.correlation_id import (
    CorrelationIDMiddleware,
)

app = FastAPI()

app.add_middleware(CorrelationIDMiddleware)