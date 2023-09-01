import calendar
import datetime

year = int(input('Enter a year to find all dates: '))

for x in range(1, 13):
    c = calendar.monthcalendar(year, x)
    second_saturday = datetime.date(year=year, month=x, day=c[1][5])
    print(second_saturday)


"""
[2, 3, 4, 5, 6, 7, 8]
[9, 10, 11, 12, 13, 14, 15]
[16, 17, 18, 19, 20, 21, 22]
[23, 24, 25, 26, 27, 28, 29]
[30, 31, 0, 0, 0, 0, 0]
"""