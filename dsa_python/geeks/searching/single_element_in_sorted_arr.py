# Given a sorted array of integers A where every element appears twice except for one
# element which appears once, find and
# return this single element that appears only once.


def solution(arr):
    lo = 0
    hi = len(arr) - 1
    max_hi = hi
    res = -1

    if len(arr) % 2 == 0:
        return res
    while lo < hi:
        mid = (lo + hi) // 2

        if mid % 2 == 0:
            if arr[mid+1] == arr[mid] and mid != 0 and mid != max_hi:
                lo = mid + 1
            else:
                hi = mid
        else:
            if arr[mid-1] == arr[mid] and mid != 0 and mid != max_hi:
                lo = mid + 1
            else:
                hi = mid

        if lo == hi:
            return arr[lo]
    return res

arr = [1,1,2]
result = solution(arr)
print(result)
