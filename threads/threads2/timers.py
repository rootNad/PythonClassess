import threading
import time


def test():
    while True:
        print("test")
        time.sleep(1)


# Thread starts after 10 seconds
# thr = threading.Timer(10, test)
# thr.start()
#
#
# # Time don't block main thread
# while True:
#     print("111")
#     time.sleep(2)


thr = threading.Timer(5, test)
thr.start()

for _ in range(3):
    print("111")
    time.sleep(1)

# To stop thread before finish use
thr.cancel()
print("finish")
"""

"""