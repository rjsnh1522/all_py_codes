
def search_elem_in_matrix(arr, search):
    row = 0
    col = len(arr[0]) - 1
    found = False
    while col >= 0 and row < len(arr):
        if search == arr[row][col]:
            return row+1 * 1009 + col+1
        if search > arr[0][col]:
            row += 1
        else:
            col -= 1
    return -1



A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = 2

print(search_elem_in_matrix(A, B))
