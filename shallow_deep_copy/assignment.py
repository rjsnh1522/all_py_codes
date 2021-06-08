from copy import copy, deepcopy
num = [1,2,3,4,56,9]

new_num = num


new_num[0] = 99

print('num', num)
print('id', id(num))

print('new_num', num)
print('new_num id', id(new_num))
