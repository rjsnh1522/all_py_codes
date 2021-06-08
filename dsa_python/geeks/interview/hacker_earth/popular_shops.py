from heapq import nlargest


def popular_shop(l, r, make_dict):
    for i in range(l, r+1):
        make_dict[i] += 1


t = int(input())
for j in range(t):
    n_m = list(map(int, input().strip().split()))
    n = n_m[0]
    m = n_m[1]
    make_dict = {i + 1: 0 for i in range(n)}
    for i in range(m):
        arr_el = list(map(int, input().strip().split()))
        l = arr_el[0]
        r = arr_el[1]
        popular_shop(l, r, make_dict)
    three_largest = nlargest(3, make_dict, key=make_dict.get)
    three_largest.sort()
    for i in three_largest:
        print(i, end=" ")



# input
# 1
# 6 5
# 3 5
# 2 3
# 4 6
# 1 6
# 5 6
# out put
# 3 4 5
