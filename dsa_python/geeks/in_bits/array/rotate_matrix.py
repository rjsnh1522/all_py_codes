class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        for i in range(0, n):
            for j in range(0,n):
                if i != j:
                    if i>j:
                        A[i][j],A[j][i] = A[j][i],A[i][j]
        c = n-1
        for i in range(0, n):
           for j in range(0, n//2):
                A[i][c-j], A[i][j] = A[i][j], A[i][c-j]
            
        return A
       




a = [
    [1,2,3,'a'],
    [4,5,6,'b'],
    [7,8,9,'c']
]
Solution().rotate(a)
# print(Solution().rotate(a))
