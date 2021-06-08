class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        n = len(A)
        srt = sorted(A)
        srt = A.sort()
        print(A)
        res = 0
        for i in range(0, n-2):
            j = i+1
            k = n-1
            while(j<k):
                if (A[i] + A[j] + A[k] < 2 and A[i] + A[j] + A[k] > 1):
                    k = k-1
                    res = 1
                else:
                    j = j+1

        return res
                    


    

A = [0.6, 0.7, 0.8, 1.2, 0.4]
print(Solution().solve(A))