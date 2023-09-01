"""
pop([i]): removes the element in the last position of the list when the index is not given
del list[index]: Removes an element from the list
remove(x): Removes an element from the list
clear: Removes all element from the list
"""


myList = ["Juan", "Juanita", "Panchito", "Panchita"]
myList.pop()
print(myList)
myList.pop(0)
print(myList)

print()

anotherList = ["Juan", "Juanita", "Panchito", "Panchita"]
del anotherList[0:2]
print(anotherList)


anotherList.remove("Panchito")
print(anotherList)

anotherList.clear()
print(anotherList)