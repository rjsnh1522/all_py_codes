

def the_maximum_sum(arr, size_of_arr):
    lent = size_of_arr
    for i in range(lent):
        if i+1 < lent:
            if arr[i] > arr[i+1]:
                arr[i] = arr[i+1]
            else:
                rp = 0
                while rp < i:
                    if arr[i] < arr[rp]:
                        arr[rp] = arr[i]
                    rp += 1
        if i+1 == lent:
            if arr[i-1] > arr[i]:
                arr[i-1] = arr[i]
    print(arr)
    return sum(arr)



aaa = [1, 5, 2, 5, 4]
print(the_maximum_sum(aaa, len(aaa)))

# t = int(input())
# for j in range(t):
#     size_of_arr = int(input())
#     arr_el = list(map(int, input().strip().split()))
#     print(the_maximum_sum(arr_el, size_of_arr))
