nums = [1, 2, 3, 4, 5, 6, 7, 8, 10]


def find_missing_num(given_list):
    for x in range(0, len(given_list) + 2):
        if given_list[x] + 1 is not given_list[x + 1]:
            return given_list[x] + 1
    else:
        return -1


def find_missing_num_2(given_list):
    start = given_list[0]
    end = given_list[len(given_list) - 1]
    actual_list = list(range(start, end + 1))

    return sum(actual_list) - sum(nums)


print(find_missing_num(nums))
print(find_missing_num_2(nums))
