sum = 0
numberOfNums = int(input("How many numbers you want to sum? "))

while numberOfNums >0:
    sum+= int(input("Enter a number: "))
    numberOfNums-=1

print("The sum is ",sum)
