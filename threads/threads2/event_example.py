import time
import threading


event = threading.Event()


def image_handler():
    thr_num = threading.current_thread().name
    print(f"Processing image from thread - [{thr_num}]")
    # Block all threads until image processing
    event.wait()
    print("Image send to server")


for i in range(10):
    threading.Thread(target=image_handler, name=f"thr - {i}").start()
    print(f"Thread [{i}] is started!")
    time.sleep(1)

if threading.active_count() >= 10:
    # If >=10 threads process image continue thread work
    event.set()
