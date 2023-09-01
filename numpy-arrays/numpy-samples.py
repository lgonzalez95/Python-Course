import numpy as np
import pprint

ar = np.array([1, 3, 5, 7, 9])
print(ar)
print()

two_dim_ar = np.array([[1, 3, 5, 7, 9], [3, 4, 6, 8, 10]])
pprint.pprint(two_dim_ar)
print()

three_dim_ar = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(three_dim_ar)
print()

# Create our array specifying the dimension
ar2 = np.array([1, 2, 3, 4, 5], ndmin=3)
print(ar2)

"""
Attributes:
dtype: Returns the datatype
shape: Returns the shape of an array (number of rows and columns)
itemsize: How much memory the items are consuming
ndim: Returns the dimension of the array: 1, 2, 3, etc.
nbytes: Total memmory consumed by all elements
"""

print(two_dim_ar.ndim)
print(ar2.ndim)
print()

print(two_dim_ar.shape)
print(ar2.shape)
print()

print(two_dim_ar.dtype)
print(ar2.dtype)
print()

print(two_dim_ar.itemsize)
print(ar2.itemsize)
print()

print(two_dim_ar.nbytes)
print(ar2.nbytes)
print()