

def rotated_sorted_array(arr, key):
    lo = 0
    hi = len(arr) - 1
    res = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            res = mid
            return res
        if arr[mid] <= arr[hi]:
            if key > arr[mid] and key <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        elif arr[mid] >= arr[lo]:
            if key < arr[mid] and key >= arr[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
    return res


# arr = [12, 14, 18, 21, 3, 6, 8, 9]
# arr = [73, 85, 94, 21, 27, 34, 47, 54, 66]
arr = [186, 192, 193, 202, 204, 2, 3, 6, 10, 11, 12, 17, 21, 28, 29, 30, 31, 32, 37,
        38, 39, 40, 41, 47, 49, 50, 51, 52, 55, 57, 58, 59, 60, 65, 67, 68, 71, 72, 74,
        77, 78, 80, 82, 83, 88, 89, 90, 94, 100, 107, 108, 109, 111, 112, 114, 115, 116,
        118, 119, 121, 123, 124, 126, 129, 133, 134, 135, 137, 138, 144, 147, 148, 150, 151,
        154, 156, 159, 161, 163, 165, 166, 167, 168, 169, 174, 178, 180, 182, 183, 185]
elem = 73
elem = 143
result = rotated_sorted_array(arr, elem)
print(result)

