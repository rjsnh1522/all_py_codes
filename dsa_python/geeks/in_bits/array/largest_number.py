
# class Solution:
#     # @param A : tuple of integers
#     # @return a strings
#     def largestNumber(self, A):
#         res = ""
#         n = len(A)
#         # A = sorted(A,reverse=True)
#         for i in range(0, n):
#             forw = res + str(A[i])
#             back = str(A[i]) + res
#             if forw > back:
#                 res = forw
#             else:
#                 res = back
#         return res




# class LargerNumKey(str):
#     def __lt__(self, x, y):
#         return x+y > y+x
        
# class Solution:
#     def largestNumber(self, nums):
#         largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
#         return '0' if largest_num[0] == '0' else largest_num


# from itertools import permutations 

# class Solution:

#   def largestNumber(self, A):
#     lst = [] 
#     for i in permutations(A, len(A)): 
#         lst.append("".join(map(str,i)))  
#     return max(lst) 



class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


A = [8, 89]
A = [ 3, 30, 34, 5, 9,0 ]

A = [0,30,34,31,32]
# A = sorted(A,reverse=True)

print(Solution().largestNumber(A))