import csv
import pprint

"""
Way #1
"""
f = open('data.csv', 'r')
csv_reader = csv.reader(f)
next(csv_reader)
sals = []
for x in csv_reader:
    print(x)
    sals.append(int(x[3]))

print(min(sals))
print(max(sals))
f.close()

"""
Way #2
"""
f = open('data.csv', 'r')
csv_reader = csv.DictReader(f)
dct = {}
for x in csv_reader:
    print(type(x))
    dct[x['name']] = x

f.close()
pprint.pprint(dct)
print('Luis Info: ', dct.get('Luis'))
