initial = int(input("Enter The initial term: "))
difference = int(input("Enter the common difference: "))
totalTerms = int(input("Enter how many terms you want: "))
sequence = ""
for x in range(initial, difference * totalTerms, difference ):
    sequence+= str(x) + ","

print(sequence)