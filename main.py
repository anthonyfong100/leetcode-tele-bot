import uvicorn
from fastapi import FastAPI

from leetcode_tele_bot.routes import tele_bot_router

app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    redoc_url=None,
)
app.include_router(tele_bot_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
