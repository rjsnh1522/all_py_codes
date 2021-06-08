# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self, head):
        self.head = head

    def reverse_loop(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def recur_util(self, curr, prev):

        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev

        self.recur_util(next, curr)

    def reverse_recursion(self):
        if self.head is None:
            return
        self.recur_util(self.head, None)
        return self.head

    def change_head(self, val):
        self.head = val


a_1 = ListNode(1)
a_2 = ListNode(2)
a_3 = ListNode(3)
a_4 = ListNode(4)
a_5 = ListNode(5)
a_1.next = a_2
a_2.next = a_3
a_3.next = a_4
a_4.next = a_5

sol = Solution(a_1)
rev_head = sol.reverse_loop()
cpy = rev_head
while rev_head is not None:
    print('l', rev_head.val)
    rev_head = rev_head.next

sol.change_head(cpy)
rec_head = sol.reverse_recursion()
while rec_head is not None:
    print('rec', rec_head.val)
    rec_head = rec_head.next
