# # def solution(a,b):
# #     pass
# #
# #
# #
# #
# #
# # t = int(input())
# #
# # for i in range(t):
# #     size_of_arr = int(input())
# #     arr_el = list(map(int, input().strip().split()))
# #     print(solution(arr_el, size_of_arr))
#

class Solve:
    def solve(self, A):
        i = 0
        j = 0
        max_len = 0
        zeros = 1
        zero_one = {0: 0, 1: 0}
        while j < len(A):
            if A[j] == 1:
                zero_one[1] += 1
                max_len = max(max_len, (zero_one[0] + zero_one[1]))
                j += 1
            else:
                if zeros > 0:
                    zeros -= 1
                    zero_one[0] += 1
                    max_len = max(max_len, (zero_one[0] + zero_one[1]))
                    j += 1
                else:
                    if i < len(A):
                        zero_one[A[i]] -= 1
                        if A[i] == 0:
                            zeros += 1
                        i += 1
                        max_len = max(max_len, (zero_one[0] + zero_one[1]))
                    else:
                        break
        return max_len


t = int(input())

for i in range(t):
    number_of_char = int(input())
    arr_el = list(map(int, input().strip()))
    sol = Solve()
    print(sol.solve(arr_el))


