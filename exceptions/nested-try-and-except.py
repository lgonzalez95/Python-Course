try:
    a = int(input('Enter a number: '))
    b = int(input('Enter a number: '))
    try:
        c = a // b
        print(c)
    except ZeroDivisionError as e:
        print(e)
except ValueError:
    print('Value error')
