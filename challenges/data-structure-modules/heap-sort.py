import heapq

elements = [10, 50, 201, 43, 2, 54, 30, 20]
heapq.heapify(elements)


def sort_heapq(list):
    new_list = []
    for x in range(len(list)):
        new_list.append(heapq.heappop(list))
    return new_list


print(sort_heapq(elements))
