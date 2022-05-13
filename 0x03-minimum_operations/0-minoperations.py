#!/usr/bin/python3
"""
0x03. Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations
    needed to result in exactly n H characters in the file."""
    totalOperations = 0

    if n > 1:
        for i in range(2, n + 1):
            while n % i == 0:
                totalOperations += i
                n = n / i

    return totalOperations
