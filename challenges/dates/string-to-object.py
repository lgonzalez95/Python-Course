from datetime import *

date_input = input('Enter a date with format DD-MM-YYYY:')

d, m, y = date_input.split('-')
date_obj = date(day=int(d), month=int(m), year=int(y))
print(date_obj)
