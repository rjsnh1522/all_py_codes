
arr = [1, 2, 3, 4, 5, 6]
n = 7

def missing_number(arr, n):
    total = n*(n+1)//2
    sum_ = 0
    for i in range(len(arr)):
        sum_ += arr[i]
    return total - sum_


t = int(input())

for i in range(t):
    size_of_arr = int(input())
    arr_el = list(map(int, input().strip().split()))
    print(missing_number(arr_el, size_of_arr))



