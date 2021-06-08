class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListNode:
    def __init__(self, r):
        self.root = r
        self.size = 0
        self.current = self.root

    def insert_node(self, val):
        new_node = Node(val)
        self.current.next = new_node
        self.current = new_node
        self.size += 1

    def delete_node(self, val):
        current = self.root
        prev_node = None
        while current:
            if current.data == val:
                if prev_node is not None:
                    prev_node.next = current.next
                else:
                    self.root = current.next
                self.size -=1
                return True
            else:
                prev_node = current
                current = current.next
        return False

    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
