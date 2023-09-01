terms = int(input("Enter a number to show its fibonacci series: "))

first = 0
second = 1
for x in range(terms+1):
    print(first)
    aux = first + second
    first = second
    second = aux