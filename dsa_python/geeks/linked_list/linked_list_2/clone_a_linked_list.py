class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

def clonelist(A):
    copy_from = A
    header = None
    address_book = dict()
    ptr = None
    while copy_from is not None:
        if header is None:
            curr = ListNode(copy_from.val)
            header = curr
            ptr = curr
            address_book[copy_from] = ptr
        else:
            noddy = ListNode(copy_from.val)
            ptr.next = noddy
            ptr = ptr.next
            address_book[copy_from] = ptr
        copy_from = copy_from.next
    copy_from = A
    ptr = header
    while copy_from is not None:
        ptr.random = address_book[copy_from.random]
        ptr = ptr.next
        copy_from = copy_from.ext
    return header
