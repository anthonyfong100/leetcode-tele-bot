import os

import telegram_svc.logger as logger
from common.leetcode_url_generator import (
    get_curr_datetime,
    get_daily_problem_url,
)
from telegram_svc.api.telegram import TelegramApiClient


def push_daily_leetcode_message(message):
    curr_time = get_curr_datetime()
    chat_id = message.chat.id
    leetcode_problem_url = get_daily_problem_url(curr_time)
    message = TelegramApiClient.send_message(chat_id, leetcode_problem_url)
    logger.get_logger().info(f"message from push_daily_leetcode_message is: {message}")
