import leetcode_tele_bot.handlers as handlers
from leetcode_tele_bot.api.telegram import TelegramApiClient


@TelegramApiClient.message_handler(commands=["get_question"])
def daily_problem(message) -> None:
    handlers.leetcode.push_daily_leetcode_message()


@TelegramApiClient.message_handler(commands=["start"])
def send_welcome(message):
    handlers.telebot.send_welcome(message)
