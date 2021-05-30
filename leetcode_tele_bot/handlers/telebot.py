from leetcode_tele_bot.api.telegram import TelegramApiClient


def send_welcome(message):
    TelegramApiClient.reply_to(message, "Howdy, how are you doing?")
