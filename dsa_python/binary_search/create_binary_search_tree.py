import time
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.is_left = None
        self.is_right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                node.is_left = True
            else:
                self._insert(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
                node.is_right = True
            else:
                self._insert(value, node.right)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print("node", node.value, 'left', node.is_left, 'right', node.is_right)
            self._print_tree(node.right)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, root, curr_height):
        if root is None:
            return curr_height
        left_h = self._height(root.left, curr_height+1)
        right_h = self._height(root.right, curr_height+1)
        return max(left_h, right_h)

    def search(self, value):
        if self.root is None:
            return False
        return self._search(self.root, value)

    def _search(self, root, value):
        if root.value == value:
            return True
        elif root.value > value and root.left is not None:
            return self._search(root.left, value)
        elif root.value < value and root.right is not None:
            return self._search(root.right, value)
        return False


def fill_tree(tree, num_ele=2000, max_int=200000):
    from random import randint
    for _ in range(num_ele):
        cur_ele = randint(0, max_int)
        tree.insert(cur_ele)
    return tree

bt = BinarySearchTree()
# tree = fill_tree(bt)
bt.insert(10)
bt.insert(6)
bt.insert(20)
bt.insert(30)
bt.print_tree()
print("height", bt.height())

print(bt.search(10))
print(bt.search(30))
print(bt.search(40))
