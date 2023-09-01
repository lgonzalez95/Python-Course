import calendar

print(calendar.isleap(2020))
print(calendar.weekday(2020, 12, 20))
print(calendar.prmonth(2023, 7))

c = calendar.Calendar()
for x in c.iterweekdays():
    print(x)

for x in c.itermonthdates(2022, 2):
    print(x)

for x in c.itermonthdays2(2022, 2):
    print(x)

for x in c.itermonthdays3(2022, 2):
    print(x)

for x in c.itermonthdays4(2022, 2):
    print(x)

for x in c.monthdatescalendar(2022, 2):
    print(x)

c2 = calendar.TextCalendar()
print(c2.prmonth(2023, 7))
print(c2.formatmonth(2023, 7))

c3 = calendar.HTMLCalendar()
print(c3.formatmonth(2023, 7))