class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        C = len(A[0])
        R = len(A)
        row = [1] * R
        col = [1] * C
          
        # Initialize all values of row[] as 1  
        for i in range(0, R): 
            row[i] = 1
              
        # Initialize all values of col[] as 1  
        for i in range(0, C) : 
            col[i] = 1
      
      
        # Store the rows and columns to be marked  
        # as 0 in row[] and col[] arrays respectively  
        for i in range(0, R) : 
              
            for j in range(0, C) : 
                if (A[i][j] == 0) : 
                    row[i] = 0
                    col[j] = 0
                  
        # Modify the input matrix mat[] using the  
        # above constructed row[] and col[] arrays  
        for i in range(0, R) : 
              
            for j in range(0, C): 
                if ( row[i] == 0 or col[j] == 0 ) : 
                    A[i][j] = 0
       
        return A





# R = 3
# C = 4
  
# def modifyMatrix(mat): 
#     row = [1] * R  
#     col = [1] * C  
      
#     # Initialize all values of row[] as 1  
#     for i in range(0, R): 
#         row[i] = 1
          
#     # Initialize all values of col[] as 1  
#     for i in range(0, C) : 
#         col[i] = 1
  
  
#     # Store the rows and columns to be marked  
#     # as 0 in row[] and col[] arrays respectively  
#     for i in range(0, R) : 
          
#         for j in range(0, C) : 
#             if (mat[i][j] == 0) : 
#                 row[i] = 0
#                 col[j] = 0
              
#     # Modify the input matrix mat[] using the  
#     # above constructed row[] and col[] arrays  
#     for i in range(0, R) : 
          
#         for j in range(0, C): 
#             if ( row[i] == 0 or col[j] == 0 ) : 
#                 mat[i][j] = 0
                  
# # A utility function to print a 2D matrix  
# def printMatrix(mat) : 
#     for i in range(0, R): 
          
#         for j in range(0, C) : 
#             print(mat[i][j], end = " ") 
#         print() 
          
# # Driver Code 
# mat = [ [1, 1, 1, 1], 
#         [0, 1, 1, 0], 
#         [0, 1, 0, 0] ]  
  
# print("Input Matrix n") 
# printMatrix(mat) 
  
# modifyMatrix(mat) 
  
# print("Matrix after modification n") 
# printMatrix(mat) 










a = [[1,0,1],[1,1,1],[1,1,1]]

print(Solution().setZeroes(a))