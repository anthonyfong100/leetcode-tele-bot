import os

import uvicorn
from fastapi import FastAPI

# import config  # load the config
from telebot_backend_svc.routes import leetcode_router

app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    redoc_url=None,
)

app.include_router(leetcode_router, prefix="/api", tags=["telebot"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
