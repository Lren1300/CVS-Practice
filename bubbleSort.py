def bubbleSort(given_array):
    n = len(given_array)
    # Traverse through all array elements
    for i in range(n):
        is_swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if given_array[j] > given_array[j+1]:
                given_array[j], given_array[j+1] = given_array[j+1], given_array[j]
                is_swapped = True

        if not is_swapped:
            break


# Driver code to test
if __name__ == "__main__":
    given_array = [64, 34, 25, 12, 22, 11, 90]
    bubbleSort(given_array)
    for i in range(len(given_array)):
        print("%d" % given_array[i], end=" ")

