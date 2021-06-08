import multiprocessing


result = []
def square_list(mylist):
    # global result
    for num in mylist:
        result.append(num * num)
    print(f"result in process p1 {result}")


if __name__ == '__main__':
    mylist = [1,2,4,5,56,7,4]
    p1 = multiprocessing.Process(target=square_list, args=(mylist, ))
    p1.start()
    p1.join()
    print(f"Result in Main {result}")
