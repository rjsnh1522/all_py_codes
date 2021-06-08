import math


def solution(row_n, col_m):
    if row_n == 1 and col_m == 1:
        return 1
    if row_n == 0 or col_m == 0:
        return 0
    return solution(row_n-1, col_m) + solution(row_n, col_m-1)

print(solution(4, 4))



def sol2(row_n, col_m):
    ways = (row_n + col_m - 2)
    m = min(row_n, col_m)
    num = 1
    for i in range(ways, ways-m, -1):
        num *= i
    return num // math.factorial(m)

print(solution(4, 4))
