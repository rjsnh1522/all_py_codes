# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def min_height(self, A):

        if A is None:
            return 0

        lh = self.min_height(A.left)
        rh = self.min_height(A.right)

        return max(lh, rh) + 1


# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n1.left = n2
# n3 = TreeNode(3)
# n1.right = n3
# n4 = TreeNode(4)
# n3.left = n4
# n5 = TreeNode(5)
# n4.right = n5

n3 = TreeNode(3)
n9 = TreeNode(9)
# n20 = TreeNode(20)
# n15 = TreeNode(15)
# n7 = TreeNode(7)

n3.left = n9
# n3.right = n20
# n20.left = n15
# n20.right = n7


sol = Solution()
print(sol.min_height(n3))
