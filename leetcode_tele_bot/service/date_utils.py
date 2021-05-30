import datetime
import math
from calendar import monthrange
from typing import Tuple

import leetcode_tele_bot.service.constants as constants
from leetcode_tele_bot.service.models import Month


def get_curr_datetime() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def get_today_date() -> Tuple[int]:
    """
    Return year month date in the format (YYYY,MM,DD) in UTC time
    """
    dt = datetime.datetime.now(datetime.timezone.utc)
    return (dt.year, dt.month, dt.day)


def get_week_in_month(dt: datetime.datetime) -> int:
    # leetcode website counts week as weeks from starting date of the month
    # e.g. if month starts at friday --> next monday is still week 1 (week doesnt end on sunday, is strictly 7 days)
    dom = dt.day
    return int(math.ceil(dom / 7.0))


def get_week_offset_from_start(curr_date: datetime.datetime) -> int:
    # return the dt object for the monday on the start date (start date is a fixed time calculated from Jan 1st 2021)
    years_offset = (
        curr_date.year - constants.START_DATETIME.year
    ) * constants.NUM_WEEKS_PER_YEAR
    month_offset = constants.WEEK_OFFSET_FROM_START_MONTH_MAP[
        Month(curr_date.month)
    ]
    week_offset = get_week_in_month(curr_date) - 1
    return years_offset + month_offset + week_offset


def get_problem_offset_from_start(curr_date: datetime.datetime) -> int:
    # leetcode has 7 daily problem and one weekly problem a week

    days_offset = (curr_date - constants.START_DATETIME).days
    problem_offset = days_offset + get_week_offset_from_start(
        curr_date
    )  # additional weekly problem
    if curr_date.hour < 7:
        problem_offset -= 1  # new problem is released after 7am UTC
    return problem_offset + 1  # first problem of week is weekly problem


def get_num_days_in_month(year: int, month: int) -> int:
    return monthrange(year, month)[1]
