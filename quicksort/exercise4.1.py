# Write out the code for the earlier sum function

arr = [2, 4, 6]

def total_nums(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])


print(total_nums(arr))
