reversed = 0
num = int(input("Enter the number to reverse it: "))

while num > 0:
    r = num % 10
    num = num//10
    reversed = reversed * 10 + r

print("The reversed number is ",reversed)