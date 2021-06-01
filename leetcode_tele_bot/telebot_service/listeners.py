from typing import Callable, List

import leetcode_tele_bot.telebot_service.logger as logger
import telebot


def logger_listener(message):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in message:
        print("logger called")
        logger.get_logger().info(f"[{m.chat.id}]: {m.text}")


all_listeners = [logger_listener]


def register_listeners(
    telegram_client: telebot.TeleBot, listeners: List[Callable]
):
    for listener in listeners:
        telegram_client.set_update_listener(listener)
