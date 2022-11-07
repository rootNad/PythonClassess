import time
import random
from threading import Thread, Barrier, current_thread


def test(barrier):
    slp = random.randint(13, 17)
    time.sleep(slp)
    print(f"Thread [{current_thread().name}] starts at ({time.ctime()})")

    # All threads must call wait
    # If one thread don't call wait
    # Barrier block all threads
    # And wait until the last thread calls wait
    barrier.wait()  # waits for all threads to run
    print(f"Thread [{current_thread().name}] overcame the barrier at ({time.ctime()})")


bar = Barrier(5)
for i in range(5):
    Thread(target=test, args=(bar,), name=f"thr-{i}").start()
