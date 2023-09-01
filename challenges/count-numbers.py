count = 0
num = int(input("Enter the number to display its multiplication table: "))

while num > 0:
    num = num //10
    count+=1

print("There are", count, "digits")