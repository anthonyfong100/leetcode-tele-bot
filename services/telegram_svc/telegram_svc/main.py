import logging
import os

import telebot

import telegram_svc.routes  # isort:skip
from telegram_svc.api.telegram import TelegramApiClient  # isort:skip
from telegram_svc.listeners import all_listeners, register_listeners  # isort:skip
from telegram_svc.logger import InitLogger  # isort:skip


def main():
    InitLogger()
    register_listeners(TelegramApiClient, all_listeners)
    TelegramApiClient.infinity_polling()  # hand exce


if __name__ == "__main__":
    main()
