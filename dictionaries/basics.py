"""
Key must be inmutable: Set and List are not allowed
Values can be of any type
"""

dict1 = {1: "one", 2: "Two", 3: "Three", 4: "Four"}

dict1[4] = "Juan"
print(dict1)


for i in dict1:
    print(i, dict1[i])