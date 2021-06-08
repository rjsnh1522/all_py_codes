# find index of arr where arr[i] == i


def solve(arr):
    lo = 0
    hi = len(arr) - 1
    res = -1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == mid:
            return mid
        if arr[mid] > mid:
            hi = mid - 1
        else:
            lo = mid + 1
    return res

arr = [-1, 0, 1, 3, 5, 10]
result = solve(arr)
print(result)
