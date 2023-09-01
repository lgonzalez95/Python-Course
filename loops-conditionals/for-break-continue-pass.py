for x in range(11):
    if x > 5:
        break
    else:
        print(x)


for x in range(11):
    if x > 5:
        break
else:
    print("Hi")


for x in range(11):
    print(x)
else:
    print("For completed")


for x in range(11):
    pass

print("Program ended")


for x in range(11):
    if x % 5 == 0:
        continue
    print(x)

print("Continue ended")
