import os

import telebot

TelegramApiClient = telebot.TeleBot(os.getenv("TELEBOT_TOKEN"))
