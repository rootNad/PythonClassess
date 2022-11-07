import time
import threading

data = threading.local()
#
#
# def get():
#     print(data.value)
#
#
# # Data only in local thread(t1)
# def t1():
#     data.value = {
#         "value1": 1,
#         "value2": 2,
#         "value3": 3
#     }
#     print(f"t1: {data.value}")
#
#
# # Data only in local thread(t2)
# def t2():
#     data.test = ["test1", "test2", "test3"]
#     print(f"t2: {data.test}")
#
#
# threading.Thread(target=t1).start()
# threading.Thread(target=t2).start()


def get_name():
    print(data.name)


def t1():
    data.name = threading.current_thread().name
    get_name()


def t2():
    data.name = threading.current_thread().name
    get_name()


threading.Thread(target=t1, name="t1").start()
threading.Thread(target=t2, name="t2").start()
