# Definition for a  binary tree node
# NOT_SOLVED


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        in_order = self.in_order_traversal(A)
        print(in_order)
        index_b = -1
        index_c = -1
        for i in range(len(in_order)):
            if in_order[i] == B:
                index_b = i
            if in_order[i] == C:
                index_c = i

        return abs(index_b - index_c)

    def in_order_traversal(self, current):
        answer, stack = [], []
        if not current:
            return answer

        while True:
            if current:
                stack.append(current)
                current = current.left
            elif len(stack) > 0:
                pop = stack.pop(-1)
                answer.append(pop.val)
                current = pop.right
            else:
                break
        return answer


t5 = TreeNode(5)
t2 = TreeNode(2)
t8 = TreeNode(8)

t1 = TreeNode(1)
t4 = TreeNode(4)
t6 = TreeNode(6)
t11 = TreeNode(11)

t5.left = t2
t5.right = t8
t2.left = t1
t2.right = t4

t8.left = t6
t8.right = t11

sol = Solution()
print(sol.solve(t5, 2, 5))
