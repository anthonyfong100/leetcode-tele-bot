from fastapi import Response, status
from leetcode_tele_bot.api.telegram import TelegramApiClient
from leetcode_tele_bot.service.leetcode_url_generator import (
    get_curr_datetime,
    get_daily_problem_url,
)


def push_daily_leetcode_message():
    curr_time = get_curr_datetime()
    leetcode_problem_url = get_daily_problem_url(curr_time)
    err = TelegramApiClient.send(leetcode_problem_url)
    if not err:
        return Response(status_code=status.HTTP_200_OK)
    return Response(
        content=err, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )
