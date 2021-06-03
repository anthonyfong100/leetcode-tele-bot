import datetime

from common.models import Month

# 2021/01/01 UTC time
START_DATETIME = datetime.datetime(2021, 1, 1, tzinfo=datetime.timezone.utc)
START_PROBLEM_OFFSET = 3588
START_WEEK_OFFSET = 579

# week offset at first day of the month from year start
# Feb = 5 because jan has 5 weeks (round up number of weeks)
WEEK_OFFSET_FROM_START_MONTH_MAP = {
    Month.JANUARY: 0,
    Month.FEBUARY: 5,
    Month.MARCH: 9,
    Month.APRIL: 14,
    Month.MAY: 19,
    Month.JUNE: 24,
    Month.JULY: 29,
    Month.AUGUST: 34,
    Month.SEPTEMBER: 39,
    Month.OCTOBER: 44,
    Month.NOVEMBER: 49,
    Month.DECEMBER: 54,
}
NUM_WEEKS_PER_YEAR = 54
