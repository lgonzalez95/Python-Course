import datetime

year = int(input('Enter a year: '))
count = 0

for x in range(1, 13):
    date = datetime.date(year=year, month=x, day=1)
    if date.weekday() == 0:
        count += 1
print('There are', count, 'months that start with monday for the year', year)
