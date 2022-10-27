import time
import threading

locker = threading.Lock()


def blocked():
    print("Blocking Thread...")
    locker.acquire()
    print("Unblocking Thread...")


# t1 = threading.Thread(target=blocked)
# t2 = threading.Thread(target=blocked)
# t1.start()
# t2.start()

# First thread block blocked function
# Second thread can't work
# Thread can be unblocked with any thread
# ipython -i thread_sync_rlock.py
# locker.release()


# When we use RLock only thread that blocked can unblock function

#
r_locker = threading.RLock()


def r_blocked():
    print("Blocking Thread...")
    r_locker.acquire()
    print("Unblocking Thread...")


t1 = threading.Thread(target=r_blocked)
t2 = threading.Thread(target=r_blocked)
t1.start()
t2.start()

# ipython -i thread_sync_rlock.py
# r_locker.release()
