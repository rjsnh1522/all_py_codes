from copy import copy, deepcopy

old_list = [[1,2,3],[4,5,6],[7,8,9]]
new_list = copy(old_list)


# new_list[0] =['a', 'b','c']
new_list[0][0] = 99
# print(old_list)
# print(new_list)

k_list = [[1,2,3], 99, 'a']

new_k_list = deepcopy(k_list)
new_k_list[0][0] = 000
print(k_list, new_k_list)
