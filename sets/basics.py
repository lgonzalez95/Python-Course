"""
Collection of unique values which don't have indexes
The order is not preserved in sets
Sets are mutable: We can remove and insert new elements.
Proper set: A ser should contain some of the values of a set, not all
Disjoin sets: Two sets that are not having common elements but both are sub sets of a set
"""

s1 = {"Jack", 50, 5.5, "John", True, "Smith"}
s2 = set(["Test", 1, 5.25, True, 1, True])

print(s1)

s1.discard("Jack")
print(s1)

s1.add("Jacky")
print(s1)


print(s2)