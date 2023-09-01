import copy

l = [10, 20, 30, 40, 50]

# creates a new list with the same elements.
# The elements of the new list point to the same position of the original list
cp = copy.copy(l)
# Different Ids because a new list is created
print(id(l))
print(id(cp))

print()

# Same Ids because the elements are not new
print(id(l[0]))
print(id(cp[0]))

print()
print()

# creates a new list with new elements
fake_dcp = copy.deepcopy(l)  # Deep copy does not work with: int, float and str
# Different Ids because a new list is created
print(id(l))
print(id(fake_dcp))

print()

# Same Ids because Deep copy does not work with: int, float and str
print(id(l[0]))
print(id(fake_dcp[0]))

print()
print()


class Person:
    def __init__(self, name):
        self.name = name


people = [Person('Juan'), Person('Sofía')]
real_dcp = copy.deepcopy(people)

print(id(people))
print(id(real_dcp))

print()

# Different Ids because Deep copy DOES work with: data types different than int, float and str
print(id(people[0]))
print(id(real_dcp[0]))
