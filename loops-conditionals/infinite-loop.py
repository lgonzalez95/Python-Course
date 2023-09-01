# while True:
#     n = int (input("Enter a number: "))
#     if(n>0):
#         print("Positive")
#     elif (n<0):
#         print("negative")
#     else:
#         break

# Pass = do nothing
# Continue = skip the rest of the current iteration
count = 0
while count < 10:
    n = int(input("Enter a number: "))
    if n % 3 == 0:
        pass
    else:
        print(count)
    count += 1

while count < 10:
    n = int(input("Enter a number: "))
    if n % 3 == 0:
        continue
    else:
        print(count)
    count += 1