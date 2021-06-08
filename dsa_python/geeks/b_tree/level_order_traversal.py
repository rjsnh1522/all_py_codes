# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, A):
        queue = []
        ansr_queue = []
        queue.append(A)
        marker = "$"
        queue.append(marker)
        row = []
        while len(queue) > 0:
            ele = queue.pop(0)
            if ele != marker:
                row.append(ele.val)
                if ele.left is not None:
                    left = ele.left
                    queue.append(left)
                if ele.right is not None:
                    right = ele.right
                    queue.append(right)
            else:
                ansr_queue.append(row)
                row = []
                if len(queue) == 0:
                    break
                queue.append(marker)
        return ansr_queue
