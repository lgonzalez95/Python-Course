"""
|: union
&: intersection
-: difference:
^: symetric difference
<: If the left set is subset of the right one
<=: If the left set is subset or equal of the right one
>: If the left set is superset of the right one
>=: If the left set is superset or equal of the right one
==
!=
in
not in
"""
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a = {1, 2, 3, 5, 7}
c = {1, 2, 3, 5, 7}
b = {5, 7, 9, 10, 11}

print(s|a)
print(s&a)
print(s-a)
print(a^b)

print()

print(a<s)
print(s>a)
print(a!=b)
print(a==c)
print(10 in s)