from datetime import *

starting_time = datetime.now()
for i in range(0, 100000000):
    pass
ending_time = datetime.now()
exec_time = ending_time - starting_time

print('Execution time:', exec_time.seconds, ':', exec_time.microseconds)
