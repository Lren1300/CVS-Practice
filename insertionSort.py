def insertionSort(given_array):
    # Traverse through 1 to len(arr)
    for i in range(1, len(given_array)):
        key = given_array[i]

        # Move elements of given_array[0..i-1], that are
        # greater than key to one position ahead
        # of their current position
        j=i-1
        while j>=0 and key<given_array[j]:
            given_array[j+1] = given_array[j]
            j-=1
        given_array[j+1] = key


# Driver code to test above
given = [12, 11, 13, 5, 6]
insertionSort(given)
for i in range(len(given)):
    print("% d" % given[i], end= " ,")