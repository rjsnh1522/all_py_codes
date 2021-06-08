

def solution(arr, size, total):
    pass




t = int(input())

for i in range(t):
    n_s = list(map(int, input().strip().split()))
    size_of_arr = n_s[0]
    total_sum = n_s[1]
    arr_el = list(map(int, input().strip().split()))
    print(solution(arr_el, size_of_arr, total_sum))
