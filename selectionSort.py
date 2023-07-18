test_array= [69, 33, 13, 27, 9]

# Traverse through all array elements
for i in range(len(test_array)):
    # Find the minimum element in remaining
    # unsorted array
    min_index = i
    for j in range(i+1, len(test_array)):
        if test_array[min_index] > test_array[j]:
            min_idx = j
    # Swap the found minimum element with
    # the first element
    test_array[i], test_array[min_index] = test_array[min_index], test_array[i]

# Driver code to test
for i in range(len(test_array)):
    print("%d" % test_array[i], end=" , ")