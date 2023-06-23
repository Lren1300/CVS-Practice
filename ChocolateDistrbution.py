"""
Chocolate distribution problem:
    Given an array of N integers where each value
    represents the number of chocolates in a packet.
    Each packet can have a variable number of
    chocolates. There are m students.

    The task is to distribute chocolate packets such
    that:
        -Each student gets one packet
        -The difference between the number of chocolates
        in the packet with maximum chocolates and the
        packet with minimum chocolates is minimum
"""

"""
choco_dist: function that contains the logic to solve the 
given problem

Args:
    -packets: given array of values of the 'packets of chocolate'
    -n: number of packets/size of the array
    -m: number of students
"""


def choco_dist(packets, n, s):
    # use the baked in sort() function to sort the packets in asc order
    packets.sort()

    # variable made to track the minimum difference throughout the loop
    # it is initialized to the maximum possible difference
    curr_diff = packets[n - 1] - packets[0]

    # variable made to keep track of current packets given
    # it is initialized to all 0's to begin
    curr_diff_arr = [0]*s

    # loop through the possible subsets within the array
    # these are subsets have a size of number of students
    for i in range(len(packets) - s + 1):

        # we set our variable to the minimum of the max and min
        # of the current subset and the current minimum distance
        curr_diff = min(curr_diff, packets[i + s - 1] - packets[i])

        # if there is a new minimum, we update the array that holds
        # the values of the packets that will be given
        if curr_diff == packets[i + s - 1] - packets[i]:
            for j in range(s):
                curr_diff_arr[j] = (packets[i + j])

    # once the loop is over, the minimum distance will be stored
    # and the problem is now complete
    print("The minimum difference is: " + str(curr_diff))
    print("The packets given were: " + str(curr_diff_arr))


# Driver code to test function
if __name__ == '__main__':
    packets = [8, 2, 3, 4, 9, 11, 18]
    s = 4
    n = len(packets)
    choco_dist(packets, n, s)
