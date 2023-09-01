from threading import *
from time import *


def display(str):
    lock.acquire()  # Mutex synchronisation
    for x in str:
        print(x)
        sleep(0.3)
    lock.release()  # Mutex synchronisation


lock = Lock()  # Mutex synchronisation: Allows only 1 thread to access the resource
t1 = Thread(target=display, args=('HELLO WORLD',))  # Race condition since both threads try to use the same function
t2 = Thread(target=display, args=('you are welcome',))  # Race condition since both threads try to use the same function

t1.start()
t2.start()
t1.join()
t2.join()
