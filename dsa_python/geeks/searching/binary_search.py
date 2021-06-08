

def binary_search(arr, elem):
    lo = 0
    hi = len(arr) - 1
    res = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == elem:
            res = mid
            return res
        if arr[mid] > elem:
            hi = mid - 1
        else:
            lo = mid + 1
    return res


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elem = 10
result = binary_search(arr, elem)
print(result)

