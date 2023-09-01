"""
random(): Float random number 0-1
uniform(x, y): Float random from x, y
randint(x, y): int random from x, y
randrange(x, y, z): int random from x, y, skipping by z

seed: Starting point to generate numbers
choice(): Picks a random element from a list
choises(l, k): Picks random k elements from a list l allowing elements to be repeated
sample(l, k): Picks random k elements from a list l with unique elements
shuffle(): shuffles the elements of a list
getrandbits: returns a random number based on the given bits
"""

import random

print(random.random())
print(random.uniform(1, 10))
print(random.randint(1, 10))
print(random.randrange(1, 20, 2))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choices([1, 2, 3, 4, 5], k=2))
print(random.sample([1, 2, 3, 4, 5], k=2))
print(random.getrandbits(3))  # from 0 to 7
