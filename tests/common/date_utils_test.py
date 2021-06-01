import datetime

from leetcode_tele_bot.common.date_utils import (
    get_problem_offset_from_start,
    get_week_in_month,
    get_week_offset_from_start,
)


def test_get_week_in_month_normal_case():
    may_1_2021 = datetime.datetime(2021, 5, 1, tzinfo=datetime.timezone.utc)
    assert get_week_in_month(may_1_2021) == 1

    may_7_2021 = datetime.datetime(2021, 5, 7, tzinfo=datetime.timezone.utc)
    assert get_week_in_month(may_7_2021) == 1


def test_get_week_in_month_boundary_val():
    may_28_2021 = datetime.datetime(2021, 5, 28, tzinfo=datetime.timezone.utc)
    assert get_week_in_month(may_28_2021) == 4

    may_29_2021 = datetime.datetime(2021, 5, 29, tzinfo=datetime.timezone.utc)
    assert get_week_in_month(may_29_2021) == 5

    jan_7_2021 = datetime.datetime(2021, 1, 7, tzinfo=datetime.timezone.utc)
    assert get_week_in_month(jan_7_2021) == 1


def test_get_week_offset_from_start():
    jan_1_2021 = datetime.datetime(2021, 1, 1, tzinfo=datetime.timezone.utc)
    assert get_week_offset_from_start(jan_1_2021) == 0

    jan_7_2021 = datetime.datetime(2021, 1, 7, tzinfo=datetime.timezone.utc)
    assert get_week_offset_from_start(jan_7_2021) == 0

    feb_1_2021 = datetime.datetime(2021, 2, 1, tzinfo=datetime.timezone.utc)
    assert get_week_offset_from_start(feb_1_2021) == 5

    may_28_2021 = datetime.datetime(2021, 5, 28, tzinfo=datetime.timezone.utc)
    assert get_week_offset_from_start(may_28_2021) == 22


def test_get_problem_offset_from_start():
    jan_1_2021 = datetime.datetime(2021, 1, 1, tzinfo=datetime.timezone.utc)
    assert get_problem_offset_from_start(jan_1_2021) == 0

    jan_1_2021_hr_7 = datetime.datetime(
        2021, 1, 1, hour=7, tzinfo=datetime.timezone.utc
    )
    assert get_problem_offset_from_start(jan_1_2021_hr_7) == 1

    jan_1_2021_hr_12 = datetime.datetime(
        2021, 1, 1, hour=12, tzinfo=datetime.timezone.utc
    )
    assert get_problem_offset_from_start(jan_1_2021_hr_12) == 1

    jan_7_2021 = datetime.datetime(
        2021, 1, 7, hour=12, tzinfo=datetime.timezone.utc
    )
    assert get_problem_offset_from_start(jan_7_2021) == 7

    feb_1_2021 = datetime.datetime(
        2021, 2, 1, hour=12, tzinfo=datetime.timezone.utc
    )
    assert get_problem_offset_from_start(feb_1_2021) == 37
