from fastapi import APIRouter, Response, status

tele_bot_router = APIRouter()


@tele_bot_router.get("/healthcheck")
async def root():
    return Response(status_code=status.HTTP_200_OK)
