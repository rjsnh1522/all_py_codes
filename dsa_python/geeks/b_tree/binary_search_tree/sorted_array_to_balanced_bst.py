# SOLVED
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        start = 0
        end = (len(A) - 1)
        root = self.tree_maker(A, start, end)
        return root

    def tree_maker(self, arr, start, end):
        if start > end:
            return None
        mid = (start+end)//2
        root = TreeNode(arr[mid])
        root.left = self.tree_maker(arr, start, mid-1)
        root.right = self.tree_maker(arr, mid+1, end)

        return root


a = [1, 2, 3]
sol = Solution()
rooter = sol.sortedArrayToBST(a)
print(rooter.val)
