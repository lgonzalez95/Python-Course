import array

nums = [10, 20, 13, 14, 15, 13, 17, 10, 20, 13]
my_nums = array.array('i', nums)


def find_duplicate(array):
    s = set()
    for x in array:
        if x not in s:
            s.add(x)
        else:
            return x
    else:
        return -1


print(find_duplicate(my_nums))
