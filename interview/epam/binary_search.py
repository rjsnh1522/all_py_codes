
def bs(arr, find):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) //2
        if arr[mid] == find:
            return True
        elif arr[mid] < find:
            start = mid + 1
        else:
            end = mid - 1
    return False

arr = [1 ,2 ,3 ,4 ,5 ,9 ,6]
find = 9
print(bs(arr, find))

