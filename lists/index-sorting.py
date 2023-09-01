"""
index(x, [, start[,end]]): returns the index of an element. If the element is not found it returns an error
count: Counts number of occurrences for an element
reverse
sort: Modifies the original list
sorted: Does not modify the original list
"""

list = [5, 6, 7, 5 , 8, 9, 6, 10, 6]

print(list.index(5))
print(list.index(5, 2, 7))
#print(list.index(35)) #error

print(list.count(5))

list.reverse()
print(list)

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list2 = ["BB", "ZZ", "aa", "jj", "mm", "yy"]
list2.sort()
print(list2)

list2 = ["BB", "ZZ", "aa", "jj", "mm", "yy"]
list2.sort(key=str.lower)
print(list2)

list3 = ["BB", "ZZ", "aa", "jj", "mm", "yy"]
print(list3)
