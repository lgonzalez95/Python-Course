"""
These methods create a new set, they don't modify the original sets
union
intersection
intersection_update: Update the original set
difference
difference_update: Update the original set
symmetric_difference: Elements only in A and only in B but not common
symmetric_difference_update: Update the original set

issubset
issuperset
isdisjoint
"""


s1 = {1, 2, 3, 5, 7}
s2 = {5, 7, 9, 10, 11}
s3 = {5, 7, 15, 20}
s4 = {20}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print()

s1.intersection_update(s2)
print(s1)
s3.difference_update(s2)
print(s3)

s4.symmetric_difference_update(s3)
print(s4)

print()
print(s4.issubset(s3))
print(s1.issuperset(s2))
print(s4.isdisjoint(s1))
