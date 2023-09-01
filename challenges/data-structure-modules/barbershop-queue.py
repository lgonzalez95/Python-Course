from collections import deque

dq = deque([])


def walk_in(customer):
    dq.append(customer)
    print('A new client has joined to the queue: ', dq)


def serviced():
    leaves = dq.popleft()
    print(leaves, 'was served, the following clients are still waiting: ', dq)


walk_in("Juan")
walk_in("Maria")
walk_in("Sofia")
walk_in("Luis")

serviced()
serviced()