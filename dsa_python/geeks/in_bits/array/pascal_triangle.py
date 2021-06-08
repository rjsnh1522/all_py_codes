# class Solution:
#
#     def generate(self, A):
#         arr = []
#         n = A
#         for line in range(0, n):
#             for i in range(0, line + 1):
#                 a = self.binomial_coeff(line, i)
#                 print(a)
#                 print("---")
#                 # arr.append([''.join(map(str, a))])
#         return arr
#
#     def binomial_coeff(self, n, k):
#         res = 1
#         if (k > n - k):
#             k = n - k
#         for i in range(0, k):
#             res = res * (n - i)
#             res = res // (i + 1)
#
#         return res
#
#
# print(Solution().generate(7))
#


class Solution:

    def generate(self, A):
        arr = []
        ns = A
        for line in range(0, ns):

            a = []
            for i in range(0, line + 1):
                a.append(self.binomialCoeff(line, i))
            arr.append(a)

        return arr

    # for details of this function
    def binomialCoeff(self, ns, k):
        res = 1
        if (k > ns - k):
            k = ns - k
        for i in range(0, k):
            res = res * (ns - i)
            res = res // (i + 1)

        return res


# Driver program
n = 7
print(Solution().generate(n))




# # posted code
# class Solution:
#
#     def generate(self, A):
#         arr = []
#         n = A
#         for line in range(0, n):
#             for i in range(0, line + 1):
#                 arr.append([self.binomial_coeff(line, i)])
#                 # print(binomialCoeff(line, i),
#                 #         " ", end="")
#             # print()
#         return arr
#
#     def binomial_coeff(self, n, k):
#         res = 1
#         if (k > n - k):
#             k = n - k
#         for i in range(0, k):
#             res = res * (n - i)
#             res = res // (i + 1)
#
#         return res




