count = 0
for i in range(1, 101):
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i, "is prime")
    count = 0
