"""
Pattern: Divide and Conquer

Solution: Use a "while loop" to repeatedly divide the search space in half, comparing the middle element with the target value. Adjust the search space (low/high bounds) based on whether the target is greater or less than the middle element.

Time Complexity: 0(log n) also known as log time

Time Complexity Explanation: If each iteration divides the input size in half (e.g., from n to n/2 to n/4...), the time complexity is likely O(log n). The number of required operations grows logarithmically, not linearly, with the input size.
"""

my_list = [1, 3, 5, 7, 9]
def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(my_list, 3)) # => 1
print(binary_search(my_list, -1)) # => None