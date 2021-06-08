# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    # pre order traversal is N L R
    def pre_order_traversal(self, A):
        current = A
        if not current:
            return []
        stack = []
        anser = []
        stack.append(current)
        while len(stack) > 0:
            pop = stack.pop()
            anser.append(pop.val)
            #  stack is last in first out that's why we are putting right first then left
            if pop.right is not None:
                stack.append(pop.right)
            if pop.left is not None:
                stack.append(pop.left)
        return anser

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.pre_order_traversal(root))
