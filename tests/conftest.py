import os

import pytest
from dotenv import load_dotenv
from leetcode_tele_bot.logger import InitLogger


@pytest.fixture(scope="session", autouse=True)
def setup_config():
    load_dotenv(verbose=True, dotenv_path=".dev.env")
    InitLogger()
