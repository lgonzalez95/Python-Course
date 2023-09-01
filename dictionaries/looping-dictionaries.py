dict1 = {100: "Production", 101: "Accounts", 102: "Sales", 104: "Inventory"}

for x in dict1:
    print(x, dict1[x])# Does give error if the element is not found

print()

for x in dict1:
    print(x, dict1.get(x))# Does not give error if the element is not found

key = "Invalid"
print(dict1.get(key, "%s element not found" %key))

for x in dict1.keys():
    print(x)

for x in dict1.values():
    print(x)

for x in dict1.items():
    print(x)