from threading import *
from time import *


class MyData:
    def __init__(self):
        self.data = 0
        self.is_there_new_data = False
        self.lock = Lock()

    def put(self, data):
        while self.is_there_new_data:
            pass
        self.lock.acquire()
        self.data = data
        self.is_there_new_data = True
        self.lock.release()

    def get(self):
        while not self.is_there_new_data:
            pass
        self.lock.acquire()
        data = self.data
        self.is_there_new_data = False
        self.lock.release()
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
