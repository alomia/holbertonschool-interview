#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """

    minOper = 0
    div = 2
    while isinstance(n, int) and n > 1:
        while n % div:
            div += 1
        minOper += div
        n = int(n / div)
    return minOper
