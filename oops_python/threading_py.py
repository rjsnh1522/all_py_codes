
# race condition

import threading
import os
for i in range(os.cpu_count()):
    print(i)




#
# import threading
# x = 0
#
#
# def thread_task(lock):
#     global x
#     for i in range(1000000):
#         lock.acquire()
#         x += 1
#         lock.release()
#
#
# def main_task():
#     lock = threading.Lock()
#     t1 = threading.Thread(target=thread_task, args=(lock,))
#     t2 = threading.Thread(target=thread_task, args=(lock,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#
#
# main_task()
# print(x)
















# import threading
# import concurrent.futures
# import time
#
# start_time = time.perf_counter()
#
#
# def do_something(num):
#     print('sleeep 1 sec ', num, end="\n")
#     time.sleep(num)
#     return f'done sleeping {num}'
#
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     # for i in range(10):
#     #     f1 = executor.submit(do_something, i)
#     #     print(f1.result())
#     secs = [5,4,3,2,1]
#     results = [executor.submit(do_something, sec) for sec in secs]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())












#
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
#
#
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()

#
# threads = []
# for i in range(10):
#     t1 = threading.Thread(target=do_something, args=[i])
#     t1.start()
#     threads.append(t1)
# for th in threads:
#     th.join()

# fin = time.perf_counter()
# print(f"finished in {round(fin-start_time)} seconds")
