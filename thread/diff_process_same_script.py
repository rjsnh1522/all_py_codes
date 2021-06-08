import multiprocessing
import os
import time


def worker1():
    print("I am start now")
    # time.sleep(10)
    print(f"id of process running worker 1 {os.getpid()}")


def worker2():
    print("I am 2")
    print(f"id of process worker2 {os.getpid()}")


if __name__ == "__main__":
    print(f"id of process main {os.getpid()}")
    p1 = multiprocessing.Process(target=worker1)
    p2 = multiprocessing.Process(target=worker2)
    p1.start()
    p2.start()
    print(f"ID of process p1 {p1.pid}")
    print(f"ID of process p2 {p2.pid}")
    p1.join()
    p2.join()
    print(f"Process p1 is alive {p1.is_alive()}") 
    print(f"Process p2 is alive {p2.is_alive()}")




