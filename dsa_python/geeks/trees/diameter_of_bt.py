

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data, ch):
        if node is None:
            return self.createNode(data)
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


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(str, input().strip().split()))
        if n == 0:
            print(0)
            continue
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
            k += 3
        print(diameter(root))


''' This is a function problem.You only need to complete the function given below '''
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return the diameter of the tree


def height(root, ans):
    if root == None:
        return 0

    lh = height(root.left, ans)
    rh = height(root.right, ans)

    ans[0] = max(ans[0], 1 + lh + rh)
    return 1 + max(lh, rh)


def diameter(root):
    # Code here
    if root == None:
        return 0;

    ans = [-999999999999]
    he = height(root, ans)
    return ans[0]
