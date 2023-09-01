def get_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c


print(get_max(4, 4, 4))
