import multiprocessing

def square_list(mylist, result, square_sum):
    for idx,num in enumerate(mylist):
        result[idx] = num * num
    square_sum.value = sum(result)
    print(f"ram in f1 {ram}")
    print(f"Result in process p1 {result[:]}")
    print(f"Sum of squares in process {square_sum.value}")

def method2(mylist, ram):
    print(f"ram in f2 {ram}")
    print(result[:])

if __name__ == "__main__":
    mylist = [1,2,3,4]
    # creating Array of int data type with space for 4 integers 
    result = multiprocessing.Array('i', 4)
    # result = []
    # creating Value of int data type 
    square_sum = multiprocessing.Value('i')
    ram = "ssd"
    p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum, ))
    p2 = multiprocessing.Process(target=method2, args=(mylist, ram))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Result(in main program): {}".format(result[:])) 
    print("Sum of squares(in main program): {}".format(square_sum.value)) 


