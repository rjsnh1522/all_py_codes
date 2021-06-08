def solution(arr, size):
    leader_list = list()
    leader_now = arr[size - 1]
    for i in range(size - 1, -1, -1):
        if leader_now <= arr[i]:
            leader_now = arr[i]
            leader_list.append(leader_now)
    return leader_list


t = int(input())

for i in range(t):
    size_of_arr = int(input())
    arr_el = list(map(int, input().strip().split()))
    leader_list = solution(arr_el, size_of_arr)
    for i in range(len(leader_list) - 1, -1, -1):
        print(leader_list[i], end=" ")
    print()


