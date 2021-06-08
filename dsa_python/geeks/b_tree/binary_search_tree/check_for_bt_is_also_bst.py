# Check for BST with exactly one child of each internal nodes



class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):

        size = len(A)
        if A[size-1] > A[size-2]:
            maxi = A[size-1]
            mini = A[size-2]
        else:
            mini = A[size-1]
            maxi = A[size-2]
        for i in range(size-3,0, -1):
            if A[i] < mini:
                mini = A[i]
            elif A[i] > maxi:
                maxi = A[i]
            else:
                return "NO"
        return "YES"






a = [25, 42, 49, 2, 44]
# a = [ 4, 10, 5 ,8 ]
a = [25, 42, 49, 44, 2]
# a = [8, 3, 5, 7, 6]
a = [44, 49, 42, 25, 2]
sol = Solution()
print(sol.solve(a))












#
# class BST:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# class Solution:
#     # @param A : list of integers
#     # @return a strings
#     def solve(self, A):
#         root = BST(A[0])
#         head = root
#         for i in range(1, len(A)):
#             if root.val >= A[i]:
#                 root.left = BST(A[i])
#                 root = root.left
#             else:
#                 root.right = BST(A[i])
#                 root = root.right
#         return self.traver_tree(head)
#
#     def traver_tree(self, root):
#         if not root:
#             return True
#
#         left = self.traver_tree(root.left)
#         right = self.traver_tree(root.right)
#
#         if left and right:
#             return False
#         else:
#             return True


