# Iterators
L = [1, 2, 3, 4, 5]
T = (1, 2, 3, 4, 5)
S = {1, 2, 3, 4, 5}
D = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}

itr = iter(L)
itr2 = iter(T)
itr3 = iter(S)
itr4 = iter(S)

print(next(itr))
print(next(itr))

print(next(itr2))
print(next(itr2))

print(next(itr3))
print(next(itr3))

print(next(itr4))
print(next(itr4))


# Our own generator function
def days_week():
    i = 0
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    while True:
        x = days[i]
        i = (i + 1) % 7
        yield x


d = days_week()
print(next(d))
print(next(d))
print(next(d))
