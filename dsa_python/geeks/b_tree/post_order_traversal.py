# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    # pre order traversal is L R N
    def pre_order_traversal(self, A):
        current = A
        if not current:
            return []
        stack1 = []
        anser = []
        stack2 = []
        stack1.append(current)
        while len(stack1) > 0:
            pop = stack1.pop()
            stack2.append(pop)
            if pop.left is not None:
                stack1.append(pop.left)
            if pop.right is not None:
                stack1.append(pop.right)
        while len(stack2) > 0:
            anser.append(stack2.pop(-1).val)
        return anser

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.pre_order_traversal(root))
