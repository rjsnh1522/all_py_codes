

def index_of_last_occurrence_of(arr, elem):
    lo = 0
    hi = len(arr) - 1
    res = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == elem:
            res = mid
            lo = mid + 1
        elif arr[mid] > elem:
            hi = mid - 1
        else:
            lo = mid + 1
    return res

arr = [2, 4, 4, 10, 10, 10, 18, 18, 20, 90, 90]
elem = 18
result = index_of_last_occurrence_of(arr, elem)
print(result)

