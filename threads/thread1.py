import time
import threading


def get_data(data):
    while True:
        print(f"[{threading.current_thread().name} - {data}]")
        time.sleep(0.1)


thr1 = threading.Thread(
    target=get_data,
    args=(str(time.time()), ),
    name="thr-1",
    daemon=False
)

thr1.start()

for i in range(10):
    print(f"Current: {i}")
    time.sleep(0.1)