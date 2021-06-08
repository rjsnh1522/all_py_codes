# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode, mini=-math.inf, maxi=math.inf) -> bool:
        if root is None:
            return True
        if root.val < mini or root.val >= maxi:
            return False

        # left = self.isValidBST(root.left, mini, root.val)
        # right = self.isValidBST(root.right, root.val, maxi)

        return self.isValidBST(root.left, mini, root.val) and self.isValidBST(root.right, root.val, maxi)

