
arr = [3, 1, 2, 4, 0, 1, 3, 2]
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
arr = [4, 2, 0, 3, 2, 5]


def water_trapped(arr):
    left_aux = []
    right_aux = []
    curr_left_max = arr[0]
    curr_right_max = arr[-1]

    for i in arr:
        if i >= curr_left_max:
            curr_left_max = i
        left_aux.append(curr_left_max)

    for i in range(len(arr)-1, -1, -1):
        if arr[i] >= curr_right_max:
            curr_right_max = arr[i]
        right_aux.insert(0, curr_right_max)

    trapped_water = 0
    for i in range(len(left_aux)):
        trapped_water += (min(left_aux[i], right_aux[i]) - arr[i])
    return trapped_water


print(water_trapped(arr))

