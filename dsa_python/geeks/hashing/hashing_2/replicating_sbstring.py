class Solution:
    def solve(self, B, A):
        string = A
        counter = B
        dicter = dict()
        for i in string:
            if i in dicter:
                dicter[i] += 1
            else:
                dicter[i] = 1

        for i in dicter:
            if dicter[i] % counter != 0:
                return -1
        return 1

sol = Solution()
print(sol.solve(3, 'ababab'))
