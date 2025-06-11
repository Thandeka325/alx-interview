#!/usr/bin/python3
"""Change making module using dynamic programming.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet total.
    Args:
        coins (list): coin denominations.
        total (int): total amount to make change for.
    Returns:
        int: fewest number of coins, or -1 if impossible.
    """
    if total <= 0:
        return 0

    # Initialize DP array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
