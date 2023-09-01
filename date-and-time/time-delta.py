from datetime import datetime

dt1 = datetime(2020, 10, 15, 10, 20, 30)
dt2 = datetime(2019, 10, 15, 10, 20, 30)
td = dt1 - dt2
print(td)
print(type(td))
print(divmod(td.days, 30))
print(divmod(td.days, 7))