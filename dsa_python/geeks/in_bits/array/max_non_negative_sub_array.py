class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        i=0
        max_ = -1
        ans = []
        while i<len(A):
            while i<len(A) and A[i]<0:
                i += 1
            l = []
            while i<len(A) and A[i]>=0:
                l.append(A[i])
                i += 1
            if sum(l)>max_:
                ans = l
                max_ = sum(l)
        return ans

A =[1, 2, 5, -7, 2, 3]
print(Solution().maxset(A)) 