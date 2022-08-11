# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

def middle_element(head):
    if head is None:
        return None
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow


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
# a_98.next = a_26
# a_26.next = a_36
# a_36.next = a_28
# a_28.next = a_57
# a_57.next = a_93


print(middle_element(a_14).val)
