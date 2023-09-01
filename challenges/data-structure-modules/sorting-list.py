import bisect

elements = [2, 4, 6, 10, 1, 3, 5, 7, 9]


def insertion_sort(list):
    sorted_list = []
    for x in list:
        bisect.insort(sorted_list, x)
        print(sorted_list)
    return sorted_list


print(insertion_sort(elements))
