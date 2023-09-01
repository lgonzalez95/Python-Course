"""
Tuples are inmutable
Tuples can contain duplicates
Tupple does not have append method
Allows packing and unpacking
"""

t1 = ("Juan", "Pedro", "Lucía")

t2 = (tuple("Juan"), 1)

t3 = 1, 2, 3, 4, 5 #Packing

a, b, c, d, e = t3 #unpacking
f, *g, h = t3 #unpacking
print(t1)
print(t2)
print(t3)
print(a, b, c, d, e)
print(f, g, h)