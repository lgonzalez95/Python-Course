num = int(input("Enter a number to check whether it is prime: "))

count = 0
for x in range (1, num+1):
    if num % x == 0:
        count+=1
    else:
        pass 

if count == 2:
    print(num, "is prime")
else:
    print(num, "is not prime")