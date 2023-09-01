def find_highest_product(elements):
    sorted_elements = sorted(elements)
    last_element = len(sorted_elements) - 1
    before_last = len(sorted_elements) - 2
    return (sorted_elements[before_last]), (sorted_elements[last_element])


input_1 = {2, 4, -16, 8, 3, 7, -9}
input_2 = {0, -1, -3, -5, -8, 2, 4}

print(find_highest_product(input_1))
print(find_highest_product(input_2))
