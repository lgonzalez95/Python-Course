def invert_dictionary(dictionary):
    return dict(zip(dictionary.values(), dictionary.keys()))


dict1 = {'a': 1, 'b': 2, 'c': 3}

print(invert_dictionary(dict1))
