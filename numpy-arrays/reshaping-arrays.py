import numpy as np

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

two_dimension = my_array.reshape(4, 3)
print(two_dimension)  # Two dimension
print('--------')

three_dimension = my_array.reshape(3, 2, 2)
print(three_dimension)  # Three dimension
print('--------')

back_to_one_dimension = three_dimension.flatten()
print(back_to_one_dimension)  # One dimension
print('--------')

another_way_to_one_dimension = three_dimension.reshape(12)
print(another_way_to_one_dimension)  # One dimension
print('--------')
