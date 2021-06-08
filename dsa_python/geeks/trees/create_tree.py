
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Tree:
    def create_node(self, data):
        return Node(data)

    def insert(self, node, data, ch):
        if node is None:
            return self.create_node(data)
        if (ch == 'L'):
            node.left = self.insert(node.left, data, ch)
            return node.left
        else:
            node.right = self.insert(node.right, data, ch)
            return node.right

    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if i.data == data:
                return i
