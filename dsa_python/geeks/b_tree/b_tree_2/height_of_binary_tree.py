# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def height(self, A):

        if A is None:
            return -1

        lh = self.height(A.left)
        rh = self.height(A.right)

        return max(lh, rh) + 1


n1 = TreeNode(1)
n2 = TreeNode(2)
n1.left = n2
n3 = TreeNode(3)
n1.right = n3
n4 = TreeNode(4)
n3.left = n4
n5 = TreeNode(5)
n4.right = n5

sol = Solution()
print(sol.height(n1))
