
# 1. dict1 = dict()
dict1 = dict()
for x in range(1, 6):
    dict1[x] = x*2
print(dict1)

# 2. dict2 = dict((iterable pairs))
dict2 = dict((x, x*2) for x in range(10))
print(dict2)

# 3. dict3 = dict(zip(iterable, iterable)): zip is usted to combine
# Skips elements if a list has more elements than the other
a = ['A', 'B', 'C']
b = ['Apple', 'Ball', 'Cat']
dict3 = dict(zip(a, b))
print(dict3)

# 4. dict4 = dict(enumerate(iterable)) #enumerate function gives a tuple with the index and the value
dict4 = dict(enumerate([11, 22, 33, 44]))
print(dict4)

# 5. dict5 = {x:w for x in range(y, z)}
dict5 = {x: x*2 for x in range(1, 6)}
print(dict5)

# 6. dict6 = {(x, w) for x in range(y, z)}
dict6 = dict((x, x**2) for x in range(1, 6))
print(dict6)

# 7. dict7 = {x:y for x,y in zip (iterable, iterable)}
dict7 = {x: y for x, y in zip(["Juan", "Pedro"], [1, 2])}
print(dict7)

# 8. dict8 = {x:y for x,y in zip (iterable, iterable)}
dict8 = {x: y for x, y in enumerate(["Juan", "Pedro", "Mary"])}
print(dict8)

