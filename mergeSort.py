def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        # Into 2 halves
        # this was a new python function I learned
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        # temp variables
        i = j = z = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[z] = L[i]
                i += 1
            else:
                arr[z] = R[j]
                j += 1
            z += 1
        # Checking if any element was left
        while i < len(L):
            arr[z] = L[i]
            i += 1
            z += 1
        while j < len(R):
            arr[z] = R[j]
            j += 1
            z += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Driver Code
if __name__ == '__main__':
    arr = [15, 10, 702, 77, 104, 435]
    print("Given array:")
    printList(arr)
    mergeSort(arr)
    print("Sorted array:")
    printList(arr)
