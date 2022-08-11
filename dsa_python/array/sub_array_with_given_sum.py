#
# def sumwithhash(arr, s):
#     hashed = {}
#     curr_sum = 0
#     start = 0
#     end = -1
#     for i in range(len(arr)):
#         curr_sum += arr[i]
#         hashed[curr_sum] = i
#         if curr_sum - s == 0:
#             start = 0
#             end = i
#             break
#         if (curr_sum - s) in hashed:
#             start = hashed[curr_sum - s]
#             end = i
#             break
#     if end == -1:
#         print("Not found")
#     else:
#         print("found at", [start, end])
#
#     print(hashed)



def subArraySum(arr, s):
    left = 0
    right = 0
    c_sum = 0
    while right <= len(arr):
        if c_sum == s:
            return [left, right]
        elif c_sum < s:
            c_sum += arr[right]
            right += 1
        elif c_sum > s:
            c_sum -= arr[left]
            left += 1
    return [-1]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    s = 4
    # print(sumwithhash(arr, s))
    print(subArraySum(arr, s))
