"""
1. For
2. For using range
3. While
"""
myList = ["Juan", "Juanita", "Panchito", "Panchita"]
for x in myList:
    print(x)

print()

for x in range(0, len(myList)):
    print(myList[x])

print()

for x in range(len(myList)-1, -1, -1):  # reversed
    print(myList[x])

print()

i = 0
while i < len(myList):
    print(myList[i])
    i+=1