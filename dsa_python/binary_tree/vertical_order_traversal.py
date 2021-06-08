# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None



def vertical_travers(root):
    traversal_table = {}
    queue = []
    hd = 0
    queue.append((root, hd))
    while len(queue) > 0:
        element = queue.pop(0)
        hd = element[1]
        node = element[0]
        if hd in traversal_table:
            traversal_table[hd].append(node.val)
        else:
            traversal_table[hd] = [node.val]

        if node.left is not None:
            queue.append((node.left, hd-1))
        if node.right is not None:
            queue.append((node.right, hd+1))
    print(traversal_table)



bt = TreeNode(5)
bt.left = TreeNode(10)
bt.right = TreeNode(15)
bt.right.left = TreeNode(13)
bt.right.right = TreeNode(23)
bt.left.left = TreeNode(33)
bt.left.right = TreeNode(43)

print(vertical_travers(bt))
