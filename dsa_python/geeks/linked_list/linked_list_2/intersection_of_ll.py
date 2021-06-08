# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def getIntersectionNode(self, A, B):
    #     myset = set()
    #     tmp = A
    #     while tmp.next is not None:
    #         myset.add(tmp)
    #         tmp = tmp.next
    #     tmp = B
    #     while tmp.next is not None:
    #         if tmp in myset:
    #             return tmp
    #         tmp = tmp.next
    #     return None

    def getIntersectionNode(self, A, B):
        hasher = {}
        found_at = None
        if A is None or B is None:
            return None
        while A is not None:
            hasher[A] = True
            A = A.next
        while B is not None:
            if B in hasher:
                return B
            B = B.next

        return found_at


a_5 = ListNode(5)
a_8 = ListNode(8)
a_26 = ListNode(20)

b_4 = ListNode(4)
b_11 = ListNode(11)
b_15 = ListNode(15)

c_23 = ListNode(23)
c_25 = ListNode(25)
c_27 = ListNode(27)

a_5.next = a_8
a_8.next = a_26
a_26.next = c_23

b_4.next = b_11
b_11.next = b_15
b_15.next = c_23

c_23.next = c_25
c_25.next = c_27
c_27.next = None


a_1 = ListNode(1)
a_2 = ListNode(2)
b_3 = ListNode(3)
c_4 = ListNode(4)
a_1.next = a_2
a_2.next = c_4
b_3.next = c_4
c_4.next = None


sol = Solution()

inter = sol.getIntersectionNode(a_1, b_3)

print(inter.val)
