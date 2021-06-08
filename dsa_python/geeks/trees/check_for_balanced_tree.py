# User function Template for python3

class Node:
    # Constructor to create a new Node 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# This function should return tree if passed  tree
# is balanced, else false.  Time complexity should
# be O(n) where n is number of nodes in tree */
def height(root):
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)

    return max(lh, rh) + 1


def isBalanced(root):
    # add code here
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    if abs(lh - rh) <= 1 and isBalanced(root.left) is True and isBalanced(root.right) is True:
        return True

    return False


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    root = None
    t = int(input())
    for i in range(t):
        # root = None
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

        if isBalanced(root):
            print(1)
        else:
            print(0)
            # } Driver Code Ends
