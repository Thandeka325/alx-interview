#!/usr/bin/python3
"""
This module calculates the minimum operations to get exactly n H characters
using only Copy All and Paste operations.
"""


def minOperations(n: int) -> int:
    """
    Calculates the minimum number of operations needed to reach exactly n Hs.

    Parameters:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations needed, or 0 if impossible.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
