# list[expression for item in iterable]

list = [x for x in range(10)]
print(list)


list2 = [x**2 for x in range(1,6)]
print(list2)


list3 = [x for x in (1, 2, 3, 4, 5, 6) if x%2 == 0]
print(list3)


list4 = [x.lower() for x in "Python"]
print(list4)

list5 = [x for x in "Pydsf3245ytrhds;34p2873ywhthon" if x.isalpha()]
print(list5)