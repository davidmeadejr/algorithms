"""
Pattern: Find Smallest Element

Solution: Use a loop to repeatedly find the smallest element in the array, remove it from the original array and append it to a new array until no elements remain. Return the new sorted array

Time Complexity: 0(n^2) also known as quadratic time.

Time Complexity Explanation: For each element you touch all elements again.
"""

# Find the smallest element in an array
def find_smallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

# Use the selection sort algorithm to sort an array in ascending order
def selection_sort(arr):
	new_arr = []
	for i in range(len(arr)):
		smallest = find_smallest(arr)
		new_arr.append(arr.pop(smallest))
	return new_arr

print(selection_sort([5, 3, 6, 2, 10]))

