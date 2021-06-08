# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    # IN order is L N R
    def inorderTraversal(self, A):
        current = A
        stack = []
        anser = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif len(stack) > 0:
                pop = stack.pop()
                if pop.val is not None:
                    anser.append(pop.val)
                current = pop.right
            else:
                break
        return anser

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.inorderTraversal(root))
