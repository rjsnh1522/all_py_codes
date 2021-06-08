class Solution:

    def getRow(self, A):

        return self.solve(A)

    def solve(self, n):
        arr = []
        an = n
        n = an + 1
        for line in range(0, n):

            a = []

            for i in range(0, line + 1):
                a.append(self.binomialCoeff(line, i))
            arr.append(a)

            if line == an:

                return a
    
    def binomialCoeff(self, n, k):
        res = 1
        if (k > n - k):
            k = n - k
        for i in range(0, k):
            res = res * (n - i)
            res = res // (i + 1)

        return res



n = 3
print(Solution().getRow(n))

# class Solution:
#     # @param A : integer
#     # @return a list of integers
#     def getRow(self, A):
