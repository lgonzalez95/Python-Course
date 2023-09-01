list = [int(x) for x in input("Enter a numeric list separated by space: ").split(" ")]
uniqueElements = []

for x in list:
    if x not in uniqueElements:
        uniqueElements.append(x)

print(uniqueElements)

for x in list:
    if list.count(x) > 1:
        list.remove(x)

print(list)