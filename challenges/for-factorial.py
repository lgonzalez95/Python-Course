num = int(input("Enter a number to show its factorial: "))
sum = 1

for x in range(1, num):
    sum += sum*x

print("The factorial of", num, " is", sum)
