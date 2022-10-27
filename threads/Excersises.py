import threading
import time

"""
    Write a programm using two threads
    such that one writes even numbers in increasing order
    and the other odd numbers in increasing order.
    Example:
        input -> 3
        Output ->
                    T-Even 0
                    T-Odd 1
                    T-Even 2
                    T-Odd 3
"""


def thread_function(name, max, y):
    print(name, y)
    time.sleep(0.1)
    for i in range(int(max / 2)):
        time.sleep(0.3)
        y = y + 2
        print(name, y)


n = int(input("Input an integer \n"))
p = 0

mt1 = threading.Thread(
        target=thread_function,
        args=("T-Even", n, p, )
)
mt2 = threading.Thread(
    target=thread_function,
    args=("T-Odd", n, p+1, )
)

mt1.start()
time.sleep(0.1)
mt2.start()

mt1.join()