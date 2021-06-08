
inv_count = 0

def sorter(l_res , r_res):
    global inv_count
    i = 0
    r = 0
    results = []
    while i < len(l_res) and r < len(r_res):
        if l_res[i] > r_res[r]:
            results.append(r_res[r])
            inv_count += len(l_res) - i
            r += 1
        else:
            results.append(l_res[i])
            i += 1

    while i < len(l_res):
        results.append(l_res[i])
        i += 1

    while r < len(r_res):
        results.append(r_res[r])
        r += 1

    return results


def divider(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    l_arr = arr[0:mid]
    r_arr = arr[mid:]
    l_res = divider(l_arr)
    r_res = divider(r_arr)
    arr = sorter(l_res, r_res)
    return arr


A = [6, 5, 2, 1, 5, 6]
res = divider(A)
print(inv_count)



#
# def brute_force(arr):
#     arr = A
#     lent = len(arr)
#     inv_c = 0
#     for i in range(lent):
#         for j in range(i+1, lent):
#             if arr[i] > arr[j]:
#                 inv_c += 1
#     return inv_c % (10**7 + 7)
#
#
# A = [1, 2, 3, 4, 5, 6]
# res = brute_force(A)
# print(res)

