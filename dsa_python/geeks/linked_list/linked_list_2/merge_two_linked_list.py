# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        i = A
        j = B
        head = None
        checker = None
        while i and j:
            if i.val < j.val:
                temp = ListNode(i.val)
                temp.next = None
                if head is None:
                    head = temp
                    checker = temp
                else:
                    checker.next = temp
                    checker = checker.next
                i = i.next
            else:
                temp = ListNode(j.val)
                temp.next = None
                if head is None:
                    head = temp
                    checker = temp
                else:
                    checker.next = temp
                    checker = checker.next
                j = j.next

        if i is not None:
            checker.next = i
        elif j is not None:
            checker.next = j
        return head

a_1 = ListNode(5)
a_4 = ListNode(8)
a_6 = ListNode(20)
a_1.next = a_4
a_4.next = a_6
a_6.next = None


b_2 = ListNode(4)
b_3 = ListNode(11)
b_5 = ListNode(15)
b_2.next = b_3
b_3.next = b_5
b_5.next = None

sol = Solution()
hh = sol.mergeTwoLists(a_1, b_2)

while hh is not None:
    print(hh.val)
    hh = hh.next
