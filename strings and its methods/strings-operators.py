"""
concatenation
repetition
indexing
slicing
in
not in
"""

#concatenation
string = "Hello world!"
print(string + str(15))

#repetition
print(string * 3)

#indexing
print(string[1])
print(string[-1])

for i in range(0, len(string)):
    print(string[i])

#slicing
#string[start:end:step]
print(string[0: 5: 1])
print(string[0: 5: 2])
print(string[::])
print(string[::-1])



#in
print("Hello" in string)
#not in
print("#" not in string)