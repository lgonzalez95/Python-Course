food = ["pizza", "nuggests", "hotdog", "noodles", "pasta", "burguer"]

letter = input("Enter a letter to find its food: ")
food_found = []
for x in food: 
    if x[0].casefold() == letter.casefold():
        food_found.append(x)

if(len(food_found) > 0):
    print("We found: " + ", ".join(food_found))
else:
    print("There was no food found for the letter %s!" %(letter))