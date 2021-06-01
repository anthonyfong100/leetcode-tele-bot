import logging
import os

import config  # load the config
import telebot
from leetcode_tele_bot.telebot_service.api.telegram import TelegramApiClient
from leetcode_tele_bot.telebot_service.listeners import (
    all_listeners,
    register_listeners,
)
from leetcode_tele_bot.telebot_service.logger import InitLogger

if __name__ == "__main__":
    import leetcode_tele_bot.telebot_service.routes  # need to import this to load the routes

    InitLogger()
    register_listeners(TelegramApiClient, all_listeners)
    TelegramApiClient.infinity_polling()  # hand exce
