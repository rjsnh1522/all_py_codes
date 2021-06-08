from copy import copy
class Solution:
    def solve(self, A):
        digits = [1, 2, 3]
        queue = copy(digits)
        ans = []
        for i in range(A):
            ele = queue.pop(0)
            ans.append(ele)
            for k in digits:
                queue.append(int(str(ele)+str(k)))
        return ans


dd = [1, 2, 3, 4]
nn = 20
sol = Solution()
print(sol.solve(nn))
