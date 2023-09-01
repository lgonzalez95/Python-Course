reversed = 0
inialNum = int(input("Enter the number to reverse it: "))
num = inialNum
while num > 0:
    r = num % 10
    num = num//10
    reversed = reversed * 10 + r

print("The reversed number is ",reversed)

if inialNum == reversed:
    print ("The number is a palindrome")