# def solution(arr, size):
#     for i in range(size):
#         l_sum = 0
#         r_sum = 0
#         for j in range(i):
#             l_sum += arr[j]
#
#         for j in range(i+1, size):
#             r_sum += arr[j]
#
#         if l_sum == r_sum:
#             return arr[i]
#     return -1


def solution(arr, size):
    leftsum = 0
    total = sum(arr)
    print(total)
    for i in range(size):
        total -= arr[i]
        if leftsum == total:
            return i+1
        leftsum += arr[i]
    return -1

t = int(input())

for r in range(t):
    size_of_arr = int(input())
    arr_el = list(map(int, input().strip().split()))
    leader_list = solution(arr_el, size_of_arr)
    print(leader_list)
