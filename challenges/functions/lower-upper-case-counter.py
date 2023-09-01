def count_letters(phrase):
    upper = 0
    lower = 0
    for x in phrase:
        if x.islower():
            lower += 1
        elif x.isupper():
            upper += 1

    return lower, upper

print(count_letters("HeasdASDl"))
