from collections import Counter

l = ['Mark', 'David', 'Juan', 'David', 'Mark', 'Mark']
c = Counter(l)
print(c)
print(c.get('David'))
print(c.keys())
print(c.values())

c.update({'Ericka': 6})
print(c)

for x in c.elements():
    print(x)

print(c.most_common(1))
print(c.most_common(2))
