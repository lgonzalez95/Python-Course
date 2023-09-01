import heapq

elements = [10, 50, 201, 43, 2, 54, 30, 20]
heapq.heapify(elements)


def sort_heapq(list, k):
    new_list = []
    for x in range(len(list)):
        new_list.append(heapq.heappop(list))
    print('Sorted list', new_list)
    new_list.reverse()
    return new_list[k-1]


print('Kth largest element is', sort_heapq(elements, 5))
