from threading import *
from time import *


class MyData:
    def __init__(self):
        self.data = 0
        self.condition_var = Condition()

    def put(self, data):
        self.condition_var.acquire()
        self.condition_var.wait(timeout=0)
        self.data = data
        self.condition_var.notify()
        self.condition_var.release()

    def get(self):
        self.condition_var.acquire()
        self.condition_var.wait(timeout=0)
        data = self.data
        self.condition_var.notify()
        self.condition_var.release()
        return data


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


data = MyData()
t1 = Thread(target=lambda: producer(data))
t2 = Thread(target=lambda: consumer(data))

t1.start()
t2.start()
t1.join()
t2.join()
