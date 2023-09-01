"""
zeros(3)
ones(3)
empty(3)
eye(3)
diag(3)
arange(start, end, step)
linspace(start, end, num=5)
"""

import numpy as np

print(np.zeros(3))
print(type(np.zeros(3)))
print(np.zeros((3, 3)))
print(np.zeros((3, 3, 3)))
print('--------------------')

print(np.ones((3, 3, 3)))
print('--------------------')

print(np.empty((3, 3, 3)))
print('--------------------')

print(np.eye(4))
print('--------------------')

print(np.diag([2, 4, 6]))
print('--------------------')

print(np.arange(-10, 4, 2))
print('--------------------')

print(np.linspace(0, 20, 6 ))
print('--------------------')
