import logging
import os

import telebot


def InitLogger():
    logger = telebot.logger
    telebot.logger.setLevel(
        int(os.getenv("LOGGING_LEVEL"))
    )  # Outputs debug messages to console.
    return logger
