


# solution is in n2 n square

def water_volume(arr):
    n = len(arr)
    res = 0
    for i in range(0, n-1):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        right = arr[i]
        for j in range(i+1, n):
            right = max(right, arr[j])

        res = res + (min(left, right) - arr[i])
    return res



def water_trapping_with_o_n_solution(arr):
    size = len(arr)
    left = [0]*size
    right = [0]*size
    water = 0

    left[0] = arr[0]
    for i in range(1, size):
        left[i] = max(left[i-1], arr[i])

    right[size-1] = arr[size-1]
    for i in range(size-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    print(left)
    print(right)
    for i in range(0, size):
        water = water + (min(left[i], right[i]) - arr[i])

    return water


arr = [0, 1, 0, 2, 1, 0,1, 3, 2, 1, 2, 1]
# arr = [3, 0, 0, 2, 0, 4]
# print(water_trapping_with_o_n_solution(arr))

# print(water_volume(arr))


def water_tapping_prob_with_o_one_space_and_o_n_time(arr):
    size = len(arr)
    lo = 0
    hi = size-1
    low_max = 0
    high_max = 0
    total = 0

    while lo <= hi:
        if arr[lo] < arr[hi]:
            if arr[lo] > low_max:
                low_max = arr[lo]
            else:
                total += low_max - arr[lo]
            lo += 1
        else:
            if arr[hi] > high_max:
                high_max = arr[hi]
            else:
                total += high_max - arr[hi]
            hi -= 1

    return total

print(water_tapping_prob_with_o_one_space_and_o_n_time(arr))
