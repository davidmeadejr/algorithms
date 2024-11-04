"""
Pattern: Recursion

Explanation:
- Recursion is when a function calls itself.
- A recursive function has a base case and a recursive case
- I main value is in improving readability not necessarily performance  

"""
# Example
def countdown(i):
    if i <= 0: # Base case
        return i
    else: # Recursive case
        print(i)
        return countdown(i - 1)

print(countdown(10))
