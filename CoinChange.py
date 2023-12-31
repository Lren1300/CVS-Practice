"""
    Coin Change Problem:
        Given a value N, if we want to make change for N cents,
        and we have an infinite supply of change C = {C1, C2, ... , Cm},
        how many ways can we make the change?
"""


def coin_change(c, n, s):
    """
        coin_change function: recursive function that gives the number of possible
        combinations of the sum to a certain number in a set of numbers.

        Args:
            c = set of ascending numbers that represent our coins
            n = number of coins in C
            s = number we wish the change to add up too

        Function influenced by GeeksForGeeks recursive tree explanation
        at https://www.geeksforgeeks.org/coin-change-dp-7/
    """

    # if the total becomes 0 it is a solution
    if s == 0:
        return 1

    # If total is less than 0 then the
    # solution does not exist (cant have negative coins)
    if s < 0:
        return 0

    # If there are no coins and total
    # is greater than 0, then no
    # solution exist
    if n <= 0:
        return 0

    # simulating a recursive tree
    # we explore the cases above by manipulating
    # our variables in two ways:
    # 1. Keeping the total value the same and decreasing
    #    the number of coins
    # 2. Keeping the same number of coins and decreasing the sum
    #    by the largest possible coin value
    # once all recursive calls are made, they all end up
    # at one of the 3 cases above.
    return coin_change(c, n - 1, s) + coin_change(c, n, s - c[n - 1])


# Driver program to test above function
given_coins = [2, 5, 3, 6]
n = len(given_coins)
s = 10
print(coin_change(given_coins, n, s))
