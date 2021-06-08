#
t_cases = int(input())
#
# for k in range(0, t_cases):
#     n_of_ele = int(input())
#     arr_list = input().split()
#     j = 1
#     arr_list.sort()
#     missed = None
#     for i in arr_list:
#         if j == int(i):
#             pass
#         else:
#             missed = j
#         j += 1
#
#     print(missed)
for t in range(0, t_cases):
    n_of_ele = int(input())
    actual_sum = ((n_of_ele)*(2*1 + (n_of_ele-1)*1))//2
    arr_list = input().split()
    current_sum = sum([int(x) for x in arr_list])
    print(actual_sum-current_sum)
