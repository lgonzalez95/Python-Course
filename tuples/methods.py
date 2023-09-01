"""
count
index
"""

t1 = (x for x in range(10)) #Wrong
t2 = (tuple(x for x in range(10))) #Correct
t3 = (*(x for x in range(10)),) #Correct

print(t1)
print(t2)
print(t3)

print(t2.count(1))
print(t2.index(9))