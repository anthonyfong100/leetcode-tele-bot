import datetime

from leetcode_tele_bot.leetcode_api.url_generator import get_daily_problem_url


def test_get_daily_problem_url():
    may_28_2021 = datetime.datetime(2021, 5, 28, tzinfo=datetime.timezone.utc)
    expected_url = "https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3758/"
    assert get_daily_problem_url(may_28_2021) == expected_url

    may_29_2021 = datetime.datetime(2021, 5, 29, tzinfo=datetime.timezone.utc)
    expected_url = "https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3760/"
    assert get_daily_problem_url(may_29_2021) == expected_url

    jan_7_2021 = datetime.datetime(2021, 1, 7, tzinfo=datetime.timezone.utc)
    expected_url = "https://leetcode.com/explore/featured/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3595/"
    assert get_daily_problem_url(jan_7_2021) == expected_url
