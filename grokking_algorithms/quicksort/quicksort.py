"""
Pattern: Divide and Conquer + Recursion

Solution: Define a base case that returns the simplest instance of the problem to stop the recursion, and then implement the recursive case where the function calls itself with a modified argument to gradually approach the base case.

Time Complexity: Depends on the pivot used (see below)
- Worst Case: O(n^2) happens when the pivot consistently selects the smallest or largest elements, leading to unbalanced partitions.
- Average Case: O(n log n) occurs when the pivot splits the array into two approximately equal parts.

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