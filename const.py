import os
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


ERROR_MSG = """
    Invalid message format. Message should be in the following format:
    {"dt_from": "2022-09-01T00:00:00", "dt_upto":
    "2022-12-31T23:59:00", "group_type": "month"}
"""
