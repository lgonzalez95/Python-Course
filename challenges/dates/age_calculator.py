import datetime
from datetime import *

dob = input('Enter the person\'s DOB with format DD-MM-YYYY: ')
d, m, y = dob.split('-')
dob_obj = date(day=int(d), month=int(m), year=int(y))
current_date = datetime.today().date()

years = current_date.year - dob_obj.year
if (current_date.month, current_date.day) < (dob_obj.month, dob_obj.day):
    years -= 1
print('The person\'s age is', years)
