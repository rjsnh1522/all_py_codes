# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, root, value):
        if root.left is None:
            root.left = TreeNode(value)
            return True
        else:
            self._insert(root.left, value)
        if root.right is None:
            root.right = TreeNode(value)
            return True
        else:
            self._insert(root.right, value)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, root):
        if root is not None:
            self._print_tree(root.left)
            self._print_tree(root.right)


def print_level_order_traversal(root):
    queue = []
    answer_queue = []
    queue.append(root)
    while len(queue) > 0:
        ele = queue.pop(0)
        print(ele.val)
        answer_queue.append(ele.val)
        if ele.left is not None:
            queue.append(ele.left)
        if ele.right is not None:
            queue.append(ele.right)
    print('answer_queue', answer_queue)


def fill_tree(tree, num_ele=4, max_int=20):
    from random import randint
    for _ in range(num_ele):
        cur_ele = randint(0, max_int)
        tree.insert(cur_ele)
    return tree

bt = TreeNode()
bt.left = TreeNode(10)
bt.right = TreeNode(15)
bt.right.left = TreeNode(13)
bt.right.right = TreeNode(23)
bt.left.left = TreeNode(33)
bt.left.right = TreeNode(43)
bt = fill_tree(bt)
bt.print_tree()
print(bt.root)
print_level_order_traversal(bt)
