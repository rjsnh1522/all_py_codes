
# def find_similar_in_3_arrays(a, b, c):
#     ii, jj, kk = 0, 0, 0
#     result = []
#     while (ii <= len(a)) and (jj <= len(b)) and (kk <= len(c)):
#         ii
#         if a[ii] > b[jj] and a[ii] > c[kk]:
#             print("a i ", a[ii])
#             jj += 1
#             kk += 1
#         elif b[jj] > a[ii] and b[jj] > c[kk]:
#             print("b j ", b[jj])
#             ii += 1
#             kk += 1
#         elif c[kk] > a[ii] and c[kk] > b[jj]:
#             print("c k ", c[kk])
#             ii += 1
#             jj += 1
#         elif a[ii] == b[jj] == c[kk]:
#             print("equal ", a[ii])
#             result.append(a[ii])
#             maxer = max(max(ii, jj), kk)
#             ii, jj, kk = maxer, maxer, maxer
#         else:
#             print(result)
#             import ipdb; ipdb.set_trace()
#     print(result)




def find_common(a, b, c):
    ii, jj, kk = 0, 0, 0
    results = []
    while ii < len(a):
        if a[ii] > b[jj] and a[ii] > c[kk]:
            while jj < len(b) and b[jj] < a[ii]:
                jj += 1
            while kk < len(c) and c[kk] < a[ii]:
                kk += 1
        if jj < len(b) and kk < len(c) and a[ii] == b[jj] == c[kk]:
            results.append(a[ii])

        ii += 1
    return results

a = [1, 6, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 6, 15, 20, 30, 70, 80, 120]
# aa = [12, 30, 50]
# bb = [10, 30, 50]
# cc = [25, 30]
# print(find_common(a, b, c))
print(find_common(a, b, c))
ans = [20, 80]
