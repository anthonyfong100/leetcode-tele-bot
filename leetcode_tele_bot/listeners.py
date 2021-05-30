import logging
from typing import Callable, List

import telebot


def logger_listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == "text":
            # print the sent message to the console
            logging.info(f"{m.chat.first_name} [{m.chat.id}]: {m.text}")


all_listeners = [logger_listener]


def register_listeners(
    telegram_client: telebot.TeleBot, listeners: List[Callable]
):
    for listener in listeners:
        telegram_client.set_update_listener(listener)
