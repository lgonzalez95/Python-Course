import datetime


def prev_day(day):
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    idx = week.index(day)
    today = datetime.datetime.now()
    diff = (idx - today.weekday() - 7)
    print(datetime.date(year=today.year, day=(today.day + diff), month=today.month))


prev_day('Monday')
