class Solution:
    def longestCommonPrefix(self, A):
        first_string = A[0]
        found_prefix = first_string
        for i in range(1, len(A)):
            looper = found_prefix
            temp_pre = ""
            len_looper = len(looper)
            len_cur_str = len(A[i])
            if len_looper > len_cur_str:
                looper = looper[0:len_cur_str]
            else:
                A[i] = A[i][0:len_looper]
            for j in range(len(looper)):
                if looper[j] == A[i][j]:
                    temp_pre += looper[j]
                else:
                    break
            found_prefix = temp_pre
        return found_prefix


sol = Solution()
A = ["abcd", "abcd", "efgh"]
A = ['abcd']

print(sol.longestCommonPrefix(A))
