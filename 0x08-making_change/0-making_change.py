#!/usr/bin/python3
"""Optimized change making module using efficient DP
"""


def makeChange(coins, total):
    """Returns the fewest number of coins needed to make up a given total.

    Args:
        coins (list): list of positive integers (coin values).
        total (int): target amount.

    Returns:
        int: Minimum number of coins to reach total, or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Filter and sort coins to reduce unnecessary processing
    coins = list(set(filter(lambda c: c <= total, coins)))
    if not coins:
        return -1

    # Initialize DP array
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
