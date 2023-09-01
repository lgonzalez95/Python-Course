"""
Smaller numbers have the highest priority
"""
import heapq

hq = []  # 10, 50, 301, 20, 50, 30, 70, 5
heapq.heappush(hq, 10)
heapq.heappush(hq, 50)
heapq.heappush(hq, 301)
heapq.heappush(hq, 20)
heapq.heappush(hq, 50)
heapq.heappush(hq, 30)
heapq.heappush(hq, 70)
heapq.heappush(hq, 5)

print(heapq.heappop(hq))
print(hq)

print(heapq.heappop(hq))
print(hq)

print(heapq.heappop(hq))
print(hq)

l = [50, 30, 60, 40]
heapq.heapify(l)  # Converts a given list in the form of a heap
print(l)

print(heapq.nlargest(2, l))  # N greater numbers
print(heapq.nsmallest(2, l))  # N smaller numbers
