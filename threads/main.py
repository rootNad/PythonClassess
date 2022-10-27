import time
import threading


def get_data(data):
    print(f"[{threading.current_thread().name} - {data}]")
    time.sleep(2)

# get_data(str(time.time()))
thr = threading.Thread(
    target=get_data,
    args=(str(time.time()), ),
    name="thr-1"
)

thr.start()