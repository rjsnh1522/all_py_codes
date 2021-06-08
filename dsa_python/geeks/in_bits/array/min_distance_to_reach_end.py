
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        sum=0
        n=len(A)
        for i in range(1,n):
            a=(A[i]-A[i-1])
            a=abs(a)
            b=B[i]-B[i-1]
            b=abs(b)
            sum=sum+max(a,b)
        return sum
        


A = [1,2,3,4,5,6]
B = [3,2,4,53,2]

s = Solution()
print(s.coverPoints(A,B))