

def find_peak_in_unsorted_arr(arr):
    lo = 0
    hi = len(arr) - 1
    res = -1
    max_hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid == 0 and arr[mid] >= arr[mid+1]:
            return arr[mid]
        if mid == max_hi and arr[mid] >= arr[mid-1]:
            return arr[mid]
        if mid != 0:
            if arr[mid] >= arr[mid+1] and arr[mid] >= arr[mid-1]:
                return arr[mid]
            if arr[mid] >= arr[mid+1]:
                hi = mid - 1
            else:
                lo = mid + 1
    return res


arr = [1, 10, 10]
result = find_peak_in_unsorted_arr(arr)
print(result)

