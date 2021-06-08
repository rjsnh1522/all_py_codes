# Definition for a  binary tree node

# NOT_SOLVED

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0

    def solve(self, A, B, C):
        in_order = self.in_order_traversal(A)
        index_c = -1
        index_b = -1
        for i in range(len(in_order)):
            if in_order[i] == B:
                index_b = i
            if in_order[i] == C:
                index_c = i
        return abs(index_c - index_b) + 1

    def in_order_traversal(self, root):
        stack = []
        answer = []
        if not root:
            return answer

        while True:
            if root:
                stack.append(root)
                root = root.left
            elif len(stack) > 0:
                pop = stack.pop(-1)
                answer.append(pop.val)
                root = pop.right
            else:
                break
        return answer

