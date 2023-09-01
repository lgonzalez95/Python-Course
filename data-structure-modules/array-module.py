"""
b: Int
B: Int
i: Signed int
I: Unsigned int
l: Signed long
L: Unsigned long
q: Signed long long
Q: Unsigned long long
f: float
D: Double float
"""

import array

my_array = array.array('i', [10, 20, 30, 40])
print(my_array)

my_other_array = array.array('d', [33.5010, 40.234, 55.76])
my_other__float_array = array.array('f', [33.5010, 40.234, 55.76])

print(my_other_array)
print(my_other__float_array)

print(my_array[1:3])

my_array.append(50)
print(my_array)

print(my_array.index(40))

# all list methods are available
