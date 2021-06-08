

def find_occurrence_of_an_ele_in_sorted_arr(arr, elem):
    lo = 0
    hi = len(arr) - 1
    first_occ = -1
    count = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == elem:
            first_occ = mid
            hi = mid - 1
        elif arr[mid] > elem:
            hi = mid - 1
        else:
            lo = mid + 1

    lo = 0
    hi = len(arr) - 1
    last_occ = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == elem:
            last_occ = mid
            lo = mid + 1
        elif arr[mid] > elem:
            hi = mid - 1
        else:
            lo = mid + 1

    if last_occ != -1 and first_occ != -1:
        return (last_occ - first_occ) + 1
    return count


arr = [2, 4, 4, 10, 10, 10, 18, 18, 20, 90, 90]
elem = 18
result = find_occurrence_of_an_ele_in_sorted_arr(arr, elem)
print(result)

