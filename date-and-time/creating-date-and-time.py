"""
Some methods:
time.time()
time.localtime([sec])
time.ctime([sec])
datetime.datetime.now()
datetime.datetime.today()

Subtraction works on datetime and date, but not on time
"""
import datetime
import time

dt1 = datetime.datetime(year=2010, month=1, day=1, minute=10, second=10, microsecond=10)
dt2 = datetime.datetime(year=2011, month=1, day=1, minute=10, second=10, microsecond=10)
d1 = datetime.date(year=2020, month=12, day=12)
d2 = datetime.date(year=2010, month=12, day=12)
print(dt1)
print(dt2 - dt1)
print(d1)

dtime = datetime.time(minute=50, second=30, microsecond=20)
dtime2 = datetime.time(minute=51, second=30, microsecond=20)
print(datetime.datetime.combine(dt1, dtime))

print(d1 - d2)
# print(dtime - dtime2) not allowed
