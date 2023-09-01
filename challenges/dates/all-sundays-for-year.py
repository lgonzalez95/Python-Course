import datetime

year = int(input('Enter a year to find all dates: '))
year_obj = datetime.datetime(year=year, month=1, day=1)

days_to_next_sunday = (6 - year_obj.weekday())
year_obj = year_obj + datetime.timedelta(days=days_to_next_sunday)

while year_obj.year == year:
    print(year_obj)
    year_obj = year_obj + datetime.timedelta(days=7)
