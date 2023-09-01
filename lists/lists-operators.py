"""
[]: Index
[:]: Slide does not modify the original list
+: 
*: Duplicates N times the elements of a list
in
not in
"""
myList = ["Juan", "Juanita", "Panchito", "Panchita"]
print(myList[0])
print(myList[1:3])
print(myList[0:4:2])

myList[0:3] = ["Lucía"]
print(myList)


ages = [10, 5, 15, 30]
print(myList + ages)
print(ages.extend((11, 12, 13)))  # Modifies original list
print(ages)

print(ages*2) 

if 10 in ages:
    print("It is there")

if 1 not in ages:
    print("It is not there")