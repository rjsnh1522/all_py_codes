
def solution(arr, size):
    ele_count = dict()
    for i in range(0, size):
        if arr[i] in ele_count:
            ele_count[arr[i]] += 1
        else:
            ele_count[arr[i]] = 1

    found_ele = None
    for j in ele_count:
        if ele_count[j] > size//2:
            found_ele = j

    if found_ele is None:
        return -1
    else:
        return found_ele




t = int(input())

for i in range(t):
    size_of_arr = int(input())
    arr_el = list(map(int, input().strip().split()))
    print(solution(arr_el, size_of_arr))
