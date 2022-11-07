import time
import threading

condition = threading.Condition()


def f1():
    while True:
        with condition:
            # Block f2 from f1
            condition.wait()  # Wait for notification
            print("f2: Get event")


def f2():
    for i in range(100):
        if i % 10 == 0:
            with condition:
                condition.notify()  # Unblock f1 from f2
        else:
            print(f"f1: {i}")
        time.sleep(0.2)


threading.Thread(target=f1).start()
threading.Thread(target=f2).start()