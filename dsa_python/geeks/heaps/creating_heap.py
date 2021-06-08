# The corresponding complete binary tree for this array of elements [4, 10, 3, 5, 1] will be:
#
#        4
#       / \
#     10    3
#    / \
#   5   1
#
# Note:
# Root is at index 0 in array.
# Left child of i-th node is at (2*i + 1)th index.
# Right child of i-th node is at (2*i + 2)th index.
# Parent of i-th node is at (i-1)/2 index.

def heapify(arr, n, i):
    largest = i
    l = (2*i) + 1
    r = (2*i) + 2

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_heap(arr, n):
    start_index = (n//2 - 1)
    for i in range(start_index, -1, -1):
        heapify(arr, n, i)

def print_heap(arr, n):
    print("Array representation of Heap is:")

    for i in range(n):
        print(arr[i], end=" ")
    print()

arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]

n = len(arr)
build_heap(arr, n)
print_heap(arr, n)
