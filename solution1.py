#!/usr/bin/env python3

def find_x(n, isTooSweet):
    """
    It finds the smallest x such that isTooSweet(x) is True

    :param n: the maximum value of x
    :param isTooSweet: a function that takes in a number and returns True if the number is too sweet, False otherwise
    :return: The number of cookies that can be made with the given ingredients.
    """
    l = 0
    r = n
    while l < r:
        mid = (l + r) // 2
        if isTooSweet(mid):
            r = mid
        else:
            l = mid + 1
    return l


