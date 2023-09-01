"""
append(x): Will modify the same list
extent(iterable): Same as append but allows to add collections; list, tuple, or string
insert(i, x): Insert new element in an existing list for the given index 
copy(): Copies a list and returns a new list
"""

myList = ["Juan", "Juanita", "Panchito", "Panchita"]
myList.append("Sofía")
print(myList)

myList[5:5] = [1,2]
print(myList)

myList.extend([100, 101, 102])
print(myList)

myList[len(myList):] = [2001, 2002]
print(myList)

myList.insert(1, "New element")
print(myList)

copy = myList.copy()
print(copy)