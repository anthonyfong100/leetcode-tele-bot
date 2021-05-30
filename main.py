import logging
import os

import telebot

import config  # load the config
from leetcode_tele_bot.api.telegram import TelegramApiClient
from leetcode_tele_bot.listeners import all_listeners, register_listeners

if __name__ == "__main__":
    import leetcode_tele_bot.routes  # need to import this to load the routes

    register_listeners(TelegramApiClient, all_listeners)
    TelegramApiClient.infinity_polling()  # hand exce
