import logging
import os

import telebot

logger_client = None


def InitLogger():
    global logger_client
    logger_client = telebot.logger
    telebot.logger.setLevel(
        int(os.getenv("LOGGING_LEVEL"))
    )  # Outputs debug messages to console.


def get_logger() -> logging.Logger:
    return logger_client
