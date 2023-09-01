import numpy as np

"""
Slice bidimensional array:  array[start:end:steps, start:end:steps]
[
[2, 4, 6, 8], 
[1, 3, 5, 7], 
[11, 22, 33, 44], 
[10, 20, 30, 40]
]
"""
my_array = np.array([[2, 4, 6, 8], [1, 3, 5, 7], [11, 22, 33, 44], [10, 20, 30, 40]])

print(my_array[-3, -3])
print('-------------')

print(my_array[0:2])  # slices the array by rows, hence it takes the first two rows only
print('-------------')

print(my_array[0:3: 2])
print('-------------')

print(my_array[:, 0:2])  # slices the array by columns, hence it takes the first two columns only
print('-------------')

print(my_array[1: 3, 2:4])  # slices the array by rows and columns
print('-------------')

print(my_array[1: 4: 2, 1:4: 2])  # slices the array by rows and columns skipping one row and one column
print('-------------')
