#!/usr/bin/python3
"""
This module provides a function to determine the fewest number of coins
needed to meet a given amount using available denominations.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to make change for.

    Returns:
        int: Fewest number of coins needed to meet total,
             or -1 if total cannot be met by any combination.
    """
    if total <= 0:
        return 0

    coins = sorted(set(coins))  # Remove duplicates & sort
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
