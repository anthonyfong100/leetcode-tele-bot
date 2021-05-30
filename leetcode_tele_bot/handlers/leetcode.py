import os

from fastapi import Response, status
from leetcode_tele_bot.api.telegram import TelegramApiClient
from leetcode_tele_bot.service.leetcode_url_generator import (
    get_curr_datetime,
    get_daily_problem_url,
)


def push_daily_leetcode_message():
    curr_time = get_curr_datetime()
    leetcode_problem_url = get_daily_problem_url(curr_time)
    message = TelegramApiClient.send_message(
        os.getenv("secret_cache"), leetcode_problem_url
    )
    print(f"message is {message}")
    if message:
        return Response(status_code=status.HTTP_200_OK)
    return Response(
        content=message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
