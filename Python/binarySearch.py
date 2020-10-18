# @author: Jorge Reyes

"""
The binary search algorithm works by splitting the array recursively. Keep in mind that this algorithm needs an already sorted array.
"""

def binarySearch(arr, n):
    # Base Case
    if (len(arr) == 1 and n != arr[0]):
        return False

    # Get the middle item of the array
    half = len(arr)//2

    # Check if the middle item is equal to 'n'
    if (arr[half] == n):
        return True
    else:
        # If 'n' is smaller than the number in the middle of the array, search the left part
        if (n < arr[half]):
            return binarySearch(arr[0:half], n)
        else:
            # If 'n' is greater than the number in the middle of the arrau, search the right part
            return binarySearch(arr[half:len(arr)], n)


# Example
arr = [293, 394, 598, 829, 4000]

print(binarySearch(arr, 293))
print(binarySearch(arr, 100))