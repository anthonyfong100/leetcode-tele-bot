from fastapi import APIRouter, Response, status

from leetcode_tele_bot.api.telegram import TelegramApiClient
from leetcode_tele_bot.handlers.leetcode import push_daily_leetcode_message

tele_bot_router = APIRouter()


@tele_bot_router.get("/healthcheck")
async def root() -> Response:
    return Response(status_code=status.HTTP_200_OK)


@TelegramApiClient.message_handler(commands=["get_question"])
def daily_problem(message) -> Response:
    return push_daily_leetcode_message()


@TelegramApiClient.message_handler(commands=["start", "help"])
def send_welcome(message):
    TelegramApiClient.reply_to(message, "Howdy, how are you doing?")
    raise Exception("simulate panic")


@TelegramApiClient.message_handler(func=lambda m: True)
def echo_message(message):
    TelegramApiClient.reply_to(message, message.text)
