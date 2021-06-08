class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


n = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

n.left = n2
n.right = n3

n2.left = n4
n2.right = n5

n3.left = n6
n3.right = n7

n6.right = n8


def level_order_traverse(n):
    q = list()
    q.append(n)
    while len(q) != 0:
        out = q.pop(0)
        print(out.data)
        if out.left is not None:
            q.append(out.left)

        if out.right is not None:
            q.append(out.right)


# level_order_traverse(n)

def left_order_traversal_type_1(root):
    que = list()
    que.append(root)
    que.append(None)
    is_none = True
    while len(que) != 0:
        out = que.pop(0)
        if out is not None:
            if is_none:
                print(out.data,end=' ')
                is_none = False
            if out.left is not None:
                que.append(out.left)
            if out.right is not None:
                que.append(out.right)
        else:
            is_none = True
            if len(que) == 0 and out is None:
                break
            else:
                que.append(None)


# left_order_traversal_type_1(n)


def right_order_traversal_type_1(root):
    que = list()
    que.append(root)
    que.append(None)
    is_none = True
    while len(que) != 0:
        out = que.pop(0)
        if out is not None:
            if is_none:
                print(out.data, end=' ')
                is_none = False

            if out.left is not None:
                que.append(out.left)

            if out.right is not None:
                que.append(out.right)
        else:
            is_none = True
            if len(que) == 0 and out is None:
                break
            else:
                que.append(None)


# right_order_traversal_type_1(n)


# bst input

p = Node(20)
p1 = Node(10)
p2 = Node(18)
p3 = Node(-4)
p4 = Node(3)

p.left = p1
p.right = p2

p1.left = p3
p1.right = p4


def isBSTUtil(root, prev):
    if root != None:
        if isBSTUtil(root.left, prev) == True:
            return False
        if prev is not None and root.data <= prev.data:
            return False
        prev = root
        return isBSTUtil(root.right, prev)

    return True


def isBST(root):
    prev = None
    return isBSTUtil(root, prev)


print(isBST(n))
