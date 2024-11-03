"""
Pattern: Divide and Conquer + Recursion

Solution:

Time Complexity: 

Time Complexity Explanation: 
"""

arr = [11, 23, 46, 57, 9, 14, 233, 6, 4, 35]

def quicksort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    more = [i for i in arr[1:] if i > pivot]

  return quicksort(less) + [pivot] + quicksort(more)

print(quicksort(arr))


