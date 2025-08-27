from datetime import datetime, date

set_date = '202s5.10.09'


def get_days_from_today(date: str) -> int:
    '''
    a function that calculates the number of days between a given date and the current date.
    '''
    # subtract the current date from the specified date
    try:
        days_left = (datetime.strptime(date, "%Y.%m.%d").date() -
                     datetime.today().date()).days
        return days_left
    except ValueError:
        return f'{set_date} is not date! Write date in format "YYYY.MM.DD"'


print(get_days_from_today(set_date))
