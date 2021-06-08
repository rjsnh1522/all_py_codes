
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Driver Program
if __name__ == '__main__':

    root = None
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n == 0:
            print(0)
            continue
        dictTree = dict()

        for j in range(n):
            if arr[3 * j] not in dictTree:
                dictTree[arr[3 * j]] = Node(arr[3 * j])
                parent = dictTree[arr[3 * j]]
                if j is 0:
                    root = parent

            else:
                parent = dictTree[arr[3 * j]]

            child = Node(arr[3 * j + 1])
            if (arr[3 * j + 2] == 'L'):
                parent.left = child
            else:
                parent.right = child
            dictTree[arr[3 * j + 1]] = child

        print(countLeaves(root))
''' This is a function problem.You only need to complete the function given below '''
# User function Template for python3
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case


def countLeaves(root):
# Code here
    if root is None:
        return

    if (root.left is None) and (root.right is None):
        return 1
    else:
        return countLeaves(root.left) + countLeaves(root.right)

