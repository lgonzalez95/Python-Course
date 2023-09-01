from threading import *
from time import *
from queue import *

queue = Queue()


def producer(data):
    i = 1
    while True:
        data.put(i)
        print('Producer has produced', i)
        i += 1
        sleep(0.1)


def consumer(data):
    while True:
        x = data.get()
        print('Consumer has got', x)
        sleep(0.1)


t1 = Thread(target=lambda: producer(queue))
t2 = Thread(target=lambda: consumer(queue))

t1.start()
t2.start()
t1.join()
t2.join()
