import os

import leetcode_tele_bot.logger as logger
from leetcode_tele_bot.api.telegram import TelegramApiClient
from leetcode_tele_bot.service.leetcode_url_generator import (
    get_curr_datetime,
    get_daily_problem_url,
)


def push_daily_leetcode_message(message):
    curr_time = get_curr_datetime()
    chat_id = message.chat.id
    leetcode_problem_url = get_daily_problem_url(curr_time)
    message = TelegramApiClient.send_message(chat_id, leetcode_problem_url)
    logger.get_logger().info(
        f"message from push_daily_leetcode_message is: {message}"
    )
