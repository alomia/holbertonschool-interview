#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
    """

    if type(n) is not int:
        return 0

    totalOperations = 0

    for i in range(2, n + 1):
        while n % i == 0:
            totalOperations += i
            n = n // i

    return totalOperations
