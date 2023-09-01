"""
copy: Copies a dictiorary and returns it
update(iterable): Adds elements from one dictionary to another dictionary
setdefault(key, default): If the key doesn't exist, it creates a new key-value pair with a default value and returns that value.
fromkeys(sequence, value): Creates a new dictionary where the keys are taken from a sequence or iterable, and values are set to a specified value
pop(key, default): Deletes an element
popItem(): Removes the last item inserted
clear(): Removes all elements from the dictionary
"""
dict1 = {100: "Production", 101: "Accounts", 102: "Sales", 104: "Inventory"}
dict3 = {105: "Designing"}

dict2 = dict1.copy()
print(dict2)

dict1.update(dict3) 

dict3.setdefault(500, "Default")
print(dict3)
print(dict3.setdefault(500))

L1 = ["JUAN", True, 55.50, 10]

dict4 = {}
dict4 = dict4.fromkeys(L1, "VALUE")
print(dict4)

dict4.pop("JUAN")
print(dict4)

print(dict4.pop("JUAN", "JUAN is not found"))

dict4.popitem()
print(dict4)