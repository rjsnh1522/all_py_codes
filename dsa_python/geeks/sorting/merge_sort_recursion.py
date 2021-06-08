def sorting_merger(l_res, r_res):
    i = 0
    j = 0
    result = []
    while i < len(l_res) and j < len(r_res):
        if l_res[i] > r_res[j]:
            result.append(r_res[j])
            j += 1
        else:
            result.append(l_res[i])
            i += 1

    while i < len(l_res):
        result.append(l_res[i])
        i += 1

    while j < len(r_res):
        result.append(r_res[j])
        j += 1

    return result


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    left = arr[0:mid]
    right = arr[mid:]
    l_res = merge_sort(left)
    r_res = merge_sort(right)
    sorted_arr = sorting_merger(l_res, r_res)
    return sorted_arr


arrs = [7, 6, 5, 4, 3, 2, 1, 11, 31, 13]
res = merge_sort(arrs)
print(res)
