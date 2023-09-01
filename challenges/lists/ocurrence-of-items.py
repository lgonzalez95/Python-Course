list = ['A', 'B', 'C', 'D', 'E', 'A', 'B', 'E', 'B', 'D', 'B', 'E']

result = []

for x in list:
    if x not in result:
        result.append(x)
        result.append(list.count(x))

print(result)