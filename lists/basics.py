"""
List is a mutable ordered collection of objects that can have duplicates
"""

myList = ["Juan", "Juanita", "Panchito", "Panchita"]
anotherList = list((1, 2, 3, 4, 5))
differentTyoes = ["Juan", 1, True, 50.35, 5+7j]

print(myList)
print(anotherList)
print(differentTyoes)

differentTyoes[0] = "Luis"
print(differentTyoes)