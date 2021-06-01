from leetcode_tele_bot.telebot_service.api.telegram import TelegramApiClient


def send_welcome(message):
    TelegramApiClient.reply_to(message, "Howdy, how are you doing?")
