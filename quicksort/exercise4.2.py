# Write a recursive function to count the number of items in a list

nums_list = [3, 7, 15, 6, 8, 19]

def item_nums(nums_list):
	if len(nums_list) == 0:
		return 0
	else:
		return 1 + item_nums(nums_list[1:])

print(item_nums(nums_list))	

