def div(a, b):
    if b > 0:
        return a // b
    else:
        raise ZeroDivisionError


a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

try:
    c = div(a, b)
    print(c)
except ZeroDivisionError:
    print('Zero division error')
