"""
add: adds a new element to an existing set
copy: creates a copy of a set and returns it
update: adds multiple values to a set 

pop: removes a random element
discard: removes an element and ignores any failure if it is not found
remove: removes an element and returns an error if the element is not found
clear: removes all elements
"""

s1 = {50, 20, 40, 10, 30}

s1.add(60)
print(s1)

s2 = s1.copy()
print(s2)

s2.update([33, 44])
print(s2)

s2.pop()
print(s2)

s2.discard(44)
print(s2)

s2.remove(333)