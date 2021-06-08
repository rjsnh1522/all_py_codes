# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 0->1->1->2->3->3
class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        prev = None
        tortoise = A
        head = tortoise
        while tortoise.next is not None:
            if tortoise.val == tortoise.next.val:
                if prev is None:
                    temp = tortoise.next
                    tortoise.next = None
                    tortoise = temp
                    head = tortoise
                else:
                    temp = tortoise.next
                    tortoise = None
                    prev.next = temp
                    tortoise = temp
            else:
                prev = tortoise
                tortoise = tortoise.next

        return head


a_0 = ListNode(0)
a_1 = ListNode(1)
a_11 = ListNode(1)
a_2 = ListNode(2)
a_3 = ListNode(3)
a_33 = ListNode(3)

a_0.next = a_1
a_1.next = a_11
a_11.next = a_2
a_2.next = a_3
a_3.next = a_33


s = Solution()
ss = s.deleteDuplicates(a_0)

while ss.next is not None:
    print(ss.val)
    ss = ss.next
