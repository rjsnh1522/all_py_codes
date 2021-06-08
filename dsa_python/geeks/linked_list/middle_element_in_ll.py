# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def solve(self, A):
        tortoise = A
        if A.next != None and A.next.next != None:
            hare = A.next.next
        elif A.next !=None and A.next.next == None:
            return A.next.val
        elif A.next == None:
            return A.val

        while hare.next != None:
            tortoise = tortoise.next
            if hare.next.next != None:
                hare = hare.next.next
            elif hare.next !=None:
                hare = hare.next
            else:
                pass

        if hare.next == None:
            return tortoise.next.val
        elif hare.next.next == None:
            return tortoise.next.next.val



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

# a_1 = ListNode(1)
# a_2 = ListNode(2)
# a_3 = ListNode(3)
# a_4 = ListNode(4)
# a_5 = ListNode(5)
# a_1.next = a_2
# a_2.next = a_3
# a_3.next = a_4
# a_4.next = a_5

#
# a_1 = ListNode(1)
# a_5 = ListNode(5)
# a_6 = ListNode(6)
# a_2 = ListNode(2)
# a_3 = ListNode(3)
# a_4 = ListNode(4)
# a_1.next = a_5
# a_5.next = a_6
# a_6.next = a_2
# a_2.next = a_3
# a_3.next = a_4

# a_39 = ListNode(39)
# a_95 = ListNode(95)
# a_39.next = a_95

sol = Solution()
print(sol.solve(a_14))
