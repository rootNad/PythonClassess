# Semaphore is counter
# Using semaphores we can limit
# The number of threads
import random
import time
from threading import Thread, BoundedSemaphore, current_thread

max_connection = 5
pool = BoundedSemaphore(value=max_connection)


def test():
    with pool:
        spl = random.randint(1, 5)
        print(f"{current_thread().name} - sleep ({spl})")
        time.sleep(spl)


for i in range(10):
    Thread(target=test, name=f"thr-{i}").start()
