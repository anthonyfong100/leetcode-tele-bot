import datetime

import common.constants as constants
import common.models as models
from common.date_utils import (
    get_num_days_in_month,
    get_problem_offset_from_start,
    get_week_in_month,
    get_week_offset_from_start,
)


def get_curr_datetime() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def get_daily_problem_url(dt: datetime.datetime) -> str:
    month: str = models.Month(dt.month).name.lower()
    week_id = get_explore_week_id(dt)
    week_string = get_week_string(dt)
    problem_id = get_explore_problem_id(dt)
    website_url = (
        f"https://leetcode.com/explore/featured/card/{month}"
        f"-leetcoding-challenge-{dt.year}/{week_id}/{week_string}/{problem_id}/"
    )
    return website_url


def get_explore_week_id(dt: datetime.datetime) -> int:
    return get_week_offset_from_start(dt) + constants.START_WEEK_OFFSET


def get_explore_problem_id(dt: datetime.datetime) -> int:
    return get_problem_offset_from_start(dt) + constants.START_PROBLEM_OFFSET


def get_week_string(dt: datetime.datetime) -> str:
    week_num = get_week_in_month(dt)
    month_str: str = models.Month(dt.month).name.lower()
    if week_num == 1:
        return f"week-1-{month_str}-1st-{month_str}-7th"
    elif week_num == 2:
        return f"week-2-{month_str}-8th-{month_str}-14th"
    elif week_num == 3:
        return f"week-3-{month_str}-15th-{month_str}-21st"
    elif week_num == 4:
        return f"week-4-{month_str}-22nd-{month_str}-28th"

    if get_num_days_in_month(dt.year, dt.month) == 30:
        return f"week-5-{month_str}-29th-{month_str}-30th"
    return f"week-5-{month_str}-29th-{month_str}-31st"
