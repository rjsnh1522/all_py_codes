

def wave_form_array_sort(arr):
    size = len(arr)
    arr.sort()
    for i in range(size):
        if i != size-1:
            if i % 2 == 0:
                if arr[i] <= arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                if arr[i] >= arr[i+1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


arr = [9, 11, 3, 4, 5, 2, 4, 4, 5, 0, 9]
# arr = [1, 2, 3, 4]
print(wave_form_array_sort(arr))
