from collections import deque

d = [1, 2, 3, 4, 5]
dq = deque(d)

dq.append(6)
dq.appendleft(0)
print(dq)

dq.pop()
dq.popleft()
print(dq)

dq.extend([6, 7, 8])
dq.extendleft([0, -1, -2])
print(dq)

dq.rotate(3)
print(dq)

dq.insert(5, 50)
print(dq)