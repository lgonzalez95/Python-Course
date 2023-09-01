def add(a, b, c, d, e, f):
    return a + b + c + d + e + f


# first two are positional only and rest of them can be either positional or keyword arguments
def add2(a, b, /, c, d, e, f):
    return a + b + c + d + e + f


# first two must be positional arguments
# middle two can be either positional or keyword arguments
# last two must be keyword arguments
def add3(a, b, /, c, d, *, e, f):
    return a + b + c + d + e + f


add(2, 5, 9, 7, 3, 8)
add(f=8, c=9, b=5, e=3, d=7, a=2)

add2(2, 5, 6, 7, 9, 4)  # all positional
add2(2, 5, d=7, f=4, e=9, c=6)
# add2(a=2, b=5, 7, 4, 9, 6) # not allowed

# add3(2, 5, 9, 7, 3, 8) not allowed
add3(2, 5, 9, 7, e=3, f=8)
