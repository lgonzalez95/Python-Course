from collections import deque

students = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def serve_meal(dq):
    dq.rotate(-1)
    print(dq)


serve_meal(students)
serve_meal(students)
serve_meal(students)
serve_meal(students)