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
        new = None
        ptr = None
        while i and j:
            if i.val > j.val:
                tmp = ListNode(j.val)
                if new is None:
                    ptr = tmp
                    new = tmp
                else:
                    ptr.next = tmp
                    ptr = ptr.next
                j = j.next
            else:
                tmp = ListNode(i.val)
                if new is None:
                    new = tmp
                    ptr = tmp
                else:
                    ptr.next = tmp
                    ptr = ptr.next

                i = i.next
        if i is not None:
            ptr.next = i
        elif j is not None:
            ptr.next = j
        return new



a1 = ListNode(5)
a8 = ListNode(8)
a20 = ListNode(20)


b1 = ListNode(4)
b11 = ListNode(11)
b15 = ListNode(15)

A = a1
a1.next = a8
a8.next = a20

B = b1
b1.next = b11
b11.next = b15


s = Solution()
print(s.mergeTwoLists(A, B))
