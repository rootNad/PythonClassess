import time
import threading

value = 0
locker = threading.Lock()


def inc_value():
    global value
    while True:
        locker.acquire()
        value += 1
        time.sleep(0.1)
        print(f"Value is: {value}")
        locker.release()

def inc_value_short():
    global value
    while True:
        with locker:
            value += 1
            time.sleep(1)
            print(f"Value is: {value}")


for _ in range(5):
    # threading.Thread(target=inc_value).start()
    threading.Thread(target=inc_value).start()


def blocked():
    print("Blocking Thread...")
    locker.acquire()
    print("Unblocking Thread...")
