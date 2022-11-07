import threading
import time

event = threading.Event()  # Event contains only True/False


# By default Event contains False


def test():
    while True:
        event.wait()  # Wait to True
        print("Test")
        time.sleep(2)


event.clear()  # EVENT SET FALSE
threading.Thread(target=test).start()

# ipython -i event.py
# threading.active_count()
# threading.enumerate()
# event.is_set() - show if thread are True
# event.set() - set event to True (start thread)
# event.clear() - set event to False

