
def total_water_trapped(arr):
    size = len(arr)
    left_arr = [0] * size
    right_arr = [0] * size
    water = 0
    left_arr[0] = arr[0]
    right_arr[size-1] = arr[size-1]
    for i in range(size):
        left_arr[i] = max(arr[i], left_arr[i-1])

    for i in range(size - 2, -1, -1):
        right_arr[i] = max(right_arr[i + 1], arr[i])

    for i in range(size):
        water += (min(left_arr[i], right_arr[i]) - arr[i])

    return water


A = [0,1,0,2,1,0,1,3,2,1,2,1]
size = 12

print(total_water_trapped(A))
