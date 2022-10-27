import time
import threading


def get_data(data):
    for _ in range(5):
        print(f"[{threading.current_thread().name}] - {data}")
        time.sleep(1)


thr = threading.Thread(
    target=get_data,
    args=(str(time.time()), ),
    daemon=False
)

thr_deamon = threading.Thread(
    target=get_data,
    args=(str(time.time()), ),
    daemon=True
)

# thr.start()
# print("finish thr")
# Program with thread finish when all thread are finish their work

thr_deamon.start()
time.sleep(1)
print("finish deamon")
# Deamon finish when main thread are finished
