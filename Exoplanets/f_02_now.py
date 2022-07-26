
import datetime
from datetime import datetime, timedelta


def f_now():
    now = datetime.now()
    now = now.strftime("%Y-%m-%d")

    return now
