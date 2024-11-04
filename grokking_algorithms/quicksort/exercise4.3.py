# Find the maximum number in a list.

nums_list = [3, 7, 15, 6, 8, 19]

def max_num(nums_list):
  if nums_list == []:
    return 0
  else:
    first_element = nums_list[0]
    max_in_rest = max_num(nums_list[1:])
    return max(first_element, max_in_rest)
    
print(max_num(nums_list))
