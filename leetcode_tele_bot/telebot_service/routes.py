import leetcode_tele_bot.telebot_service.handlers as handlers
from leetcode_tele_bot.telebot_service.api.telegram import TelegramApiClient


@TelegramApiClient.message_handler(commands=["get_question"])
def daily_problem(message) -> None:
    handlers.leetcode.push_daily_leetcode_message(message)


@TelegramApiClient.message_handler(commands=["start"])
def send_welcome(message):
    handlers.telebot.send_welcome(message)
