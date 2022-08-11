# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


def top_view_of_bt(root):
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
    return traversal_table


bt = TreeNode('a')
bt.left = TreeNode('b')
bt.right = TreeNode('c')
bt.right.left = TreeNode('f')
bt.right.left.left = TreeNode('h')
bt.right.left.right = TreeNode('i')
bt.right.left.right.right = TreeNode('j')
bt.right.left.right.right.right = TreeNode('k')
bt.right.right = TreeNode('g')
bt.left.left = TreeNode('d')
bt.left.left.left = TreeNode('l')
bt.left.right = TreeNode('e')

print(top_view_of_bt(bt))
