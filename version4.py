from datetime import datetime


def _get_book_return_date():
    lend_time_period = 14
    current_date = date.today()
    return current_date + datetime.timedelta(days=lend_time_period)