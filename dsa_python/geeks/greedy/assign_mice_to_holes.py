class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()
        ans = 0
        for i in range(len(A)):
            ans = max(ans, abs(A[i]-B[i]))
        return ans


A = [4, -4, 2]
B = [4, 0, 5]
s = Solution()
print(s.mice(A, B))
