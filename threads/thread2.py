import time
import threading


def get_data(data):
    while True:
        print(f"[{threading.current_thread().name} - {data}]")
        time.sleep(1)


thr = threading.Thread(
    target=get_data,
    args=(str(time.time()), ),
    name="thr-1"
)

thr.start()

for i in range(100):
    print(f"Current: {i}")
    time.sleep(1)

    if i % 10 == 0:
        print(f"active thread: {threading.active_count()}")
        print(f"enumerate: {threading.enumerate()}")
        print(f"thr-1 is alive: {thr.is_alive()}")


# Get main thread
# print(f"Main thread name: {threading.main_thread().name}")
# threading.main_thread().name = "NewMainThreadName"
# print(f"Result: {threading.main_thread().name}")