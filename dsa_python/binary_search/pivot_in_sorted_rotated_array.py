

def find_pivot(array_list, low, high):
    if low > high:
        return -1
    if high == low:
        return low
    mid = (low + high)//2

    if mid < high and array_list[mid] > array_list[mid+1]:
        return mid

    if mid > low and array_list[mid] < array_list[mid-1]:
        return mid - 1

    if array_list[low] >= array_list[mid]:
        return find_pivot(array_list, low, mid-1)
    return find_pivot(array_list, mid+1, high)


array_list = [0, 1, 2, 4, 5, 6, 7]
print(find_pivot(array_list, 0, 6))
