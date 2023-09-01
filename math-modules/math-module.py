"""
math.ceil: Takes a float value and returns the upper value: 1.3=> 2
math.floor: Takes a float value and returns the lower value: 1.3=> 1
math.fabs: Gives always the positive value of a given number
math.fmod: Same as %

math.sqrt: Returns the float square root of a number
math.isqrt: Returns the int square root of a number
math.pow: Returns the power of one number
math.factorial: Returns the factorial of a number

math.gcd: Returns the common divisor of two numbers (without taking into consideration 1)
math.perm: Returns the number of ways to choose k items from n items with order and without repetition
math.comb: Returns the number of ways to choose k items from n items without repetition and order

math.prod: Returns the product of an iterable
math.fsum: Returns the sum of an iterable

math.pi: Pi value
math.e: e value
nan: not a number value
inf: infinity value
"""

import math

print(math.ceil(1.3))
print(math.floor(1.3))
print(math.fabs(-1))
print(math.fmod(11, 2))
print()

print(math.sqrt(25))
print(math.isqrt(25))
print(math.pow(3, 3))
print(math.factorial(3))
print()

print(math.gcd(25, 10))
print(math.perm(5, 2))
print(math.comb(5, 2))
print()

print(math.prod([1, 2, 3, 4]))
print(math.fsum([1, 2, 3, 4]))
print()

print(math.pi)
print(math.e)
print(math.nan)