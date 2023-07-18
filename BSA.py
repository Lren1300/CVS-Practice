
def binarySearch(arr, left, right, x):
    while left <= right:
        mid = left + (right - left) // 2
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore left half
        elif arr[mid] < x:
            left = mid + 1
        # If x is smaller, ignore right half
        else:
            right = mid - 1
    # if x is not in the list, return -1
    return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 4, 5, 10, 26, 33, 44, 89, 100]
    x = 44

    # Function call
    result = binarySearch(arr, 0, len(arr) - 1, x)
    if result != -1:
        print("Element is at index", result)
    else:
        print("Element is not in array")