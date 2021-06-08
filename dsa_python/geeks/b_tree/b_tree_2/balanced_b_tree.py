# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        is_bal = self.height(A)
        return 1 if is_bal[0] else 0

    def height(self, A):

        if A is None:
            return True, -1

        lh = self.height(A.left)
        rh = self.height(A.right)

        maxer = max(lh[1], rh[1]) + 1
        if lh[0] is True and rh[0] is True:
            if abs(lh[1]-rh[1]) <= 1:
                return True, maxer
            else:
                return False, maxer
        else:
            return False, maxer


n1 = TreeNode(1)
n2 = TreeNode(2)
n1.left = n2
n3 = TreeNode(3)
n1.right = n3
n4 = TreeNode(4)
n3.left = n4
n5 = TreeNode(5)
n4.right = n5
n6 = TreeNode(6)
n5.left = n6
n7 = TreeNode(7)
n6.left = n7

sol = Solution()
print(sol.isBalanced(n1))
