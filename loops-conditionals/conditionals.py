
"""
Relatinal operators
<
<=
>
>=
==
!=

Logical operators
and
or
not
"""

num = int(input("Enter a number: "))

if num > 0:
    if (num > 0 and num < 10):
        print("Num is greater than 0 but less than 10")
    elif ((num > 10 and num <= 100) or num == 10):
            print("Num is equal or greater than 10 but less than 101")
    else:
        if (not num > 200):
            print("Num is less than 200")
else:
    print("Num is negative")
