my_list = [1, 3, 5, 7, 9]

def binary_search(my_list, target):
  low = 0
  high = len(my_list) - 1

  while low <= high:
    mid = (low + high) // 2
    guess = my_list[mid]

    if guess == target:
      return mid
    elif guess > high:
      high = mid - 1
    else:
      low = mid + 1
  
  return -1

print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => -1