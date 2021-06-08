# Definition for singly-linked list.
# TODO its working
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, A, B):
        tortoise = A
        hare = A
        prev = None
        head = None
        len = 0
        while A is not None:
            A = A.next
            len += 1
        if B > len:
            B = len
        for i in range(len-(B)):
            hare = hare.next

        while tortoise is not None:
            if hare == tortoise:
                if prev is None:
                    prev = tortoise
                prev.next = tortoise.next
                tortoise = tortoise.next
            else:
                prev = tortoise
                tortoise = tortoise.next
                if head is None:
                    head = prev
        return head
# 1 2 3 4 5 6 7 8 9 10---> 5
#
# 1 5
# 2 6
# 3 7
# 4 8
# 5 9
# 6 10

a_14 = ListNode(14)
a_42 = ListNode(42)
a_98 = ListNode(98)
a_26 = ListNode(26)
a_36 = ListNode(36)
a_28 = ListNode(28)
a_57 = ListNode(57)
a_93 = ListNode(93)
a_14.next = a_42
a_42.next = a_98
a_98.next = a_26
a_26.next = a_36
a_36.next = a_28
a_28.next = a_57
a_57.next = a_93

sol = Solution()
header = sol.removeNthFromEnd(a_14, 10)
while header is not None:
    print(header.val)
    header = header.next
