

# def nearest_palin(number):
# 	numb_str = str(number)
# 	## check if number is palindrome if yes return it
# 	if numb_str == numb_str[::-1]:
# 		return numb_str

# 	if len(numb_str) % 2 == 0:
# 		pass
# 	else:
# 		pass




# a = 5

# def add():
# 	global a
# 	b = a
# 	a = 15
# 	total = b + a
# 	print(total) 


# print(a)
# print(add())


dicto = {'twenty':20, 'ten': 10, 'thirty': 30, 'ninety': 90, 'zero': 0, 'one':1, 'two': 2}


def sort_on_values_without_using_sorted(dicto):
	values = dicto.values()
	values_list = list(values)
	keys = dicto.keys()
	keys_list = list(keys)
	dict2 = {}
	for i in range(len(values_list)):
		dict2[i] = values_list[i]
	values_list.sort()
	sorted_values_list = values_list
	unsorted_indexes = list(dict2.values())
	new_list = []
	for i in range(len(sorted_values_list)):
		key = None
		for k in dict2.keys():
			if dict2[k] == sorted_values_list[i]:
				key = k
				break
		new_list.append(keys_list[key])
		del dict2[key]
	final_dict = {}
	for i in range(len(new_list)):
		final_dict[new_list[i]] = sorted_values_list[i]
	return final_dict


print(sort_on_values_without_using_sorted(dicto))










