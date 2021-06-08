class Node:
    """ Class Node """

    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:
    def createNode(self, data):
        return (Node(data))

    def insert(self, node, data, ch):
        if (node is None):
            return (self.createNode(data))
        if (ch == 'L'):
            node.left = self.insert(node.left, data, ch)
            return (node.left)
        else:
            node.right = self.insert(node.right, data, ch)
            return (node.right)

    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if (i.data == data):
                return (i)


s = 0


def size(node):
    # code here
    if node is None:
        return s
    else:
        return size(node.left)+1+size(node.right)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        tree = Tree()
        lis = []
        root = None
        root = tree.insert(root, int(arr[0]), 'L')
        lis.append(root)
        k = 0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k + 1]), arr[k + 2]))
            # print (arr[k], arr[k+1], ptr)
            k += 3
        print(size(root))


''' This is a function problem.You only need to complete the function given below '''
# Your task to complete this function
# function should return size of the binary tree as integer

