from datetime import datetime, date

set_date = '2025.10.09'


def get_days_from_today(date: str) -> int:
    '''
    a function that calculates the number of days between a given date and the current date.
    '''
    days_left = (datetime.strptime(date, "%Y.%m.%d").date(
        # subtract the current date from the specified date
    ) - datetime.today().date()).days
    return days_left


print(get_days_from_today(set_date))
