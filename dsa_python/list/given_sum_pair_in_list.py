
def pair_with_given_sum(gs, array_list):
    array_list.sort()
    left = 0
    right = len(array_list) - 1
    pairs = []
    while left < right:
        if array_list[left] + array_list[right] > gs:
            right -= 1
        elif array_list[left] + array_list[right] < gs:
            left += 1
        else:
            pairs.append((array_list[left], array_list[right]))
            left += 1
    return pairs

array_list = [1,2,3,4,9,10]
gs = 11
print(pair_with_given_sum(gs, array_list))
