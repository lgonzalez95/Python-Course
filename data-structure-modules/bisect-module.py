import bisect

b = [10, 20, 20, 30, 50, 60, 70, 90, 90]
bisect.insort(b, 25)
print(b)

bisect.insort_left(b, 69)
print(b)

bisect.insort_right(b, 49)
print(b)

print(bisect.bisect(b, 19))
print(bisect.bisect_right(b, 90))
print(bisect.bisect_left(b, 90))
