class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        dicto = {}
        for i in A:
            if str(i) in dicto:
                return i
            else:
                dicto[str(i)] = 1
        return -1


a = Solution()
b = [3, 4, 1, 5, 1]
print(a.repeatedNumber(b))