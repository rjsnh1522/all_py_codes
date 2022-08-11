# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

def detect_loop_in_linked_list(head):
    # by using hash
    hash_table = {}
    is_loop = False
    while head.next is not None:
        if head.val in hash_table:
            is_loop = True
            break
        else:
            hash_table[head.val] = True
            head = head.next
    return is_loop



    # assign two var p and q
    # move p one step q two step while anyone is null.
    # while p and q and p.next



if __name__ == '__main__':
    # Start with the empty list
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
    a_93.next = a_26

    print(detect_loop_in_linked_list(a_14))

