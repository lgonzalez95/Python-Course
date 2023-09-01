from threading import *
from time import *


def display(str):
    lock.acquire()  # Semaphore synchronisation
    for x in str:
        print(x)
        sleep(0.1)
    lock.release()  # Semaphore synchronisation


lock = Semaphore(2)  # Semaphore synchronisation: Allows 2 threads to access the same resource
t1 = Thread(target=display, args=('HELLO WORLD',))  # Race condition since both threads try to use the same function
t2 = Thread(target=display, args=('you are welcome',))  # Race condition since both threads try to use the same function
t3 = Thread(target=display, args=('1234567890',))  # Race condition since both threads try to use the same function

t1.start()
t2.start()
t1.join()
t2.join()
t3.start()
t3.join()