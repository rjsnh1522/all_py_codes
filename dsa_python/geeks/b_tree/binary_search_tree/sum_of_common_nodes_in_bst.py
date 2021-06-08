# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer

    def in_order_traversal(self, root):
        current = root
        stack = []
        anser = []
        if not current:
            return anser
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif len(stack) > 0:
                pop = stack.pop(-1)
                anser.append(pop.val)
                current = pop.right
            else:
                break
        return anser

    def solve(self, A, B):
        traversed_a = self.in_order_traversal(A)
        traversed_b = self.in_order_traversal(B)
        print(traversed_a, traversed_b)
        summer = 0
        while traversed_b and traversed_a:
            pop_a = traversed_a.pop(-1)
            pop_b = traversed_b.pop(-1)
            print(pop_a, pop_b)
            if pop_a == pop_b:
                summer += pop_b
            elif pop_a > pop_b:
                traversed_b.append(pop_b)
            else:
                traversed_a.append(pop_a)

        return summer





# tree 1
t5  = TreeNode(5)
t2 = TreeNode(2)
t3 = TreeNode(3)
t5.left = t2
t2.right = t3
t8 = TreeNode(8)
t5.right = t8
t15 = TreeNode(15)
t8.right = t15
t7 = TreeNode(7)
t15.left = t7

# tree 2

b7 = TreeNode(7)
b1 = TreeNode(1)
b2 = TreeNode(2)
b10 = TreeNode(10)
b15 = TreeNode(15)
b8 = TreeNode(8)

b7.left = b1
b7.right = b10
b1.right = b2
b10.right = b15
b15.left = b8



sol = Solution()
print(sol.solve(t5, b7))










# class Solution:
#     # @param A : root node of tree
#     # @param B : root node of tree
#     # @return an integer
#
#     def in_order_traversal(self, root):
#         current = root
#         stack = []
#         anser = {}
#         if not current:
#             return anser
#         while True:
#             if current:
#                 stack.append(current)
#                 current = current.left
#             elif len(stack) > 0:
#                 pop = stack.pop(-1)
#                 anser[pop.val] = True
#                 current = pop.right
#             else:
#                 break
#         return anser
#
#     def solve(self, A, B):
#         traversed_a = self.in_order_traversal(A)
#         traversed_b = self.in_order_traversal(B)
#         summer = 0
#         for i in traversed_a:
#             if i in traversed_b:
#                 summer += i
#         return summer
