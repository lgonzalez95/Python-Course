L = [10, 20, 30, 40, 50]


try:
    index = int(input('Enter a list index: '))
    print(L[index])
except (IndexError, ValueError) as msg:
    print('An error has occurred:', msg)

print('Program finished')
