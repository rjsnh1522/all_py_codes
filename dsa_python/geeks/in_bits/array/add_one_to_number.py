class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A) 
   

        A[n-1] += 1
        carry = A[n-1]/10
        A[n-1] = A[n-1] % 10

        for i in range(n-2,-1,-1): 
            if (carry == 1): 
               A[i] += 1
               carry = A[i]/10
               A[i] = A[i] % 10

        if (carry == 1): 
          A.insert(0, 1)

        not_found = True
        for i in range(0, n):
            if n !=1 and A[0] == 0 and not_found:
                A.remove(0)
            else:
                not_found = False
        return A

A = [ 0,1,0,0, 3, 7, 6, 4, 0, 5, 5, 5 ]

print(Solution().plusOne(A))