fav1 = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']
fav2 = ['burger', 'hotdog', 'noodles', 'pasta', 'nuggets', 'pizza']

minIndex = 99
for x in fav1:
    if (fav2.index(x)+fav1.index(x) < minIndex):
        minIndex = fav2.index(x)+fav1.index(x)
        dish = x

print("They should order "+ dish)